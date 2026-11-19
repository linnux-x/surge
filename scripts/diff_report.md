# Surge Rule Diff Report
Generated: 2026-11-19T16:04:30.174052

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 10 |
| Rules removed | 20 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110644 | 110647 | +3 | -0 | ~0 |
| ChinaMedia.list | 384 | 377 | +5 | -12 | ~0 |
| WeChat.list | 101 | 95 | +2 | -8 | ~0 |

## China.list

**Added: 3** (showing first 3)
```
  + [SukkaW Domestic] 57c18cd172d4  DOMAIN-SUFFIX,qpic.cn
  + [blackmatrix7 ChinaMaxNoIP Domain] 58f514d5819b  DOMAIN-SUFFIX,tenpay.com
  + [SukkaW Domestic] c39fd4550951  DOMAIN-SUFFIX,qlogo.cn
```

## ChinaMedia.list

**Added: 5** (showing first 5)
```
  + [Manual Rules] 05655084f59f  USER-AGENT,bili/*
  + [Manual Rules] 0613fa6923a4  USER-AGENT,bilibili/*
  + [Manual Rules] 15f2255265b0  DOMAIN-SUFFIX,tv.sohu.com
  + [Manual Rules] 600e8946b9e4  DOMAIN,film.sohu.com
  + [Manual Rules] c84bdce232db  DOMAIN-SUFFIX,tv.itc.cn
```

**Removed: 12** (showing first 12)
```
  - [blackmatrix7 ChinaMedia] 164bfc51712a  DOMAIN-SUFFIX,ai.xiaomi.com
  - [blackmatrix7 ChinaMedia] 1f0cc8df5c73  IP-CIDR,119.176.0.0/12,no-resolve
  - [blackmatrix7 ChinaMedia] 3370db0c197b  DOMAIN-SUFFIX,sohu.com
  - [blackmatrix7 ChinaMedia] 45fe301bc5f3  IP-CIDR,119.29.29.29/32,no-resolve
  - [blackmatrix7 ChinaMedia] 62ba15eb1ea0  IP-CIDR,203.107.1.0/24,no-resolve
  - [blackmatrix7 ChinaMedia] 8616538bd7b8  USER-AGENT,bili*
  - [blackmatrix7 ChinaMedia] 91ee31d9657a  IP-CIDR,106.11.0.0/16,no-resolve
  - [blackmatrix7 ChinaMedia] a81023748e98  DOMAIN-SUFFIX,itc.cn
  - [blackmatrix7 ChinaMedia] abe5068276c8  USER-AGENT,bili-inter*
  - [blackmatrix7 ChinaMedia] b10b1ff58a4c  USER-AGENT,*bili*
  - [blackmatrix7 ChinaMedia] bdd954ae4546  IP-CIDR,101.224.0.0/13,no-resolve
  - [blackmatrix7 ChinaMedia] c1364709d93b  DOMAIN-SUFFIX,sohu.com.cn
```

## WeChat.list

**Added: 2** (showing first 2)
```
  + [Manual Rules] 88418904b4c7  DOMAIN,mmbiz.qpic.cn
  + [Manual Rules] d7c6e4c3484e  DOMAIN,wx.qlogo.cn
```

**Removed: 8** (showing first 8)
```
  - [blackmatrix7 WeChat] 0f3870166843  DOMAIN-SUFFIX,map.qq.com
  - [blackmatrix7 WeChat] 178a77dbe9d2  IP-ASN,132203,no-resolve
  - [blackmatrix7 WeChat] 57c18cd172d4  DOMAIN-SUFFIX,qpic.cn
  - [blackmatrix7 WeChat] 58f514d5819b  DOMAIN-SUFFIX,tenpay.com
  - [blackmatrix7 WeChat] 9a03a6d9bb6f  DOMAIN-SUFFIX,lbs.gtimg.com
  - [blackmatrix7 WeChat] c39fd4550951  DOMAIN-SUFFIX,qlogo.cn
  - [blackmatrix7 WeChat] cc33162af915  USER-AGENT,WeChat*
  - [blackmatrix7 WeChat] fed261f41a71  USER-AGENT,MicroMessenger*
```
