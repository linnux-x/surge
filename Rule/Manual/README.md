# 手工规则目录

> **本目录中的 `*.txt` 与 `*.exclude.txt` 会提交到公开仓库**，用于让本地、CI 和定时生成使用同一套手工 include / exclude 输入。
> Fork 用户可以在这里添加自己的 include / exclude 规则；如果规则含私有域名、IP、token、订阅地址或个人基础设施信息，请不要提交到公开仓库。公开/私有边界以仓库根目录 `SOURCE_OF_TRUTH.md` 为准。
> `override-manifest.json` 是本目录的公开治理账本：所有 `*.txt` 文件必须有文件级基线；新增或修改会影响 first-match 路由的例外，必须额外建立条目级记录和路由测试。

---

## 文件约定

| 文件模式 | 用途 | 优先级 |
|---|---|---|
| `<RulesetName>.txt` | 手工追加规则，生成时放在对应规则集顶部 | 最高 |
| `<RulesetName>.exclude.txt` | 按显式类型和值从上游移除规则 | 护栏前应用 |

---

## 格式

两类文件格式相同：

- 每行一条规则；
- 支持空行；
- 支持 `#` 注释。

### `<RulesetName>.txt`：手工 include

```text
# 添加应始终出现在该规则集中的规则
DOMAIN-SUFFIX,example.com
DOMAIN,api.example.com
IP-CIDR,10.0.0.0/8
```

这些规则会出现在生成后的 `.list` 文件顶部，位于所有上游来源之前。

### `<RulesetName>.exclude.txt`：手工 exclude

exclude 必须写出明确的规则类型和值，裸域名和裸关键词会使生成及 CI 失败。

- `DOMAIN`、`DOMAIN-SUFFIX`、`DOMAIN-KEYWORD`、`DOMAIN-WILDCARD` 按 **类型和值**（忽略大小写）排除，同一身份的 `extended-matching` 变体一并移除。
- 其他类型仍按整行精确匹配；例如 `IP-ASN,13335,no-resolve` 不排除 `IP-ASN,13335`，不能抹掉 IP 选项的语义。
- 排除不是子串匹配或父后缀覆盖：`DOMAIN-SUFFIX,example.com` 不排除 `DOMAIN,example.com` 或 `DOMAIN,api.example.com`；需要分别声明。
- 手工 include 优先于上游 exclude，可显式保留服务专属端点。CI 独立扫描最终生成物，阻止排除规则以选项变体泄漏。

```text
# 按域名规则身份排除（也移除 extended-matching 变体）
DOMAIN-SUFFIX,sentry.io

# 也正确：同时匹配 DOMAIN 和 DOMAIN-SUFFIX 两种变体
DOMAIN,o33249.ingest.sentry.io
DOMAIN-SUFFIX,o33249.ingest.sentry.io
```

exclude 会在每个 source 内、护栏应用前执行。因此，如果不同上游对同一条目使用不同规则类型，例如一个是 `DOMAIN,example.com`，另一个是 `DOMAIN-SUFFIX,example.com`，就需要在 exclude 文件里同时写出两种完整规则行。

---

## 示例

如果 fork 用户想给 `AI.list` 增加自定义代理规则，并从 `Global.list` 排除一些域名，可以使用：

```text
Rule/Manual/
├── AI.txt              # 额外加入 AI 规则集的域名
├── AI.exclude.txt      # 从上游 AI 来源中移除的域名
├── Global.exclude.txt  # 从上游 Global 来源中移除的域名
└── README.md           # 本说明文件
```
