# Source Guide

## Official Surge Documentation

- LLM index: https://nssurge.com/llms.txt
- Manual LLM index: https://manual.nssurge.com/llms.txt
- Ruleset manual: https://manual.nssurge.com/rule/ruleset.html
- Domain-based rules: https://manual.nssurge.com/rule/domain-based.html
- IP-based rules: https://manual.nssurge.com/rule/ip-based.html
- Knowledge Base LLM index: https://kb.nssurge.com/llms.txt
- Beta release log: https://nssurge.com/mac/latest/appcast-signed-beta.xml

Start with the unified LLM index and route the task to the appropriate documentation set. When official sources conflict, use this priority: release log, Manual, then Knowledge Base. Do not infer undocumented behavior or assume examples describe the latest release.

## Fixed Community References

- ConnersHua RuleGo: https://github.com/ConnersHua/RuleGo/tree/master/Surge/Ruleset
- SukkaW Surge: https://github.com/SukkaW/Surge
- Rabbit-Spec Surge: https://github.com/Rabbit-Spec/Surge/tree/Master/Rules
- blackmatrix7 ios_rule_script: https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Surge
- QuixoticHeart rule-set: https://github.com/QuixoticHeart/rule-set/tree/master/custom

These repositories are comparison inputs, not unquestioned sources of truth. Inspect source files and update dates. Several aggregate lists include shared AWS or CDN ranges that can route unrelated traffic.

## Streaming-Service Network Sources

- Netflix Open Connect: https://openconnect.netflix.com/en/
- Netflix Open Connect peering: https://openconnect.netflix.com/en/peering/
- Netflix AS2906 routing view: https://bgp.he.net/AS2906
- blackmatrix7 Netflix ruleset: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Netflix/Netflix.list

Use service-operated delivery documentation and current route-origin data to identify dedicated streaming prefixes. Use large generated rulesets such as the blackmatrix7 Netflix list to discover domain and cloud candidates, but inspect their rule-type counts before merging. Provider-published AWS or CloudFront ranges describe shared infrastructure, not exclusive service ownership.

## Messaging-Service Sources

- Telegram published CIDRs: https://core.telegram.org/resources/cidr.txt
- Telegram iOS source: https://github.com/TelegramMessenger/Telegram-iOS
- Telegram Desktop source: https://github.com/telegramdesktop/tdesktop
- Telegram Android source: https://github.com/DrKLO/Telegram

Use official client source code to confirm service-owned domains and platform behavior. For third-party clients, verify client-specific domains against their own source or official site and at least one current ruleset; do not infer ownership from a client process name alone.

## AI and Apple Intelligence Sources

- SukkaW AI rules: https://github.com/SukkaW/Surge/blob/master/Source/non_ip/ai.conf
- SukkaW Apple Intelligence rules: https://github.com/SukkaW/Surge/blob/master/Source/non_ip/apple_intelligence.conf
- Rabbit-Spec AIGC rules: https://github.com/Rabbit-Spec/Surge/blob/Master/Rules/AIGC.list
- QuixoticHeart Apple Intelligence rules: https://github.com/QuixoticHeart/rule-set/blob/master/custom/apple-intelligence.list
- Apple Private Cloud Compute security guide: https://security.apple.com/documentation/private-cloud-compute/
- Apple PCC reference implementation: https://github.com/apple/security-pcc
- OpenAI platform documentation: https://platform.openai.com/docs/
- Anthropic documentation: https://docs.anthropic.com/
- Google Gemini API documentation: https://ai.google.dev/gemini-api/docs
- Microsoft Copilot documentation: https://learn.microsoft.com/copilot/
- AWS Bedrock endpoints: https://docs.aws.amazon.com/general/latest/gr/bedrock.html

Use official product sites to verify that a service is active and owned by the named vendor. Use endpoint documentation, official client code, reproducible traffic evidence, or agreement between independent maintained rulesets before adding non-obvious support domains. For Apple Intelligence, distinguish Private Cloud Compute relay traffic from broader Siri, geolocation, Maps, and iCloud traffic; shared Apple endpoints require an explicit functional justification.

For broad AI category rulesets, inventory at least assistants and search, model APIs, coding agents, image/video/audio generation, research and productivity, voice agents, and local/open tooling. Apply the user's geographic scope to vendor ownership, not merely to the domain's hosting region.

## Product-Family Separation Sources

- Google product and API documentation: https://developers.google.com/products
- Google API discovery directory: https://discovery.googleapis.com/discovery/v1/apis
- YouTube Data API documentation: https://developers.google.com/youtube/v3
- YouTube Music official site: https://music.youtube.com/

When splitting products owned by one provider, inspect both the broad provider ruleset and every sibling product ruleset. A parent suffix such as `google.com`, `googleapis.com`, or `googleusercontent.com` cannot strictly exclude selected child hosts. Replace it with explicit product hosts when strict separation is required, and test known sibling endpoints as negative samples.

## CDN Category Sources

- SukkaW CDN domain set: https://github.com/SukkaW/Surge/blob/master/Source/domainset/cdn.conf
- SukkaW CDN classical rules: https://github.com/SukkaW/Surge/blob/master/Source/non_ip/cdn.conf
- SukkaW CDN IP rules: https://github.com/SukkaW/Surge/blob/master/Source/ip/cdn.conf

SukkaW's CDN category is designed for a broad secondary policy and includes static assets, hosted sites, object storage, service-specific resources, telemetry, certificate services, and other content-like traffic. When building a narrower reusable CDN ruleset, classify candidates by function and exclude arbitrary tenant-hosting parents, shared cloud roots, APIs, OCSP, NTP, telemetry, and geo-sensitive playback unless the requested policy explicitly includes them.

## Mainland China Category Sources

- SukkaW Domestic domains: https://github.com/SukkaW/Surge/blob/master/Source/non_ip/domestic.conf
- SukkaW China CIDR builder: https://github.com/SukkaW/Surge/blob/master/Build/build-chn-cidr.ts
- SukkaW China CIDR supplement: https://github.com/SukkaW/Surge/blob/master/Source/ip/domestic.conf
- blackmatrix7 China domains: https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Surge/China/China_Domain.list
- blackmatrix7 China IPs: https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Surge/ChinaIPs/ChinaIPs.list
- Rabbit-Spec China: https://github.com/Rabbit-Spec/Surge/blob/Master/Rules/China.list
- Rabbit-Spec China CIDR: https://github.com/Rabbit-Spec/Surge/blob/Master/Rules/ChinaCIDR.list
- gaoyifan China operator IP: https://github.com/gaoyifan/china-operator-ip
- Loyalsoldier China CIDR: https://github.com/Loyalsoldier/surge-rules/blob/release/ruleset/cncidr.txt

For direct-routing rules, distinguish current routes announced inside Mainland China from registry or GeoIP country allocations. Compare both classes, but do not blindly union them: an allocation-oriented list can retain unannounced, transferred, anycast, or overseas-operated prefixes. Also inspect repository-specific manual sections separately; they may contain personal DIRECT preferences such as foreign vendors or overseas cloud single-host IPs rather than geographic China evidence.

When a China IP candidate appears in only one synchronized upstream, cross-check it against gaoyifan `china46.txt` or equivalent current route-origin evidence before accepting it. This is especially important for prefixes originated by small CN ASNs, global transit providers, or foreign-looking IPv4/IPv6 allocations. After merging sources, prune CIDR subnets already covered by broader CIDRs in the same policy file; the broader rule is equivalent for routing and keeps the generated set smaller.

## Research Priority

1. Official Surge syntax documentation.
2. Official target-service documentation and owned domains.
3. Current RIR, WHOIS, ASN, and BGP route-origin data for IP ownership.
4. Current source files from the fixed community references.
5. Official product websites used to confirm ownership and current availability.
6. Other reputable community sources used only to identify candidates for verification.

For current network ownership, verify both the registered holder and the announced route origin when possible. A cloud-provider prefix used by a service is not automatically dedicated to that service.

When comparing an upstream list, report total rules by type, shared rules, local-only rules, and upstream-only rules. Explain high-volume differences by ownership class rather than treating a larger count as better coverage.

Do not treat DNS resolution, a valid TLS certificate, a search result, or appearance in one ruleset as sufficient evidence by itself. Record deliberate exclusions when candidates are shared identity, telemetry, analytics, consent, payment, CDN, cloud-hosting, or unrelated corporate domains.
