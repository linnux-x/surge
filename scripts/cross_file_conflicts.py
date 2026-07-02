#!/usr/bin/env python3
"""Report cross-file domain conflicts for Surge rulesets.

Monthly review helper: find the same domain value appearing in multiple .list
files whose policies differ in Conf/Linnux.conf first-match order.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
CONF_FILE = ROOT / "Conf" / "Linnux.conf"

TRACKED_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-WILDCARD"}
HIGH_RISK_FILES = {
    "Global.list", "China.list", "Apple_CN.list", "AI.list",
    "GlobalMedia.list", "ChinaMedia.list", "Download.list", "Microsoft.list",
}


def load_policy_order() -> dict[str, tuple[int, str]]:
    """Map ruleset filename to (order index, policy) from Conf/Linnux.conf."""
    mapping: dict[str, tuple[int, str]] = {}
    if not CONF_FILE.exists():
        return mapping

    in_rule = False
    order_index = 0
    for raw in CONF_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line == "[Rule]":
            in_rule = True
            continue
        if in_rule and line.startswith("[") and line.endswith("]"):
            break
        if not in_rule or not line or line.startswith("#"):
            continue
        match = re.match(r"RULE-SET,.*?/Rule/([A-Za-z0-9_]+[.]list),(\S+)(?:,|$)", line)
        if not match:
            # Inline WeChat mirrors Rule/WeChat.list.
            match = re.match(r"RULE-SET,WeChat,(\S+)(?:,|$)", line)
            if match:
                mapping["WeChat.list"] = (order_index, match.group(1))
                order_index += 1
            continue
        mapping[match.group(1)] = (order_index, match.group(2))
        order_index += 1
    return mapping


def load_domain_index() -> dict[str, list[tuple[str, str, str]]]:
    """Return domain -> [(file, type, rule), ...]."""
    index: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for path in sorted(RULE_DIR.glob("*.list")):
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            rule = raw.strip()
            if not rule or rule.startswith("#"):
                continue
            parts = [part.strip() for part in rule.split(",")]
            if len(parts) < 2:
                continue
            rule_type = parts[0].upper()
            if rule_type not in TRACKED_TYPES:
                continue
            value = parts[1].lower()
            index[value].append((path.name, rule_type, rule))
    return index


def main() -> int:
    policy_order = load_policy_order()
    domain_index = load_domain_index()
    conflicts: list[tuple[int, str, list[tuple[str, str, str, str]]]] = []

    for domain, entries in domain_index.items():
        files = {entry[0] for entry in entries}
        if len(files) < 2:
            continue
        enriched = []
        policies = set()
        min_order = 10_000
        for filename, rule_type, rule in entries:
            order, policy = policy_order.get(filename, (9999, "<not-in-conf>"))
            min_order = min(min_order, order)
            policies.add(policy)
            enriched.append((filename, policy, rule_type, rule))
        if len(policies) < 2:
            continue
        risk_bonus = 0 if files & HIGH_RISK_FILES else 1000
        conflicts.append((risk_bonus + min_order, domain, enriched))

    conflicts.sort(key=lambda item: (item[0], item[1]))

    print("### Cross-file Policy Conflicts")
    print()
    if not conflicts:
        print("No same-domain cross-file policy conflicts found.")
        return 0

    print(f"Found {len(conflicts)} same-domain entries that appear under multiple policies.")
    print("Showing up to 100, sorted by first-match risk.")
    print()

    for _rank, domain, entries in conflicts[:100]:
        entries.sort(key=lambda item: policy_order.get(item[0], (9999, ""))[0])
        effective_file, effective_policy, _rule_type, _rule = entries[0]
        print(f"- `{domain}` → effective `{effective_file}` / `{effective_policy}`")
        for filename, policy, rule_type, rule in entries:
            print(f"  - `{filename}` / `{policy}`: `{rule}`")
    if len(conflicts) > 100:
        print()
        print(f"_Truncated: {len(conflicts) - 100} additional conflicts omitted._")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
