# linnux-x/surge 全方位审计报告

> [!IMPORTANT]
> **这是 2026-07-03 的历史快照，不代表当前状态。** 下文所有"发现"按当时的时态书写，其中多数已修复。
>
> 复核于 2026-07-30（HEAD `5889bb4`，快照之后约 280 个提交）：
>
> | 条目 | 现状 |
> |---|---|
> | 3.1 下载无超时 | **已修复** — `generate_rules.py` 的 `CURL_OPTS` 已含 `--connect-timeout 10 --max-time 60`，外层另有 `FETCH_SUBPROCESS_TIMEOUT = 120` 兜底 |
> | 3.2 上游抓取两遍 | **已修复** — `audit_rules.py` 改为 `fetch_all_sources()` 抓一次后复用 |
> | 3.3 HTTP 三套实现 | **部分修复** — 已提取 `scripts/http_util.py`，但目前只有 `audit_rules.py` 引用；`generate_rules.py` 仍用 curl 子进程、`check_upstream_updates.py` 仍直接用 `urllib`（三者超时行为已各自补齐） |
> | 3.4 策略常量分散 | **已修复** — 新增 `scripts/policy.py` 作为唯一源，5 个脚本引用；宽档审计集合改为由严格集合派生，无法再漂移 |
> | git 历史膨胀（§ 结论部分） | **仍存在且已增长** — `.git` 约 35 MB / 284 提交 / 47 天。注意报告建议的"生成物移孤儿分支"方案有跨仓库破坏性，见 `SOURCE_OF_TRUTH.md` 的下游消费者表 |
>
> 另有事实性漂移：报告称 `.github/workflows/` 有 3 条 workflow、`Rule/*.list` 23 个，当前是 2 条、24 个。

- **审计对象**：https://github.com/linnux-x/surge @ `1b13a57`（2026-07-03）
- **审计范围**：`Conf/Linnux.conf`、`Rule/*.list`（23 个规则文件，约 16.4 万行）、`clash/*.yaml`、`Module/`（不含 VPS-Monitor，按要求排除）、`scripts/*.py`（11 个）、`.github/workflows/`（3 条）、`tests/`
- **方法**：克隆到本地只读分析 + 规则文件逐类抽查 + 脚本逐个通读 + 对照 Surge 官方文档（manual.nssurge.com / kb.nssurge.com）核实每条配置建议
- **结论先行**：仓库工程化水平高于绝大多数同类规则仓库，未发现功能性缺陷或安全漏洞；发现 2 个可靠性问题（高优先级）、若干去重与维护性优化项。

---

## 1. 总体评价

**做得好的地方（审计中逐一核实）：**

| 项 | 说明 |
|---|---|
| 单一上游源定义 | `scripts/sources.py` 集中定义 11 个上游 URL 与规则集规格，其余脚本统一引用 |
| 零第三方依赖 | 全部脚本仅用 Python 标准库，供应链攻击面极小 |
| 状态原子提升 | 上游状态先写 `source_state.next.json`，仅在提交前才提升为正式状态（`auto-rules.yml:62-65, 211-212`），push 失败不会污染状态 —— 设计正确 |
| CI 供应链加固 | 所有 GitHub Actions 已按 commit SHA 固定；workflow 权限最小化（`ci.yml` 只读，`auto-rules.yml` 才有 `contents: write`）；无硬编码 secrets |
| 规则质量 | 抽查 12 个含 IP 的服务规则文件，IP 规则 100% 带 `no-resolve`；`# TOTAL` 头与实际计数一致；仅使用合法规则类型 |
| 防泄漏配置 | `udp-policy-not-supported-behaviour = reject`、`always-real-ip` 覆盖 STUN/NTP/游戏主机、`skip-proxy` 完整 |
| 验证纵深 | 生成期变换（guardrails）+ 提交前校验（validator）+ 联网审计（audit）三层，dry-run 指纹门禁 |

---

## 2. 重点章节 A：Surge 配置与规则质量

### 2.1 ✅ 无需处理：大规则集加载方式（已对照官方文档）

`China.list`（112,395 条）以 `RULE-SET` + `extended-matching` 加载（`Conf/Linnux.conf:143`）。
按 [Surge iOS 5.8.1 官方发布说明](https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-ios)，RULE-SET 与 DOMAIN-SET 的实现已完全重写，Surge 在资源更新时自动预处理并建立索引，**两者性能与内存占用已无差异**（约 10 万条域名规则单次匹配从 100ms 降至个位数毫秒）。因此**无需转换为 DOMAIN-SET**，当前写法即官方推荐状态。

同理，规则集索引化后 `[Rule]` 段内的排序对性能影响可忽略，`LAN` 放在 `China.list` 之后（`Linnux.conf:146`）语义上也无问题（两者都是 DIRECT），不需调整。

**唯一建议**：在 README 中注明最低客户端版本 —— `extended-matching` 需 Surge 5.8.0+，规则集索引优化需 5.8.1+。

### 2.2 🟡 跨文件死规则：7 个域名同时存在于 China.list 与 Global.list

以下 `DOMAIN-SUFFIX` 在两个文件中完全相同：

```
1password.com  agilebits.com  asus.com  avermedia.com
futu5.com  futunn.com  immersivetranslate.com
```

由于 `Global.list`（策略 Global，`Linnux.conf:140`）排在 `China.list`（DIRECT，`:143`）之前，这 7 条实际**全部走代理**，`China.list` 中的对应条目永远不会命中，是死规则。`cross_file_conflicts.py` 的月度检测能发现它们，但主配置的语义歧义仍在。

**建议**：为每个域名做一次归属决策 —— 该直连的加入 `Rule/Manual/Global.exclude.txt`，该代理的加入 `Rule/Manual/China.exclude.txt`，让每个域名只出现在一个文件中。

### 2.3 🟡 引导（bootstrap）依赖：全部资源指向 raw.githubusercontent.com

托管配置首行（`Linnux.conf:1`）与全部 21 条 RULE-SET 均从 `raw.githubusercontent.com` 拉取，该域名在中国大陆直连不可达。运行期影响有限（Surge 缓存旧规则集 + managed-config 非 strict 模式允许更新失败），但**新设备首次导入配置时若无可用代理会失败**。

**建议**（二选一）：
- 在 README「快速上手」中明确说明首次导入需在代理可用的网络环境下进行；
- 或提供一份镜像变体配置（如 jsDelivr `cdn.jsdelivr.net/gh/linnux-x/surge@main/...`），注明镜像有缓存延迟的代价。

### 2.4 🔵 可选增强：hijack-dns 通配符

当前 `hijack-dns = 8.8.8.8:53, 8.8.4.4:53`（`Linnux.conf:29`）只接管 Google DNS。[官方手册 Misc Options](https://manual.nssurge.com/others/misc-options.html) 明确支持 `hijack-dns = *:53` 接管所有明文 DNS 查询（含 IPv6 fake responder），可拦截 IoT 设备与 App 硬编码的任意 DNS。取舍：极少数依赖特定 DNS 做就近调度的内网场景可能受影响，可先在一台设备验证。

### 2.5 🔵 信息项：平台特定规则类型

- `PROCESS-NAME` 共 56 条（上游带入）：仅在 macOS 生效，iPhone 上不匹配但无害。
- `USER-AGENT` 共 179 条：官方文档支持，但仅对可解析 HTTP 的流量生效。
- `China_IP.list` 是纯 IP 规则集，加载时带的 `extended-matching`（`Linnux.conf:149`）对 IP 规则无意义（该参数只作用于域名匹配 SNI/Host），可去掉保持配置整洁，无功能影响。

---

## 3. 重点章节 B：脚本性能与去重

### 3.1 🔴 高：`generate_rules.py` 下载无超时（可靠性）

`fetch_source()`（`scripts/generate_rules.py:217-222`）调用 `curl -fsSL` 仅带重试参数，**既无 `--max-time`，`subprocess.run` 也无 `timeout=`**。上游连接挂起（stalled）时不会触发 curl 重试，每日 workflow 会卡死直到 GitHub Actions 6 小时强制超时。

**建议**：curl 加 `--max-time 60 --connect-timeout 10`，`subprocess.run` 加 `timeout=120` 兜底。这是本次审计最值得改的一条。

### 3.2 🟠 中高：`audit_rules.py` 对同一批上游抓取两遍

`check_upstream_reachability()`（`audit_rules.py:50-55`）与 `check_upstream_vs_generated()`（`:75-91`）各自对全部上游 URL 调一次 `fetch_text()`，每次审计产生约 2 倍的冗余 HTTP 请求，审计耗时接近翻倍，也加倍了对上游（GitHub raw、skk.moe）的请求压力。

**建议**：抓取一次并缓存 `{url: content}`，可达性检查用「content 是否为 None」判断，比例检查复用同一份内容。改动小、收益直接。

### 3.3 🟠 中：HTTP 客户端三套实现，行为不一致

| 位置 | 实现 | 超时 | 重试 |
|---|---|---|---|
| `generate_rules.py:217` | curl 子进程 | 无 | curl `--retry 3` |
| `check_upstream_updates.py:44-92` | `urllib.request` | 20s | 无 |
| `audit_rules.py:26` | `urllib` + `ssl` | 30s | 无 |

同一个上游在三个阶段可能表现出三种不同的失败方式，排障时难以对齐。**建议**：提取共享 `http_util.py`（统一超时、重试、UA），三处引用。

### 3.4 🟠 中：策略知识分散在三个文件，靠人工保持同步

「生成期变换 + 校验期检查」的两层设计本身是正确的纵深防御（不建议合并），但**策略常量**重复定义：

- `fast.com`、`github|ghcr.io` 等过滤正则写在 `generate_rules.py:120-127`，对应的校验逻辑又独立写在 `rule_validator.py` 中；
- 共享基础设施域名清单有两份：`SHARED_CDN_PARENTS`（`rule_validator.py:32`）与 `BROAD_SHARED_SUFFIXES`（`audit_rules.py:142` 起，注释说明是有意更宽的清单）。分级合理，但两份清单无引用关系，新增条目需记得改两处。

**建议**：新建 `scripts/policy.py`（或并入 `sources.py`）集中定义策略常量，分 `STRICT`/`BROAD` 两级，validator 与 audit 分别引用对应级别。

### 3.5 🟡 中低：CIDR supernet 冗余检测逻辑复制了两份

同一段「对每个网段枚举所有前缀长度查 supernet」的逻辑分别实现于 `generate_rules.py:193-199`（裁剪用）与 `rule_validator.py:251-258`（校验用）。

**说明**：两处都用 set 查找，复杂度为 O(n × 前缀长度)，**不是性能问题**（初步分析工具曾误报 O(n²)，已核实排除），纯属重复代码。**建议**：提取为共享函数；若顺手重构可改用标准库 `ipaddress.collapse_addresses()`，语义更清晰。

### 3.6 🟡 低：单个规则文件生成过程写盘三次

`process_rule()`（`generate_rules.py:263-292`）流程为：写盘 → `prune_redundant_cidr` 读回再写 → 读回校验 → 加头最终写。对 `China.list`（112k 行）即 3 写 2 读。实测量级仍是秒级，收益有限，仅在下次重构该函数时顺带改为内存中完成即可。

### 3.7 ✅ 无需处理

- `check_upstream_updates.py:39` `MAX_WORKERS = 8`：仅 11 个上游 URL / 37 个规则源，8 并发已充分，不必调整。
- `manifest.py` 的逐文件正则解析：文件数与规模下开销可忽略。

---

## 4. 次要章节：安全

- 🟡 **上游信任模型未成文**：`curl -fsSL` 直接信任 11 个上游（blackmatrix7 / SukkaW / Loyalsoldier / ConnersHua 等），无校验和 —— 对规则类内容这是行业常态，且 audit 的规则数比例检查已能发现大规模异常，风险可接受。**建议**只补文档：在 README 加一节「信任模型」，写明信任哪些上游、防线是什么（HTTPS + 比例审计 + manifest diff 人工可查）。
- ✅ **正面确认**：Actions 全部 SHA 固定（不建议改回浮动 tag）；workflow 权限最小化；dry-run 指纹验证门禁；仓库中无任何硬编码凭据。

---

## 5. 次要章节：CI 与仓库卫生

- 🟡 **git 历史长期膨胀**：`Rule/`（12MB）+ `clash/`（7.8MB）每日重生成提交。文本 delta 压缩下当前增速温和（建仓 20 天共 12.9MB），但年尺度可能达数百 MB。可选方案（按侵入性排序）：
  1. 暂不动，每季度看一次 repo size（当前完全可接受）；
  2. 生成物移入孤儿分支（如 `release`）每日 force-push，`main` 只留源码 —— Loyalsoldier/surge-rules 模式；**注意**这会改变所有 RULE-SET URL，对已有用户是破坏性变更，需公告过渡。
- 🟡 **产物混入源码目录**：`scripts/diff_report.md`、`diff_report.json`、`source_state.json` 是流水线产物/状态，建议移到独立的 `data/` 或 `.state/` 目录，`scripts/` 只留代码。
- 🔵 **提交路径硬编码**：`auto-rules.yml:217-218` 手写 `git add Rule/ clash/ Module/ ...`，与 `sources.py` 的规则集定义脱节；新增输出目录时需记得同步。低优先级。
- 🔵 **测试缺口**：`tests/expected-routing.csv` 77 个用例全部是域名路径，无 IP 规则、DOMAIN-WILDCARD 用例；`ios_privacy_to_surge.py`、`cross_file_conflicts.py`、`manifest.py --diff` 无自动化测试（CI 已覆盖语法校验 + Clash 校验 + 路由测试，基本盘是好的）。
- ✅ **无需处理**：monthly-review 的「28-31 号触发 + 判断明天是否 1 号」是 cron 不支持月末的标准解法，逻辑正确。

---

## 6. 优先级汇总

| 优先级 | 建议 | 位置 | 预估工作量 |
|:--:|---|---|:--:|
| 🔴 高 | curl 加 `--max-time` / subprocess 加 timeout | `generate_rules.py:217-222` | 10 分钟 |
| 🟠 中高 | audit 上游抓取合并为单遍 + 缓存 | `audit_rules.py:50-91` | 0.5 小时 |
| 🟠 中 | 策略常量集中到单一模块（分级） | `generate_rules.py` / `rule_validator.py:32` / `audit_rules.py:142` | 2 小时 |
| 🟠 中 | 统一 HTTP 客户端工具模块 | 三个脚本 | 2 小时 |
| 🟠 中 | 7 个跨文件死规则归属决策（exclude） | `Rule/Manual/*.exclude.txt` | 0.5 小时 |
| 🟡 中低 | 产物移出 `scripts/` 目录 | `scripts/` + `auto-rules.yml` | 1 小时 |
| 🟡 中低 | README 补：最低 Surge 版本、bootstrap 说明、信任模型 | `README.md` | 1 小时 |
| 🔵 低 | `hijack-dns = *:53`（先单设备验证） | `Linnux.conf:29` | 5 分钟 |
| 🔵 低 | `China_IP.list` 去掉无效的 `extended-matching` | `Linnux.conf:149` | 1 分钟 |
| 🔵 低 | CIDR supernet 逻辑合并为共享函数 | 两处 | 1 小时 |
| 🔵 低 | 补 IP/wildcard 路由测试用例与脚本单测 | `tests/` | 按需 |

## 7. 已核查为「无需处理」的项（避免无效改动）

1. **China.list 转 DOMAIN-SET**：Surge 5.8.1 起两者性能/内存无差异（官方发布说明），现状即最优。
2. **LAN 规则位置**：索引化后排序无性能影响，且与 China.list 同为 DIRECT，无语义差异。
3. **CIDR 检查 O(n²)**：误报，实际为 set 查找。
4. **状态回滚风险**：`.next.json` 提升机制已正确处理。
5. **monthly-review cron**：标准月末 workaround，正确。
6. **MAX_WORKERS 调优**：源数量下无收益。

---

*参考文档：[Surge iOS Release Notes（5.8.0 extended-matching / 5.8.1 规则集重写）](https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-ios) · [Surge Manual — Misc Options（hijack-dns）](https://manual.nssurge.com/others/misc-options.html) · [Surge Manual — Ruleset](https://manual.nssurge.com/rule/ruleset.html)*
