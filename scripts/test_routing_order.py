#!/usr/bin/env python3
"""Simulate Surge first-match routing order and validate against expected results.

Loads Rule/*.list files and tests/expected-routing.csv, then checks that
each domain routes to the expected ruleset in Surge's first-match order.

The routing order is read from Conf/LINNUX.conf (or a hardcoded fallback).
Uses only the Python standard library.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
CONF_FILE = ROOT / "Conf" / "LINNUX.conf"
TEST_CSV = ROOT / "tests" / "expected-routing.csv"

# ── Routing order ──────────────────────────────────────────────────────

# Fallback order (matches Conf/LINNUX.conf [Rule] section)
FALLBACK_ORDER: list[tuple[str, str]] = [
    ("WeChat.list", "WeChat.list"),
    ("Speedtest.list", "Speedtest.list"),
    ("AI.list", "AI.list"),
    ("Apple_CN.list", "DIRECT"),
    ("Apple.list", "Apple.list"),
    ("Microsoft_CDN.list", "DIRECT"),
    ("Microsoft.list", "Microsoft.list"),
    ("Telegram.list", "Telegram.list"),
    ("Download.list", "Download.list"),
    ("Game.list", "Game.list"),
    ("YouTube.list", "YouTube.list"),
    ("TikTok.list", "TikTok.list"),
    ("SocialMedia.list", "SocialMedia.list"),
    ("PayPal.list", "PayPal.list"),
    ("Google.list", "Google.list"),
    ("Netflix.list", "Netflix.list"),
    ("Disney.list", "Disney.list"),
    ("ChinaMedia.list", "ChinaMedia.list"),
    ("GlobalMedia.list", "GlobalMedia.list"),
    ("CDN.list", "CDN.list"),
    ("Global.list", "Global.list"),
    ("China.list", "DIRECT"),
    ("LAN", "DIRECT"),
    ("China_IP.list", "DIRECT"),
]


def load_ruleset(path: Path) -> set[str]:
    """Load a .list file and return set of lowercase non-comment rules."""
    raw_rules: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        raw_rules.add(line.lower())
    return raw_rules


def extract_domain(rule: str) -> str | None:
    """Extract domain from a Surge rule line.

    Supports: DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-WILDCARD, IP-CIDR, IP-CIDR6
    Returns the domain portion, or None for non-domain rules.
    """
    parts = [p.strip() for p in rule.split(",")]
    if len(parts) < 2:
        return None

    rule_type = parts[0].upper()
    value = parts[1].lower()

    if rule_type == "DOMAIN":
        return value
    elif rule_type == "DOMAIN-SUFFIX":
        return value
    elif rule_type == "DOMAIN-KEYWORD":
        return value
    elif rule_type == "DOMAIN-WILDCARD":
        return value
    elif rule_type == "IP-CIDR":
        return value  # e.g. "10.0.0.0/8"
    elif rule_type == "IP-CIDR6":
        return value
    else:
        return None


def match_domain(domain: str, rules: set[str]) -> bool:
    """Check if a domain matches any rule in a ruleset.

    Implements Surge's matching logic:
    - DOMAIN: exact match
    - DOMAIN-SUFFIX: domain equals or ends with .suffix
    - DOMAIN-KEYWORD: keyword appears anywhere in domain
    - DOMAIN-WILDCARD: wildcard match (basic * support)
    - IP-CIDR/IP-CIDR6: exact match on CIDR (basic)
    """
    domain_lower = domain.lower()

    for rule in rules:
        parts = [p.strip() for p in rule.split(",")]
        if len(parts) < 2:
            continue

        rule_type = parts[0].upper()
        value = parts[1].lower()

        # Strip options like no-resolve
        value_clean = re.sub(r",no-resolve$", "", value)

        if rule_type == "DOMAIN":
            if domain_lower == value_clean:
                return True
        elif rule_type == "DOMAIN-SUFFIX":
            if domain_lower == value_clean:
                return True
            if domain_lower.endswith("." + value_clean):
                return True
        elif rule_type == "DOMAIN-KEYWORD":
            if value_clean in domain_lower:
                return True
        elif rule_type == "DOMAIN-WILDCARD":
            # Simple wildcard: * → .* regex
            pattern = "^" + re.escape(value_clean).replace(r"\*", ".*") + "$"
            if re.match(pattern, domain_lower):
                return True

    return False


def load_routing_order() -> list[tuple[str, str]]:
    """Parse routing order from LINNUX.conf, or return fallback."""
    if not CONF_FILE.exists():
        return FALLBACK_ORDER

    order: list[tuple[str, str]] = []
    content = CONF_FILE.read_text(encoding="utf-8", errors="replace")

    in_rule_section = False
    for line in content.splitlines():
        line = line.strip()

        if line == "[Rule]":
            in_rule_section = True
            continue
        if in_rule_section and line.startswith("[") and line.endswith("]"):
            break
        if not in_rule_section:
            continue

        # RULE-SET,url,POLICY
        m = re.match(
            r"RULE-SET,.*?/Rule/([A-Za-z0-9_]+\.list),(\S+)(?:,|$)", line
        )
        if m:
            ruleset_name = m.group(1)
            policy = m.group(2)
            order.append((ruleset_name, policy))
            continue

        # RULE-SET,LAN,DIRECT
        m_lan = re.match(r"RULE-SET,LAN,(\S+)", line)
        if m_lan:
            order.append(("LAN", m_lan.group(1)))
            continue

        # FINAL,policy
        m_final = re.match(r"FINAL,(\S+)", line)
        if m_final:
            order.append(("FINAL", m_final.group(1)))
            continue

    return order if order else FALLBACK_ORDER


def simulate_routing(domain: str, routing_order: list[tuple[str, str]],
                     rulesets: dict[str, set[str]]) -> str:
    """Simulate first-match routing for a domain.

    Returns the matched ruleset name (or DIRECT/Global/policy name).
    """
    for ruleset_name, policy in routing_order:
        if ruleset_name == "LAN":
            # LAN matches RFC 1918 / loopback
            if re.match(r"^(10\.|172\.(1[6-9]|2\d|3[01])\.|192\.168\.|127\.)", domain):
                return f"LAN→{policy}"
            continue

        if ruleset_name == "FINAL":
            return f"FINAL→{policy}"

        # Check if this is a .list ruleset
        if ruleset_name in rulesets:
            if match_domain(domain, rulesets[ruleset_name]):
                return f"{ruleset_name}→{policy}"

    return "FINAL→Global"  # unreachable fallback


def main() -> int:
    # Load routing order
    routing_order = load_routing_order()
    print(f"Loaded routing order: {len(routing_order)} steps")

    # Load all .list files
    rulesets: dict[str, set[str]] = {}
    for list_file in sorted(RULE_DIR.glob("*.list")):
        name = list_file.name
        rulesets[name] = load_ruleset(list_file)
        rule_count = len(rulesets[name])
        print(f"  Loaded {name}: {rule_count} rules")

    if not rulesets:
        print("ERROR: No .list files found in Rule/")
        return 1

    # Load test cases
    if not TEST_CSV.exists():
        print(f"\nERROR: Test CSV not found: {TEST_CSV}")
        return 1

    test_cases: list[dict[str, str]] = []
    with open(TEST_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_cases.append(row)

    if not test_cases:
        print("No test cases found")
        return 0

    # Simulate routing
    print(f"\n{'='*70}")
    print(f"Running {len(test_cases)} routing tests...")
    print(f"{'='*70}\n")

    passed = 0
    failed: list[dict] = []

    for tc in test_cases:
        domain = tc["domain"].strip()
        expected = tc["expected_ruleset"].strip()
        note = tc.get("note", "").strip()

        actual = simulate_routing(domain, routing_order, rulesets)

        # Normalize: we care about which ruleset matched (or DIRECT/Global)
        # actual format: "AI.list→AI" or "DIRECT" etc.
        matched_ruleset = actual.split("→")[0] if "→" in actual else actual

        # Normalize expected: "DIRECT" could be matched by China.list→DIRECT or LAN→DIRECT or China_IP.list→DIRECT
        if expected == "DIRECT":
            # Any match that routes to DIRECT counts
            policy = actual.split("→")[1] if "→" in actual else actual
            success = policy == "DIRECT"
        elif expected == "Global":
            # Global.list→Global or FINAL→Global
            success = matched_ruleset in ("Global.list", "FINAL")
        else:
            success = matched_ruleset == expected

        status = "✅" if success else "❌"
        if success:
            passed += 1
        else:
            failed.append({"domain": domain, "expected": expected, "actual": actual, "note": note})

        print(f"  {status} {domain:40s} → {actual:35s} (expected: {expected})"
              + (f"  # {note}" if note else ""))

    # Summary
    total = len(test_cases)
    print(f"\n{'='*70}")
    print(f"Results: {passed}/{total} passed"
          + (f", {len(failed)} FAILED" if failed else ", all passed! ✅"))
    print(f"{'='*70}")

    if failed:
        print(f"\n❌ FAILURES ({len(failed)}):")
        for f_entry in failed:
            print(f"  • {f_entry['domain']} — expected: {f_entry['expected']}, got: {f_entry['actual']}"
                  + (f"  ({f_entry['note']})" if f_entry['note'] else ""))

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
