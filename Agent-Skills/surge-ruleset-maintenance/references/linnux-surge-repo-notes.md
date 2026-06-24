# Linnux Surge Repository Notes

These notes capture durable, repo-specific facts from an audit of `linnux-x/surge`. Keep operational details concise; re-check the repository before acting because workflows and file inventories can change.

## Repository Shape

- Local checkout used in the session: `/root/surge`.
- Rule files live under `Rule/*.list`.
- Manual durable overrides live under `Rule/Manual/*.txt` and `Rule/Manual/*.exclude.txt`.
- Main Surge profile is `Conf/LINNUX.conf`.
- The repository contains an in-repo Codex skill at `.codex/skills/surge-ruleset-builder/SKILL.md`, plus references under `.codex/skills/surge-ruleset-builder/references/`.

## Important Project Guardrails

- GitHub family rules should not be in `Microsoft.list`.
- Broad GitHub content suffixes should route through `Global.list`; Copilot through `AI.list`; only explicit download asset hosts such as `release-assets.githubusercontent.com` should be treated as CDN exceptions.
- `fast.com` belongs only in `Speedtest.list`.
- `China.list` should be domain-only.
- `China_IP.list` intentionally omits `no-resolve` so unresolved domains can be classified by Mainland IP after local DNS resolution.
- Other IP rules normally need `no-resolve`.
- Avoid broad shared CDN parents in service/media/provider/China lists unless the routing policy explicitly intends broad CDN treatment.

## Audit Findings from the Session

- `README.md` originally listed stale files and omitted current files. It was updated locally so its rule table matched the 22 current `Rule/*.list` files.
- Main workflow `.github/workflows/auto-rules.yml` generated the same 22 current rule files as the repository contained at audit time.
- Deprecated workflow `.github/workflows/auto-surge-rules.yml` still had a schedule and the same workflow `name: Auto-Surge-Rules`. It targeted stale files such as `BiliBili.list`, `ChinaASN.list`, `ChinaCIDR.list`, `Facebook.list`, `Instagram.list`, `Meta.list`, `Proxy.list`, `Spotify.list`, and `TelegramASN.list`, while missing current files such as `Apple_CN.list`, `CDN.list`, `China_IP.list`, `Global.list`, `Microsoft_CDN.list`, `PayPal.list`, `SocialMedia.list`, `Speedtest.list`, and `WeChat.list`.
- The duplicate workflow name can make `gh workflow run Auto-Surge-Rules` ambiguous. Prefer file-specific invocation like `gh workflow run auto-rules.yml`, or rename/disable/remove the deprecated workflow.
- A naive search for `github` in `Microsoft.list` can false-positive on file header comments such as `# REPO: https://github.com/...`. Guardrail checks should ignore comments and blank lines.
- Actual upstream file URLs in `auto-rules.yml` were reachable during the audit; base variable URLs were not all fetchable and should not be counted as source failures.

## Suggested Reusable Checks

For future work, implement or run a script that verifies:

1. README rule table equals `Rule/*.list` inventory.
2. Main workflow `process_rule` inventory equals `Rule/*.list` inventory.
3. No scheduled deprecated workflow regenerates stale files.
4. Workflow `name:` values are unique or invocation docs use file names.
5. Non-comment rules obey project guardrails.
6. Expanded source file URLs are reachable.
7. `# TOTAL` headers equal actual non-comment rule count.
8. Representative domains are evaluated through the profile's actual `RULE-SET` order, not by standalone file membership.
9. Each ruleset report includes rule type counts, Manual add/exclude inputs, intended traffic class, first-match role, guardrail status, and cleanup opportunities.

## First-Match Audit Pattern

When the user asks whether each rule follows the agreed logic, read `Conf/LINNUX.conf` first and build the effective rule order from `[Rule]`. Evaluate overlaps through this order:

- Earlier focused rules intentionally override later broad rules. Examples from this repo: `AI` before `Microsoft`/`Google`, `YouTube` before `Google`, `Speedtest` before `Netflix`/`Global`, `WeChat` before `China`, `CDN` before `Global`, and `China` before `China_IP`.
- A later broad fallback containing the same domain is not necessarily a routing bug if an earlier focused ruleset catches it first. Report it as hygiene/size/semantic debt instead.
- Peer overlaps with different policies still deserve cleanup when they obscure intent, especially `CDN` vs service-specific rules, `Global`/`GlobalMedia` vs focused services, and `China` vs overseas/global services.
- Always include representative first-match samples for repository guardrails: `fast.com`, `github.com`, `githubusercontent.com`, `release-assets.githubusercontent.com`, `githubcopilot.com`, `copilot.microsoft.com`, `youtube.com`, `googlevideo.com`, `rmonitor.qq.com`, `tiktok.com`, `netflix.com`, `cdn-apple.com`, and `telegram.org`.

## Current Optimization Themes Observed

These are durable cleanup themes for `linnux-x/surge`; re-check current files before editing:

- The active `Conf/LINNUX.conf` order matched the intended high-level policy during audit: focused service rules first, then CDN, Global, China domain fallback, LAN, China IP fallback, and FINAL.
- Syntax/guardrail validation passed for all 22 `.list` files: no unsupported types, no policy names in external rulesets, no exact duplicate rules, valid CIDRs, `China.list` domain-only, `China_IP.list` without `no-resolve`, other IP rules with `no-resolve`, no `DOMAIN-WILDCARD`, and no dotted IP fragments encoded as `DOMAIN-KEYWORD`.
- The highest risk remained workflow drift: deprecated `.github/workflows/auto-surge-rules.yml` was scheduled, shared `name: Auto-Surge-Rules`, and could regenerate stale files. The remediation pattern is to rename/disable the legacy workflow, remove its `schedule`, and delete any stale rule files it already regenerated after rebasing from origin.
- `auto-rules.yml` should not append the existing generated `Rule/*.list` files as a “Current Project Baseline”. Baseline preservation caused upstream withdrawals and local historical mistakes to persist indefinitely. Durable local additions/removals belong in `Rule/Manual/*.txt` and `Rule/Manual/*.exclude.txt` only.
- SukkaW marker/test domain `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe` must be filtered globally during source cleaning and validated as absent from generated output.
- `CDN.list` contained broad CDN parents such as `cloudfront.net`, `azureedge.net`, `akamaihd.net`, `akamaized.net`, `b-cdn.net`, and `fastly.net`. Keep them only if the user's policy intentionally routes all tenant CDN content through the CDN policy; otherwise narrow to verified asset/download hosts.
- `China.list` was syntactically clean but semantically broad. Continue excluding international media/live-stream Akamai hosts, games/Blizzard/Steam, Microsoft CDN, TikTok/overseas ByteDance, and shared CDN/cloud entries that should not be Mainland direct fallback.
- `Global.list` and `GlobalMedia.list` had large overlaps with focused service rules. This is usually safe at runtime because focused rules are earlier, but it increases size and obscures intent. Prioritize cleanup for YouTube, Netflix, Disney, Google, Microsoft, Telegram, TikTok, SocialMedia, PayPal, and Speedtest where dedicated policies exist. In `linnux-x/surge`, `auto-rules.yml` uses a post-generation `prune_global_first_match_overlaps` step after all focused rules have been generated so exact overlaps are removed from `Global.list`, `# TOTAL` is recalculated, and destinations can be reported by first-match ruleset.
- `Game.list` before `CDN.list` means game download CDN hosts follow the Game policy, not the CDN policy. Keep verified overseas game service hosts there, but put generic download/CDN endpoints in `Download.list` when the active config has a Download layer before Game. Remove Microsoft account/store/CDN helper hosts that are already caught by earlier `Microsoft.list` or `Microsoft_CDN.list`. Xbox-specific short/service domains such as `xbx.lv` should be excluded from broad `Microsoft.list` when they are meant to hit `Game.list` by first-match order. Mainland China game download/cache endpoints that work directly in China, such as Steam China/CDN, Perfect World Steam, NetEase/Blizzard China CDN, and Xbox China service hosts, belong in `China.list` via Manual include/exclude pairs rather than in `Game.list`.
- `gvt1.com`/`gvt2.com` are broad Google download/update host families, not YouTube-only. Keep them out of `YouTube.list` via `Rule/Manual/YouTube.exclude.txt` and include them in `Google.list` via `Rule/Manual/Google.txt`; exact Download rules such as `edgedl.me.gvt1.com` still win earlier through `Download.list`. Keep YouTube-specific delivery on `googlevideo.com`, `ytimg.com`, `youtube*.googleapis.com`, and YouTube domains.
- `GEOIP,GOOGLE` was added to `Rule/Manual/Google.txt` (2026-06-24). It matches all Google ASN IP ranges as a fallback for Google IPs not covered by domain rules. `validate_surge_repo.py`'s `ALLOWED_TYPES` and the workflow's inline `validate_rules()` awk regex both include `GEOIP`.
- Microsoft Copilot/Bing Chat split: keep `copilot.microsoft.com`, `copilot.cloud.microsoft`, and `sydney.bing.com` in `AI.list` via `Rule/Manual/AI.txt` so they first-match AI before broad `Microsoft.list` suffixes such as `microsoft.com` and `bing.com`. Do not move ordinary Bing (`bing.com`, `cn.bing.com`) out of Microsoft without a specific reason.
- Dedicated Download split: `Download.list` should be generated from SukkaW `Source/domainset/download.conf` plus `Source/domainset/game-download.conf`, with a `Download` policy before `Game` in `Conf/LINNUX.conf`. Add download CDN hosts to `Rule/Manual/Game.exclude.txt` when they are covered by `Download.list`, so `Game.list` keeps game service identity rather than transport/download endpoints.
- SukkaW direct/domestic/download borrowing pattern: `non_ip/domestic.conf` is already a `China.list` upstream in this repo; exact-missing checks should be zero before adding Manual duplicates. `non_ip/download.conf` currently contributes only compatible `URL-REGEX` rules because its `DOMAIN-WILDCARD` entries are intentionally not emitted here. `non_ip/direct.conf` is not a ruleset to import wholesale; only downloader process names have been borrowed into `Rule/Manual/Download.txt`, while proxy processes, PT trackers, academic sites, and remote-control processes stay out unless the user asks for a dedicated direct/academic class.
- Telegram split: keep Telegram domains, official CIDRs, ASNs, and Telegram client process names in `Telegram.list`, and exclude Telegram leftovers from broader social/forum sources. `Rule/Manual/Telegram.exclude.txt` should prune stale/broad upstream Telegram IP ranges when official narrower CIDRs are present, and can drop redundant OR rules when the same ASNs already exist as standalone `IP-ASN` rules. `Rule/Manual/SocialMedia.exclude.txt` should remove Telegram domains/IPs so `SocialMedia.list` has no exact Telegram overlap.
- SocialMedia hygiene: `Telegram.list` precedes `SocialMedia.list`, so Telegram domains in SocialMedia are semantic duplicates and should be excluded via `Rule/Manual/SocialMedia.exclude.txt`; AI chat/social products such as `grok.com` and `poe.com` should likewise be excluded from SocialMedia and owned by `AI.list`. Domestic social/forum-style sites should not be automatically forced into proxy SocialMedia: verify first-match and route China-local services (e.g. `linkedin.cn`, many domestic tech/digital forums) to `China.list` or a future dedicated forum/tech class instead of overloading SocialMedia. Existing forum-like SocialMedia coverage includes `nodeseek.com`, `linux.do`, and `v2ex.com`; candidate forums discovered for future review include `hostloc.com`, `lowendtalk.com`, `chiphell.com`, `coolapk.com`, `52pojie.cn`, `sspai.com`, `smzdm.com`, `ithome.com`, `right.com.cn`, `pcbeta.com`, `nga.cn`, and `ngabbs.com`.

## Focused Split Patterns Confirmed

- AI vs Google: Google AI/Gemini/AI Studio/NotebookLM/Jules/Antigravity entries should be durable in `Rule/Manual/AI.txt` and excluded from `Rule/Manual/Google.exclude.txt`. Keep generic `google.com` / `googleapis.com` in `Google.list`; specific AI API hosts first-match `AI.list` because AI precedes Google in `Conf/LINNUX.conf`.
- Anthropic/Claude: Keep `anthropic.com`, `claude.ai`, `claude.com`, `clau.de`, `claudeusercontent.com`, MCP content/client domains, and Anthropic auth/CDN helper hosts in `AI.list` via Manual so upstream withdrawals do not break Claude routing.
- Apple split: `Conf/LINNUX.conf` evaluates `Apple_CN.list` with `DIRECT` before `Apple.list` with the Apple policy group. China/.cn Apple properties and China Apple CDN edges should live in `Rule/Manual/Apple_CN.txt` and be excluded from `Rule/Manual/Apple.exclude.txt`.
- For Apple, exact overlap alone missed the issue: `Apple.list` broad suffixes such as `apple.com`, `apple.cn`, `mzstatic.com`, `cdn-apple.com`, `apple-mapkit.com`, and `aaplimg.com` shadowed many `Apple_CN.list` entries. Use a suffix-shadowing check plus representative first-match samples.
- Representative Apple checks: `apple.com.cn`, `www.apple.com.cn`, `icloud.com.cn`, and `apple.cn` should hit `Apple_CN.list`; `apple.com` should hit `Apple.list`; `apple-relay.apple.com` should continue to hit `AI.list` because of Apple Intelligence.

## Reporting Pattern for This Repo

When reporting an audit or edit, include:

- changed files;
- whether edits are local only or pushed;
- validation summary;
- workflow/manual-rule implications;
- any actions that require GitHub Actions manual run or gateway/new-session reload.
