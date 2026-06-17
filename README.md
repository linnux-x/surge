# surge自用仓库

自动同步上游规则的 Surge 规则仓库。

## 规则列表

| 规则文件 | 上游来源 | 说明 |
|---------|---------|------|
| `AI.list` | EAlyce/conf | AI 服务（ChatGPT 等） |
| `Apple.list` | blackmatrix7 | Apple 全系服务 |
| `BiliBili.list` | blackmatrix7 | 哔哩哔哩 |
| `China.list` | blackmatrix7 | 中国直连 |
| `ChinaCIDR.list` | Loyalsoldier | 中国 CIDR |
| `ChinaASN.list` | VirgilClyne | 中国 ASN |
| `ChinaMedia.list` | blackmatrix7 | 中国媒体 |
| `Disney.list` | blackmatrix7 | Disney+ |
| `Facebook.list` | blackmatrix7 | Facebook |
| `Game.list` | blackmatrix7 (聚合) | 游戏平台（Steam/Epic/Sony/Nintendo） |
| `GlobalMedia.list` | blackmatrix7 | 国际媒体 |
| `Google.list` | blackmatrix7 | Google 服务 |
| `Instagram.list` | blackmatrix7 | Instagram |
| `Meta.list` | AMEKIN | Meta（Facebook 母公司） |
| `Microsoft.list` | blackmatrix7 | Microsoft 服务 |
| `Netflix.list` | blackmatrix7 | Netflix |
| `Proxy.list` | blackmatrix7 (聚合) | 代理（GitHub/Telegram/Proxy） |
| `Spotify.list` | blackmatrix7 | Spotify |
| `Telegram.list` | Sukka | Telegram |
| `TelegramASN.list` | VirgilClyne | Telegram ASN |
| `TikTok.list` | blackmatrix7 | TikTok |
| `YouTube.list` | blackmatrix7 | YouTube |

## 自动更新

规则每天北京时间 04:00 自动同步上游并提交。

也可在 GitHub Actions 页面手动触发：`Auto-Surge-Rules` → `Run workflow`。

## 手动规则

在 `Rule/Manual/` 目录下可放置自定义规则文件：

- `<名称>.txt` — 手动追加规则（优先级最高）
- `<名称>.exclude.txt` — 排除关键词（匹配的行不会被写入）

## 致谢

上游规则来源：
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules)
- [Sukka/Surge](https://github.com/Sukka/Surge)
- [VirgilClyne/GetSomeFries](https://github.com/VirgilClyne/GetSomeFries)
- [EAlyce/conf](https://github.com/EAlyce/conf)
- [AMEKIN/Surge](https://github.com/AMEKIN/Surge)

工作流基于 [Rabbit-Spec/Surge](https://github.com/Rabbit-Spec/Surge) 改编。
