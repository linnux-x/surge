# Surge Rule Diff Report
Generated: 2026-11-23T08:25:29.993094

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 6 |
| Rules added | 17 |
| Rules removed | 19 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 561 | 562 | +1 | -0 | ~1 |
| China.list | 110664 | 110661 | +0 | -3 | ~0 |
| ChinaMedia.list | 344 | 343 | +0 | -1 | ~0 |
| Global.list | 24635 | 24648 | +13 | -0 | ~0 |
| GlobalMedia.list | 2162 | 2158 | +3 | -7 | ~0 |
| SocialMedia.list | 671 | 663 | +0 | -8 | ~0 |

## AI.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 3f22cbdc0d9c  DOMAIN,ai.meta.com
```

**Source changed: 1**
```
  ~ 4dad2df0bf10: [SukkaW AI → Manual Rules]
```

## China.list

**Removed: 3** (showing first 3)
```
  - [SukkaW Domestic] 1e2dbaff18e5  USER-AGENT,TeslaMap
  - [SukkaW Domestic] 359cc6c5c715  USER-AGENT,%E4%BC%98%E9%85%B7*
  - [SukkaW Domestic] 4ef1969d7902  USER-AGENT,%E6%89%8B%E6%9C%BA%E6%B7%98%E5%AE%9D*
```

## ChinaMedia.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 ChinaMedia] 6f6f8f376d3d  IP-CIDR,23.211.15.99/32,no-resolve
```

## Global.list

**Added: 13** (showing first 13)
```
  + [Manual Rules] 05332accf4b6  IP-CIDR,54.235.23.242/32,no-resolve
  + [Manual Rules] 236d8663dc39  DOMAIN-SUFFIX,kakaocorp.com
  + [Manual Rules] 28b4c827d811  DOMAIN-SUFFIX,kakao.com
  + [Manual Rules] 393693fb8365  DOMAIN-SUFFIX,kakao.co.kr
  + [Manual Rules] 4929ba7060c0  IP-CIDR,35.157.217.255/32,no-resolve
  + [Manual Rules] 5c7e313f6444  DOMAIN-SUFFIX,daum.net
  + [Manual Rules] 5ce134845213  DOMAIN-SUFFIX,naver.com
  + [Manual Rules] 616b5d77c5a7  IP-CIDR,3.123.36.126/32,no-resolve
  + [Manual Rules] 7495e2303c7c  IP-CIDR,54.162.243.80/32,no-resolve
  + [Manual Rules] 777be6a67e2e  IP-CIDR,23.211.15.0/24,no-resolve
  + [Manual Rules] 96ae53d4e98b  DOMAIN-SUFFIX,daumkakao.io
  + [Manual Rules] b2b2431dd384  IP-CIDR,54.173.34.141/32,no-resolve
  + [Manual Rules] fcc2a23cad15  IP-CIDR,35.157.215.84/32,no-resolve
```

## GlobalMedia.list

**Added: 3** (showing first 3)
```
  + [Manual Rules] 58185bf7a239  DOMAIN-SUFFIX,tv.kakao.com
  + [Manual Rules] 9dcabe745a4c  DOMAIN-SUFFIX,tv.naver.com
  + [Manual Rules] d89f5c57600e  DOMAIN-SUFFIX,chzzk.naver.com
```

**Removed: 7** (showing first 7)
```
  - [blackmatrix7 GlobalMedia] 236d8663dc39  DOMAIN-SUFFIX,kakaocorp.com
  - [blackmatrix7 GlobalMedia] 28b4c827d811  DOMAIN-SUFFIX,kakao.com
  - [blackmatrix7 GlobalMedia] 393693fb8365  DOMAIN-SUFFIX,kakao.co.kr
  - [blackmatrix7 GlobalMedia] 5c7e313f6444  DOMAIN-SUFFIX,daum.net
  - [blackmatrix7 GlobalMedia] 5ce134845213  DOMAIN-SUFFIX,naver.com
  - [blackmatrix7 GlobalMedia] 777be6a67e2e  IP-CIDR,23.211.15.0/24,no-resolve
  - [blackmatrix7 GlobalMedia] 96ae53d4e98b  DOMAIN-SUFFIX,daumkakao.io
```

## SocialMedia.list

**Removed: 8** (showing first 8)
```
  - [blackmatrix7 Facebook] 05332accf4b6  IP-CIDR,54.235.23.242/32,no-resolve
  - [blackmatrix7 Facebook] 4929ba7060c0  IP-CIDR,35.157.217.255/32,no-resolve
  - [blackmatrix7 Facebook] 616b5d77c5a7  IP-CIDR,3.123.36.126/32,no-resolve
  - [blackmatrix7 Facebook] 7495e2303c7c  IP-CIDR,54.162.243.80/32,no-resolve
  - [blackmatrix7 Facebook] 8977a1c28e3f  IP-CIDR,52.58.209.134/32,no-resolve
  - [blackmatrix7 Facebook] b2b2431dd384  IP-CIDR,54.173.34.141/32,no-resolve
  - [blackmatrix7 Facebook] fa92f0ef44ac  IP-CIDR,54.93.124.31/32,no-resolve
  - [blackmatrix7 Facebook] fcc2a23cad15  IP-CIDR,35.157.215.84/32,no-resolve
```
