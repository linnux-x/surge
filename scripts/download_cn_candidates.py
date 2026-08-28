#!/usr/bin/env python3
"""审计 Surge TrafficStatistics CSV 中的国内下载候选，绝不自动改规则。

该工具只分析当前 first-match 命中 ``Download.list`` 的域名：

    python3 scripts/download_cn_candidates.py TrafficStatistics.csv \
      --resolve -o /tmp/download-cn-candidates.json

输出只能是 JSON / CSV 审计材料，不能写入 Rule/ 或生成任何 DIRECT 规则。DNS
解析与 China_IP.list 命中仅是“候选信号”，不是地域、服务归属或下载用途的证明。
每个 ``REVIEW_REQUIRED`` 项仍须具备官方所有权/区域文档和路由回归测试，才能被
人工加入受治理的 Download_CN.list（若未来创建）。
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import ipaddress
import json
import socket
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
CHINA_IP_RULES = RULE_DIR / "China_IP.list"
ROUTING_SCRIPT = ROOT / "scripts" / "test_routing_order.py"

# TrafficStatistics exports differ slightly between Surge versions/locales.
# Host is mandatory; counters are optional and default to zero when absent.
FIELD_ALIASES = {
    "host": ("host", "domain", "hostname"),
    "request_count": ("requestcount", "request_count", "requests", "count"),
    "upload": ("upload", "uploadbytes", "upload_bytes"),
    "download": ("download", "downloadbytes", "download_bytes"),
}

# Public CDN/cloud/telemetry parents cannot be promoted from a DNS observation.
# This is intentionally conservative: unknown hosts remain candidates, not rules.
BLOCKED_PARENT_SUFFIXES = {
    "akadns.net", "akamaiedge.net", "akamaihd.net", "akamaized.net",
    "amazonaws.com", "azure.com", "azureedge.net", "b-cdn.net",
    "cloudflare.net", "cloudflarestorage.com", "cloudfront.net",
    "edgekey.net", "edgesuite.net", "fastly.net", "googleapis.com",
    "myqcloud.com", "aliyuncs.com", "blob.core.windows.net",
    "file.core.windows.net", "r2.dev", "sentry.io", "segment.io",
}


@dataclass(frozen=True)
class TrafficRow:
    host: str
    request_count: int
    upload: int
    download: int


@dataclass(frozen=True)
class Candidate:
    host: str
    request_count: int
    upload: int
    download: int
    total_bytes: int
    current_route: str
    cn_ip_signal: str
    resolved_ips: list[str]
    disposition: str
    reason: str
    proposed_rule: str | None


def normalize_header(value: str | None) -> str:
    return "".join(ch for ch in (value or "").lower() if ch.isalnum())


def parse_number(value: str | None) -> int:
    """Parse decimal counters defensively; blank/malformed values are zero."""
    raw = (value or "").strip().replace(",", "")
    if not raw:
        return 0
    try:
        number = int(float(raw))
    except ValueError:
        return 0
    return max(number, 0)


def is_domain(host: str) -> bool:
    if not host or len(host) > 253 or ".." in host:
        return False
    try:
        ipaddress.ip_address(host)
    except ValueError:
        pass
    else:
        return False
    labels = host.split(".")
    return len(labels) >= 2 and all(
        label and len(label) <= 63 and label[0].isalnum() and label[-1].isalnum()
        and all(ch.isalnum() or ch == "-" for ch in label)
        for label in labels
    )


def parse_traffic_csv(path: Path) -> list[TrafficRow]:
    """Load and aggregate valid host rows from a Surge TrafficStatistics CSV."""
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV 缺少表头")
        by_normalized = {normalize_header(name): name for name in reader.fieldnames}
        columns: dict[str, str | None] = {}
        for semantic, aliases in FIELD_ALIASES.items():
            columns[semantic] = next((by_normalized.get(alias) for alias in aliases if alias in by_normalized), None)
        if not columns["host"]:
            raise ValueError("CSV 缺少 Host / Domain / Hostname 列")

        totals: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
        for row in reader:
            host = (row.get(columns["host"] or "") or "").strip().lower().rstrip(".")
            if not is_domain(host):
                continue
            values = totals[host]
            values[0] += parse_number(row.get(columns["request_count"] or ""))
            values[1] += parse_number(row.get(columns["upload"] or ""))
            values[2] += parse_number(row.get(columns["download"] or ""))

    return [
        TrafficRow(host, values[0], values[1], values[2])
        for host, values in sorted(totals.items())
    ]


def load_china_networks(path: Path = CHINA_IP_RULES) -> list[ipaddress._BaseNetwork]:
    """Load only valid IP-CIDR/IP-CIDR6 entries from the generated China IP list."""
    networks: list[ipaddress._BaseNetwork] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        parts = [part.strip() for part in raw.split(",")]
        if len(parts) < 2 or parts[0] not in {"IP-CIDR", "IP-CIDR6"}:
            continue
        try:
            networks.append(ipaddress.ip_network(parts[1], strict=False))
        except ValueError:
            continue
    if not networks:
        raise ValueError(f"未从 {path} 读取到 China IP CIDR")
    return networks


def resolve_host(host: str) -> list[str]:
    """Resolve A/AAAA records using the local resolver; failures yield no signal."""
    try:
        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)
    except socket.gaierror:
        return []
    return sorted({str(answer[4][0]) for answer in answers})


def cn_ip_signal(ips: Iterable[str], networks: list[ipaddress._BaseNetwork]) -> str:
    """Classify observed IPs only; this deliberately does not claim CDN geography."""
    addresses: list[ipaddress._BaseAddress] = []
    for raw in ips:
        try:
            addresses.append(ipaddress.ip_address(raw))
        except ValueError:
            continue
    if not addresses:
        return "UNRESOLVED"
    matches = [any(address in network for network in networks) for address in addresses]
    if all(matches):
        return "ALL_CN_IP"
    if any(matches):
        return "MIXED_IP"
    return "NO_CN_IP"


def has_blocked_parent(host: str) -> bool:
    return any(host == suffix or host.endswith("." + suffix) for suffix in BLOCKED_PARENT_SUFFIXES)


def load_routing_module():
    spec = importlib.util.spec_from_file_location("routing_order", ROUTING_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载路由模拟器: {ROUTING_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_current_rules():
    module = load_routing_module()
    rulesets = {
        list_file.name: module.load_ruleset(list_file)
        for list_file in sorted(RULE_DIR.glob("*.list"))
    }
    return module, module.load_routing_order(), rulesets


def build_candidates(
    rows: Iterable[TrafficRow],
    routing_module,
    routing_order,
    rulesets: dict[str, set[str]],
    networks: list[ipaddress._BaseNetwork],
    resolve: bool,
    resolver: Callable[[str], list[str]] = resolve_host,
) -> list[Candidate]:
    """Return review-only candidates ordered by observed traffic volume."""
    candidates: list[Candidate] = []
    for row in rows:
        route = routing_module.simulate_routing(row.host, routing_order, rulesets)
        if not route.startswith("Download.list→"):
            continue

        ips = resolver(row.host) if resolve else []
        signal = cn_ip_signal(ips, networks) if resolve else "NOT_RESOLVED"
        if has_blocked_parent(row.host):
            disposition = "REJECT_SHARED_INFRA"
            reason = "命中公共 CDN、对象存储或遥测父域；DNS 结果不能证明大陆下载归属"
            proposed_rule = None
        elif signal == "ALL_CN_IP":
            disposition = "REVIEW_REQUIRED"
            reason = "当前本地 DNS 的全部结果位于 China_IP.list；仍需官方所有权/大陆区域证据和路由测试"
            proposed_rule = f"DOMAIN,{row.host}"
        elif signal == "MIXED_IP":
            disposition = "REJECT_MIXED_IP"
            reason = "同时解析到中国与非中国 IP，不能以单一域名固定为 DIRECT"
            proposed_rule = None
        elif signal == "NO_CN_IP":
            disposition = "REJECT_NON_CN_IP"
            reason = "当前本地 DNS 未解析到 China_IP.list；保持国际下载代理"
            proposed_rule = None
        elif signal == "UNRESOLVED":
            disposition = "REVIEW_REQUIRED"
            reason = "DNS 无结果；仅凭流量与下载规则不能判断地区，需补充官方证据"
            proposed_rule = f"DOMAIN,{row.host}"
        else:
            disposition = "REVIEW_REQUIRED"
            reason = "未执行 DNS 解析；需要补充官方区域证据和本地 DNS 观测"
            proposed_rule = f"DOMAIN,{row.host}"

        candidates.append(Candidate(
            host=row.host,
            request_count=row.request_count,
            upload=row.upload,
            download=row.download,
            total_bytes=row.upload + row.download,
            current_route=route,
            cn_ip_signal=signal,
            resolved_ips=ips,
            disposition=disposition,
            reason=reason,
            proposed_rule=proposed_rule,
        ))
    return sorted(candidates, key=lambda item: (-item.total_bytes, item.host))


def render_csv(candidates: list[Candidate]) -> str:
    from io import StringIO

    output = StringIO()
    fields = list(Candidate.__dataclass_fields__)
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    for candidate in candidates:
        item = asdict(candidate)
        item["resolved_ips"] = ";".join(item["resolved_ips"])
        writer.writerow(item)
    return output.getvalue()


def validate_output_path(path: Path) -> None:
    resolved = path.resolve()
    if RULE_DIR.resolve() in resolved.parents or resolved.suffix.lower() == ".list":
        raise ValueError("候选报告不得写入 Rule/，也不得输出 .list；该工具不生成生效规则")
    if resolved.suffix.lower() not in {".json", ".csv"}:
        raise ValueError("输出文件必须使用 .json 或 .csv")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="审计 TrafficStatistics 中的国内下载候选（只读，不生成规则）")
    parser.add_argument("traffic_csv", type=Path, help="Surge TrafficStatistics CSV 导出文件")
    parser.add_argument("-o", "--output", type=Path, required=True, help="输出 .json 或 .csv 审计报告")
    parser.add_argument("--resolve", action="store_true", help="通过当前本地 DNS 解析候选；结果仅为辅助信号")
    args = parser.parse_args(argv)

    try:
        validate_output_path(args.output)
        rows = parse_traffic_csv(args.traffic_csv)
        routing_module, routing_order, rulesets = load_current_rules()
        candidates = build_candidates(
            rows, routing_module, routing_order, rulesets, load_china_networks(), args.resolve,
        )
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    report = {
        "schema_version": 1,
        "mode": "review_only",
        "dns_resolution": args.resolve,
        "input_rows": len(rows),
        "download_route_candidates": len(candidates),
        "direct_rules_written": 0,
        "notice": (
            "此报告不构成地区或所有权证明。REVIEW_REQUIRED 必须补充官方证据、"
            "排除共享基础设施，并新增 first-match 路由测试后才能人工加入规则。"
        ),
        "candidates": [asdict(candidate) for candidate in candidates],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() == ".json":
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        args.output.write_text(render_csv(candidates), encoding="utf-8")

    review_count = sum(item.disposition == "REVIEW_REQUIRED" for item in candidates)
    print(f"已聚合 {len(rows)} 个有效主机；当前 Download.list 命中 {len(candidates)} 个")
    print(f"需人工复核 {review_count} 个；未写入任何 DIRECT 规则")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
