# Looking Glass · 参考路由追踪

安装地址（合并进 main 后可用）：

```text
https://raw.githubusercontent.com/linnux-x/surge/main/Module/RouteTrace.sgmodule
```

在 Surge 中添加模块后启用，点击面板发起测试。面板没有自动刷新间隔，单次脚本最长 60 秒；不需要 MITM 或 API token。

- `Proxy`：用于查询落地 IP 的策略或策略组，默认 `跟随规则`。
- `Probe`：首段公共探针位置，默认 `自动`；可填 `Nanjing+AS4134` 等 Globalping 条件。
- `MaskIP`：默认 `true`，遮盖面板上的本地、入口、落地 IP；中间跳不遮盖。

模块通过 Surge 最近请求识别代理入口，用 Globalping 公共探针分别测到入口、落地 IP 的 MTR。每跳显示 IPv4、位置、AS 号和最小 RTT；连续无响应跳合并显示。找不到同城同网探针时会依次放宽选点条件，实际所选探针显示在面板中。

公共探针的路径可能与本机完全不同；两段结果不能拼成真实代理路径，专线也无法由公网探针观察。入口无法识别时仅显示到落地的参考追踪。目前仅支持 IPv4。

Globalping 会收到入口和落地目标 IP，测量结果可能被持有测量 ID 的人读取；平安 IP 接口收到需要查询归属的地址，IPPure 用于查询出口。`MaskIP` 仅控制面板显示，不会隐藏发给服务方的目标。每次最多创建两次成功测量，免费额度和探针可用性由 Globalping 决定。

本地验证：

```sh
node tests/test_route_trace.js
python3 scripts/pipeline.py verify --ci
```
