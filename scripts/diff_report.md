# Surge Rule Diff Report
Generated: 2026-07-19T05:00:54.084312

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 6 |
| Rules removed | 14 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 140 | 143 | +3 | -0 | ~0 |
| China_IP.list | 11507 | 11497 | +3 | -13 | ~0 |
| Global.list | 24143 | 24142 | +0 | -1 | ~0 |

## AI.list

**Added: 3** (showing first 3)
```
  + [Rabbit-Spec AIGC] af656b6ca087  DOMAIN-SUFFIX,pool.ntp.org
  + [Rabbit-Spec AIGC] b5ea3a4fb747  IP-ASN,13335,no-resolve
  + [Rabbit-Spec AIGC] d2b9889587fc  DOMAIN-SUFFIX,api.revenuecat.com
```

## China_IP.list

**Added: 3** (showing first 3)
```
  + [Loyalsoldier China CIDR] 21983b47abd4  IP-CIDR6,2a0f:1cc5:140::/43
  + [Loyalsoldier China CIDR] be94217b9581  IP-CIDR6,2a0f:1cc5:160::/44
  + [Loyalsoldier China CIDR] fb60fe8cca5f  IP-CIDR6,2a14:67c1:b589::/48
```

**Removed: 13** (showing first 13)
```
  - [Rabbit-Spec China CIDR] 0ca56d06b721  IP-CIDR6,2400:e3e0:abf1::/48
  - [Rabbit-Spec China CIDR] 18b938e005eb  IP-CIDR6,2400:e3e0:aa00::/40
  - [Rabbit-Spec China CIDR] 2134172f45c6  IP-CIDR6,2400:e3e0:abe0::/44
  - [Rabbit-Spec China CIDR] 482b19d75997  IP-CIDR6,2a14:67c1:b588::/47
  - [Rabbit-Spec China CIDR] 4ed09acbf6ef  IP-CIDR6,2400:e3e0:ab80::/42
  - [Rabbit-Spec China CIDR] 5cd602ed46cd  IP-CIDR6,2a14:c380:21::/48
  - [Rabbit-Spec China CIDR] 60834f67a21e  IP-CIDR6,2400:e3e0:abf8::/45
  - [Rabbit-Spec China CIDR] 6901b5602816  IP-CIDR6,2400:e3e0:abc0::/43
  - [Rabbit-Spec China CIDR] 803f98886454  IP-CIDR6,2400:e3e0:abf2::/47
  - [Rabbit-Spec China CIDR] 8b72752a4841  IP-CIDR6,2400:e3e0:ab00::/41
  - [Rabbit-Spec China CIDR] b6a56606b608  IP-CIDR6,2400:e3e0:abf4::/46
  - [Rabbit-Spec China CIDR] e72483c14908  IP-CIDR6,2a0f:7802:e100::/46
  - [Rabbit-Spec China CIDR] fd290490a422  IP-CIDR6,2a0f:1cc5:140::/42
```

## Global.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Global] af656b6ca087  DOMAIN-SUFFIX,pool.ntp.org
```
