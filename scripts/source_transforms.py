"""Shared source transformations for generation and contribution audits.

Keep format conversion separate from exclusions and project guardrails: manual
rules bypass upstream exclusions, and generation applies guardrails after merge.
This module performs no fetching or output writes.
"""
from __future__ import annotations

import ipaddress
import json
import re
from pathlib import Path
from typing import Optional

from policy import (
    CHINA_FALLBACK_EXCLUDE_PATTERNS,
    FASTCOM_RE,
    FASTCOM_RULESETS,
    GITHUB_RE,
    HOST_SCOPED_RULESETS,
    SHARED_INFRA_EXEMPT_FILES,
    SHARED_THIRD_PARTY_SUFFIXES,
    YOUTUBE_RE,
    violates_routing_boundary,
)
from rule_validator import SUKKAW_MARKER
from exclusions import exclusion_key, read_exclusions
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


def convert_chatgpt_voice(lines: list[str]) -> list[str]:
    """Match the official Voice prefixes only on UDP 3478."""
    payload = json.loads("\n".join(lines))
    prefixes = payload.get("prefixes") if isinstance(payload, dict) else None
    if not isinstance(prefixes, list) or not prefixes:
        raise ValueError("ChatGPT Voice metadata must contain a non-empty prefixes array")

    networks = set()
    for prefix in prefixes:
        if not isinstance(prefix, dict) or len(prefix.keys() & {"ipv4Prefix", "ipv6Prefix"}) != 1:
            raise ValueError("ChatGPT Voice entry must contain exactly one IP prefix")
        field = "ipv4Prefix" if "ipv4Prefix" in prefix else "ipv6Prefix"
        value = prefix[field]
        if not isinstance(value, str) or "/" not in value:
            raise ValueError("ChatGPT Voice entry must use CIDR notation")
        network = ipaddress.ip_network(value)
        if network.version != (4 if field == "ipv4Prefix" else 6) or not network.is_global:
            raise ValueError(f"Invalid ChatGPT Voice prefix: {value}")
        networks.add(network)

    return [
        f"AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR{'6' if network.version == 6 else ''},{network},no-resolve))"
        for network in sorted(networks, key=ipaddress.get_mixed_type_key)
    ]


def filter_candidates(lines: list[str], exclude_file: Optional[Path]) -> list[str]:
    """Remove explicitly typed exclusions, including domain option variants."""
    if not exclude_file or not exclude_file.is_file() or exclude_file.stat().st_size == 0:
        return lines
    patterns = {exclusion_key(rule) for rule in read_exclusions(exclude_file)}
    if not patterns:
        return lines
    return [line for line in lines if exclusion_key(line) not in patterns]


def apply_project_guardrails(target_name: str, lines: list[str]) -> list[str]:
    """Apply repository-specific guardrails."""
    out = lines[:]

    # Filter SukkaW watermark domains before anything else
    out = [l for l in out if not SUKKAW_MARKER.search(l)]
    if target_name not in FASTCOM_RULESETS:
        out = [l for l in out if not FASTCOM_RE.search(l)]

    # Surge GEOIP is documented for ISO country codes only. Convert the common
    # community shorthand for Google-owned IP ranges to Surge-native IP-ASN.
    out = [
        "IP-ASN,15169" if re.match(r"^GEOIP,GOOGLE$", l, re.IGNORECASE) else l
        for l in out
    ]

    if target_name == "Microsoft.list":
        out = [l for l in out if not GITHUB_RE.search(l)]
    elif target_name == "Google.list":
        # Chrome and YouTube share this Google account endpoint.
        out = [line for line in out
               if line == "DOMAIN,accounts.youtube.com" or not YOUTUBE_RE.search(line)]
    elif target_name == "China.list":
        out = [l for l in out if not re.match(r"^(IP-CIDR|IP-CIDR6|IP-ASN),", l, re.IGNORECASE)]
        out = [
            line for line in out
            if not any(pattern.search(line.lower()) for pattern in CHINA_FALLBACK_EXCLUDE_PATTERNS)
        ]
    elif target_name == "China_IP.list":
        out = [re.sub(r",(no-resolve|NO-RESOLVE)", "", l, flags=re.IGNORECASE) for l in out]

    if target_name in HOST_SCOPED_RULESETS or target_name == "AI.list":
        out = [
            line for line in out
            if not violates_routing_boundary(target_name, line)
        ]

    # The strict validator rejects whole shared identity, telemetry, and consent
    # suffixes in service-specific rulesets. Enforce the same invariant before
    # validation so a source-format or exclusion-path regression cannot block
    # an otherwise safe incremental generation run.
    if target_name not in SHARED_INFRA_EXEMPT_FILES:
        out = [
            line for line in out
            if not (
                line.upper().startswith("DOMAIN-SUFFIX,")
                and line.split(",", 2)[1].lower() in SHARED_THIRD_PARTY_SUFFIXES
            )
        ]

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
    if source_format == "chatgpt-voice-json":
        return convert_chatgpt_voice(lines)
    cleaned = clean_source(lines)
    if source_format == "domainset":
        return convert_domainset(cleaned)
    if source_format == "cidr":
        return convert_cidr(cleaned)
    return cleaned
