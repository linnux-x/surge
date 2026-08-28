# 脚本目录｜Surge 规则流水线

本目录保存 `linnux-x/surge` 仓库的规则生成、校验、审计和辅助脚本。

所有核心流水线脚本只使用 **Python 3.10+ 标准库**，不依赖第三方包。

---


## Full generation 发布前审计

手动触发 GitHub Actions `workflow_dispatch` 会进行 full generation。发布门禁的完整流程以 `CONTRIBUTING.md` 为准：先 `dry_run=true` 审查生成结果、manifest diff 和在线审计输出，审计通过后才允许 `manual_audit_confirmed=true` 发布。

Rabbit-Spec 来源当前明确保留，用于补充 AIGC、China、ChinaCIDR 覆盖；不要在普通源清理中移除。

---

## 流水线顺序

| 步骤 | 脚本 | 作用 |
|---:|---|---|
| 1 | `check_upstream_updates.py` | 并行检查所有上游源是否变更，识别需要更新的规则集 |
| 2 | `generate_rules.py` | 下载、合并、清洗、校验规则；应用手工规则、排除规则、护栏、CIDR 裁剪和 Global 重叠裁剪 |
| 3 | `manifest.py` | 生成每个规则文件的 manifest：`<stable_id>	<source_name>`；`--diff` 用于生成差异报告 |
| 4 | `generate_receipt.py` | 汇总 manifest、diff、规则类型与公开 Manual 基线，生成确定性发布收据 |
| 5 | `generate_clash_rules.py` | 将 `Rule/*.list` 转换为 `clash/*.yaml`，供 Clash / mihomo rule-provider 使用 |
| 6 | `validate_surge_repo.py` | 仓库级不变量检查，含公开 Manual override manifest 合同 |
| 7 | `audit_rules.py` | 生成后联网审计：上游可达性、规则数量、共享基础设施、Surge 文档、exclude 覆盖等 |
| 8 | `cross_file_conflicts.py` | 手动辅助（不再由自动任务调用）：列出同一域名跨不同策略文件重复出现时的 first-match 实际生效关系 |

---

## 单一事实来源

| 模块 | 作用 |
|---|---|
| `sources.py` | 所有上游 URL 和规则集规格的单一来源 |
| `policy.py` | 路由策略常量的单一来源：服务边界正则（GitHub / fast.com / YouTube）、共享基础设施域名清单（严格层阻断提交，宽泛层仅审计告警，宽泛层按超集构造，两层不会漂移） |
| `rule_validator.py` | `generate_rules.py` 和 `validate_surge_repo.py` 共用的规则校验逻辑，策略常量取自 `policy.py` |
| `http_util.py` | urllib 抓取的统一入口（超时 / UA 一致）；`generate_rules.py` 保留 curl 用于批量下载（带显式超时），`check_upstream_updates.py` 保留专用 HEAD 探测 |

---

## 脚本产物的入库规则

三个产物入库、一个不入库，规则不是随意的：

| 文件 | 是否入库 | 原因 |
|---|---|---|
| `source_state.json` | ✅ | 上游 Last-Modified / ETag 基线。CI 靠它判断"哪些上游变了"，不入库则每次全量重下 |
| `diff_report.*` / `generation_receipt.*` | ✅ | 变更审阅材料与确定性发布收据；入库才能复核规则增删、来源与类型摘要 |
| `audit_report.json` | ❌ | 联网审计的即时结果，随上游可达性和网络状况波动，入库只会制造无意义的 diff 噪声。已在 `.gitignore` 排除 |

判断标准：**跨运行需要保持的状态、以及需要被人审阅的变更记录才入库；每次运行都会变且只反映当时环境的结果不入库。**

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
python3 scripts/generate_receipt.py

# 4. 生成 Clash / mihomo rule-provider
python3 scripts/generate_clash_rules.py --validate

# 5. 校验仓库
python3 scripts/validate_surge_repo.py

# 6. 联网审计
python3 scripts/audit_rules.py

# 7. 查看跨文件策略冲突（--summary 为 CI 信息性输出同款）
python3 scripts/cross_file_conflicts.py
python3 scripts/cross_file_conflicts.py --summary

# 测试路由顺序
python3 scripts/test_routing_order.py

# 从 iOS 隐私报告生成 Surge 规则（示例输出到 /tmp，避免误认为仓库固定规则文件）
python3 scripts/ios_privacy_to_surge.py report.ndjson
privacy2surge report.ndjson -o /tmp/App.list

# 审计当前 Download.list 命中的下载主机；报告仅供人工复核，不会写入规则
python3 scripts/download_cn_candidates.py TrafficStatistics.csv \
  --resolve -o /tmp/download-cn-candidates.json
```

---

## 工具脚本

| 脚本 | 作用 |
|---|---|
| `ios_privacy_to_surge.py` | 将 iOS 隐私报告 `.ndjson` 转换为 Surge / Loon 规则；过滤系统流量、合并子域名、通过 iTunes API 和内置映射识别 App |
| `download_cn_candidates.py` | 审计 Surge TrafficStatistics CSV 中当前命中 Download.list 的主机；可选本地 DNS + China_IP 信号，仅输出待人工复核候选，绝不生成或写入 DIRECT 规则 |
| `app_mapping.json` | Bundle ID 到 App 名称、域名、IP 的可扩展映射 |

---

## 设计原则

- **不需要 pip install**：核心流水线脚本只依赖标准库。
- **单一事实来源**：上游源集中在 `sources.py`，校验规则集中在 `rule_validator.py`，策略常量集中在 `policy.py`。
- **减少散落文件**：CIDR 裁剪内置于 `generate_rules.py`，manifest diff 内置于 `manifest.py --diff`。
- **导入模块，不解析配置**：脚本直接 import `sources.py`，不再解析 YAML / JSON 作为 source 配置。
