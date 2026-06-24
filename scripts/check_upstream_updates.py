#!/usr/bin/env python3
"""Check upstream rule sources for updates using parallel HTTP HEAD requests.

Compares cached Last-Modified / ETag headers against current upstream.
Outputs a JSON summary; exits 0 if nothing changed, 1 if changes detected.

Sources that don't support HEAD fall back to Range GET then full GET.
When no timestamp info is available, marks source as "unknown" and
regenerates (conservative).

All source URLs come from scripts/sources.py — the single source of truth.
State file: scripts/source_state.json (committed to git).
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Ensure scripts/ is on the path so 'import sources' works
_scripts_dir = Path(__file__).resolve().parent
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from sources import SOURCE_URL_MAP, OVERLAP_DEPENDENTS

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "scripts" / "source_state.json"

# Conservative: GitHub allows ~60 req/min unauthenticated
MAX_WORKERS = 8
REQUEST_TIMEOUT = 20


def fetch_upstream_info(url: str) -> dict:
    """Fetch timestamp info from upstream URL via HEAD, fallback to Range GET, then full GET.

    Returns dict with: last_modified, etag, content_length, source_available
    """
    result: dict[str, str | bool | None] = {
        "last_modified": None,
        "etag": None,
        "content_length": None,
        "source_available": False,
    }

    # ── Try HEAD first ──
    req = urllib.request.Request(url, method="HEAD")
    try:
        resp = urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT)
        result["last_modified"] = resp.headers.get("Last-Modified")
        result["etag"] = resp.headers.get("ETag")
        result["content_length"] = resp.headers.get("Content-Length")
        result["source_available"] = True
        return result
    except (urllib.error.URLError, OSError, ValueError):
        pass

    # ── Fallback: Range GET (bytes=0-0) ──
    req = urllib.request.Request(url, method="GET")
    req.add_header("Range", "bytes=0-0")
    try:
        resp = urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT)
        result["last_modified"] = resp.headers.get("Last-Modified")
        result["etag"] = resp.headers.get("ETag")
        result["content_length"] = resp.headers.get("Content-Length")
        result["source_available"] = True
        return result
    except (urllib.error.URLError, OSError, ValueError):
        pass

    # ── Last resort: full GET ──
    try:
        resp = urllib.request.urlopen(url, timeout=REQUEST_TIMEOUT)
        result["last_modified"] = resp.headers.get("Last-Modified")
        result["etag"] = resp.headers.get("ETag")
        result["content_length"] = str(len(resp.read()))
        result["source_available"] = True
        return result
    except (urllib.error.URLError, OSError, ValueError) as e:
        print(f"  ⚠  Unreachable: {url} — {e}", file=sys.stderr)
        return result


def load_state() -> dict:
    """Load cached source_state.json, returning {} if missing or corrupt."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_state(state: dict) -> None:
    """Persist state, pruning stale entries not in SOURCE_URL_MAP."""
    active_urls = set(SOURCE_URL_MAP.keys())
    pruned = {url: info for url, info in state.items() if url in active_urls}
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(pruned, indent=2, sort_keys=True) + "\n")


def has_changed(current: dict, cached: dict) -> bool:
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

    # Compare timestamps in priority order: ETag > Last-Modified > Content-Length
    cur_etag = current.get("etag")
    cached_etag = cached.get("etag")
    if cur_etag and cached_etag:
        return cur_etag != cached_etag

    cur_lm = current.get("last_modified")
    cached_lm = cached.get("last_modified")
    if cur_lm and cached_lm:
        return cur_lm != cached_lm

    cur_cl = current.get("content_length")
    cached_cl = cached.get("content_length")
    if cur_cl and cached_cl:
        return cur_cl != cached_cl

    # Can't compare anything meaningful — assume changed (conservative)
    return True


def check_all_sources_parallel(
    urls: list[str],
    state: dict,
) -> tuple[set[str], dict, int, int]:
    """Check all source URLs in parallel via ThreadPoolExecutor.

    Returns: (changed_rulesets, updated_state, changed_count, unknown_count)
    """
    changed_rulesets: set[str] = set()
    new_state: dict = {}
    changed_count = 0
    unknown_count = 0

    def _check_one(url: str) -> tuple[str, dict, bool, bool]:
        """Worker: fetch info and compare. Returns (url, current_info, changed, is_unknown)."""
        current = fetch_upstream_info(url)
        cached = state.get(url, {})
        is_changed = has_changed(current, cached)

        has_ts = bool(current.get("last_modified") or current.get("etag"))
        return url, current, is_changed, not has_ts

    total = len(urls)
    completed = 0

    print(f"Checking {total} upstream sources (parallel, {MAX_WORKERS} workers)...",
          file=sys.stderr)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(_check_one, url): url for url in urls}
        for future in as_completed(futures):
            url, current, is_changed, is_unknown = future.result()
            completed += 1

            # Update state
            new_state[url] = current

            # Track unknowns
            if is_unknown:
                unknown_count += 1

            # Track changes
            status = "CHANGED" if is_changed else "unchanged"
            rulesets = SOURCE_URL_MAP.get(url, ["<unknown>"])
            print(f"  [{completed}/{total}] {status:>9s}  {url}",
                  file=sys.stderr)
            if is_changed:
                changed_count += 1
                for rs in rulesets:
                    changed_rulesets.add(rs)

    # If any overlap-dependent ruleset changed, add Global.list for re-pruning
    if changed_rulesets & OVERLAP_DEPENDENTS:
        changed_rulesets.add("Global.list")
        print("\n  → Global.list added (overlap prune required)", file=sys.stderr)

    return changed_rulesets, new_state, changed_count, unknown_count


def main() -> None:
    urls = list(SOURCE_URL_MAP.keys())
    if not urls:
        print("No sources configured.", file=sys.stderr)
        sys.exit(0)

    state = load_state()

    changed_rulesets, new_state, changed_count, unknown_count = \
        check_all_sources_parallel(urls, state)

    # Persist updated state (with stale entry pruning)
    save_state(new_state)

    # Build summary
    summary = {
        "changed": bool(changed_rulesets),
        "changed_count": changed_count,
        "total_sources": len(urls),
        "unknown_timestamp_sources": unknown_count,
        "rulesets": sorted(changed_rulesets),
    }
    print(file=sys.stderr)
    print(json.dumps(summary, ensure_ascii=False), file=sys.stdout)

    sys.exit(1 if changed_rulesets else 0)


if __name__ == "__main__":
    main()
