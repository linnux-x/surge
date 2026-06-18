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
- For geographic direct-routing IP sets, distinguish current route-origin coverage from registry or GeoIP country allocation. Use allocation lists as comparison inventories, but avoid a blind union when the routing policy is intended to represent traffic currently announced inside the region.
- Audit manually maintained sections of community category lists separately from their synchronized upstream data. Personal DIRECT preferences can include foreign vendor domains and overseas cloud single-host IPs that are useful to one author but are not evidence of geographic ownership.
- Treat community automation workflows as reusable plumbing, not reusable policy. A workflow that preserves local baseline files must still run repository-specific cleanup and validation after every merge, or stale local mistakes and upstream personal preferences will survive regeneration.
- Validate guardrails as hard checks after applying them. Cleanup filters can miss changed upstream formats; final validation should fail on domain/IP layer violations such as IP rules in a domain-only ruleset, missing `no-resolve` outside the intended IP-fallback exception, or dotted IP fragments stored as `DOMAIN-KEYWORD`.
