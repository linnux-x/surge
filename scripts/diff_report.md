# Surge Rule Diff Report
Generated: 2026-07-18T05:00:46.550070

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 25 |
| Rules removed | 33 |
| Source attribution changed | 13 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 111938 | 111948 | +10 | -0 | ~0 |
| China_IP.list | 11530 | 11507 | +10 | -33 | ~13 |
| Global.list | 24138 | 24143 | +5 | -0 | ~0 |

## China.list

**Added: 10** (showing first 10)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 0f0468b452f1  DOMAIN-SUFFIX,sdshdc.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 279f32bfa4ca  DOMAIN-SUFFIX,dczcy.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 4c330c986237  DOMAIN,api.blipsandchitz.me
  + [blackmatrix7 ChinaMaxNoIP Domain] 77d967076357  DOMAIN-SUFFIX,didifinance.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 7e8095a8f5e9  DOMAIN-SUFFIX,shicheng6.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 7ed6e38b3054  DOMAIN-SUFFIX,yxingfan.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 8f6a0f67aff6  DOMAIN-SUFFIX,ulongemg.com
  + [blackmatrix7 ChinaMaxNoIP Domain] a22de2fc6e19  DOMAIN-SUFFIX,jietianz.com
  + [blackmatrix7 ChinaMaxNoIP Domain] acb7c8ac00f4  DOMAIN-SUFFIX,hrsecn.com
  + [blackmatrix7 ChinaMaxNoIP Domain] e3503da9a673  DOMAIN-SUFFIX,fuchenkj.com
```

## China_IP.list

**Added: 10** (showing first 10)
```
  + [Loyalsoldier China CIDR] 395549457df8  IP-CIDR6,2a0f:6284:4c00::/44
  + [Loyalsoldier China CIDR] 44f50aa2b155  IP-CIDR6,2a0f:6280:1440::/43
  + [blackmatrix7 China IPs] 5ef4b802a92f  IP-CIDR,163.128.254.0/23
  + [Loyalsoldier China CIDR] 60ee77f765a7  IP-CIDR6,2a06:9f81:4620::/43
  + [Loyalsoldier China CIDR] 63d977e5e8d9  IP-CIDR6,2a0f:6280:1430::/44
  + [Loyalsoldier China CIDR] a138136ca45d  IP-CIDR6,2a0f:1cc5:f09::/48
  + [Loyalsoldier China CIDR] a9b1484ee3c8  IP-CIDR6,2a14:7586:6104::/47
  + [Loyalsoldier China CIDR] b38c3eb541d8  IP-CIDR6,2a0f:6280:1480::/44
  + [Loyalsoldier China CIDR] d386124aa910  IP-CIDR6,2a14:7586:6106::/48
  + [Loyalsoldier China CIDR] db69b4550bc7  IP-CIDR6,2a06:9f81:4600::/44
```

**Removed: 33** (showing first 33)
```
  - [blackmatrix7 China IPs] 04a0cf2c28ba  IP-CIDR,82.110.98.0/24
  - [blackmatrix7 China IPs] 0555710c3dc6  IP-CIDR6,2a0e:4005:ff41::/48
  - [blackmatrix7 China IPs] 170444d2dd94  IP-CIDR6,2a14:7586:6113::/48
  - [blackmatrix7 China IPs] 1d61b0407e6a  IP-CIDR,218.252.64.0/19
  - [blackmatrix7 China IPs] 24a6c8a6c42f  IP-CIDR,61.15.0.0/18
  - [blackmatrix7 China IPs] 352fa100e450  IP-CIDR,222.166.128.0/20
  - [blackmatrix7 China IPs] 3fc6be92d626  IP-CIDR,195.40.158.0/24
  - [blackmatrix7 China IPs] 4517c7447992  IP-CIDR6,2a06:9f81:4600::/42
  - [blackmatrix7 China IPs] 510cdef3330c  IP-CIDR,185.116.90.0/24
  - [blackmatrix7 China IPs] 51c3b5582a8c  IP-CIDR6,2a0e:aa07:e28d::/48
  - [blackmatrix7 China IPs] 5a2151112e6d  IP-CIDR,222.166.160.0/20
  - [blackmatrix7 China IPs] 63c2911f401d  IP-CIDR,222.166.224.0/19
  - [blackmatrix7 China IPs] 66b978cfb10b  IP-CIDR,222.166.208.0/20
  - [blackmatrix7 China IPs] 6a0bc4e16437  IP-CIDR6,2a07:54c1:2205::/48
  - [blackmatrix7 China IPs] 6a254dc81814  IP-CIDR,218.252.0.0/18
  - [blackmatrix7 China IPs] 6f475d7f2eba  IP-CIDR,82.38.92.0/24
  - [blackmatrix7 China IPs] 7afd957ba698  IP-CIDR,222.166.96.0/20
  - [blackmatrix7 China IPs] 84d2a438d31d  IP-CIDR,200.102.179.0/24
  - [blackmatrix7 China IPs] 8b5f09bf0e42  IP-CIDR,218.253.0.0/18
  - [blackmatrix7 China IPs] 912c156f4ceb  IP-CIDR6,2a0f:1cc5:f08::/47
  - [blackmatrix7 China IPs] a42586c93490  IP-CIDR,61.10.128.0/20
  - [blackmatrix7 China IPs] a9ad5a941e8d  IP-CIDR,191.44.18.0/24
  - [blackmatrix7 China IPs] adafe872bb28  IP-CIDR,78.154.108.0/24
  - [blackmatrix7 China IPs] b37393a84369  IP-CIDR,2.26.167.0/24
  - [blackmatrix7 China IPs] ba4856ba8818  IP-CIDR,65.86.204.0/24
  - [blackmatrix7 China IPs] bb52ec8766ce  IP-CIDR,61.10.160.0/19
  - [blackmatrix7 China IPs] bcbda6793b49  IP-CIDR,61.18.0.0/18
  - [blackmatrix7 China IPs] c6ca909bbee7  IP-CIDR,189.75.180.0/24
  - [blackmatrix7 China IPs] cc7fb4de1a1a  IP-CIDR6,2a14:7586:6104::/46
  - [blackmatrix7 China IPs] cf01a991e9dc  IP-CIDR,61.10.96.0/20
  - [blackmatrix7 China IPs] dae405619306  IP-CIDR,193.8.114.0/24
  - [blackmatrix7 China IPs] e6f10363842b  IP-CIDR6,2a0f:6284:4c00::/43
  - [blackmatrix7 China IPs] f46bf97ad540  IP-CIDR,72.244.62.0/24
```

**Source changed: 13**
```
  ~ 0ca56d06b721: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 60834f67a21e: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 803f98886454: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 18b938e005eb: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 5cd602ed46cd: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 8b72752a4841: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ b6a56606b608: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 4ed09acbf6ef: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ fd290490a422: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 6901b5602816: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 482b19d75997: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ 2134172f45c6: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
  ~ e72483c14908: [Loyalsoldier China CIDR → Rabbit-Spec China CIDR]
```

## Global.list

**Added: 5** (showing first 5)
```
  + [blackmatrix7 Global] 13381722149a  DOMAIN-SUFFIX,mhgui.com
  + [blackmatrix7 Global] 2054269d5933  DOMAIN-SUFFIX,netxh.blog
  + [blackmatrix7 Global] 466bf1edf7f3  DOMAIN-SUFFIX,starlink.com
  + [blackmatrix7 Global] 6efaf0014242  DOMAIN-SUFFIX,azureedge.us
  + [blackmatrix7 Global] d18d979d2495  DOMAIN-SUFFIX,copilot-stg.com
```
