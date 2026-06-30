# Contributing to Linnux Surge Rules

Thanks for your interest in contributing! This repository is an automated Surge ruleset pipeline. Here's how to help.

## Quick Start

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/surge.git
cd surge

# 2. No dependencies needed — Python 3.10+ stdlib only
python3 --version  # should be 3.10+

# 3. Run the test suite
python3 scripts/test_routing_order.py

# 4. Run validation
python3 scripts/validate_surge_repo.py
```

## What You Can Contribute

| Area | Examples |
|------|----------|
| 🐛 **Bug fixes** | Pipeline script fixes, validation logic corrections, README inaccuracies |
| 🔧 **New rulesets** | Adding a new upstream source for a missing service category |
| 📝 **Documentation** | README improvements, code comments, usage guides |
| 🧪 **Tests** | Adding test cases to `tests/expected-routing.csv` |
| 🛡️ **Validation** | New invariant checks in `scripts/rule_validator.py` |

## Project Architecture

```
scripts/
├── sources.py                 ← Single source of truth for upstream URLs
├── check_upstream_updates.py  ← Detects changed upstreams (parallel HEAD)
├── generate_rules.py          ← Downloads, merges, cleans, validates rules
│   └── rule_validator.py      ← Shared validation engine
├── manifest.py                ← Generates manifests + diffs against git HEAD
├── validate_surge_repo.py     ← Repository-level invariants
├── audit_rules.py             ← Post-generation online audits
├── test_routing_order.py      ← Routing simulation tests
├── ios_privacy_to_surge.py    ← iOS privacy report → Surge rules converter
└── vps_monitor.py             ← Lightweight VPS metrics server for Surge Panel

tests/
└── expected-routing.csv       ← Domain → expected ruleset mappings
```

**Key principle:** `scripts/sources.py` is the single source of truth for upstream URLs. `scripts/rule_validator.py` is the single source of truth for validation rules. All other scripts import from these — never duplicate or hardcode.

## Development Workflow

1. **Create a branch:** `git checkout -b fix/your-change`
2. **Make changes:** Edit the relevant scripts
3. **Test locally:**
   ```bash
   python3 scripts/test_routing_order.py
   python3 scripts/validate_surge_repo.py
   ```
4. **Format:** No formatter required — keep code readable and consistent with existing style
5. **Commit:** Clear, concise commit messages
6. **Open a PR:** Target `main` branch


## Full Generation 发布前手动审计

`workflow_dispatch` 会触发 full generation：即使上游没有检测到变化，也会重新生成所有规则集。为了避免一次性全量生成把上游异常、分类漂移或共享基础设施误提交到公开仓库，发布前必须先做一次手动审计。

推荐流程：

1. 在 GitHub Actions 手动运行 `Auto-Surge-Rules`，设置 `dry_run=true`。
2. 审查 Actions 输出中的：
   - `Generate Rules`
   - `Generate Manifests & Diff`
   - `Validate Repository Invariants`
   - `Online Audit`
3. 重点检查：
   - `Rule/*.list` 是否出现异常大幅增删；
   - `scripts/diff_report.md` 是否符合预期；
   - Rabbit-Spec 来源是否仍保留并正常拉取；
   - shared infrastructure 提示是否需要 exclude 或 service-owned 例外；
   - `audit_rules.py` 是否无 error / warning。
4. 手动审计通过后，再次运行 `workflow_dispatch`，设置：
   - `dry_run=false`
   - `manual_audit_confirmed=true`

如果未确认 `manual_audit_confirmed=true`，full generation 不允许 commit / push。

## Pull Request Guidelines

- **One concern per PR.** Bug fix, feature, and refactor in separate PRs.
- **Test your changes.** Add test cases if you're changing routing logic.
- **Don't change `Rule/*.list` directly.** These are auto-generated. Edit `scripts/` or `Rule/Manual/` instead.
- **Don't add third-party dependencies.** All scripts must use Python stdlib only.
- **Update `scripts/README.md`** if you add new scripts.
- **If adding to `Rule/Manual/README.md`**, that file is tracked (not .gitignored) — personal rules go in `.txt` / `.exclude.txt`.

## Adding a New Upstream Source

1. Add the URL to `scripts/sources.py` in `RULE_SPECS`
2. Create `Rule/Manual/<RulesetName>.txt` if manual rules needed
3. Create `Rule/Manual/<RulesetName>.exclude.txt` if any patterns need excluding
4. Add a row to the README rule list table
5. Add the ruleset to `Conf/Linnux.conf` [Rule] section at the correct priority position
6. Run `python3 scripts/validate_surge_repo.py` to verify

## Adding a New Validation Check

1. Add the check function to `scripts/rule_validator.py` — it's used by both `generate_rules.py` and `validate_surge_repo.py`
2. Add corresponding test cases to `tests/expected-routing.csv` if routing-visible

## Code Style

- Python 3.10+ type hints (`list[str]`, `dict[str, int]`, `str | None`)
- Standard library only — no `pip install` required
- Use `pathlib.Path` for file operations
- Functions should be small, single-purpose, well-documented
- Use `from __future__ import annotations` at top of files

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
