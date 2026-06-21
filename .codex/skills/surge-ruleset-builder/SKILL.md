---
name: surge-ruleset-builder
description: Research, create, refine, and validate Surge external RULE-SET files. Use when Codex is asked to generate a Surge rule collection for a service or category, compare community rule repositories, search online for missing domains or IP ranges, convert a rule file to .list, reduce false positives, or save a ruleset in the current project.
---

# Surge Ruleset Builder

Create compact, complete, auditable Surge external rulesets. Prefer verified service-specific coverage over blindly merging large community lists.

## Project Preferences

Apply these repository-specific choices before generic ownership or upstream conventions:

- Store generated rulesets in `Rule/` unless the user requests another path.
- Keep GitHub separate from Microsoft. Exclude GitHub, GitHub Pages, GitHub assets, GitHub user content, and GitHub Copilot domains from `Microsoft.list`; route broad GitHub service/content suffixes through `Global.list`, Copilot through `AI.list`, and only explicit download-asset hosts such as `release-assets.githubusercontent.com` through `CDN.list`.
- Do not put broad GitHub parent suffixes such as `githubusercontent.com`, `githubassets.com`, or `github.io` in `CDN.list`; they catch ordinary GitHub content before `Global.list`.
- Treat `fast.com` as a speed-test service. Keep it only in `Speedtest.list`, not in `Netflix.list`, `GlobalMedia.list`, or `Global.list`.
- Omit `no-resolve` from `China_IP.list` so unmatched domains can be resolved locally and classified by their Mainland IP address. Put proxy domain rules before `China_IP.list`, and put `China_IP.list` before the final fallback.
- Use first-match order deliberately when broad provider or country rules overlap focused services: service-specific rules such as YouTube, Telegram, WeChat, Netflix, Speedtest, and AI should precede provider/category rules such as Google, Microsoft, GlobalMedia, CDN, Global, China, and China_IP.
- Keep automated publish workflows aligned with local policy. The workflow should build generated `Rule/*.list` files from `Rule/Manual/*.txt` plus current upstream sources only, apply `Rule/Manual/*.exclude.txt`, convert explicit domainset sources, filter upstream marker/test domains, and enforce repository guardrails before writing output.
- Treat borrowed workflows as automation mechanics only. Do not assume a reference repository's source choices, local manual preferences, or final rule semantics match this project; map every generated file to the user's selected upstreams and guardrails explicitly.
- Do not preserve the current generated `Rule/*.list` files as an automation baseline. Existing generated files can silently retain upstream withdrawals and stale local mistakes. Move durable local additions into `Rule/Manual/*.txt` and durable removals into `Rule/Manual/*.exclude.txt`.
- Strip upstream inline trailing comments during source cleaning. In Surge external rulesets, a line such as `DOMAIN-SUFFIX,example.com # note` is not a comment-bearing rule; the note becomes part of the hostname and should fail validation.
- Do not accept undocumented wildcard rule types such as `DOMAIN-WILDCARD` in generated `.list` files unless current official Surge documentation explicitly confirms support. Convert to documented exact or suffix rules only when the wildcard can be narrowed safely; otherwise exclude it.
- Route broad shared CDN parent suffixes through `CDN.list` when the repository has a CDN policy, not through service, media, provider, China direct, or broad Global rulesets. Examples include Akamai, CloudFront, AzureEdge, Fastly, Bunny, and CDN77 parent domains.
- Remove exact overlap between peer rulesets that assign different policies, such as `Microsoft.list` versus `Microsoft_CDN.list`, `Global.list` versus `CDN.list`, and `GlobalMedia.list` versus `CDN.list`. Preserve only intentional parent-child first-match overlap.
- Keep `China.list` as a Mainland/direct domain fallback, not a catch-all for Chinese-owned overseas products. Remove overseas media, short-video, social-video, and foreign sports/media domains from China rules unless the user explicitly requests a direct fallback exception. Judge actual routing by configured first match, but do not use first-match order to justify retaining clearly non-China entries in `China.list`.
- Prefer the user's selected automated sources unless they become unavailable or inaccurate: blackmatrix7 `ChinaMaxNoIP_Domain.list` for the expanded `China.list` domain inventory, SukkaW `Source/domainset/speedtest.conf` plus a manual `DOMAIN-SUFFIX,fast.com` for `Speedtest.list`, SukkaW Apple/Microsoft CDN outputs for regional CDN rules, Telegram's official `resources/cidr.txt` for Telegram CIDR coverage, and blackmatrix7 Disney/PayPal for those service rules.
- Preserve these choices when importing or synchronizing upstream rules. Report an upstream conflict instead of silently restoring a removed rule.
- Filter SukkaW's marker/test domain `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe` during source cleaning and validate that it is absent from generated output.

## Workflow

1. Read `references/sources.md` and `references/Learned Patterns.md`, then select the relevant official and community sources.
2. Read the current project ruleset before modifying it, but do not treat generated `Rule/*.list` files as durable baseline input. Preserve intentional local entries by moving them to `Rule/Manual/*.txt`; remove durable exclusions through `Rule/Manual/*.exclude.txt`.
3. Check current Surge syntax in the official documentation when syntax or feature support is uncertain. Follow the official source priority: release log, then Manual, then Knowledge Base.
4. Compare at least two relevant community sources. For major streaming services, compare all fixed repositories listed in `references/sources.md` when practical.
5. Search the web for recent official domain, ASN, network, API endpoint, or client information. Prefer official service documentation, RIR/BGP data, and repository source files.
6. Define the ruleset's intended product surface before selecting candidates, such as consumer playback versus corporate, investor, studio, or engineering sites. For requests using words such as "all" or "every", turn the scope into an explicit product-category inventory and state that coverage is current and evidence-based rather than permanently exhaustive.
7. Measure large upstream lists by rule type and ownership. Treat generated cloud-provider ranges as candidates for verification, not evidence that every address belongs in the final ruleset.
8. Build a normalized candidate set, then remove duplicates, covered entries, stale entries, unrelated product surfaces, and high-risk shared infrastructure. Treat a CIDR subnet covered by a broader CIDR in the same policy file as redundant and remove it. Compare sibling rulesets in the project when products share a provider or infrastructure.
9. For category or repository-wide work, assign each rule to an ownership layer such as dedicated service, regional direct, CDN, broad global, or IP fallback. Define the intended first-match order before resolving cross-file overlap.
10. Save the result as `<Service>.list` in the user's requested project directory. In this repository, default to `Rule/` when no path is given.
11. When changing automation, update the workflow source inventory and generated files together. Re-run local generation when practical, confirm all external URLs are reachable, and verify the workflow's `process_rule` inventory matches the repository's `.list` files. Also verify the workflow has project-policy checks, not only cleanup filters. In this repository, run `python3 scripts/validate_surge_repo.py` before committing workflow or ruleset changes; the main workflow also runs this script after generation.
12. Delete obsolete legacy workflows instead of retaining them. If a legacy workflow must be retained for rare reference, give it a unique `name:`, remove `schedule`, and document that it must not regenerate stale rule inventories.
13. Validate the file and report the path, rule count, important inclusions, and deliberate exclusions. For a final repository audit, validate every `.list`, re-fetch time-sensitive canonical sources, and test representative first-match behavior across related files. Treat a later broad-match hit as harmless when an earlier focused rule is the actual configured first match.
14. Run the continuous-improvement review below. Update the skill only when the task produced durable, verified knowledge.

## Construction Rules

- Produce a Surge external ruleset, not a complete Surge profile.
- Put one rule on each line and never append a policy name. The main profile assigns the policy in its `RULE-SET` line.
- Use `.list` by default. Convert `.txt` to `.list` when requested without changing content unnecessarily.
- Convert explicit domainset inputs before merging into a Surge `.list`: `.example.com` becomes `DOMAIN-SUFFIX,example.com`, a bare hostname becomes `DOMAIN,hostname`, and upstream marker domains or metadata lines should be removed.
- Name files consistently: capitalize the first filename segment, preserve established service capitalization, and write segments after `_` in uppercase, such as `Apple_CN.list` and `China_IP.list`. Correct obvious spelling drift and update all textual references after a rename.
- Use ASCII comments beginning with `#`. Keep headers short and include the update date and source repositories.
- Prefer `DOMAIN` for a single host, `DOMAIN-SUFFIX` for an owned domain tree, and `DOMAIN-KEYWORD` only for stable dynamic naming patterns.
- Do not treat upstream wildcard-looking host patterns as Surge rules. If a source uses glob syntax, either replace it with a verified safe suffix or exact host inventory, or exclude it and document why.
- Treat a product website as ownership evidence, not automatic proof that every vendor domain is a runtime dependency. Prefer official endpoint documentation, client source, reproducible traffic, or agreement between independent current sources for supporting hosts.
- Add `no-resolve` to `IP-CIDR` and `IP-CIDR6` unless IP matching must resolve domain requests. This repository intentionally omits it from `China_IP.list` for local DNS-based Mainland classification. With `no-resolve`, Surge skips that IP rule when the request target is still a domain.
- Include `USER-AGENT` or `PROCESS-NAME` only as documented client fallbacks. `USER-AGENT` applies only to HTTP/HTTPS requests, while `PROCESS-NAME` is Mac-only and ignored by Surge iOS; neither is primary cross-platform coverage.
- Keep ruleset-wide options such as `extended-matching` in the main profile's `RULE-SET` declaration. Enable it only when SNI and HTTP Host or `:authority` matching is required.
- Allow documented Surge logical rule types such as `AND`, `OR`, and `NOT` when they appear as policy-free sub-rules in an external ruleset.
- Order rules as exact domains, domain suffixes, domain keywords, IPv4, IPv6, then client fallbacks.

## Precision Policy

- Do not copy an upstream list wholesale merely because it is large or popular.
- Exclude broad AWS, CloudFront, Azure, Google Cloud, or other shared cloud ranges unless they are demonstrably dedicated to the target service or the user explicitly requests maximum-coverage mode.
- Exclude shared consent, analytics, telemetry, CDN, and identity domains such as generic OneTrust domains unless the target service fails without them and the match can be narrowed.
- Prefer service-owned ASN prefixes over shared cloud-provider prefixes.
- For streaming services, use owned delivery-network prefixes for IP fallback and use verified domains for cloud-hosted control-plane traffic. Do not substitute all provider-published cloud ranges for service ownership.
- Keep consumer-service rulesets focused on login, API, media, search, playback, and diagnostics. Exclude corporate or editorial properties unless the requested policy intentionally covers the whole company.
- When third-party clients are in scope, separate their proprietary control-plane domains from the official service. Prefer exact API hosts or client-owned suffixes, and exclude generic hosting, analytics, and unrelated product domains.
- Remove client fallback rules that cannot match on the user's target platforms, even when they appear in a popular upstream list.
- Collapse numbered or generated host families into a safe `DOMAIN-KEYWORD` only when the pattern is specific enough to avoid unrelated matches.
- Do not encode IP address fragments as `DOMAIN-KEYWORD`. Convert verified network targets to bounded `IP-CIDR` or `IP-CIDR6` rules; otherwise exclude them.
- Remove an exact domain when an included `DOMAIN-SUFFIX` already covers it, unless ordering or exceptional behavior makes the exact rule meaningful.
- When a child product must be excluded from a provider-wide ruleset, do not retain a parent suffix or keyword that still matches the child. Surge external rulesets cannot express negative child-domain exceptions; use explicit service hosts, or clearly document a first-match load-order dependency when broad coverage is more important than strict separation.
- Distinguish ownership from geography. A Chinese company can operate overseas subdomains, and a foreign company can operate verified Mainland delivery endpoints. Keep the broad owner suffix only when useful, place verified geographic exceptions in an earlier ruleset, and test the intended first match.
- For China direct rules, classify by Mainland routing intent rather than company origin. International services from Chinese-owned brands, Hong Kong/Taiwan/global media, TikTok/ByteDance overseas domains, Kwai overseas domains, and global sports/media domains belong in their focused or global category, not `China.list`.
- Treat cross-file overlap as a routing decision, not automatically as duplication. Remove accidental overlap between peer categories such as `CDN` and `Global`; retain justified parent-child overlap when a narrower earlier rule intentionally overrides a broad later category. Document the required load order in both files.
- Keep diagnostic products in their functional category. For example, a speed-test hostname associated with a streaming vendor belongs in the speed-test ruleset when the policy is based on function rather than corporate ownership.
- Treat a wider network prefix as a replacement only after verifying ownership and route origin; never widen CIDRs by visual inference alone.
- For generated geographic IP rulesets, compare the local set against the current canonical route source by exact additions and removals. Apply withdrawals as well as additions, collapse losslessly, and do not union allocation-oriented or overseas-announced operator ranges into a route-origin set merely to increase coverage.
- Separate optional aggressive coverage from the default ruleset instead of weakening the default set.
- For category rulesets, group entries by product class and exclude vendors outside the requested geography or ownership scope. Do not call a list "all" solely because it merges many community lists.

## Validation

Before finishing, verify:

- The file exists and has the `.list` extension.
- Every non-comment line begins with a supported Surge rule type.
- No rule contains a policy name.
- There are no exact duplicate rules.
- CIDRs are syntactically valid and follow the ruleset's resolution policy: `no-resolve` by default, except `China_IP.list` in this repository.
- No `IP-CIDR` or `IP-CIDR6` rule is a redundant subnet of a broader CIDR in the same policy file.
- `China.list` is domain-only, `China_IP.list` carries Mainland IPv4/IPv6 fallback without `no-resolve`, and all other real `IP-CIDR`, `IP-CIDR6`, and `IP-ASN` rules carry `no-resolve`.
- No IP address fragment is encoded as `DOMAIN-KEYWORD`, including dotted prefixes such as `DOMAIN-KEYWORD,101.226.129.`.
- `Microsoft.list` contains no GitHub family rules, broad GitHub content suffixes hit `Global.list`, `release-assets.githubusercontent.com` is the only intended GitHub CDN exception, and `fast.com` exists only in `Speedtest.list`.
- Domain entries are lowercase and do not include URL schemes or paths.
- Broad shared-provider entries have a written justification or are removed.
- Representative positive samples for every product class match the final ruleset.
- Explicit exclusions and sibling-product negative samples do not match the final ruleset.
- Cross-file overlap is intentional and documented when related project rulesets can match the same hostname.
- Peer rulesets with different policies have no exact overlap unless a documented first-match exception requires it. Dedicated CDN/resource rules should not remain duplicated in their parent provider or broad category file.
- Peer-category semantic overlap is checked in both directions: exact-in-suffix, suffix-in-suffix, and child exceptions beneath broad parents. The documented first-match order is tested with representative hosts.
- Explicit negative samples are evaluated through the configured profile order. A domain that appears in a later broad fallback ruleset is not a routing error if an earlier focused ruleset intentionally catches it first.
- Current canonical network sources are compared against local CIDRs for both missing and stale prefixes; the final networks remain losslessly collapsed.
- Filenames and internal references follow the project naming convention, and renamed files leave no stale references.
- The final rule count matches the reported count.

Supported common types include `DOMAIN`, `DOMAIN-SUFFIX`, `DOMAIN-KEYWORD`, `IP-CIDR`, `IP-CIDR6`, `IP-ASN`, `USER-AGENT`, `PROCESS-NAME`, and documented logical wrappers such as `AND`, `OR`, and `NOT`. Verify less common types against current Surge documentation before using them.

## Write Safety

- Save locally first unless the user explicitly requests a GitHub write.
- Do not commit, push, or overwrite a remote file without explicit user intent and adequate repository permission.
- When an existing file changes, summarize meaningful additions, removals, prefix corrections, and false-positive protections.

## Continuous Improvement

After each completed ruleset task:

1. Identify any repeated failure, missing validation, ambiguous instruction, newly reliable source class, or reusable false-positive lesson.
2. Decide whether the lesson applies across multiple services or future tasks. Do not generalize from one unexplained endpoint or one community list.
3. If durable and verified, make the smallest useful update to this skill. Keep workflow changes in `SKILL.md` and detailed reusable findings in `references/Learned Patterns.md`.
4. Remove or replace guidance when current official documentation disproves it. Preserve no obsolete advice merely for history.
5. Check that `agents/openai.yaml` still represents the skill accurately, then run the Skill validator after changes.

Do not modify the skill when a task yields no reusable improvement. Skill edits must improve future execution rather than record task history.
