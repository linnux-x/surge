# 脚本目录｜Surge 规则流水线

本目录保存 `linnux-x/surge` 仓库的规则生成、校验、审计和辅助脚本。

所有核心流水线脚本只使用 **Python 3.10+ 标准库**，不依赖第三方包。

---


## Full generation 发布前审计

手动触发 GitHub Actions `workflow_dispatch` 时，会进行 full generation。正式发布前必须先运行一次 `dry_run=true`，人工审查生成结果、manifest diff 和在线审计输出。审计通过后，才允许使用 `manual_audit_confirmed=true` 发布。

Rabbit-Spec 来源当前明确保留，用于补充 AIGC、China、ChinaCIDR 覆盖；不要在普通源清理中移除。

---

## 流水线顺序

| 步骤 | 脚本 | 作用 |
|---:|---|---|
| 1 | `check_upstream_updates.py` | 并行检查所有上游源是否变更，识别需要更新的规则集 |
| 2 | `generate_rules.py` | 下载、合并、清洗、校验规则；应用手工规则、排除规则、护栏、CIDR 裁剪和 Global 重叠裁剪 |
| 3 | `manifest.py` | 生成每个规则文件的 manifest：`<stable_id>	<source_name>`；`--diff` 用于生成差异报告 |
| 4 | `validate_surge_repo.py` | 仓库级不变量检查，规则内容校验委托给 `rule_validator.py` |
| 5 | `audit_rules.py` | 生成后联网审计：上游可达性、规则数量、共享基础设施、Surge 文档、exclude 覆盖等 |

---

## 单一事实来源

| 模块 | 作用 |
|---|---|
| `sources.py` | 所有上游 URL 和规则集规格的单一来源 |
| `rule_validator.py` | `generate_rules.py` 和 `validate_surge_repo.py` 共用的规则校验逻辑 |

---

## 本地使用

```bash
# 1. 检查哪些上游发生变化
python3 scripts/check_upstream_updates.py

# 2. 生成规则
CHANGED_RULESETS='["AI.list"]' python3 scripts/generate_rules.py

# 3. 生成 manifest 和 diff 报告
python3 scripts/manifest.py
python3 scripts/manifest.py --diff

# 4. 校验仓库
python3 scripts/validate_surge_repo.py

# 5. 联网审计
python3 scripts/audit_rules.py

# 测试路由顺序
python3 scripts/test_routing_order.py

# 从 iOS 隐私报告生成 Surge 规则
python3 scripts/ios_privacy_to_surge.py report.ndjson
privacy2surge report.ndjson -o Rule/App.list
```

---

## 工具脚本

| 脚本 | 作用 |
|---|---|
| `ios_privacy_to_surge.py` | 将 iOS 隐私报告 `.ndjson` 转换为 Surge / Loon 规则；过滤系统流量、合并子域名、通过 iTunes API 和内置映射识别 App |
| `app_mapping.json` | Bundle ID 到 App 名称、域名、IP 的可扩展映射 |
| `vps_monitor.py` | 轻量 HTTP 服务，暴露系统指标 JSON，供 Surge Panel 使用；通过 `VPS_MONITOR_HOST` 和 `VPS_MONITOR_TOKEN` 配置 |

---

## 设计原则

- **不需要 pip install**：核心流水线脚本只依赖标准库。
- **单一事实来源**：上游源集中在 `sources.py`，校验规则集中在 `rule_validator.py`。
- **减少散落文件**：CIDR 裁剪内置于 `generate_rules.py`，manifest diff 内置于 `manifest.py --diff`。
- **导入模块，不解析配置**：脚本直接 import `sources.py`，不再解析 YAML / JSON 作为 source 配置。
