# Learned Patterns

Store only verified, reusable knowledge that improves future Surge ruleset work. This file is a compact operational reference, not a task log or changelog.

## Admission Criteria

Add a finding only when all conditions hold:

- It was observed or validated during a real ruleset task.
- It applies to more than one service or is a stable Surge-specific behavior.
- Its evidence can be reproduced from official documentation, authoritative network data, or multiple credible sources.
- It changes how future rules should be researched, constructed, or validated.

Do not add temporary service endpoints, unsupported guesses, task-specific source lists, or conclusions based only on one unverified repository.

## Reusable Findings

- A larger upstream list is not necessarily more complete: shared cloud, CDN, identity, analytics, and consent infrastructure often increases false positives without improving core service coverage.
- Verify network prefixes using both registration and current route origin where practical. Registration alone does not prove that a prefix is currently dedicated to the target service.
- Treat generated hostname families as keyword candidates only after confirming the stable portion is service-specific and cannot reasonably match unrelated traffic.
- Prefer updating a source or validation method over adding one-off exceptions when the same omission pattern appears in multiple rulesets.
- When a service publishes a current canonical network list, compare community additions against it and remove unexplained extras instead of assuming that more prefixes improve coverage.
- Treat single-host IP rules and community-labeled backup endpoints as volatile. Keep them only when current official data, route ownership, source code, or reproducible traffic evidence supports their purpose.
- Treat `USER-AGENT` and `PROCESS-NAME` as platform-limited fallback coverage: user-agent rules do not cover non-HTTP TCP traffic, and process rules are ignored by Surge iOS.
- Interpret `no-resolve` operationally: an IP-based rule carrying it is skipped while the request target is a domain, avoiding a DNS lookup during that rule test.
- Put ruleset-wide behavior such as `extended-matching` on the parent `RULE-SET` declaration so domain sub-rules can also inspect SNI and HTTP Host or `:authority` when needed.
- Define the intended product surface before comparing coverage. Consumer streaming rules normally need account, API, media, playback, search, and diagnostic traffic, not investor, studio, corporate, or engineering publications.
- Decompose unusually large upstream lists by rule type and network owner. Thousands of generated cloud CIDRs can dominate the rule count while adding shared-infrastructure false positives rather than dedicated service coverage.
- For cloud-hosted control planes, prefer verified service domains. Reserve IP fallback for prefixes currently originated by the service or otherwise demonstrated to be dedicated.
- Evaluate client fallbacks against the actual target platforms. An Android package name does not improve an iPhone and Mac ruleset, and a Mac process rule cannot provide iOS coverage.
- Treat dotted IP fragments stored as `DOMAIN-KEYWORD` as unnormalized network observations, not domain rules. Replace them only with ownership-verified CIDRs that have correct boundaries; otherwise omit them.
- For third-party clients of a shared protocol, distinguish the official service data plane from each client's proprietary backend. Add only verified API hosts or owned domain suffixes, not broad name keywords, shared content-hosting domains, or client analytics by association.
- A domain ruleset cannot both include a parent suffix and strictly exclude selected child hosts beneath it. Replace the parent match with explicit product hosts for strict separation; traffic sharing the same hostname but differing only by URL path cannot be separated by domain rules.
- For a CDN category, distinguish static asset delivery from arbitrary tenant hosting and shared service infrastructure. A provider suffix such as `cloudfront.net`, `azureedge.net`, `b-cdn.net`, or a hosted-app suffix can carry APIs, login traffic, media playback, and complete websites; prefer verified asset hosts and dedicated delivery suffixes unless the policy intentionally routes all tenant content.
- For GitHub, broad content suffixes such as `githubusercontent.com`, `githubassets.com`, and `github.io` are not generic CDN parents in this project. Keep them in the Global layer, and add only explicit download-asset hosts such as `release-assets.githubusercontent.com` to CDN when a separate CDN policy is desired.
- For geographic direct-routing IP sets, distinguish current route-origin coverage from registry or GeoIP country allocation. Use allocation lists as comparison inventories, but avoid a blind union when the routing policy is intended to represent traffic currently announced inside the region.
- Audit manually maintained sections of community category lists separately from their synchronized upstream data. Personal DIRECT preferences can include foreign vendor domains and overseas cloud single-host IPs that are useful to one author but are not evidence of geographic ownership.
- Treat community automation workflows as reusable plumbing, not reusable policy. Avoid using existing generated `.list` files as a preserved baseline; stale upstream withdrawals and old local mistakes will otherwise survive indefinitely. Durable local intent should live in Manual include/exclude files, followed by repository-specific cleanup and validation after every merge.
- Validate guardrails as hard checks after applying them. Cleanup filters can miss changed upstream formats; final validation should fail on domain/IP layer violations such as IP rules in a domain-only ruleset, missing `no-resolve` outside the intended IP-fallback exception, or dotted IP fragments stored as `DOMAIN-KEYWORD`.
- For repository-wide audits, evaluate false positives through the actual configured first-match order. A later broad fallback match is not a routing bug when an earlier focused ruleset catches the domain first; report it as standalone ruleset hygiene only if that matters.
- Strip inline trailing comments from upstream rules before validation. External rulesets do not support hostname-level inline comments, so the comment text would otherwise become part of the rule value.
- Do not pass through upstream wildcard-looking rule types just because a community source uses them. If current official Surge documentation does not list the type, treat it as invalid for `.list` output and either narrow it to verified `DOMAIN`/`DOMAIN-SUFFIX` entries or exclude it.
- For direct China domain rules, company origin is not enough. Chinese-owned overseas media, short-video, social-video, and international service domains should stay in focused/global rules unless the user explicitly wants them as Mainland direct fallback exceptions.
- For China IP synchronization, treat single-upstream additions as candidates. Accept them after current route-origin cross-checks such as gaoyifan `china46.txt`, especially when the visible allocation or origin holder looks foreign or small-provider-specific.
- Exact duplicate checks are not enough for IP rules. Also remove CIDR subnets that are fully covered by broader CIDRs in the same policy file, because they add rule cost without changing routing.
- Keep repository invariant checks as executable scripts when the same guardrails are used by humans and CI. A standard-library validator that checks workflow inventory, README inventory, duplicate workflow names, deprecated workflow schedules, rule syntax, `# TOTAL` counts, and project-specific routing guardrails prevents documentation-only instructions from drifting.
- Filter known upstream marker/test domains at source-cleaning time, not only through per-file excludes. SukkaW's marker `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe` can appear in multiple lists and should fail validation if it reaches generated output.
- For broad fallback layers such as `Global.list`, exact overlap with earlier focused rulesets is runtime-safe but obscures intent and inflates rule size. Prefer an automated post-generation subtraction step that removes exact first-match overlaps after all focused rules have been generated, then recalculate `# TOTAL` and report removed entries by their destination ruleset.
