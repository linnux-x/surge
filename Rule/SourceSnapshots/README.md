# 已审查来源快照

本目录保存无法作为可靠自动化上游、但已由维护者审核并纳入生成链的规则输入快照。生成器只从本目录读取 `snapshot` 格式来源；`check_upstream_updates.py` 不探测这些本地文件，因此不会把临时网络故障误判为规则更新。

## Speedtest（Kelee / Loon）

| 文件 | 原始引用 URL | 获取方式 | 规则数 | 上游标注时间 | SHA-256 |
|---|---|---|---:|---|---|
| SpeedtestChina.lsr | https://kelee.one/Tool/Loon/Lsr/SpeedtestChina.lsr | GitHub 公开镜像 `mihoyo-typ/KeleeOne@ab6c3182fb2b09bcc34456f496282ec0b8e9217b` | 9 | 2025-09-16 02:27:32 | `c5c5b41f812cdd071a7e7f2a5b6c07b84f191ff84b3274bb532c2f8261b97258` |
| SpeedtestInternational.lsr | https://kelee.one/Tool/Loon/Lsr/SpeedtestInternational.lsr | GitHub 公开镜像 `ClaraCora/ege@main` | 17,692 | 2026-08-22 05:18:32 | `624081287e01fc6cd480e2733a700048aa005ece1d0ff6a8c42038c2c939089a` |

2026-08-28 复核时，两个原始 `kelee.one` URL 在当前生成环境均被 Cloudflare 拒绝（HTTP 403），故**不**将其直接加入每日网络拉取。后续仅在可重新获取、核对内容差异并审查通过后更新本快照、规则测试、manifest 与哈希记录。

快照保留 Loon 原始文本；`scripts/generate_rules.py` 在输出 Surge 规则时仅规范化逗号后的空白，且对 IP 规则补充 Surge 所需的 `no-resolve`。