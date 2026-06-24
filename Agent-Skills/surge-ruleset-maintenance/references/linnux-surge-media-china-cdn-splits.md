# Linnux Surge Media / China / CDN Split Patterns

Durable patterns learned while optimizing `linnux-x/surge` media, China fallback, and CDN rules. Re-check current files before applying; these notes describe the intended maintenance approach, not a frozen inventory.

## Always report destinations

When removing or moving any rule entry, final reports must say where the traffic now goes:

- explicit target ruleset after adding a Manual include;
- earlier first-match ruleset that already catches it;
- later fallback / `FINAL` if no focused ruleset catches it;
- Manual exclude file used to prevent upstream reintroduction.

This is required even when an entry is simply deleted from a broad fallback such as `China.list`.

## China / China_IP

- `China.list` should stay domain-only; no `IP-CIDR`, `IP-CIDR6`, or `IP-ASN` rules.
- `China_IP.list` should stay IP-only and intentionally omit `no-resolve` so unresolved domains can be classified after DNS resolution.
- When pruning `China.list`, distinguish:
  - entries already caught by earlier focused rules (`ChinaMedia`, `Game`, `TikTok`, `GlobalMedia`, etc.);
  - entries with no focused match, which should fall through to later fallback / `FINAL` rather than DIRECT.
- Good candidates to exclude from `China.list`: overseas live-stream Akamai/EdgeSuite/CloudFront hosts, TikTok/overseas ByteDance hosts, and shared CDN/cloud entries that should not be Mainland direct fallback.

Representative destination checks used:

- `qq.com` -> `China.list`
- `bilibili.com` -> `ChinaMedia.list`
- `p-bstarstatic.akamaized.net` -> `ChinaMedia.list` or `GlobalMedia.list` depending on the B-Star split
- `steamcommunity-a.akamaihd.net` -> `Game.list`
- `tiktoknewaccount.com` -> `TikTok.list` if covered; otherwise fall through after being excluded from `China.list`
- `rthklive1-lh.akamaihd.net` -> `GlobalMedia.list` if covered; otherwise fall through

## CDN

Avoid keeping broad shared CDN parent suffixes in `CDN.list` unless the user explicitly wants all tenants on that CDN to follow the CDN policy. Prefer narrow, verified hosts.

Broad parents that were excluded from `CDN.list`:

- `akadns.net`
- `akamaiedge.net`
- `akamaihd.net`
- `akamaized.net`
- `azureedge.net`
- `b-cdn.net`
- `cdn77.org`
- `cloudfront.net`
- `edgekey.net`
- `edgesuite.net`
- `fastly.net`

Keep explicit CDN exceptions only when justified. For this repo, `release-assets.githubusercontent.com` is intentionally in `CDN.list`; broader GitHub hosts should stay in focused/global rules.

Representative destination checks:

- `release-assets.githubusercontent.com` -> `CDN.list`
- OpenAI/Anthropic CDN helpers -> `AI.list`
- Microsoft CDN Akamai hosts -> `Microsoft_CDN.list`
- Apple China CDN edges -> `Apple_CN.list`
- Netflix / Hulu / social CDN hosts -> their media/social rules or fallback, not broad CDN parent rules

## ChinaMedia / GlobalMedia

`ChinaMedia.list` is for Mainland/China media DIRECT-like behavior. `GlobalMedia.list` is for overseas/global media services. Use Manual include/exclude pairs so future upstream syncs do not undo the split.

Patterns confirmed:

- Bilibili China domains such as `bilibili.com` remain in `ChinaMedia.list`.
- Bilibili international / B-Star entries belong in `GlobalMedia.list`, not `ChinaMedia.list`, for example:
  - `bilibili.tv`
  - `biliintl.com`
  - `p-bstarstatic.akamaized.net`
  - `p.bstarstatic.com`
  - `upos-bstar-mirrorakam.akamaized.net`
  - `upos-bstar1-mirrorakam.akamaized.net`
  - `upos-hz-mirrorakam.akamaized.net`
  - `PROCESS-NAME,com.bilibili.comic.intl`
- YouTube/Google video entries should be excluded from `GlobalMedia.list` and caught by `YouTube.list`:
  - `youtube*`
  - `googlevideo.com`
  - `ggpht.com` / `ggpht.cn`
  - `gvt1.com` / `gvt2.com`
  - `video.google.com`
  - `youtu.be`
- TikTok entries should be excluded from `GlobalMedia.list` and caught by `TikTok.list` where covered.
- AI/Coding assistant entries should be excluded from `GlobalMedia.list` and caught by `AI.list`:
  - GitHub Copilot (`api.githubcopilot.com`, `githubcopilot.com`)
  - Groq (`groq.com`)
  - NotebookLM / Google AI
  - Anthropic / Claude keyword leakage

Representative checks:

- `api.githubcopilot.com` -> `AI.list`
- `api.groq.com` -> `AI.list`
- `notebooklm.google.com` -> `AI.list`
- `youtube.com`, `googlevideo.com`, `video.google.com`, `youtu.be` -> `YouTube.list`
- `tiktokcdn.com` -> `TikTok.list`
- `bilibili.tv`, `biliintl.com`, B-Star CDN -> `GlobalMedia.list`
- `bilibili.com` -> `ChinaMedia.list`
- `hulu.com` -> `GlobalMedia.list`
- `netflix.com` -> `Netflix.list`
- `disneyplus.com` -> `Disney.list`

## Focused update workflow

1. Update Manual include/exclude files first.
2. Run the active generator/workflow.
3. Restore unrelated generated `.list` files.
4. Verify every modified `Rule/*.list` has refreshed `# UPDATED` and correct `# TOTAL`.
5. Run `python3 scripts/validate_surge_repo.py` plus YAML/syntax checks.
6. Produce a destination report for every moved/removed group before finalizing.
