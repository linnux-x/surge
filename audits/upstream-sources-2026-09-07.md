# 上游入口与补充源审计 · 2026-09-07

保留现有主要作者和全部 41 个来源入口。本轮统一 SukkaW AI、CDN、Game Download
到作者官方 `https://ruleset.skk.moe/List`，其他既有 List URL 统一引用同一常量。
Download 主列表与 Speedtest 暂留 Source：分发产物增加了覆盖，须单独审查策略影响。

本次结论来自同一批冻结输入的离线回放；没有改写 `Rule/*.list` 或 Clash 产物，
也不代表变更已发布。工作基于主线 `74c06205706c106d8bcc63530e1a95d253b958b0`
及本地审计修复 `7173cbf09667bfb8cdf0267eddf716793a5fee16`。

## 分发入口决策

作者文档区分源片段与构建产物，并提供官方分发与镜像；不能假设路径替换等价。
参见 [SukkaW 官方仓库](https://github.com/SukkaW/Surge)、
[官方分发站](https://ruleset.skk.moe/)、[官方 GitHub 镜像](https://github.com/SukkaLab/ruleset.skk.moe)。
这次采样不证明 Source 与 List 对应同一提交，差异可能同时包含构建处理与更新时差。

| SukkaW 来源 | Source 规范化条数 | List 规范化条数 | 本轮处理 |
|---|---:|---:|---|
| AI | 51 | 50 | 切换；减少的 openai.com 后缀由其他 AI 来源覆盖 |
| CDN | 25 | 25 | 切换；集合相同 |
| Game Download | 54 | 52 | 切换；减少的两条在 Download 合并后不产生集合差异 |
| Download | 1630 | 1964 | 暂留；包括较广泛的 S3 下载域名覆盖 |
| Speedtest | 123 | 3368 | 暂留；包含新增境内测速端点 |

调用实际生成器执行清洗、Manual、exclude、护栏、去重、后缀及 CIDR 裁剪、Global 重叠裁剪后：

- **本轮选择：所有文件的有效规则集合增删为零。** 这是冻结输入对照，不保证未来上游内容永远等价。
- 全部五个入口切换：Download 新增 297 条，Speedtest 新增 657 条，均无删除。
- 对全部切换结果作 1,381 个合成主机/IP 探针对照，有 1,248 个 first-match 变化。其中 578 个从 GlobalMedia 进入 Download，16 个从 China/DIRECT 进入 Speedtest。后缀同时取根域与一个子域探针，数字不是独立服务数，更不是实际流量比例。
- 境内测速示例包括 `speedtest.bmcc.com.cn`、`beijing.unicomtest.com`、`ookla.speedtest.cnix.cn`。策略组变化不证明真实连接使用哪条出口。

后续先分类新增 S3 与境内测速域名，补充预期路由用例，再决定这两个入口是否切换。
当前不通过大范围 exclude 抵消差异，以免把上游迁移变成隐含的策略重写。

## 补充源价值

对本轮采用后的来源，逐个与同规则集其他来源及 Manual 比较。
“独有”指该保守模型下未被其他来源覆盖；不推断关键词、通配或 ASN 的语义包含。
CIDR 用区间并集比较，残余片段可能多于原规则数量；地址数去除自身重叠。
这些是规则覆盖指标，不是实际流量收益，也未验证每条新增地址的归属或可用性。

| 来源 / 规则集 | 规范化规则 | 未被其他来源覆盖 | 含义 |
|---|---:|---:|---|
| Rabbit-Spec / AI | 118 | 51 条 | 有实质补充，继续保留 |
| ConnersHua / AI | 63 | 18 条 | 有实质补充，继续保留 |
| Rabbit-Spec / China | 3712 | 186 条 | 有实质补充，继续保留 |
| Rabbit-Spec / China_IP | 9636 | 14 条、14 个 IPv4 地址 | 补充规模较小，先观察 |
| Telegram 官方 CIDR | 14 | 4 个片段、4096 个 IPv4 地址 | 保留官方地址补充 |
| Loyalsoldier / China_IP | 9622 | 0 | 本次全部被同组来源覆盖，列为观察项，不删除 |
| SukkaW / Telegram IP | 10 | 0 | 本次全部被同组来源覆盖，列为观察项，不删除 |
| Kelee 国际测速 | 17692 | 17054 个片段 | 大量补充，但本次使用 fallback，须结合新鲜度判断 |

零独有覆盖不等于没有维护、溯源或独立上游的价值。今后删减应至少结合多个更新周期的
同口径快照、失败/fallback 情况、完整生成差异及路由验证；本轮不执行来源删减。

## 证据与复现

[机器可读摘要](upstream-sources-2026-09-07.json) 保存 46 个 URL 的采样时间、状态、
内容 SHA-256、来源/Manual 哈希、全部 59 行来源贡献及入口回放增删规则。
46 个 URL 是 41 个配置来源加 5 个对照入口；44 个 live，Kelee 两个采用已登记快照。
Kelee China 快照标注 2025-09-16，国际快照标注 2026-08-22；采样时间不是快照内容更新时间。

本机原始缓存及完整贡献残余、合成路由探针报告保留于
`/Users/linnux/Desktop/.automation-state/upstream-audit-20260907/`，不把完整第三方原始列表复制入库。
`adopted-report/` 为本轮贡献，`report/entrypoint-routing-diff.json` 为全部切换的探针对照，
`replay/entrypoint-rule-diff.json` 为三种入口模式的生成对照。

使用 `scripts/audit_upstream_sources.py` 采样或按 SHA-256 校验后离线复核；
使用 `scripts/replay_upstream_entrypoints.py` 回放 legacy/adopted/distribution。
命令见 [脚本说明](../scripts/README.md#上游入口与贡献审计)。重新联网采样需新空缓存目录；
未来内容改变时数字可能不同。回放仅重新生成受影响文件及 Global，其他规则文件沿用
当前 checkout；合成路由分析没有模拟 DNS、ASN、进程或 SNI，不能替代完整发布审查。
