# Surge Rule Diff Report
Generated: 2026-11-21T19:50:13.102081

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 4 |
| Rules added | 25 |
| Rules removed | 47 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110668 | 110665 | +0 | -3 | ~1 |
| Download.list | 1612 | 1614 | +2 | -0 | ~0 |
| Game.list | 570 | 549 | +21 | -42 | ~0 |
| Global.list | 24641 | 24641 | +2 | -2 | ~0 |

## China.list

**Removed: 3** (showing first 3)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 9cbe05fb7e77  DOMAIN-SUFFIX,dcn01.ps4.update.playstation.net
  - [Manual Rules] ac912fef9a7b  DOMAIN-SUFFIX,steamserver.net
  - [blackmatrix7 ChinaMaxNoIP Domain] be80c88b5891  DOMAIN-SUFFIX,dcn01.ps5.update.playstation.net
```

**Source changed: 1**
```
  ~ 318c61730e78: [blackmatrix7 ChinaMaxNoIP Domain → Manual Rules]
```

## Download.list

**Added: 2** (showing first 2)
```
  + [Manual Rules] 388ee7bfac75  DOMAIN-SUFFIX,ps4.update.playstation.net
  + [Manual Rules] 6f66f1eb92b0  DOMAIN-SUFFIX,ps5.update.playstation.net
```

## Game.list

**Added: 21** (showing first 21)
```
  + [Manual Rules] 025603985404  DOMAIN,game.boombeachgame.com
  + [Manual Rules] 1410f354aeff  IP-CIDR6,2602:801:f005::/48,no-resolve
  + [Manual Rules] 36b2f37d37c8  IP-CIDR6,2404:3fc0::/46,no-resolve
  + [Manual Rules] 44bada408c18  IP-CIDR6,2602:801:f006::/47,no-resolve
  + [Manual Rules] 47440916e869  IP-CIDR6,2602:801:f008::/46,no-resolve
  + [Manual Rules] 6395d9294562  IP-CIDR6,2602:801:f00d::/48,no-resolve
  + [Manual Rules] 6b613a816bc3  IP-CIDR6,2a01:bc80:8::/46,no-resolve
  + [Manual Rules] 73fdfb85b555  DOMAIN-SUFFIX,playfabapi.com
  + [Manual Rules] 748a890fe212  DOMAIN,game.clashroyaleapp.com
  + [Manual Rules] 9d258dee2b90  IP-CIDR6,2404:3fc0:a::/48,no-resolve
  + [Manual Rules] ac912fef9a7b  DOMAIN-SUFFIX,steamserver.net
  + [Manual Rules] bd2f34f7b016  IP-CIDR6,2a01:bc80:c::/48,no-resolve
  + [Manual Rules] bebbbb807078  IP-CIDR6,2404:3fc0:8::/47,no-resolve
  + [Manual Rules] c356ae668362  DOMAIN,game.haydaygame.com
  + [Manual Rules] cc74629acbca  DOMAIN,api.minecraftservices.com
  + [Manual Rules] cda5c435368c  DOMAIN,game.clashofclans.com
  + [Manual Rules] d2bb3a822032  DOMAIN,zyngasupport.helpshift.com
  + [Manual Rules] d4632fdc41ea  IP-CIDR6,2602:801:f000::/46,no-resolve
  + [Manual Rules] ec12c2faa40d  DOMAIN,niantic.helpshift.com
  + [Manual Rules] f4dc836df5aa  IP-CIDR6,2602:801:f00e::/48,no-resolve
  + [Manual Rules] f820ae7fe10a  IP-CIDR6,2a01:bc80::/45,no-resolve
```

**Removed: 42** (showing first 42)
```
  - [blackmatrix7 Game] 066e41c8f590  IP-CIDR,3.82.147.36/32,no-resolve
  - [blackmatrix7 Game] 0b68072311bd  IP-CIDR,18.231.148.103/32,no-resolve
  - [blackmatrix7 Game] 0d9f432b39f1  DOMAIN,originasserts.akamaized.net
  - [blackmatrix7 Game] 10f15f5d307d  DOMAIN-SUFFIX,f3b7q2p3.ssl.hwcdn.net
  - [blackmatrix7 Game] 11360efcbe82  IP-CIDR,13.210.25.233/32,no-resolve
  - [blackmatrix7 Game] 1492fcfd3af9  DOMAIN-SUFFIX,sony.com
  - [blackmatrix7 Game] 14f994852189  DOMAIN-SUFFIX,wiipartyu.com
  - [blackmatrix7 Game] 1ecd32798eb8  DOMAIN-SUFFIX,blizzard.nefficient.co.kr
  - [blackmatrix7 Game] 2d33d4ede174  IP-CIDR,18.156.137.147/32,no-resolve
  - [blackmatrix7 Game] 2e05ab5e93fc  DOMAIN-SUFFIX,riotgames.tv
  - [blackmatrix7 Game] 318c61730e78  DOMAIN-SUFFIX,wowchina.com
  - [blackmatrix7 Game] 365f96135c8d  DOMAIN-SUFFIX,seagroup.com
  - [blackmatrix7 Game] 37286db0388a  IP-CIDR,15.254.1.17/32,no-resolve
  - [blackmatrix7 Game] 373e94a2bdd4  DOMAIN-SUFFIX,thelegendarystarfy.com
  - [blackmatrix7 Game] 3c5a059fbff4  DOMAIN-KEYWORD,steamstore
  - [blackmatrix7 Game] 40345a550237  IP-CIDR,52.50.131.212/32,no-resolve
  - [blackmatrix7 Game] 41fe27f95bb2  IP-CIDR,13.212.171.212/32,no-resolve
  - [blackmatrix7 Game] 425e99c387a4  IP-CIDR,15.161.130.86/32,no-resolve
  - [blackmatrix7 Game] 42cf10478b13  DOMAIN-SUFFIX,championshipseriesleague.com
  - [blackmatrix7 Game] 45b85af82228  IP-CIDR,54.207.107.12/32,no-resolve
  - [blackmatrix7 Game] 5165a2a822e2  IP-CIDR,13.212.170.102/32,no-resolve
  - [blackmatrix7 Game] 567425cb2d0e  IP-CIDR,34.220.160.16/32,no-resolve
  - [blackmatrix7 Game] 5e9bd9b8d671  IP-CIDR,3.25.190.152/32,no-resolve
  - [blackmatrix7 Game] 60a47f1ee4bf  DOMAIN,eaasserts-a.akamaihd.net
  - [blackmatrix7 Game] 62dccbd21b70  DOMAIN-KEYWORD,steambroadcast
  - [blackmatrix7 Game] 6d1196fe63d4  IP-CIDR,52.13.42.120/32,no-resolve
  - [blackmatrix7 Game] 7936fa1901f3  DOMAIN-SUFFIX,helpshift.com
  - [blackmatrix7 Game] 8b57dabf07e1  IP-CIDR,3.1.80.68/32,no-resolve
  - [blackmatrix7 Game] 9989f32813f4  IP-CIDR,54.207.104.145/32,no-resolve
  - [blackmatrix7 Game] 9c030630a814  IP-CIDR,54.248.64.192/32,no-resolve
  - [blackmatrix7 Game] 9e5960e47090  IP-CIDR,52.13.150.128/32,no-resolve
  - [blackmatrix7 Game] b267472030f9  IP-CIDR,35.72.32.125/32,no-resolve
  - [blackmatrix7 Game] b32965e7f535  DOMAIN-KEYWORD,steamuserimages
  - [blackmatrix7 Game] b47244e808fe  DOMAIN-SUFFIX,pokemonwifi.net
  - [blackmatrix7 Game] c032ab0e4de4  IP-CIDR,18.141.176.65/32,no-resolve
  - [blackmatrix7 Game] c19ecdd4fe34  DOMAIN-SUFFIX,cdp.cloud.unity3d.com
  - [blackmatrix7 Game] c3806d988eea  IP-CIDR,35.154.64.7/32,no-resolve
  - [blackmatrix7 Game] e7782d926bc4  IP-CIDR,54.94.196.47/32,no-resolve
  - [blackmatrix7 Game] ed40aaba9679  DOMAIN-SUFFIX,ulol.com
  - [blackmatrix7 Game] eefb87445b06  DOMAIN-SUFFIX,flipnotestudio.com
  - [blackmatrix7 Game] f0e61b23f0f1  DOMAIN-SUFFIX,wiifitu.com
  - [blackmatrix7 Game] fa7aacb7fe56  IP-CIDR,54.207.168.84/32,no-resolve
```

## Global.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 Global] 365f96135c8d  DOMAIN-SUFFIX,seagroup.com
  + [blackmatrix7 Global] 7936fa1901f3  DOMAIN-SUFFIX,helpshift.com
```

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 Global] 3821f336d196  DOMAIN,blizzard.nefficient.co.kr
  - [blackmatrix7 Global] 73fdfb85b555  DOMAIN-SUFFIX,playfabapi.com
```
