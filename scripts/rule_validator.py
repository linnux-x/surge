"""Shared Surge rule validation logic.

Used by both generate_rules.py (inline validation during generation)
and validate_surge_repo.py (post-generation repository checks).

Single function: validate_rule_file(path, lines) → list of error strings.
"""

from __future__ import annotations

import ipaddress
import re
from collections import Counter
from pathlib import Path

ALLOWED_TYPES = {
    "DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-WILDCARD",
    "IP-CIDR", "IP-CIDR6", "IP-ASN",
    "GEOIP", "USER-AGENT", "PROCESS-NAME", "URL-REGEX",
    "AND", "OR", "NOT",
}
OPTION_TOKENS = {"no-resolve", "extended-matching"}
SUKKAW_MARKER = "7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe"

SHARED_CDN_PARENTS = {
    "akadns.net", "akamaiedge.net", "akamaihd.net", "akamaized.net",
    "azureedge.net", "b-cdn.net", "cdn77.org", "cloudfront.net",
    "edgekey.net", "edgesuite.net", "fastly.net",
}

SHARED_THIRD_PARTY_SUFFIXES = {
    "cookielaw.org", "onetrust.com", "adobedtm.com",
    "braze.com", "newrelic.com", "nr-data.net",
    "optimizely.com", "segment.io", "sentry.io",
}
SHARED_THIRD_PARTY_DOMAINS = {"js-agent.newrelic.com"}

SHARED_THIRD_PARTY_EXEMPT = {
    "Global.list", "GlobalMedia.list", "CDN.list", "Direct.list",
    "China.list", "China_IP.list", "ChinaMedia.list", "Download.list",
}

PAYPAL_CN_DOMAINS = {
    "anfutong.cn", "anfutong.com", "anfutong.com.cn",
    "beibao.cn", "beibao.com", "beibao.com.cn",
    "paypal.cn", "paypal.com.cn", "paypal.net.cn", "paypal.org.cn",
    "paypal-corp.cn", "paypal-corp.com.cn",
    "paypal-notice.cn", "paypal-notice.com.cn",
    "paypalcommunity.cn", "paypalhere.cn", "paypalhere.com.cn",
    "paypalobjects.cn", "paypalobjects.com.cn",
    "xoom.net.cn", "xn--bnq297cix3a.cn",
}

NON_CHINA_FALLBACK_PATTERNS = [
    re.compile(r"^domain,rthklive2-lh[.]akamaihd[.]net$", re.I),
    re.compile(
        r"^domain-suffix,(bilibili[.]tv|biliintl[.]co|biliintl[.]com|"
        r"himalaya[.]com|iflix[.]com|iq[.]com|joox[.]com|"
        r"kwai-group[.]com|kwai[.]com|kwai[.]net|kwaicdn[.]com|"
        r"nba[.]com|snssdk[.]com|tiktokd[.]net|tiktokd[.]org|"
        r"wetv[.]vip|wetvinfo[.]com)$",
        re.I,
    ),
    re.compile(r"^user-agent,(himalaya[*]|tiktok[*])$", re.I),
]


def validate_rule_file(lines: list[str], target_name: str) -> list[str]:
    """Validate a rule file's content against Surge syntax and project policies.

    Args:
        lines: Non-comment, non-empty lines from the rule file.
        target_name: Filename (e.g. 'AI.list', 'China.list').

    Returns:
        List of error strings (empty = valid).
    """
    errors: list[str] = []

    # Header check
    if any("Current Project Baseline" in line for line in lines[:5]):
        errors.append(f"{target_name}: obsolete Current Project Baseline section")

    counts = Counter(r.lower() for r in lines)
    duplicates = [r for r, cnt in counts.items() if cnt > 1]
    if duplicates:
        errors.append(f"{target_name}: {len(duplicates)} duplicate rules, examples: {duplicates[:5]}")

    networks: list[tuple[int, ipaddress._BaseNetwork]] = []
    all_networks: set[ipaddress._BaseNetwork] = set()

    for index, rule in enumerate(lines, start=1):
        parts = [p.strip() for p in rule.split(",")]
        rule_type = parts[0].upper()
        low = rule.lower()

        if rule_type not in ALLOWED_TYPES:
            errors.append(f"{target_name}:{index} unsupported rule type: {rule}")
            continue

        if SUKKAW_MARKER in low:
            errors.append(f"{target_name}:{index} SukkaW marker leaked: {rule}")

        # Domain checks
        if rule_type in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-WILDCARD"} and len(parts) >= 2:
            value = parts[1]
            if value != value.lower():
                errors.append(f"{target_name}:{index} domain not lowercase: {rule}")
            if "://" in value or "/" in value:
                errors.append(f"{target_name}:{index} domain contains URL scheme/path: {rule}")

        # Policy name check
        if rule_type in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-WILDCARD",
                         "IP-CIDR", "IP-CIDR6", "IP-ASN",
                         "USER-AGENT", "PROCESS-NAME"}:
            if len(parts) >= 3 and parts[2].lower() not in OPTION_TOKENS:
                errors.append(f"{target_name}:{index} possible policy name: {rule}")

        # Numeric DOMAIN-KEYWORD
        if rule_type == "DOMAIN-KEYWORD" and len(parts) >= 2 and \
                re.match(r"^[0-9]+([.][0-9]+){1,3}[.]?$", parts[1]):
            errors.append(f"{target_name}:{index} numeric DOMAIN-KEYWORD: {rule}")

        # ── Project-specific policies ──

        if target_name == "China.list" and rule_type in {"IP-CIDR", "IP-CIDR6", "IP-ASN"}:
            errors.append(f"{target_name}:{index} IP rule in China.list: {rule}")
        if target_name == "China_IP.list" and rule_type in {"IP-CIDR", "IP-CIDR6", "IP-ASN"} and \
                ",no-resolve" in low:
            errors.append(f"{target_name}:{index} no-resolve in China_IP.list: {rule}")
        if target_name != "China_IP.list" and rule_type in {"IP-CIDR", "IP-CIDR6", "IP-ASN"} and \
                ",no-resolve" not in low:
            errors.append(f"{target_name}:{index} missing no-resolve: {rule}")

        if target_name == "Microsoft.list" and re.search(r"github|ghcr[.]io", low):
            errors.append(f"{target_name}:{index} GitHub in Microsoft.list: {rule}")
        if target_name != "Speedtest.list" and \
                re.search(r"(^|,)([^,]*[.])?fast[.]com(,|$)", low):
            errors.append(f"{target_name}:{index} fast.com outside Speedtest.list: {rule}")
        if target_name != "CDN.list" and rule_type == "DOMAIN-SUFFIX" and \
                len(parts) >= 2 and parts[1].lower() in SHARED_CDN_PARENTS:
            errors.append(f"{target_name}:{index} shared CDN outside CDN.list: {rule}")
        if target_name == "China.list" and \
                any(p.search(low) for p in NON_CHINA_FALLBACK_PATTERNS):
            errors.append(f"{target_name}:{index} non-China media in China.list: {rule}")

        # ── Shared third-party infrastructure ──
        if (target_name not in SHARED_THIRD_PARTY_EXEMPT and
                rule_type in {"DOMAIN", "DOMAIN-SUFFIX"} and len(parts) >= 2):
            domain_val = parts[1].lower()

            if domain_val in SHARED_THIRD_PARTY_DOMAINS:
                errors.append(f"{target_name}:{index} shared third-party domain: {rule}")
            if rule_type == "DOMAIN-SUFFIX" and domain_val in SHARED_THIRD_PARTY_SUFFIXES:
                errors.append(f"{target_name}:{index} shared third-party suffix: {rule}")
            elif rule_type == "DOMAIN-SUFFIX":
                for suffix in SHARED_THIRD_PARTY_SUFFIXES:
                    if domain_val.endswith(f".{suffix}"):
                        sub = domain_val[:-(len(suffix) + 1)]
                        first_label = sub.split(".")[0].lower()
                        is_opaque = (
                            first_label.isdigit() or
                            all(c in "0123456789abcdef" for c in first_label) or
                            (len(first_label) <= 6 and
                             any(c.isdigit() for c in first_label) and
                             not first_label.isalpha())
                        )
                        if is_opaque:
                            errors.append(f"{target_name}:{index} opaque shared subdomain: {rule}")
                        break

        # ── PayPal CN domains ──
        if target_name == "PayPal.list" and rule_type in {"DOMAIN", "DOMAIN-SUFFIX"} and \
                len(parts) >= 2:
            domain_val = parts[1].lower()
            if domain_val in PAYPAL_CN_DOMAINS:
                errors.append(f"{target_name}:{index} PayPal CN domain: {rule}")
            elif rule_type == "DOMAIN-SUFFIX":
                for cn_dom in PAYPAL_CN_DOMAINS:
                    if domain_val == cn_dom or domain_val.endswith(f".{cn_dom}"):
                        errors.append(f"{target_name}:{index} PayPal CN domain: {rule}")
                        break

        # ── Opaque CDN edge nodes ──
        if (target_name != "CDN.list" and target_name not in SHARED_THIRD_PARTY_EXEMPT and
                rule_type == "DOMAIN" and len(parts) >= 2):
            domain_val = parts[1].lower()
            for parent in SHARED_CDN_PARENTS:
                if domain_val.endswith(f".{parent}") or domain_val == parent:
                    sub = domain_val[:-len(parent) - 1] if domain_val.endswith(f".{parent}") else ""
                    first_label = sub.split(".")[0].lower() if sub else ""
                    is_opaque = (
                        first_label.isdigit() or
                        all(c in "0123456789abcdef" for c in first_label) or
                        (len(first_label) <= 6 and
                         any(c.isdigit() for c in first_label) and
                         not first_label.isalpha())
                    )
                    if is_opaque:
                        errors.append(f"{target_name}:{index} opaque CDN node: {rule}")
                    break

        # ── CIDR checks ──
        if rule_type in {"IP-CIDR", "IP-CIDR6"} and len(parts) >= 2:
            try:
                network = ipaddress.ip_network(parts[1], strict=False)
            except ValueError as exc:
                errors.append(f"{target_name}:{index} invalid CIDR {parts[1]!r}: {exc}")
            else:
                networks.append((index, network))
                all_networks.add(network)

    # ── CIDR redundancy ──
    for index, network in networks:
        for prefix in range(network.prefixlen):
            try:
                if network.supernet(new_prefix=prefix) in all_networks:
                    errors.append(f"{target_name}:{index} redundant CIDR: {network}")
                    break
            except ValueError:
                pass

    return errors


def parse_total_header(path: Path) -> int | None:
    """Extract # TOTAL: from a rule file's header."""
    try:
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines()[:20]:
            m = re.match(r"#\s*TOTAL:\s*(\d+)\s*$", raw)
            if m:
                return int(m.group(1))
    except (OSError, UnicodeDecodeError):
        pass
    return None


def non_comment_rules(path_or_lines: Path | list[str]) -> list[str]:
    """Extract non-comment, non-empty lines from a file path or list of lines."""
    if isinstance(path_or_lines, Path):
        lines = path_or_lines.read_text(encoding="utf-8", errors="replace").splitlines()
    else:
        lines = path_or_lines
    return [s.strip() for s in lines if s.strip() and not s.strip().startswith("#")]
