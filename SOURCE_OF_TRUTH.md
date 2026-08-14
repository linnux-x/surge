# Source of truth

本文件是公开仓库、私有配置、真实设备配置之间的边界权威说明。其他文档只保留入口指针，不重复展开私有配置细节。

- **规则源码与生成逻辑**：本仓库 `~/Desktop/github/surge`。
- **公开分发**：GitHub 公开仓库 `linnux-x/surge` 的受跟踪规则、模块和 Raw URL。
- **真实设备配置**：不在本仓库；物理正典位于 `~/Library/Application Support/LinnuxPrivateData/private-config/surge-devices`，桌面 `private-config` 为兼容入口。
- **正确方向**：可信上游 → 下载/清洗/校验/测试 → commit/push → 设备通过公开规则 URL 获取。
- **禁止内容**：真实代理凭据、MITM 材料、私钥、内网信息和设备完整配置。
- **每日流水线归属**：由维护者的 Hermes agent 在本机执行（北京时间 05:00），跑本仓库同一套 `scripts/*.py` 并直接 push。调度在 Hermes 自身的任务系统内，不在 crontab / launchd / GitHub Actions；`auto-rules.yml` 只保留手动触发。因此 Hermes 未运行时当天不会同步，且从系统层看不到该计划任务。

## 下游消费者（Raw URL 是对外契约）

以下路径的 Raw URL 已被外部消费，**视为公开契约，不得改路径、不得迁移到孤儿分支**；确需变更须先同步下游：

| 路径 | 消费方 | 说明 |
|---|---|---|
| `Rule/*.list` | 私有 `private-config/surge-devices/{ios,mac,tvos}.conf` | 真实设备配置直接引用 Raw URL |
| `Conf/Linnux.conf` | Surge 客户端 | 首行 `#!MANAGED-CONFIG`，`interval=86400` 自拉 |
| `clash/*.yaml` | 私有仓库 `linnux-x/clash` 的 `Clash_Local.yaml` | 16+ 个 `rule-provider` 硬引用 `main/clash/*.yaml` |

> `audits/full-repo-audit-2026-07-03.md` 曾建议将生成物迁到孤儿分支以控制 `.git` 体积。该方案会同时打断上表三类消费者（尤其 `clash` 私有仓库），执行前必须先改下游引用。
