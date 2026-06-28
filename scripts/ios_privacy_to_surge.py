#!/usr/bin/env python3
"""
iOS 隐私报告 → Surge/Loon 分流规则生成器

用法:
  python3 ios_privacy_to_surge.py privacy_report.ndjson
  python3 ios_privacy_to_surge.py report.ndjson -o Rule/MyApp.list
  python3 ios_privacy_to_surge.py report.ndjson --format loon --suffix-threshold 5
  python3 ios_privacy_to_surge.py report.ndjson --no-itunes --output-single SocialMedia.list

输入: iOS 设置 → 隐私 → App 隐私报告 → 存储 App 活动 → 导出 .ndjson
输出: Surge 或 Loon 格式的分流规则
"""

import argparse
import ipaddress
import json
import os
import re
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

# ── 常量 ──────────────────────────────────────────────────────

# 系统/代理工具产生的假 IP（私有 + 链路本地 + 多播 + 已知代理伪造地址）
FAKE_IP_PATTERNS = [
    # RFC 1918 私有地址
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    # 回环
    ipaddress.ip_network("127.0.0.0/8"),
    # 链路本地
    ipaddress.ip_network("169.254.0.0/16"),
    # 多播
    ipaddress.ip_network("224.0.0.0/4"),
    # DNS 特例
    ipaddress.ip_network("0.0.0.0/8"),
    ipaddress.ip_network("17.0.0.0/8"),  # Apple 内部
    # IPv6
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fe80::/10"),
    ipaddress.ip_network("fc00::/7"),
    ipaddress.ip_network("ff00::/8"),
    ipaddress.ip_network("::ffff:0:0/96"),  # IPv4-mapped
]

# 默认排除的系统 Bundle ID 前缀
SYSTEM_BUNDLE_PREFIXES = [
    "com.apple.springboard",
    "com.apple.analyticsd",
    "com.apple.locationd",
    "com.apple.assistantd",
    "com.apple.WebKit.Networking",
    "com.apple.cloudd",
    "com.apple.duetactivityscheduler",
    "com.apple.nsurlsessiond",
    "com.apple.remindd",
    "com.apple.assistant-services",
    "com.apple.CoreRoutine",
    "com.apple.photos.ImageConversionService",
    "com.apple.commcenter",
    "com.apple.siri",
    "com.apple.searchd",
    "com.apple.suggestd",
]

# iTunes API
ITUNES_LOOKUP_URL = "https://itunes.apple.com/lookup"
ITUNES_CACHE_TTL = 86400  # 24h

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MAPPING_PATH = SCRIPT_DIR / "app_mapping.json"


# ── 工具函数 ──────────────────────────────────────────────────

def load_mapping(path: Path) -> dict:
    """加载 Bundle ID → 应用信息映射表"""
    if not path.exists():
        print(f"⚠ 映射文件不存在: {path}，将仅使用 iTunes API", file=sys.stderr)
        return {}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if not k.startswith("_")}


def is_fake_ip(ip_str: str) -> bool:
    """判断 IP 是否为代理工具产生的假 IP"""
    try:
        addr = ipaddress.ip_address(ip_str.strip())
    except ValueError:
        return True  # 无效 IP 直接丢弃
    for net in FAKE_IP_PATTERNS:
        if addr in net:
            return True
    return False


def is_system_bundle(bundle_id: str, mapping: dict) -> bool:
    """判断是否为系统 Bundle ID"""
    for prefix in SYSTEM_BUNDLE_PREFIXES:
        if bundle_id == prefix or bundle_id.startswith(prefix + "."):
            return True
    # 也检查映射表中的 is_system 标记
    entry = mapping.get(bundle_id, {})
    return entry.get("is_system", False)


def suffix_from_domain(domain: str) -> str:
    """提取域名的可注册后缀 + 一级（e.g. a.b.example.com → example.com）"""
    # 移除末尾点
    domain = domain.rstrip(".")
    parts = domain.split(".")
    if len(parts) <= 2:
        return domain
    # 公共后缀启发式：保留后 2~3 段（com.cn → 3, com → 2）
    # 使用简单启发式而非完整 PSL 库
    tld = parts[-1]
    sld = parts[-2] if len(parts) >= 2 else ""
    # 中国常见双后缀
    if sld in ("com", "net", "org", "gov", "edu", "co", "ac") and tld in ("cn", "hk", "tw", "jp", "kr", "uk", "au", "sg", "my"):
        if len(parts) >= 3:
            return ".".join(parts[-3:])
    # 国际双后缀
    if sld in ("co", "com", "net", "org", "gov", "edu", "ac") and tld in ("uk", "jp", "kr", "au", "nz", "br", "za", "in", "th"):
        if len(parts) >= 3:
            return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def query_itunes(bundle_id: str, cache: dict) -> str | None:
    """通过 iTunes API 查询应用名称（带缓存）"""
    if bundle_id in cache:
        entry = cache[bundle_id]
        if time.time() - entry["ts"] < ITUNES_CACHE_TTL:
            return entry["name"]
    try:
        url = f"{ITUNES_LOOKUP_URL}?bundleId={bundle_id}&country=cn&limit=1"
        req = urllib.request.Request(url, headers={"User-Agent": "privacy2surge/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
        if data.get("resultCount", 0) > 0:
            name = data["results"][0].get("trackName") or data["results"][0].get("trackCensoredName")
            if name:
                cache[bundle_id] = {"name": name, "ts": time.time()}
                return name
    except Exception:
        pass
    cache[bundle_id] = {"name": None, "ts": time.time()}
    return None


def get_app_name(bundle_id: str, mapping: dict, itunes_cache: dict, use_itunes: bool) -> str:
    """获取应用显示名称：映射表 > iTunes > bundle_id"""
    entry = mapping.get(bundle_id, {})
    if entry.get("name"):
        return entry["name"]
    if use_itunes:
        name = query_itunes(bundle_id, itunes_cache)
        if name:
            return name
    # 回退：从 bundle_id 取最后一段
    return bundle_id.split(".")[-1]


# ── 核心处理 ──────────────────────────────────────────────────

def process_ndjson(
    path: str,
    mapping: dict,
    suffix_threshold: int,
    use_itunes: bool,
    format_type: str,
) -> tuple[dict, dict, dict]:
    """
    处理 NDJSON 文件，返回:
      app_rules: {app_name: {domains: set, ips: set, ips_v6: set}}
      unknown_domains: {domain: set of bundle_ids}
      stats: 统计信息
    """
    app_raw = defaultdict(lambda: {"domains": set(), "ips": set(), "ips_v6": set()})
    unknown_domains = defaultdict(set)
    itunes_cache = {}
    stats = {
        "total_lines": 0,
        "app_initiated": 0,
        "system_filtered": 0,
        "fake_ip_filtered": 0,
        "valid_entries": 0,
    }

    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            stats["total_lines"] += 1

            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue

            # 字段可以是驼峰或下划线
            initiated = record.get("initiatedType") or record.get("initiated_type") or ""
            bundle_id = record.get("bundleID") or record.get("bundle_id") or ""
            domain = record.get("domain") or ""

            if not domain:
                continue

            # 过滤：只保留 AppInitiated
            if initiated != "AppInitiated":
                continue
            stats["app_initiated"] += 1

            # 过滤：系统应用
            if is_system_bundle(bundle_id, mapping):
                stats["system_filtered"] += 1
                continue

            # IP 还是域名？
            domain_clean = domain.strip().rstrip(".")
            if not domain_clean:
                continue

            # 判断是否 IP
            try:
                ip_addr = ipaddress.ip_address(domain_clean)
                if is_fake_ip(domain_clean):
                    stats["fake_ip_filtered"] += 1
                    continue
                if ip_addr.version == 6:
                    app_raw[bundle_id]["ips_v6"].add(domain_clean)
                else:
                    app_raw[bundle_id]["ips"].add(domain_clean)
                stats["valid_entries"] += 1
                continue
            except ValueError:
                pass  # 不是 IP，是域名

            # 域名处理
            if is_domain_valid(domain_clean):
                app_raw[bundle_id]["domains"].add(domain_clean.lower())
                stats["valid_entries"] += 1

    # 识别应用名称并合并 IP 到预定义 CIDR
    app_rules = {}
    for bundle_id, raw in app_raw.items():
        app_name = get_app_name(bundle_id, mapping, itunes_cache, use_itunes)

        # 应用预定义域名和 IP
        entry = mapping.get(bundle_id, {})
        known_domains = set(entry.get("domains", []))
        known_ips = set(entry.get("ips", []))
        known_ips_v6 = set(entry.get("ips_v6", []))

        # 子域合并: 从报告域名中提取
        exact_domains, suffix_domains = merge_subdomains(raw["domains"], suffix_threshold)

        # IP 分类：预定义 CIDR vs 裸 IP
        def _split_cidr_raw(ips: set) -> tuple[set, set]:
            cidr, raw_ip = set(), set()
            for ip in ips:
                ip = ip.strip()
                if "/" in ip:
                    cidr.add(ip)
                else:
                    raw_ip.add(ip)
            return cidr, raw_ip

        known_cidr, _ = _split_cidr_raw(known_ips)
        _, new_raw_ips = _split_cidr_raw(raw["ips"])
        known_cidr_v6, _ = _split_cidr_raw(known_ips_v6)
        _, new_raw_ips_v6 = _split_cidr_raw(raw["ips_v6"])

        # 合并已知 + 新发现的
        all_exact = known_domains | exact_domains
        all_suffixes = suffix_domains  # 已知域名不参与 suffix 合并
        all_cidr = known_cidr
        all_raw_ips = new_raw_ips
        all_cidr_v6 = known_cidr_v6
        all_raw_ips_v6 = new_raw_ips_v6

        if app_name not in app_rules:
            app_rules[app_name] = {
                "domains": set(), "suffixes": set(),
                "cidr_ips": set(), "raw_ips": set(),
                "cidr_ips_v6": set(), "raw_ips_v6": set(),
                "bundle_ids": set(),
            }

        app_rules[app_name]["domains"] |= all_exact
        app_rules[app_name]["suffixes"] |= all_suffixes
        app_rules[app_name]["cidr_ips"] |= all_cidr
        app_rules[app_name]["raw_ips"] |= all_raw_ips
        app_rules[app_name]["cidr_ips_v6"] |= all_cidr_v6
        app_rules[app_name]["raw_ips_v6"] |= all_raw_ips_v6
        app_rules[app_name]["bundle_ids"].add(bundle_id)

    # 跨应用域名去重 + 冲突检测
    app_rules = deduplicate_cross_app(app_rules)

    return app_rules, unknown_domains, stats


def is_domain_valid(domain: str) -> bool:
    """基本域名合法性检查"""
    domain = domain.rstrip(".")
    if not domain or len(domain) > 253:
        return False
    # 必须有点
    if "." not in domain:
        return False
    # 排除纯数字 TLD
    parts = domain.split(".")
    if parts[-1].isdigit():
        return False
    # 每个段检查
    for part in parts:
        if not part or len(part) > 63:
            return False
    return True


def merge_subdomains(domains: set, threshold: int) -> tuple[set, set]:
    """
    子域合并算法:
    - 统计每个父域名的子域数量
    - 子域 ≥ threshold → 合并为一个 DOMAIN-SUFFIX
    - 否则保留各子域为 DOMAIN
    返回: (domain_set, suffix_set)
    """
    if threshold <= 0:
        return domains.copy(), set()

    suffix_count = defaultdict(set)
    for d in domains:
        parent = suffix_from_domain(d)
        suffix_count[parent].add(d)

    exact_set = set()
    suffix_set = set()
    for parent, children in suffix_count.items():
        if len(children) >= threshold:
            suffix_set.add(parent)
        else:
            exact_set |= children
    return exact_set, suffix_set


def deduplicate_cross_app(app_rules: dict) -> dict:
    """
    跨应用去重:
    - DOMAIN 和 DOMAIN-SUFFIX 分别检查
    - 同一个域名/suffix 出现在多个应用中 → 保留到第一个、其他移除
    """
    for field in ("domains", "suffixes"):
        seen = {}
        conflicts = []
        for app_name, rules in app_rules.items():
            to_remove = set()
            for val in rules[field]:
                if val in seen:
                    conflicts.append((val, seen[val], app_name))
                    to_remove.add(val)
                else:
                    seen[val] = app_name
            rules[field] -= to_remove
        if conflicts:
            tag = "DOMAIN-SUFFIX" if field == "suffixes" else "DOMAIN"
            print(f"\n⚠ 跨应用 {tag} 冲突 (first-match，保留前者):", file=sys.stderr)
            for val, keep, rem in conflicts[:20]:
                print(f"  {val}: 保留 {keep}，跳过 {rem}", file=sys.stderr)
            if len(conflicts) > 20:
                print(f"  ... 还有 {len(conflicts) - 20} 条", file=sys.stderr)
    return app_rules


# ── 输出 ──────────────────────────────────────────────────────

def _rule_count(rules: dict) -> int:
    return (
        len(rules["domains"]) + len(rules["suffixes"])
        + len(rules["cidr_ips"]) + len(rules["raw_ips"])
        + len(rules["cidr_ips_v6"]) + len(rules["raw_ips_v6"])
    )


def format_surge(app_rules: dict, stats: dict) -> str:
    """输出 Surge 规则格式"""
    lines = []
    lines.append(f"# Surge 分流规则 - 由 iOS 隐私报告生成")
    lines.append(f"# 生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"# 解析记录: {stats['total_lines']} | AppInitiated: {stats['app_initiated']} | 有效: {stats['valid_entries']}")
    lines.append(f"# 应用数: {len(app_rules)}")
    lines.append("")

    for app_name in sorted(app_rules.keys()):
        rules = app_rules[app_name]
        total = _rule_count(rules)
        if total == 0:
            continue

        bundle_str = ", ".join(sorted(rules["bundle_ids"]))
        lines.append(f"# {'=' * 30}")
        lines.append(f"# {app_name}  ({bundle_str})")
        lines.append(f"# {'=' * 30}")

        # DOMAIN-SUFFIX: 子域合并后的父域名
        for domain in sorted(rules["suffixes"]):
            lines.append(f"DOMAIN-SUFFIX,{domain}")

        # DOMAIN: 精确域名
        for domain in sorted(rules["domains"]):
            lines.append(f"DOMAIN,{domain}")

        # IP-CIDR: 预定义 CIDR
        for ip in sorted(rules["cidr_ips"]):
            lines.append(f"IP-CIDR,{ip},no-resolve")

        # IP-CIDR: 裸 IPv4 → /32
        for ip in sorted(rules["raw_ips"]):
            lines.append(f"IP-CIDR,{ip}/32,no-resolve")

        # IP-CIDR6: 预定义 IPv6 CIDR
        for ipv6 in sorted(rules["cidr_ips_v6"]):
            lines.append(f"IP-CIDR6,{ipv6},no-resolve")

        # IP-CIDR6: 裸 IPv6 → /128
        for ipv6 in sorted(rules["raw_ips_v6"]):
            lines.append(f"IP-CIDR6,{ipv6}/128,no-resolve")

        lines.append("")

    total = sum(_rule_count(r) for r in app_rules.values())
    lines.append(f"# TOTAL: {total}")
    return "\n".join(lines)


def format_loon(app_rules: dict, stats: dict) -> str:
    """输出 Loon 规则格式"""
    lines = []
    lines.append(f"# Loon 分流规则 - 由 iOS 隐私报告生成")
    lines.append(f"# UpdateTime: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"# 解析记录: {stats['total_lines']} | AppInitiated: {stats['app_initiated']} | 有效: {stats['valid_entries']}")
    lines.append(f"# 应用数: {len(app_rules)}")
    lines.append("")

    for app_name in sorted(app_rules.keys()):
        rules = app_rules[app_name]
        total = _rule_count(rules)
        if total == 0:
            continue

        bundle_str = ", ".join(sorted(rules["bundle_ids"]))
        lines.append(f"# {'=' * 30}")
        lines.append(f"# {app_name}  ({bundle_str})")
        lines.append(f"# {'=' * 30}")

        for domain in sorted(rules["suffixes"]):
            lines.append(f"DOMAIN-SUFFIX,{domain}")
        for domain in sorted(rules["domains"]):
            lines.append(f"DOMAIN-SUFFIX,{domain}")  # Loon 统一用 DOMAIN-SUFFIX
        for ip in sorted(rules["cidr_ips"]):
            lines.append(f"IP-CIDR,{ip},no-resolve")
        for ip in sorted(rules["raw_ips"]):
            lines.append(f"IP-CIDR,{ip}/32,no-resolve")
        for ipv6 in sorted(rules["cidr_ips_v6"]):
            lines.append(f"IP-CIDR6,{ipv6},no-resolve")
        for ipv6 in sorted(rules["raw_ips_v6"]):
            lines.append(f"IP-CIDR6,{ipv6}/128,no-resolve")

        lines.append("")

    total = sum(_rule_count(r) for r in app_rules.values())
    lines.append(f"# RuleCount: {total}")
    return "\n".join(lines)


# ── 入口 ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="iOS 隐私报告 → Surge/Loon 分流规则生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s privacy_report.ndjson
  %(prog)s report.ndjson -o Rule/App.list
  %(prog)s report.ndjson --format loon --suffix-threshold 5
  %(prog)s report.ndjson --no-itunes --mapping my_apps.json
        """,
    )
    parser.add_argument("input", help="iOS 隐私报告 .ndjson 文件路径")
    parser.add_argument("-o", "--output", default="-", help="输出文件路径 (默认: stdout)")
    parser.add_argument("--format", choices=["surge", "loon"], default="surge", help="输出格式 (默认: surge)")
    parser.add_argument(
        "--suffix-threshold",
        type=int,
        default=3,
        help="子域合并阈值：同一父域名的子域 >= N 条时才合并为 DOMAIN-SUFFIX (默认: 3, 0=不合并)",
    )
    parser.add_argument("--no-itunes", action="store_true", help="不查询 iTunes API 获取应用名称")
    parser.add_argument("--mapping", default=str(DEFAULT_MAPPING_PATH), help="自定义映射表路径")
    args = parser.parse_args()

    # 检查输入文件
    if not os.path.isfile(args.input):
        print(f"错误: 找不到文件 {args.input}", file=sys.stderr)
        sys.exit(1)

    # 加载映射表
    mapping_path = Path(args.mapping)
    mapping = load_mapping(mapping_path)
    print(f"📋 加载映射表: {len(mapping)} 个应用", file=sys.stderr)

    # 处理
    print(f"📖 解析中: {args.input}", file=sys.stderr)
    app_rules, unknown_domains, stats = process_ndjson(
        args.input, mapping, args.suffix_threshold, not args.no_itunes, args.format
    )

    # 输出
    if args.format == "loon":
        output = format_loon(app_rules, stats)
    else:
        output = format_surge(app_rules, stats)

    if args.output == "-":
        print(output)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"✅ 已输出: {args.output}", file=sys.stderr)

    # 统计摘要
    total_rules = sum(_rule_count(r) for r in app_rules.values())
    print(f"\n📊 统计:", file=sys.stderr)
    print(f"  记录总数: {stats['total_lines']}", file=sys.stderr)
    print(f"  应用发起: {stats['app_initiated']}", file=sys.stderr)
    print(f"  系统过滤: {stats['system_filtered']}", file=sys.stderr)
    print(f"  假 IP 过滤: {stats['fake_ip_filtered']}", file=sys.stderr)
    print(f"  有效条目: {stats['valid_entries']}", file=sys.stderr)
    print(f"  应用数量: {len(app_rules)}", file=sys.stderr)
    print(f"  输出规则: {total_rules}", file=sys.stderr)


if __name__ == "__main__":
    main()
