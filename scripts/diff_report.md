# Surge Rule Diff Report
Generated: 2026-06-23T20:07:12.527137

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 7 |
| Rules added | 21 |
| Rules removed | 68 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Apple.list | 1549 | 1548 | +0 | -1 | ~0 |
| China.list | 112664 | 112611 | +11 | -64 | ~0 |
| China_IP.list | 11426 | 11431 | +6 | -1 | ~0 |
| Download.list | 1684 | 1686 | +2 | -0 | ~0 |
| Global.list | 29430 | 29432 | +2 | -0 | ~0 |
| Netflix.list | 1154 | 1153 | +0 | -1 | ~0 |
| SocialMedia.list | 918 | 917 | +0 | -1 | ~0 |

## Apple.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Apple] a4082dfd38b1
```

## China.list

**Added: 11** (showing first 11)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 04cfed5d04aa
  + [blackmatrix7 ChinaMaxNoIP Domain] 1aae3f5fc16d
  + [blackmatrix7 ChinaMaxNoIP Domain] 260e85388363
  + [blackmatrix7 ChinaMaxNoIP Domain] 5394da999e0c
  + [blackmatrix7 ChinaMaxNoIP Domain] 5b97c461bc02
  + [blackmatrix7 ChinaMaxNoIP Domain] 6358d7f06b8f
  + [blackmatrix7 ChinaMaxNoIP Domain] a4f3f3c9f347
  + [blackmatrix7 ChinaMaxNoIP Domain] c1539dd0515f
  + [blackmatrix7 ChinaMaxNoIP Domain] cd9dc6a2d50e
  + [blackmatrix7 ChinaMaxNoIP Domain] f5e6bb972aa3
  + [blackmatrix7 ChinaMaxNoIP Domain] f9ef12a34882
```

**Removed: 64** (showing first 64)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 069c2d52bdc9
  - [blackmatrix7 ChinaMaxNoIP Domain] 0a7ce45ca5a7
  - [blackmatrix7 ChinaMaxNoIP Domain] 0c1dd6a92b33
  - [blackmatrix7 ChinaMaxNoIP Domain] 15cf88540f25
  - [blackmatrix7 ChinaMaxNoIP Domain] 182dae80575b
  - [blackmatrix7 ChinaMaxNoIP Domain] 20dd0d67de72
  - [blackmatrix7 ChinaMaxNoIP Domain] 22a0cec395fa
  - [blackmatrix7 ChinaMaxNoIP Domain] 22d74accffde
  - [blackmatrix7 ChinaMaxNoIP Domain] 27df5354eb84
  - [blackmatrix7 ChinaMaxNoIP Domain] 28777417c657
  - [blackmatrix7 ChinaMaxNoIP Domain] 2d09ff8c1bf0
  - [blackmatrix7 ChinaMaxNoIP Domain] 309e66020d70
  - [blackmatrix7 ChinaMaxNoIP Domain] 3207997344a8
  - [blackmatrix7 ChinaMaxNoIP Domain] 36a8b7cf6056
  - [blackmatrix7 ChinaMaxNoIP Domain] 3bd4f077a092
  - [blackmatrix7 ChinaMaxNoIP Domain] 3c9b8eb7a4ca
  - [blackmatrix7 ChinaMaxNoIP Domain] 42bb4d13f49d
  - [blackmatrix7 ChinaMaxNoIP Domain] 432b985fc5f6
  - [blackmatrix7 ChinaMaxNoIP Domain] 4653fe60fcda
  - [blackmatrix7 ChinaMaxNoIP Domain] 55a60b2b99c8
  - [blackmatrix7 ChinaMaxNoIP Domain] 592b96de76bd
  - [blackmatrix7 ChinaMaxNoIP Domain] 604fdabe1194
  - [blackmatrix7 ChinaMaxNoIP Domain] 607b9b9622bf
  - [blackmatrix7 ChinaMaxNoIP Domain] 6083d7f74797
  - [blackmatrix7 ChinaMaxNoIP Domain] 6f4bea642d9f
  - [blackmatrix7 ChinaMaxNoIP Domain] 7068b2e526bf
  - [blackmatrix7 ChinaMaxNoIP Domain] 70738ea3c60c
  - [blackmatrix7 ChinaMaxNoIP Domain] 7a6c6c208f02
  - [blackmatrix7 ChinaMaxNoIP Domain] 7cdfec1d3895
  - [blackmatrix7 ChinaMaxNoIP Domain] 809bf73fdcfd
  - [blackmatrix7 ChinaMaxNoIP Domain] 85fff1372e25
  - [blackmatrix7 ChinaMaxNoIP Domain] 91a43700d489
  - [blackmatrix7 ChinaMaxNoIP Domain] 940a885a6aa0
  - [blackmatrix7 ChinaMaxNoIP Domain] 96f105c354d2
  - [blackmatrix7 ChinaMaxNoIP Domain] 9a52bdfe451d
  - [blackmatrix7 ChinaMaxNoIP Domain] a0c0cfd21101
  - [blackmatrix7 ChinaMaxNoIP Domain] a3720a23eff8
  - [blackmatrix7 ChinaMaxNoIP Domain] a91121670962
  - [blackmatrix7 ChinaMaxNoIP Domain] a946b908eca7
  - [blackmatrix7 ChinaMaxNoIP Domain] acc0cc6bfc58
  - [blackmatrix7 ChinaMaxNoIP Domain] ad994e30bd58
  - [blackmatrix7 ChinaMaxNoIP Domain] b76ccaaf6d14
  - [blackmatrix7 ChinaMaxNoIP Domain] c3d2451f8882
  - [blackmatrix7 ChinaMaxNoIP Domain] c7cd11f592dd
  - [blackmatrix7 ChinaMaxNoIP Domain] cad79379a27d
  - [blackmatrix7 ChinaMaxNoIP Domain] ccaf321af0b8
  - [blackmatrix7 ChinaMaxNoIP Domain] cdaf3ee2cd96
  - [blackmatrix7 ChinaMaxNoIP Domain] ce56358c0a0f
  - [blackmatrix7 ChinaMaxNoIP Domain] cffb11c64e55
  - [blackmatrix7 ChinaMaxNoIP Domain] d0ee16c8586f
  - [blackmatrix7 ChinaMaxNoIP Domain] d8a39be4f93d
  - [blackmatrix7 ChinaMaxNoIP Domain] da7fcf7806b1
  - [blackmatrix7 ChinaMaxNoIP Domain] daae3e39a59a
  - [blackmatrix7 ChinaMaxNoIP Domain] de13dc9230de
  - [blackmatrix7 ChinaMaxNoIP Domain] e098dd932ece
  - [blackmatrix7 ChinaMaxNoIP Domain] e2f1d3cd8c3a
  - [blackmatrix7 ChinaMaxNoIP Domain] e45b73164951
  - [blackmatrix7 ChinaMaxNoIP Domain] eb72cce31de9
  - [blackmatrix7 ChinaMaxNoIP Domain] f4c2da27eeb0
  - [blackmatrix7 ChinaMaxNoIP Domain] f6a6dd8e8299
  - [blackmatrix7 ChinaMaxNoIP Domain] f9a3b5720075
  - [blackmatrix7 ChinaMaxNoIP Domain] fa91bc2bcd79
  - [blackmatrix7 ChinaMaxNoIP Domain] fda6acd44458
  - [blackmatrix7 ChinaMaxNoIP Domain] fef5110deaeb
```

## China_IP.list

**Added: 6** (showing first 6)
```
  + [blackmatrix7 China IPs] 5a2151112e6d
  + [blackmatrix7 China IPs] 7afd957ba698
  + [blackmatrix7 China IPs] a9a0a5b2c5b6
  + [blackmatrix7 China IPs] bb52ec8766ce
  + [blackmatrix7 China IPs] ceacd0d92ea8
  + [blackmatrix7 China IPs] f78bcec0ccf3
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 China IPs] 4efacf093591
```

## Download.list

**Added: 2** (showing first 2)
```
  + [SukkaW Download] 418fced0daec
  + [SukkaW Download] af2d32761982
```

## Global.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 Global] 721b15bb1465
  + [blackmatrix7 Global] b857683709e4
```

## Netflix.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Netflix] b7fdea40fb16
```

## SocialMedia.list

**Removed: 1** (showing first 1)
```
  - [QuixoticHeart SocialMedia] 761a7e8bb386
```
