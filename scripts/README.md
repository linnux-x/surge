# scripts

> Pipeline scripts for the linnux-x/surge rule repository.
> All scripts use Python 3.10+ standard library only — no third-party dependencies.

## Pipeline order

| Step | Script | What it does |
|------|--------|--------------|
| 1 | `check_upstream_updates.py` | Parallel HEAD checks against all upstream sources (8 threads); detects changed rulesets |
| 2 | `generate_rules.py` | Downloads, merges, cleans, validates all changed rules; applies manual rules, excludes, guardrails, CIDR pruning, Global overlap pruning |
| 3 | `manifest.py` | Generates per-file rule manifests (`<stable_id>\t<source_name>`) for diff tracking |
| 4 | `diff_manifests.py` | Compares current manifests against git HEAD → `diff_report.md` + `diff_report.json` |
| 5 | `validate_surge_repo.py` | Repository invariant checks (15+ rules); rule content delegated to `rule_validator.py` |
| 6 | `audit_rules.py` | Post-generation online audit (5 checks): upstream reachability, rule counts, shared infrastructure, Surge docs, exclude coverage |

## Source of truth

| Module | Role |
|--------|------|
| `sources.py` | Single source of truth for all upstream URLs and ruleset specs. Every other script imports from here. |
| `rule_validator.py` | Shared validation rules used by both `generate_rules.py` and `validate_surge_repo.py`. |
| `prune_cidr.py` | CIDR deduplication — called by `generate_rules.py` after rule generation. |

## Local usage

```bash
# Step 1: Check which upstreams have changed
python3 scripts/check_upstream_updates.py

# Step 2: Generate rules for specific changed sets
CHANGED_RULESETS='["AI.list"]' python3 scripts/generate_rules.py

# Or process all (simulates workflow_dispatch)
GITHUB_EVENT_NAME=workflow_dispatch python3 scripts/generate_rules.py

# Step 3: Generate manifests
python3 scripts/manifest.py

# Step 4: Diff against git HEAD
python3 scripts/diff_manifests.py

# Step 5: Validate repo
python3 scripts/validate_surge_repo.py

# Step 6: Online audit
python3 scripts/audit_rules.py
```

## Design principles

- **No pip install** — all scripts use Python standard library only
- **Single source of truth** — upstream URLs in `sources.py`; validation rules in `rule_validator.py`
- **Import, not parse** — scripts import from `sources.py`, never parse YAML/JSON for source configuration
- **Shared validation** — `rule_validator.py` is the single validation engine; adding a policy check requires editing only that file
