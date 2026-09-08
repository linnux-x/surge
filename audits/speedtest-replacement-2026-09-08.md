# Speedtest 来源替换 · 2026-09-08

审计基线：`eacc958ec665c892d0e9d609940d6fc3b14f4ef2`。按维护者要求移除 Kelee 的两个上游，
并为原有两份测速规则接入持续更新来源。公开 Rule / Clash URL 和策略顺序不变。

## 采用来源

- [SukkaW/speedtest-net-servers](https://github.com/SukkaW/speedtest-net-servers)：官方构建流程将数据发布至
  [SukkaLab/speedtest-net-servers-dist](https://github.com/SukkaLab/speedtest-net-servers-dist)。使用官方 GitHub
  `master/servers.json`，与作者现有 Surge 构建的数据源一致。查询时近三次 schedule 均成功；数据提交
  `9d6fb9e39919aa400515253a1d48e21d97ff121c` 于 2026-09-07 18:00 UTC 更新，前一天也有内容更新。
- [spiritLHLS/speedtest.cn-CN-ID](https://github.com/spiritLHLS/speedtest.cn-CN-ID)：使用 CN.csv 补充大陆节点。
  仓库仍每日同步，但文件最近一次实质变更为 2026-06-03、提交 `4909e12062fdbb8c5892cb7bb8fc8950d792eb98`。
  因此将其作为补充源，不能将每日仓库活动称为每日节点内容变化。
- 保留原 SukkaW Speedtest 服务域名片段和本地 fast.com / nperf.com Manual。

Sukka 的结构化数据按 `cc=CN` 且 `country=China` 生成大陆主机，其他一致的地区标签生成国际主机。
标签矛盾的记录不猜测分类。CSV 只接纳 `country_code=CN`、大陆省份白名单及 `active=1` 的记录，
其他 active 值暂不接纳。只取精确主机/IP，不扩大为运营商后缀；香港、澳门、台湾不归入大陆直连。

对照项目 spiritLHLS/speedtest.net-CN-ID 的 CN.csv 存在 `country_code=CN` 但 `country=Taiwan`
的记录；本次不直接接入该文件。QuixoticHeart 等聚合规则缺少可用的逐服务器地区字段，未作为两地区分类依据。

## 变更与验证

| 文件 | 原规则数 | 新规则数 | 增加 | 删除 |
|---|---:|---:|---:|---:|
| Speedtest.list | 17177 | 1709 | 36 | 15504 |
| Speedtest_China.list | 9 | 53 | 45 | 1 |
| Global.list | 24328 | 24334 | 6 | 0 |

Global 依赖重建同时取得 blackmatrix7 当前上游的 6 条新增规则；完整条目、来源变更见
`scripts/diff_report.md` 及 manifest。国际覆盖显著小于 Kelee 旧快照，不能声称等量替换。
这次选用可核验更新和地理分类的数据；未被新列表覆盖的测速服务器继续按后续规则匹配。

移除两个 Kelee URL、专用快照及回退代码。一次生成只下载一次共享 JSON，保证两个地区视图
使用相同输入。上游失败、格式不符或选取结果为空会阻断发布；不会用空结果覆盖已发布规则。
现有 05:00 Codex 任务沿用 scripts/sources.py：JSON 变更同时触发两份测速规则及 Global，
CSV 变更触发大陆规则及 Global，保留 Agent 审查与 exact-SHA CI。

47 项单元测试、132 项路由测试、仓库不变量、Clash payload 校验和收据生成通过。
联网审计：41 个唯一上游，0 ERROR、0 WARN、6 INFO，不再使用 Kelee 回退。
两个原有大陆测试域名仍命中 Speedtest_China → DIRECT，新增境内与境外样例也按预期分流。
测试不模拟真实设备连接、服务器可用性或 DNS 解析；未来第三方节点变化仍须经同一审查流程。
