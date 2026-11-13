# 四个实用模块

本仓库保存经过检查和修改的上游副本。每个模块保留独立文件及来源信息，脚本来自本仓库，不会自动跟随上游仓库变更。脚本自身仍会通过 Surge 的远程资源更新机制获取本仓库的新版本。

以下地址在本 PR 合并到 main 后可安装；分支上的模块引用 main 脚本，不适合提前安装。

| 模块 | 正式安装地址 |
| --- | --- |
| 京东比价 | https://raw.githubusercontent.com/linnux-x/surge/main/Module/jd_price2.sgmodule |
| Telegram 跳转 | https://raw.githubusercontent.com/linnux-x/surge/main/Module/TgRedirect.sgmodule |
| po0 防火墙加白 | https://raw.githubusercontent.com/linnux-x/surge/main/Module/po0-firewall-whitelist.sgmodule |
| Reddit 自动翻译 | https://raw.githubusercontent.com/linnux-x/surge/main/Module/RedditTranslation.sgmodule |

## 京东比价

先启用获取慢慢买登录数据的脚本，再打开慢慢买 App 的「我的」，随后打开京东商品详情。获取成功后可将 `MMMCK_SCRIPT` 设为 `#` 禁用采集脚本。数据保存在当前设备的 `manmanbuy_val`，不会通过 iCloud 模块文件同步。

- 保留慢慢买 V1/V2 请求顺序与原签名；`mmb_v` 持久化参数仍可选择 V2，默认 V1。
- 获取登录数据后明确结束脚本；数据不完整时不覆盖旧值；通知与日志不再显示完整登录数据。
- 网络、HTTP 状态、JSON、价格列表异常有清楚提示；超时总预算限制在脚本超时之前。
- 注入兼容带属性或大写的 `<body>`，服务返回的内容经过 HTML 转义，表格样式只作用于比价区域。
- 删除未使用的多客户端 Env 及 Node 自执行测试代码，保留内置 MD5 以维持签名兼容；现在仅面向 Surge。

需要 MITM 两个模块指定域名。登录数据仅保存在本机，并随查询发给慢慢买官方接口。结果依赖第三方服务和京东 App 版本，模拟测试不能证明当前 App 页面兼容。

## Telegram 跳转

`Client` 可选 Telegram、Swiftgram、Turrit、iMe、Nicegram、Lingogram 或其 scheme 简写。需要设备已安装对应客户端，且 MITM 已启用并信任证书。

保留机器人 `start`、小程序 `startapp`、评论等参数，支持私有频道、话题、表情包和分组链接。路径已经确定的目标字段不会被查询串里的同名参数覆盖。只接受列出的客户端 scheme；不认识的路径继续网页访问；POST 和明确非 HTML 的请求放行。未带 Accept 的 GET 请求按页面访问处理。

转换规则参考 [Telegram Deep links](https://core.telegram.org/api/links)。第三方客户端是否支持每个深链由客户端决定。

## po0 防火墙加白

在模块参数 `tokens` 中填 API token，多个用逗号分隔，可附 `@0` 等固定槽位。不要将实际 token 写进公开模块或脚本。同一设备只启用一份 po0 加白模块，避免重复触发。

- Surge 请求在脚本内指定 DIRECT，禁用自动 Cookie 和重定向；模块仍保留 API 直连规则。
- 槽位要求非负安全整数，拼写错误不会降级为无槽位写入；错误编码的参数不会意外使用持久化的旧 token。
- HTTP 非成功状态不能被误报为已加白；响应格式异常、无状态回调都能正常结束。
- 网络错误最多尝试三次，临时 5xx 和裸 400 可重试，其余状态不重试；通知中的 token 被脱敏。

API 按原协议将 token 放在 HTTPS URL 路径中；API 服务及 Surge 本地请求记录仍可能看到该 URL。历史状态与存储键保持上游约定。没有调用真实加白接口做测试。

## Reddit 自动翻译

`Lang` 默认 `zh-hans`，可选 `zh-hant`。只在模块列出的 Reddit GraphQL 域名上替换翻译请求头，删除旧头时忽略大小写；保留其他请求头，不读写登录数据，不另发请求。需要 MITM 指定域名并在 Reddit App 中访问内容。实际翻译可用性由 Reddit 服务和 App 决定。

## 验证与来源

```sh
node tests/test_audited_modules.js
python3 scripts/pipeline.py verify --ci
```

测试使用模拟网络和合成凭据，覆盖 V1/V2 签名、登录数据采集、HTML 转义、网络失败/超时、链接转换、域名匹配、槽位验证和 API 错误。四个模块尚未在 iPhone App 内端到端验证，也没有安装到设备或修改现有配置。

来源：githubdulong/Script、wf021325/qx、Yu9191/Rewrite、w0ven/po0fw、fmz200/wool_scripts、RavelloH gist。模块文件头保留来源 URL 和获取时文件哈希；其中 fmz200/wool_scripts 声明 GPL-3.0，其余直接来源未声明许可证。这些第三方衍生文件不适用本仓库 MIT，原作者权利与上游声明不变。
