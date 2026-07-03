#!/usr/bin/env python3
"""Generate Clash/mihomo rule-provider files from Surge rulesets.

The repository keeps Surge rule sets as the canonical generated output under
``Rule/*.list``. This script mirrors those files into Clash-compatible
``classical`` rule-provider YAML files under ``clash/*.yaml``.

The payload intentionally keeps the rule body policy-free, matching Clash rule
provider syntax:

    payload:
      - 'DOMAIN-SUFFIX,example.com'

Only Python stdlib is used so the script can run in GitHub Actions without
additional dependencies.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RULE_DIR = Path("Rule")
CLASH_DIR = Path("clash")

# Clash Premium supports the core types. mihomo supports a broader superset such
# as DOMAIN-WILDCARD and IP-ASN. We preserve them rather than silently dropping
# rules, and emit a summary so compatibility-sensitive users can audit them.
MIHOMO_ONLY_OR_COMPAT_TYPES = {
    "DOMAIN-WILDCARD",
    "IP-ASN",
    "PROCESS-NAME",
    "URL-REGEX",
    "USER-AGENT",
}

HEADER_RE = re.compile(r"^#\s*(TOTAL|UPDATED|SOURCES|Generated|Source)", re.IGNORECASE)


def yaml_quote(value: str) -> str:
    """Return a YAML single-quoted scalar."""
    return "'" + value.replace("'", "''") + "'"


def parse_surge_file(path: Path) -> tuple[list[str], list[str]]:
    """Split a Surge .list file into header comments and payload rules."""
    comments: list[str] = []
    rules: list[str] = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            if HEADER_RE.match(line):
                comments.append(line)
            continue
        rules.append(line)

    return comments, rules


def clash_path_for(source: Path) -> Path:
    return CLASH_DIR / f"{source.stem}.yaml"


def render_clash_yaml(source: Path, comments: list[str], rules: list[str]) -> str:
    lines = [
        f"# Generated from {source.as_posix()}",
        "# Format: Clash/mihomo rule-provider, behavior: classical",
    ]
    lines.extend(comments)
    lines.append("payload:")
    lines.extend(f"  - {yaml_quote(rule)}" for rule in rules)
    lines.append("")
    return "\n".join(lines)


def generate(check: bool = False) -> int:
    if not RULE_DIR.is_dir():
        raise SystemExit(f"Rule directory not found: {RULE_DIR}")

    sources = sorted(RULE_DIR.glob("*.list"))
    if not sources:
        raise SystemExit("No Rule/*.list files found")

    CLASH_DIR.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    total_rules = 0
    compat_counts: dict[str, int] = {}

    expected_files = {clash_path_for(source) for source in sources}

    for source in sources:
        comments, rules = parse_surge_file(source)
        total_rules += len(rules)
        for rule in rules:
            rule_type = rule.split(",", 1)[0]
            if rule_type in MIHOMO_ONLY_OR_COMPAT_TYPES:
                compat_counts[rule_type] = compat_counts.get(rule_type, 0) + 1

        out_path = clash_path_for(source)
        rendered = render_clash_yaml(source, comments, rules)
        if check:
            existing = out_path.read_text(encoding="utf-8") if out_path.exists() else None
            if existing != rendered:
                errors.append(f"out of date: {out_path}")
        else:
            out_path.write_text(rendered, encoding="utf-8", newline="\n")

    # Remove stale Clash files when the Surge source was deleted/renamed.
    for stale in sorted(CLASH_DIR.glob("*.yaml")):
        if stale not in expected_files:
            if check:
                errors.append(f"stale file: {stale}")
            else:
                stale.unlink()

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Generated {len(sources)} Clash rule-provider files with {total_rules} payload rules.")
    if compat_counts:
        detail = ", ".join(f"{k}:{v}" for k, v in sorted(compat_counts.items()))
        print(f"Compatibility note: preserved mihomo/extended rule types: {detail}")
    return 0


def validate_payload_counts() -> int:
    """Validate generated YAML shape and source/payload line counts."""
    errors: list[str] = []
    for source in sorted(RULE_DIR.glob("*.list")):
        out_path = clash_path_for(source)
        if not out_path.exists():
            errors.append(f"missing output: {out_path}")
            continue
        _, source_rules = parse_surge_file(source)
        payload_rules = []
        seen_payload = False
        for raw in out_path.read_text(encoding="utf-8").splitlines():
            if raw == "payload:":
                seen_payload = True
                continue
            if raw.startswith("  - "):
                payload_rules.append(raw)
        if not seen_payload:
            errors.append(f"missing payload key: {out_path}")
        if len(payload_rules) != len(source_rules):
            errors.append(
                f"payload count mismatch for {out_path}: "
                f"{len(payload_rules)} != {len(source_rules)}"
            )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Clash payload validation passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are out of date")
    parser.add_argument("--validate", action="store_true", help="validate generated payload counts")
    args = parser.parse_args()

    status = generate(check=args.check)
    if status != 0:
        return status
    if args.validate:
        return validate_payload_counts()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
