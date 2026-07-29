# Source of truth

- **规则源码与生成逻辑**：本仓库 `~/Desktop/github/surge`。
- **公开分发**：GitHub 公开仓库 `linnux-x/surge` 的受跟踪规则、模块和 Raw URL。
- **真实设备配置**：不在本仓库；物理正典位于 `~/Library/Application Support/LinnuxPrivateData/private-config/surge-devices`，桌面 `private-config` 为兼容入口。
- **正确方向**：可信上游 → 下载/清洗/校验/测试 → commit/push → 设备通过公开规则 URL 获取。
- **禁止内容**：真实代理凭据、MITM 材料、私钥、内网信息和设备完整配置。
