# Tests

> Routing order simulation and validation tests for linnux-x/surge.
> Uses Python 3.10+ standard library only.

## Running tests

```bash
# Simulate routing and check against expected results
python3 scripts/test_routing_order.py

# Or from the repo root
cd /path/to/surge
python3 scripts/test_routing_order.py
```

## Test files

| File | Purpose |
|------|---------|
| `expected-routing.csv` | Test cases: domain → expected matching ruleset |
| *(future)* `sample-request.txt` | Sample Surge request logs for bulk testing |

## Adding test cases

Edit `tests/expected-routing.csv`. Format:

```csv
domain,expected_ruleset,note
example.com,AI.list,description of why this should match AI.list
```

- `domain` — the domain to test (lowercase)
- `expected_ruleset` — which `.list` file (or `DIRECT` for China/LAN rules, or `Global` for FINAL)
- `note` — human-readable explanation

The test script loads all `Rule/*.list` files and simulates Surge's first-match logic,
then reports any mismatches between expected and actual routing.
