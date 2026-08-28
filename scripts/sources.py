"""Canonical upstream source definitions for surge rule generation.

This is the single source of truth for all upstream URLs and their
mapping to ruleset files.  Both `check_upstream_updates.py` and
`generate_rules.py` import from here — when you add or remove an
upstream source, edit only this file.

Exported symbols:
    BASE_URIS          — dict of reusable base URLs
    RULE_SPECS         — {ruleset_name: (display_name, [(label, url, fmt)])}
    SOURCE_URL_MAP     — {url: [ruleset_name, ...]}
    OVERLAP_DEPENDENTS — rulesets that trigger Global.list re-pruning
    ALL_RULESETS       — set of all ruleset filenames
"""

from __future__ import annotations

# ── Reusable base URIs ────────────────────────────────────────────────────

BASE_URIS = {
    "BM7": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge",
    "SUKKA": "https://raw.githubusercontent.com/SukkaW/Surge/master/Source",
    # Rabbit-Spec is intentionally retained. It provides useful AIGC/China
    # coverage and the repo workflow credits Rabbit-Spec design ideas. Do not
    # remove it during source-pruning unless a manual full-generation audit
    # finds a concrete replacement with equal or better coverage.
    "RABBIT": "https://raw.githubusercontent.com/Rabbit-Spec/Surge/Master/Rules",
    "CHUA": "https://raw.githubusercontent.com/ConnersHua/RuleGo/master/Surge/Ruleset/Extra",
    "ROC301": "https://raw.githubusercontent.com/RocM301/Apple-Rule/refs/heads/main",
}

BM7 = BASE_URIS["BM7"]
SUKKA = BASE_URIS["SUKKA"]
RABBIT = BASE_URIS["RABBIT"]
CHUA = BASE_URIS["CHUA"]
ROC301 = BASE_URIS["ROC301"]

# User-directed primary upstreams.  The corresponding reviewed snapshots are
# used only when Kelee is temporarily blocked by WAF/TLS/network failures.
KELEE_SPEEDTEST_CHINA = "https://kelee.one/Tool/Loon/Lsr/SpeedtestChina.lsr"
KELEE_SPEEDTEST_INTERNATIONAL = "https://kelee.one/Tool/Loon/Lsr/SpeedtestInternational.lsr"
SNAPSHOT_FALLBACKS: dict[str, str] = {
    KELEE_SPEEDTEST_CHINA: "Rule/SourceSnapshots/SpeedtestChina.lsr",
    KELEE_SPEEDTEST_INTERNATIONAL: "Rule/SourceSnapshots/SpeedtestInternational.lsr",
}

# ── Canonical source list ─────────────────────────────────────────────────
# Each entry: (source_label, source_url, target_ruleset, format_or_None)
# format: "domainset" | "cidr" | "snapshot" | "loon-snapshot" | None

_SOURCES: list[tuple[str, str, str, str | None]] = [
    # Apple_AI.list
    ("RocM301 Apple-AI", f"{ROC301}/Apple-AI.list", "Apple_AI.list", None),
    ("SukkaW Apple Intelligence", "https://ruleset.skk.moe/List/non_ip/apple_intelligence.conf", "Apple_AI.list", None),
    # AI.list
    ("SukkaW AI", f"{SUKKA}/non_ip/ai.conf", "AI.list", None),
    ("Rabbit-Spec AIGC", f"{RABBIT}/AIGC.list", "AI.list", None),
    ("ConnersHua AI", f"{CHUA}/AI.list", "AI.list", None),
    # Apple.list
    ("blackmatrix7 Apple", f"{BM7}/Apple/Apple_All_No_Resolve.list", "Apple.list", None),
    # Apple_CN.list
    ("SukkaW Apple CN", "https://ruleset.skk.moe/List/non_ip/apple_cn.conf", "Apple_CN.list", None),
    ("SukkaW Apple CDN", "https://ruleset.skk.moe/List/domainset/apple_cdn.conf", "Apple_CN.list", "domainset"),
    # CDN.list
    ("SukkaW CDN", f"{SUKKA}/non_ip/cdn.conf", "CDN.list", None),
    # Download.list
    ("SukkaW Download", f"{SUKKA}/domainset/download.conf", "Download.list", "domainset"),
    ("SukkaW Game Download", f"{SUKKA}/domainset/game-download.conf", "Download.list", "domainset"),
    # China.list
    ("SukkaW Domestic", "https://ruleset.skk.moe/List/non_ip/domestic.conf", "China.list", None),
    ("blackmatrix7 ChinaMaxNoIP Domain", f"{BM7}/ChinaMaxNoIP/ChinaMaxNoIP_Domain.list", "China.list", "domainset"),
    ("Rabbit-Spec China", f"{RABBIT}/China.list", "China.list", None),
    # China_IP.list
    ("Loyalsoldier China CIDR", "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/cncidr.txt", "China_IP.list", None),
    ("blackmatrix7 China IPs", f"{BM7}/ChinaIPs/ChinaIPs.list", "China_IP.list", None),
    ("Rabbit-Spec China CIDR", f"{RABBIT}/ChinaCIDR.list", "China_IP.list", None),
    # ChinaMedia.list
    ("blackmatrix7 ChinaMedia", f"{BM7}/ChinaMedia/ChinaMedia.list", "ChinaMedia.list", None),
    # Disney.list
    ("blackmatrix7 Disney", f"{BM7}/Disney/Disney.list", "Disney.list", None),
    # Game.list
    ("blackmatrix7 Game", f"{BM7}/Game/Game.list", "Game.list", None),
    # Global.list
    ("blackmatrix7 Global", f"{BM7}/Global/Global_All_No_Resolve.list", "Global.list", None),
    # GlobalMedia.list
    ("blackmatrix7 GlobalMedia", f"{BM7}/GlobalMedia/GlobalMedia_All_No_Resolve.list", "GlobalMedia.list", None),
    # Google.list
    ("blackmatrix7 Google", f"{BM7}/Google/Google.list", "Google.list", None),
    # Microsoft.list
    ("blackmatrix7 Microsoft", f"{BM7}/Microsoft/Microsoft.list", "Microsoft.list", None),
    # Microsoft_CDN.list
    ("SukkaW Microsoft CDN", "https://ruleset.skk.moe/List/non_ip/microsoft_cdn.conf", "Microsoft_CDN.list", None),
    # Netflix.list
    ("blackmatrix7 Netflix", f"{BM7}/Netflix/Netflix.list", "Netflix.list", None),
    # PayPal.list
    ("blackmatrix7 PayPal", f"{BM7}/PayPal/PayPal.list", "PayPal.list", None),
    # SocialMedia.list
    ("blackmatrix7 Discord", f"{BM7}/Discord/Discord.list", "SocialMedia.list", None),
    ("blackmatrix7 Facebook", f"{BM7}/Facebook/Facebook.list", "SocialMedia.list", None),
    ("blackmatrix7 Instagram", f"{BM7}/Instagram/Instagram.list", "SocialMedia.list", None),
    ("blackmatrix7 Twitter", f"{BM7}/Twitter/Twitter.list", "SocialMedia.list", None),
    # Speedtest.list
    ("SukkaW Speedtest", f"{SUKKA}/domainset/speedtest.conf", "Speedtest.list", "domainset"),
    # Kelee is a daily primary upstream.  A reviewed local snapshot is used
    # only when the primary cannot be fetched; see SNAPSHOT_FALLBACKS.
    ("Kelee Speedtest International", KELEE_SPEEDTEST_INTERNATIONAL, "Speedtest.list", "loon-snapshot"),
    ("Kelee Speedtest China", KELEE_SPEEDTEST_CHINA, "Speedtest_China.list", "loon-snapshot"),
    # Spotify.list
    ("blackmatrix7 Spotify", f"{BM7}/Spotify/Spotify.list", "Spotify.list", None),
    # Telegram.list
    ("blackmatrix7 Telegram", f"{BM7}/Telegram/Telegram.list", "Telegram.list", None),
    ("Telegram Official CIDR", "https://core.telegram.org/resources/cidr.txt", "Telegram.list", "cidr"),
    ("SukkaW Telegram IP", "https://ruleset.skk.moe/List/ip/telegram.conf", "Telegram.list", None),
    # TikTok.list
    ("blackmatrix7 TikTok", f"{BM7}/TikTok/TikTok.list", "TikTok.list", None),
    # WeChat.list
    ("blackmatrix7 WeChat", f"{BM7}/WeChat/WeChat.list", "WeChat.list", None),
    # YouTube.list
    ("blackmatrix7 YouTube", f"{BM7}/YouTube/YouTube.list", "YouTube.list", None),
]

# ── Derived views (auto-generated from _SOURCES) ──────────────────────────

# SOURCE_URL_MAP: url → [ruleset_name, ...]  (for check_upstream_updates.py)
SOURCE_URL_MAP: dict[str, list[str]] = {}
for _label, _url, _rs, _fmt in _SOURCES:
    # Reviewed local snapshots are regenerated on every full build but are not
    # network upstreams: probing them would create a false daily-change loop.
    if _fmt != "snapshot":
        SOURCE_URL_MAP.setdefault(_url, []).append(_rs)

# RULE_SPECS: ruleset_name → (display_name, [(label, url, fmt), ...])
# (for generate_rules.py)
RULE_SPECS: dict[str, tuple[str, list[tuple[str, str, str | None]]]] = {}
for _label, _url, _rs, _fmt in _SOURCES:
    if _rs not in RULE_SPECS:
        display_name = _rs.replace(".list", "")
        RULE_SPECS[_rs] = (display_name, [])
    RULE_SPECS[_rs][1].append((_label, _url, _fmt))

# ALL_RULESETS: set of all ruleset filenames
ALL_RULESETS: set[str] = set(RULE_SPECS.keys())

# OVERLAP_DEPENDENTS: rulesets whose change triggers Global.list re-pruning
OVERLAP_DEPENDENTS: set[str] = {
    "WeChat.list", "Speedtest_China.list", "Speedtest.list", "Apple_AI.list", "AI.list", "Apple_CN.list",
    "Apple.list", "Microsoft_CDN.list", "Microsoft.list",
    "Telegram.list", "Download.list", "Game.list", "YouTube.list",
    "TikTok.list", "SocialMedia.list", "PayPal.list", "Google.list",
    "Netflix.list", "Disney.list", "ChinaMedia.list", "Spotify.list",
    "GlobalMedia.list",
    "CDN.list",
}

# Sanity check at import time: every overlap dependent must be a known ruleset
_missing = OVERLAP_DEPENDENTS - ALL_RULESETS
if _missing:
    raise SystemExit(
        f"OVERLAP_DEPENDENTS references unknown rulesets: {sorted(_missing)}"
    )
