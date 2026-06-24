# Incremental Upstream Change Detection — linnux-x/surge Implementation

## Overview

The `check_upstream_updates.py` script enables incremental rule regeneration by comparing HTTP timestamp headers of all upstream sources against a cached state file. Only rulesets with changed upstream sources are regenerated, saving ~90% of workflow runtime on days with no upstream changes.

## Script: `scripts/check_upstream_updates.py`

Full implementation: `scripts/check_upstream_updates.py` in linnux-x/surge repo.

### Key Design Decisions

**HTTP HEAD with fallback chain:**
1. `HEAD` request → `Last-Modified`, `ETag`, `Content-Length`
2. Fallback `GET` with `Range: bytes=0-0` (minimal data transfer, ~200 bytes)
3. Last resort `GET` full file → reads Content-Length from `len(body)`

**Change detection logic:**
- ETag comparison preferred (most granular)
- Fallback to Last-Modified comparison
- Fallback to Content-Length comparison
- If no comparison available → treat as unchanged (conservative)
- Previously unavailable source that becomes available → CHANGED (new source)
- Was available, now unavailable → unchanged (network blip suppression)

**Source-to-ruleset mapping (`SOURCE_RULESET_MAP`):**
Maps each upstream URL → list of ruleset filenames. Must mirror the workflow's `process_rule` calls exactly. When the workflow adds/removes a source, this dict must be updated simultaneously.

**Dependency tracking (`OVERLAP_DEPENDENTS`):**
21 rulesets whose regeneration also requires `Global.list` to be re-pruned. When any of these changes, `Global.list` is automatically added to the changed list.

### State File: `scripts/source_state.json`

Committed to git. Each entry:
```json
{
  "https://...": {
    "last_modified": "Tue, 22 Jun 2026 12:00:00 GMT",
    "etag": "W/\"abc123\"",
    "content_length": "12345",
    "source_available": true
  }
}
```

### Workflow Integration (auto-rules.yml)

```yaml
- name: Check Upstream Updates
  id: check_upstream
  shell: bash
  run: |
    output=$(python3 scripts/check_upstream_updates.py 2>&1) || true
    summary=$(echo "$output" | grep '^{' | tail -1)
    echo "changed_rulesets=..." >> "$GITHUB_OUTPUT"
    echo "changed_count=..." >> "$GITHUB_OUTPUT"
```

All subsequent steps (Generate Rules, Manifests, Diff, Validate, Audit, Commit) are gated on `changed_count > 0`. The DNS-Mapping module sync runs unconditionally.

### Conditional Generation

Each `process_rule` call is wrapped in `should_process`:

```bash
should_process() {
  local target="$1"
  for c in "${CHANGED[@]}"; do
    [ "$c" = "$target" ] && return 0
  done
  return 1
}

if should_process "YouTube.list"; then
  process_rule "YouTube.list" "YouTube" \
    "blackmatrix7 YouTube|$BM7/YouTube/YouTube.list"
fi
```

### Known Issues

- **ruleset.skk.moe returns 403** on HEAD/Range requests → `source_available: false`, treated as unchanged. Manual `workflow_dispatch` to force-regenerate.
- **First run always full regeneration** — no cached state yet. The state file is committed after the first run.
- **Workflow must git-add `source_state.json` and `check_upstream_updates.py`** in the commit step, or state won't persist.
