"""Shared source transformations for generation and contribution audits.

Keep format conversion separate from exclusions and project guardrails: manual
rules bypass upstream exclusions, and generation applies guardrails after merge.
This module performs no fetching or output writes.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from policy import FASTCOM_RE, GITHUB_RE, YOUTUBE_RE
from rule_validator import SUKKAW_MARKER
from speedtest_sources import convert_speedtest

SUKKA_MARKER = re.compile(r"7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset[.]skk[.]moe", re.IGNORECASE)


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
        # Loon rules commonly include a space after the comma. Surge rule
        # validators require compact comma-separated fields; normalize it at
        # ingestion so the immutable source snapshot remains byte-for-byte
        # auditable while generated output is valid Surge syntax.
        out.append(re.sub(r",\s+", ",", line))
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


def filter_candidates(lines: list[str], exclude_file: Optional[Path]) -> list[str]:
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

    # Filter SukkaW watermark domains before anything else
    out = [l for l in out if not SUKKAW_MARKER.search(l)]

    # Surge GEOIP is documented for ISO country codes only. Convert the common
    # community shorthand for Google-owned IP ranges to Surge-native IP-ASN.
    out = [
        "IP-ASN,15169" if re.match(r"^GEOIP,GOOGLE$", l, re.IGNORECASE) else l
        for l in out
    ]

    if target_name == "Microsoft.list":
        out = [l for l in out if not GITHUB_RE.search(l)]
    elif target_name in ("Netflix.list", "GlobalMedia.list", "Global.list"):
        out = [l for l in out if not FASTCOM_RE.search(l)]
    elif target_name == "Google.list":
        out = [l for l in out if not YOUTUBE_RE.search(l)]
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


def convert_source(lines: list[str], source_format: str | None) -> list[str]:
    """Clean and convert one upstream response, preserving order and duplicates.

    Empty-source rejection belongs to the generator; an audit may quantify an
    empty text source. Structured formats retain their own schema/empty checks.
    """
    if source_format and source_format.startswith("speedtest-"):
        return convert_speedtest(lines, source_format)
    cleaned = clean_source(lines)
    if source_format == "domainset":
        return convert_domainset(cleaned)
    if source_format == "cidr":
        return convert_cidr(cleaned)
    return cleaned
