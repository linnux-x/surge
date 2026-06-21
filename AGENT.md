# AGENT.md

## User Context

- The user travels globally, especially across mainland China, Hong Kong, Japan, and the United States.
- The primary devices are iPhone and MacBook, with Surge used for proxy routing and traffic classification.
- Rules must remain useful across regions without assuming that every platform supports the same fallback types.
- The user's repository-specific classification choices override generic corporate ownership groupings.

## Project Preferences

- Store rulesets in `Rule/`.
- Keep all GitHub family domains out of `Microsoft.list`. Route GitHub service and broad content-hosting domains through `Global.list`, Copilot through `AI.list`, and only explicit download-asset hosts such as `release-assets.githubusercontent.com` through `CDN.list`.
- Do not put broad GitHub parent suffixes such as `githubusercontent.com`, `githubassets.com`, or `github.io` in `CDN.list`; they would steal ordinary GitHub content before `Global.list`.
- Keep `fast.com` only in `Speedtest.list`; exclude it from `Netflix.list`, `GlobalMedia.list`, and `Global.list`.
- Omit `no-resolve` from `China_IP.list` so unmatched domains can be resolved locally before Mainland IP classification. Proxy domain rules must precede `China_IP.list`.
- Load focused service rules before broad provider and country rules. In particular, place YouTube before Google, WeChat before China, CDN before Global when CDN routing differs, and China before China_IP.
- Maintain `.github/workflows/auto-rules.yml` when rule sources change. It should regenerate files in `Rule/` from `Rule/Manual/*.txt` plus current upstream sources only, apply `Rule/Manual/*.exclude.txt`, convert supported domainset sources, filter known upstream marker/test domains, and enforce repository-specific guardrails.
- Treat reference workflows as mechanics, not policy. When adapting Rabbit-Spec, SukkaW, blackmatrix7, or other automation, explicitly remap sources and guardrails to this repository instead of inheriting the reference repository's final rule semantics.
- Do not preserve the current generated `Rule/*.list` files as an automation baseline. Existing generated files can contain stale upstream withdrawals; durable local intent belongs in `Rule/Manual/*.txt` or `Rule/Manual/*.exclude.txt`. Guardrails must run after manual and upstream merge, before writing output.
- Always filter SukkaW's marker/test domain `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe` during source cleaning so it never reaches generated rules.
- Strip upstream inline trailing comments before validation, because rules such as `DOMAIN-SUFFIX,example.com # note` make the comment part of the hostname in a Surge external ruleset.
- Do not allow `DOMAIN-WILDCARD` in generated `.list` files unless current official Surge documentation explicitly confirms support. Prefer documented `DOMAIN`, `DOMAIN-SUFFIX`, and `DOMAIN-KEYWORD` forms.
- Keep shared CDN parent suffixes such as Akamai, CloudFront, AzureEdge, Fastly, Bunny, and CDN77 out of service, media, provider, and China direct rulesets. Route broad shared CDN parents through `CDN.list` when a CDN policy is intended, and de-duplicate them from `Global.list`.
- Remove exact overlap between peer rulesets that have different policies, such as `Microsoft.list` versus `Microsoft_CDN.list`, `Global.list` versus `CDN.list`, and `GlobalMedia.list` versus `CDN.list`. Keep only intentional first-match parent-child overlap.
- Keep `China.list` as a Mainland/direct domain fallback, not a catch-all for Chinese-owned overseas products. Remove overseas media, short-video, social-video, and foreign sports/media domains such as international iQIYI/Bilibili/WeTV/JOOX/Kwai/NBA/TikTok-related entries from `China.list` unless the user explicitly requests a direct fallback exception.
- Leave `rmonitor.qq.com` under the broad `qq.com` China direct fallback; do not classify it as WeChat unless the user explicitly changes that policy.
- Current automated source choices include blackmatrix7 `ChinaMaxNoIP_Domain.list` for the expanded `China.list` domain inventory, SukkaW `Source/domainset/speedtest.conf` plus manual `fast.com` for `Speedtest.list`, SukkaW Apple/Microsoft CDN outputs for regional CDN rules, Telegram's official `resources/cidr.txt` for Telegram CIDR coverage, and blackmatrix7 Disney/PayPal for those service rules.
- Do not reintroduce these entries from an upstream list during synchronization without explicit user approval.

## Core Task

Research, create, optimize, and validate reusable Surge external rulesets. Save each result as a `.list` file in this project unless the user specifies another path.

## Required Workflow

1. Use `.codex/skills/surge-ruleset-builder/SKILL.md` for ruleset work and read its required references.
2. Define the requested product, geography, client, and feature scope before collecting rules. Convert requests for "all" services into an explicit current category inventory; do not promise permanent exhaustiveness.
3. Prefer current official documentation, official client source, service-owned domains, RIR/BGP data, and reproducible traffic evidence.
4. Compare at least two maintained community sources. Treat community lists as candidate inventories rather than authority.
5. Preserve justified local rules through `Rule/Manual/*.txt` or `Rule/Manual/*.exclude.txt`, then normalize and remove duplicates, covered entries, stale services, unrelated properties, and shared infrastructure with excessive false-positive risk.
6. For provider families such as Google and YouTube, compare sibling project rulesets and test both intended matches and explicit exclusions. Do not use a broad parent suffix or keyword when a child product must be excluded.
7. For third-party clients, separate proprietary client backends from the official service data plane. Include only verified client-owned API hosts or suffixes.
8. Prefer `DOMAIN`, then safe `DOMAIN-SUFFIX`, and use `DOMAIN-KEYWORD` only for stable service-specific patterns. Never put a policy name in an external ruleset.
9. Add `no-resolve` to IP rules unless resolution is intentionally required. `China_IP.list` is the project exception and must omit it for local DNS classification. Include IP ranges only after verifying boundaries, registration, and current route origin when practical.
10. Keep `China.list` domain-only. Put Mainland IPv4/IPv6 fallback only in `China_IP.list`; do not move foreign vendor or overseas cloud single-host IPs into China IP merely because a community list labels them DIRECT.
11. Allow documented Surge logical rules such as `AND`, `OR`, and `NOT` when upstream rulesets use them without policy names.
12. Use `USER-AGENT` and `PROCESS-NAME` only as documented platform-specific fallbacks. Do not treat Android package names or Mac-only process rules as iOS coverage.
13. Exclude generic analytics, telemetry, consent, identity, payment, CDN, shared cloud ranges, and volatile single-host IP rules unless they are necessary and narrowly justified.
14. Keep comments in `.list` files concise ASCII and save text files as UTF-8.
15. Classify broad repository rules by routing layer: dedicated regional rules first, then CDN, broad Global, China domains, China IPs, and fallback when that ordering matches the requested policy. Record a different order explicitly when needed.
16. Distinguish geographic routing from corporate ownership. Preserve verified overseas child exceptions above broad Chinese provider suffixes, and keep verified Mainland endpoints of foreign vendors in focused regional rulesets.
17. Use consistent filenames: capitalize the first segment, preserve service branding, and uppercase every segment after `_`, for example `SocialMedia.list`, `Apple_CN.list`, and `China_IP.list`. Update all references after renaming.

## Validation

Before finishing:

1. Verify every non-comment line uses a supported Surge rule type and contains no policy name.
2. Check exact duplicates, parent-suffix coverage, suffix-to-suffix coverage, lowercase domains, URL fragments, and CIDR syntax.
3. Test representative positive domains for every product class.
4. Test explicit exclusions and sibling-product domains as negative samples.
5. Audit overlaps with related `.list` files and document intentional shared infrastructure.
6. Check semantic overlap in both directions, including exact domains beneath suffixes, narrower suffixes beneath broader parents, and CIDR prefixes covered by broader prefixes in the same policy file. Remove peer-category overlap such as CDN versus Global; keep only intentional first-match exceptions with a documented load order.
7. For geographic IP sets, compare against the current canonical route source for both additions and withdrawals, verify lossless CIDR collapse, and keep allocation-oriented or overseas-announced operator ranges separate from Mainland route-origin coverage.
8. Test repository-level first-match behavior with representative hosts from regional direct, CDN, Global, China, and IP fallback categories. Judge negative samples by the first matching configured `RULE-SET`, not by whether a later broad ruleset would also match.
9. Compare rule counts and rule types with major upstreams, explaining differences by ownership and false-positive risk.
10. Report the saved path, final rule count, major additions, removals, and deliberate exclusions.
11. Confirm that `Microsoft.list` has no GitHub family rules, broad GitHub content suffixes hit `Global.list`, `release-assets.githubusercontent.com` is the only intended GitHub CDN exception, `fast.com` appears only in `Speedtest.list`, `China.list` contains no IP rules, `China_IP.list` contains no `no-resolve` option, all other IP rules include `no-resolve`, no dotted IP fragment is stored as `DOMAIN-KEYWORD`, and no IP rule is a redundant subnet of another IP rule in the same file.
12. When the automation workflow changes, run a full local regeneration when possible, then run `python3 scripts/validate_surge_repo.py`. Confirm every configured upstream URL is reachable, compare the generated file set with the workflow rule inventory, make project guardrail violations fail validation before committing, and keep any retained legacy workflow uniquely named with no `schedule` trigger.

## Skill Maintenance

- After real ruleset work, update the skill only when a durable, reproducible lesson improves future tasks.
- Keep workflow instructions in `SKILL.md`, detailed sources in `references/sources.md`, and reusable findings in `references/Learned Patterns.md`.
- Check `agents/openai.yaml` after skill changes and run the official skill validator when its dependencies are available.
- Never weaken source traceability or false-positive protections merely to increase the rule count.

## Completion Standard

A task is complete only after the ruleset is saved, syntax and overlap checks pass, positive and negative samples are tested, current canonical network sources have no unexplained local additions or withdrawals, filename references are consistent, source differences are explained, and skill-maintenance review is finished.
