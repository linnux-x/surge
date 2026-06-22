#!/usr/bin/env python3
"""Compare current and previous manifests to produce a diff report.

Reads compact .manifest files from Rule/.manifests/ and compares against
the previous version from git HEAD. Outputs diff_report.md (committed)
and diff_report.json (committed).

Uses only the Python standard library.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANIFEST_DIR = ROOT / "Rule" / ".manifests"
REPORT_MD = ROOT / "scripts" / "diff_report.md"
REPORT_JSON = ROOT / "scripts" / "diff_report.json"


def git_show_previous(manifest_path: Path) -> dict[str, str] | None:
    """Load previous manifest from git HEAD as {id: source}."""
    rel = manifest_path.relative_to(ROOT)
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{rel}"],
            capture_output=True, text=True, timeout=10,
            cwd=str(ROOT),
        )
        if result.returncode == 0:
            prev: dict[str, str] = {}
            for line in result.stdout.splitlines():
                parts = line.strip().split("\t", 1)
                if len(parts) == 2:
                    prev[parts[0]] = parts[1]
            return prev
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def load_current_manifest(manifest_path: Path) -> dict[str, str]:
    """Load current manifest as {id: source}."""
    data: dict[str, str] = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        parts = line.strip().split("\t", 1)
        if len(parts) == 2:
            data[parts[0]] = parts[1]
    return data


def get_rule_from_list(list_path: Path, rule_index: int) -> str:
    """Get rule text by 0-based index from .list file (skipping comments/blanks)."""
    idx = 0
    for line in list_path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if idx == rule_index:
            return s
        idx += 1
    return ""


def main() -> int:
    now = datetime.now().isoformat()
    manifest_files = sorted(MANIFEST_DIR.glob("*.manifest"))

    if not manifest_files:
        print("No manifest files found. Run manifest.py first.")
        return 1

    print(f"Comparing {len(manifest_files)} manifests against previous commit...")
    diffs: list[dict] = []

    for mf in manifest_files:
        curr = load_current_manifest(mf)
        prev = git_show_previous(mf)

        target_name = f"{mf.stem}.list"
        list_path = RULE_DIR / target_name

        if prev is None:
            # First time
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

        # Build added/removed with rule text from .list
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

    # Per-file table
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

    # Details
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

    report_md = "\n".join(lines)
    REPORT_MD.write_text(report_md, encoding="utf-8")

    # JSON report
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


if __name__ == "__main__":
    raise SystemExit(main())
