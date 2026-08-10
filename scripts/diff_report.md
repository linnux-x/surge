# Surge Rule Diff Report
Generated: 2026-08-10T23:05:39.933533

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 10 |
| Rules removed | 7 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Apple_AI.list | 17 | 18 | +1 | -0 | ~0 |
| CDN.list | 29 | 31 | +2 | -0 | ~0 |
| China.list | 111440 | 111441 | +1 | -0 | ~1 |
| China_IP.list | 11506 | 11508 | +3 | -1 | ~0 |
| Download.list | 1688 | 1685 | +3 | -6 | ~0 |

## Apple_AI.list

**Added: 1** (showing first 1)
```
  + [RocM301 Apple-AI] a9765c10ff5e  DOMAIN-KEYWORD,siri
```

## CDN.list

**Added: 2** (showing first 2)
```
  + [SukkaW CDN] 3ad31346eb51  DOMAIN-WILDCARD,cdn.*.dmm.co.jp
  + [SukkaW CDN] 840292ed5b7e  DOMAIN-KEYWORD,-assets.dmm.co.jp
```

## China.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 8e212fff64ee  DOMAIN-SUFFIX,lifexue.com
```

**Source changed: 1**
```
  ~ b0587cd1a358: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
```

## China_IP.list

**Added: 3** (showing first 3)
```
  + [blackmatrix7 China IPs] 3749d17bf657  IP-CIDR,166.1.232.0/24
  + [blackmatrix7 China IPs] 6883c0947707  IP-CIDR,166.1.218.0/24
  + [blackmatrix7 China IPs] bcf2575de367  IP-CIDR,166.1.139.0/24
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 China IPs] eacf5978ca7b  IP-CIDR,136.0.34.0/24
```

## Download.list

**Added: 3** (showing first 3)
```
  + [SukkaW Download] b14484db25d5  DOMAIN-SUFFIX,s3.yandex.net
  + [SukkaW Download] da4bd1f5bd7c  DOMAIN,download.fcitx-im.org
  + [SukkaW Download] f37733851efc  DOMAIN,dl.pikpak.io
```

**Removed: 6** (showing first 6)
```
  - [SukkaW Download] 59dda76bf44a  DOMAIN,mirror1.hcgen.de
  - [SukkaW Download] 6883ff8f2214  DOMAIN,edge.zerofs.link
  - [SukkaW Download] b54ce40390ca  DOMAIN,mirrors.wikimedia.org
  - [SukkaW Download] c6452d37d723  DOMAIN,mirror.hyperdedic.ru
  - [SukkaW Download] d7e51cb83152  DOMAIN,ubuntu.syxpi.fr
  - [SukkaW Download] fa0b3ab4c66b  DOMAIN,download.nus.edu.sg
```
