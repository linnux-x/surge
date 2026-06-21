# Linnux Surge 自用规则仓库

这是一个面向 Surge 的自用规则仓库，用于在 iPhone、MacBook 等设备上进行代理分流、区域直连、媒体服务、AI 服务、CDN 与中国大陆 IP/域名分类。

仓库会通过 GitHub Actions 定时同步多个上游规则源，合并本地手动规则，并应用本仓库专属的规则清洗与校验策略。生成时不会把当前已有 `Rule/*.list` 当作 baseline 继续保留，避免上游已删除或本地历史遗留规则长期滞留。

## 目录结构

| 路径 | 说明 |
|------|------|
| `Conf/LINNUX.conf` | 主 Surge 配置示例，包含策略组和 `RULE-SET` 加载顺序 |
| `Rule/*.list` | Surge 外部规则集文件 |
| `Rule/Manual/*.txt` | 手动追加规则，优先级高于同步规则 |
| `Rule/Manual/*.exclude.txt` | 排除规则，匹配到的上游行不会写入最终规则 |
| `Module/*.sgmodule` | Surge 模块文件 |
| `.github/workflows/auto-rules.yml` | 当前主要规则同步工作流 |
| `.github/workflows/sync-dns-mapping.yml` | DNS Mapping 模块同步工作流 |
| `.codex/skills/surge-ruleset-builder/` | 规则维护与校验说明 |

## 规则列表

| 规则文件 | 主要上游来源 | 说明 |
|---------|-------------|------|
| `AI.list` | SukkaW、Rabbit-Spec | AI 服务、模型 API、Apple Intelligence、AIGC 等 |
| `Apple.list` | blackmatrix7 | Apple 全系服务 |
| `Apple_CN.list` | SukkaW | Apple 中国区与 Apple CDN 直连规则 |
| `CDN.list` | SukkaW | CDN、静态资源、部分专用下载资源 |
| `China.list` | SukkaW、blackmatrix7、Rabbit-Spec | 中国大陆直连域名规则；保持 domain-only |
| `China_IP.list` | Loyalsoldier、blackmatrix7、Rabbit-Spec | 中国大陆 IP 回退规则；本仓库特意不加 `no-resolve` |
| `ChinaMedia.list` | blackmatrix7 | 中国媒体服务 |
| `Disney.list` | blackmatrix7 | Disney+ |
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
| `Telegram.list` | blackmatrix7、Telegram 官方、SukkaW | Telegram 域名、CIDR、ASN 与客户端 fallback |
| `TikTok.list` | blackmatrix7 | TikTok |
| `WeChat.list` | blackmatrix7 | 微信相关服务 |
| `YouTube.list` | blackmatrix7 | YouTube 与 YouTube Music |

## 主配置加载顺序

`Conf/LINNUX.conf` 中的规则顺序遵循 Surge first-match 逻辑，重点服务规则会放在更宽泛的提供商、CDN、Global、China 和 IP fallback 之前。

当前主要顺序：

1. WeChat
2. Speedtest
3. AI
4. Apple
5. Microsoft
6. Telegram
7. Game
8. YouTube
9. TikTok
10. SocialMedia
11. PayPal
12. Google
13. Streaming Media
14. CDN
15. Global
16. China
17. LAN
18. China IP
19. FINAL

## 自动更新

规则每天北京时间 04:00 自动同步上游并提交。

当前主要工作流是：

```text
.github/workflows/auto-rules.yml
```

可在 GitHub Actions 页面手动触发，也可以使用 GitHub CLI 指定文件名触发：

```bash
gh workflow run auto-rules.yml
```

> 旧版 `.github/workflows/auto-surge-rules.yml` 已删除，避免重新生成旧规则文件。当前只保留 `.github/workflows/auto-rules.yml` 作为规则同步 workflow。

## 手动规则

在 `Rule/Manual/` 目录下可放置自定义规则文件：

- `<名称>.txt`：手动追加规则，会被放在对应规则文件顶部，优先级最高。
- `<名称>.exclude.txt`：排除关键词，匹配到的上游规则行不会写入最终文件。

> 如果某条当前规则需要长期保留，请放入对应 `Rule/Manual/<名称>.txt`；如果某条上游规则需要长期排除，请放入对应 `Rule/Manual/<名称>.exclude.txt`。不要依赖旧生成文件作为隐式 baseline。

示例：

```text
Rule/Manual/AI.txt
Rule/Manual/AI.exclude.txt
Rule/Manual/Speedtest.txt
```

## 本仓库的关键策略

- GitHub 不归入 `Microsoft.list`。
- GitHub 普通服务、Pages、Assets、User Content 走 `Global.list`。
- GitHub Copilot 走 `AI.list`。
- 只有明确下载资源域名，例如 `release-assets.githubusercontent.com`，才进入 `CDN.list`。
- `fast.com` 只放在 `Speedtest.list`。
- `China.list` 只保存中国大陆直连域名，不放 IP 规则。
- `China_IP.list` 作为本仓库特例，不添加 `no-resolve`，以便未命中的域名可通过本地解析后再做中国大陆 IP 分类。
- 其他 IP 规则默认应添加 `no-resolve`。
- 生成规则时不保留当前 `Rule/*.list` 作为 baseline；本地长期规则必须进入 `Rule/Manual/*.txt` 或 `Rule/Manual/*.exclude.txt`。
- 全局过滤 SukkaW marker/test 域名 `7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe`。
- 避免把共享 CDN、共享云服务、统计分析、遥测、登录/支付等高误伤基础设施盲目合并到服务规则中。

## 规则维护要求

修改规则或同步逻辑前，请优先阅读：

```text
AGENT.md
.codex/skills/surge-ruleset-builder/SKILL.md
.codex/skills/surge-ruleset-builder/references/sources.md
.codex/skills/surge-ruleset-builder/references/Learned Patterns.md
```

提交前建议运行：

```bash
python3 scripts/validate_surge_repo.py
```

该脚本会检查：

- 非注释行是否为 Surge 支持的规则类型；
- 外部 ruleset 中是否误带策略名；
- 是否有重复规则；
- `# TOTAL` 头是否等于实际非注释规则数；
- `China.list` 是否仍然 domain-only；
- `China_IP.list` 是否没有 `no-resolve`；
- 其他 IP 规则是否带有 `no-resolve`；
- `Microsoft.list` 是否没有 GitHub 家族规则；
- `fast.com` 是否只出现在 `Speedtest.list`；
- README、workflow 与实际 `Rule/*.list` 文件是否一致；
- 生成文件是否不含旧 baseline 区块和 SukkaW marker/test 域名；
- 非主 workflow 是否仍有定时触发或重复 workflow 名称。

## 致谢

上游规则与参考来源：

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules)
- [SukkaW/Surge](https://github.com/SukkaW/Surge)
- [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge)
- [QuixoticHeart/rule-set](https://github.com/QuixoticHeart/rule-set)
- [Telegram 官方 CIDR](https://core.telegram.org/resources/cidr.txt)

工作流基于 [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge) 的思路改编，并加入了本仓库自己的分类策略和校验规则。
