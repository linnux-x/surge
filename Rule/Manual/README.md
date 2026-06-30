# Manual Rules｜手工规则目录

> **本目录已加入 `.gitignore`**：个人手工规则不会提交到公开仓库。  
> Fork 用户可以在这里添加自己的 include / exclude 规则。

---

## 文件约定

| 文件模式 | 用途 | 优先级 |
|---|---|---|
| `<RulesetName>.txt` | 手工追加规则，生成时放在对应规则集顶部 | 最高 |
| `<RulesetName>.exclude.txt` | 从上游生成规则中移除的精确规则行 | 护栏前应用 |

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

> ⚠️ exclude 使用 **整行精确匹配**，不是子串匹配。  
> 必须写出和上游来源中完全一致的完整规则行。

```text
# 正确：精确匹配上游规则行
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
