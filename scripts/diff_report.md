# Surge Rule Diff Report
Generated: 2026-07-26T05:01:12.993661

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 18 |
| Rules removed | 32 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China_IP.list | 11506 | 11486 | +12 | -32 | ~0 |
| Download.list | 1685 | 1686 | +1 | -0 | ~0 |
| Global.list | 24153 | 24158 | +5 | -0 | ~0 |

## China_IP.list

**Added: 12** (showing first 12)
```
  + [Loyalsoldier China CIDR] 1d84b628b37d  IP-CIDR6,2a14:7586:6100::/48
  + [Loyalsoldier China CIDR] 256efeeacdb9  IP-CIDR6,2a14:67c1:b586::/48
  + [Loyalsoldier China CIDR] 434818f015f7  IP-CIDR6,2a0e:aa07:e28b::/48
  + [Loyalsoldier China CIDR] 6b9697e660ed  IP-CIDR6,2a14:7583:f707::/48
  + [Loyalsoldier China CIDR] 812a24960223  IP-CIDR6,2a14:67c1:b100::/47
  + [blackmatrix7 China IPs] 85658fc1ca74  IP-CIDR,102.220.90.0/24
  + [Loyalsoldier China CIDR] 8c5b01c70ac2  IP-CIDR6,2a14:7583:f70b::/48
  + [Loyalsoldier China CIDR] 915c6c6dcafc  IP-CIDR6,2a14:67c1:b147::/48
  + [blackmatrix7 China IPs] 91bab069ce37  IP-CIDR,102.141.200.0/24
  + [Loyalsoldier China CIDR] c7539cd3d504  IP-CIDR6,2a14:7583:f708::/47
  + [Loyalsoldier China CIDR] c9822e9b5541  IP-CIDR6,2a0e:aa07:e288::/47
  + [Loyalsoldier China CIDR] ee260102abd5  IP-CIDR6,2a14:7583:f704::/47
```

**Removed: 32** (showing first 32)
```
  - [blackmatrix7 China IPs] 0f4a0f7f6ba5  IP-CIDR6,2a0f:1cc5:1cc0::/48
  - [blackmatrix7 China IPs] 16927a0ce817  IP-CIDR6,2a14:7586:6100::/47
  - [blackmatrix7 China IPs] 190f575bb70e  IP-CIDR6,2a0e:4005:ff20::/48
  - [blackmatrix7 China IPs] 1e2c41002798  IP-CIDR6,2a14:67c1:b582::/48
  - [blackmatrix7 China IPs] 3277d45b5692  IP-CIDR6,2a0f:1cc5:661::/48
  - [blackmatrix7 China IPs] 35e8de89da61  IP-CIDR6,2a0f:1cc5:45ff::/48
  - [blackmatrix7 China IPs] 36438ea4f483  IP-CIDR,201.14.219.0/24
  - [blackmatrix7 China IPs] 374bc2f1ff98  IP-CIDR6,2a14:7583:f704::/46
  - [blackmatrix7 China IPs] 377bd404450b  IP-CIDR6,2a0f:1cc5:4508::/46
  - [blackmatrix7 China IPs] 3a7470d9b820  IP-CIDR,188.220.127.0/24
  - [blackmatrix7 China IPs] 46bfe2479fb4  IP-CIDR6,2a14:67c1:a02f::/48
  - [blackmatrix7 China IPs] 49ae1dd6a5f2  IP-CIDR6,2a0f:1cc5:40::/48
  - [blackmatrix7 China IPs] 4c164f649300  IP-CIDR,166.0.97.0/24
  - [blackmatrix7 China IPs] 51f1ab9b30cf  IP-CIDR6,2a0f:1cc5:1c20::/48
  - [blackmatrix7 China IPs] 55c7b00fbc54  IP-CIDR6,2a14:67c1:b107::/48
  - [blackmatrix7 China IPs] 560be30e1205  IP-CIDR6,2a14:7583:f708::/46
  - [blackmatrix7 China IPs] 646197d2b590  IP-CIDR6,2a14:67c1:a024::/48
  - [blackmatrix7 China IPs] 7122733ade2a  IP-CIDR6,2a0e:aa07:e288::/46
  - [blackmatrix7 China IPs] 7c5209ffe4c4  IP-CIDR,200.102.180.0/24
  - [blackmatrix7 China IPs] 7d6dff8d0d11  IP-CIDR6,2a14:67c1:b146::/47
  - [blackmatrix7 China IPs] 7e8e23387d0a  IP-CIDR6,2a14:67c1:b105::/48
  - [blackmatrix7 China IPs] 80c545d036da  IP-CIDR,192.6.121.0/24
  - [blackmatrix7 China IPs] 877670c98657  IP-CIDR6,2a14:67c1:b141::/48
  - [blackmatrix7 China IPs] 954307202edf  IP-CIDR6,2a0e:4005:ff13::/48
  - [blackmatrix7 China IPs] a4d402db4ba3  IP-CIDR,166.0.100.0/24
  - [blackmatrix7 China IPs] a74e9c51de90  IP-CIDR6,2a14:67c1:b586::/47
  - [blackmatrix7 China IPs] bd03f228b78f  IP-CIDR6,2a14:67c1:b100::/46
  - [blackmatrix7 China IPs] bef1af0cc655  IP-CIDR,51.241.143.0/24
  - [blackmatrix7 China IPs] db6bd4e95d63  IP-CIDR6,2a12:cb41:1300::/44
  - [blackmatrix7 China IPs] e14605273f2a  IP-CIDR6,2602:f9ba:a8::/48
  - [blackmatrix7 China IPs] f9bbe22e438d  IP-CIDR6,2a0f:1cc5:450c::/47
  - [blackmatrix7 China IPs] fe97570b45ef  IP-CIDR6,2a14:67c1:a023::/48
```

## Download.list

**Added: 1** (showing first 1)
```
  + [SukkaW Download] c77ca9cb3417  DOMAIN,omtapp.garmin.com
```

## Global.list

**Added: 5** (showing first 5)
```
  + [blackmatrix7 Global] 991fdf77f3c2  DOMAIN-SUFFIX,circle19.org
  + [blackmatrix7 Global] 9cd0b5d409ed  DOMAIN-SUFFIX,log.rw
  + [blackmatrix7 Global] c0f1511ee366  DOMAIN-SUFFIX,try.rw
  + [blackmatrix7 Global] f005dcc5f495  DOMAIN-SUFFIX,docs.rw
  + [blackmatrix7 Global] f3373256e946  DOMAIN-SUFFIX,kards.com
```
