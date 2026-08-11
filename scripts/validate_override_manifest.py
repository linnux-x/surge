#!/usr/bin/env python3
"""Validate the public Manual override manifest against Rule/Manual inputs."""
from __future__ import annotations
import json
import re
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "Rule" / "Manual"
MANIFEST = MANUAL / "override-manifest.json"
TEST_CSV = ROOT / "tests" / "expected-routing.csv"
FORBIDDEN = re.compile(r"(?:\b(?:10|127)\.\d{1,3}\.|\b192\.168\.|\b172\.(?:1[6-9]|2\d|3[01])\.|token=|password=|secret=|ghp_|github_pat_|sk-|BEGIN (?:RSA|OPENSSH|PRIVATE)|https?://[^\s,]+:[^\s,@]+@)", re.I)
RISKY_DOMAIN_KEYWORDS = {"amazon", "api", "apple", "cdn", "cloud", "google", "java", "microsoft"}


def active_rules(path: Path) -> set[str]:
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")}


def routing_test_domains() -> set[str]:
    with TEST_CSV.open(newline="", encoding="utf-8") as handle:
        return {row["domain"].strip().lower() for row in csv.DictReader(handle) if row.get("domain")}


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[FAIL] invalid override manifest: {exc}")
        return 1
    files = data.get("files")
    entries = data.get("entries")
    if data.get("schema_version") != 1 or not isinstance(files, dict) or not isinstance(entries, list):
        print("[FAIL] override manifest schema_version/files/entries is invalid")
        return 1
    manual_files = {p.name: p for p in MANUAL.glob("*.txt") if p.name != "README.md"}
    if set(files) != set(manual_files):
        errors.append("file baseline mismatch: declared and actual Manual files must match")
    for name, record in files.items():
        if not isinstance(record, dict) or record.get("action") not in {"include", "exclude"}:
            errors.append(f"{name}: invalid action")
        for field in ("reason", "destination"):
            if not isinstance(record, dict) or not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f"{name}: missing {field}")
    declared: dict[tuple[str, str], dict] = {}
    test_domains = routing_test_domains()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("entry is not an object"); continue
        key = (entry.get("source_file", ""), entry.get("rule", ""))
        if not key[0] or not key[1] or key in declared:
            errors.append("entry has missing or duplicate source_file/rule"); continue
        declared[key] = entry
        if key[0] not in manual_files or key[1] not in active_rules(manual_files[key[0]]):
            errors.append(f"entry does not match Manual input: {key[0]}")
        if not entry.get("reason") or not entry.get("destination"):
            errors.append(f"entry missing reason/destination: {key[0]}")
        route_tests = entry.get("route_tests")
        if not isinstance(route_tests, list) or not route_tests or not all(isinstance(item, str) and item.strip() for item in route_tests):
            errors.append(f"entry missing route_tests: {key[0]}")
        elif missing := sorted({item.strip().lower() for item in route_tests} - test_domains):
            errors.append(f"entry route_tests absent from expected-routing.csv: {key[0]}: {missing}")
    for path in manual_files.values():
        for rule in active_rules(path):
            if FORBIDDEN.search(rule):
                errors.append(f"sensitive/public-boundary pattern in {path.name}")
            parts = [part.strip() for part in rule.split(",")]
            if (len(parts) >= 2 and parts[0] == "DOMAIN-KEYWORD"
                    and parts[1].lower() in RISKY_DOMAIN_KEYWORDS
                    and (path.name, rule) not in declared):
                errors.append(f"risky broad keyword requires entry-level approval: {path.name}: {rule}")
    if errors:
        print("[FAIL] override manifest validation")
        for error in errors: print(f"- {error}")
        return 1
    print(f"[PASS] override manifest: {len(manual_files)} file baselines, {len(entries)} entry-level exceptions")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
