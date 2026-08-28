# 已审查来源快照

本目录保存 Kelee Speedtest 每日主上游的已审查兜底快照。`check_upstream_updates.py` 每日探测 Kelee 原始 URL；只有 URL 恢复且内容指纹改变时，才会触发相关规则集的重新生成。生成时若 Kelee 临时遭遇 WAF、TLS 或网络故障，生成器和审计会显式降级为本目录的快照，不把故障误判为内容更新或清空已发布规则。

## Speedtest（Kelee / Loon）

| 文件 | 原始引用 URL | 获取方式 | 规则数 | 上游标注时间 | SHA-256 |
|---|---|---|---:|---|---|
| SpeedtestChina.lsr | https://kelee.one/Tool/Loon/Lsr/SpeedtestChina.lsr | GitHub 公开镜像 `mihoyo-typ/KeleeOne@ab6c3182fb2b09bcc34456f496282ec0b8e9217b` | 9 | 2025-09-16 02:27:32 | `c5c5b41f812cdd071a7e7f2a5b6c07b84f191ff84b3274bb532c2f8261b97258` |
| SpeedtestInternational.lsr | https://kelee.one/Tool/Loon/Lsr/SpeedtestInternational.lsr | GitHub 公开镜像 `ClaraCora/ege@main` | 17,692 | 2026-08-22 05:18:32 | `624081287e01fc6cd480e2733a700048aa005ece1d0ff6a8c42038c2c939089a` |

2026-08-28 复核时，两个原始 `kelee.one` URL 在当前生成环境均被 Cloudflare 拒绝（HTTP 403）。按维护者明确要求，二者仍作为**每日主上游**；本快照仅在主上游不可用时提供 fail-closed 的内容兜底。主上游恢复后，只有每日状态检查检测到内容指纹变化才会触发重新生成；更新后的规则仍须通过生成、manifest、路由、审计和 CI 门禁。

快照保留 Loon 原始文本；`scripts/generate_rules.py` 在输出 Surge 规则时仅规范化逗号后的空白，且对 IP 规则补充 Surge 所需的 `no-resolve`。