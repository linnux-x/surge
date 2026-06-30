#!/usr/bin/env python3
"""Generate Surge rulesets from upstream sources.

Replaces the inline bash in .github/workflows/auto-rules.yml with Python.
Reads CHANGED_RULESETS from environment (JSON array) or processes all rulesets
on workflow_dispatch (GITHUB_EVENT_NAME=workflow_dispatch).

Supports: manual rules, exclude files, domainset/cidr conversion, guardrails,
dedup, CIDR pruning, validation, and Global overlap pruning.
"""

import json
import ipaddress
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# Ensure scripts/ is on the path so 'import sources' works
_scripts_dir = Path(__file__).resolve().parent
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from sources import RULE_SPECS
from rule_validator import validate_rule_file

# ── Constants ─────────────────────────────────────────────────────────────

SUKKA_MARKER = re.compile(r"7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset[.]skk[.]moe", re.IGNORECASE)
RULE_DIR = Path("Rule")
MANUAL_DIR = RULE_DIR / "Manual"
REPO_URL = os.environ.get("REPO_URL", "https://github.com/linnux-x/surge")
AUTHOR_NAME = os.environ.get("AUTHOR_NAME", "linnux-x")
CURL_RETRY = ["--retry", "3", "--retry-delay", "5"]


# ── Helpers ────────────────────────────────────────────────────────────────

def should_process(target: str, changed_rulesets: list[str], force_all: bool) -> bool:
    """Determine if a ruleset should be processed this run."""
    if force_all:
        return True
    return target in changed_rulesets


def clean_source(lines: list[str]) -> list[str]:
    """Strip comments, whitespace, and SukkaW marker lines."""
    out = []
    for line in lines:
        line = line.rstrip("\r\n").rstrip()
        # Remove inline trailing comment
        line = re.sub(r"\s+#.*$", "", line)
        if not line or line.startswith("#"):
            continue
        if SUKKA_MARKER.search(line):
            continue
        out.append(line)
    return out


def convert_domainset(lines: list[str]) -> list[str]:
    """Convert domainset format (one domain per line) to Surge DOMAIN-SUFFIX/DOMAIN."""
    out = []
    for line in lines:
        if not line:
            continue
        low = line.lower()
        if low.startswith("."):
            out.append(f"DOMAIN-SUFFIX,{low[1:]}")
        elif re.match(r"^[A-Za-z0-9_.-]+\.[A-Za-z0-9.-]+$", line):
            out.append(f"DOMAIN,{low}")
        else:
            out.append(low)
    return out


def convert_cidr(lines: list[str]) -> list[str]:
    """Convert bare CIDR lines to Surge IP-CIDR/IP-CIDR6."""
    out = []
    for line in lines:
        if not line:
            continue
        if re.match(r"^\d+\.\d+\.\d+\.\d+/\d+$", line):
            out.append(f"IP-CIDR,{line}")
        elif re.match(r"^[0-9A-Fa-f:]+/\d+$", line):
            out.append(f"IP-CIDR6,{line.lower()}")
        else:
            out.append(line)
    return out


def filter_candidates(lines: list[str], exclude_file: Path | None) -> list[str]:
    """Remove lines exactly matching entries in exclude file."""
    if not exclude_file or not exclude_file.is_file() or exclude_file.stat().st_size == 0:
        return lines
    patterns = set()
    for raw in exclude_file.read_text(encoding="utf-8").splitlines():
        raw = raw.rstrip("\r").strip()
        if raw and not raw.startswith("#"):
            patterns.add(raw)
    if not patterns:
        return lines
    return [l for l in lines if l not in patterns]


def apply_project_guardrails(target_name: str, lines: list[str]) -> list[str]:
    """Apply repository-specific guardrails."""
    out = lines[:]

    # Surge GEOIP is documented for ISO country codes only. Convert the common
    # community shorthand for Google-owned IP ranges to Surge-native IP-ASN.
    out = [
        "IP-ASN,15169" if re.match(r"^GEOIP,GOOGLE$", l, re.IGNORECASE) else l
        for l in out
    ]

    if target_name == "Microsoft.list":
        out = [l for l in out if not re.search(r"github|ghcr\.io", l, re.IGNORECASE)]
    elif target_name in ("Netflix.list", "GlobalMedia.list", "Global.list"):
        out = [l for l in out if not re.search(r"(^|,)([^,]*\.)?fast\.com(,|$)", l, re.IGNORECASE)]
    elif target_name == "Google.list":
        out = [l for l in out if not re.search(
            r"youtube|ytimg\.com|googlevideo\.com|youtubei\.googleapis\.com", l, re.IGNORECASE)]
    elif target_name == "China.list":
        out = [l for l in out if not re.match(r"^(IP-CIDR|IP-CIDR6|IP-ASN),", l, re.IGNORECASE)]
    elif target_name == "China_IP.list":
        out = [re.sub(r",(no-resolve|NO-RESOLVE)", "", l, flags=re.IGNORECASE) for l in out]

    # Remove numeric DOMAIN-KEYWORD fragments
    out = [l for l in out if not re.match(r"^DOMAIN-KEYWORD,\d+(\.\d+){1,3}\.?$", l, re.IGNORECASE)]

    # Add no-resolve to IP rules (except China_IP.list)
    if target_name != "China_IP.list":
        out = _add_no_resolve(out)

    return out


def _add_no_resolve(lines: list[str]) -> list[str]:
    """Ensure all IP rules have no-resolve (except China_IP.list)."""
    out = []
    for line in lines:
        if re.match(r"^(IP-CIDR|IP-CIDR6|IP-ASN),", line, re.IGNORECASE):
            if not re.search(r",no-resolve($|,)", line, re.IGNORECASE):
                line += ",no-resolve"
        out.append(line)
    return out


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

    Built into generate_rules.py (was scripts/prune_cidr.py).
    Returns (before, after) counts; prints summary if pruning occurred.
    """
    lines = filepath.read_text(encoding="utf-8").splitlines()

    cidrs: list[tuple[int, ipaddress.IPv4Network | ipaddress.IPv6Network]] = []
    all_nets: set[ipaddress.IPv4Network | ipaddress.IPv6Network] = set()

    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = [p.strip() for p in stripped.split(",")]
        if len(parts) < 2 or parts[0].upper() not in {"IP-CIDR", "IP-CIDR6"}:
            continue
        try:
            network = ipaddress.ip_network(parts[1], strict=False)
        except ValueError:
            continue
        cidrs.append((index, network))
        all_nets.add(network)

    before = len(cidrs)
    remove: set[int] = set()

    for index, network in cidrs:
        for prefix in range(network.prefixlen):
            try:
                if network.supernet(new_prefix=prefix) in all_nets:
                    remove.add(index)
                    break
            except ipaddress.NetmaskValueError:
                break

    if remove:
        filepath.write_text(
            "\n".join(line for i, line in enumerate(lines) if i not in remove) + "\n",
            encoding="utf-8",
        )

    after = before - len(remove)
    if before != after:
        print(f"  CIDR prune: {before} → {after} ({len(remove)} redundant)")


# ── Processing ──────────────────────────────────────────────────────────────

def fetch_source(url: str) -> list[str]:
    """Fetch a remote source and return lines."""
    result = subprocess.run(
        ["curl", "-fsSL", *CURL_RETRY, url],
        capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


def process_rule(target_name: str, display_name: str, sources: list[tuple[str, str, str | None]]):
    """Generate a single ruleset file from its sources."""
    target_path = RULE_DIR / target_name
    filename_no_ext = target_name.rsplit(".", 1)[0]
    exclude_file = MANUAL_DIR / f"{filename_no_ext}.exclude.txt"

    lines: list[str] = []

    # Manual rules first (highest priority)
    manual_file = MANUAL_DIR / f"{filename_no_ext}.txt"
    if manual_file.is_file():
        lines.append("# ======= Manual Rules ========")
        lines.extend(manual_file.read_text(encoding="utf-8").replace("\r", "").splitlines())
        lines.append("")

    # Upstream sources
    for source_name, source_url, source_format in sources:
        raw = fetch_source(source_url)
        cleaned = clean_source(raw)

        if source_format == "domainset":
            converted = convert_domainset(cleaned)
        elif source_format == "cidr":
            converted = convert_cidr(cleaned)
        else:
            converted = cleaned

        filtered = filter_candidates(converted, exclude_file)

        lines.append(f"# ======= {source_name} ========")
        lines.extend(filtered)
        lines.append("")

    # Guardrails, dedup, CIDR prune
    lines = apply_project_guardrails(target_name, lines)
    lines = dedupe_preserve_order(lines)

    # Write to file for CIDR pruning (needs physical file)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    prune_redundant_cidr(target_path)

    # Read back once: validate rules + get pruned lines for final write
    pruned_lines = target_path.read_text(encoding="utf-8").splitlines()
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


def prune_global_first_match_overlaps():
    """Remove rules from Global.list that appear in earlier-matched rulesets."""
    target_path = RULE_DIR / "Global.list"
    if not target_path.exists():
        return

    earlier_rulesets = [
        "WeChat.list", "Speedtest.list", "AI.list", "Apple_CN.list", "Apple.list",
        "Microsoft_CDN.list", "Microsoft.list", "Telegram.list", "Download.list",
        "Game.list", "YouTube.list", "TikTok.list", "SocialMedia.list",
        "PayPal.list", "Google.list", "Netflix.list", "Disney.list",
        "ChinaMedia.list", "GlobalMedia.list", "CDN.list",
    ]

    # Collect all earlier rules
    overlap: set[str] = set()
    for ruleset in earlier_rulesets:
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

    target_path.write_text("\n".join(result) + "\n", encoding="utf-8")

    # Validate after pruning
    rules = [l for l in result if not l.startswith("#") and l.strip()]
    errors = validate_rule_file(rules, "Global.list")
    if errors:
        print("VALIDATION FAILED for Global.list after pruning:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    RULE_DIR.mkdir(parents=True, exist_ok=True)
    MANUAL_DIR.mkdir(parents=True, exist_ok=True)

    is_workflow_dispatch = os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
    changed_raw = os.environ.get("CHANGED_RULESETS", "[]")
    try:
        changed_rulesets: list[str] = json.loads(changed_raw)
    except (json.JSONDecodeError, TypeError):
        changed_rulesets = []

    processed = False
    for target_name, (display_name, sources) in RULE_SPECS.items():
        if should_process(target_name, changed_rulesets, is_workflow_dispatch):
            print(f"Processing {target_name} ...")
            process_rule(target_name, display_name, sources)
            processed = True

    # Prune Global overlaps if anything was processed
    if processed:
        print("Pruning Global.list first-match overlaps ...")
        prune_global_first_match_overlaps()

    print("Done.")


if __name__ == "__main__":
    main()
