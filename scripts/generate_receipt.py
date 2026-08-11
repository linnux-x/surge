#!/usr/bin/env python3
"""Generate deterministic public rule-generation receipts from existing artifacts."""
from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANIFEST_DIR = RULE_DIR / ".manifests"
OUT_JSON = ROOT / "scripts" / "generation_receipt.json"
OUT_MD = ROOT / "scripts" / "generation_receipt.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_time() -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cI"], cwd=ROOT,
        capture_output=True, text=True, check=False,
    )
    return result.stdout.strip() or "unknown"


def active_rules(path: Path) -> list[str]:
    return [
        line.strip() for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def source_attribution() -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in sorted(MANIFEST_DIR.glob("*.manifest")):
        for line in path.read_text(encoding="utf-8").splitlines():
            parts = line.split("\t", 1)
            if len(parts) == 2:
                counts[parts[1]] += 1
    return counts


def main() -> int:
    from generate_clash_rules import CLASH_UNSUPPORTED_TYPES, MIHOMO_ONLY_OR_COMPAT_TYPES

    files: list[dict] = []
    rule_types: Counter[str] = Counter()
    unsupported: Counter[str] = Counter()
    compatibility: Counter[str] = Counter()
    total_rules = 0
    for path in sorted(RULE_DIR.glob("*.list")):
        rules = active_rules(path)
        types = Counter(rule.split(",", 1)[0] for rule in rules)
        rule_types.update(types)
        total_rules += len(rules)
        unsupported.update({name: count for name, count in types.items() if name in CLASH_UNSUPPORTED_TYPES})
        compatibility.update({name: count for name, count in types.items() if name in MIHOMO_ONLY_OR_COMPAT_TYPES})
        files.append({
            "file": path.name,
            "rules": len(rules),
            "types": dict(sorted(types.items())),
            "sha256": sha256(path),
        })

    diff_path = ROOT / "scripts" / "diff_report.json"
    diff = json.loads(diff_path.read_text(encoding="utf-8")) if diff_path.exists() else {}
    manifests = sorted(MANIFEST_DIR.glob("*.manifest"))
    dropped = sum(unsupported.values())
    data = {
        "schema_version": 1,
        "baseline_commit_time": git_time(),
        "rule_files": files,
        "total_rules": total_rules,
        "rule_types": dict(sorted(rule_types.items())),
        "source_attribution": dict(sorted(source_attribution().items())),
        "manifest_files": len(manifests),
        "manifests_sha256": {path.name: sha256(path) for path in manifests},
        "sources_sha256": sha256(ROOT / "scripts" / "sources.py"),
        "override_manifest_sha256": sha256(RULE_DIR / "Manual" / "override-manifest.json"),
        "clash_compatibility": {
            "payload_rules": total_rules - dropped,
            "dropped_surge_only_types": dict(sorted(unsupported.items())),
            "preserved_mihomo_extended_types": dict(sorted(compatibility.items())),
        },
        "diff_summary": {key: diff.get(key, 0) for key in (
            "total_added", "total_removed", "total_source_changed",
        )},
    }
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Surge 规则生成收据", "",
        f"- 基线提交时间：{data['baseline_commit_time']}",
        f"- 规则文件：{len(files)}", f"- 规则总数：{total_rules}",
        f"- manifest 文件：{len(manifests)}", "", "## 差异摘要", "",
        f"- 新增：{data['diff_summary']['total_added']}",
        f"- 删除：{data['diff_summary']['total_removed']}",
        f"- 来源迁移：{data['diff_summary']['total_source_changed']}", "", "## Clash 兼容性", "",
        f"- 生成 payload：{total_rules - dropped}",
        f"- 跳过 Surge 专属规则：{dict(sorted(unsupported.items()))}",
        f"- 保留 mihomo 扩展类型：{dict(sorted(compatibility.items()))}", "", "## 规则类型", "",
    ]
    lines.extend(f"- {name}: {count}" for name, count in data["rule_types"].items())
    lines.extend(["", "## 来源归属", ""])
    lines.extend(f"- {name}: {count}" for name, count in data["source_attribution"].items())
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[PASS] generation receipt: {len(files)} files, {total_rules} rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
