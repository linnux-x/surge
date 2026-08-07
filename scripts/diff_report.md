# Surge Rule Diff Report
Generated: 2026-08-08T05:01:46.188845

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 66 |
| Rules removed | 17 |
| Source attribution changed | 2 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 111437 | 111440 | +3 | -0 | ~0 |
| China_IP.list | 11495 | 11506 | +28 | -17 | ~2 |
| Global.list | 24222 | 24257 | +35 | -0 | ~0 |

## China.list

**Added: 3** (showing first 3)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 04edf14e3d72  DOMAIN-SUFFIX,micstatic.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 0975914b4dfe  DOMAIN-SUFFIX,made-in-china.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 93bf64741807  DOMAIN-SUFFIX,poweremarket.com
```

## China_IP.list

**Added: 28** (showing first 28)
```
  + [Loyalsoldier China CIDR] 0374450f8de0  IP-CIDR6,2a14:7dc0:512::/48
  + [Loyalsoldier China CIDR] 1018cb580e96  IP-CIDR,212.189.57.0/24
  + [Loyalsoldier China CIDR] 15131ad9269b  IP-CIDR6,2a14:7dc0:515::/48
  + [Loyalsoldier China CIDR] 1c2503d0de54  IP-CIDR6,2a0a:d685:1fd::/48
  + [Loyalsoldier China CIDR] 2dc83a0d0718  IP-CIDR,82.29.98.0/24
  + [Loyalsoldier China CIDR] 2fe98f7bfcc3  IP-CIDR6,2a14:67c1:b531::/48
  + [Loyalsoldier China CIDR] 3d222f57237d  IP-CIDR,82.109.172.0/24
  + [Loyalsoldier China CIDR] 44b4df605369  IP-CIDR,154.208.67.0/24
  + [Loyalsoldier China CIDR] 58dc9a4f722a  IP-CIDR6,2a14:7586:6101::/48
  + [Loyalsoldier China CIDR] 5d624eec72f1  IP-CIDR,138.252.118.0/24
  + [Loyalsoldier China CIDR] 5fabe37bcb0f  IP-CIDR,87.76.149.0/24
  + [Loyalsoldier China CIDR] 6c4fc10aa644  IP-CIDR6,2a06:9f81:4620::/44
  + [Loyalsoldier China CIDR] 70db5b2fbd2d  IP-CIDR,154.94.60.0/24
  + [Loyalsoldier China CIDR] 75c06cf03fee  IP-CIDR,2.27.155.0/24
  + [Loyalsoldier China CIDR] 78a56efce28c  IP-CIDR,107.149.9.0/24
  + [Loyalsoldier China CIDR] 80b46e8940fc  IP-CIDR6,2a0f:1cc5:6a0::/47
  + [Loyalsoldier China CIDR] 8388d6301546  IP-CIDR6,2a14:67c1:b533::/48
  + [Loyalsoldier China CIDR] 93e9de09071f  IP-CIDR,168.222.18.0/24
  + [Loyalsoldier China CIDR] 9408087d4cae  IP-CIDR,157.254.130.0/24
  + [Loyalsoldier China CIDR] a138136ca45d  IP-CIDR6,2a0f:1cc5:f09::/48
  + [Loyalsoldier China CIDR] aa5d17185027  IP-CIDR,213.218.216.0/24
  + [Loyalsoldier China CIDR] acdcb3b36ea0  IP-CIDR,79.176.227.0/24
  + [Loyalsoldier China CIDR] ad1df9faaa1e  IP-CIDR6,2a14:7dc0:510::/47
  + [Loyalsoldier China CIDR] ad671e3a5b06  IP-CIDR6,2a14:7dc0:51b::/48
  + [Loyalsoldier China CIDR] bfdb33d1c74f  IP-CIDR,163.5.97.0/24
  + [Loyalsoldier China CIDR] ea8ddc44fed7  IP-CIDR,178.83.133.0/24
  + [Loyalsoldier China CIDR] f0ed5ba46627  IP-CIDR6,2a14:7dc0:516::/47
  + [Loyalsoldier China CIDR] f99705cdb340  IP-CIDR,193.39.10.0/24
```

**Removed: 17** (showing first 17)
```
  - [Loyalsoldier China CIDR] 02b6bf99b4f0  IP-CIDR,107.149.27.0/24
  - [Loyalsoldier China CIDR] 16927a0ce817  IP-CIDR6,2a14:7586:6100::/47
  - [Loyalsoldier China CIDR] 1aef175440ee  IP-CIDR,195.162.248.0/24
  - [Loyalsoldier China CIDR] 395549457df8  IP-CIDR6,2a0f:6284:4c00::/44
  - [Loyalsoldier China CIDR] 4d21e4a6d94f  IP-CIDR,82.163.16.0/24
  - [Loyalsoldier China CIDR] 60ee77f765a7  IP-CIDR6,2a06:9f81:4620::/43
  - [Loyalsoldier China CIDR] 63d977e5e8d9  IP-CIDR6,2a0f:6280:1430::/44
  - [Loyalsoldier China CIDR] 6801cad2a342  IP-CIDR,188.220.7.0/24
  - [Loyalsoldier China CIDR] 7262890fbef3  IP-CIDR6,2a12:cb41:200::/44
  - [Loyalsoldier China CIDR] 7558479514f7  IP-CIDR6,2a14:7583:f4fe::/48
  - [Loyalsoldier China CIDR] 7db8a1e6c896  IP-CIDR6,2a14:67c1:b530::/44
  - [Loyalsoldier China CIDR] 852f2d88e69a  IP-CIDR,143.109.55.0/24
  - [Loyalsoldier China CIDR] 912c156f4ceb  IP-CIDR6,2a0f:1cc5:f08::/47
  - [Loyalsoldier China CIDR] 9ab7eb41236e  IP-CIDR,85.239.154.0/24
  - [Loyalsoldier China CIDR] c9111a78c78b  IP-CIDR,45.196.104.0/24
  - [Loyalsoldier China CIDR] ccf0171705fd  IP-CIDR,82.139.229.0/24
  - [Loyalsoldier China CIDR] d37a058b0b26  IP-CIDR6,2a0f:1cc5:6a0::/48
```

**Source changed: 2**
```
  ~ c1621f750560: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 6c04920ec2a0: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Global.list

**Added: 35** (showing first 35)
```
  + [blackmatrix7 Global] 11f52509eaa0  DOMAIN-SUFFIX,wiresock.net
  + [blackmatrix7 Global] 1aac43cd384b  DOMAIN-SUFFIX,stash.ws
  + [blackmatrix7 Global] 1eafc4dfaef9  DOMAIN-SUFFIX,nsloon.com
  + [blackmatrix7 Global] 26bfd0b20046  DOMAIN-SUFFIX,lucasfilm.com
  + [blackmatrix7 Global] 3c91030646c4  DOMAIN-SUFFIX,onexray.com
  + [blackmatrix7 Global] 457a52441ad0  DOMAIN-SUFFIX,2ch.life
  + [blackmatrix7 Global] 478f897d940a  DOMAIN-SUFFIX,pixar.com
  + [blackmatrix7 Global] 4b6e9735a8ff  DOMAIN-SUFFIX,karing.app
  + [blackmatrix7 Global] 4d0fef5393d1  DOMAIN-SUFFIX,cloudflare.pay
  + [blackmatrix7 Global] 63c8c3e97830  DOMAIN-SUFFIX,2dust.link
  + [blackmatrix7 Global] 694b59072165  DOMAIN-SUFFIX,searchlightpictures.com
  + [blackmatrix7 Global] 69fab98c2e93  DOMAIN-SUFFIX,disneyanimation.com
  + [blackmatrix7 Global] 6c27ee2e5870  DOMAIN-SUFFIX,wgtunnel.com
  + [blackmatrix7 Global] 7f3e466c3499  DOMAIN-SUFFIX,stash.wiki
  + [blackmatrix7 Global] 8168ad607113  DOMAIN-SUFFIX,neigbuy.com
  + [blackmatrix7 Global] 8331dbe09c9c  DOMAIN-SUFFIX,20thcenturystudios.com
  + [blackmatrix7 Global] 8931887733ba  DOMAIN-SUFFIX,disneyaccount.com
  + [blackmatrix7 Global] 8f44ed0325b4  DOMAIN-SUFFIX,incy.cc
  + [blackmatrix7 Global] 95960bb80523  DOMAIN-SUFFIX,freeform.com
  + [blackmatrix7 Global] 9a8ee235908b  DOMAIN-SUFFIX,tokyodisneyresort.jp
  + [blackmatrix7 Global] a28d8ef722af  DOMAIN-SUFFIX,2ch.org
  + [blackmatrix7 Global] a5f06f200a40  DOMAIN-SUFFIX,bamtech.net
  + [blackmatrix7 Global] a9a1c57162ad  DOMAIN-SUFFIX,clashmi.app
  + [blackmatrix7 Global] adf5d564aa73  DOMAIN-SUFFIX,cloudflare.app
  + [blackmatrix7 Global] b39919d1950e  DOMAIN-SUFFIX,detpress.com
  + [blackmatrix7 Global] bd60ca44f144  DOMAIN-SUFFIX,hongkongdisneyland.com
  + [blackmatrix7 Global] c8510c959a34  DOMAIN-SUFFIX,prizrak.app
  + [blackmatrix7 Global] d176e4de703b  DOMAIN-SUFFIX,2ch.su
  + [blackmatrix7 Global] d3ac95f66e23  DOMAIN-SUFFIX,waltdisneystudios.com
  + [blackmatrix7 Global] d6a43c39c722  DOMAIN-SUFFIX,shadowlaunch.com
  + [blackmatrix7 Global] e166748869bb  DOMAIN-SUFFIX,flowvy.io
  + [blackmatrix7 Global] e2bd0e998a0a  DOMAIN-SUFFIX,clashverge.dev
  + [blackmatrix7 Global] e768ba40ad0e  DOMAIN-SUFFIX,amnezia.org
  + [blackmatrix7 Global] f8891b60e838  DOMAIN-SUFFIX,clashparty.org
  + [blackmatrix7 Global] fd23d37fb67e  DOMAIN-SUFFIX,flclashx.app
```
