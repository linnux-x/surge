# Surge 规则仓库

聚合上游规则，生成 Surge 规则集和 Clash / mihomo 镜像，通过来源索引、规则校验、联网审计和 CI 发布。

[![CI](https://github.com/linnux-x/surge/actions/workflows/ci.yml/badge.svg)](https://github.com/linnux-x/surge/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 当前运行方式

- 26 个 Surge 规则集、41 个唯一上游 URL；具体来源由 [sources.py](scripts/sources.py) 统一定义。
- 维护者本机 Codex 每日北京时间 **05:00** 执行更新，保留 Agent 审查。任务依赖本机与 Codex 可用，调度不在 GitHub Actions。
- 更新经分支和 PR 发布，精确提交的 CI 通过后合并 `main`。GitHub Actions 提供手动全量生成和已审阅产物发布。
- Python 脚本无需第三方 Python 包；本地完整流程需要 **Python 3.10+、curl、Git**，向 GitHub 发布还需已认证的 **GitHub CLI**。
- 当前规则数、来源归属和 Clash 兼容性见 [生成收据](scripts/generation_receipt.md)，最新增删见 [差异报告](scripts/diff_report.md)。

## 使用规则

在已有 Surge 配置的 `[Rule]` 段添加规则；`PROXY` 请替换为你已有的代理策略名：

```ini
RULE-SET,https://raw.githubusercontent.com/linnux-x/surge/main/Rule/AI.list,PROXY
RULE-SET,https://raw.githubusercontent.com/linnux-x/surge/main/Rule/China.list,DIRECT
```

规则按 first-match 顺序匹配。完整加载顺序以 [Conf/Linnux.conf](Conf/Linnux.conf) 为准：
微信、测速、Apple AI、AI 等专用服务在前，Global、China、LAN、China IP 和 FINAL 在后。
其中 `Speedtest_China` 先于 `Speedtest`，`Apple_CN` 先于 `Apple`，下载和游戏先于宽泛 Microsoft 规则。

### 使用完整配置示例

1. 导入下方地址，在 Surge 中复制为普通配置，解除整份配置的托管更新。
2. 在副本的 `[Proxy Group]` 中，将 `✈️ 我的节点` 的 `policy-path=你的订阅地址` 改为自己的订阅。
3. 远程 `RULE-SET` 继续独立更新；副本中的整份配置与策略组由你维护。

```text
https://raw.githubusercontent.com/linnux-x/surge/main/Conf/Linnux.conf
```

托管配置不能直接本地编辑，见 [Surge 配置说明](https://manual.nssurge.com/profile/format.html)。
示例使用 `extended-matching` 等功能，导入时应按客户端提示检查兼容性；本仓库的模拟测试不等于所有客户端版本的实机验证。
首次导入需能访问 GitHub Raw。托管头使用 `interval=86400`，未开启 strict，更新失败时客户端可继续使用旧配置。
真实订阅、节点凭据和设备配置不在本仓库，边界见 [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md)。

### Clash / mihomo

使用 [clash/](clash/) 下的 YAML rule-provider，普通文件采用 `behavior: classical`。
Surge 专属类型会按转换器规则排除；扩展规则类型及数量见生成收据，需按客户端支持情况使用。
`China_Domain.yaml` 与 `China_Extra.yaml` 是配套拆分输出，前者用于 domain provider，后者承接剩余 classical 规则，二者需要配合使用。

`Rule/*.list`、`clash/*.yaml` 和 `Conf/Linnux.conf` 的公开路径是下游契约，不随内部整理迁移。

## 规则列表

| 规则文件 | 上游来源 | 说明 |
|---------|---------|------|
| 📱 AI.list | 3 源 · 手动 | AI 服务与模型 API |
| 🍎 Apple.list | blackmatrix7 | Apple 全系服务 |
| 🍎 Apple_AI.list | 2 源 · 手动 | Apple Intelligence、Siri 与 Private Relay |
| 🍎 Apple_CN.list | 2 源 | Apple 中国区 CDN 直连 |
| 📦 CDN.list | SukkaW | CDN、静态资源、下载资源 |
| 🏠 China.list | 3 源 | 中国大陆直连域名（domain-only） |
| 🌐 China_IP.list | 3 源 | 中国大陆 IP 回退（不加 no-resolve） |
| 📺 ChinaMedia.list | blackmatrix7 | 中国媒体服务 |
| 🏰 Disney.list | blackmatrix7 | Disney+ |
| ⬇️ Download.list | 2 源 | 下载、软件更新、游戏 CDN |
| 🎮 Game.list | blackmatrix7 | 游戏平台与服务 |
| 🌍 Global.list | blackmatrix7 | 通用海外/代理域名 |
| 🎬 GlobalMedia.list | blackmatrix7 | 国际流媒体服务 |
| 🔍 Google.list | blackmatrix7 | Google 服务（不含 YouTube） |
| 🪟 Microsoft.list | blackmatrix7 | Microsoft 服务（不含 GitHub） |
| 🪟 Microsoft_CDN.list | SukkaW | MS CDN 直连 |
| 🎥 Netflix.list | blackmatrix7 | Netflix |
| 💰 PayPal.list | blackmatrix7 | PayPal |
| 💬 SocialMedia.list | 4 源 | 社交媒体聚合（海外平台） |
| ⚡ Speedtest_China.list | Sukka 官方服务器数据 · spiritLHLS | 按明确大陆地区字段筛选测速主机并直连 |
| ⚡ Speedtest.list | SukkaW · 官方服务器数据 · 手动 | 国际测速节点与测速服务 · fast.com 仅此文件 |
| 🎧 Spotify.list | blackmatrix7 | Spotify 音乐服务 |
| ✈️ Telegram.list | 3 源 | 域名、CIDR、ASN |
| 🎵 TikTok.list | blackmatrix7 | TikTok |
| 💚 WeChat.list | blackmatrix7 | 微信相关服务 |
| ▶️ YouTube.list | blackmatrix7 | YouTube 与 YouTube Music |

## 测速来源与覆盖

- `Speedtest.list`：Sukka 的服务域名列表、官方测速服务器数据中的境外主机，以及本地 fast.com / nperf.com 规则。
- `Speedtest_China.list`：同一 Sukka 数据中 `cc=CN` 且 `country=China` 的主机，再由 spiritLHLS 的大陆省份 CSV 补充。
- Sukka 官方 JSON 一次下载、分别生成两份列表；JSON 更新会触发两份规则和 Global 重建，CSV 更新会触发大陆规则和 Global 重建。
- Kelee 两个入口与专用快照已移除。国际覆盖小于原快照，未覆盖的节点由后续规则匹配；不能把替代来源视为全球测速节点全集。

Sukka 数据有每日构建；spiritLHLS 仓库每日同步不代表 CSV 每日变化，其文件在本次接入审查时最近变更于 2026-06-03。
来源与日期证据见 [测速替换审计](audits/speedtest-replacement-2026-09-08.md)。规则数量随更新变化，以生成收据为准。
地区分类依赖上游标签，不凭域名后缀推测，也不将香港、澳门、台湾记录归入大陆直连。

## 更新与发布

### 每日更新

```text
上游检查 → 受影响规则重建 → manifest / diff / receipt → Clash 镜像
→ 不变量与路由校验 → 联网审计 → Agent 审查 → PR → exact-SHA CI → 合并 main
```

有可比较的 ETag / Last-Modified 时据此判断变化；缺少可比较指纹时保守重建。
上游失败或格式异常不会使用空结果替换规则。长期追加与排除写在 `Rule/Manual/`，不把旧生成文件当作新增规则来源。

### 手动全量审阅

在 GitHub Actions 选择 `Auto-Surge-Rules`，设置 `dry_run=true`；或使用：

```bash
gh workflow run auto-rules.yml --repo linnux-x/surge --ref main -f dry_run=true
```

此运行生成全部规则、同步 DNS Mapping 模块，并上传完整 `reviewed-release` 快照，不提交规则。
审查生成结果、manifest 差异和联网审计后，发布运行必须提供：

- `dry_run=false`
- `manual_audit_confirmed=true`
- `reviewed_run_id`：刚审查过的成功 dry-run ID

发布恢复该次审阅的确切文件，不再重新下载上游。仓库、运行 ID、基础提交和内容哈希必须匹配；
主线已变化或产物失效时重新生成并审阅。完整操作见 [CONTRIBUTING.md](CONTRIBUTING.md)。
Fork 用户先按贡献指南修改仓库限制及自己的调度方式，不要直接对本仓库发起更新。

## 本地验证

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/test_routing_order.py
python3 scripts/validate_surge_repo.py
python3 scripts/generate_clash_rules.py --check --validate
python3 scripts/generate_receipt.py
git diff --exit-code -- scripts/generation_receipt.json scripts/generation_receipt.md
```

生成规则后、提交前还必须运行联网审计：

```bash
python3 scripts/audit_rules.py
```

ERROR 阻断流程，WARN 不直接改变脚本退出码但需要审阅，INFO 记录供复核。
路由测试同时断言规则文件与目标策略；不模拟 DNS、ASN、进程或 SNI/HTTP Host，也不证明测速服务器在线。

## 自定义与维护

| 入口 | 职责 |
|---|---|
| [Rule/Manual/README.md](Rule/Manual/README.md) | 追加规则、整行精确匹配排除、公开 override 合同 |
| [scripts/README.md](scripts/README.md) | 生成脚本、来源审计、测速格式转换和发布快照 |
| [tests/README.md](tests/README.md) | 路由测试及预期策略 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | PR、全量审阅与 Fork 适配 |
| [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md) | 公私边界与下游 URL 契约 |
| [audits/](audits/) | 标注日期和基线的审计记录，历史记录不代表当前状态 |

## 上游与致谢

| 来源 | 项目 |
|---|---|
| blackmatrix7 | [ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) |
| Loyalsoldier | [surge-rules](https://github.com/Loyalsoldier/surge-rules) |
| SukkaW / SukkaLab | [Surge](https://github.com/SukkaW/Surge)、[测速服务器采集](https://github.com/SukkaW/speedtest-net-servers)、[官方数据分发](https://github.com/SukkaLab/speedtest-net-servers-dist) |
| Rabbit-Spec | [Surge](https://github.com/Rabbit-Spec/Surge)，同时参考其工作流设计 |
| ConnersHua | [RuleGo](https://github.com/ConnersHua/RuleGo) |
| RocM301 | [Apple-Rule](https://github.com/RocM301/Apple-Rule) |
| spiritLHLS | [speedtest.cn-CN-ID](https://github.com/spiritLHLS/speedtest.cn-CN-ID) |
| Telegram | [官方 CIDR](https://core.telegram.org/resources/cidr.txt) |

本仓库代码许可证见 [LICENSE](LICENSE)；引用的上游内容仍应遵守各来源声明。

架构、数据流、重构优先级和行为保持测试见 [架构说明](ARCHITECTURE.md)。
