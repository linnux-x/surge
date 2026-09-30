#!/usr/bin/env python3
"""Report domain rules fully shadowed by an earlier ruleset with another policy.

The report covers DOMAIN and DOMAIN-SUFFIX exact/parent relationships in
Conf/Linnux.conf order. It does not claim to model keyword, wildcard, IP,
process, or DNS matching; use test_routing_order.py for concrete hosts.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
CONF_FILE = ROOT / "Conf" / "Linnux.conf"
TRACKED_TYPES = {"DOMAIN", "DOMAIN-SUFFIX"}


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
        match = re.match(r"RULE-SET,.*?/Rule/([A-Za-z0-9_]+[.]list),([^,]+)(?:,|$)", line)
        if not match:
            # Inline WeChat mirrors Rule/WeChat.list.
            match = re.match(r"RULE-SET,WeChat,([^,]+)(?:,|$)", line)
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
            if len(parts) < 2 or parts[0].upper() not in TRACKED_TYPES:
                continue
            index[parts[1].lower()].append((path.name, parts[0].upper(), rule))
    return index


def covering_values(value: str) -> list[str]:
    """Return the value and every domain-label parent, most specific first."""
    parts = value.split(".")
    return [".".join(parts[i:]) for i in range(len(parts))]


def collect_conflicts(policy_order, domain_index):
    """Find later rules whose entire domain match set has an earlier winner.

    A DOMAIN can be covered by an identical DOMAIN or a parent DOMAIN-SUFFIX.
    A DOMAIN-SUFFIX needs an earlier identical/parent DOMAIN-SUFFIX; an exact
    DOMAIN covers only the suffix apex and therefore cannot shadow it.
    """
    conflicts = []
    for value, entries in domain_index.items():
        for filename, rule_type, rule in entries:
            if filename not in policy_order:
                continue
            loser_order, loser_policy = policy_order[filename]
            winner = None
            for candidate_value in covering_values(value):
                for earlier_file, earlier_type, earlier_rule in domain_index.get(candidate_value, ()):
                    if earlier_file == filename or earlier_file not in policy_order:
                        continue
                    earlier_order, earlier_policy = policy_order[earlier_file]
                    if earlier_order >= loser_order:
                        continue
                    if earlier_type != "DOMAIN-SUFFIX" and not (
                        rule_type == "DOMAIN" and candidate_value == value
                    ):
                        continue
                    if winner is None or earlier_order < winner[0]:
                        winner = (earlier_order, earlier_file, earlier_policy, earlier_rule)
            if winner is not None and winner[2] != loser_policy:
                conflicts.append((winner[0], value, winner[1:], (filename, loser_policy, rule)))
    conflicts.sort(key=lambda item: (item[0], item[1], item[3][0], item[3][2]))
    return conflicts


def print_summary(conflicts) -> None:
    pair_counts: dict[tuple[str, str, str, str], int] = defaultdict(int)
    for _rank, _value, winner, loser in conflicts:
        pair_counts[(winner[0], winner[1], loser[0], loser[1])] += 1

    print("### Cross-file Policy Shadows — Summary")
    print()
    print(f"Fully shadowed DOMAIN/DOMAIN-SUFFIX entries with a different policy: {len(conflicts)}")
    print()
    print("| count | effective first match | shadowed entry |")
    print("|---:|---|---|")
    for (winner_file, winner_policy, loser_file, loser_policy), n in sorted(
        pair_counts.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"| {n} | `{winner_file}` / `{winner_policy}` | `{loser_file}` / `{loser_policy}` |")
    print()
    print("_Informational: review intent before excluding either rule. "
          "Keyword, wildcard, IP, and inline matches are outside this report._")


def main() -> int:
    conflicts = collect_conflicts(load_policy_order(), load_domain_index())
    if "--summary" in sys.argv:
        print_summary(conflicts)
        return 0

    print("### Cross-file Policy Shadows")
    print()
    print(f"Found {len(conflicts)} fully shadowed DOMAIN/DOMAIN-SUFFIX entries with a different policy.")
    print("Showing up to 100 in first-match order.")
    print()
    for _rank, value, winner, loser in conflicts[:100]:
        print(f"- `{value}`: effective `{winner[0]}` / `{winner[1]}` via `{winner[2]}`")
        print(f"  - shadowed `{loser[0]}` / `{loser[1]}`: `{loser[2]}`")
    if len(conflicts) > 100:
        print()
        print(f"_Truncated: {len(conflicts) - 100} additional entries omitted._")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
