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
