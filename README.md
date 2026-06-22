# Linnux Surge 自用规则仓库

这是一个面向 Surge 的自用规则仓库，用于在 iPhone、MacBook 等设备上进行代理分流、区域直连、媒体服务、AI 服务、CDN 与中国大陆 IP/域名分类。

仓库通过 GitHub Actions 定时同步多个上游规则源，合并本地手动规则，并应用仓库专属的规则清洗与校验策略。生成时不保留当前 `Rule/*.list` 作为 baseline，避免上游已删除或历史遗留规则长期滞留。

## 目录结构

| 路径 | 说明 |
|------|------|
| `Conf/LINNUX.conf` | 主 Surge 配置示例，包含策略组和 `RULE-SET` 加载顺序 |
| `Rule/*.list` | Surge 外部规则集文件（自动生成，勿手改） |
| `Rule/Manual/*.txt` | 手动追加规则，优先级最高 |
| `Rule/Manual/*.exclude.txt` | 排除规则，匹配到的上游行不会写入最终 ||
| `Rule/.manifests/*.manifest` | 规则清单索引（每行：稳定哈希ID + 来源标注） |
| `Module/*.sgmodule` | Surge 模块文件 |
| `scripts/manifest.py` | 规则清单生成器（基于内容哈希的稳定ID + 来源追踪） |
| `scripts/diff_manifests.py` | 清单差异对比器（本次 vs git HEAD 的增减变化） |
| `scripts/diff_report.md` | 差异报告（markdown） |
| `scripts/diff_report.json` | 差异报告（JSON） |
| `scripts/validate_surge_repo.py` | 仓库不变量检查器 |
| `scripts/audit_rules.py` | 联网审查脚本（上游可达、共享基础设施、Surge 文档等） |
| `.github/workflows/auto-rules.yml` | 规则同步 + DNS Mapping 模块同步 |
| `AGENT.md` | 项目指令文档（用户偏好、分类策略、验证标准——所有 agent 必读） |
| `.codex/skills/surge-ruleset-builder/` | Codex 规则维护 Skill 精简入口 |

## 规则列表

| 规则文件 | 主要上游来源 | 说明 |
|---------|-------------|------|
| `AI.list` | SukkaW、Rabbit-Spec | AI 服务、模型 API、Apple Intelligence、AIGC 等 |
| `Apple.list` | blackmatrix7 | Apple 全系服务 |
| `Apple_CN.list` | SukkaW | Apple 中国区与 Apple CDN 直连规则 |
| `CDN.list` | SukkaW | CDN、静态资源、部分专用下载资源 |
| `China.list` | SukkaW、blackmatrix7、Rabbit-Spec | 中国大陆直连域名规则；保持 domain-only |
| `China_IP.list` | Loyalsoldier、blackmatrix7、Rabbit-Spec | 中国大陆 IP 回退规则；特意不加 `no-resolve` |
| `ChinaMedia.list` | blackmatrix7 | 中国媒体服务 |
| `Disney.list` | blackmatrix7 | Disney+ |
| `Download.list` | SukkaW | 通用下载、软件更新、包管理、对象存储与游戏客户端下载 CDN |
| `Game.list` | blackmatrix7 | 游戏平台与游戏服务 |
| `Global.list` | blackmatrix7 | 通用海外/代理域名规则 |
| `GlobalMedia.list` | blackmatrix7 | 国际流媒体服务 |
| `Google.list` | blackmatrix7 | Google 服务，不包含 YouTube 专属规则 |
| `Microsoft.list` | blackmatrix7 | Microsoft 服务；不包含 GitHub 家族规则 |
| `Microsoft_CDN.list` | SukkaW | Microsoft CDN / 下载资源直连规则 |
| `Netflix.list` | blackmatrix7 | Netflix |
| `PayPal.list` | blackmatrix7 | PayPal |
| `SocialMedia.list` | QuixoticHeart、blackmatrix7 | 社交媒体聚合规则 |
| `Speedtest.list` | SukkaW、手动规则 | 测速服务；`fast.com` 仅保留在此文件 |
| `Telegram.list` | blackmatrix7、Telegram 官方 | Telegram 域名、CIDR、ASN 与客户端 fallback |
| `TikTok.list` | blackmatrix7 | TikTok |
| `WeChat.list` | blackmatrix7 | 微信相关服务 |
| `YouTube.list` | blackmatrix7 | YouTube 与 YouTube Music |

## 主配置加载顺序

`Conf/LINNUX.conf` 中的规则顺序遵循 Surge first-match 逻辑，重点服务规则放在宽泛规则之前。

1. WeChat（微信直连优先）
2. Speedtest（测速不走代理）
3. AI（AI 服务专用路由）
4. Apple（Apple 原生服务）
5. Microsoft（Microsoft/Office 服务）
6. Telegram（Telegram 协议规避混淆）
7. Download（下载 CDN 直连）
8. Game（游戏平台直连/代理）
9. YouTube（YouTube 流媒体路由）
10. TikTok（TikTok 路由）
11. SocialMedia（社交媒体）
12. PayPal（支付服务）
13. Google（Google 服务）
14. Streaming Media（Netflix、Disney+、国际/中国媒体）
15. CDN（共享 CDN 后台回退）
16. Global（通用代理回退）
17. China（中国大陆直连域名）
18. LAN（局域网直连）
19. China IP（中国大陆 IP 回退）
20. FINAL（最终代理）

## 自动更新

### 触发方式

- **定时触发**：每天北京时间 04:00 自动同步
- **手动触发**：GitHub Actions 页面或 GitHub CLI

```bash
gh workflow run auto-rules.yml
```

### 完整流水线

每次 workflow 运行执行以下步骤：

```
触发 workflow
  ↓
1. 拉取上游源 → 合并手动规则 → 应用排除 → 清洗校验
  ↓
2. 生成紧凑清单（稳定内容哈希ID + 来源标注） ← scripts/manifest.py
  ↓
3. 对比 git HEAD 生成增量差异报告             ← scripts/diff_manifests.py
  ↓
4. 验证仓库不变量                              ← scripts/validate_surge_repo.py
  ↓
5. 联网审查（5 项检查）                       ← scripts/audit_rules.py
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

> 流程中的 **Generate Rule Manifests**、**Online Audit** 和 **Sync DNS Mapping** 步骤由本仓库新增或合并，确保每次变更有据可查、可审计。

### 清单索引系统

每条规则在 `Rule/.manifests/*.manifest` 中有一个 12 字符的稳定内容哈希 ID，并标注其上游来源（如 `blackmatrix7 Apple`、`SukkaW CDN`、`Manual Rules`）。

数据格式（每行一个规则）：

```
<12字符哈希ID>\t<来源名称>
```

好处：
- 跨版本追踪每条规则的**增减变化**
- 识别规则在来源间的**归属转移**
- 生成增量差异报告（`scripts/diff_report.md`）
- 上游规则变动可量化审计

## 手动规则

在 `Rule/Manual/` 目录下可放置自定义规则文件：

- `<名称>.txt`：手动追加规则，放在对应规则文件顶部，优先级最高。
- `<名称>.exclude.txt`：排除规则。每行一行 Surge 规则或子串，上游匹配到的规则行不会写入最终文件。

### exclude 匹配机制

exclude 使用 `grep -vFf`（固定字符串匹配），**不是**正则匹配。这意味着：

- `DOMAIN-SUFFIX,sentry.io` 只匹配**完全相同的行**
- `DOMAIN-SUFFIX,o207216.ingest.sentry.io` **不会被** `DOMAIN-SUFFIX,sentry.io` 匹配到（字符串不同）
- 如需匹配子域名变体，使用子串模式如 `.ingest.sentry.io`，或逐一列举

> 长期需要保留/排除的规则必须放入对应的 `.txt` / `.exclude.txt`。不要依赖旧生成文件作为隐式 baseline。

## 规则校验

提交前运行：

```bash
python3 scripts/validate_surge_repo.py
```

检查项：

- Surge 规则类型合法性
- 无策略名渗入
- 无重复规则
- `# TOTAL` 头与实际计数一致
- `China.list` domain-only
- `China_IP.list` 无 `no-resolve`
- 其他 IP 规则带 `no-resolve`
- `Microsoft.list` 无 GitHub 家族
- `fast.com` 仅出现在 `Speedtest.list`
- README、workflow 与 `.list` 文件一致性
- 无旧 baseline 区块和 SukkaW marker 域名
- **共享第三方基础设施**检测（cookielaw、onetrust、adobedtm、braze、newrelic、segment、sentry、optimizely 等出现在服务规则中时告警）← 新增
- **PayPal CN 域名**检测（.cn 域名不应在 PayPal.list 中）← 新增
- **不透明子域名**检测（纯数字/十六进制前缀的子域名如 `o207216.ingest.sentry.io` 标记为可疑共享基础设施）← 新增

## 联网审查

每次 workflow 生成规则后、提交 GitHub 前，执行 `scripts/audit_rules.py` 进行检查：

| 检查项 | 说明 |
|--------|------|
| 上游可达性 | 所有配置的 URL 可正常访问 |
| 规则数对比 | 生成 vs 上游比例异常时告警（多源合并文件豁免） |
| 共享基础设施 | 已知共享平台出现在服务规则中时告警 |
| Surge 文档 | 检查是否有新的 Surge 规则类型发布 |
| exclude 覆盖率 | 所有在用的 exclude 文件仍有效 |

审计结果中：
- **ERROR** → workflow 失败，必须修复
- **WARN** → workflow 继续，但需人工确认
- **INFO** → 仅供参考，无需处理

## 关键策略

- **GitHub** 不归入 `Microsoft.list`。GitHub 普通服务走 `Global.list`，Copilot 走 `AI.list`，仅明确下载资源域名如 `release-assets.githubusercontent.com` 进入 `CDN.list`。
- **`fast.com`** 只放在 `Speedtest.list`。
- **`China.list`** 只保存中国大陆直连域名，不放 IP 规则。
- **`China_IP.list`** 不加 `no-resolve`，以便未命中域名解析后做中国大陆 IP 分类。
- 其他 IP 规则默认加 `no-resolve`。
- 生成规则时不保留当前 `Rule/*.list` 作为 baseline；长期规则必须进入 `Rule/Manual/*.txt` / `exclude.txt`。
- **共享第三方基础设施**（CDN / 遥测 / 分析 / 隐私合规 / 共享云）不作为服务专属规则合并。
- 服务专属子域名（如 `disney.my.sentry.io`、`netflix.demdex.net`）可保留；**不透明**子域名（如 `o207216.ingest.sentry.io`）应排除。

## 规则维护要求

修改规则或同步逻辑前，请优先阅读 `AGENT.md`。该文件包含完整的用户偏好、分类策略、验证标准和工作流程。

## 致谢

上游规则与参考来源：

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules)
- [SukkaW/Surge](https://github.com/SukkaW/Surge)
- [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge)
- [QuixoticHeart/rule-set](https://github.com/QuixoticHeart/rule-set)
- [Telegram 官方 CIDR](https://core.telegram.org/resources/cidr.txt)

工作流基于 [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge) 的思路改编，并加入了本仓库自己的分类策略、校验规则和联网审查流水线。
