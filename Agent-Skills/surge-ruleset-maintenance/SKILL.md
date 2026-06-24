---
name: surge-ruleset-maintenance
description: Use when auditing, generating, synchronizing, or validating Surge external RULE-SET `.list` files and their GitHub Actions workflows, especially repositories that merge upstream rule sources with local Manual include/exclude files. Covers Surge syntax, first-match ordering, workflow inventory checks, README/Rule consistency, and repository guardrails.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [surge, ruleset, proxy-rules, github-actions, validation, networking]
    related_skills: [github-repo-management, github-pr-workflow, systematic-debugging]
---

# Surge Ruleset Maintenance

## Overview

Use this skill for Surge rule repositories that maintain external `.list` rulesets, synchronize upstream rule sources, and publish rules through GitHub Actions.

The objective is precise, auditable routing behavior: avoid stale upstream rules, cross-file policy overlap, invalid Surge syntax, and workflow drift.

## Required Workflow

1. **Sync and inspect repository state.** Pull the latest branch and confirm the working tree state before editing.
2. **Read project instructions first.** Check `AGENT.md`, `AGENTS.md`, in-repo skills, README, and workflow files before changing rules.
3. **Classify the task.** Determine whether the user is asking for:
   - README/documentation update;
   - rule file edit;
   - Manual include/exclude adjustment;
   - workflow source change;
   - full ruleset audit;
   - token/context optimization of the rule-maintenance skill itself.
4. **Prefer durable Manual inputs.** For upstream synchronization repos, use `Rule/Manual/<Name>.txt` and `Rule/Manual/<Name>.exclude.txt` for local additions/removals when the workflow is designed to regenerate `.list` files. Do not use current generated `Rule/*.list` files as an implicit baseline; that preserves stale upstream withdrawals indefinitely.
5. **Filter known upstream marker/test domains.** For SukkaW sources, globally remove `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe` during source cleaning and validate it never reaches generated output.
6. **Validate generated `.list` files.** Check supported rule types, policy-name leakage, duplicates, domain formatting, CIDR validity, and `no-resolve` policy.
7. **Check workflow inventory.** Compare workflow `process_rule` targets with actual `Rule/*.list` and README references. Old workflows can reintroduce deleted files. For `linnux-x/surge`, run `python3 scripts/validate_surge_repo.py` when available; it checks rule inventory, README inventory, workflow-name collisions, stale scheduled rule workflows, `# TOTAL` counts, marker-domain leakage, syntax, CIDR redundancy, and project guardrails.
8. **Check upstream URLs.** Test the actual source URLs used by the workflow, not only base variables.
9. **Verify new upstream sources before merging.** When adding a new upstream to the workflow: (a) fetch the raw file and confirm it's valid Surge syntax, (b) check for trailing policy names (e.g. `,extended-matching` is OK, `,Proxy` is not), (c) check excluded entries against existing `Rule/Manual/*.exclude.txt` patterns — know which entries the exclude will filter out and which it won't, (d) identify what UNIQUE rules the new source brings vs. existing sources (avoid empty redundancy), (e) if the source has subdomain variations of shared infrastructure (e.g., `o33249.ingest.sentry.io`, `aida.googleapis.com`), decide whether they are service-prefixed (keep) or opaque/external (add to exclude), (f) run a test workflow and verify the generated file's rule count, source attribution, and diff report look correct, (g) update README rule table, acknowledgements, and sources.md references in the same commit.
10. **For focused ruleset refreshes, keep the commit narrow but refresh every modified rule.** Run the active workflow/generator so outputs and `# UPDATED` timestamps are produced by automation, then restore unrelated generated `.list` files before review/commit. For every `Rule/*.list` file that remains modified in the commit, verify its `# UPDATED` changed, `# TOTAL` is correct, rule content changed only if intended, and cross-file exclusions still hold.
10. **Report before commit.** Summarize saved paths, changed rules, validation results, and intentional exclusions. When domains/IPs are moved out of a ruleset, moved into another ruleset, or deleted, explicitly report their destination: target ruleset, earlier first-match ruleset that still catches them, or no focused match so they fall through to later fallback/FINAL. Commit/push only when requested.
11. **For full repository audits, report by configured first-match order.** For each ruleset include: intended routing layer, policy from `Conf/*.conf`, rule count/type mix, manual add/exclude inputs, what traffic it contains, whether repository guardrails are satisfied, first-match implications with earlier/later overlaps, and concrete cleanup opportunities.

## Surge Syntax Checks

External rulesets should contain rule declarations without policy names. Common valid types:

- `DOMAIN`
- `DOMAIN-SUFFIX`
- `DOMAIN-KEYWORD`
- `IP-CIDR`
- `IP-CIDR6`
- `IP-ASN`
- `USER-AGENT`
- `PROCESS-NAME`
- `URL-REGEX`
- `GEOIP`
- documented logical wrappers such as `AND`, `OR`, `NOT`

Use current Surge docs when support for less common types is uncertain.

## Validation Checklist

- [ ] Every non-comment line starts with an allowed Surge rule type.
- [ ] External `.list` rules contain no policy name.
- [ ] No exact duplicate non-comment rules.
- [ ] Domain values are lowercase and contain no URL schemes, paths, or inline comments.
- [ ] CIDRs parse successfully.
- [ ] IP rules include `no-resolve` unless the project explicitly documents an exception.
- [ ] No dotted IP fragments are encoded as `DOMAIN-KEYWORD`.
- [ ] README rule table matches actual `Rule/*.list` files.
- [ ] Main workflow target list matches actual generated files.
- [ ] Deprecated workflows are removed when obsolete; if retained for rare reference, they are disabled, uniquely named, and clearly documented.
- [ ] Upstream source URLs used by generation are reachable.
- [ ] No shared third-party infrastructure (OneTrust, Adobe DTM, Braze, New Relic, Optimizely, etc.) in service-specific rulesets — bare shared suffixes are forbidden; service-prefixed subdomains are allowed.
- [ ] No domestic country-code domains (e.g., PayPal `.cn`) in service proxy rules — they belong in the regional direct ruleset (e.g., `China.txt`).
- [ ] `validate_surge_repo.py` passes after any rule or Manual file change. The script checks shared third-party infrastructure, domestic domain misplacement, and all other guardrails automatically.

## Manifest Index and Diff Pipeline

For large Surge rule repos (100K+ rules), maintain a sidecar index system so every rule has a stable identity across workflow runs:

1. **Compact manifests** (`scripts/manifest.py`): generate tab-separated `Rule/.manifests/<Name>.manifest` with `stable_hash_id<TAB>source_name` per rule. Stable ID is SHA-256[:12] of the lowercase rule text — deterministic across runs.
2. **Diff reports** (`scripts/diff_manifests.py`): compare current manifests against git HEAD, produce `scripts/diff_report.md` (committed) and `scripts/diff_report.json` (committed). Show added/removed/source-changed counts per file with samples.
3. **Manifests ARE committed to git.** The compact tab-separated format is only ~6.6 MB total (vs 38 MB JSON) — manageable for git. When committed, `diff_manifests.py` can load the previous version from `git show HEAD:` and produce true incremental diffs. For China.list (112K rules) the compact manifest is ~5 MB. Generate *after* rule generation in the workflow, commit alongside .list files.
4. **Workflow integration**: add `Generate Rule Manifests` and `Generate Diff Report` steps after rule generation, before validation and audit. The diff report is committed alongside rule updates.
5. **Source attribution**: parse `# ======= SourceName ========` section headers in .list files to tag each rule with its upstream source. This enables source-level diff analysis (e.g., "3 rules added from blackmatrix7, 1 removed from SukkaW").

## Incremental Upstream Change Detection

For repos with many upstream sources (30+), avoid full regeneration on every scheduled run. Instead, detect which sources actually changed and only regenerate affected rulesets:

### Architecture

1. **`scripts/check_upstream_updates.py`** — standalone Python script (stdlib only, GA-compatible) that:
   - Maintains a `scripts/source_state.json` committed to git
   - For each upstream URL, sends HTTP HEAD → reads `Last-Modified` / `ETag` / `Content-Length`
   - Falls back to GET with `Range: bytes=0-0`, then full GET as last resort
   - Compares current values against cached state; detects changes
   - Outputs JSON summary with `changed`, `changed_count`, `rulesets[]`
   - Exits 0 (no changes) or 1 (changes detected)

2. **`scripts/source_state.json`** — committed state file tracking each source's last-known timestamp

3. **Workflow integration** — a dedicated `Check Upstream Updates` step runs before generation, sets `changed_rulesets` and `changed_count` outputs. Subsequent steps become conditional on `changed_count > 0`.

### Source-to-Ruleset Mapping

Each upstream URL maps to one or more ruleset filenames. Maintain this mapping in `check_upstream_updates.py` as a `SOURCE_RULESET_MAP` dict — it must mirror the `process_rule` calls in the workflow exactly, or regeneration will miss changes.

### Dependency Tracking

Some rulesets depend on others. Key dependency: `Global.list` needs re-pruning after any overlap-dependent ruleset changes. The check script maintains an `OVERLAP_DEPENDENTS` set — when a match is found, `Global.list` is automatically added to the changed list.

### Workflow Pattern

```yaml
- name: Check Upstream Updates
  id: check_upstream
  run: |
    output=$(python3 scripts/check_upstream_updates.py 2>&1) || true
    summary=$(echo "$output" | grep '^{' | tail -1)
    echo "changed_rulesets=..." >> "$GITHUB_OUTPUT"
    echo "changed_count=..." >> "$GITHUB_OUTPUT"

- name: Generate Rules
  if: ${{ fromJson(steps.check_upstream.outputs.changed_count) > 0 }}
  run: |
    # Parse changed list, wrap each process_rule in should_process()

- name: Generate Manifests / Diff / Validate / Audit / Commit
  if: ${{ fromJson(steps.check_upstream.outputs.changed_count) > 0 }}
  run: ...
```

### Conditional `should_process()` in Bash

```bash
IFS=' ' read -ra CHANGED < <(echo '${{ steps.check_upstream.outputs.changed_rulesets }}' | \
  python3 -c "import json,sys; [print(r) for r in json.load(sys.stdin)]")

should_process() {
  local target="$1"
  for c in "${CHANGED[@]}"; do
    [ "$c" = "$target" ] && return 0
  done
  return 1
}

if should_process "YouTube.list"; then
  process_rule "YouTube.list" "YouTube" "blackmatrix7 YouTube|$BM7/YouTube/YouTube.list"
fi
```

### Pitfalls

- **ruleset.skk.moe returns 403 on HEAD/Range requests.** `check_upstream_updates.py` marks these as `source_available: false` → they are treated as unchanged (conservative). Their sources will always show "unchanged" and require a manual `workflow_dispatch` to force-regenerate.
- **First run always reports everything as CHANGED.** This is correct — there's no cached state yet. The state file is committed after the first run, so subsequent runs detect real deltas.
- **GitHub raw URLs return Last-Modified = the file's last commit date.** This is good enough for daily change detection. ETag is more granular but less consistent across CDN nodes.
- **Keep SOURCE_RULESET_MAP in sync with the workflow.** Every time a `process_rule` call is added, removed, or its source URLs change, the check script's mapping must be updated too. Out-of-sync mapping = missed changes or false positives.
- **`git add` must include `scripts/source_state.json` and `scripts/check_upstream_updates.py`** in the commit step, or the state file won't persist across runs, defeating change detection.

## Online Audit Pipeline

After each workflow run, before committing to GitHub, run `scripts/audit_rules.py` for 5 checks:

1. **Upstream reachability** — all configured source URLs must be accessible (ERROR if unreachable → blocks commit).
2. **Upstream vs generated comparison** — flag abnormal rule-count ratios. **Skip multi-source rulesets** — they naturally exceed any single upstream's count.
3. **Shared infrastructure scan** — broader than `validate_surge_repo.py`. Covers analytics/telemetry/consent/ad-tech/cloud/CDN parent suffixes. **Service-OWNED infrastructure** (Google's doubleclick.net/googleapis.com, Microsoft's azure.com, Meta's facebook.net/fbcdn.net) must be exempted from flagging — they legitimately belong in their service rulesets.
4. **Surge documentation check** — detect new rule types from the LLM index.
5. **Exclude coverage** — verify exclude patterns are effective.

Audit severity levels:
- 🔴 **ERROR** — blocks commit
- 🟡 **WARN** — requires review
- 🔵 **INFO** — for awareness

**Continuous evolution**: WARN findings confirmed as needing exclusion → add to `Rule/Manual/*.exclude.txt` → update both `scripts/audit_rules.py` (`BROAD_SHARED_SUFFIXES`) and `scripts/validate_surge_repo.py` (`SHARED_THIRD_PARTY_SUFFIXES`) → update skill references.

## Common Pitfalls

1. **Old workflow drift.** A deprecated workflow can still be scheduled and regenerate removed files. Check every `.github/workflows/*.yml`, not just the newest one.
2. **Workflow name collisions.** Two workflow files with the same `name:` make manual `gh workflow run <name>` ambiguous. Use file names or rename workflows.
3. **Checking base URLs instead of source URLs.** Variables like `BM7=https://.../rule/Surge` are not fetchable files; validate the expanded file URLs passed to generation.
4. **First-match confusion.** Cross-file overlap is a routing decision. Evaluate representative hosts against the configured `RULE-SET` order, not against standalone files only.
5. **Editing generated `.list` files when Manual files are the durable source.** Direct edits may be overwritten by the next scheduled sync.
6. **Rebase after workflow changes can resurrect stale generated files.** If `origin/main` advanced because an old or scheduled workflow committed generated rules while you were editing, rebase first, then rerun the active generator locally, delete any rule files no longer in the active workflow inventory, run `python3 scripts/validate_surge_repo.py`, and only then continue/amend the commit. Do not resolve generated-rule conflicts by hand.
7. **Accidentally committing bytecode.** Running Python validators can create `__pycache__/` under new script directories. Remove it before committing (`rm -rf scripts/__pycache__`) or ensure it is ignored. Before or alongside the first script commit, create `.gitignore` with at minimum: `__pycache__/`, `*.py[cod]`, `.DS_Store`, `*~`, `*.swp`, `*.orig`.
8. **Blank/comment lines in Manual exclude files can over-filter.** If a workflow uses `grep -vFf "$exclude_file"`, an empty line in `Rule/Manual/*.exclude.txt` matches every line and can wipe a generated ruleset. Sanitize exclude patterns first with: `grep -vFf <(sed 's/\\r$//' "$exclude_file" | awk 'NF && $0 !~ /^[[:space:]]*#/')`.
9. **grep -vFf fixed-string matching misses subdomain variants.** An exclude pattern `DOMAIN-SUFFIX,sentry.io` does NOT match `DOMAIN-SUFFIX,o207216.ingest.sentry.io` because the full line differs. Workaround: add broader substring patterns like `.ingest.sentry.io` (without the rule-type prefix) to the exclude file. Be cautious not to over-exclude.
10. **Full regeneration touches every rule header timestamp.**
11. **Focused rules must be durable on both sides of the split.** When moving a service subset out of a broad provider ruleset, add the subset to `Rule/Manual/<Focused>.txt` AND matching patterns to `Rule/Manual/<Broad>.exclude.txt`. Regenerate and verify first-match samples.
12. **Extend the validate script alongside exclude files.** When adding semantic exclude patterns, also add corresponding invariant checks to `scripts/validate_surge_repo.py` so regressions are caught automatically. Workflow: (1) add exclude entries, (2) add validate checks, (3) run validate to confirm violations, (4) run workflow, (5) run validate again to confirm clean.
13. **Keep AGENT.md as the single source of truth for project instructions.** Other agent docs should reference AGENT.md rather than duplicate it. Duplicates drift apart — when AGENT.md is updated, stale duplicates become contradictory.
14. **Merge co-scheduled small workflows into the main workflow.** When multiple workflows run at the same schedule, merge them. Add the secondary task as a step before Commit, and update `git add` to include its files.
15. **Update the `git add` command in the commit step when adding new steps.** New generation steps that create files must be reflected in the Commit step's `git add` line. Otherwise the new files won't be committed.
16. **`git push` rejection from auto-committed workflow runs.** When a scheduled workflow committed while you were editing locally, use `git pull origin main --rebase` then push again. Do NOT force push — that drops the workflow commit.
17. **Separate download transport from service identity.** Place `Download.list` before service rules if download CDN traffic should use the Download policy. Exclude exact download/CDN hosts from service rulesets so they stay focused.
18. **Check both exact overlap and shadowing.** A broad suffix can shadow more-specific hosts depending on `[Rule]` order. For split rulesets, compute exact intersection plus suffix/keyword shadowing against the configured first-match order.
19. **Keep README synchronized with the full pipeline.** When adding a workflow step, script, or directory that affects the pipeline, immediately update the README's directory table, pipeline diagram, and relevant subsections in the same session.
20. **Extract inline Python heredocs from workflows into standalone scripts.** Extract `<<'PY' ... PY` blocks to `scripts/<name>.py` with `if __name__ == "__main__":`. This removes ~36 workflow lines, makes scripts independently testable, and lets the workflow call them with a single line.
21. **Scope full repository audits systematically.** Cover 6 dimensions: (1) file structure, (2) workflow, (3) Python scripts, (4) configuration, (5) documentation, (6) generated file policy. Report prioritized by severity (🔴 / 🟡 / 🔵 / ⚪).
22. **Be selective with SukkaW direct/download sources.** `Source/non_ip/domestic.conf` is a China source; do not duplicate. `Source/non_ip/download.conf` may have `DOMAIN-WILDCARD` — only copy compatible rules. `Source/non_ip/direct.conf` is a personal mix; borrow targeted downloader process rules only.
23. **Use DOMAIN (not DOMAIN-SUFFIX) for exact hostnames in exclude files.** `DOMAIN-SUFFIX` would match hypothetical subdomains, over-excluding. Only use `DOMAIN-SUFFIX` for registrable domains meant to cover all subdomains.
24. **When the remote has an auto-generated workflow commit, do not rebase local `.list` edits.** Keep only Manual include/exclude changes, reset `.list` files to remote HEAD, commit Manual files alone. The next workflow run regenerates `.list` with new excludes.
25. **Prune shared third-party service domains from service-specific rulesets.** Exclude bare shared suffixes (onetrust.com, braze.com, etc.) but KEEP service-prefixed subdomains (disney-portal.my.onetrust.com ✅).
26. **Service-OWNED infrastructure is not shared third-party.** Domains owned by Google (doubleclick.net, googleapis.com), Microsoft (azure.com), Meta (facebook.net) legitimately belong in their service rulesets.
28. **Opaque-ID subdomains under shared infrastructure are NOT service-prefixed.** Opaque hex/numeric IDs (o207216.ingest.sentry.io) are not brand prefixes. Heuristic: first label is all-digits, all-hex, or ≤6 random chars → exclude. Brand-prefixed (disney.my.sentry.io) → keep.
29. **Re-route domestic country-code domains from proxy rules to DIRECT.** Exclude `.cn` domains from service proxy rules and add to `Rule/Manual/China.txt`. Add to BOTH the service's `*.exclude.txt` AND `China.txt`.

## Incremental Upstream Update Workflow

For repos that sync multiple upstream rule sources on a schedule, avoid
regenerating every ruleset on every run. Use an **HTTP HEAD timestamp
check** to only regenerate changed rulesets.

### Architecture

```
06:00 JST Cron Trigger
  ↓
① check_upstream_updates.py
   HTTP HEAD each of 38+ upstream URLs
   Compare Last-Modified / ETag with cached state (source_state.json)
   Output: JSON list of changed ruleset filenames
  ↓
② changed_count > 0?
   YES → regenerate only changed rulesets
   NO  → skip all generation steps, no commit
  ↓
③ manifests → diff → validate → audit → commit
```

### Script: `scripts/check_upstream_updates.py`

Key design decisions:

1. **HTTP HEAD first** — lightweight, no body download. Falls back to
   GET (Range: 0-0) then full GET if HEAD fails.
2. **ETag > Last-Modified > Content-Length** — ETag is the most reliable
   change indicator; Content-Length is the least reliable fallback.
3. **Source→ruleset mapping** — hardcoded dict in the script maps each
   upstream URL to the `.list` file(s) it feeds into. Must match the
   workflow's `process_rule` calls exactly.
4. **State file** (`scripts/source_state.json`) — committed to git so
   each workflow run compares against the previous run's state.
5. **Unknown-timestamp sources** — if a source returns no timestamp
   headers (403, timeout), it's treated as "unchanged" to avoid
   regenerating every run. The count of unknown sources is reported.
6. **Global.list cascade** — when any overlap-dependent ruleset changes
   (YouTube, Netflix, Disney, etc.), Global.list is automatically added
   to the changed list because `prune_global_first_match_overlaps` must
   rerun.

### Workflow integration

Add these steps before the generation step:

```yaml
- name: Check Upstream Updates
  id: check_upstream
  shell: bash
  run: |
    set -euo pipefail
    output=$(python3 scripts/check_upstream_updates.py 2>&1) || true
    echo "$output"
    summary=$(echo "$output" | grep '^{' | tail -1)
    changed=$(echo "$summary" | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d['rulesets']))" 2>/dev/null || echo "[]")
    echo "changed_rulesets=$changed" >> "$GITHUB_OUTPUT"
    count=$(echo "$summary" | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d['rulesets']))" 2>/dev/null || echo "0")
    echo "changed_count=$count" >> "$GITHUB_OUTPUT"
```

Then wrap the generation step in a conditional:

```yaml
- name: Generate Rules
  if: ${{ fromJson(steps.check_upstream.outputs.changed_count) > 0 }}
  shell: bash
  run: |
    # Parse changed rulesets into array
    IFS=' ' read -ra CHANGED < <(echo '${{ steps.check_upstream.outputs.changed_rulesets }}' | python3 -c "import json,sys; [print(r) for r in json.load(sys.stdin)]")
    
    should_process() {
      local target="$1"
      for c in "${CHANGED[@]}"; do [ "$c" = "$target" ] && return 0; done
      return 1
    }
    
    # Then wrap each process_rule call:
    if should_process "YouTube.list"; then
      process_rule "YouTube.list" "YouTube" \
        "blackmatrix7 YouTube|$BM7/YouTube/YouTube.list"
    fi
```

All downstream steps (manifests, diff, validate, audit, commit) should
also be conditional on `changed_count > 0`.

### Pitfalls

- **Source URL list must be manually synced** with the workflow's
  `process_rule` calls. If you add/remove a source in the workflow, the
  `SOURCE_RULESET_MAP` in the check script must be updated too.
- **First run always shows all sources as "changed"** because there's no
  previous state to compare against. This is correct — it regenerates
  everything once, then subsequent runs are incremental.
- **Unavailable sources are marked unchanged** to avoid spam. If a source
  is down, the check script treats it as "no change" and won't regenerate
  its ruleset. This means a genuinely changed source that happens to be
  unreachable will be missed until it's reachable again.
- **`source_state.json` must be git-committed** for the cross-run
  comparison to work. Add it to the workflow's `git add` line.
- **Cron schedule should use the timezone-correct UTC offset.** For 06:00
  JST (UTC+9), use `0 21 * * *`.
29. **ruleset.skk.moe blocks HEAD requests (403 Forbidden).** The check script gracefully marks these as unavailable → unchanged. To force their update, trigger `workflow_dispatch` manually in GitHub Actions. The source URLs still work for the actual content fetch within `process_rule` — only the HEAD check fails.
30. **SOURCECODE_MAP drift from workflow changes.** Every time you add/remove/modify a `process_rule` call in the workflow, update `check_upstream_updates.py`'s `SOURCE_RULESET_MAP` dict. The mapping encodes the same data as the workflow's `process_rule` arguments — they must agree. Add a CI step or lint check to catch drift early.
31. **Conditional workflow steps break manual dispatch dry-run.** If you wrap generation in `if: changed_count > 0`, a manual `workflow_dispatch` with `dry_run=true` won't run generation on a no-change day. Add a secondary condition: `if: changed_count > 0 || github.event_name == 'workflow_dispatch'`.
33. **New rule types need dual registration in TWO validation checkpoints.** When adding a Surge rule type not already in the known-good list (e.g. `GEOIP`), you MUST add it to BOTH: (a) `scripts/validate_surge_repo.py` → `ALLOWED_TYPES` set, AND (b) `.github/workflows/auto-rules.yml` → the awk regex inside `validate_rules()` (the `$0 !~ /^(DOMAIN|...)/` pattern). Missing either causes the workflow to fail at the Validate step. The workflow's inline awk validation runs BEFORE `validate_surge_repo.py` and catches new types first.
34. **README rule table must render as single-line rows on GitHub.** Key rules:
   - **No backticks** around filenames (e.g. `AI.list`, not `` `AI.list` ``) — wastes column width.
   - **Use `·` (U+00B7 middle dot)** as multi-source separator instead of `、` or `,` (more compact, renders everywhere).
   - **Use `（）` (fullwidth or halfwidth parens)** for sub-clauses: `（domain-only）` not `· domain-only`.
   - **Avoid flag emojis** (🇨🇳) in tables — they use 2 codepoints and may not render on all systems. Use single-codepoint emojis (🍎).
   - **Related files MUST use the same emoji.** When two rulesets share a brand family (Apple/Apple_CN, Microsoft/Microsoft_CDN), use identical emoji. Different emoji for a single brand's sub-files reads as inconsistency — user will flag it.
   - **No empty-column tables** (`| | |` with `|---|---|`) — use dash lists (`- 🎯 **label**：...`) instead.
   - **Describe every row in ≤1 line.** Compress descriptions aggressively. Drop filler words like "规则"、`专属` when context already clear.
   - **Non-primary upstream sources** should be removed from source columns (e.g. Rabbit-Spec reuses others' upstreams — remove from table, keep in acknowledgments only).
   - **Data-only sources** (Telegram CIDR, public IP lists) don't belong in acknowledgments — that section is for projects/people to thank.
   - **Loading order entries** should use actual ruleset names (`GlobalMedia + ChinaMedia`), not abstract labels (`Streaming Media`).
36. **P0 issues from external code reviews.** When a review flags these, fix immediately — they are correctness/trust issues, not style:
    - **Missing LICENSE file**: README says MIT but no `LICENSE` exists → create standard MIT with `Copyright (c) <year> <owner>`.
    - **dry_run not honored**: workflow has `inputs.dry_run` but the Commit step doesn't check it → add `&& inputs.dry_run != 'true'` to the step's `if:` condition and add a `Dry Run Summary` step that echoes `::notice::` and runs `git status --short`.
    - **README/cron time mismatch**: README says 04:00 Beijing but cron is `0 21 * * *` (05:00 Beijing) → fix README to match actual cron, update workflow comment to include Beijing time.
    - **Manifest glob mismatch**: `audit_rules.py` looks for `*.manifest.json` but `manifest.py` generates `*.manifest` → fix glob to `*.manifest`.
    - **Stale docstring**: `manifest.py` says `.manifests/ is NOT committed` but workflow `git add` includes it → update docstring to say it IS committed (needed for `diff_manifests.py` to diff against HEAD).
37. **GitHub repo polish checklist for first public release.** When a Surge rules repo goes public, three things matter for discoverability and trust:
    - **Repository description**: set via `gh repo edit --description "..."`. Keep it to one line — what does the repo do, for whom.
    - **Topics**: `gh repo edit --add-topic <tag>` for each relevant keyword. Common: `surge`, `rule-set`, `proxy`, `github-actions`, `python`, `automation`.
    - **Initial release**: `git tag -a v0.1.0 -m "..."` then `gh release create v0.1.0 --title "..." --notes "..."`. Signals the repo is in a usable state. Include capability summary in release notes.

38. **"等 wraps alone" anti-pattern in description columns.** When a table description is one character over the line-break threshold, a trailing `等` often wraps to its own line — reads as a visual bug. If the description pushes the column to the edge, drop trailing `等` and trim the list. Prefer: "AI 服务与模型 API" over "AI 服务、模型 API、Cursor、Zed、Groq、xAI、Doubao 等". If a user sends a screenshot with a red box around a lone character on line 2, it's this bug.

39. **README brevity: details live in AGENT.md, not README tables.** README is for discovery and overview. When AGENT.md already has verbose policy descriptions, examples, and domain lists, the README should be a crisp one-line-per-row summary. Strip: backtick formatting, bold markup, parenthetical examples (e.g. `（如 release-assets.githubusercontent.com）`), domain lists, and long sub-clauses. Each table row must fit on one visual line.

40. **Agent-Reach inspired README restyle.** When modernizing a README, borrow these patterns from high-star repos:
    - **Badge row** at top: License, Python version, relevant ecosystem badges.
    - **Blockquote tagline** after the title: one bold sentence summing up the project's value.
    - **📌 Project overview card**: target user, core value, license, update frequency, quality — as a dash list (not an empty-column `| | |` table).
    - **❓ Why this repo**: pain-point → solution table with emoji.
    - **✅ Core features**: compact table, no duplicates with the "why" section.
    - **🚀 Quick start**: copy-pasteable one-liners.
    - **Emoji section headers** with horizontal rules between sections.
    - Delete verbose descriptions the user flags with "后面不需要写这么多" or "说明没必要写这么详细".
    - If a review says "没有图标" about an emoji, check if it's a flag emoji (2 codepoints, often broken). Replace with single-codepoint alternatives.

41. **Public/private layer separation for personal rule repos.** When a repo started as a personal project but is now public (or about to go public), split into two layers:\n    - **Public layer** (committed): `README.md`, `LICENSE`, `Conf/`, `Rule/*.list` (generated), `Rule/.manifests/`, `scripts/`, `Module/`, `.github/`, `AGENT.md` (strategy only).\n    - **Private layer** (local only): `Rule/Manual/` (personal add/exclude rules), `.codex/` or `.skills/` (agent skills), personal preferences.\n    Steps: (a) `echo -e '\\n# Private\\nRule/Manual/\\n.codex/\\n.skills/' >> .gitignore`, (b) `git rm -r --cached Rule/Manual/ .codex/` to untrack without deleting local files, (c) move agent skills to `~/.skills/skills/` (prefer `.skills` over `.codex` — no brand association, harder for others to deduce the agent platform), (d) rewrite `AGENT.md` to strip Skill Maintenance, Completion Standard, and agent-internal workflow references — keep only routing strategy, rule authoring guidelines, pipeline rules, and validation checklist, (e) verify local files still exist after untracking.\n    - **Naming convention**: always use `~/.skills/` not `~/.codex/` for local agent skill storage. The latter leaks which agent platform the user runs. The former is generic and could be any editor/agent/IDE.\n\n42. **Workflow refactoring: bash → Python extraction.** When a workflow YAML is 600+ lines with embedded bash functions, extract to a Python script:
    - Create `scripts/generate_rules.py` with all rule specs, source URIs, processing functions, guardrails, validation, and Global overlap pruning.
    - Pass `CHANGED_RULESETS` via environment variable (JSON array from `check_upstream_updates` output).
    - On `workflow_dispatch` (manual trigger), process all rulesets regardless of changed list.
    - After extraction, delete all orphaned bash lines from the YAML; a YAML syntax check will catch leftovers.
    - Test import: `python3 -c "import scripts.generate_rules; print(len(generate_rules.RULE_SPECS))"`.
    - Expected result: 632-line workflow → 127 lines, all logic in Python that can be tested independently.

42. **P1 hardening after P0 fixes.** After fixing critical issues, harden the pipeline:
    - **curl retry**: add `--retry 3 --retry-delay 5` to all rule-source fetch commands in both bash and Python.
    - **Lightweight CI**: add `.github/workflows/ci.yml` triggered on `push`/`pull_request` to `main`, running `validate_surge_repo.py` only. Catches manual rule-edit regressions before commit.
    - **Fork guide in README**: add "适合谁 / 如何 Fork" section with: who this is for / not for, 3-step adaptation after fork, upstream sync command.
    - **AGENT.md privacy**: remove personal details (travel paths, specific devices) from public repo; keep only general constraints. Remove agent-internal wording like "update Hermes memory", "check agents/openai.yaml".

## Project-Specific References

- `references/linnux-surge-repo-notes.md` — durable notes from auditing `linnux-x/surge`, including workflow risks and guardrails.
- `references/linnux-surge-incremental-upstream-check.md` — implementation details for the `check_upstream_updates.py` script, source→ruleset mapping, state file format, and workflow integration.
- `references/linnux-surge-rule-split-patterns.md` — concrete split/refactor patterns from AI, Apple, and CDN rule cleanup, including timestamp discipline, Manual include/exclude hygiene, and first-match samples.
- `references/linnux-surge-media-china-cdn-splits.md` — detailed destination-reporting and split patterns for China/China_IP, CDN, ChinaMedia, and GlobalMedia cleanup.
- `references/linnux-surge-global-fallback-pruning.md` — post-generation Global fallback pruning pattern, destination reporting by first-match ruleset, and Apple Akamai exception handling.
- `references/linnux-surge-semantic-overlap-pruning.md` — pruning redundant entries from later rulesets when early-position rules (Speedtest, WeChat, PayPal, Netflix, Disney) already match them; DOMAIN vs DOMAIN-SUFFIX correctness in excludes; git conflict resolution with auto-generated workflow commits.
- `references/linnux-surge-validate-script-enhancement.md` — pattern for extending validate_surge_repo.py alongside exclude files; shared third-party infrastructure checks; PayPal CN domain checks; prefix heuristic for service-specific subdomains.
- `references/linnux-surge-third-party-and-domestic-pruning.md` — identifying and excluding shared third-party service domains (onetrust, adobedtm, braze, conviva, AWS regions, etc.) from service-specific rulesets; prefix-based keep/exclude decision table; domestic country-code domain re-routing (PayPal China → DIRECT).
- `references/linnux-surge-upstream-analysis.md` — comparative analysis of ConnersHua/RuleGo and SukkaW/Surge upstream repositories: design philosophies, rule inventories, coverage gaps, and what was adopted (GEOIP,GOOGLE, etc.).
