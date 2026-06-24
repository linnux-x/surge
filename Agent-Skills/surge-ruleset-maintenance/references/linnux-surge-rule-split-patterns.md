# Linnux Surge Rule Split Patterns

Session-derived patterns for `linnux-x/surge` rule maintenance. Re-check the live repo before acting, but use these as durable heuristics.

## Focused Rule Changes and `# UPDATED`

- Any `Rule/*.list` file whose rule body changes must have its header `# UPDATED` refreshed in the same commit.
- The preferred way is to run the active generator/workflow, then restore unrelated generated `.list` files before committing.
- For focused commits, verify every remaining modified `Rule/*.list` has:
  - changed `# UPDATED`;
  - correct `# TOTAL` count;
  - intended rule-body delta only.

## Moving Traffic from Broad Provider Rules to Focused Rules

When moving a subset out of a broad provider ruleset:

1. Add durable includes to `Rule/Manual/<Focused>.txt`.
2. Add durable excludes to `Rule/Manual/<Broad>.exclude.txt`.
3. Regenerate with the active workflow.
4. Restore unrelated `.list` timestamp churn.
5. Verify representative first-match samples against `Conf/LINNUX.conf` order.

Examples from this session:

- Google AI / Gemini / AI Studio / NotebookLM / Jules / Antigravity moved out of `Google.list` and into `AI.list`.
- Apple China / `.cn` / Apple China CDN edge hosts moved out of `Apple.list` and into `Apple_CN.list`.
- Broad shared CDN parent domains moved out of `CDN.list` so service-specific CDN hosts remain controlled by focused rules.

## Manual Exclude Hygiene

`Rule/Manual/*.exclude.txt` may contain comments and blank lines only if the workflow sanitizes patterns before `grep -vFf`.

Safe pattern:

```bash
grep -vFf <(sed 's/\r$//' "$exclude_file" | awk 'NF && $0 !~ /^[[:space:]]*#/')
```

Without this, a blank line in an exclude file can match every line and wipe a generated ruleset.

## CDN Parent Cleanup Heuristic

Treat broad shared CDN parents as too wide for `CDN.list` unless the user explicitly wants all tenants of that CDN routed by the CDN policy.

Examples removed/excluded from `CDN.list`:

```text
akadns.net
akamaiedge.net
akamaihd.net
akamaized.net
azureedge.net
b-cdn.net
cdn77.org
cloudfront.net
edgekey.net
edgesuite.net
fastly.net
```

Keep explicit exceptions when they encode a deliberate policy, e.g. `DOMAIN,release-assets.githubusercontent.com` for GitHub release assets.

## Apple Split Checks

For `Apple_CN.list` before `Apple.list`:

- exact overlap between `Apple.list` and `Apple_CN.list` should be zero;
- `.cn` Apple properties should not remain in `Apple.list`;
- broad `akadns.net` parent rules should not remain in `Apple.list`;
- representative samples should hit as intended:
  - `apple.com.cn`, `icloud.com.cn`, `apple.cn` -> `Apple_CN.list`;
  - `apple.com` -> `Apple.list`;
  - `apple-relay.apple.com` -> `AI.list` if Apple Intelligence rules are earlier.

## CDN Split Checks

Representative samples after narrowing CDN:

- `release-assets.githubusercontent.com` -> `CDN.list`;
- OpenAI/Anthropic CDN hosts such as `production-openaicom-storage.azureedge.net` and `servd-anthropic-website.b-cdn.net` -> `AI.list`;
- Microsoft CDN hosts -> `Microsoft_CDN.list`;
- Apple China CDN hosts -> `Apple_CN.list`;
- Netflix / GlobalMedia CDN hosts -> their focused media rules;
- bare broad parents such as `cloudfront.net` should not be caught by `CDN.list`.
