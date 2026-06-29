# Surge Rule Diff Report
Generated: 2026-06-29T23:09:40.698373

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 2 |
| Rules added | 82 |
| Rules removed | 40 |
| Source attribution changed | 240 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 112523 | 112566 | +82 | -39 | ~240 |
| GlobalMedia.list | 2272 | 2271 | +0 | -1 | ~0 |

## China.list

**Added: 82** (showing first 82)
```
  + [Manual Rules] 01ad27c8a689
  + [Manual Rules] 07e3a48db7e7
  + [Manual Rules] 0ba27ecb6c7f
  + [SukkaW Domestic] 100bc655efc2
  + [Manual Rules] 12a4a7de68e3
  + [Manual Rules] 1425e4f5b9e1
  + [SukkaW Domestic] 159b44e9f0aa
  + [SukkaW Domestic] 16cc277d84fa
  + [Manual Rules] 17730cc28d93
  + [SukkaW Domestic] 18062c5676bb
  + [SukkaW Domestic] 1a6f38dda773
  + [SukkaW Domestic] 1f3c75a70129
  + [SukkaW Domestic] 22901d154dc4
  + [Manual Rules] 237cf7c6a88e
  + [SukkaW Domestic] 2396c63fb39b
  + [Manual Rules] 24f5b65de060
  + [Manual Rules] 27e4a30640ad
  + [Manual Rules] 296bbad54385
  + [SukkaW Domestic] 2a0407accef4
  + [Manual Rules] 301053938a7d
  + [SukkaW Domestic] 3719202d0bd4
  + [Manual Rules] 374d6669518d
  + [Manual Rules] 3c29272ccccf
  + [SukkaW Domestic] 3cb27c1b3ebb
  + [Manual Rules] 3dab2086eb1c
  + [SukkaW Domestic] 3e20897b7037
  + [SukkaW Domestic] 49db13626e35
  + [SukkaW Domestic] 4bba20231d75
  + [Manual Rules] 4cf86824fc0e
  + [SukkaW Domestic] 4fd400c5aefa
  + [SukkaW Domestic] 51fd192a6c33
  + [SukkaW Domestic] 57a6ccb1c23e
  + [SukkaW Domestic] 5d6e4bd4f479
  + [SukkaW Domestic] 5d8836c4372e
  + [Manual Rules] 5d9406e49e89
  + [SukkaW Domestic] 62445e745303
  + [Manual Rules] 628e67079edd
  + [Manual Rules] 64111722672f
  + [Manual Rules] 645ab8f37f1b
  + [Manual Rules] 67381c4973b1
  + [SukkaW Domestic] 68296be188e3
  + [SukkaW Domestic] 68c35110f3f0
  + [Manual Rules] 68d25090d494
  + [SukkaW Domestic] 6a5834f25379
  + [SukkaW Domestic] 6affc1cfc706
  + [Manual Rules] 72fe7175eaf0
  + [SukkaW Domestic] 7a86d54ad9e0
  + [Manual Rules] 7a88492568c1
  + [SukkaW Domestic] 8d15ebe356c9
  + [SukkaW Domestic] 8e5f1563a836
  + [SukkaW Domestic] 90d235a1a4da
  + [Manual Rules] 926924e31ba8
  + [Manual Rules] 959544495d73
  + [SukkaW Domestic] 964786a7afb4
  + [Manual Rules] 965cbe8138ba
  + [SukkaW Domestic] 9fb89ed13f40
  + [SukkaW Domestic] a78e576065c9
  + [SukkaW Domestic] a9f1cf9bd8f7
  + [SukkaW Domestic] ad174688268f
  + [SukkaW Domestic] b172209cb77b
  + [SukkaW Domestic] bedbf9a40b11
  + [Manual Rules] bef1502ef171
  + [Manual Rules] c0c26faaf575
  + [Manual Rules] c10278cee389
  + [Manual Rules] c137b1cda156
  + [Manual Rules] c45cd60e3dab
  + [SukkaW Domestic] c9a6d3c659f8
  + [SukkaW Domestic] cdc9d268abe4
  + [Manual Rules] d6847d557a10
  + [SukkaW Domestic] d705eb04fed4
  + [SukkaW Domestic] d80df310b09a
  + [SukkaW Domestic] df944e43aacb
  + [Manual Rules] dfada6a8c7df
  + [SukkaW Domestic] e45f65ab0cff
  + [SukkaW Domestic] e6c1cfd2cc32
  + [Manual Rules] eb2b9efc3f4a
  + [SukkaW Domestic] f1d42620023f
  + [Manual Rules] f32ea29281c2
  + [Manual Rules] f63ece95e664
  + [SukkaW Domestic] f934ca26a89d
  + [SukkaW Domestic] fa7a056619ec
  + [Manual Rules] ffa769bfe1e5
```

**Removed: 39** (showing first 39)
```
  - [SukkaW Domestic] 01719ba9ba9d
  - [SukkaW Domestic] 02af1d4b748e
  - [SukkaW Domestic] 037be25c8f80
  - [SukkaW Domestic] 0b8e81d9c84c
  - [SukkaW Domestic] 1922735c7f33
  - [SukkaW Domestic] 1d85b19943b8
  - [SukkaW Domestic] 234f1875a4ed
  - [SukkaW Domestic] 237de8fdebdb
  - [SukkaW Domestic] 26b4bb114457
  - [SukkaW Domestic] 2c8fdd89699e
  - [SukkaW Domestic] 31fc1e78db68
  - [SukkaW Domestic] 397b7815aee9
  - [SukkaW Domestic] 516efbdbeecc
  - [SukkaW Domestic] 518821dfce1d
  - [SukkaW Domestic] 59ff13e316ad
  - [SukkaW Domestic] 5b6fa2bf7b3e
  - [SukkaW Domestic] 5fcdaa3fa90d
  - [SukkaW Domestic] 63f497d6da9d
  - [SukkaW Domestic] 6634b3aaa212
  - [SukkaW Domestic] 77ed5a08ff31
  - [SukkaW Domestic] 7c027328770f
  - [SukkaW Domestic] 7d57b7e43aa4
  - [SukkaW Domestic] 7df4acc92fb3
  - [SukkaW Domestic] 8b333feb1087
  - [SukkaW Domestic] 8fb4f8c839e5
  - [SukkaW Domestic] 933bd03efdd4
  - [SukkaW Domestic] 93e6b19bcf00
  - [SukkaW Domestic] 93f0c4bf6cd7
  - [SukkaW Domestic] 969c99e817a7
  - [SukkaW Domestic] b0d4f5f6062b
  - [SukkaW Domestic] bf039a20f19a
  - [SukkaW Domestic] c12edc532dc8
  - [SukkaW Domestic] c1364709d93b
  - [SukkaW Domestic] c26007222a93
  - [SukkaW Domestic] c4fda56acf59
  - [SukkaW Domestic] c833cc7b6b30
  - [SukkaW Domestic] d19e598582ac
  - [SukkaW Domestic] db3992d73b9b
  - [SukkaW Domestic] e6c9b63a03b4
```

**Source changed: 240**
```
  ~ 7116846602d5: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 7d46345c3c4e: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 367bc509ec15: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ aa60f24304f6: [Rabbit-Spec China → SukkaW Domestic]
  ~ fa4e040d559e: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 817b172c9d21: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ d11dbe9c309e: [Rabbit-Spec China → SukkaW Domestic]
  ~ 0c77cf4814ba: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 82a325583146: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 30a6dbe8fa7c: [Rabbit-Spec China → SukkaW Domestic]
  ~ 5af14b7f38e8: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 0f817c14b1a6: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 23914a56b6fa: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ f9a54e13ba33: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 34e5e47503f5: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 06512113e855: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 74b0e90964ab: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 92b7764226a1: [Rabbit-Spec China → SukkaW Domestic]
  ~ 45dac2432d8f: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ bdf1593788fd: [Rabbit-Spec China → SukkaW Domestic]
  ~ 23d6e5bc4591: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 5793d883dc3c: [Rabbit-Spec China → SukkaW Domestic]
  ~ 6fa527587c22: [Rabbit-Spec China → SukkaW Domestic]
  ~ f65ec2558247: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ f564d79b127b: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ b839c3a390ec: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 9ac8cc8fe7e7: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 86595503e328: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 14194e960702: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ edc81fdc8bdd: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ b0145afd3318: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ d2169c52a73f: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 3a71c8cf1b51: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ b471bf1f9dcc: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 512f1b4014cf: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 6aa7504497fd: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 098236654450: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ c6f33cfd6761: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 9eacb59b0161: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 369f7d58dc24: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 23f7933c1088: [Rabbit-Spec China → SukkaW Domestic]
  ~ 30620083b6f0: [Rabbit-Spec China → SukkaW Domestic]
  ~ 3e1e77692242: [Rabbit-Spec China → SukkaW Domestic]
  ~ 97a9a31fd0f6: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ c6b1f30988e4: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 1cf158fcf3cd: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 8fcb12a4aee8: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 9ffe843cca4b: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 244305e0d2b4: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ~ 4158edbce68c: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
  ... and 190 more
```

## GlobalMedia.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 GlobalMedia] a3fa2f7a0586
```
