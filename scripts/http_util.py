"""Shared HTTP fetch helper for pipeline scripts (stdlib only).

Every urllib-based text fetch in the pipeline goes through fetch_text() so
timeout and User-Agent behaviour stay consistent across scripts.

Deliberate exceptions:
- generate_rules.py keeps curl (subprocess) for bulk ruleset downloads —
  battle-tested retry/redirect handling for large payloads, now with
  explicit connect/total timeouts.
- check_upstream_updates.py keeps its specialised HEAD/Range prober — it
  needs response headers (ETag/Last-Modified), not body text.
"""

from __future__ import annotations

import ssl
import urllib.request

DEFAULT_TIMEOUT = 30
DEFAULT_USER_AGENT = "surge-pipeline/1.0"


def fetch_text(
    url: str,
    timeout: int = DEFAULT_TIMEOUT,
    user_agent: str = DEFAULT_USER_AGENT,
) -> str | None:
    """Fetch URL content, return text or None on failure."""
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        print(f"  ⚠ FETCH FAILED: {url} → {exc}")
        return None
