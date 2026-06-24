# Upstream Repository Analysis: ConnersHua & SukkaW

Analysis performed 2026-06-24 comparing linnux-x/surge against two upstream
repository designs. Summary of what was learned and what was adopted.

## ConnersHua/RuleGo

Repository: <https://github.com/ConnersHua/RuleGo>
Last active: Apr 2026 (Reject), Jul 2025 (Direct+)

### Design Philosophy

ConnersHua uses a **layered policy approach**:

```
Direct.list   = rigid direct (email/PayPal/Steam/system updates — break if proxied)
Direct+.list  = flexible direct (analytics/tracking/telemetry — direct OR reject)
Proxy.list    = broad proxy aggregation (~200 domains)
Proxy+.list   = single GEOIP rule: GEOIP,GOOGLE
```

### Key Insight: GEOIP,GOOGLE

`Proxy+.list` contains exactly ONE line: `GEOIP,GOOGLE`. This matches all
Google ASN IP ranges and routes them through the proxy — a clever fallback
that avoids maintaining thousands of Google domain rules. We adopted this
in `Rule/Manual/Google.txt` (2026-06-24).

### Valuable Rulesets (not yet adopted)

| File | Content | Status |
|------|---------|--------|
| `Crypto.list` | 25 crypto exchanges (Binance/OKX/Bybit/Coinbase/Kraken) | Not yet created in our repo |
| `Scholar.list` | 63 academic databases (Nature/Science/Elsevier/IEEE/Springer) | Not yet created in our repo |
| `GeoLoc.list` | 10 Chinese platform geolocation APIs | Domains should go into `China.list` |
| `AI.list` | AI services — already integrated into our workflow | ✅ Active upstream |
| `Reject/` | Ad/tracking blocking — mobile users prefer dedicated blockers | Not adopted |

### Already Covered

- `Direct.list`: 82% covered by our existing rules (China/Microsoft/PayPal/Download)
- `Proxy.list`: Overlaps with our `Global.list` from blackmatrix7
- `Telegram/PayPal/WeChat/X`: Already have dedicated rulesets

## SukkaW/Surge

Repository: <https://github.com/SukkaW/Surge>
Stars: 4.2k · Maintained actively (last update Jun 2026)

### Architecture

```
Source/
├── non_ip/       (domain rules, .conf format)
│   ├── ai.conf, apple_cn.conf, apple_intelligence.conf, apple_services.conf
│   ├── cdn.conf, global.conf, domestic.conf
│   ├── download.conf, direct.conf
│   ├── microsoft.conf, telegram.conf, gitlab.conf
│   ├── reject.conf, reject-drop.conf, reject-no-drop.conf
│   └── my_direct.conf, my_proxy.conf, my_reject.conf ... (personal overrides)
├── domainset/    (DOMAIN-SET format)
│   ├── cdn.conf, download.conf, game-download.conf
│   ├── reject.conf, reject_extra.conf, speedtest.conf
│   └── icloud_private_relay.conf
└── ip/           (IP rules)
```

### Key Insight: `my_*.conf` Personal Overlay Pattern

SukkaW maintains personal override files (`my_direct.conf`, `my_proxy.conf`,
`my_reject.conf`) that sit ON TOP of the general rules without modifying
upstream sources. This is a cleaner version of the `Rule/Manual/*.txt`
pattern we already use.

### game-download.conf Coverage

All 46 domains in SukkaW's `game-download.conf` are already covered by our
`Download.list` (1702 rules). No adoption needed.

### SukkaW Rules Already Integrated

Most SukkaW `non_ip/*.conf` files are already upstream sources in our workflow:
- `ai.conf` → `AI.list`
- `apple_cn.conf` → `Apple_CN.list`
- `cdn.conf` → `CDN.list`
- `domestic.conf` → `China.list`
- `download.conf` → `Download.list`
- `microsoft.conf` → `Microsoft.list`
- `telegram.conf` → `Telegram.list`
- `speedtest.conf` → `Speedtest.list`
- `global.conf` → `Global.list`
