# Semantic Overlap Pruning for Early-Position Rules

When a ruleset appears early in the configured `RULE-SET` order (e.g., WeChat at position 1, Speedtest at position 2), its domains/IPs may also appear in later, broader fallback rulesets. These later entries are semantically redundant because the early rule will always match first. Removing them from the later rulesets (via `Rule/Manual/<Later>.exclude.txt`) keeps the fallback sets focused and avoids confusion about which policy governs the traffic.

## Pattern

1. **Identify the early rule's coverage.** Parse all `DOMAIN`, `DOMAIN-SUFFIX`, and `USER-AGENT` entries from the early-position `.list` file.
2. **Scan later rulesets for overlaps.** For each ruleset after the target in `Conf/*.conf` order:
   - Exact `DOMAIN` match → the same host appears in both.
   - `DOMAIN` in later file whose value ends with `.<suffix>` from the early file → shadowed by the early suffix.
   - `DOMAIN-SUFFIX` in later file that equals or is a subdomain of an early `DOMAIN-SUFFIX` → shadowed.
3. **Add exclusions to later rulesets' `*.exclude.txt`.** Use the correct rule type:
   - `DOMAIN,exact.host.com` for exact hostname matches.
   - `DOMAIN-SUFFIX,parent.com` only when the value is truly a domain suffix covering subdomains.
   - **Never use `DOMAIN-SUFFIX` for a leaf hostname** (e.g., `mensura.cdn-apple.com`) — that would over-exclude by also matching hypothetical subdomains.
4. **Do not manually edit `.list` files.** Let the next workflow run regenerate them with excludes applied. If you must verify immediately, run the generator locally.
5. **Handle git push conflicts from auto-commits.** If the remote has a workflow-generated commit that conflicts with your local `.list` edits, reset all `.list` files to the remote HEAD and commit only the Manual file changes. The workflow will apply the excludes on the next scheduled run.

## Speedtest Overlaps (linnux-x/surge)

Speedtest.list is at position 2. Overlaps found and excluded in:

| Later ruleset | Excluded entries | Reason |
|---|---|---|
| `Apple_CN.list` | `DOMAIN,mensura.cdn-apple.com` | Apple Network Quality speed test |
| `Global.list` | 11 Speedtest domain/suffix entries | Speedtest nodes also in global fallback |
| `GlobalMedia.list` | `DOMAIN-SUFFIX,speed.hinet.net` | HiNet speed test |
| `Google.list` | `DOMAIN-SUFFIX,speed.googlefiber.net` | Google Fiber speed test |
| `Download.list` | `DOMAIN,desktop.wifiman.com` | Ubiquiti speed test client |

## WeChat Overlaps (linnux-x/surge)

WeChat.list is at position 1. Overlaps found and excluded in:

| Later ruleset | Excluded entries | Reason |
|---|---|---|
| `China.list` | 24 WeChat domain/suffix + 2 USER-AGENT + 8 weixin subdomains | WeChat domains in China fallback |
| `ChinaMedia.list` | `DOMAIN,dldir1.qq.com`, `DOMAIN,soup.v.qq.com` | Shared Tencent download/video domains |
| `Download.list` | `DOMAIN,dl.wechat.com` | WeChat download endpoint |

## PayPal Overlaps (linnux-x/surge)

PayPal.list is at position 14. Chinese domestic services should route through China DIRECT, not PayPal proxy.

| Later ruleset | Excluded entries | Reason |
|---|---|---|
| `PayPal.list` | 14 `.cn` domains (anfutong.cn, beibao.cn, paypal.com.cn, etc.) | 安付通/贝宝 — China domestic → China DIRECT |

**Note:** These exclusions are in `Rule/Manual/PayPal.exclude.txt`. The `.cn` domains are added to `Rule/Manual/China.txt` so they route DIRECT via China policy.

## Netflix Overlaps (linnux-x/surge)

Netflix.list is at position 16. Community lists often include shared third-party services used by thousands of sites.

| Later ruleset | Excluded entries | Reason |
|---|---|---|
| `Netflix.list` | `DOMAIN-SUFFIX,cookielaw.org` | OneTrust cookie consent, thousands of sites |
| `Netflix.list` | `DOMAIN-SUFFIX,onetrust.com` | OneTrust privacy platform, thousands of sites |
| `Netflix.list` | `DOMAIN-SUFFIX,us-west-2.amazonaws.com` | Entire AWS region — too broad |

**Decision:** Keep Akamai/EdgeSuite entries with Netflix prefixes (e.g., `netflix.com.edgesuite.net`), but exclude completely generic shared infrastructure.

## Disney Overlaps (linnux-x/surge)

Disney.list is at position 17. Exclude non-Disney-proprietary third-party services while keeping Disney/ESPN-prefixed subdomains.

| Later ruleset | Excluded entries | Reason |
|---|---|---|
| `Disney.list` | `DOMAIN-SUFFIX,adobedtm.com` | Adobe Tag Manager (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,braze.com` | Marketing platform (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,conviva.com` | Video analytics — keep `cws.conviva.com` |
| `Disney.list` | `DOMAIN-SUFFIX,cdn.optimizely.com` | A/B testing CDN (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,bam.nr-data.net` | New Relic data collection (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,js-agent.newrelic.com` | New Relic JS agent (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,execute-api.us-east-1.amazonaws.com` | AWS API Gateway (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,d9.flashtalking.com` | Flashtalking ad tracking (shared) |
| `Disney.list` | `DOMAIN-SUFFIX,hsprepack.akamaized.net` | Akamai CDN (shared) |

**Kept:** `disney.demdex.net`, `disneyplus.com.ssl.sc.omtrdc.net`, `espn.hb.omtrdc.net`, `disney-portal.my.onetrust.com`, `disney.my.sentry.io` — all have Disney/ESPN prefixes, so they're Disney-specific.

## GitHub Workflow Commit Conflict Handling

When the remote has advanced due to a scheduled workflow auto-commit that touched `.list` files while you were editing Manual files:

1. **Do NOT rebase `.list` conflicts by hand.** Manual resolution of generated rules creates brittle timestamp/count mismatches.
2. **Reset all `.list` files to remote HEAD.** The workflow is the source of truth for generated output.
3. **Commit only Manual file changes.** Your `.txt` and `.exclude.txt` edits are durable.
4. **Push Manual changes.** The next scheduled workflow run will automatically regenerate `.list` files with the new excludes applied.

Pattern:
```bash
# After remote advanced with workflow commit
git pull origin main
# If conflicts on .list files:
git reset HEAD -- Rule/*.list  # Reset all .list to remote version
git add Rule/Manual/
git commit -m "fix: add semantic excludes for ..."
git push origin main
# Next workflow run will regenerate .list with excludes applied
```

## Destination Reporting Convention

When excluding domains from a later ruleset, always report where the traffic goes:

- **Target ruleset**: The early rule that now exclusively matches (e.g., "goes to WeChat.list → WeChat policy").
- **Earlier first-match still catches it**: If another even-earlier rule also matches.
- **No focused match**: Falls through to generic fallback (Global/China) or FINAL.

### Example Destination Reports

| Excluded from | Rule | Destination | Reason |
|---|---|---|---|
| China.list | `DOMAIN-SUFFIX,qq.com` | WeChat (position 1) | Early WeChat rule shadows later China fallback |
| PayPal.list | `DOMAIN-SUFFIX,beibao.cn` | China (position 17) | China domestic service → DIRECT |
| Netflix.list | `DOMAIN-SUFFIX,cookielaw.org` | Global (position 16) | Shared service, not Netflix-specific |
| Disney.list | `DOMAIN-SUFFIX,conviva.com` | Global (position 16) | Shared analytics; `cws.conviva.com` stays in Disney |
