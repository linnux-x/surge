#!/usr/bin/env python3
"""Generate rule manifests and diff against previous commit.

Two modes:
  manifest.py              → Generate .manifest files from .list files
  manifest.py --diff       → Compare manifests vs git HEAD → diff reports

.manifest format: <stable_id>\t<source_name> (one rule per line, tab-separated)

Uses only the Python standard library.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANIFEST_DIR = ROOT / "Rule" / ".manifests"
REPORT_MD = ROOT / "scripts" / "diff_report.md"
REPORT_JSON = ROOT / "scripts" / "diff_report.json"


# ── Shared helpers ──────────────────────────────────────────────────────

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


# ── Generate mode ───────────────────────────────────────────────────────

def generate_manifests() -> int:
    """Generate .manifest files from all .list files."""
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
        seen: set[str] = set()
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


# ── Diff mode ───────────────────────────────────────────────────────────

def git_show_previous(manifest_path: Path) -> dict[str, str] | None:
    """Load previous manifest from git HEAD as {id: source}."""
    rel = manifest_path.relative_to(ROOT)
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{rel}"],
            capture_output=True, text=True, timeout=10,
            cwd=str(ROOT),
            check=False,
        )
        if result.returncode != 0:
            return None
        prev: dict[str, str] = {}
        for line in result.stdout.splitlines():
            parts = line.strip().split("\t", 1)
            if len(parts) == 2:
                prev[parts[0]] = parts[1]
        return prev
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        print(f"Warning: git timeout for {rel}, treating as first run")
        return None


def load_current_manifest(manifest_path: Path) -> dict[str, str]:
    """Load current manifest as {id: source}."""
    data: dict[str, str] = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        parts = line.strip().split("\t", 1)
        if len(parts) == 2:
            data[parts[0]] = parts[1]
    return data


def diff_manifests() -> int:
    """Compare current manifests vs git HEAD and produce diff reports."""
    now = datetime.now().isoformat()
    manifest_files = sorted(MANIFEST_DIR.glob("*.manifest"))

    if not manifest_files:
        print("No manifest files found. Run 'python3 scripts/manifest.py' first.")
        return 1

    print(f"Comparing {len(manifest_files)} manifests against previous commit...")
    diffs: list[dict] = []

    for mf in manifest_files:
        curr = load_current_manifest(mf)
        prev = git_show_previous(mf)

        target_name = f"{mf.stem}.list"

        if prev is None:
            added_ids = set(curr.keys())
            removed_ids: set[str] = set()
            source_changed: list[dict] = []
        else:
            prev_set = set(prev.keys())
            curr_set = set(curr.keys())
            added_ids = curr_set - prev_set
            removed_ids = prev_set - curr_set
            source_changed = [
                {"id": sid, "old_source": prev[sid], "new_source": curr[sid]}
                for sid in prev_set & curr_set
                if prev[sid] != curr[sid]
            ]

        added = sorted(
            [{"id": sid, "source": curr[sid]} for sid in added_ids],
            key=lambda x: x["id"],
        )
        removed = sorted(
            [{"id": sid, "source": prev[sid] if prev else ""} for sid in removed_ids],
            key=lambda x: x["id"],
        )

        diffs.append({
            "file": target_name,
            "prev_total": len(prev) if prev else 0,
            "curr_total": len(curr),
            "added_count": len(added),
            "removed_count": len(removed),
            "source_changed_count": len(source_changed),
            "added_sample": added[:100],
            "removed_sample": removed[:100],
            "source_changed_sample": source_changed[:50],
        })

        if len(added_ids) + len(removed_ids) + len(source_changed) > 0:
            print(f"  {target_name}: +{len(added_ids)} / -{len(removed_ids)} / ~{len(source_changed)}")
        else:
            print(f"  {target_name}: no changes")

    # ── Markdown Report ──────────────────────────────────────────
    total_added = sum(d["added_count"] for d in diffs)
    total_removed = sum(d["removed_count"] for d in diffs)
    total_changed = sum(d["source_changed_count"] for d in diffs)
    files_changed = sum(1 for d in diffs if d["added_count"] + d["removed_count"] + d["source_changed_count"] > 0)

    lines: list[str] = [
        "# Surge Rule Diff Report",
        f"Generated: {now}",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Files changed | {files_changed} |",
        f"| Rules added | {total_added} |",
        f"| Rules removed | {total_removed} |",
        f"| Source attribution changed | {total_changed} |",
        "",
    ]

    lines.append("## Per-File Changes")
    lines.append("")
    lines.append("| File | Prev | Curr | Added | Removed | Source Δ |")
    lines.append("|------|------|------|-------|---------|----------|")
    for d in diffs:
        if d["added_count"] + d["removed_count"] + d["source_changed_count"] > 0:
            lines.append(
                f"| {d['file']} | {d['prev_total']} | {d['curr_total']} "
                f"| +{d['added_count']} | -{d['removed_count']} | ~{d['source_changed_count']} |"
            )
    lines.append("")

    for d in diffs:
        if d["added_count"] + d["removed_count"] + d["source_changed_count"] == 0:
            continue
        lines.append(f"## {d['file']}")
        lines.append("")
        if d["added_count"] > 0:
            lines.append(f"**Added: {d['added_count']}** (showing first {min(d['added_count'], 100)})")
            lines.append("```")
            for r in d["added_sample"]:
                lines.append(f"  + [{r['source']}] {r['id']}")
            if d["added_count"] > 100:
                lines.append(f"  ... and {d['added_count'] - 100} more")
            lines.append("```")
            lines.append("")
        if d["removed_count"] > 0:
            lines.append(f"**Removed: {d['removed_count']}** (showing first {min(d['removed_count'], 100)})")
            lines.append("```")
            for r in d["removed_sample"]:
                lines.append(f"  - [{r['source']}] {r['id']}")
            if d["removed_count"] > 100:
                lines.append(f"  ... and {d['removed_count'] - 100} more")
            lines.append("```")
            lines.append("")
        if d["source_changed_count"] > 0:
            lines.append(f"**Source changed: {d['source_changed_count']}**")
            lines.append("```")
            for r in d["source_changed_sample"]:
                lines.append(f"  ~ {r['id']}: [{r['old_source']} → {r['new_source']}]")
            if d["source_changed_count"] > 50:
                lines.append(f"  ... and {d['source_changed_count'] - 50} more")
            lines.append("```")
            lines.append("")

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    REPORT_JSON.write_text(
        json.dumps({
            "generated_at": now,
            "total_added": total_added,
            "total_removed": total_removed,
            "total_source_changed": total_changed,
            "diffs": diffs,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\nDiff: +{total_added} added, -{total_removed} removed")
    print(f"Report: {REPORT_MD}")
    return 0


# ── Main ────────────────────────────────────────────────────────────────

def main() -> int:
    if "--diff" in sys.argv:
        return diff_manifests()
    return generate_manifests()


if __name__ == "__main__":
    raise SystemExit(main())
