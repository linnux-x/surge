# 测试目录｜路由顺序与校验

本目录用于保存 `linnux-x/surge` 的路由顺序模拟和校验测试数据。

测试脚本只使用 **Python 3.10+ 标准库**。

---

## 运行测试

```bash
# 全部单元与行为保持测试
python3 -B -m unittest discover -s tests -p 'test_*.py'

# 模拟 Surge first-match 路由逻辑，并与预期结果对比
python3 scripts/test_routing_order.py

# 或从仓库根目录运行
cd /path/to/surge
python3 scripts/test_routing_order.py
```

---

## 测试文件

| 文件 | 用途 |
|---|---|
| `expected-routing.csv` | 测试用例：域名 → 期望命中的规则集 |

---

## 添加测试用例

编辑：

```text
tests/expected-routing.csv
```

格式：

```csv
domain,expected_ruleset,expected_policy,note
example.com,AI.list,AI,说明为什么应该命中 AI.list
```

字段说明：

| 字段 | 说明 |
|---|---|
| `domain` | 要测试的域名，建议小写 |
| `expected_ruleset` | 期望命中的 `.list` 文件；中国 / 局域网规则可写 `DIRECT`，最终兜底可写 `Global` |
| `expected_policy` | 必填，期望目标策略；与规则集同时断言，防止意外直连 |
| `note` | 人类可读说明，解释为什么应命中该规则 |

测试脚本会读取所有 `Rule/*.list` 文件，模拟 Surge 的 first-match 逻辑，并报告预期与实际路由不一致的条目。

模拟覆盖域名、尾随点规范化与字面 IPv4/IPv6 CIDR 匹配。不执行 DNS 查询，也不模拟 ASN、进程或 SNI/HTTP Host；这些场景需要真实 Surge 验收。

## 重构行为基线

`test_source_transforms.py` 使用 `fixtures/generation-baseline.json` 中从 `d84c77e` 提前采集的结果，比较六种格式的完整文件字节和 26 个目标的过滤行为。`test_upstream_probe.py` 覆盖 HTTP 回退顺序、元数据与响应关闭。基线不能为了让测试通过而自动重录；有意改变行为时应单独审阅预期结果。


`test_cidr_contracts.py` 使用从 `716da36` 提前采集的 `fixtures/cidr-baseline.json`，
验证 CIDR 文件字节、错误与日志，并用独立的两两网段包含判据验证索引算法。
`test_ruleset_dependencies.py` 检查全部来源的增量依赖与 Global 裁剪范围，明确保留 Apple_CN 例外。

当前规则语料的新旧全文件对照（不联网、不改写 Rule/）：

```bash
python3 -B tests/compare_pipeline_baseline.py
```

该脚本需要 Git 中存在基线 `716da36709816751da26abd22a400ea650956ba9`；浅克隆需先取得该提交。
它从基线提取旧脚本，在独立进程中回放当前规则、Manual 及 Global 后处理，并比较完整内容和诊断。
计时只是单次本地离线观测，不能推断网络生成或发布速度。


`test_automation_preflight.py` 验证主收据不可写时的备用失败证据、0600 权限、
就绪状态不能覆盖业务结果，并在临时真实 Git 仓库中检查 origin、dirty 阻断、
旧调度器 ACTIVE 阻断与原子替换清理；不接触真实任务收据。

## 2026-10-04 审计修复回归

`test_exclusions.py` 覆盖裸值拒绝、域名大小写/选项变体、规则类型边界、IP 选项保留及独立
生成物检查。`test_file_batch.py` 注入暂存失败、晚期替换失败和回滚失败，检查新增、删除、
原文件权限和恢复材料。`test_generation_safety.py` 验证第二个来源失败不会发布第一个结果；
`test_upstream_probe.py` 验证不可达与无版本标记分开处理，失败不提升源状态。

路由表保留原有 197 项，并扩展历史排除迁移、AWS、ByteOversea、共享遥测与关键词负例。
合成的 `audit-child.*`、`*.example.com` 只用于规则求值，不代表实际访问记录。
