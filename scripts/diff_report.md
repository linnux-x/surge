# Surge Rule Diff Report
Generated: 2026-07-11T05:01:11.045513

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 33 |
| Rules removed | 8 |
| Source attribution changed | 24 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 138 | 139 | +1 | -0 | ~0 |
| China.list | 112187 | 112190 | +3 | -0 | ~0 |
| China_IP.list | 11428 | 11444 | +22 | -6 | ~24 |
| Global.list | 24099 | 24105 | +6 | -0 | ~0 |
| Microsoft_CDN.list | 84 | 83 | +1 | -2 | ~0 |

## AI.list

**Added: 1** (showing first 1)
```
  + [Rabbit-Spec AIGC] 4f9b7a9bf580  DOMAIN-SUFFIX,aicode.googleapis.com
```

## China.list

**Added: 3** (showing first 3)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 43bb94bb631d  DOMAIN-SUFFIX,zx.com
  + [Rabbit-Spec China] 6b332785cbec  DOMAIN-KEYWORD,sleep.pokemon
  + [blackmatrix7 ChinaMaxNoIP Domain] 81408f8fdbce  DOMAIN-SUFFIX,twyxh.com
```

## China_IP.list

**Added: 22** (showing first 22)
```
  + [Loyalsoldier China CIDR] 0fd0ee531860  IP-CIDR6,2a0f:6284:4cc0::/43
  + [Loyalsoldier China CIDR] 10548dcf6a08  IP-CIDR6,2a0f:6284:4c40::/43
  + [Loyalsoldier China CIDR] 445ac4821895  IP-CIDR,44.30.164.0/24
  + [Loyalsoldier China CIDR] 4517c7447992  IP-CIDR6,2a06:9f81:4600::/42
  + [Loyalsoldier China CIDR] 4ff5e77db84a  IP-CIDR6,2a14:7586:6500::/48
  + [Loyalsoldier China CIDR] 5124585b460f  IP-CIDR6,2a0f:6284:4c20::/44
  + [Loyalsoldier China CIDR] 570b05465d58  IP-CIDR6,2a0f:1cc6:b210::/47
  + [Loyalsoldier China CIDR] 586a51d4d47a  IP-CIDR,216.75.141.0/24
  + [Loyalsoldier China CIDR] 7122733ade2a  IP-CIDR6,2a0e:aa07:e288::/46
  + [Loyalsoldier China CIDR] 82ad764e5788  IP-CIDR6,2a0f:6284:4ca0::/44
  + [Loyalsoldier China CIDR] 84d2a438d31d  IP-CIDR,200.102.179.0/24
  + [Loyalsoldier China CIDR] a5356e4e1807  IP-CIDR6,2a0f:6284:4c80::/43
  + [Loyalsoldier China CIDR] beca888da6cb  IP-CIDR6,2a14:67c3:30::/44
  + [Loyalsoldier China CIDR] c580b30f3dd4  IP-CIDR6,2a13:aac4:f000::/44
  + [Loyalsoldier China CIDR] c6ca909bbee7  IP-CIDR,189.75.180.0/24
  + [Loyalsoldier China CIDR] d2f421260b87  IP-CIDR6,2a06:9f81:4660::/44
  + [Loyalsoldier China CIDR] d9c0538a8f92  IP-CIDR6,2a0f:6284:4c30::/48
  + [Loyalsoldier China CIDR] da06aad6bd37  IP-CIDR6,2a0f:1cc6:b212::/48
  + [Loyalsoldier China CIDR] e251767d9e79  IP-CIDR6,2a06:9f81:4640::/43
  + [Loyalsoldier China CIDR] e6f10363842b  IP-CIDR6,2a0f:6284:4c00::/43
  + [Loyalsoldier China CIDR] f46bf97ad540  IP-CIDR,72.244.62.0/24
  + [Loyalsoldier China CIDR] f49e0740abf9  IP-CIDR6,2a0f:6284:4c60::/44
```

**Removed: 6** (showing first 6)
```
  - [blackmatrix7 China IPs] 1c5022e9e384  IP-CIDR6,2a13:aac4:f009::/48
  - [blackmatrix7 China IPs] 4156e5116947  IP-CIDR6,2a13:aac4:f00a::/47
  - [Loyalsoldier China CIDR] 807d623ef3c1  IP-CIDR6,2a0e:aa07:e28a::/48
  - [blackmatrix7 China IPs] 970b4a8697b4  IP-CIDR6,2a13:aac4:f000::/45
  - [blackmatrix7 China IPs] c58e7f64814d  IP-CIDR6,2a13:aac4:f00c::/48
  - [Loyalsoldier China CIDR] c9822e9b5541  IP-CIDR6,2a0e:aa07:e288::/47
```

**Source changed: 24**
```
  ~ 1fe54f8b0361: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 260cd8bdce17: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ a181936defc2: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 51f1ab9b30cf: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 95e2f5a5da41: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ a538d9e7475d: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ e8306b6d34b4: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7da0bc281438: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ cf1359620869: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ ee86a9b14b09: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 172ed5fc53f9: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 475ffd418052: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 5ffad8d39de9: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ b2c71fe21b40: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 5678db0017cc: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 90538aa62153: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 134c1a95eed8: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 3277d45b5692: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 16927a0ce817: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ a97fd095f5f9: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ a63fdaffe832: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ e9a6f5e29764: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ de1e716e741c: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 80b46e8940fc: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Global.list

**Added: 6** (showing first 6)
```
  + [blackmatrix7 Global] 028f36ba4e84  DOMAIN-SUFFIX,funpay.ru
  + [blackmatrix7 Global] 2e587452ce92  DOMAIN-SUFFIX,funpay.com
  + [blackmatrix7 Global] 632e34e23470  DOMAIN-SUFFIX,sfunpay.com
  + [blackmatrix7 Global] ac46b5658776  DOMAIN-SUFFIX,tildacdn.net
  + [blackmatrix7 Global] f5d1ee5d1971  DOMAIN-SUFFIX,flowwow.com
  + [blackmatrix7 Global] f79261cd8675  DOMAIN-SUFFIX,flowwow-images.com
```

## Microsoft_CDN.list

**Added: 1** (showing first 1)
```
  + [SukkaW Microsoft CDN] 768ec1e63e2c  DOMAIN,statics.teams.cdn.office.net
```

**Removed: 2** (showing first 2)
```
  - [SukkaW Microsoft CDN] 9cfc6a93e23d  DOMAIN-SUFFIX,storeedgefd.dsx.mp.microsoft.com
  - [SukkaW Microsoft CDN] b9c9f91ee318  DOMAIN-SUFFIX,statics.teams.cdn.office.net
```
