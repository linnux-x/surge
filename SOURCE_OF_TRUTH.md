# Source of truth

本文件是公开仓库、私有配置、真实设备配置之间的边界权威说明。其他文档只保留入口指针，不重复展开私有配置细节。

- **规则源码与生成逻辑**：本仓库 `~/Desktop/github/surge`。
- **公开分发**：GitHub 公开仓库 `linnux-x/surge` 的受跟踪规则、模块和 Raw URL。
- **真实设备配置**：不在本仓库；物理正典位于 `~/Library/Application Support/LinnuxPrivateData/private-config/surge-devices`，桌面 `private-config` 为兼容入口。
- **正确方向**：可信上游 → 下载/清洗/校验/测试 → 自动化分支/PR → exact-SHA CI → 合并 `main` → 设备通过公开规则 URL 获取。
- **禁止内容**：真实代理凭据、MITM 材料、私钥、内网信息和设备完整配置。
- **规则同步流水线归属**：由维护者本机 Hermes 每天北京时间 05:00 调度并运行本仓库同一套 `scripts/*.py`，旧 Codex 规则维护任务已暂停。Hermes 在隔离工作区完成上游探测、生成、校验和 Agent 审阅，把确定性产物推到唯一自动化分支并创建 PR；只有 exact head SHA 的 CI 全绿后才合并 `main`。`auto-rules.yml` 只保留手动 full generation。调度配置应保持每天 05:00，与任务提示词一致；启用状态与模型正常返回不能证明维护成功，须核对本轮执行日志、收据时间、PR 和合并后 CI。
- **发布故障闭环**：自动化 PR 的 CI 失败时保留分支和 PR，并以稳定 finding code 更新唯一故障 Issue；`main` CI 失败由 `ci-failure-issue.yml` 去重记录，恢复后追加证据并关闭。

## 下游消费者（Raw URL 是对外契约）

以下路径的 Raw URL 已被外部消费，**视为公开契约，不得改路径、不得迁移到孤儿分支**；确需变更须先同步下游：

| 路径 | 消费方 | 说明 |
|---|---|---|
| `Rule/*.list` | 私有 `private-config/surge-devices/{ios,mac,tvos}.conf` | 真实设备配置直接引用 Raw URL |
| `Conf/Linnux.conf` | Surge 客户端 | 首行 `#!MANAGED-CONFIG`，`interval=86400` 自拉 |
| `clash/*.yaml` | 私有仓库 `linnux-x/clash` 的 `Clash_Local.yaml` | 16+ 个 `rule-provider` 硬引用 `main/clash/*.yaml` |

> 将生成物迁到孤儿分支会打断上表三类消费者（尤其 `clash` 私有仓库）。如需调整分发结构，必须先完成下游引用迁移。
