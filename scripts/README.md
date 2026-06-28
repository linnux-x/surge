# scripts

> Pipeline scripts for the linnux-x/surge rule repository.
> All scripts use Python 3.10+ standard library only — no third-party dependencies.

## Pipeline order

| Step | Script | What it does |
|------|--------|--------------|
| 1 | `check_upstream_updates.py` | Parallel HEAD checks against all upstream sources (8 threads); detects changed rulesets |
| 2 | `generate_rules.py` | Downloads, merges, cleans, validates all changed rules; applies manual rules, excludes, guardrails, CIDR pruning (built-in), Global overlap pruning |
| 3 | `manifest.py` | Generates per-file rule manifests (`<stable_id>\t<source_name>`); `--diff` compares against git HEAD → `diff_report.md` + `diff_report.json` |
| 4 | `validate_surge_repo.py` | Repository invariant checks (15+ rules); rule content delegated to `rule_validator.py` |
| 5 | `audit_rules.py` | Post-generation online audit (5 checks): upstream reachability, rule counts, shared infrastructure, Surge docs, exclude coverage |

## Source of truth

| Module | Role |
|--------|------|
| `sources.py` | Single source of truth for all upstream URLs and ruleset specs |
| `rule_validator.py` | Shared validation rules used by both `generate_rules.py` and `validate_surge_repo.py` |

## Local usage

```bash
# Step 1: Check which upstreams have changed
python3 scripts/check_upstream_updates.py

# Step 2: Generate rules
CHANGED_RULESETS='["AI.list"]' python3 scripts/generate_rules.py

# Step 3: Generate manifests + diff report
python3 scripts/manifest.py
python3 scripts/manifest.py --diff

# Step 4: Validate repo
python3 scripts/validate_surge_repo.py

# Step 5: Online audit
python3 scripts/audit_rules.py

# Test routing order
python3 scripts/test_routing_order.py

# Generate Surge rules from iOS privacy report
python3 scripts/ios_privacy_to_surge.py report.ndjson
privacy2surge report.ndjson -o Rule/App.list
```

## Utility scripts

| Script | What it does |
|--------|--------------|
| `ios_privacy_to_surge.py` | Convert iOS privacy report (.ndjson) → Surge/Loon rules. Filters system traffic, merges subdomains, matches apps via iTunes API + built-in mapping |
| `app_mapping.json` | Bundle ID → app name + domain/IP mapping (extensible) |
| `vps_monitor.py` | Lightweight HTTP server exposing system metrics as JSON. Designed for Surge Panel. Use `VPS_MONITOR_HOST` and `VPS_MONITOR_TOKEN` env vars. |

## Design principles

- **No pip install** — all pipeline scripts use Python standard library only (`ios_privacy_to_surge.py` uses stdlib too; iTunes API calls are optional)
- **Single source of truth** — upstream URLs in `sources.py`; validation rules in `rule_validator.py`
- **Minimal files** — CIDR pruning built into `generate_rules.py`; manifest diff built into `manifest.py --diff`
- **Import, not parse** — scripts import from `sources.py`, never parse YAML/JSON for source configuration
