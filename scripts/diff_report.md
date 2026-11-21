# Surge Rule Diff Report
Generated: 2026-11-21T12:45:41.611460

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 11 |
| Rules added | 32 |
| Rules removed | 65 |
| Source attribution changed | 3 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| ChinaMedia.list | 377 | 375 | +0 | -2 | ~0 |
| Global.list | 24604 | 24611 | +7 | -0 | ~0 |
| GlobalMedia.list | 2271 | 2253 | +4 | -22 | ~0 |
| HKMedia.list | 34 | 29 | +3 | -8 | ~0 |
| InternationalMedia.list | 0 | 14 | +14 | -0 | ~0 |
| JPMedia.list | 27 | 26 | +2 | -3 | ~0 |
| Netflix.list | 1123 | 1115 | +0 | -8 | ~0 |
| SocialMedia.list | 675 | 670 | +1 | -6 | ~3 |
| Spotify.list | 32 | 32 | +1 | -1 | ~0 |
| TWMedia.list | 26 | 22 | +0 | -4 | ~0 |
| USMedia.list | 51 | 40 | +0 | -11 | ~0 |

## ChinaMedia.list

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 ChinaMedia] 4bfd990ec7e8  DOMAIN-SUFFIX,pgdt.gtimg.cn
  - [blackmatrix7 ChinaMedia] 799312f14494  DOMAIN,rdelivery.qq.com
```

## Global.list

**Added: 7** (showing first 7)
```
  + [blackmatrix7 Global] 567541f24729  DOMAIN-SUFFIX,fanfox.net
  + [blackmatrix7 Global] 6cd2972f4358  DOMAIN-SUFFIX,amebaownd.com
  + [blackmatrix7 Global] 7f4684f6d7a0  DOMAIN-SUFFIX,ycombinator.com
  + [blackmatrix7 Global] adaf147ff85d  DOMAIN-SUFFIX,amebaowndme.com
  + [Manual Rules] c23217fe3601  IP-CIDR,54.214.128.0/17,no-resolve
  + [blackmatrix7 Global] d2e351b20519  DOMAIN-SUFFIX,dmm.com
  + [blackmatrix7 Global] dbf22636fb7d  DOMAIN-SUFFIX,mangafox.me
```

## GlobalMedia.list

**Added: 4** (showing first 4)
```
  + [Manual Rules] 1400542b735e  DOMAIN-SUFFIX,spotify.com
  + [Manual Rules] 6a2de9afdf7f  DOMAIN-SUFFIX,spotifycdn.com
  + [Manual Rules] aff29961427f  DOMAIN-WILDCARD,*-spotify-com.akamaized.net
  + [Manual Rules] db4c9a0b8f7f  DOMAIN-SUFFIX,spotifycdn.net
```

**Removed: 22** (showing first 22)
```
  - [blackmatrix7 GlobalMedia] 0fd799971846  IP-CIDR,23.78.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 12a9abfd863e  USER-AGENT,Anime*
  - [blackmatrix7 GlobalMedia] 1600715fc4a4  USER-AGENT,TVer-Release*
  - [blackmatrix7 GlobalMedia] 19b8924dcc66  IP-CIDR,54.0.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 2fc98960cf0f  USER-AGENT,LINE*
  - [blackmatrix7 GlobalMedia] 37b160037c57  IP-CIDR,218.102.32.0/19,no-resolve
  - [blackmatrix7 GlobalMedia] 49a06a91a555  DOMAIN-KEYWORD,rthklive
  - [blackmatrix7 GlobalMedia] 4bb4b0aed913  IP-CIDR,203.116.0.0/16,no-resolve
  - [SukkaW Stream] 567541f24729  DOMAIN-SUFFIX,fanfox.net
  - [blackmatrix7 GlobalMedia] 5781b9282bc9  IP-CIDR,203.198.80.0/21,no-resolve
  - [SukkaW Stream] 59a5d84869ed  DOMAIN-KEYWORD,-spotify-com
  - [blackmatrix7 GlobalMedia] 6cd2972f4358  DOMAIN-SUFFIX,amebaownd.com
  - [blackmatrix7 GlobalMedia] 8427837d9df1  USER-AGENT,Max*
  - [blackmatrix7 GlobalMedia] 90c518d72d69  DOMAIN-KEYWORD,nowtv100
  - [SukkaW Stream] 9d988c5bc9da  PROCESS-NAME,com.bstar.intl
  - [blackmatrix7 GlobalMedia] a9dd62bf4de6  IP-CIDR,203.198.0.0/20,no-resolve
  - [blackmatrix7 GlobalMedia] adaf147ff85d  DOMAIN-SUFFIX,amebaowndme.com
  - [blackmatrix7 GlobalMedia] b528f18fa1c2  DOMAIN-SUFFIX,viblast.com
  - [blackmatrix7 GlobalMedia] c23217fe3601  IP-CIDR,54.214.128.0/17,no-resolve
  - [blackmatrix7 GlobalMedia] d2e351b20519  DOMAIN-SUFFIX,dmm.com
  - [SukkaW Stream] dbf22636fb7d  DOMAIN-SUFFIX,mangafox.me
  - [blackmatrix7 GlobalMedia] e101cd433b8a  IP-CIDR,219.76.0.0/17,no-resolve
```

## HKMedia.list

**Added: 3** (showing first 3)
```
  + [Manual Rules] 1e802272cc27  DOMAIN-SUFFIX,rthk.org.hk
  + [Manual Rules] e8d4bb224eb5  DOMAIN,rthklive2-lh.akamaihd.net
  + [Manual Rules] eb159a702d51  DOMAIN-SUFFIX,rthk.hk
```

**Removed: 8** (showing first 8)
```
  - [SukkaW Stream HK] 49a06a91a555  DOMAIN-KEYWORD,rthklive
  - [SukkaW Stream HK] 540dc1deb7d1  DOMAIN,upos-bstar-mirrorakam.akamaized.net
  - [SukkaW Stream HK] 7e8af3829204  DOMAIN,apm-misaka.biliapi.net
  - [SukkaW Stream HK] 907992957486  DOMAIN,upos-bstar1-mirrorakam.akamaized.net
  - [SukkaW Stream HK] 90c518d72d69  DOMAIN-KEYWORD,nowtv100
  - [SukkaW Stream HK] 9d988c5bc9da  PROCESS-NAME,com.bstar.intl
  - [SukkaW Stream HK] a418f196ad15  DOMAIN-SUFFIX,biliintl.com
  - [SukkaW Stream HK] df6d0b8ae84d  DOMAIN-SUFFIX,bilibili.tv
```

## InternationalMedia.list

**Added: 14** (showing first 14)
```
  + [Manual Rules] 030d91226d77  DOMAIN-SUFFIX,inter.iqiyi.com
  + [Manual Rules] 0fc322b3a516  DOMAIN-SUFFIX,bstarstatic.com
  + [Manual Rules] 1f80510bc598  DOMAIN-SUFFIX,iq.com
  + [Manual Rules] 328455886527  DOMAIN-SUFFIX,intl-rcd.iqiyi.com
  + [Manual Rules] 4726be509a57  DOMAIN,akmcdnoversea-tw.inter.ptqy.gitv.tv
  + [Manual Rules] 540dc1deb7d1  DOMAIN,upos-bstar-mirrorakam.akamaized.net
  + [Manual Rules] 7e8af3829204  DOMAIN,apm-misaka.biliapi.net
  + [Manual Rules] 907992957486  DOMAIN,upos-bstar1-mirrorakam.akamaized.net
  + [Manual Rules] 9683b9d72951  DOMAIN,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv
  + [Manual Rules] a418f196ad15  DOMAIN-SUFFIX,biliintl.com
  + [Manual Rules] a7f15d5d644d  DOMAIN,p-bstarstatic.akamaized.net
  + [Manual Rules] bb3f123d8b43  DOMAIN-SUFFIX,intl-subscription.iqiyi.com
  + [Manual Rules] d70993d55aa3  DOMAIN-SUFFIX,intl.iqiyi.com
  + [Manual Rules] df6d0b8ae84d  DOMAIN-SUFFIX,bilibili.tv
```

## JPMedia.list

**Added: 2** (showing first 2)
```
  + [Manual Rules] 08f0d2bb4437  DOMAIN-SUFFIX,tv.dmm.com
  + [Manual Rules] a8c72ac6889b  DOMAIN-SUFFIX,video.dmm.com
```

**Removed: 3** (showing first 3)
```
  - [SukkaW Stream JP] 6cd2972f4358  DOMAIN-SUFFIX,amebaownd.com
  - [SukkaW Stream JP] adaf147ff85d  DOMAIN-SUFFIX,amebaowndme.com
  - [SukkaW Stream JP] d2e351b20519  DOMAIN-SUFFIX,dmm.com
```

## Netflix.list

**Removed: 8** (showing first 8)
```
  - [blackmatrix7 Netflix] 0fd799971846  IP-CIDR,23.78.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 19b8924dcc66  IP-CIDR,54.0.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 37b160037c57  IP-CIDR,218.102.32.0/19,no-resolve
  - [blackmatrix7 Netflix] 4bb4b0aed913  IP-CIDR,203.116.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 5781b9282bc9  IP-CIDR,203.198.80.0/21,no-resolve
  - [blackmatrix7 Netflix] a9dd62bf4de6  IP-CIDR,203.198.0.0/20,no-resolve
  - [blackmatrix7 Netflix] c23217fe3601  IP-CIDR,54.214.128.0/17,no-resolve
  - [blackmatrix7 Netflix] e101cd433b8a  IP-CIDR,219.76.0.0/17,no-resolve
```

## SocialMedia.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] d998b921cbe4  DOMAIN,news.ycombinator.com
```

**Removed: 6** (showing first 6)
```
  - [blackmatrix7 Facebook] 58cd66ecb7af  DOMAIN-KEYWORD,facebook
  - [Manual Rules] 7f4684f6d7a0  DOMAIN-SUFFIX,ycombinator.com
  - [blackmatrix7 Instagram] 86491268f2c4  DOMAIN-KEYWORD,instagram
  - [blackmatrix7 Facebook] 8cf22cab2f0c  DOMAIN-KEYWORD,fbcdn
  - [Manual Rules] ac8f076a6d57  DOMAIN-KEYWORD,whatsapp
  - [blackmatrix7 Twitter] c59028273ffc  DOMAIN-KEYWORD,twitter
```

**Source changed: 3**
```
  ~ 982bf62398a2: [blackmatrix7 Facebook → Manual Rules]
  ~ ca241ae3a9b1: [blackmatrix7 Facebook → Manual Rules]
  ~ b6bc1bcd70e0: [blackmatrix7 Facebook → Manual Rules]
```

## Spotify.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] aff29961427f  DOMAIN-WILDCARD,*-spotify-com.akamaized.net
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Spotify] 67f7c913a65e  DOMAIN-KEYWORD,spotify
```

## TWMedia.list

**Removed: 4** (showing first 4)
```
  - [SukkaW Stream TW] 12a9abfd863e  USER-AGENT,Anime*
  - [SukkaW Stream TW] 567541f24729  DOMAIN-SUFFIX,fanfox.net
  - [SukkaW Stream TW] b528f18fa1c2  DOMAIN-SUFFIX,viblast.com
  - [SukkaW Stream TW] dbf22636fb7d  DOMAIN-SUFFIX,mangafox.me
```

## USMedia.list

**Removed: 11** (showing first 11)
```
  - [SukkaW Stream US] 0d37eb70a201  USER-AGENT,discovery+*
  - [SukkaW Stream US] 1600715fc4a4  USER-AGENT,TVer-Release*
  - [SukkaW Stream US] 167bddb0ac75  DOMAIN-SUFFIX,discoveryplus.com
  - [SukkaW Stream US] 2d3123fea9e4  DOMAIN-SUFFIX,disco-api.com
  - [SukkaW Stream US] 5c6356321742  DOMAIN-SUFFIX,hjholdings.jp
  - [SukkaW Stream US] 621d52db8fd7  DOMAIN-SUFFIX,happyon.jp
  - [SukkaW Stream US] 763cf4f2d14f  DOMAIN-SUFFIX,hulu.jp
  - [SukkaW Stream US] 7c8534b1ff6c  DOMAIN-SUFFIX,discoveryplus.in
  - [SukkaW Stream US] 886bbee134b6  USER-AGENT,DPlus*
  - [SukkaW Stream US] c407b044de11  USER-AGENT,Hulu*
  - [SukkaW Stream US] f8c50ecbd862  DOMAIN-SUFFIX,discoveryplus.co.uk
```
