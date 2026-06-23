#!/usr/bin/env python3
"""
Check upstream rule sources for updates using HTTP HEAD requests.

Compares cached Last-Modified / ETag headers against current upstream.
Outputs a JSON array of rule .list filenames that need regeneration.
Exits with code 0 if nothing changed, code 1 if changes detected.

Sources that don't support HEAD fall back to GET and check Content-Length.
When no timestamp info is available at all, marks the source as "unknown"
(still regenerates — conservative).

State file: scripts/source_state.json (committed to git)
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "scripts" / "source_state.json"

# ── Source URL → ruleset mapping (must match auto-rules.yml) ──────────────────
BM7 = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge"
SUKKA = "https://raw.githubusercontent.com/SukkaW/Surge/master/Source"
RABBIT = "https://raw.githubusercontent.com/Rabbit-Spec/Surge/Master/Rules"
QUIXOTIC = "https://raw.githubusercontent.com/QuixoticHeart/rule-set/refs/heads/ruleset/surge"
CHUA = "https://raw.githubusercontent.com/ConnersHua/RuleGo/master/Surge/Ruleset/Extra"

SOURCE_RULESET_MAP: dict[str, list[str]] = {
    # AI.list
    f"{SUKKA}/non_ip/ai.conf": ["AI.list"],
    f"{SUKKA}/non_ip/apple_intelligence.conf": ["AI.list"],
    f"{RABBIT}/AIGC.list": ["AI.list"],
    f"{CHUA}/AI.list": ["AI.list"],
    # Apple.list
    f"{BM7}/Apple/Apple_All_No_Resolve.list": ["Apple.list"],
    # Apple_CN.list
    "https://ruleset.skk.moe/List/non_ip/apple_cn.conf": ["Apple_CN.list"],
    "https://ruleset.skk.moe/List/domainset/apple_cdn.conf": ["Apple_CN.list"],
    # CDN.list
    f"{SUKKA}/non_ip/cdn.conf": ["CDN.list"],
    # Download.list
    f"{SUKKA}/domainset/download.conf": ["Download.list"],
    f"{SUKKA}/domainset/game-download.conf": ["Download.list"],
    # China.list
    f"{SUKKA}/non_ip/domestic.conf": ["China.list"],
    f"{BM7}/ChinaMaxNoIP/ChinaMaxNoIP_Domain.list": ["China.list"],
    f"{RABBIT}/China.list": ["China.list"],
    # China_IP.list
    "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/cncidr.txt": ["China_IP.list"],
    f"{BM7}/ChinaIPs/ChinaIPs.list": ["China_IP.list"],
    f"{RABBIT}/ChinaCIDR.list": ["China_IP.list"],
    # ChinaMedia.list
    f"{BM7}/ChinaMedia/ChinaMedia.list": ["ChinaMedia.list"],
    # Disney.list
    f"{BM7}/Disney/Disney.list": ["Disney.list"],
    # Game.list
    f"{BM7}/Game/Game.list": ["Game.list"],
    # Global.list
    f"{BM7}/Global/Global_All_No_Resolve.list": ["Global.list"],
    # GlobalMedia.list
    f"{BM7}/GlobalMedia/GlobalMedia_All_No_Resolve.list": ["GlobalMedia.list"],
    # Google.list
    f"{BM7}/Google/Google.list": ["Google.list"],
    # Microsoft.list
    f"{BM7}/Microsoft/Microsoft.list": ["Microsoft.list"],
    # Microsoft_CDN.list
    "https://ruleset.skk.moe/List/non_ip/microsoft_cdn.conf": ["Microsoft_CDN.list"],
    # Netflix.list
    f"{BM7}/Netflix/Netflix.list": ["Netflix.list"],
    # PayPal.list
    f"{BM7}/PayPal/PayPal.list": ["PayPal.list"],
    # SocialMedia.list
    f"{QUIXOTIC}/socialmedia.list": ["SocialMedia.list"],
    f"{QUIXOTIC}/forum.list": ["SocialMedia.list"],
    f"{BM7}/Facebook/Facebook.list": ["SocialMedia.list"],
    f"{BM7}/Instagram/Instagram.list": ["SocialMedia.list"],
    f"{BM7}/Twitter/Twitter.list": ["SocialMedia.list"],
    # Speedtest.list
    f"{SUKKA}/domainset/speedtest.conf": ["Speedtest.list"],
    # Telegram.list
    f"{BM7}/Telegram/Telegram.list": ["Telegram.list"],
    "https://core.telegram.org/resources/cidr.txt": ["Telegram.list"],
    "https://ruleset.skk.moe/List/ip/telegram.conf": ["Telegram.list"],
    # TikTok.list
    f"{BM7}/TikTok/TikTok.list": ["TikTok.list"],
    # WeChat.list
    f"{BM7}/WeChat/WeChat.list": ["WeChat.list"],
    # YouTube.list
    f"{BM7}/YouTube/YouTube.list": ["YouTube.list"],
}

# Rulesets whose regeneration also requires Global.list to be re-pruned
OVERLAP_DEPENDENTS = {
    "WeChat.list", "Speedtest.list", "AI.list", "Apple_CN.list",
    "Apple.list", "Microsoft_CDN.list", "Microsoft.list",
    "Telegram.list", "Download.list", "Game.list", "YouTube.list",
    "TikTok.list", "SocialMedia.list", "PayPal.list", "Google.list",
    "Netflix.list", "Disney.list", "ChinaMedia.list", "GlobalMedia.list",
    "CDN.list",
}
ALL_RULESET_NAMES: set[str] = set()
for names in SOURCE_RULESET_MAP.values():
    ALL_RULESET_NAMES.update(names)


def fetch_upstream_info(url: str) -> dict:
    """Fetch timestamp info from upstream URL via HEAD, fallback to GET.

    Returns dict with keys: last_modified, etag, content_length, source_available
    """
    result = {
        "last_modified": None,
        "etag": None,
        "content_length": None,
        "source_available": False,
    }

    # Try HEAD first
    req = urllib.request.Request(url, method="HEAD")
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        result["last_modified"] = resp.headers.get("Last-Modified")
        result["etag"] = resp.headers.get("ETag")
        result["content_length"] = resp.headers.get("Content-Length")
        result["source_available"] = True
        return result
    except (urllib.error.URLError, OSError, ValueError):
        pass

    # Fallback: GET with Range:0-0 (minimal data transfer)
    req = urllib.request.Request(url, method="GET")
    req.add_header("Range", "bytes=0-0")
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        result["last_modified"] = resp.headers.get("Last-Modified")
        result["etag"] = resp.headers.get("ETag")
        result["content_length"] = resp.headers.get("Content-Length")
        result["source_available"] = True
        return result
    except (urllib.error.URLError, OSError, ValueError):
        # Full GET as last resort
        try:
            resp = urllib.request.urlopen(url, timeout=15)
            result["last_modified"] = resp.headers.get("Last-Modified")
            result["etag"] = resp.headers.get("ETag")
            result["content_length"] = len(resp.read())
            result["source_available"] = True
            return result
        except (urllib.error.URLError, OSError, ValueError) as e:
            print(f"  ⚠  Unreachable: {url} — {e}", file=sys.stderr)
            return result


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def has_changed(current: dict[str, str | None], cached: dict) -> bool:
    """Compare current upstream info with cached state."""
    if not cached.get("source_available"):
        # Previously unavailable → still unavailable = no change
        if not current.get("source_available"):
            return False
        # Was unavailable, now available = change
        return True

    if not current.get("source_available"):
        # Was available, now unavailable = treat as unchanged (network blip)
        return False

    # Compare timestamps
    cur_lm = current.get("last_modified")
    cur_etag = current.get("etag")
    cur_cl = current.get("content_length")
    cached_lm = cached.get("last_modified")
    cached_etag = cached.get("etag")
    cached_cl = cached.get("content_length")

    if cur_etag and cached_etag:
        return cur_etag != cached_etag
    if cur_lm and cached_lm:
        return cur_lm != cached_lm
    if cur_cl and cached_cl:
        return cur_cl != cached_cl
    # If we can't compare anything meaningful, assume changed
    return True


def main() -> None:
    state = load_state()
    changed_rulesets: set[str] = set()
    total_sources = len(SOURCE_RULESET_MAP)
    changed_count = 0
    unknown_count = 0

    print(f"Checking {total_sources} upstream sources...", file=sys.stderr)

    for idx, (url, rulesets) in enumerate(SOURCE_RULESET_MAP.items(), 1):
        print(f"  [{idx}/{total_sources}] {url}", file=sys.stderr)
        current = fetch_upstream_info(url)
        cached = state.get(url, {})

        # Flag sources with no detectable timestamp info
        has_any_timestamp = bool(
            current.get("last_modified") or current.get("etag")
        )
        if not has_any_timestamp:
            unknown_count += 1

        if has_changed(current, cached):
            changed_count += 1
            for rs in rulesets:
                changed_rulesets.add(rs)
            print(f"    → CHANGED (affects: {', '.join(rulesets)})", file=sys.stderr)
        else:
            print(f"    → unchanged", file=sys.stderr)

        # Always update state with current info
        state[url] = current

    # If Global.list needs pruning and something changed, add it
    if changed_rulesets & OVERLAP_DEPENDENTS:
        changed_rulesets.add("Global.list")
        print(f"\n  → Global.list added (overlap prune required)", file=sys.stderr)

    # Save updated state
    save_state(state)

    # Summary
    summary = {
        "changed": bool(changed_rulesets),
        "changed_count": changed_count,
        "total_sources": total_sources,
        "unknown_timestamp_sources": unknown_count,
        "rulesets": sorted(changed_rulesets),
    }
    print(file=sys.stderr)
    print(json.dumps(summary, ensure_ascii=False), file=sys.stdout)

    if changed_rulesets:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
