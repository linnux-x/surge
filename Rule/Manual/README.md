# Manual Rules

> **This directory is .gitignored** — your personal rules are never committed to the public repository.
> Fork users: add your own include/exclude rules here.

## File conventions

| Pattern | Purpose | Priority |
|---------|---------|----------|
| `<RulesetName>.txt` | Manually appended rules, placed at the top of the generated ruleset | Highest |
| `<RulesetName>.exclude.txt` | Exact rule lines to remove from upstream-generated rules | Applied before guardrails |

## Format

Both files follow the same format: one rule per line. Blank lines and `#` comments are supported.

### `<RulesetName>.txt` — manual includes

```text
# Add rules that should always appear in this ruleset
DOMAIN-SUFFIX,example.com
DOMAIN,api.example.com
IP-CIDR,10.0.0.0/8
```

These rules appear at the top of the generated `.list` file, before any upstream sources.

### `<RulesetName>.exclude.txt` — manual excludes

> ⚠️ **Exclude matching is exact-line matching, not substring matching.**
> You must write the complete rule line as it appears in the upstream source.

```text
# Correct — matches the exact upstream rule line
DOMAIN-SUFFIX,sentry.io

# Also correct — matches both DOMAIN and DOMAIN-SUFFIX variants
DOMAIN,o33249.ingest.sentry.io
DOMAIN-SUFFIX,o33249.ingest.sentry.io
```

Excludes are applied per-source before guardrails, so they can remove entries that differ in format across upstreams. If one upstream provides `DOMAIN,example.com` and another provides `DOMAIN-SUFFIX,example.com`, both must appear in the exclude file.

## Example

For a fork user who wants to add custom proxy rules to `AI.list` and exclude some domains from `Global.list`:

```
Rule/Manual/
├── AI.txt              # extra AI domains to proxy
├── AI.exclude.txt      # domains to remove from upstream AI sources
├── Global.exclude.txt  # domains to remove from upstream Global sources
└── README.md           # this file
```
