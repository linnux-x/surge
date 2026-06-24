# AGENT.md

## Routing Strategy

- Store rulesets in `Rule/`.
- Keep all GitHub family domains out of `Microsoft.list`. Route GitHub service and broad content-hosting domains through `Global.list`, Copilot through `AI.list`, and only explicit download-asset hosts such as `release-assets.githubusercontent.com` through `CDN.list`.
- Do not put broad GitHub parent suffixes such as `githubusercontent.com`, `githubassets.com`, or `github.io` in `CDN.list`; they would steal ordinary GitHub content before `Global.list`.
- Keep `fast.com` only in `Speedtest.list`; exclude it from `Netflix.list`, `GlobalMedia.list`, and `Global.list`.
- Omit `no-resolve` from `China_IP.list` so unmatched domains can be resolved locally before Mainland IP classification. Proxy domain rules must precede `China_IP.list`.
- Load focused service rules before broad provider and country rules. In particular, place YouTube before Google, WeChat before China, Download before Game for download CDN hosts, CDN before Global when CDN routing differs, and China before China_IP.
- Keep `China.list` as a Mainland/direct domain fallback, not a catch-all for Chinese-owned overseas products. Remove overseas media, short-video, social-video, and foreign sports/media domains such as international iQIYI/Bilibili/WeTV/JOOX/Kwai/NBA/TikTok-related entries from `China.list`.
- Keep Mainland China game download/cache endpoints out of `Game.list` when they are usable directly in China. Put durable exclusions in `Rule/Manual/Game.exclude.txt` and direct entries in `Rule/Manual/China.txt`.
- Remove exact overlap between peer rulesets that have different policies, such as `Microsoft.list` versus `Microsoft_CDN.list`, `Global.list` versus `CDN.list`, and `GlobalMedia.list` versus `CDN.list`. Keep only intentional first-match parent-child overlap.
- Leave `rmonitor.qq.com` under the broad `qq.com` China direct fallback; do not classify it as WeChat.

## Rule Authoring

1. Prefer current official documentation, official client source, service-owned domains, RIR/BGP data, and reproducible traffic evidence.
2. Compare at least two maintained community sources. Treat community lists as candidate inventories rather than authority.
3. Prefer `DOMAIN`, then safe `DOMAIN-SUFFIX`, and use `DOMAIN-KEYWORD` only for stable service-specific patterns. Never put a policy name in an external ruleset.
4. Add `no-resolve` to IP rules unless resolution is intentionally required. `China_IP.list` is the project exception and must omit it for local DNS classification.
5. Keep `China.list` domain-only. Put Mainland IPv4/IPv6 fallback only in `China_IP.list`.
6. For provider families such as Google and YouTube, compare sibling project rulesets and test both intended matches and explicit exclusions.
7. For third-party clients, separate proprietary client backends from the official service data plane.
8. Exclude generic analytics, telemetry, consent, identity, payment, CDN, shared cloud ranges, and volatile single-host IP rules unless necessary and narrowly justified.
9. Keep comments concise ASCII and save text files as UTF-8.
10. Use consistent filenames: capitalize the first segment, preserve service branding, and uppercase every segment after `_`, for example `SocialMedia.list`, `Apple_CN.list`, and `China_IP.list`.

## Pipeline Rules

- Maintain `.github/workflows/auto-rules.yml` when rule sources change.
- Do not preserve the current generated `Rule/*.list` files as an automation baseline. Durable local intent belongs in `Rule/Manual/*.txt` or `Rule/Manual/*.exclude.txt`.
- Always filter SukkaW's marker/test domain `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe` during source cleaning.
- Strip upstream inline trailing comments before validation — `DOMAIN-SUFFIX,example.com # note` makes the comment part of the hostname in a Surge external ruleset.
- Do not allow `DOMAIN-WILDCARD` in generated `.list` files unless Surge docs explicitly confirm support.
- Keep shared CDN parent suffixes (Akamai, CloudFront, AzureEdge, Fastly, Bunny, CDN77) out of service, media, provider, and China direct rulesets.
- Treat reference workflows as mechanics, not policy. When adapting upstream automation, explicitly remap sources and guardrails to this repository.

## Service vs Shared Infrastructure

Community rulesets often include non-service-proprietary shared infrastructure. Classify by **service ownership**, not corporate affiliation:

| Category | Example | Treatment |
|---|---|---|
| China domestic services | PayPal .cn domains | Exclude from service rules → `China.txt` → DIRECT |
| Shared analytics/telemetry | New Relic, Conviva | Exclude unless service-prefixed subdomain |
| Shared compliance/privacy | OneTrust (cookielaw.org) | Exclude — used by thousands of sites |
| Shared cloud platforms | `us-west-2.amazonaws.com` | Regional scope too broad — exclude |
| Shared CDNs | Akamai, CloudFront, Fastly | Keep only service-prefixed subdomains |
| Dedicated service CDN | `disney.my.sentry.io` | Service-prefixed — keep |

**Key principles:**
- Subdomains with explicit service/brand prefixes are service-specific.
- Avoid matching entire regions, platforms, or CDN parent suffixes.
- Third-party platforms (Adobe, New Relic, AWS) default to Global unless service-prefixed.
- China-domestic domains go to China (DIRECT), not overseas service rules.

## Online Audit Pipeline

Every workflow run must pass `scripts/audit_rules.py` before committing:

1. **Upstream reachability** — all configured source URLs must be accessible
2. **Upstream vs generated comparison** — flag abnormal rule-count ratios
3. **Shared infrastructure scan** — broader than `validate_surge_repo.py`
4. **Surge documentation check** — detect new rule types
5. **Exclude coverage** — verify exclude patterns are effective

Audit severity levels:
- 🔴 **ERROR** — blocks commit (e.g., unreachable upstream)
- 🟡 **WARN** — requires review (e.g., new shared infrastructure found)
- 🔵 **INFO** — for awareness (e.g., upstream rule count difference)

**Continuous evolution:**
- WARN findings confirmed as needing exclusion → add to `Rule/Manual/*.exclude.txt`
- New shared infrastructure patterns → update both `audit_rules.py` and `validate_surge_repo.py`

## Validation Checklist

Before finishing ruleset work:

1. Verify every non-comment line uses a supported Surge rule type and contains no policy name.
2. Check exact duplicates, parent-suffix coverage, CIDR syntax, and lowercase domains.
3. Test representative positive and negative domain samples.
4. Audit overlaps with related `.list` files and document intentional shared infrastructure.
5. Confirm: `Microsoft.list` no GitHub, `fast.com` only in `Speedtest.list`, `China.list` no IP rules, `China_IP.list` no `no-resolve`, all other IP rules have `no-resolve`.
6. Run `python3 scripts/validate_surge_repo.py` before committing.
