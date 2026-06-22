---
name: surge-ruleset-builder
description: Research, create, refine, and validate Surge external RULE-SET files. Use when Codex is asked to generate a Surge rule collection for a service or category, compare community rule repositories, search online for missing domains or IP ranges, convert a rule file to .list, reduce false positives, or save a ruleset in the current project.
---

# Surge Ruleset Builder

Create compact, complete, auditable Surge external rulesets.

## Start Here

**Read `AGENT.md` first.** It contains all repository-specific preferences, project guardrails, validation standards, and the service vs shared infrastructure classification guide. This skill does not duplicate those rules — it extends them with Codex-specific workflow and construction details.

After reading AGENT.md, read:
- `references/sources.md` — upstream rule sources and research priority
- `references/Learned Patterns.md` — verified reusable findings from past tasks

## Codex Workflow

1. Read `AGENT.md`, `references/sources.md`, and `references/Learned Patterns.md`.
2. Select relevant official and community sources from `references/sources.md`.
3. Read the current project ruleset before modifying. Do not treat generated `Rule/*.list` files as durable baseline. Preserve local entries in `Rule/Manual/*.txt`; remove durable exclusions through `Rule/Manual/*.exclude.txt`.
4. Check current Surge syntax in the official documentation when uncertain. Follow priority: release log → Manual → Knowledge Base. Use `https://nssurge.com/llms.txt` as the unified index.
5. Compare at least two relevant community sources. Treat community lists as candidate inventories, not authority.
6. Search the web for recent official domain, ASN, network, API endpoint, or client information.
7. Define the ruleset's intended product surface before selecting candidates. For "all" requests, turn scope into an explicit product-category inventory.
8. Build a normalized candidate set, then remove duplicates, covered entries, stale entries, unrelated surfaces, and high-risk shared infrastructure.
9. For repository-wide work, assign each rule to an ownership layer and define first-match order before resolving cross-file overlap.
10. Save as `<Service>.list` in `Rule/` by default.
11. When changing automation, update the workflow and generated files together. Run `python3 scripts/validate_surge_repo.py` before committing.
12. Delete obsolete legacy workflows instead of retaining them.
13. Validate and report: path, rule count, inclusions, exclusions, and destination of removed entries.
14. Run the Continuous Improvement review below only when the task produced durable, verified knowledge.

## Construction Rules

- Produce a Surge external ruleset, not a complete Surge profile.
- One rule per line, never append a policy name.
- Convert explicit domainset inputs: `.example.com` → `DOMAIN-SUFFIX,example.com`, bare hostname → `DOMAIN,hostname`.
- Name files consistently: capitalize first segment, preserve service capitalization, uppercase after `_`. Example: `Apple_CN.list`, `China_IP.list`.
- Use ASCII `#` comments. Keep headers short.
- Prefer `DOMAIN` → `DOMAIN-SUFFIX` → `DOMAIN-KEYWORD` (only for stable patterns).
- Do not treat upstream wildcard-looking host patterns as Surge rules. Convert or exclude.
- Add `no-resolve` to IP rules unless resolution is intentionally required. `China_IP.list` is the project exception.
- `USER-AGENT` and `PROCESS-PROCESS` are platform-limited fallbacks. `PROCESS-NAME` is Mac-only, ignored by Surge iOS.
- Keep ruleset-wide options such as `extended-matching` on the `RULE-SET` declaration in the main profile.
- Allow documented Surge logical rules (`AND`, `OR`, `NOT`) when policy-free.
- Order rules: exact domains → suffixes → keywords → IPv4 → IPv6 → client fallbacks.

## Write Safety

- Save locally first unless the user explicitly requests a GitHub write.
- Do not commit, push, or overwrite a remote file without explicit user intent.
- Summarize meaningful additions, removals, prefix corrections, and false-positive protections.

## Continuous Improvement

After each completed ruleset task:

1. Identify repeated failures, missing validation, ambiguous instruction, or reusable false-positive lessons.
2. Decide whether the lesson applies across multiple services or future tasks.
3. If durable and verified, make the smallest useful update to this skill. Keep workflow changes in `SKILL.md` and detailed findings in `references/Learned Patterns.md`.
4. Remove or replace guidance when current official documentation disproves it.
5. Do not modify the skill when a task yields no reusable improvement.
