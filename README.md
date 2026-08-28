# Surge 自用规则仓库 — 全自动、可审计的 Surge 分流规则

> **一句总结：** 多上游源每日同步、自动清洗校验、清单追踪变更、联网审计质量 — 让你只需关心策略，不用操心底层规则。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.10+-green.svg?logo=python&logoColor=white)](https://www.python.org/) [![Surge](https://img.shields.io/badge/Surge-Rule%20Set-orange.svg)](https://manual.nssurge.com/) [![No Dependencies](https://img.shields.io/badge/deps-stdlib%20only-brightgreen.svg)]()

---

## 📌 项目速览

- 🎯 **目标用户**：Surge 用户（iPhone / MacBook），需要精细化代理分流与规则管理
- 💡 **核心价值**：多上游源自动聚合 → 清洗校验 → 清单追踪 → 联网审计，全链路自动化
- 📜 **许可证**：MIT
- 🔄 **更新频率**：维护者本机的 Hermes agent 每日北京时间 05:00 自动同步
- 🧪 **质量保障**：每次更新须通过 5 项联网审查 + 15+ 项不变量校验
- 📦 **零依赖**：所有脚本仅使用 Python 3.10+ 标准库，无需 pip install

```bash
# 快速使用：在 Surge 配置中加载规则
RULE-SET,https://raw.githubusercontent.com/linnux-x/surge/main/Rule/AI.list,PROXY
RULE-SET,https://raw.githubusercontent.com/linnux-x/surge/main/Rule/China.list,DIRECT
```

---

## ❓ 为什么需要这个仓库？

手动维护 Surge 规则面临多种痛点：

| 痛点 | 解决方式 |
|------|----------|
| 🔄 上游规则频繁更新 | 本地 agent **每日自动同步** 6+ 上游源（跑同一套流水线脚本） |
| 🧹 规则污染 / 残留 | 每次重新生成，不保留旧文件作为 baseline |
| 📊 变更不可追溯 | **清单索引系统**：每条规则有 12 字符稳定哈希 + 来源标注 |
| ⚠️ 共享基础设施混入 | 自动检测并排除 cookielaw / sentry / newrelic 等第三方平台 |
| 🧪 质量无保障 | **联网审查流水线**：5 项检查（可达性 / 比例 / 共享设施 / Surge 文档 / exclude 覆盖） |
| ✏️ 手动规则管理 | `Rule/Manual/` 支持追加 + 排除，优先级最高 |

---

## ✅ 核心特性

| 特性 | 说明 |
|------|------|
| 🤖 **全自动同步** | 检查 39 个上游源的 Last-Modified / ETag，只同步有变更的规则集，无变化跳过提交 |
| 🧪 **自动校验** | 15+ 不变量检查：规则类型合法性、无策略名渗入、无重复、domain-only 约束、no-resolve 策略等 |
| 📋 **清单索引** | 每条规则拥有 12 字符稳定内容哈希 ID + 上游来源标注，支持跨版本追踪 |
| 📊 **增量差异报告** | 每次变更生成 manifest diff（markdown + JSON），明确增减来源 |
| 🔍 **联网审查** | 5 项审计检查，ERROR 阻断提交、WARN 需确认、INFO 仅记录 |
| 🧹 **自动清洗** | 排除共享 CDN / 遥测 / 分析平台，检测不透明子域名 |

---

## 📁 目录结构

> 文档职责：`README.md` 只做公开入口；公开/私有边界以 `SOURCE_OF_TRUTH.md` 为准；脚本细节以 `scripts/README.md` 为准；贡献流程以 `CONTRIBUTING.md` 为准；手工规则格式以 `Rule/Manual/README.md` 为准。

| 路径 | 说明 |
|------|------|
| `Conf/Linnux.conf` | 主 Surge 配置示例，包含策略组和 `RULE-SET` 加载顺序 |
| `Rule/*.list` | Surge 外部规则集文件（自动生成，**勿手动修改**） |
| `clash/*.yaml` | Clash / mihomo rule-provider 文件（由 `Rule/*.list` 转换生成）；**有私有下游消费者，Raw URL 不可变更**，见 `SOURCE_OF_TRUTH.md` |
| `Rule/Manual/*.txt` / `*.exclude.txt` | 手动追加（最高优先级）与排除规则 |
| `Rule/.manifests/*.manifest` | 规则清单索引（每行：稳定哈希ID + 来源标注） |
| `Module/*.sgmodule` | Surge 模块文件 |
| `scripts/` | 规则生成、校验、审计和 Clash 镜像脚本；脚本顺序见 `scripts/README.md` |
| `tests/expected-routing.csv` | 路由测试预期（域名 → 期望规则集） |
| `.github/workflows/auto-rules.yml` | 规则同步 + DNS Mapping 模块同步流水线 |
| `CONTRIBUTING.md` | 贡献指南 |

---

## 📋 规则列表

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
| ⚡ Speedtest_China.list | Kelee 每日主上游 · 已审查快照兜底 | 中国大陆测速节点直连，优先于国际测速规则 |
| ⚡ Speedtest.list | SukkaW · Kelee 每日主上游 · 已审查快照兜底 · 手动 | 国际测速节点与测速服务 · fast.com 仅此文件 |
| 🎧 Spotify.list | blackmatrix7 | Spotify 音乐服务 |
| ✈️ Telegram.list | 3 源 | 域名、CIDR、ASN |
| 🎵 TikTok.list | blackmatrix7 | TikTok |
| 💚 WeChat.list | blackmatrix7 | 微信相关服务 |
| ▶️ YouTube.list | blackmatrix7 | YouTube 与 YouTube Music |

---

## 🔄 主配置加载顺序

`Conf/Linnux.conf` 中的规则遵循 Surge **first-match** 逻辑，重点服务规则放在宽泛规则之前：

1. 💚 **WeChat** → 微信直连优先
2. ⚡ **Speedtest_China → Speedtest** → 中国大陆测速服务器直连；国际测速流量进入可选测速策略
3. 🍎 **Apple_AI** → Apple Intelligence、Siri 与 Private Relay 优先代理
4. 📱 **AI** → 通用 AI 服务专用路由
5. 🍎 **Apple_CN → Apple** → 中国区 CDN 先直连，再处理 Apple 通用服务
6. 🪟 **Microsoft_CDN** → Windows、Office 与 Visual Studio CDN 直连
7. ⬇️ **Download** → 下载与软件更新先于宽泛 Microsoft 规则
8. 🎮 **Game** → Xbox、Minecraft 等游戏流量先于宽泛 Microsoft 规则
9. 🪟 **Microsoft** → Microsoft / Office 通用服务
10. ✈️ **Telegram** → Telegram 专用路由
11. ▶️ **YouTube** → 先于 Google 通用规则
12. 🎵 **TikTok** → TikTok 路由
13. 💬 **SocialMedia** → 社交媒体
14. 💰 **PayPal** → 支付服务
15. 🔍 **Google** → Google 通用服务
16. 🎬 **Netflix → Disney → ChinaMedia → Spotify → GlobalMedia** → 专用媒体优先于宽泛媒体
17. 📦 **CDN** → 共享 CDN 后台回退
18. 🌍 **Global** → 通用代理回退
19. 🏠 **China** → 中国大陆直连域名
20. 🏢 **LAN** → 局域网直连
21. 🌐 **China IP** → 中国大陆 IP 回退
22. 🔚 **FINAL** → 最终代理

---

## 🤖 自动化流水线

### 触发方式

| 方式 | 说明 |
|------|------|
| 🤖 **每日同步** | 维护者本机的 Hermes agent 每日北京时间 05:00 运行同一套流水线脚本并推送；调度在 Hermes 内部，不是 Actions 计划任务，详见 `SOURCE_OF_TRUTH.md` |
| 🖐 **手动触发** | GitHub Actions 页面点击 Run workflow（全量重新生成 + 发布门禁） |
| ⌨️ **CLI 触发** | `gh workflow run auto-rules.yml` |

### 完整流程

```text
上游检查 → 规则生成 → manifest/diff → generation receipt → Clash 镜像 → 不变量/路由校验 → 联网审计 → DNS Mapping → 提交 → exact-SHA CI
```

脚本顺序和单一事实来源见 `scripts/README.md`；full generation 发布门禁见 `CONTRIBUTING.md`。

### 清单索引系统

每条规则在 `Rule/.manifests/*.manifest` 中拥有 **12 字符稳定内容哈希 ID + 来源标注**，用于跨版本追踪、归属迁移识别和 `diff_report.md` / `diff_report.json` 增量报告。

---

## 🛡️ 校验 & 审计

提交前至少运行：
```bash
python3 scripts/validate_surge_repo.py
python3 scripts/test_routing_order.py   # 路由顺序模拟测试
```

生成规则后、提交 GitHub 前执行：
```bash
python3 scripts/audit_rules.py
```

校验覆盖规则类型、策略名渗入、`# TOTAL`、China/China_IP 约束、GitHub/Microsoft 边界、fast.com 唯一归属、共享基础设施、PayPal CN、不透明子域名、README/workflow/规则文件一致性等；联网审计覆盖上游可达性、规则数比例、共享基础设施、Surge 文档更新和 exclude 覆盖率。详细脚本职责见 `scripts/README.md`。

> 🔴 **ERROR** → workflow 失败，必须修复  
> 🟡 **WARN** → workflow 继续，但需人工确认  
> 🔵 **INFO** → 仅供参考，无需处理

---

## 🔑 关键策略

| 策略 | 说明 |
|------|------|
| 🐙 **GitHub** | 不归入 Microsoft。普通服务走 Global，Copilot 走 AI，下载资源走 CDN |
| ⚡ **fast.com** | 仅 Speedtest.list，其他地方不重复 |
| 🏠 **China.list** | 仅中国大陆直连域名，不放 IP |
| 🌐 **China_IP.list** | 不加 no-resolve，用于 IP 分类回落 |
| 🔒 **IP 规则** | 其他 IP 默认加 no-resolve |
| 🔄 **无 baseline** | 不保留旧 Rule/*.list；长期规则进 Rule/Manual/ |
| 🏗️ **共享基础设施** | CDN / 遥测 / 分析等共享平台不作为服务规则合并 |
| 🔍 **子域名策略** | 服务专属子域名可保留，不透明子域名应排除 |

---

## 🚀 快速上手

> **最低版本要求**：Surge iOS 5.8.1+ / Surge Mac 5.x 对应版本。配置使用了 `extended-matching`（5.8.0 引入）；5.8.1 起 RULE-SET 在资源更新时自动预处理并索引，大规则集（如 China.list 11 万条）匹配为毫秒级，与 DOMAIN-SET 无性能差异。
>
> **首次导入提示**：托管配置与全部规则集均从 `raw.githubusercontent.com` 拉取，请在代理可用的网络环境下完成首次导入；导入后 Surge 会缓存规则集，且托管配置为非 strict 模式，更新失败时继续使用旧配置。

### 新手三步骤

1. **导入托管配置** → 使用 `Conf/Linnux.conf`，首行已包含 Surge `#!MANAGED-CONFIG`，默认每日检查更新
2. **添加自己的订阅** → 将 `[Proxy Group]` 中 `✈️ 我的节点` 的 `policy-path=你的订阅地址` 改为自己的订阅地址
3. **保持规则更新** → 本仓库规则每日由维护者的 agent 流水线自动更新，托管配置引用的 `Rule/*.list` 无需你做任何操作

托管配置地址：

```text
https://raw.githubusercontent.com/linnux-x/surge/main/Conf/Linnux.conf
```

`Conf/Linnux.conf` 首行固定为：

```text
#!MANAGED-CONFIG https://raw.githubusercontent.com/linnux-x/surge/main/Conf/Linnux.conf interval=86400
```

`strict` 保持 Surge 默认值 `false`：远端更新失败时，客户端可以继续使用旧配置。

### 手动更新

```bash
# Fork 后手动触发同步
gh workflow run auto-rules.yml --repo linnux-x/surge
```

### 自定义规则

在 `Rule/Manual/` 目录下放置：
- `<名称>.txt` → 手动追加规则，放在对应规则文件顶部，优先级最高
- `<名称>.exclude.txt` → 排除规则，按生成后规则整行精确匹配（大小写敏感，非正则；需与上游格式完全一致）

> ⚠️ **注意**：长期需要保留/排除的规则必须放入 `Rule/Manual/` 对应文件。不要依赖旧生成文件作为隐式 baseline。

### 适合谁

**适合：** Surge 用户需要一个自动更新、有校验、有审计的规则仓库，不想手动维护上游变更。

**不适合：** 只需要几条静态规则的用户；使用非 Surge 客户端的用户（规则格式为 Surge 专用）。

想 Fork 本仓库自建规则源，见 [`CONTRIBUTING.md` 的 Fork 后适配](CONTRIBUTING.md#fork-后适配)。

---

## 📝 规则维护要求

- 修改规则或同步逻辑前，先读 `CONTRIBUTING.md`。
- 查看脚本流水线和单一事实来源，读 `scripts/README.md`。
- 添加或排除手工规则，读 `Rule/Manual/README.md`。
- 公开仓库与真实设备/私有配置的边界，以 `SOURCE_OF_TRUTH.md` 为准。

> 📖 完整的用户偏好、分类经验和设备配置属于私有配置，不在本仓库中。

---

## 🙏 致谢

上游规则与参考来源：

| 来源 | 链接 |
|------|------|
| blackmatrix7 | [ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) |
| Loyalsoldier | [surge-rules](https://github.com/Loyalsoldier/surge-rules) |
| SukkaW | [Surge](https://github.com/SukkaW/Surge) |
| ConnersHua | [RuleGo](https://github.com/ConnersHua/RuleGo) |

> 工作流借鉴 [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge) 的思路，并加入了本仓库自己的分类策略、校验规则和联网审查流水线。

---

<p align="center">
  <sub>Made with ❤️ for Surge users | MIT License</sub>
</p>
