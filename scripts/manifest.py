#!/usr/bin/env python3
"""Generate compact rule manifests for diff tracking.

Each .list file gets a .manifest sidecar in Rule/.manifests/ with one line
per rule: <stable_id>\t<source_name>

The .manifests/ directory is committed to git so diff_manifests.py can compare against HEAD.

Uses only the Python standard library.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANIFEST_DIR = ROOT / "Rule" / ".manifests"


def stable_id(rule: str) -> str:
    """Content-hash based stable ID. Deterministic across runs."""
    return hashlib.sha256(rule.lower().strip().encode("utf-8")).hexdigest()[:12]


def parse_source_sections(text: str) -> list[tuple[str, list[str]]]:
    """Parse .list text into [(source_name, [rules])].

    Sections are delimited by: # ======= SourceName ========
    Rules before any header are attributed to "Manual".
    """
    sections: list[tuple[str, list[str]]] = []
    current_source = "Manual"
    current_rules: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        m = re.match(r"^#\s*={5,}\s*(.+?)\s*={5,}\s*$", stripped)
        if m:
            if current_rules:
                sections.append((current_source, current_rules))
            current_source = m.group(1).strip()
            current_rules = []
            continue
        if not stripped or stripped.startswith("#"):
            continue
        current_rules.append(stripped)

    if current_rules:
        sections.append((current_source, current_rules))
    return sections


def main() -> int:
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    list_files = sorted(RULE_DIR.glob("*.list"))
    if not list_files:
        print("No .list files found")
        return 1

    print(f"Generating manifests for {len(list_files)} ruleset files...")
    total_rules = 0

    for list_path in list_files:
        text = list_path.read_text(encoding="utf-8", errors="replace")
        sections = parse_source_sections(text)

        out_path = MANIFEST_DIR / f"{list_path.stem}.manifest"
        lines: list[str] = []
        seen: set[str] = set()  # lowercase dedup
        source_counts: dict[str, int] = {}

        for source_name, source_rules in sections:
            count = 0
            for rule in source_rules:
                rule_lower = rule.lower().strip()
                if rule_lower in seen:
                    continue
                seen.add(rule_lower)
                sid = stable_id(rule)
                lines.append(f"{sid}\t{source_name}")
                count += 1
            source_counts[source_name] = source_counts.get(source_name, 0) + count

        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        total_rules += len(lines)
        sources = ", ".join(f"{k}({v})" for k, v in sorted(source_counts.items()))
        print(f"  ✓ {list_path.name}: {len(lines)} rules — {sources}")

    print(f"\nTotal: {total_rules} rules across {len(list_files)} files")
    print(f"Manifests saved to {MANIFEST_DIR}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
