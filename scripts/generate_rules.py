#!/usr/bin/env python3
"""Generate Surge rulesets from upstream sources.

Replaces the inline bash in .github/workflows/auto-rules.yml with Python.
Reads CHANGED_RULESETS from environment (JSON array) or processes all rulesets
on workflow_dispatch (GITHUB_EVENT_NAME=workflow_dispatch).

Supports: manual rules, exclude files, domainset/cidr conversion, guardrails,
dedup, CIDR pruning, validation, and Global overlap pruning.

A file whose regenerated content differs from the published one only in the
`# UPDATED:` header is left untouched, so unchanged rulesets never produce a
timestamp-only diff. `--check` performs the same generation without publishing
and exits 1 when any ruleset would change.

Every published ruleset is paired with `Rule/.sources/<name>.json`, which pins
the converted upstream inputs by SHA-256; online runs keep the raw responses in
a local cache (see source_cache.py). `--offline` rebuilds the selected rulesets
from exactly those pinned inputs, so a Manual edit can be regenerated without
pulling in upstream drift. `--rulesets` selects targets instead of the
CHANGED_RULESETS environment variable.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import shutil
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Optional, Tuple
from zoneinfo import ZoneInfo

# Ensure scripts/ is on the path so 'import sources' works
_scripts_dir = Path(__file__).resolve().parent
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from sources import (
    RULE_SPECS, OVERLAP_DEPENDENTS, GLOBAL_OVERLAP_RULESETS,
    expand_ruleset_dependencies,
)
from cidr_rules import prune_cidr_lines
from rule_validator import validate_rule_file
from file_batch import publish_files
import source_cache
# Re-export existing helper names for callers importing from generate_rules.
from source_transforms import (
    clean_source, convert_domainset, convert_cidr, filter_candidates,
    apply_project_guardrails, convert_source,
)

# ── Constants ─────────────────────────────────────────────────────────────

# Anchor to the repository, not the caller's cwd: running from another
# directory used to create an empty Rule/ there and generate without the
# Manual include/exclude inputs.
ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANUAL_DIR = RULE_DIR / "Manual"
REPO_URL = os.environ.get("REPO_URL", "https://github.com/linnux-x/surge")
AUTHOR_NAME = os.environ.get("AUTHOR_NAME", "linnux-x")
# Retries cover transient failures, including TLS handshake resets observed during
# full generation; timeouts stop a stalled upstream from hanging the workflow.
CURL_OPTS = [
    "--retry", "3", "--retry-delay", "5", "--retry-all-errors",
    "--connect-timeout", "10", "--max-time", "60",
]
FETCH_SUBPROCESS_TIMEOUT = 120  # hard backstop around the curl call itself
UPDATED_PREFIX = "# UPDATED:"
HEADER_LINES = 6  # NAME, AUTHOR, REPO, UPDATED, FORMAT, TOTAL
SNAPSHOT_DIR = ".sources"
# Set by main(--offline): read pinned snapshots from the local cache, never the network.
OFFLINE = False


# ── Helpers ────────────────────────────────────────────────────────────────

def should_process(target: str, changed_rulesets: list[str] | set[str], force_all: bool) -> bool:
    """Determine if a ruleset should be processed this run."""
    if force_all:
        return True
    return target in changed_rulesets


def prune_shadowed_domains(lines: list[str]) -> list[str]:
    """Remove DOMAIN/DOMAIN-SUFFIX rules fully covered by a broader
    DOMAIN-SUFFIX in the same file (behaviour-preserving, like CIDR pruning).

    A child is pruned only when its per-rule options are a subset of the
    covering parent's options, so options like extended-matching are never
    weakened by the prune. Comments and section headers are preserved.
    """
    suffix_opts: dict[str, set[str]] = {}
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = [p.strip() for p in stripped.split(",")]
        if len(parts) >= 2 and parts[0].upper() == "DOMAIN-SUFFIX":
            val = parts[1].lower()
            opts = {o.lower() for o in parts[2:]}
            # If the same suffix appears twice, keep the larger option set so
            # pruning stays conservative.
            if val not in suffix_opts or opts >= suffix_opts[val]:
                suffix_opts[val] = opts

    def covering_parent(value: str, include_self: bool) -> Optional[str]:
        if include_self and value in suffix_opts:
            return value
        segments = value.split(".")
        for i in range(1, len(segments)):
            parent = ".".join(segments[i:])
            if parent in suffix_opts:
                return parent
        return None

    out: list[str] = []
    removed = 0
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            parts = [p.strip() for p in stripped.split(",")]
            if len(parts) >= 2 and parts[0].upper() in {"DOMAIN", "DOMAIN-SUFFIX"}:
                val = parts[1].lower()
                opts = {o.lower() for o in parts[2:]}
                parent = covering_parent(val, include_self=(parts[0].upper() == "DOMAIN"))
                if parent is not None and opts <= suffix_opts[parent]:
                    removed += 1
                    continue
        out.append(line)

    if removed:
        print(f"  Suffix prune: removed {removed} entries covered by a broader DOMAIN-SUFFIX")
    return out


def without_updated_header(content: bytes) -> list[bytes]:
    """Return file lines with the generated `# UPDATED:` header line masked.

    Only the fixed header block is considered, so a Manual comment that happens
    to start with the same text still counts as content.
    """
    lines = content.split(b"\n")
    prefix = UPDATED_PREFIX.encode()
    return [b"" if i < HEADER_LINES and line.startswith(prefix) else line
            for i, line in enumerate(lines)]


def content_changed(old: bytes | None, new: bytes) -> bool:
    """True when publishing `new` would change more than the UPDATED timestamp."""
    return old is None or (old != new and without_updated_header(old) != without_updated_header(new))


def dedupe_preserve_order(lines: list[str]) -> list[str]:
    """Remove duplicate non-comment lines, preserving first occurrence order."""
    seen = set()
    out = []
    for line in lines:
        if line.startswith("#") or not line.strip():
            out.append(line)
        elif line.lower() not in seen:
            seen.add(line.lower())
            out.append(line)
    return out


def prune_redundant_cidr(filepath: Path):
    """Remove CIDR entries that are subnets of a broader CIDR in the same file.

    Only prune within identical option sets: no-resolve changes DNS behavior.
    Built into generate_rules.py (was scripts/prune_cidr.py).
    Compatibility file wrapper; prints summary if pruning occurred.
    """
    lines = filepath.read_text(encoding="utf-8").splitlines()

    pruned, before, after = prune_cidr_lines(lines)
    if before != after:
        filepath.write_text("\n".join(pruned) + "\n", encoding="utf-8")
        print(f"  CIDR prune: {before} → {after} ({before - after} redundant)")


# ── Processing ──────────────────────────────────────────────────────────────

@lru_cache(maxsize=None)
def fetch_remote_source(url: str) -> tuple[str, ...]:
    """Fetch a remote source; failures must stop generation."""
    result = subprocess.run(
        ["curl", "-fsSL", *CURL_OPTS, url],
        capture_output=True, text=True, check=True,
        timeout=FETCH_SUBPROCESS_TIMEOUT,
    )
    return tuple(result.stdout.splitlines())


def fetch_source(url: str, source_format: Optional[str]) -> list[str]:
    raw = list(fetch_remote_source(url))
    try:
        source_cache.put(url, raw, source_cache.lines_sha256(convert_source(raw, source_format)))
    except (OSError, ValueError) as exc:
        # The cache only enables later offline runs; it must not fail generation.
        print(f"  Warning: could not cache snapshot of {url}: {exc}")
    return raw


def snapshot_path(rule_dir: Path, target_name: str) -> Path:
    return rule_dir / SNAPSHOT_DIR / f"{target_name.rsplit('.', 1)[0]}.json"


def pinned_sources(target_name: str) -> dict[tuple[str, str, Optional[str]], str]:
    """Return {(label, url, format): converted sha256} recorded for the published ruleset."""
    path = snapshot_path(RULE_DIR, target_name)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise source_cache.SnapshotMissing(
            f"{target_name} has no {SNAPSHOT_DIR} record; run an online generation of it first") from exc
    return {(s["label"], s["url"], s["format"]): s["sha256"] for s in data["sources"]}


def load_source(target_name: str, pins: Optional[dict], source: Tuple[str, str, Optional[str]]) -> tuple[list[str], Optional[str]]:
    """Fetch a source online, or return its pinned snapshot and expected hash offline."""
    source_name, source_url, source_format = source
    if pins is None:
        return fetch_source(source_url, source_format), None
    if source not in pins:
        raise source_cache.SnapshotMissing(
            f"{target_name}: source {source_name} is not pinned; run an online generation of it first")
    return source_cache.get(source_url, pins[source]), pins[source]


def process_rule(target_name: str, display_name: str, sources: list[Tuple[str, str, Optional[str]]]):
    """Generate a single ruleset file from its sources."""
    target_path = RULE_DIR / target_name
    filename_no_ext = target_name.rsplit(".", 1)[0]
    exclude_file = MANUAL_DIR / f"{filename_no_ext}.exclude.txt"

    lines: list[str] = []
    pins = pinned_sources(target_name) if OFFLINE else None
    records: list[dict] = []

    # Manual rules first (highest priority)
    manual_file = MANUAL_DIR / f"{filename_no_ext}.txt"
    if manual_file.is_file():
        lines.append("# ======= Manual Rules ========")
        lines.extend(manual_file.read_text(encoding="utf-8").replace("\r", "").splitlines())
        lines.append("")

    # Upstream sources
    for source_name, source_url, source_format in sources:
        raw, expected = load_source(target_name, pins, (source_name, source_url, source_format))
        converted = convert_source(raw, source_format)
        if not converted:
            raise ValueError(f"Empty upstream after cleaning: {source_name} ({source_url})")
        converted_sha = source_cache.lines_sha256(converted)
        if expected is not None and converted_sha != expected:
            print(f"  Note: {source_name} converts differently under the current code; "
                  "its pin will follow the new conversion")
        records.append({"label": source_name, "url": source_url, "format": source_format,
                        "sha256": converted_sha})

        filtered = filter_candidates(converted, exclude_file)

        lines.append(f"# ======= {source_name} ========")
        lines.extend(filtered)
        lines.append("")

    # Generated files must not end in blank content lines: they add diff noise
    # and violate the repository's whitespace gate.
    while lines and not lines[-1].strip():
        lines.pop()

    # Guardrails, dedup, suffix prune, CIDR prune
    lines = apply_project_guardrails(target_name, lines)
    lines = dedupe_preserve_order(lines)
    lines = prune_shadowed_domains(lines)

    # Preserve the old write/read splitlines normalization, including empty
    # content and Unicode line separators, without a temporary-file round trip.
    pruned_lines, before, after = prune_cidr_lines(("\n".join(lines) + "\n").splitlines())
    if before != after:
        print(f"  CIDR prune: {before} → {after} ({before - after} redundant)")

    # Stage beside the destination so a failed validation leaves the old file intact.
    destination = target_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".rules-", suffix=".tmp", delete=False) as staging:
        target_path = Path(staging.name)
    try:
        rules = [l for l in pruned_lines if l.strip() and not l.strip().startswith("#")]
        errors = validate_rule_file(rules, target_name)
        if errors:
            print(f"VALIDATION FAILED for {target_name}:")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)

        # Write final file with header
        rule_count = len(rules)
        update_time = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S +0800")

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(f"# NAME: {display_name}\n")
            f.write(f"# AUTHOR: {AUTHOR_NAME}\n")
            f.write(f"# REPO: {REPO_URL}\n")
            f.write(f"# UPDATED: {update_time}\n")
            f.write(f"# FORMAT: Surge Ruleset\n")
            f.write(f"# TOTAL: {rule_count}\n")
            f.write("\n")
            f.writelines(line + "\n" for line in pruned_lines)
        target_path.chmod(destination.stat().st_mode & 0o777 if destination.exists() else 0o644)
        target_path.replace(destination)
    finally:
        target_path.unlink(missing_ok=True)
    record = snapshot_path(destination.parent, target_name)
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(json.dumps({"ruleset": target_name, "sources": records}, indent=2) + "\n",
                      encoding="utf-8")


def prune_global_first_match_overlaps():
    """Remove rules from Global.list that appear in earlier-matched rulesets."""
    target_path = RULE_DIR / "Global.list"
    if not target_path.exists():
        return

    # Collect all earlier rules
    overlap: set[str] = set()
    for ruleset in GLOBAL_OVERLAP_RULESETS:
        path = RULE_DIR / ruleset
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.startswith("#") and line.strip():
                    overlap.add(line.lower())

    # Filter Global.list
    lines = target_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("#") or not line.strip():
            out.append(line)
        elif line.lower() not in overlap:
            out.append(line)

    # Update TOTAL
    rule_count = sum(1 for l in out if not l.startswith("#") and l.strip())
    result = []
    for line in out:
        if line.startswith("# TOTAL:"):
            result.append(f"# TOTAL: {rule_count}")
        else:
            result.append(line)

    # Validate before writing the pruned Global file
    rules = [l for l in result if not l.startswith("#") and l.strip()]
    errors = validate_rule_file(rules, "Global.list")
    if errors:
        print("VALIDATION FAILED for Global.list after pruning:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    target_path.write_text("\n".join(result) + "\n", encoding="utf-8")


# ── Main ────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    global RULE_DIR, OFFLINE
    parser = argparse.ArgumentParser(description="Generate Surge rulesets from upstream sources.")
    parser.add_argument("--check", action="store_true",
                        help="generate without publishing; exit 1 if any ruleset would change")
    parser.add_argument("--offline", action="store_true",
                        help="rebuild from the snapshots pinned in Rule/.sources instead of the network")
    parser.add_argument("--rulesets", nargs="+", metavar="NAME",
                        help="rulesets to rebuild, e.g. SocialMedia.list (default: CHANGED_RULESETS)")
    args = parser.parse_args([] if argv is None else argv)

    RULE_DIR.mkdir(parents=True, exist_ok=True)
    MANUAL_DIR.mkdir(parents=True, exist_ok=True)

    is_workflow_dispatch = os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
    if args.rulesets is not None:
        unknown = [name for name in args.rulesets if name not in RULE_SPECS]
        if unknown:
            raise ValueError(f"Unknown rulesets: {', '.join(unknown)}")
        changed_rulesets: list[str] = args.rulesets
    else:
        changed_raw = os.environ.get("CHANGED_RULESETS", "[]")
        try:
            changed_rulesets = json.loads(changed_raw)
        except (json.JSONDecodeError, TypeError) as exc:
            raise ValueError("CHANGED_RULESETS must be a JSON array of known ruleset names") from exc
        if not isinstance(changed_rulesets, list) or any(
            not isinstance(name, str) or name not in RULE_SPECS for name in changed_rulesets
        ):
            raise ValueError("CHANGED_RULESETS must be a JSON array of known ruleset names")

    # Global is stored after overlap pruning. Re-pruning that old file cannot
    # restore rules removed by a service update; regenerate from its sources.
    # Resolve this here as well as in the upstream checker so direct CLI calls
    # cannot accidentally omit the dependency.
    selected_rulesets = expand_ruleset_dependencies(changed_rulesets)

    destination = RULE_DIR
    # Preserve unselected rules for Global overlap pruning. All generation and
    # validation run off to the side; a later source failure cannot publish an
    # earlier target. Manual input stays in its original read-only location.
    with tempfile.TemporaryDirectory(prefix='.generate-', dir=destination.parent) as temporary:
        staged = Path(temporary)
        for path in destination.glob('*.list'):
            shutil.copy2(path, staged / path.name)
        if (destination / SNAPSHOT_DIR).is_dir():
            shutil.copytree(destination / SNAPSHOT_DIR, staged / SNAPSHOT_DIR)
        processed: list[str] = []
        try:
            RULE_DIR = staged
            OFFLINE = args.offline
            for target_name, (display_name, sources) in RULE_SPECS.items():
                if should_process(target_name, selected_rulesets, is_workflow_dispatch):
                    print(f"Processing {target_name} ...")
                    process_rule(target_name, display_name, sources)
                    processed.append(target_name)
            if processed:
                print("Pruning Global.list first-match overlaps ...")
                prune_global_first_match_overlaps()
        finally:
            RULE_DIR = destination
            OFFLINE = False
        changed: dict[Path, bytes] = {}
        pins: dict[Path, bytes] = {}
        backfills: list[str] = []
        for p in sorted(staged.glob('*.list')) if processed else ():
            current = destination / p.name
            new = p.read_bytes()
            record = snapshot_path(destination, p.name)
            is_changed = content_changed(current.read_bytes() if current.exists() else None, new)
            if is_changed:
                changed[current] = new
            if p.name not in processed:
                # Only the Global post-pass touches unprocessed files; their pins stay as published.
                continue
            if is_changed:
                pins[record] = snapshot_path(staged, p.name).read_bytes()
            elif not record.exists():
                # Backfill: the unchanged published file was reproduced from these inputs.
                pins[record] = snapshot_path(staged, p.name).read_bytes()
                backfills.append(record.name)
        if args.check:
            for path in changed:
                print(f"Would change: {path.name}")
            for name in backfills:
                print(f"Would record snapshot: {name}")
            print(f"Check: {len(changed)} ruleset(s) would change.")
            return 1 if changed else 0
        if changed or pins:
            publish_files(destination, {**changed, **pins})

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
