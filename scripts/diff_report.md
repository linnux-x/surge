# Surge Rule Diff Report
Generated: 2026-11-22T17:38:02.407027

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 13 |
| Rules added | 31 |
| Rules removed | 1224 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| CDN.list | 32 | 35 | +3 | -0 | ~0 |
| ChinaMedia.list | 375 | 344 | +1 | -32 | ~0 |
| Disney.list | 166 | 165 | +0 | -1 | ~0 |
| Global.list | 24625 | 24635 | +12 | -2 | ~0 |
| GlobalMedia.list | 2242 | 2162 | +8 | -88 | ~0 |
| HKMedia.list | 29 | 27 | +0 | -2 | ~0 |
| InternationalMedia.list | 14 | 15 | +1 | -0 | ~0 |
| JPMedia.list | 26 | 25 | +1 | -2 | ~0 |
| Netflix.list | 1116 | 31 | +2 | -1087 | ~0 |
| SocialMedia.list | 670 | 671 | +1 | -0 | ~0 |
| Spotify.list | 32 | 30 | +0 | -2 | ~0 |
| TWMedia.list | 22 | 21 | +2 | -3 | ~0 |
| USMedia.list | 40 | 35 | +0 | -5 | ~0 |

## CDN.list

**Added: 3** (showing first 3)
```
  + [Manual Rules] 1b3cdb534a65  DOMAIN,js-agent.newrelic.com
  + [Manual Rules] 33cd4b1bc6dc  DOMAIN,cdn.statically.io
  + [Manual Rules] 9481e80817e6  DOMAIN,cdn.cookielaw.org
```

## ChinaMedia.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] c2c192a742dc  DOMAIN,cache.tv.qq.com
```

**Removed: 32** (showing first 32)
```
  - [blackmatrix7 ChinaMedia] 00382501ccea  USER-AGENT,walkman*
  - [blackmatrix7 ChinaMedia] 0429a5adb409  USER-AGENT,MiguVideo*
  - [Manual Rules] 05655084f59f  USER-AGENT,bili/*
  - [Manual Rules] 0613fa6923a4  USER-AGENT,bilibili/*
  - [blackmatrix7 ChinaMedia] 09159f8d56c1  USER-AGENT,%E9%85%B7%E6%88%91%E9%9F%B3%E4%B9%90*
  - [blackmatrix7 ChinaMedia] 1823fb02dd09  USER-AGENT,baiduyinyue
  - [blackmatrix7 ChinaMedia] 2ea606bcd51b  USER-AGENT,PPStream*
  - [blackmatrix7 ChinaMedia] 31a5d1dcbe00  USER-AGENT,%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90
  - [blackmatrix7 ChinaMedia] 359cc6c5c715  USER-AGENT,%E4%BC%98%E9%85%B7*
  - [blackmatrix7 ChinaMedia] 3647f57959ed  USER-AGENT,%E5%92%AA%E5%92%95%E8%A7%86%E9%A2%91
  - [blackmatrix7 ChinaMedia] 3c6d64324b29  USER-AGENT,NeteaseMusic*
  - [blackmatrix7 ChinaMedia] 428817a9ee9d  USER-AGENT,TencentMidasConnect*
  - [blackmatrix7 ChinaMedia] 428e8ec6e5b7  USER-AGENT,live4iphone*
  - [blackmatrix7 ChinaMedia] 43c2493e9ebc  USER-AGENT,MOO*
  - [blackmatrix7 ChinaMedia] 45845dd22646  USER-AGENT,iQiYi*
  - [blackmatrix7 ChinaMedia] 4ad7fcc47d93  USER-AGENT,YYeTs*
  - [blackmatrix7 ChinaMedia] 559761ff78e0  USER-AGENT,QQ%E9%9F%B3%E4%B9%90
  - [blackmatrix7 ChinaMedia] 590ed3d7c8ed  USER-AGENT,QIYI*
  - [blackmatrix7 ChinaMedia] 5b32de7535b5  USER-AGENT,DomesticMedia*
  - [blackmatrix7 ChinaMedia] 60004ae4ae54  USER-AGENT,%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90*
  - [blackmatrix7 ChinaMedia] 755b16237d7a  USER-AGENT,QYPlayer*
  - [blackmatrix7 ChinaMedia] 7f281bd2a532  USER-AGENT,xiami*
  - [blackmatrix7 ChinaMedia] 8947f667c761  USER-AGENT,MOO%E9%9F%B3%E4%B9%90*
  - [blackmatrix7 ChinaMedia] a0dde551080b  USER-AGENT,Youku*
  - [blackmatrix7 ChinaMedia] a238200acb2d  USER-AGENT,Bilibili*
  - [blackmatrix7 ChinaMedia] ac2e27b3d71c  USER-AGENT,AcFun*
  - [blackmatrix7 ChinaMedia] b29cdd18dafc  DOMAIN-SUFFIX,smtcdns.net
  - [blackmatrix7 ChinaMedia] bcce4db0da13  USER-AGENT,QQ%e9%9f%b3%e4%b9%90*
  - [blackmatrix7 ChinaMedia] c760a3e90a54  USER-AGENT,*QIYI*
  - [blackmatrix7 ChinaMedia] ed4be28e6ad2  USER-AGENT,qqlive4iphone*
  - [blackmatrix7 ChinaMedia] f7120ee417d1  USER-AGENT,MGTV*
  - [blackmatrix7 ChinaMedia] fe14fbdda65e  USER-AGENT,QQMusic*
```

## Disney.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Disney] 9205ffed09f9  USER-AGENT,Disney+*
```

## Global.list

**Added: 12** (showing first 12)
```
  + [Manual Rules] 0c7167e94029  IP-CIDR,99.81.97.56/32,no-resolve
  + [Manual Rules] 3fe79fe89105  DOMAIN,auth.docker.io
  + [Manual Rules] 403c39ac63a2  IP-CIDR,52.211.1.180/32,no-resolve
  + [Manual Rules] 5f5444011928  DOMAIN-SUFFIX,hinet.net
  + [Manual Rules] 62922901cca3  DOMAIN-SUFFIX,conviva.com
  + [blackmatrix7 Global] 8dee36d5fc6b  DOMAIN-SUFFIX,adobedtm.com
  + [Manual Rules] b7e9cf78da9a  DOMAIN-SUFFIX,cookielaw.org
  + [Manual Rules] ba1380095ddc  DOMAIN-SUFFIX,braze.com
  + [blackmatrix7 Global] d7cb25ccb42b  IP-CIDR,1.201.0.0/24,no-resolve
  + [Manual Rules] e39376b9e7f5  DOMAIN-SUFFIX,braze.eu
  + [Manual Rules] f930ee9ca489  DOMAIN-SUFFIX,onetrust.com
  + [Manual Rules] f9efbe85a522  DOMAIN,registry-1.docker.io
```

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 Global] 8ae4d48e750d  DOMAIN-SUFFIX,cws.conviva.com
  - [blackmatrix7 Global] f49c16eafc21  DOMAIN-SUFFIX,roco.qq.com
```

## GlobalMedia.list

**Added: 8** (showing first 8)
```
  + [SukkaW Stream] 288af4fca4a0  DOMAIN,gamer2-cds.cdn.hinet.net
  + [SukkaW Stream] 6a5d85fcce53  DOMAIN,gamer-cds.cdn.hinet.net
  + [Manual Rules] 77627133e378  IP-ASN,40027,no-resolve
  + [Manual Rules] 7dd3bd4e0cc0  DOMAIN-SUFFIX,hamivideo.hinet.net
  + [Manual Rules] 928097bfb6c2  IP-ASN,2906,no-resolve
  + [Manual Rules] b3b233330837  DOMAIN-SUFFIX,abematv.akamaized.net
  + [Manual Rules] beaddaaa4235  DOMAIN-WILDCARD,*-hamivideo.cdn.hinet.net
  + [SukkaW Stream] d99c6907f7e3  DOMAIN,4gtvfreepcvod-cds.cdn.hinet.net
```

**Removed: 88** (showing first 88)
```
  - [blackmatrix7 GlobalMedia] 0afbcb353c5f  DOMAIN-KEYWORD,apiproxy-device-prod-nlb-
  - [blackmatrix7 GlobalMedia] 0c0706da9670  USER-AGENT,ITV_Player*
  - [blackmatrix7 GlobalMedia] 0c7167e94029  IP-CIDR,99.81.97.56/32,no-resolve
  - [blackmatrix7 GlobalMedia] 0d37eb70a201  USER-AGENT,discovery+*
  - [blackmatrix7 GlobalMedia] 0e9eabe42842  USER-AGENT,FOXNOW*
  - [blackmatrix7 GlobalMedia] 0f8ab88f182f  USER-AGENT,WeMusic*
  - [blackmatrix7 GlobalMedia] 102ee7c55b53  USER-AGENT,HWTVMobile*
  - [blackmatrix7 GlobalMedia] 13caa1100d7f  USER-AGENT,Niconico*
  - [blackmatrix7 GlobalMedia] 14b1288eff94  DOMAIN-KEYWORD,netflixdnstest
  - [blackmatrix7 GlobalMedia] 1892d0572740  USER-AGENT,HBO*
  - [blackmatrix7 GlobalMedia] 1bd329e97144  USER-AGENT,NaverTV*
  - [blackmatrix7 GlobalMedia] 253166952db8  USER-AGENT,app/bstar*
  - [blackmatrix7 GlobalMedia] 2795bacd1adf  DOMAIN-KEYWORD,nivod
  - [blackmatrix7 GlobalMedia] 2cac1523c4dd  USER-AGENT,HBOMAX*
  - [blackmatrix7 GlobalMedia] 2d7d80d3f706  DOMAIN-KEYWORD,japronx
  - [blackmatrix7 GlobalMedia] 3356f99bdd44  USER-AGENT,FOXPlus*
  - [blackmatrix7 GlobalMedia] 3455cc7294ae  USER-AGENT,PeacockMobile*
  - [blackmatrix7 GlobalMedia] 396bf9603b9d  USER-AGENT,HBOGOPRODHKG*
  - [blackmatrix7 GlobalMedia] 3bbacc593c71  USER-AGENT,WeTV*
  - [blackmatrix7 GlobalMedia] 3f1be3b049f7  DOMAIN-KEYWORD,bbcfmt
  - [blackmatrix7 GlobalMedia] 403c39ac63a2  IP-CIDR,52.211.1.180/32,no-resolve
  - [blackmatrix7 GlobalMedia] 43f9cb1c0285  DOMAIN-KEYWORD,abematv.akamaized.net
  - [blackmatrix7 GlobalMedia] 4561571b4886  DOMAIN-KEYWORD,hamivideo.cdn.hinet.net
  - [blackmatrix7 GlobalMedia] 48a104f0c0b9  DOMAIN-KEYWORD,voddazn
  - [blackmatrix7 GlobalMedia] 48c7084fe49c  USER-AGENT,All4*
  - [blackmatrix7 GlobalMedia] 49603cb7b0f5  USER-AGENT,mytv*
  - [blackmatrix7 GlobalMedia] 4a3a3ec81bac  USER-AGENT,PPlus*
  - [blackmatrix7 GlobalMedia] 4cc594d67bbb  USER-AGENT,LINETV*
  - [blackmatrix7 GlobalMedia] 58e2b2d44d17  DOMAIN-KEYWORD,olevod
  - [blackmatrix7 GlobalMedia] 5bf0a7385b8f  USER-AGENT,PBS*
  - [blackmatrix7 GlobalMedia] 5f5444011928  DOMAIN-SUFFIX,hinet.net
  - [SukkaW Stream] 6038dc2fc443  USER-AGENT,Naver TV*
  - [blackmatrix7 GlobalMedia] 62922901cca3  DOMAIN-SUFFIX,conviva.com
  - [blackmatrix7 GlobalMedia] 6575d02885fc  USER-AGENT,AbemaTV*
  - [blackmatrix7 GlobalMedia] 69c97a3ecb19  USER-AGENT,Disney*
  - [blackmatrix7 GlobalMedia] 71395d34de69  USER-AGENT,BBCiPlayer*
  - [blackmatrix7 GlobalMedia] 7267ab08ef90  DOMAIN-KEYWORD,discovery.uplynk.com
  - [blackmatrix7 GlobalMedia] 729daae0aa48  USER-AGENT,Himalaya*
  - [SukkaW Stream] 73fd24f517fb  USER-AGENT,Prime Video*
  - [blackmatrix7 GlobalMedia] 759d03debb46  DOMAIN-KEYWORD,dualstack.ichnaea-web-
  - [blackmatrix7 GlobalMedia] 7673e4a8ead2  USER-AGENT,Pandora*
  - [blackmatrix7 GlobalMedia] 7dac3869489d  USER-AGENT,KKTV*
  - [blackmatrix7 GlobalMedia] 886bbee134b6  USER-AGENT,DPlus*
  - [blackmatrix7 GlobalMedia] 8b2190abec35  USER-AGENT,InstantVideo.US*
  - [blackmatrix7 GlobalMedia] 8b9c7117708e  USER-AGENT,TIDAL*dia
  - [blackmatrix7 GlobalMedia] 8dee36d5fc6b  DOMAIN-SUFFIX,adobedtm.com
  - [blackmatrix7 GlobalMedia] 9205ffed09f9  USER-AGENT,Disney+*
  - [SukkaW Stream] 931bec6c0567  USER-AGENT,FOX NOW*
  - [blackmatrix7 GlobalMedia] 93655eb657b6  USER-AGENT,HBO%20GO%20PROD*
  - [SukkaW Stream] 93aba43439e8  USER-AGENT,LINE TV*
  - [blackmatrix7 GlobalMedia] 96d3fb9721cc  USER-AGENT,encoreTVB*
  - [blackmatrix7 GlobalMedia] 98384b6ce99d  DOMAIN-KEYWORD,jooxweb-api
  - [blackmatrix7 GlobalMedia] 989e94c713f4  USER-AGENT,LINE%20TV*
  - [blackmatrix7 GlobalMedia] 9f17e27ca75b  DOMAIN-KEYWORD,tvbanywhere
  - [blackmatrix7 GlobalMedia] a2e0d67204c0  USER-AGENT,DAZN*
  - [blackmatrix7 GlobalMedia] a5009a0262da  USER-AGENT,HBO%20GO%20PROD%20HKG*
  - [blackmatrix7 GlobalMedia] a9e8c95c237f  USER-AGENT,JOOX*
  - [blackmatrix7 GlobalMedia] abcf939bc6eb  USER-AGENT,HBO%20NOW*
  - [blackmatrix7 GlobalMedia] b005efc685fe  USER-AGENT,Naver%20TV*
  - [blackmatrix7 GlobalMedia] b7e9cf78da9a  DOMAIN-SUFFIX,cookielaw.org
  - [blackmatrix7 GlobalMedia] b7fdea40fb16  DOMAIN,e13252.dscg.akamaiedge.net
  - [blackmatrix7 GlobalMedia] ba1380095ddc  DOMAIN-SUFFIX,braze.com
  - [blackmatrix7 GlobalMedia] bc73a70a6bfa  USER-AGENT,Prime%20Video*
  - [blackmatrix7 GlobalMedia] c1f8a35674ed  USER-AGENT,Overcast*
  - [blackmatrix7 GlobalMedia] c2ec71c144c1  DOMAIN-KEYWORD,uk-live
  - [blackmatrix7 GlobalMedia] c407b044de11  USER-AGENT,Hulu*
  - [blackmatrix7 GlobalMedia] cce990de8cd7  USER-AGENT,Deezer*
  - [blackmatrix7 GlobalMedia] d696ea5dcb38  USER-AGENT,HBONOW*
  - [blackmatrix7 GlobalMedia] d7cb25ccb42b  IP-CIDR,1.201.0.0/24,no-resolve
  - [blackmatrix7 GlobalMedia] d864587586cc  USER-AGENT,PrimeVideo*
  - [blackmatrix7 GlobalMedia] dc8f33a0f66b  DOMAIN-KEYWORD,avoddashs
  - [blackmatrix7 GlobalMedia] dc94acfcba51  USER-AGENT,Argo*
  - [blackmatrix7 GlobalMedia] e2f8bb43caf7  USER-AGENT,My5*
  - [blackmatrix7 GlobalMedia] e74c5bd47088  USER-AGENT,com.kktv.ios.kktv*
  - [blackmatrix7 GlobalMedia] e7ea7c184455  DOMAIN-KEYWORD,japonx
  - [blackmatrix7 GlobalMedia] e94c290ab427  DOMAIN-KEYWORD,ttvnw
  - [blackmatrix7 GlobalMedia] ede2a0c70624  USER-AGENT,SoundCloud*
  - [blackmatrix7 GlobalMedia] eed29a169554  USER-AGENT,com.kktv*
  - [blackmatrix7 GlobalMedia] f02291f504d7  USER-AGENT,ViuTV*
  - [blackmatrix7 GlobalMedia] f2e709939127  USER-AGENT,TIDAL*
  - [blackmatrix7 GlobalMedia] f33a7443c52e  USER-AGENT,Viu*
  - [blackmatrix7 GlobalMedia] f6d0c8090770  USER-AGENT,TaiwanGood*
  - [blackmatrix7 GlobalMedia] f7506eb2d0f9  DOMAIN-KEYWORD,dualstack.apiproxy-
  - [SukkaW Stream] f815b22bf5cd  USER-AGENT,HBO NOW*
  - [blackmatrix7 GlobalMedia] f930ee9ca489  DOMAIN-SUFFIX,onetrust.com
  - [blackmatrix7 GlobalMedia] fb2eed200f9f  DOMAIN-SUFFIX,js-agent.newrelic.com
  - [blackmatrix7 GlobalMedia] fb9c6bfaca9d  USER-AGENT,FOX%20NOW*
  - [blackmatrix7 GlobalMedia] fe24595bf107  DOMAIN-KEYWORD,hbogoasia
```

## HKMedia.list

**Removed: 2** (showing first 2)
```
  - [SukkaW Stream HK] 49603cb7b0f5  USER-AGENT,mytv*
  - [SukkaW Stream HK] f33a7443c52e  USER-AGENT,Viu*
```

## InternationalMedia.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] adaea4bafa14  DOMAIN,tw.iqiyi.com
```

## JPMedia.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] b3b233330837  DOMAIN-SUFFIX,abematv.akamaized.net
```

**Removed: 2** (showing first 2)
```
  - [SukkaW Stream JP] 13caa1100d7f  USER-AGENT,Niconico*
  - [SukkaW Stream JP] 6575d02885fc  USER-AGENT,AbemaTV*
```

## Netflix.list

**Added: 2** (showing first 2)
```
  + [Manual Rules] 77627133e378  IP-ASN,40027,no-resolve
  + [Manual Rules] 928097bfb6c2  IP-ASN,2906,no-resolve
```

**Removed: 1087** (showing first 100)
```
  - [blackmatrix7 Netflix] 0035e72338ff  IP-CIDR,43.207.179.176/29,no-resolve
  - [blackmatrix7 Netflix] 00c4a04027eb  IP-CIDR,44.192.255.128/28,no-resolve
  - [blackmatrix7 Netflix] 00d508cc92a0  IP-CIDR,18.153.184.88/30,no-resolve
  - [blackmatrix7 Netflix] 00eb2324232b  IP-CIDR,76.223.96.0/21,no-resolve
  - [blackmatrix7 Netflix] 015c875fc024  IP-CIDR,18.252.4.16/29,no-resolve
  - [blackmatrix7 Netflix] 0191d4adf8fc  IP-CIDR,130.176.136.0/23,no-resolve
  - [blackmatrix7 Netflix] 02287e0b4a7b  IP-CIDR,3.15.35.0/24,no-resolve
  - [blackmatrix7 Netflix] 02571b67a916  IP-CIDR,18.180.180.0/23,no-resolve
  - [blackmatrix7 Netflix] 0277f35605be  IP-CIDR,35.73.0.0/22,no-resolve
  - [blackmatrix7 Netflix] 02841435e5d5  IP-CIDR,103.87.204.0/22,no-resolve
  - [blackmatrix7 Netflix] 028b1075460e  IP-CIDR,3.255.16.0/22,no-resolve
  - [blackmatrix7 Netflix] 028e8583a54e  IP-CIDR,3.251.109.92/30,no-resolve
  - [blackmatrix7 Netflix] 02f2d94bb476  IP-CIDR,130.176.78.0/23,no-resolve
  - [blackmatrix7 Netflix] 0387ce44b581  IP-CIDR,3.35.160.0/22,no-resolve
  - [blackmatrix7 Netflix] 03f846cc5bfd  IP-CIDR,65.0.192.176/28,no-resolve
  - [blackmatrix7 Netflix] 040059397089  IP-CIDR,3.26.109.216/30,no-resolve
  - [blackmatrix7 Netflix] 043c5127c4f2  IP-CIDR,18.192.216.0/22,no-resolve
  - [blackmatrix7 Netflix] 0442cb91d034  IP-CIDR,54.247.241.96/29,no-resolve
  - [blackmatrix7 Netflix] 04450f68c744  IP-CIDR,13.52.201.0/24,no-resolve
  - [blackmatrix7 Netflix] 04616d1cb581  IP-CIDR,3.28.70.48/28,no-resolve
  - [blackmatrix7 Netflix] 049c7996fe60  IP-CIDR,18.153.184.84/31,no-resolve
  - [blackmatrix7 Netflix] 04a425552b95  IP-CIDR,3.36.190.0/23,no-resolve
  - [blackmatrix7 Netflix] 04cf5b73ed9f  IP-CIDR,13.40.202.0/23,no-resolve
  - [blackmatrix7 Netflix] 04d54b12b760  IP-CIDR,35.72.164.232/29,no-resolve
  - [blackmatrix7 Netflix] 04de006bbb6a  IP-CIDR,35.180.1.16/28,no-resolve
  - [blackmatrix7 Netflix] 0519cb2ac3e2  IP-CIDR,13.36.84.48/28,no-resolve
  - [blackmatrix7 Netflix] 0538c76423c1  IP-CIDR,18.200.212.0/23,no-resolve
  - [blackmatrix7 Netflix] 0585c2bd1407  IP-CIDR,15.222.43.64/26,no-resolve
  - [blackmatrix7 Netflix] 05903b28afa4  IP-CIDR,3.238.178.128/25,no-resolve
  - [blackmatrix7 Netflix] 06a6c7518799  IP-CIDR,3.64.226.232/29,no-resolve
  - [blackmatrix7 Netflix] 06b39ab077cd  IP-CIDR,3.251.144.0/29,no-resolve
  - [blackmatrix7 Netflix] 070612a94f40  IP-CIDR,13.48.186.128/26,no-resolve
  - [blackmatrix7 Netflix] 0726cc9330c8  IP-CIDR,3.144.141.192/26,no-resolve
  - [blackmatrix7 Netflix] 072f940b01fa  IP-CIDR,18.168.37.136/29,no-resolve
  - [blackmatrix7 Netflix] 073bf83d756d  IP-CIDR,18.246.181.0/24,no-resolve
  - [blackmatrix7 Netflix] 07572956f24e  IP-CIDR,13.250.186.128/26,no-resolve
  - [blackmatrix7 Netflix] 083ae8d2f7a7  IP-CIDR,35.152.74.136/30,no-resolve
  - [blackmatrix7 Netflix] 08538fd25e85  IP-CIDR,13.213.20.144/28,no-resolve
  - [blackmatrix7 Netflix] 08673e279fc3  IP-CIDR,13.250.186.16/29,no-resolve
  - [blackmatrix7 Netflix] 08ba2dc811d1  IP-CIDR,13.246.70.0/23,no-resolve
  - [blackmatrix7 Netflix] 08bc41c11100  IP-CIDR,3.101.226.80/28,no-resolve
  - [blackmatrix7 Netflix] 08d0dd9117a2  IP-CIDR,3.101.163.64/27,no-resolve
  - [blackmatrix7 Netflix] 08e2ded0db6d  IP-CIDR,18.168.36.0/24,no-resolve
  - [blackmatrix7 Netflix] 092aac9a95c4  IP-CIDR,205.251.218.0/24,no-resolve
  - [blackmatrix7 Netflix] 09c775f12680  IP-CIDR,3.65.128.0/21,no-resolve
  - [blackmatrix7 Netflix] 0a029fd34c11  IP-CIDR,3.71.104.0/24,no-resolve
  - [blackmatrix7 Netflix] 0a45a3e9ff65  IP-CIDR,54.182.176.0/21,no-resolve
  - [blackmatrix7 Netflix] 0a58b4372a47  IP-CIDR,13.211.12.192/27,no-resolve
  - [blackmatrix7 Netflix] 0ae601a45477  IP-CIDR,52.47.73.160/27,no-resolve
  - [blackmatrix7 Netflix] 0afbcb353c5f  DOMAIN-KEYWORD,apiproxy-device-prod-nlb-
  - [blackmatrix7 Netflix] 0b02df53955e  IP-CIDR,13.208.33.8/29,no-resolve
  - [blackmatrix7 Netflix] 0b9a5ca8b14b  IP-CIDR,13.124.247.0/24,no-resolve
  - [blackmatrix7 Netflix] 0bb4b5b63a65  IP-CIDR,3.228.181.0/24,no-resolve
  - [blackmatrix7 Netflix] 0bd8ee1e531d  IP-CIDR,3.228.182.8/31,no-resolve
  - [blackmatrix7 Netflix] 0bec7417d3c0  IP-CIDR,3.26.83.0/24,no-resolve
  - [blackmatrix7 Netflix] 0c76fc50362e  IP-CIDR,35.80.36.192/27,no-resolve
  - [blackmatrix7 Netflix] 0d03b9673472  IP-CIDR,44.234.90.252/30,no-resolve
  - [blackmatrix7 Netflix] 0d494816c8a9  IP-CIDR,44.242.181.0/27,no-resolve
  - [blackmatrix7 Netflix] 0d68a92c5808  IP-CIDR,3.146.29.66/31,no-resolve
  - [blackmatrix7 Netflix] 0ddee0cc19d2  IP-CIDR,3.101.160.240/29,no-resolve
  - [blackmatrix7 Netflix] 0e56b7447b72  IP-CIDR,3.97.192.128/25,no-resolve
  - [blackmatrix7 Netflix] 0e7447eca8dd  IP-CIDR,3.28.255.80/28,no-resolve
  - [blackmatrix7 Netflix] 0edd08798273  IP-CIDR,16.50.67.0/25,no-resolve
  - [blackmatrix7 Netflix] 0eeb8bca3d0c  IP-CIDR,18.156.54.0/23,no-resolve
  - [blackmatrix7 Netflix] 0eec6fe421dd  IP-CIDR,44.216.41.160/29,no-resolve
  - [blackmatrix7 Netflix] 0f5fcdf4662e  IP-CIDR,18.135.226.192/26,no-resolve
  - [blackmatrix7 Netflix] 0ffb62c54810  IP-CIDR,34.226.106.180/32,no-resolve
  - [blackmatrix7 Netflix] 10133a300980  IP-CIDR,13.209.1.56/29,no-resolve
  - [blackmatrix7 Netflix] 10aeb59273b5  IP-CIDR,3.112.96.0/25,no-resolve
  - [blackmatrix7 Netflix] 10cba94ef840  IP-CIDR,3.209.83.0/25,no-resolve
  - [blackmatrix7 Netflix] 115f034fb372  IP-CIDR,130.176.96.0/19,no-resolve
  - [blackmatrix7 Netflix] 116403343cbb  IP-CIDR6,2a03:5640::/32,no-resolve
  - [blackmatrix7 Netflix] 116cb7e96be2  IP-CIDR,13.39.103.180/30,no-resolve
  - [blackmatrix7 Netflix] 117d982a81a9  IP-CIDR,13.36.84.126/31,no-resolve
  - [blackmatrix7 Netflix] 1283033d09ba  IP-CIDR,15.228.151.0/24,no-resolve
  - [blackmatrix7 Netflix] 128e6d6cd202  IP-CIDR,18.254.148.0/22,no-resolve
  - [blackmatrix7 Netflix] 12a99f1869a9  IP-CIDR,15.168.105.144/28,no-resolve
  - [blackmatrix7 Netflix] 12cd2e0fbca9  IP-CIDR,15.161.247.128/27,no-resolve
  - [blackmatrix7 Netflix] 12f37699843a  IP-CIDR,18.144.76.32/29,no-resolve
  - [blackmatrix7 Netflix] 133ab186052f  IP-CIDR,18.246.184.0/23,no-resolve
  - [blackmatrix7 Netflix] 136304801cca  IP-CIDR,18.100.64.128/25,no-resolve
  - [blackmatrix7 Netflix] 139257ea5649  IP-CIDR,15.222.16.32/27,no-resolve
  - [blackmatrix7 Netflix] 13d1516971c6  IP-CIDR,43.218.56.128/25,no-resolve
  - [blackmatrix7 Netflix] 1409ff161393  IP-CIDR,54.233.255.128/26,no-resolve
  - [blackmatrix7 Netflix] 141b9131e0a0  IP-CIDR,13.230.21.128/26,no-resolve
  - [blackmatrix7 Netflix] 14277bc7e95f  IP-CIDR,3.29.89.0/24,no-resolve
  - [blackmatrix7 Netflix] 14b1288eff94  DOMAIN-KEYWORD,netflixdnstest
  - [blackmatrix7 Netflix] 14d825ccb087  IP-CIDR,35.72.36.140/30,no-resolve
  - [blackmatrix7 Netflix] 15294a7dfbcc  IP-CIDR,18.168.37.48/30,no-resolve
  - [blackmatrix7 Netflix] 15344e0348af  IP-CIDR,70.232.86.126/32,no-resolve
  - [blackmatrix7 Netflix] 15386a84c39a  IP-CIDR,54.252.79.128/26,no-resolve
  - [blackmatrix7 Netflix] 15436f4c9a37  IP-CIDR,3.251.95.128/27,no-resolve
  - [blackmatrix7 Netflix] 155835fda59b  IP-CIDR,3.248.186.64/29,no-resolve
  - [blackmatrix7 Netflix] 1587222ba575  IP-CIDR,3.21.86.0/23,no-resolve
  - [blackmatrix7 Netflix] 1589b3438601  IP-CIDR,13.209.1.0/28,no-resolve
  - [blackmatrix7 Netflix] 15a804e60118  IP-CIDR,44.222.159.166/31,no-resolve
  - [blackmatrix7 Netflix] 15a892bc7feb  IP-CIDR,3.234.232.224/27,no-resolve
  - [blackmatrix7 Netflix] 15c292077b61  IP-CIDR,3.12.23.88/29,no-resolve
  - [blackmatrix7 Netflix] 164559f76b44  IP-CIDR,54.251.31.128/26,no-resolve
  - [blackmatrix7 Netflix] 166082369f06  IP-CIDR,13.60.1.84/31,no-resolve
  ... and 987 more
```

## SocialMedia.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] fdfcf01e144e  DOMAIN,api.bsky.chat
```

## Spotify.list

**Removed: 2** (showing first 2)
```
  - [Manual Rules] 3c9e48786abd  USER-AGENT,*Spotify*
  - [blackmatrix7 Spotify] ebe09d07c69f  USER-AGENT,Spotify*
```

## TWMedia.list

**Added: 2** (showing first 2)
```
  + [Manual Rules] 7dd3bd4e0cc0  DOMAIN-SUFFIX,hamivideo.hinet.net
  + [Manual Rules] beaddaaa4235  DOMAIN-WILDCARD,*-hamivideo.cdn.hinet.net
```

**Removed: 3** (showing first 3)
```
  - [SukkaW Stream TW] 7dac3869489d  USER-AGENT,KKTV*
  - [SukkaW Stream TW] 93aba43439e8  USER-AGENT,LINE TV*
  - [SukkaW Stream TW] e74c5bd47088  USER-AGENT,com.kktv.ios.kktv*
```

## USMedia.list

**Removed: 5** (showing first 5)
```
  - [SukkaW Stream US] 3356f99bdd44  USER-AGENT,FOXPlus*
  - [SukkaW Stream US] 3455cc7294ae  USER-AGENT,PeacockMobile*
  - [SukkaW Stream US] 4a3a3ec81bac  USER-AGENT,PPlus*
  - [SukkaW Stream US] 931bec6c0567  USER-AGENT,FOX NOW*
  - [SukkaW Stream US] 96d3fb9721cc  USER-AGENT,encoreTVB*
```
