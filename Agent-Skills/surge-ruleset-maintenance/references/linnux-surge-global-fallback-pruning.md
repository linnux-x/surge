# Linnux Surge Global Fallback Pruning

Durable pattern learned while auditing `linnux-x/surge` `Global.list` after focused AI, media, China, CDN, and provider splits.

## When to use

Use this pattern when a broad fallback ruleset such as `Global.list` contains exact duplicates of earlier focused rulesets in the configured `Conf/LINNUX.conf` first-match order.

Runtime behavior may still be correct because earlier rules catch the traffic first, but leaving exact duplicates in the fallback layer:

- inflates rule size;
- obscures ownership and routing intent;
- makes destination reporting harder when entries are removed from broad layers;
- lets upstream broad lists reintroduce focused-service entries after cleanup.

## Preferred implementation

1. Generate all focused rulesets first.
2. Generate `Global.list` from upstream and Manual inputs.
3. After every earlier focused ruleset has been written, run a post-generation subtraction step that removes exact non-comment rule lines from `Global.list` when the same lowercase line exists in any earlier ruleset.
4. Recalculate `# TOTAL` after subtraction.
5. Re-validate `Global.list` and the whole repo.
6. In the final report, group removed entries by the first earlier ruleset that now catches them.

For `linnux-x/surge`, the workflow function is named `prune_global_first_match_overlaps` and runs after all `process_rule` calls. It compares `Global.list` against earlier rulesets including WeChat, Speedtest, AI, Apple, Microsoft, Telegram, Game, YouTube, TikTok, SocialMedia, PayPal, Google, Netflix, Disney, ChinaMedia, GlobalMedia, and CDN.

## Destination reporting

When reporting removals from `Global.list`, do not say only that entries were deleted. Report their destinations by first-match target, for example:

- `Apple.list` for Apple-owned exact overlaps;
- `SocialMedia.list` for Facebook/X/forum/social overlaps;
- `GlobalMedia.list` for streaming-media overlaps;
- `Google.list`, `Microsoft.list`, `PayPal.list`, `YouTube.list`, `Netflix.list`, `Disney.list`, `AI.list`, `Telegram.list`, `TikTok.list`, etc. for their focused services;
- `CDN.list` only for explicitly intended resource hosts such as `release-assets.githubusercontent.com`.

If a removed entry has no focused match, say it falls through to later fallback / `FINAL`. Do not imply it moved to a ruleset that does not actually catch it.

## Apple Akamai exception

During the Global audit, Apple-specific Akamai CNAME hosts appeared only in `Global.list` rather than `Apple.list`:

- `DOMAIN,apple.com.akadns.net`
- `DOMAIN,configuration-lb.ls-apple.com.akadns.net`
- `DOMAIN,courier-push-apple.com.akadns.net`
- `DOMAIN,push-apple.com.akadns.net`
- `DOMAIN,www-cdn.icloud.com.akadns.net`

For this repository, these belong in `Rule/Manual/Apple.txt`, then `Apple.list`, before Global pruning. This converts their destination from broad Global fallback to the Apple policy layer.

## Verification samples

Use representative first-match checks after pruning:

- `github.com` -> `Global.list`
- `githubusercontent.com` -> `Global.list`
- `release-assets.githubusercontent.com` -> `CDN.list`
- `githubcopilot.com`, `anthropic.com` -> `AI.list`
- `youtube.com`, `googlevideo.com` -> `YouTube.list`
- `tiktokcdn.com` -> `TikTok.list`
- `telegram.org` -> `Telegram.list`
- `paypal.com` -> `PayPal.list`
- `netflix.com` -> `Netflix.list`
- `disneyplus.com` -> `Disney.list`
- `facebook.com`, `x.com` -> `SocialMedia.list`
- `google.com` -> `Google.list`
- `microsoft.com` -> `Microsoft.list`
- `apple.com`, `apple.com.akadns.net`, `www-cdn.icloud.com.akadns.net` -> `Apple.list`
- unknown generic hosts such as `example.org` -> `FINAL,Global`

## Pitfalls

- Do not subtract suffix-shadowed entries unless you explicitly intend to remove them. This pattern is for exact rule-line overlap; suffix-shadowing can be policy-dependent and needs separate review.
- Do not preserve generated `Rule/*.list` as a baseline just to keep removed Global entries. Durable intent belongs in Manual include/exclude files or workflow post-processing.
- If the generator refreshes every rule timestamp, restore unrelated generated files before committing a focused Global change, unless the broader regeneration is intentional.
