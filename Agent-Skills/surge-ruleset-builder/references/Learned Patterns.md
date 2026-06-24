# Learned Patterns

Store only verified, reusable knowledge that improves future Surge ruleset work.
This file is a compact operational reference, not a task log or changelog.

## Admission Criteria

Add a finding only when all conditions hold:

- It was observed or validated during a real ruleset task.
- It applies to more than one service or is a stable Surge-specific behavior.
- Its evidence can be reproduced from official documentation, authoritative network data, or multiple credible sources.
- It changes how future rules should be researched, constructed, or validated.

Do not add temporary service endpoints, unsupported guesses, task-specific source lists, or conclusions based only on one unverified repository.

## Reusable Findings

### Source and Coverage

- A larger upstream list is not necessarily more complete: shared cloud, CDN, identity, analytics, and consent infrastructure often increases false positives without improving core service coverage.
- Verify network prefixes using both registration and current route origin where practical. Registration alone does not prove that a prefix is currently dedicated to the target service.
- When a service publishes a current canonical network list, compare community additions against it and remove unexplained extras instead of assuming that more prefixes improve coverage.
- Decompose unusually large upstream lists by rule type and network owner. Thousands of generated cloud CIDRs can dominate the rule count while adding shared-infrastructure false positives.
- For cloud-hosted control planes, prefer verified service domains. Reserve IP fallback for prefixes currently originated by the service or otherwise demonstrated to be dedicated.
- Treat single-host IP rules and community-labeled backup endpoints as volatile. Keep them only when current official data, route ownership, source code, or reproducible traffic evidence supports their purpose.

### Domain and Suffix Logic

- A domain ruleset cannot both include a parent suffix and strictly exclude selected child hosts beneath it. Replace the parent match with explicit product hosts for strict separation.
- Treat generated hostname families as keyword candidates only after confirming the stable portion is service-specific and cannot reasonably match unrelated traffic.
- Treat dotted IP fragments stored as `DOMAIN-KEYWORD` as unnormalized network observations. Replace only with ownership-verified CIDRs; otherwise omit.

### Cross-File and First-Match

- For broad fallback layers such as `Global.list`, exact overlap with earlier focused rulesets is runtime-safe but obscures intent and inflates rule size. Prefer an automated post-generation subtraction step.
- For a CDN category, distinguish static asset delivery from arbitrary tenant hosting. A provider suffix such as `cloudfront.net` can carry APIs, login traffic, media playback, and complete websites.
- When adding a dedicated `Download.list`, place it before `Game.list`, then exclude exact download/CDN entries from `Game.list`. Keep Mainland China game download endpoints in `China.list`.

### Validation and Automation

- Keep repository invariant checks as executable scripts when the same guardrails are used by humans and CI. A standard-library validator prevents documentation-only instructions from drifting.
- Validate guardrails as hard checks after applying them. Cleanup filters can miss changed upstream formats; final validation should fail on violations.
- Prefer updating a source or validation method over adding one-off exceptions when the same omission pattern appears in multiple rulesets.

### China-Specific

- For direct China domain rules, company origin is not enough. Chinese-owned overseas media, short-video, and international service domains should stay in focused/global rules unless the user explicitly wants Mainland direct fallback.
- For China IP synchronization, treat single-upstream additions as candidates. Accept after current route-origin cross-checks (e.g., gaoyifan `china46.txt`).
- Audit manually maintained sections of community China lists separately from synchronized upstream data. Personal DIRECT preferences can include foreign vendor domains not supported by geographic ownership evidence.
