# Surge Rule Diff Report
Generated: 2026-07-17T05:00:38.143224

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 108 |
| Rules removed | 10 |
| Source attribution changed | 26 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 139 | 140 | +1 | -0 | ~0 |
| China_IP.list | 11432 | 11530 | +107 | -9 | ~26 |
| Global.list | 24139 | 24138 | +0 | -1 | ~0 |

## AI.list

**Added: 1** (showing first 1)
```
  + [Rabbit-Spec AIGC] 7a24b93f8f0d  DOMAIN-SUFFIX,chatgpt.site
```

## China_IP.list

**Added: 107** (showing first 100)
```
  + [Loyalsoldier China CIDR] 004f6b8a33de  IP-CIDR6,2a0f:1cc5:1310::/44
  + [Loyalsoldier China CIDR] 006e59991d3e  IP-CIDR6,2a0a:6040:d623::/48
  + [Loyalsoldier China CIDR] 08151ebc5fd1  IP-CIDR6,2a06:a005:e70::/44
  + [Loyalsoldier China CIDR] 0b8dc02358ce  IP-CIDR6,2a14:67c1:74::/47
  + [Loyalsoldier China CIDR] 0cb867a03a5e  IP-CIDR6,2a14:7581:30b6::/48
  + [Loyalsoldier China CIDR] 123fc30872af  IP-CIDR6,2a0b:4e07:b8::/47
  + [Loyalsoldier China CIDR] 134c1a95eed8  IP-CIDR6,2a0f:1cc5:2680::/42
  + [Loyalsoldier China CIDR] 15cdb72e497f  IP-CIDR6,2a14:7581:3100::/40
  + [Loyalsoldier China CIDR] 15dce2de7b82  IP-CIDR6,2602:f92a:a470::/48
  + [Loyalsoldier China CIDR] 1638c39e1a30  IP-CIDR6,2a0a:6040:e543::/48
  + [Loyalsoldier China CIDR] 16927a0ce817  IP-CIDR6,2a14:7586:6100::/47
  + [Loyalsoldier China CIDR] 19739593a270  IP-CIDR6,2a0a:6040:6c40::/44
  + [Loyalsoldier China CIDR] 1a91bdcc1ef8  IP-CIDR,203.12.95.0/24
  + [Loyalsoldier China CIDR] 1b3762a04fbc  IP-CIDR6,2001:678:120::/48
  + [Loyalsoldier China CIDR] 1e2c41002798  IP-CIDR6,2a14:67c1:b582::/48
  + [Loyalsoldier China CIDR] 1eba13276876  IP-CIDR6,2a14:67c3:caf8::/46
  + [Loyalsoldier China CIDR] 21a6f85b6262  IP-CIDR6,2a14:67c3:caff::/48
  + [Loyalsoldier China CIDR] 260cd8bdce17  IP-CIDR6,2a12:cb41:1200::/44
  + [Loyalsoldier China CIDR] 2c3eb62b0dd1  IP-CIDR6,2a14:67c3:190::/47
  + [Loyalsoldier China CIDR] 2c67e5568fe9  IP-CIDR6,2a14:67c2:514::/46
  + [Loyalsoldier China CIDR] 2cc4b5a7a894  IP-CIDR6,2a0f:1cc5:1901::/48
  + [Loyalsoldier China CIDR] 2cddb99a9ce6  IP-CIDR,44.32.185.0/24
  + [Loyalsoldier China CIDR] 2d447737c31a  IP-CIDR6,2a14:67c2:578::/45
  + [Loyalsoldier China CIDR] 2e44d918c63e  IP-CIDR6,2a14:67c2:518::/45
  + [Loyalsoldier China CIDR] 2f09778250ec  IP-CIDR6,2a14:67c1:c600::/40
  + [Loyalsoldier China CIDR] 3277d45b5692  IP-CIDR6,2a0f:1cc5:661::/48
  + [Loyalsoldier China CIDR] 3407201f046e  IP-CIDR6,2a14:67c1:a123::/48
  + [Loyalsoldier China CIDR] 34456e90c357  IP-CIDR,151.246.184.0/24
  + [Loyalsoldier China CIDR] 3a13ca8f4e75  IP-CIDR6,2a14:67c2:574::/48
  + [Loyalsoldier China CIDR] 3db45fbd3a20  IP-CIDR6,2a0a:6040:e541::/48
  + [Loyalsoldier China CIDR] 46a96878b296  IP-CIDR6,2a13:b487:1330::/47
  + [Loyalsoldier China CIDR] 46bfe2479fb4  IP-CIDR6,2a14:67c1:a02f::/48
  + [Loyalsoldier China CIDR] 509c412f9e4e  IP-CIDR6,2a14:67c3:360::/48
  + [Loyalsoldier China CIDR] 51f1ab9b30cf  IP-CIDR6,2a0f:1cc5:1c20::/48
  + [Loyalsoldier China CIDR] 52aaed70e331  IP-CIDR6,2a0e:97c0:5ef::/48
  + [Loyalsoldier China CIDR] 55c7b00fbc54  IP-CIDR6,2a14:67c1:b107::/48
  + [Loyalsoldier China CIDR] 5b3e6c901995  IP-CIDR6,2a14:67c2:560::/44
  + [Loyalsoldier China CIDR] 5ffad8d39de9  IP-CIDR6,2a0e:aa07:f0d4::/47
  + [Loyalsoldier China CIDR] 61e09c4d5002  IP-CIDR6,2a14:67c2:511::/48
  + [Loyalsoldier China CIDR] 646197d2b590  IP-CIDR6,2a14:67c1:a024::/48
  + [Loyalsoldier China CIDR] 64e10cd434e7  IP-CIDR6,2602:f92a:dead::/48
  + [Loyalsoldier China CIDR] 68dd3d716724  IP-CIDR6,2a0a:6040:d610::/46
  + [Loyalsoldier China CIDR] 6ae3fe185ab4  IP-CIDR6,2a0e:b107:1a40::/46
  + [Loyalsoldier China CIDR] 6af7c1891969  IP-CIDR6,2a0a:d685:1fe::/47
  + [Loyalsoldier China CIDR] 6b0dd51d1d90  IP-CIDR6,2a14:67c1:b136::/48
  + [Loyalsoldier China CIDR] 6cdbcd6d7260  IP-CIDR6,2a14:7583:f4f0::/47
  + [Loyalsoldier China CIDR] 6e0c02828ac7  IP-CIDR6,2a01:e281:a410::/44
  + [Loyalsoldier China CIDR] 7064d639219c  IP-CIDR6,2a14:67c1:b142::/47
  + [Loyalsoldier China CIDR] 70e42de13265  IP-CIDR6,2a14:67c1:a128::/48
  + [Loyalsoldier China CIDR] 746f472ba163  IP-CIDR6,2a14:67c2:500::/44
  + [Loyalsoldier China CIDR] 7a0952209256  IP-CIDR6,2a14:67c1:b148::/48
  + [Loyalsoldier China CIDR] 7b80c9920e24  IP-CIDR6,2a14:7583:f306::/48
  + [Loyalsoldier China CIDR] 7d6dff8d0d11  IP-CIDR6,2a14:67c1:b146::/47
  + [Loyalsoldier China CIDR] 7e8e23387d0a  IP-CIDR6,2a14:67c1:b105::/48
  + [Loyalsoldier China CIDR] 7ef971e3166c  IP-CIDR6,2a0a:6040:e54c::/48
  + [Loyalsoldier China CIDR] 7f19e486fa01  IP-CIDR,44.30.169.0/24
  + [Loyalsoldier China CIDR] 82f125c6c9c1  IP-CIDR6,2a0a:6040:d600::/44
  + [Loyalsoldier China CIDR] 83ab0f1aa5de  IP-CIDR6,2a14:7583:f304::/47
  + [Loyalsoldier China CIDR] 877670c98657  IP-CIDR6,2a14:67c1:b141::/48
  + [Loyalsoldier China CIDR] 8b4e3f9af500  IP-CIDR6,2a14:67c2:570::/46
  + [Loyalsoldier China CIDR] 8c5218227581  IP-CIDR6,2a0f:6280:1460::/44
  + [Loyalsoldier China CIDR] 8d9cc93d33c5  IP-CIDR6,2a14:67c1:b130::/46
  + [Loyalsoldier China CIDR] 9416408e7be9  IP-CIDR6,2a14:67c1:b134::/48
  + [Loyalsoldier China CIDR] 95c51b1cf14b  IP-CIDR6,2a0a:6040:d618::/47
  + [Loyalsoldier China CIDR] 95c8e122efed  IP-CIDR6,2001:678:10d0::/48
  + [Loyalsoldier China CIDR] 95cd7654e406  IP-CIDR6,2a14:67c2:512::/47
  + [Loyalsoldier China CIDR] 98a9cc0aa8fe  IP-CIDR6,2a0a:6040:d615::/48
  + [Loyalsoldier China CIDR] a18291050977  IP-CIDR,92.118.189.0/24
  + [Loyalsoldier China CIDR] a4d6e2ce95d4  IP-CIDR6,2a06:a005:e50::/44
  + [Loyalsoldier China CIDR] a4e11dde286d  IP-CIDR6,2a0f:1cc5:c01::/48
  + [Loyalsoldier China CIDR] a7d34eac5bf4  IP-CIDR,44.30.171.0/24
  + [Loyalsoldier China CIDR] a8ed5ca027a3  IP-CIDR6,2a14:67c3:cafc::/47
  + [Loyalsoldier China CIDR] aa5703d2f4ca  IP-CIDR6,2400:9380:9282::/48
  + [Loyalsoldier China CIDR] aa7b932098ff  IP-CIDR6,2a14:67c1:70::/48
  + [Loyalsoldier China CIDR] ab641ad23b31  IP-CIDR6,2a13:9500:194::/47
  + [Loyalsoldier China CIDR] af3d6b1572e5  IP-CIDR6,2a14:67c1:b110::/48
  + [Loyalsoldier China CIDR] b126a3282db5  IP-CIDR6,2a0a:6040:d616::/48
  + [Loyalsoldier China CIDR] b1f35bc7245d  IP-CIDR6,2a12:cb41:600::/44
  + [Loyalsoldier China CIDR] b2f57580efad  IP-CIDR6,2a0a:6040:d624::/48
  + [Loyalsoldier China CIDR] b3837d1eb52d  IP-CIDR6,2a0a:6040:c770::/44
  + [Loyalsoldier China CIDR] b5d1bef08852  IP-CIDR6,2a14:67c2:540::/43
  + [Loyalsoldier China CIDR] b84482447b3a  IP-CIDR6,2a14:7583:f500::/48
  + [Loyalsoldier China CIDR] bcfc1887aa07  IP-CIDR6,2a14:7583:f300::/46
  + [Loyalsoldier China CIDR] bd03f228b78f  IP-CIDR6,2a14:67c1:b100::/46
  + [Loyalsoldier China CIDR] bf44d5374d2c  IP-CIDR6,2a14:67c1:a02a::/48
  + [Loyalsoldier China CIDR] bf849f0489c1  IP-CIDR6,2a14:67c1:a020::/48
  + [Loyalsoldier China CIDR] bf84eedca8c9  IP-CIDR6,2a14:67c1:a110::/44
  + [Loyalsoldier China CIDR] c6c37258ebd6  IP-CIDR6,2a14:67c2:580::/41
  + [Loyalsoldier China CIDR] c77a59a96912  IP-CIDR6,2a0a:6040:d629::/48
  + [Loyalsoldier China CIDR] c7ff3b47a88b  IP-CIDR6,2a01:e281:a400::/48
  + [Loyalsoldier China CIDR] dc2553c9298a  IP-CIDR6,2a0a:6040:c700::/42
  + [Loyalsoldier China CIDR] e039fd41585f  IP-CIDR6,2a0a:6040:c7a0::/48
  + [Loyalsoldier China CIDR] e0dc7b4942a3  IP-CIDR6,2a0f:6280:1400::/44
  + [Loyalsoldier China CIDR] e22ed729753d  IP-CIDR6,2a14:67c2:aa1::/48
  + [Loyalsoldier China CIDR] e4df74441581  IP-CIDR6,2a14:67c2:520::/43
  + [Loyalsoldier China CIDR] e72483c14908  IP-CIDR6,2a0f:7802:e100::/46
  + [Loyalsoldier China CIDR] e73302172525  IP-CIDR6,2a14:67c1:a125::/48
  + [Loyalsoldier China CIDR] ecff54395512  IP-CIDR,44.31.212.0/24
  + [Loyalsoldier China CIDR] ef16338a289d  IP-CIDR6,2a0a:6040:e544::/48
  + [Loyalsoldier China CIDR] f1963c3fe81f  IP-CIDR,49.213.62.0/23
  ... and 7 more
```

**Removed: 9** (showing first 9)
```
  - [Loyalsoldier China CIDR] 0706a785e381  IP-CIDR6,2a14:67c1:a114::/46
  - [Loyalsoldier China CIDR] 3af8a2ddb170  IP-CIDR6,2a14:67c1:a110::/48
  - [Loyalsoldier China CIDR] 4625f3c2f5ac  IP-CIDR6,2a14:7583:f4f0::/48
  - [Loyalsoldier China CIDR] 58dc9a4f722a  IP-CIDR6,2a14:7586:6101::/48
  - [Loyalsoldier China CIDR] 7c5f90628e95  IP-CIDR6,2a0a:d685:1ff::/48
  - [Loyalsoldier China CIDR] 8ef43edacd10  IP-CIDR6,2a13:9500:194::/48
  - [Loyalsoldier China CIDR] 9b6c6022ca4a  IP-CIDR6,2a14:67c1:a118::/45
  - [Loyalsoldier China CIDR] bea71f7790cc  IP-CIDR6,2a14:67c2:519::/48
  - [Loyalsoldier China CIDR] bf1485c9ee47  IP-CIDR6,2a14:67c1:a112::/47
```

**Source changed: 26**
```
  ~ adafe872bb28: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ de5ae4a3d385: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ a9ad5a941e8d: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 510cdef3330c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 04a0cf2c28ba: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 5eda8e03f912: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 885e9d82053e: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ ba4856ba8818: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 84d2a438d31d: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 170444d2dd94: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ cc7fb4de1a1a: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ a69f9409f647: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 3fc6be92d626: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 912c156f4ceb: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ b37393a84369: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 4517c7447992: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ e6f10363842b: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 51c3b5582a8c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ f46bf97ad540: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 11731b94f0f3: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ c6ca909bbee7: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 0555710c3dc6: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 6a0bc4e16437: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ dae405619306: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ ec5e3642ba9c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 6f475d7f2eba: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Global.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Global] 7a24b93f8f0d  DOMAIN-SUFFIX,chatgpt.site
```
