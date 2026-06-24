# Third-Party Shared Service & Domestic Domain Pruning

Community rule lists (blackmatrix7, SukkaW, etc.) often include shared third-party service domains that are NOT specific to the service the list is named after. They also include China-domestic variants that should route DIRECT, not through a proxy policy. Both categories cause incorrect routing if left in place.

## Third-Party Shared Service Pattern

### Identification

A domain in a service-specific ruleset (e.g., `Netflix.list`, `Disney.list`) is a "shared third-party service" when:

1. The domain belongs to a well-known SaaS/analytics/CDN platform.
2. The same domain is used by thousands of unrelated websites.
3. Including it would route all traffic to that platform through the service's proxy policy — far beyond the intended scope.

### Common Shared Services Found in Media/Service Rules

| Shared service | Used by | Why it's too broad |
|---|---|---|
| `cookielaw.org` | OneTrust cookie consent | Thousands of sites use this |
| `onetrust.com` | OneTrust privacy management | Thousands of sites use this |
| `adobedtm.com` | Adobe Tag Manager | Used on many non-Disney sites |
| `braze.com` | Marketing/engagement platform | Used by many apps |
| `conviva.com` | Video analytics | Used by many streaming services |
| `cdn.optimizely.com` | A/B testing CDN | Used across the web |
| `bam.nr-data.net` | New Relic data collection | Generic telemetry |
| `js-agent.newrelic.com` | New Relic JS agent | Generic telemetry |
| `d9.flashtalking.com` | Flashtalking ad tracking | Ad tech, not service-specific |
| `execute-api.us-east-1.amazonaws.com` | AWS API Gateway | Entire AWS service |
| `us-west-2.amazonaws.com` | AWS region | Entire AWS region |
| `hsprepack.akamaized.net` | Akamai CDN | May serve other clients |
| `demdex.net` | Adobe AudienceManager | Cross-site tracking |
| `sentry.io` | Error tracking | Used by thousands of apps |
| `segment.io` | Customer Data Platform (CDP) | Used by thousands of apps |
| `omtrdc.net` | Adobe Analytics | Used across many sites |
| `flashtalking.com` | Ad serving | Generic ad tech |
| `newrelic.com` | APM/monitoring | Generic observability |

### Decision Rule: Prefix-Based Filtering

When a third-party service domain has a **service-specific subdomain prefix**, it CAN be kept:

| Entry | Verdict | Reason |
|---|---|---|
| `DOMAIN-SUFFIX,conviva.com` | ❌ Exclude | Too broad |
| `DOMAIN-SUFFIX,cws.conviva.com` | ✅ Keep | `cws` is Conviva's Disney-specific subdomain |
| `DOMAIN-SUFFIX,onetrust.com` | ❌ Exclude | Too broad |
| `DOMAIN-SUFFIX,disney-portal.my.onetrust.com` | ✅ Keep | Has `disney` prefix |
| `DOMAIN-SUFFIX,omtrdc.net` | ❌ Exclude | Too broad |
| `DOMAIN-SUFFIX,disneyplus.com.ssl.sc.omtrdc.net` | ✅ Keep | Has `disneyplus` prefix |
| `DOMAIN-SUFFIX,espn.hb.omtrdc.net` | ✅ Keep | Has `espn` prefix |
| `DOMAIN-SUFFIX,demdex.net` | ❌ Exclude | Too broad |
| `DOMAIN-SUFFIX,disney.demdex.net` | ✅ Keep | Has `disney` prefix |
| `DOMAIN-SUFFIX,amazonaws.com` | ❌ Exclude | Far too broad |
| `DOMAIN-SUFFIX,execute-api.us-east-1.amazonaws.com` | ❌ Exclude | Still too broad (shared API Gateway) |
| `DOMAIN-SUFFIX,o207216.ingest.sentry.io` | ❌ Exclude | Opaque ingest endpoint — not service-prefixed |
| `DOMAIN-SUFFIX,disney.my.sentry.io` | ✅ Keep | Has `disney` prefix |

### Opaque Subdomain Detection

Some shared infrastructure subdomains have **opaque IDs** instead of brand prefixes. These do NOT qualify as "service-prefixed":

- `o207216.ingest.sentry.io` — opaque hex/numeric project ID, not a brand
- `o33249.ingest.sentry.io` — same pattern
- `e13252.dscg.akamaiedge.net` — numeric edge node ID (Akamai)

**Heuristic for "is this service-specific?":**
- First label is all-digits (`o207216` → treat `o207216` as opaque? actually `o207216` starts with `o` then digits — consider as opaque when short, digit-heavy, and not a recognizable brand)
- First label is all-hex (no recognizable brand)
- First label is ≤6 characters with mixed letters and digits (too short for a brand prefix)

When in doubt, exclude — the brand-prefixed variants will still pass through.

### grep -vFf Limitation with Subdomain Excludes

The workflow uses `grep -vFf "$exclude_file"` for FIXED-STRING matching. This means:

- `DOMAIN-SUFFIX,sentry.io` in the exclude file only matches the **exact string** `DOMAIN-SUFFIX,sentry.io` in the upstream source.
- It does NOT match `DOMAIN-SUFFIX,o207216.ingest.sentry.io` because the line is different.
- **Workaround:** add shorter substring patterns without the rule-type prefix, e.g., `.ingest.sentry.io`. These match as substrings of any line containing them.
- BUT: `.ingest.sentry.io` also matches `DOMAIN,some.ingest.sentry.io` and any other line — be specific enough to avoid over-excluding.

### Implementation

Add excluded entries to `Rule/Manual/<Service>.exclude.txt`. The next workflow run removes them from the generated `.list`.

## Service-Owned Infrastructure (Not Shared Third-Party)

Some suffixes that look like shared infrastructure are actually **owned by the service** and belong in its ruleset:

| Service | Owned Suffixes | Example |
|---------|---------------|---------|
| Google | `doubleclick.net`, `googleadservices.com`, `googleapis.com`, `googlesyndication.com`, `googletagmanager.com`, `googleanalytics.com` | Google's own ad/analytics/API infrastructure |
| Microsoft | `azure.com`, `live.com`, `msn.com`, `microsoftonline.com`, `office.com`, `office365.com` | Microsoft's own cloud/identity/office infra |
| Meta | `facebook.net`, `fbcdn.net`, `fbsbx.com`, `instagram.com` | Meta's own CDN and services |
| Apple | `apple.com`, `icloud.com`, `icloud-content.com`, `me.com` | Apple's own service infra |
| Amazon | `amazon.com`, `amazonaws.com` (careful — AWS is shared) | Amazon's own commerce and cloud |

**Decision rule:** if a suffix appears in a ruleset named after that company, it is NOT shared third-party — do not flag it. Audit tools must maintain a `SERVICE_OWNED_SUFFIXES` exemption dict mapping target file → set of owned suffixes to suppress false positives.

Conversely: `optimizely.com` in `Microsoft.list` IS shared third-party (Microsoft does not own Optimizely).

## Domestic Domain Re-Routing Pattern

### Identification

When a service's global ruleset contains country-code domains (especially `.cn`) that serve local users through domestic infrastructure, routing them through a proxy policy is incorrect. Examples:

- PayPal China: `anfutong.cn`, `beibao.cn`, `paypal.com.cn`, `paypalhere.cn` (安付通/贝宝)
- These are separate China-local products/brands, not the same as the global PayPal service.

### Implementation

1. Add the domestic domains to `Rule/Manual/<Service>.exclude.txt` — prevents re-entry from upstream.
2. Add the same domains to `Rule/Manual/China.txt` — ensures they enter `China.list` for DIRECT routing.
3. The service rule is earlier in first-match order, so excluding from it allows `China.list` (later, DIRECT policy) to catch these domains.

### Why Not Just Edit the .list?

The `.list` files are auto-generated. Direct edits get overwritten on the next scheduled sync. The Manual exclude files are the durable source of truth.

## AI (linnux-x/surge)

Position 3. 141 rules (compact: AIGC + AI tools + Apple Intelligence).

**Excluded shared infrastructure (segment.io + sentry.io):**
- `segment.io` — Customer Data Platform (shared across thousands of sites)
- `sentry.io` — Error tracking (shared across thousands of apps)
- `.ingest.sentry.io` — Opaque ingest endpoints (e.g., `o207216.ingest.sentry.io`) — caught by substring match

**Kept (AI-prefixed):** no service-branded sentry/segment variants found in AI.context.

**Rule count:** 53 Manual + 63 Rabbit-Spec AIGC + 22 SukkaW AI + 5 SukkaW Apple Intelligence.

## PayPal (linnux-x/surge)

Position 14. 234 rules. No downstream overlaps.

**Excluded to China/DIRECT:** 14 `.cn` domains (anfutong, beibao, paypal.com.cn, paypalhere, xoom.net.cn, xn--bnq297cix3a.cn).
**Note:** `venmo.s3.amazonaws.com` uses DOMAIN-SUFFIX but is effectively exact-match at 4 labels deep — no action needed.

## Netflix (linnux-x/surge)

Position 16. 1154 rules (32 domain + 1115 IP-CIDR).

**Excluded 3 overly broad shared domains:**
- `cookielaw.org` → OneTrust cookie consent (thousands of sites)
- `onetrust.com` → OneTrust privacy management (thousands of sites)
- `us-west-2.amazonaws.com` → entire AWS region

**Kept (service-prefixed Akamai/EdgeSuite):** `e13252.dscg.akamaiedge.net`, `netflix.com.edgesuite.net`

**27 domain overlaps with GlobalMedia.list** — Netflix is earlier, so these are semantically redundant in GlobalMedia but don't affect routing.

## Disney (linnux-x/surge)

Position 17. 166 rules.

**Excluded 9 non-Disney third-party services:**
- `adobedtm.com`, `bam.nr-data.net`, `braze.com`, `cdn.optimizely.com`
- `conviva.com`, `d9.flashtalking.com`, `js-agent.newrelic.com`
- `execute-api.us-east-1.amazonaws.com`, `hsprepack.akamaized.net`

**Kept (Disney/ESPN-prefixed subdomains):**
- `disney.demdex.net`, `disneyplus.com.ssl.sc.omtrdc.net`
- `espn.hb.omtrdc.net`, `espndotcom.tt.omtrdc.net`
- `abcnews.edgesuite.net`, `disney-portal.my.onetrust.com`
- `disney.my.sentry.io`, `cws.conviva.com`

**154 domain overlaps with GlobalMedia.list** — Disney is earlier, so redundant in GlobalMedia but doesn't affect routing.
