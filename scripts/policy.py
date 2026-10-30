"""Canonical routing-policy constants shared across the pipeline.

Single source of truth for policy knowledge that was previously duplicated
across three scripts:

- generate_rules.py  — generation-time transforms (filters upstream lines)
- rule_validator.py  — commit-blocking validation (strict tier)
- audit_rules.py     — online audit (broad tier, WARN only)

The broad audit tier is built as a superset of the strict tiers so the two
can never drift apart: adding a suffix to a strict set automatically makes
the audit aware of it.
"""

from __future__ import annotations

import re

# ── Service-boundary filters ───────────────────────────────────────────────
# GitHub never belongs to Microsoft.list (repo policy: plain GitHub → Global,
# Copilot → AI, release downloads → CDN).
GITHUB_RE = re.compile(r"github|ghcr[.]io", re.IGNORECASE)

# fast.com belongs to Speedtest.list only.
FASTCOM_RE = re.compile(r"(^|,)([^,]*[.])?fast[.]com(,|$)", re.IGNORECASE)

# YouTube domains never belong to Google.list (they live in YouTube.list).
YOUTUBE_RE = re.compile(
    r"youtube|ytimg[.]com|googlevideo[.]com|youtubei[.]googleapis[.]com",
    re.IGNORECASE,
)

# China fallback must not absorb overseas media services or a shared CDN parent.
# Keep these exact typed rules in the canonical policy so generation removes a
# bad upstream entry before strict validation, rather than relying only on a
# matching line in China.exclude.txt.
CHINA_FALLBACK_EXCLUDE_PATTERNS = (
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
    re.compile(r"^domain-suffix,akadns[.]net$", re.I),
)

# ── Broad DOMAIN-KEYWORD review ────────────────────────────────────────────
# DOMAIN-KEYWORD is a substring match. Single source for rule_validator.py
# (WARN on generated files) and validate_override_manifest.py (Manual files
# need an entry-level approval). Keywords that are brand-generic, or short
# enough to occur inside unrelated hosts, must be reviewed before use:
#   siri  → volcsirius.com, applesiri.cn   gmail → suningmail.com
#   1drv  → 51drv.com
RISKY_DOMAIN_KEYWORDS: frozenset[str] = frozenset({
    "amazon", "apple", "google", "microsoft", "java",
    "cdn", "cloud", "api",
    "siri", "gmail", "1drv",
})
# Any keyword this short is treated as risky unless explicitly reviewed below.
SHORT_DOMAIN_KEYWORD_MAX_LEN = 4
# Short keywords already reviewed in their current file and kept on purpose.
# Adding one here is a routing decision: record why next to it.
REVIEWED_SHORT_DOMAIN_KEYWORDS: frozenset[str] = frozenset({
    "porn",  # Global.list: adult-site coverage; collateral is limited to similar sites
    "avtb",  # Global.list: adult-site mirror family with rotating domains
})


def is_risky_domain_keyword(keyword: str) -> bool:
    """True when a DOMAIN-KEYWORD value needs routing review."""
    keyword = keyword.strip().lower()
    if keyword in RISKY_DOMAIN_KEYWORDS:
        return True
    return (len(keyword) <= SHORT_DOMAIN_KEYWORD_MAX_LEN
            and keyword not in REVIEWED_SHORT_DOMAIN_KEYWORDS)


# ── Shared infrastructure — strict tier (blocks commit via rule_validator) ──

# Shared CDN parent domains: too broad to route per-service; CDN.list only.
SHARED_CDN_PARENTS = {
    "akadns.net", "akamaiedge.net", "akamaihd.net", "akamaized.net",
    "azureedge.net", "b-cdn.net", "cdn77.org", "cloudfront.net",
    "edgekey.net", "edgesuite.net", "fastly.net",
}

# Shared telemetry / consent / identity platforms: never valid as whole-domain
# service rules. Service-scoped subdomains (e.g. DOMAIN,anthropic.auth0.com)
# remain allowed.
SHARED_THIRD_PARTY_SUFFIXES = {
    "auth0.com",
    "cookielaw.org", "onetrust.com", "adobedtm.com",
    "braze.com", "newrelic.com", "nr-data.net",
    "optimizely.com", "segment.io", "sentry.io",
}
SHARED_THIRD_PARTY_DOMAINS = {"js-agent.newrelic.com"}

# Aggregate rulesets exempt from shared-infrastructure checks.
SHARED_INFRA_EXEMPT_FILES = {
    "Global.list", "GlobalMedia.list", "CDN.list", "Direct.list",
    "China.list", "China_IP.list", "ChinaMedia.list", "Download.list",
}

# ── Shared infrastructure — broad tier (audit-only, WARN) ──────────────────
# Extra suffixes watched by audit_rules.py to catch new patterns early,
# before they graduate into the strict (commit-blocking) tiers above.
_BROAD_EXTRA_SUFFIXES = {
    # Consent/privacy
    "onetrust.io", "trustarc.com", "quantcast.com", "evidon.com",
    # Analytics/telemetry
    "optimizely.org", "branch.io", "appsflyer.com", "adjust.com",
    "kochava.com", "sentrycdn.com", "mixpanel.com", "amplitude.com",
    "segment.com", "hotjar.com", "fullstory.com", "clarity.ms",
    # Marketing/ad tech
    "flashtalking.com", "doubleclick.net", "googleadservices.com",
    "googlesyndication.com", "googletagmanager.com",
    "facebook.net", "fbcdn.net",
    # Broad cloud
    "amazonaws.com", "azure.com", "googleapis.com", "cloud.google.com",
}

BROAD_SHARED_SUFFIXES = (
    SHARED_CDN_PARENTS | SHARED_THIRD_PARTY_SUFFIXES | _BROAD_EXTRA_SUFFIXES
)
