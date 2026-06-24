# Linnux Surge 自用规则仓库 — 全自动、可审计的 Surge 分流规则

> **一句总结：** 多上游源每日同步、自动清洗校验、清单追踪变更、联网审计质量 — 让你只需关心策略，不用操心底层规则。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.10+-green.svg?logo=python&logoColor=white)](https://www.python.org/) [![Surge](https://img.shields.io/badge/Surge-Rule%20Set-orange.svg)](https://manual.nssurge.com/)

---

## 📌 项目速览

- 🎯 **目标用户**：Surge 用户（iPhone / MacBook），需要精细化代理分流与规则管理
- 💡 **核心价值**：多上游源自动聚合 → 清洗校验 → 清单追踪 → 联网审计，全链路自动化
- 📜 **许可证**：MIT
- 🔄 **更新频率**：每日北京时间 05:00 自动同步
- 🧪 **质量保障**：每次更新须通过 5 项联网审查 + 15+ 项不变量校验

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
| 🔄 上游规则频繁更新 | GitHub Actions **每日自动同步** 6+ 上游源 |
| 🧹 规则污染 / 残留 | 每次重新生成，不保留旧文件作为 baseline |
| 📊 变更不可追溯 | **清单索引系统**：每条规则有 12 字符稳定哈希 + 来源标注 |
| ⚠️ 共享基础设施混入 | 自动检测并排除 cookielaw / sentry / newrelic 等第三方平台 |
| 🧪 质量无保障 | **联网审查流水线**：5 项检查（可达性 / 比例 / 共享设施 / Surge 文档 / exclude 覆盖） |
| ✏️ 手动规则管理 | `Rule/Manual/` 支持追加 + 排除，优先级最高 |

---

## ✅ 核心特性

| 特性 | 说明 |
|------|------|
| 🤖 **全自动同步** | 检查 38 个上游源的 Last-Modified / ETag，只同步有变更的规则集，无变化跳过提交 |
| 🧪 **自动校验** | 15+ 不变量检查：规则类型合法性、无策略名渗入、无重复、domain-only 约束、no-resolve 策略等 |
| 📋 **清单索引** | 每条规则拥有 12 字符稳定内容哈希 ID + 上游来源标注，支持跨版本追踪 |
| 📊 **增量差异报告** | 每次变更生成 manifest diff（markdown + JSON），明确增减来源 |
| 🔍 **联网审查** | 5 项审计检查，ERROR 阻断提交、WARN 需确认、INFO 仅记录 |
| 🧹 **自动清洗** | 排除共享 CDN / 遥测 / 分析平台，检测不透明子域名 |

---

## 📁 目录结构

| 路径 | 说明 |
|------|------|
| `Conf/LINNUX.conf` | 主 Surge 配置示例，包含策略组和 `RULE-SET` 加载顺序 |
| `Rule/*.list` | Surge 外部规则集文件（自动生成，**勿手动修改**） |
| `Rule/Manual/*.txt` / `*.exclude.txt` | 手动追加（最高优先级）与排除规则 |
| `Rule/.manifests/*.manifest` | 规则清单索引（每行：稳定哈希ID + 来源标注） |
| `Module/*.sgmodule` | Surge 模块文件 |
| `scripts/sources.py` | 上游源配置（单一定义，所有脚本引用） |
| `scripts/check_upstream_updates.py` | 并行 HEAD 检查上游变更（8 线程） |
| `scripts/generate_rules.py` | 规则生成引擎（下载、合并、清洗、校验） |
| `scripts/manifest.py` | 规则清单生成器（稳定哈希ID + 来源追踪） |
| `scripts/diff_manifests.py` | 清单差异对比（本次 vs git HEAD） |
| `scripts/validate_surge_repo.py` | 不变量检查（15+ 项） |
| `scripts/audit_rules.py` | 联网审查（5 项审计） |
| `scripts/prune_cidr.py` | CIDR 去重裁剪 |
| `.github/workflows/auto-rules.yml` | 规则同步 + DNS Mapping 模块同步流水线 |
| `AGENT.md` | 项目指令文档（用户偏好、分类策略、验证标准 — **所有 agent 必读**） |

---

## 📋 规则列表

| 规则文件 | 上游来源 | 说明 |
|---------|---------|------|
| 📱 AI.list | SukkaW · ConnersHua | AI 服务与模型 API |
| 🍎 Apple.list | blackmatrix7 | Apple 全系服务 |
| 🍎 Apple_CN.list | SukkaW | Apple 中国区 CDN 直连 |
| 📦 CDN.list | SukkaW | CDN、静态资源、下载资源 |
| 🏠 China.list | SukkaW · blackmatrix7 | 中国大陆直连域名（domain-only） |
| 🌐 China_IP.list | Loyalsoldier · blackmatrix7 | 中国大陆 IP 回退（不加 no-resolve） |
| 📺 ChinaMedia.list | blackmatrix7 | 中国媒体服务 |
| 🏰 Disney.list | blackmatrix7 | Disney+ |
| ⬇️ Download.list | SukkaW | 下载、软件更新、游戏 CDN |
| 🎮 Game.list | blackmatrix7 | 游戏平台与服务 |
| 🌍 Global.list | blackmatrix7 | 通用海外/代理域名 |
| 🎬 GlobalMedia.list | blackmatrix7 | 国际流媒体服务 |
| 🔍 Google.list | blackmatrix7 | Google 服务（不含 YouTube） |
| 🪟 Microsoft.list | blackmatrix7 | Microsoft 服务（不含 GitHub） |
| 🪟 Microsoft_CDN.list | SukkaW | MS CDN 直连 |
| 🎥 Netflix.list | blackmatrix7 | Netflix |
| 💰 PayPal.list | blackmatrix7 | PayPal |
| 💬 SocialMedia.list | QuixoticHeart · blackmatrix7 | 社交媒体聚合（海外平台） |
| ⚡ Speedtest.list | SukkaW · 手动 | 测速 · fast.com 仅此文件 |
| ✈️ Telegram.list | blackmatrix7 · Telegram 官方 | 域名、CIDR、ASN |
| 🎵 TikTok.list | blackmatrix7 | TikTok |
| 💚 WeChat.list | blackmatrix7 | 微信相关服务 |
| ▶️ YouTube.list | blackmatrix7 | YouTube 与 YouTube Music |

---

## 🔄 主配置加载顺序

`Conf/LINNUX.conf` 中的规则遵循 Surge **first-match** 逻辑，重点服务规则放在宽泛规则之前：

1. 💚 **WeChat** → 微信直连优先
2. ⚡ **Speedtest** → 测速不走代理
3. 📱 **AI** → AI 服务专用路由
4. 🍎 **Apple** → Apple 原生服务
5. 🪟 **Microsoft** → Microsoft / Office 服务
6. ✈️ **Telegram** → 协议规避混淆
7. ⬇️ **Download** → 下载 CDN 直连
8. 🎮 **Game** → 游戏平台直连/代理
9. ▶️ **YouTube** → 流媒体路由
10. 🎵 **TikTok** → TikTok 路由
11. 💬 **SocialMedia** → 社交媒体
12. 💰 **PayPal** → 支付服务
13. 🔍 **Google** → Google 服务
14. 🎬 **GlobalMedia + ChinaMedia** → 国际与中国媒体服务
15. 📦 **CDN** → 共享 CDN 后台回退
16. 🌍 **Global** → 通用代理回退
17. 🏠 **China** → 中国大陆直连域名
18. 🏢 **LAN** → 局域网直连
19. 🌐 **China IP** → 中国大陆 IP 回退
20. 🔚 **FINAL** → 最终代理

---

## 🤖 自动化流水线

### 触发方式

| 方式 | 说明 |
|------|------|
| ⏰ **定时触发** | 每天北京时间 05:00 自动同步 |
| 🖐 **手动触发** | GitHub Actions 页面点击 Run workflow |
| ⌨️ **CLI 触发** | `gh workflow run auto-rules.yml` |

### 完整流程

```
触发 workflow
  ↓
1. 增量上游检查 → 拉取变更源 → 合并手动规则 → 应用排除 → 清洗校验
  ↓
2. 生成紧凑清单（稳定内容哈希ID + 来源标注）          ← scripts/manifest.py
  ↓
3. 对比 git HEAD 生成增量差异报告                       ← scripts/diff_manifests.py
  ↓
4. 验证仓库不变量（15+ 检查项）                         ← scripts/validate_surge_repo.py
  ↓
5. 联网审查（5 项审计检查）                            ← scripts/audit_rules.py
   ├─ 上游可达性
   ├─ 规则数比例对比
   ├─ 共享第三方基础设施扫描
   ├─ Surge 文档更新检查
   └─ exclude 排除覆盖率
  ↓
6. 同步 DNS Mapping 模块
  ↓
7. 提交到 GitHub（规则 + 清单 + 差异报告 + 模块）
```

> 流程中的 **增量上游检查**、**Generate Rule Manifests**、**Online Audit** 和 **Sync DNS Mapping** 步骤由本仓库新增，确保每次变更有据可查、可审计。

### 清单索引系统

每条规则在 `Rule/.manifests/*.manifest` 中拥有一个 **12 字符的稳定内容哈希 ID**，并标注其上游来源。

数据格式（每行一个规则）：
```
<12字符哈希ID>	<来源名称>
```

| 好处 | 说明 |
|------|------|
| 🔄 **跨版本追踪** | 每条规则的增减变化可精确追踪 |
| 🔗 **归属转移** | 识别规则在来源间的迁移（如从 China 移入 Global） |
| 📊 **增量报告** | 自动生成 `diff_report.md` + `diff_report.json` |
| 📈 **量化审计** | 上游规则变动数量、方向有据可查 |

---

## 🛡️ 校验 & 审计

### 规则校验

提交前运行：
```bash
python3 scripts/validate_surge_repo.py
```

| 检查项 | 级别 |
|--------|:--:|
| Surge 规则类型合法性 | 🔴 |
| 无策略名渗入规则文件 | 🔴 |
| 无重复规则 | 🟡 |
| `# TOTAL` 头与实际计数一致 | 🔴 |
| `China.list` domain-only | 🔴 |
| `China_IP.list` 无 `no-resolve` | 🔴 |
| 其他 IP 规则带 `no-resolve` | 🟡 |
| `Microsoft.list` 无 GitHub 家族 | 🔴 |
| `fast.com` 仅出现在 `Speedtest.list` | 🔴 |
| README、workflow 与 `.list` 文件一致性 | 🟡 |
| 无旧 baseline 区块和 SukkaW marker 域名 | 🟡 |
| **共享第三方基础设施**检测 | 🟡 |
| **PayPal CN 域名**检测（.cn 不在 PayPal.list） | 🟡 |
| **不透明子域名**检测（纯数字/十六进制前缀如 `o207216.ingest.sentry.io`） | 🟡 |

### 联网审查

每次 workflow 生成规则后、提交 GitHub 前执行 `scripts/audit_rules.py`：

| 检查项 | 说明 |
|--------|------|
| 🔗 **上游可达性** | 所有配置的 URL 可正常访问 |
| 📊 **规则数对比** | 生成 vs 上游比例异常时告警（多源合并文件豁免） |
| 🏗️ **共享基础设施** | 已知共享平台出现在服务规则中时告警 |
| 📖 **Surge 文档** | 检查是否有新的 Surge 规则类型发布 |
| 🧹 **exclude 覆盖率** | 所有在用的 exclude 文件仍有效 |

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

### 新手三步骤

1. **复制配置模板** → 将 `Conf/LINNUX.conf` 内容合并到自己的 Surge 配置
2. **添加规则集引用** → 在 `[Rule]` 段按加载顺序引用 `Rule/*.list`
3. **启用自动更新** → Fork 仓库，GitHub Actions 自动生效

### 手动更新

```bash
# Fork 后手动触发同步
gh workflow run auto-rules.yml --repo linnux-x/surge
```

### 自定义规则

在 `Rule/Manual/` 目录下放置：
- `<名称>.txt` → 手动追加规则，放在对应规则文件顶部，优先级最高
- `<名称>.exclude.txt` → 排除规则，使用 `grep -vFf`（固定字符串匹配，非正则）

> ⚠️ **注意**：长期需要保留/排除的规则必须放入 `Rule/Manual/` 对应文件。不要依赖旧生成文件作为隐式 baseline。

### 适合谁 / 如何 Fork

**适合：** Surge 用户需要一个自动更新、有校验、有审计的规则仓库，不想手动维护上游变更。

**不适合：** 只需要几条静态规则的用户；使用非 Surge 客户端的用户（规则格式为 Surge 专用）。

**Fork 后三步适配：**

1. 修改 `.github/workflows/auto-rules.yml` 中的 `REPO_URL` 和 `AUTHOR_NAME` 环境变量为你的仓库
2. 在仓库 Settings → Actions → General → Workflow permissions 中选择「Read and write permissions」
3. 按需在 `Rule/Manual/` 中添加自己的追加和排除规则

**保持同步上游：** `git remote add upstream https://github.com/linnux-x/surge.git` 后定期 `git fetch upstream && git merge upstream/main`

---

## 📝 规则维护要求

修改规则或同步逻辑前，请优先阅读 `AGENT.md`。该文件包含完整的用户偏好、分类策略、验证标准和工作流程。

> 📖 项目完整维护约定详见 `AGENT.md` — 所有 agent 和贡献者必读。

---

## 🙏 致谢

上游规则与参考来源：

| 来源 | 链接 |
|------|------|
| blackmatrix7 | [ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) |
| Loyalsoldier | [surge-rules](https://github.com/Loyalsoldier/surge-rules) |
| SukkaW | [Surge](https://github.com/SukkaW/Surge) |
| Rabbit-Spec | [Surge](https://github.com/Rabbit-Spec/Surge) |
| QuixoticHeart | [rule-set](https://github.com/QuixoticHeart/rule-set) |
| ConnersHua | [RuleGo](https://github.com/ConnersHua/RuleGo) |

> 工作流基于 [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge) 的思路改编，并加入了本仓库自己的分类策略、校验规则和联网审查流水线。

---

<p align="center">
  <sub>Made with ❤️ for Surge users | MIT License</sub>
</p>
