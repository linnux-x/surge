"""Local cache of raw upstream snapshots for exact offline regeneration.

Each published ruleset records, in ``Rule/.sources/<name>.json``, the SHA-256 of
every upstream source *after* format conversion (comments and upstream
timestamps removed). The raw responses behind those hashes are kept here, outside
the repository, so ``generate_rules.py --offline`` can rebuild a ruleset from the
exact inputs of its published version — including lines an exclude file has
since stopped removing.

Location: ``$SURGE_SOURCE_CACHE``, else ``$XDG_CACHE_HOME/linnux-surge/sources``,
else ``~/.cache/linnux-surge/sources``. Layout::

    blobs/<raw sha256>   raw upstream text
    index.json           {url: [{"raw": sha, "converted": sha, "seen": iso8601}, ...]}

Older entries per URL are pruned beyond ``KEEP_PER_URL``; a pruned snapshot is
re-created by any online run that observes the same upstream content again.
"""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

KEEP_PER_URL = 10


class SnapshotMissing(LookupError):
    """The cache has no raw snapshot for a pinned converted hash."""


def cache_dir() -> Path:
    explicit = os.environ.get("SURGE_SOURCE_CACHE")
    if explicit:
        return Path(explicit)
    base = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
    return Path(base) / "linnux-surge" / "sources"


def lines_sha256(lines: list[str] | tuple[str, ...]) -> str:
    """Hash a line sequence independently of the original line endings."""
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".tmp-", delete=False) as handle:
        handle.write(data)
        temporary = Path(handle.name)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def _load_index(root: Path) -> dict[str, list[dict]]:
    try:
        data = json.loads((root / "index.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def put(url: str, raw: list[str] | tuple[str, ...], converted_sha: str) -> None:
    """Remember the raw response behind a converted hash; most recent first."""
    root = cache_dir()
    raw_sha = lines_sha256(raw)
    blob = root / "blobs" / raw_sha
    if not blob.exists():
        _atomic_write(blob, "\n".join(raw).encode("utf-8"))
    index = _load_index(root)
    entries = [e for e in index.get(url, []) if e.get("converted") != converted_sha]
    entries.insert(0, {"raw": raw_sha, "converted": converted_sha,
                       "seen": datetime.now(timezone.utc).isoformat(timespec="seconds")})
    index[url] = entries[:KEEP_PER_URL]
    _atomic_write(root / "index.json", (json.dumps(index, indent=1, sort_keys=True) + "\n").encode("utf-8"))
    referenced = {e["raw"] for items in index.values() for e in items}
    for stale in (root / "blobs").iterdir():
        if stale.name not in referenced and not stale.name.startswith(".tmp-"):
            stale.unlink(missing_ok=True)


def get(url: str, converted_sha: str) -> list[str]:
    """Return the raw lines whose conversion produced ``converted_sha``."""
    root = cache_dir()
    for entry in _load_index(root).get(url, []):
        if entry.get("converted") == converted_sha:
            try:
                text = (root / "blobs" / entry["raw"]).read_text(encoding="utf-8")
            except OSError:
                break
            lines = text.split("\n") if text else []
            if lines_sha256(lines) == entry["raw"]:
                return lines
            break
    raise SnapshotMissing(
        f"No cached snapshot for {url} (converted sha256 {converted_sha[:12]}…); "
        "run an online generation of this ruleset first")
