# Surge Rule Diff Report
Generated: 2026-10-18T05:01:54.055792

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 550 |
| Rules removed | 262 |
| Source attribution changed | 12 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Apple_AI.list | 17 | 18 | +1 | -0 | ~0 |
| China.list | 110654 | 110567 | +12 | -99 | ~0 |
| China_IP.list | 11512 | 11843 | +346 | -15 | ~12 |
| Global.list | 24480 | 24486 | +6 | -0 | ~0 |
| Speedtest.list | 1685 | 1722 | +185 | -148 | ~0 |

## Apple_AI.list

**Added: 1** (showing first 1)
```
  + [RocM301 Apple-AI] d5d02abafd94  DOMAIN,wps.apple.com
```

## China.list

**Added: 12** (showing first 12)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 1eb69621321b  DOMAIN-SUFFIX,pyquan.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 2edec0adfa60  DOMAIN-SUFFIX,slldbs641.vip
  + [blackmatrix7 ChinaMaxNoIP Domain] 38bcd58b422f  DOMAIN-SUFFIX,dittocdn.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 5b8da9f6e8f5  DOMAIN,download.microsoft.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 7c2496172762  DOMAIN-SUFFIX,shengtai.cyou
  + [blackmatrix7 ChinaMaxNoIP Domain] 8bffc31fc54b  DOMAIN-SUFFIX,dns.lat
  + [blackmatrix7 ChinaMaxNoIP Domain] 8ecce36f67e9  DOMAIN-SUFFIX,xhlylx.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 9aad3c93d497  DOMAIN-SUFFIX,grboi.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 9b943531675d  DOMAIN-SUFFIX,9fe06a.fyi
  + [blackmatrix7 ChinaMaxNoIP Domain] c1810b29ba77  DOMAIN-SUFFIX,corexpertdata.com
  + [blackmatrix7 ChinaMaxNoIP Domain] d9641d8a7b5d  DOMAIN-SUFFIX,siriser.com
  + [blackmatrix7 ChinaMaxNoIP Domain] e14edee7ab81  DOMAIN-SUFFIX,tengcanxi.com
```

**Removed: 99** (showing first 99)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 08ab4924513d  DOMAIN-SUFFIX,zgjymg.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0ac73c22bde8  DOMAIN-SUFFIX,haommn.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0eb02982b0e6  DOMAIN-SUFFIX,jingshistudy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1025edcd2662  DOMAIN-SUFFIX,fnnspa.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 110cf5ba801e  DOMAIN-SUFFIX,syoker.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 148c87ae22dc  DOMAIN-SUFFIX,tuistone.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 181bae580e30  DOMAIN-SUFFIX,tzxwzx.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 183023741e1c  DOMAIN-SUFFIX,wochaw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1a34e97a1da0  DOMAIN-SUFFIX,46ps.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1dd138f98428  DOMAIN-SUFFIX,junziyize.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 20454aa10918  DOMAIN-SUFFIX,cdn.samsung.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 26a7b61c7300  DOMAIN-SUFFIX,shuangyanjie.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2deb102f879b  DOMAIN-SUFFIX,large.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 30eb7a3d963d  DOMAIN-SUFFIX,melizhi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 319381c9e673  DOMAIN-SUFFIX,cqtlskj.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 334d4facc27a  DOMAIN-SUFFIX,bscdnweb.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 336206eec621  DOMAIN-SUFFIX,datarelab.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3eb82ba86ad7  DOMAIN-SUFFIX,huicx7.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 405b3783898b  DOMAIN-SUFFIX,xmldz4.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 41f41cf3d765  DOMAIN-SUFFIX,acjw.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 43d717d7b28c  DOMAIN-SUFFIX,shancui1688.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 492465e163f7  DOMAIN-SUFFIX,tuirice.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4b0d819ea779  DOMAIN-SUFFIX,wedn.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 51bd3f287791  DOMAIN-SUFFIX,fcpiao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 555f2e4d78c6  DOMAIN-SUFFIX,618day.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 561dea2011b9  DOMAIN-SUFFIX,teamlogs.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 568eaf16751f  DOMAIN-SUFFIX,njletop.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5a3beeb816cc  DOMAIN-SUFFIX,lihuashouji.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5c6fa921258c  DOMAIN-SUFFIX,0515yy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5c918102f384  DOMAIN-SUFFIX,68978.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 5f71721b2d07  DOMAIN-SUFFIX,ncogvki.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 617154d53255  DOMAIN-SUFFIX,chiheshan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 61e07c7d9b8b  DOMAIN-SUFFIX,01zk.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 65af468c2020  DOMAIN-SUFFIX,913vr.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 663b3a8ff049  DOMAIN-SUFFIX,portcontainer.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 66fe94b45a7e  DOMAIN-SUFFIX,thomanmustore.shop
  - [blackmatrix7 ChinaMaxNoIP Domain] 6a805ca8a10b  DOMAIN-SUFFIX,cyegushi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6bea99e6f901  DOMAIN-SUFFIX,ddxs.vip
  - [blackmatrix7 ChinaMaxNoIP Domain] 6ddeb41bdbde  DOMAIN-SUFFIX,xuanshu.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 6edb02b14846  DOMAIN-SUFFIX,pengliao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6f2569c71454  DOMAIN-SUFFIX,kilo1kw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 72ef5e9cba9c  DOMAIN-SUFFIX,pansousuo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 745e666c0913  DOMAIN-SUFFIX,lanconvey.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 78a3a2643103  DOMAIN-SUFFIX,phpcashshare.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 78d3015a5e1b  DOMAIN-SUFFIX,jufengwuxi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 817de2b65c27  DOMAIN-SUFFIX,baofu.art
  - [blackmatrix7 ChinaMaxNoIP Domain] 821b5858d2b5  DOMAIN-SUFFIX,xiguang.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 8555f808ff6a  DOMAIN-SUFFIX,aliedge.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 86a62a7703c8  DOMAIN-SUFFIX,xegymyb.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 8bd2a50af37e  DOMAIN-SUFFIX,abbreviat.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 8c46d83eed7a  DOMAIN-SUFFIX,smartyun8.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 91bd4d456302  DOMAIN-SUFFIX,ax196.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 91c3d1107ce2  DOMAIN-SUFFIX,rongbst.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 929d712bc46e  DOMAIN-SUFFIX,817398.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 94695e09b03f  DOMAIN-SUFFIX,zjhxw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 996567552974  DOMAIN-SUFFIX,gxzdyg.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 9a53fb79b579  DOMAIN-SUFFIX,zobmxcfw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 9b32c606806c  DOMAIN-SUFFIX,ictdns.icu
  - [blackmatrix7 ChinaMaxNoIP Domain] 9e6c84134120  DOMAIN-SUFFIX,tywbw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 9ff7a94c9454  DOMAIN-SUFFIX,na.ci
  - [blackmatrix7 ChinaMaxNoIP Domain] a0a6c95cc089  DOMAIN-SUFFIX,hk0523.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a12b17315a9b  DOMAIN-SUFFIX,byd119.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a4de6458a69c  DOMAIN-SUFFIX,706net.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a6b7582422f3  DOMAIN-SUFFIX,bbgsite.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a6d10cab4c8f  DOMAIN-SUFFIX,dahongtec.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a74cba319a78  DOMAIN-SUFFIX,online-phaidon.shop
  - [blackmatrix7 ChinaMaxNoIP Domain] a834334a928f  DOMAIN-SUFFIX,gxhuachi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] b17193ccadac  DOMAIN-SUFFIX,xueshujia.com
  - [blackmatrix7 ChinaMaxNoIP Domain] b253a9682674  DOMAIN-SUFFIX,bhjinghao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] b257e0bb6b54  DOMAIN-SUFFIX,gexiao.me
  - [blackmatrix7 ChinaMaxNoIP Domain] b5b1da007997  DOMAIN-SUFFIX,c57fbfc585.skin
  - [blackmatrix7 ChinaMaxNoIP Domain] b7ccce06ab9a  DOMAIN-SUFFIX,bjqhgjj.com
  - [blackmatrix7 ChinaMaxNoIP Domain] b7e2d621ce43  DOMAIN-SUFFIX,gdgwyw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] bcb858322e77  DOMAIN-SUFFIX,dalelingtea.com
  - [blackmatrix7 ChinaMaxNoIP Domain] c566650c4982  DOMAIN-SUFFIX,heijiao.net
  - [blackmatrix7 ChinaMaxNoIP Domain] c575bb9e7ea8  DOMAIN-SUFFIX,dingdongmao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] c582c3d6950e  DOMAIN-SUFFIX,cnfiberhome.com
  - [blackmatrix7 ChinaMaxNoIP Domain] c644f007ada4  DOMAIN-SUFFIX,weareing.store
  - [blackmatrix7 ChinaMaxNoIP Domain] c81a59f6ce13  DOMAIN-SUFFIX,021-116114.com
  - [blackmatrix7 ChinaMaxNoIP Domain] c8d303a34af8  DOMAIN-SUFFIX,skd6.com
  - [blackmatrix7 ChinaMaxNoIP Domain] cb0a23dd7cff  DOMAIN-SUFFIX,ctic-lab.com
  - [blackmatrix7 ChinaMaxNoIP Domain] cd797b2e509d  DOMAIN-SUFFIX,ikncn.com
  - [blackmatrix7 ChinaMaxNoIP Domain] db6803e9dba4  DOMAIN-SUFFIX,panggugu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] dbad50b3df20  DOMAIN-SUFFIX,cgiumuo.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] e4ac4eb7f8b1  DOMAIN-SUFFIX,ponging.store
  - [blackmatrix7 ChinaMaxNoIP Domain] e5c1221b78cf  DOMAIN-SUFFIX,floatmaze.com
  - [blackmatrix7 ChinaMaxNoIP Domain] e78c76cafc4a  DOMAIN-SUFFIX,yzjdgs88.com
  - [blackmatrix7 ChinaMaxNoIP Domain] e8450c7074c8  DOMAIN-SUFFIX,iqunix.store
  - [blackmatrix7 ChinaMaxNoIP Domain] e8e8d013656b  DOMAIN-SUFFIX,download.microsoft.com
  - [blackmatrix7 ChinaMaxNoIP Domain] e9ad9c7e6588  DOMAIN-SUFFIX,fuxinews.com
  - [blackmatrix7 ChinaMaxNoIP Domain] eb0be7852ae9  DOMAIN-SUFFIX,phonelinksoft.com
  - [blackmatrix7 ChinaMaxNoIP Domain] f2357d4c3e97  DOMAIN-SUFFIX,qyhgsb.com
  - [blackmatrix7 ChinaMaxNoIP Domain] f54afb72fbc2  DOMAIN-SUFFIX,dytt2028.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] f68f374d1d05  DOMAIN-SUFFIX,famoustone.com
  - [blackmatrix7 ChinaMaxNoIP Domain] f8fb74e0c2a9  DOMAIN-SUFFIX,imtics.com
  - [blackmatrix7 ChinaMaxNoIP Domain] f9cfff51a54a  DOMAIN-SUFFIX,lighting-china.net
  - [blackmatrix7 ChinaMaxNoIP Domain] fb709d225c7c  DOMAIN-SUFFIX,8379888.com
  - [blackmatrix7 ChinaMaxNoIP Domain] fc117f5cef95  DOMAIN-SUFFIX,soyouso.com
  - [blackmatrix7 ChinaMaxNoIP Domain] fdeb03d73e1f  DOMAIN-SUFFIX,xn--wbsz85a2a.com
```

## China_IP.list

**Added: 346** (showing first 100)
```
  + [Loyalsoldier China CIDR] 021d872078f8  IP-CIDR,170.33.136.0/23
  + [Loyalsoldier China CIDR] 023a65fa0295  IP-CIDR,198.11.128.0/20
  + [Loyalsoldier China CIDR] 0371d7c0ed16  IP-CIDR,47.89.84.0/24
  + [Loyalsoldier China CIDR] 03a4e9468281  IP-CIDR,8.212.0.0/18
  + [Loyalsoldier China CIDR] 03bff4aedd02  IP-CIDR,8.220.176.0/20
  + [Loyalsoldier China CIDR] 042c6d58af98  IP-CIDR,47.246.84.0/22
  + [Loyalsoldier China CIDR] 04db2ac3c2ee  IP-CIDR,8.220.96.0/20
  + [Loyalsoldier China CIDR] 05347ca60f60  IP-CIDR,47.77.96.0/20
  + [Loyalsoldier China CIDR] 0540391c04a3  IP-CIDR,47.235.8.0/22
  + [Loyalsoldier China CIDR] 05b2fd575278  IP-CIDR,47.80.0.0/14
  + [Loyalsoldier China CIDR] 05f11067c460  IP-CIDR,47.246.122.0/23
  + [Loyalsoldier China CIDR] 0714d9a34244  IP-CIDR,139.95.16.0/22
  + [Loyalsoldier China CIDR] 081d35289161  IP-CIDR,8.218.0.0/15
  + [Loyalsoldier China CIDR] 08ccecb030d3  IP-CIDR,8.221.144.0/21
  + [Loyalsoldier China CIDR] 0959c92f89e0  IP-CIDR6,240b:4002:8000::/33
  + [Loyalsoldier China CIDR] 097eca69d164  IP-CIDR,170.33.130.0/23
  + [Loyalsoldier China CIDR] 0a0c736fbe8f  IP-CIDR,156.236.17.0/24
  + [Loyalsoldier China CIDR] 0ae045dedca5  IP-CIDR,47.89.90.0/24
  + [Loyalsoldier China CIDR] 0ae706b44a64  IP-CIDR6,240b:400c::/30
  + [Loyalsoldier China CIDR] 0b5b67ccaef2  IP-CIDR,47.237.128.0/18
  + [Loyalsoldier China CIDR] 0cafff9471fc  IP-CIDR,47.87.32.0/19
  + [Loyalsoldier China CIDR] 0e107318debe  IP-CIDR,8.208.144.0/20
  + [Loyalsoldier China CIDR] 0e52bb251e1f  IP-CIDR,47.57.128.0/18
  + [Loyalsoldier China CIDR] 0eff9ebbabc2  IP-CIDR,14.1.112.0/22
  + [Loyalsoldier China CIDR] 0f02ef47e587  IP-CIDR,47.89.96.0/20
  + [Loyalsoldier China CIDR] 11038c6ff91e  IP-CIDR,149.129.16.0/21
  + [Loyalsoldier China CIDR] 11c1fbc1543c  IP-CIDR,8.212.104.0/21
  + [Loyalsoldier China CIDR] 1299029ba5c9  IP-CIDR,47.251.136.0/21
  + [Loyalsoldier China CIDR] 13620af244de  IP-CIDR,47.246.72.0/21
  + [Loyalsoldier China CIDR] 1461c4a09574  IP-CIDR6,2402:7da0::/32
  + [Loyalsoldier China CIDR] 14d43665240e  IP-CIDR,8.220.232.0/22
  + [Loyalsoldier China CIDR] 15680e99e598  IP-CIDR,8.211.232.0/21
  + [Loyalsoldier China CIDR] 15b5de0749be  IP-CIDR6,240b:4002:1100::/40
  + [Loyalsoldier China CIDR] 15f3a542a769  IP-CIDR,47.237.0.0/17
  + [Loyalsoldier China CIDR] 1686913eea3a  IP-CIDR,47.246.91.0/24
  + [Loyalsoldier China CIDR] 18f56acd4438  IP-CIDR,139.95.64.0/23
  + [Loyalsoldier China CIDR] 1a06a98216e2  IP-CIDR,139.95.96.0/22
  + [Loyalsoldier China CIDR] 1a14e69654ba  IP-CIDR6,240b:4006:1100::/45
  + [Loyalsoldier China CIDR] 1ab7f7ffc509  IP-CIDR,170.33.192.0/23
  + [Loyalsoldier China CIDR] 1afef130d660  IP-CIDR,139.95.128.0/17
  + [Loyalsoldier China CIDR] 1b65088bead1  IP-CIDR,8.222.0.0/15
  + [Loyalsoldier China CIDR] 1b684a9faa15  IP-CIDR6,2404:2280:1000::/36
  + [Loyalsoldier China CIDR] 1ca7f1ab8abf  IP-CIDR,8.209.36.0/22
  + [Loyalsoldier China CIDR] 1cc63e17d4fc  IP-CIDR,139.95.40.0/23
  + [Loyalsoldier China CIDR] 1d0e0fa94db9  IP-CIDR6,240b:400b::/32
  + [Loyalsoldier China CIDR] 1e6bc3967f86  IP-CIDR,170.33.64.0/23
  + [Loyalsoldier China CIDR] 2177e521e5dc  IP-CIDR,47.57.200.0/21
  + [Loyalsoldier China CIDR] 21d28b383b2b  IP-CIDR,8.208.0.0/17
  + [Loyalsoldier China CIDR] 2231de14ac16  IP-CIDR,8.211.0.0/17
  + [Loyalsoldier China CIDR] 2366dc149a49  IP-CIDR,5.181.224.0/23
  + [Loyalsoldier China CIDR] 2476352a3b01  IP-CIDR,47.246.131.0/24
  + [Loyalsoldier China CIDR] 2489f9568f8a  IP-CIDR,47.236.0.0/17
  + [Loyalsoldier China CIDR] 24956b770edc  IP-CIDR,47.87.144.0/21
  + [Loyalsoldier China CIDR] 24a4a07c7b77  IP-CIDR,8.214.164.0/22
  + [Loyalsoldier China CIDR] 256a2b090cc3  IP-CIDR,47.77.24.0/22
  + [Loyalsoldier China CIDR] 260ba2bc2f34  IP-CIDR6,2404:2280:2000::/35
  + [Loyalsoldier China CIDR] 2635e32da172  IP-CIDR,8.208.160.0/19
  + [Loyalsoldier China CIDR] 28f443d1e57b  IP-CIDR,43.92.0.0/15
  + [Loyalsoldier China CIDR] 29043c807dc1  IP-CIDR,47.246.135.0/24
  + [Loyalsoldier China CIDR] 2938af393a14  IP-CIDR,8.212.80.0/21
  + [Loyalsoldier China CIDR] 2a24a8de60e6  IP-CIDR,8.221.0.0/17
  + [Loyalsoldier China CIDR] 2a26903fbbb6  IP-CIDR,47.238.32.0/19
  + [Loyalsoldier China CIDR] 2b19a4c5a359  IP-CIDR,47.251.224.0/19
  + [Loyalsoldier China CIDR] 2c328b3f4eee  IP-CIDR,47.246.32.0/22
  + [Loyalsoldier China CIDR] 2eb6c0a1fddf  IP-CIDR6,240b:4002:1080::/41
  + [Loyalsoldier China CIDR] 30a216ae0450  IP-CIDR,47.251.132.0/22
  + [Loyalsoldier China CIDR] 31323f9a79a5  IP-CIDR,156.245.1.0/24
  + [Loyalsoldier China CIDR] 314fdd0641ec  IP-CIDR6,2404:2280:4000::/36
  + [Loyalsoldier China CIDR] 317aef7bde52  IP-CIDR,149.129.0.0/20
  + [Loyalsoldier China CIDR] 31ba7a119d50  IP-CIDR,47.56.0.0/16
  + [Loyalsoldier China CIDR] 322c1ac0c9bd  IP-CIDR,47.246.136.0/21
  + [Loyalsoldier China CIDR] 326dc654a6f1  IP-CIDR,8.208.140.0/22
  + [Loyalsoldier China CIDR] 32b92483689c  IP-CIDR,8.212.192.0/18
  + [Loyalsoldier China CIDR] 33239b5b7080  IP-CIDR,47.236.192.0/20
  + [Loyalsoldier China CIDR] 36734f7d2746  IP-CIDR,47.57.192.0/22
  + [Loyalsoldier China CIDR] 3876a32b10cb  IP-CIDR,47.90.128.0/19
  + [Loyalsoldier China CIDR] 39cf394b2a98  IP-CIDR,8.220.160.0/21
  + [Loyalsoldier China CIDR] 3b38081bef28  IP-CIDR,147.139.240.0/21
  + [Loyalsoldier China CIDR] 3b7ff0339420  IP-CIDR,47.237.192.0/19
  + [Loyalsoldier China CIDR] 3bf412e9f733  IP-CIDR,47.238.16.0/21
  + [Loyalsoldier China CIDR] 3bfba9fe5db8  IP-CIDR,47.246.92.0/23
  + [Loyalsoldier China CIDR] 3ce3cb5c6e7d  IP-CIDR,8.216.72.0/22
  + [Loyalsoldier China CIDR] 3da243482da2  IP-CIDR6,240b:401f::/32
  + [Loyalsoldier China CIDR] 3da6a3a1d57f  IP-CIDR,8.212.88.0/22
  + [Loyalsoldier China CIDR] 3e913e790f4a  IP-CIDR,47.87.96.0/19
  + [Loyalsoldier China CIDR] 3fd5f7c22656  IP-CIDR6,240b:4002:1400::/38
  + [Loyalsoldier China CIDR] 412d4e5aa133  IP-CIDR,47.238.64.0/18
  + [Loyalsoldier China CIDR] 413d78e78f1f  IP-CIDR,47.246.128.0/23
  + [Loyalsoldier China CIDR] 41c4c7e2e0dc  IP-CIDR,47.246.164.0/22
  + [Loyalsoldier China CIDR] 42b81d52ac1a  IP-CIDR6,2a04:3e00:1002::/47
  + [Loyalsoldier China CIDR] 4326002c233d  IP-CIDR,47.244.0.0/16
  + [Loyalsoldier China CIDR] 43b5bdd7a7af  IP-CIDR,47.85.128.0/23
  + [Loyalsoldier China CIDR] 43f5583f688d  IP-CIDR,8.220.64.0/19
  + [Loyalsoldier China CIDR] 441cef0be6cd  IP-CIDR,47.237.249.0/24
  + [Loyalsoldier China CIDR] 445bcfc11673  IP-CIDR,149.129.128.0/19
  + [Loyalsoldier China CIDR] 44ca3346e359  IP-CIDR6,240b:4006:110c::/46
  + [Loyalsoldier China CIDR] 44d767423efb  IP-CIDR6,240b:4002:1018::/45
  + [Loyalsoldier China CIDR] 47377d5365e1  IP-CIDR,8.220.192.0/19
  + [Loyalsoldier China CIDR] 47afd48d9127  IP-CIDR,47.87.0.0/20
  + [Loyalsoldier China CIDR] 48469d294288  IP-CIDR6,240b:4006:1020::/44
  ... and 246 more
```

**Removed: 15** (showing first 15)
```
  - [blackmatrix7 China IPs] 0e852bd7b7b4  IP-CIDR,47.89.29.9/32
  - [blackmatrix7 China IPs] 157f9912c2e5  IP-CIDR,43.93.0.0/16
  - [Loyalsoldier China CIDR] 1ad4d4996292  IP-CIDR6,2a04:f580:9080::/48
  - [Loyalsoldier China CIDR] 2c548b466eb8  IP-CIDR,183.91.63.0/24
  - [Loyalsoldier China CIDR] 533149645279  IP-CIDR6,2a0a:d681:f000::/37
  - [Loyalsoldier China CIDR] 62250b972899  IP-CIDR6,2a04:f580:9030::/48
  - [blackmatrix7 China IPs] 7a99a03c121a  IP-CIDR,47.75.173.181/32
  - [Loyalsoldier China CIDR] 96f89f2dc2a6  IP-CIDR,163.223.217.0/24
  - [blackmatrix7 China IPs] 9bd9c6e6f66c  IP-CIDR,8.210.152.255/32
  - [blackmatrix7 China IPs] bee46221c2af  IP-CIDR,139.95.4.34/32
  - [Loyalsoldier China CIDR] d2ac6cf9826a  IP-CIDR6,2a0a:d681:fe00::/40
  - [blackmatrix7 China IPs] d6bc8422426b  IP-CIDR,43.92.0.0/17
  - [blackmatrix7 China IPs] e2d523b6d8e5  IP-CIDR,47.75.177.197/32
  - [Loyalsoldier China CIDR] e8575b7c40b2  IP-CIDR6,2a0a:d681:f800::/38
  - [Loyalsoldier China CIDR] eb029f4e8c5c  IP-CIDR6,2a04:3e00:1002::/48
```

**Source changed: 12**
```
  ~ 49b9f98b2220: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 0d1f2138e52c: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d58cf27ea800: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 610880638560: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ bc7602d25a14: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 25a3f0f271e6: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ fb25eb56def0: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 01b2c1f3fc06: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ ac3241b8b526: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 88dc25288775: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 80f5e647298f: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ aa20a14a3676: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Global.list

**Added: 6** (showing first 6)
```
  + [blackmatrix7 Global] 334d4facc27a  DOMAIN-SUFFIX,bscdnweb.com
  + [blackmatrix7 Global] 4a83ab2c71ea  DOMAIN-SUFFIX,sonymusic.com.hk
  + [blackmatrix7 Global] 6bbc523b2e20  DOMAIN-SUFFIX,sonyinteractive.com
  + [blackmatrix7 Global] 81f1c899f66a  DOMAIN-SUFFIX,7x24hrs.com
  + [blackmatrix7 Global] 8ca1664b8328  DOMAIN-SUFFIX,sony.com.py
  + [blackmatrix7 Global] c9a81e218c45  DOMAIN-SUFFIX,scea.com
```

## Speedtest.list

**Added: 185** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 01795d9e086e  DOMAIN,speedtest.mvdsl.com
  + [SukkaW Speedtest Servers International] 026e44155485  DOMAIN,stnanaimowireless.rogers.com
  + [SukkaW Speedtest Servers International] 06233ead16e3  DOMAIN,speedtest.phoenix.xiber.net
  + [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  + [SukkaW Speedtest Servers International] 0800ee424fae  DOMAIN,speedtest.frontlineinternetservices.com
  + [SukkaW Speedtest Servers International] 082c5acfbfb8  DOMAIN,spd-sndgcajw.wyyerd.io
  + [SukkaW Speedtest Servers International] 094cf4e8e364  DOMAIN,speedtest02.coppernet.net
  + [SukkaW Speedtest Servers International] 0a21ac426b0c  DOMAIN,speedtest.octaplus.uk
  + [SukkaW Speedtest Servers International] 0d0d03558cd2  DOMAIN,speed1.tij.attmex.mx
  + [SukkaW Speedtest Servers International] 0d3dfe4cb10b  DOMAIN,speedtest.valleycom.com
  + [SukkaW Speedtest Servers International] 0da9f0879dcc  DOMAIN,speedtestbirpara.meghbelabroadband.in
  + [SukkaW Speedtest Servers International] 0dbbbe7da5ea  DOMAIN,speedtest.wnmc.com
  + [SukkaW Speedtest Servers International] 0edf466de81a  DOMAIN,de.riospeed.com
  + [SukkaW Speedtest Servers International] 0f0b324eafca  DOMAIN,speed.webseitenserver.com
  + [SukkaW Speedtest Servers International] 120ef88aa2bc  DOMAIN,stsurreywireless.rogers.com
  + [SukkaW Speedtest Servers International] 15a31d154f70  DOMAIN,speed.catlabroadband.in
  + [SukkaW Speedtest Servers International] 15c5e928553f  DOMAIN,spd1.m5hosting.com
  + [SukkaW Speedtest Servers International] 179230a805a0  DOMAIN,speedtest.tularosa.net
  + [SukkaW Speedtest Servers International] 18669947d48d  DOMAIN,speedtest.ed.shawcable.net
  + [SukkaW Speedtest Servers International] 188233ec18b6  DOMAIN,laxir0008speedtestserver01.wiline.com
  + [SukkaW Speedtest Servers International] 1aab8ac0b3c7  DOMAIN,speedtest-sd-da1.scalematrix.com
  + [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  + [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 20b5384a3b6f  DOMAIN,stlethbridgewireless.rogers.com
  + [SukkaW Speedtest Servers International] 20cf10887c86  DOMAIN,speedtest2.co-fi.es
  + [SukkaW Speedtest Servers International] 2287e9ddefd2  DOMAIN,stcalgarywireless.rogers.com
  + [SukkaW Speedtest Servers International] 22a64e3ce5a5  DOMAIN,speedtest.skybbservices.com
  + [SukkaW Speedtest Servers International] 22ba33ffb1f2  DOMAIN,acrenettecnologia.brsserver.com.br
  + [SukkaW Speedtest Servers International] 23ab4abca32e  DOMAIN,speedtest.phoenixnap.com
  + [SukkaW Speedtest Servers International] 23b5aa93110d  DOMAIN,sp1.semfronteiras.net.br
  + [SukkaW Speedtest Servers International] 246e115e5220  DOMAIN,srv1297868.hstgr.cloud
  + [SukkaW Speedtest Servers International] 296c2479f156  DOMAIN,speedtest.3dprintingduo.ca
  + [SukkaW Speedtest Servers International] 297f9b1bd0a2  DOMAIN,speedtest.server.battern.eu
  + [SukkaW Speedtest Servers International] 2b2178711627  DOMAIN,speedtest.sinetonline.net
  + [SukkaW Speedtest Servers International] 2b71ebccbca0  DOMAIN,speedtest.jackrabbitwireless.com
  + [SukkaW Speedtest Servers International] 2bf6e39176af  DOMAIN,spd01-monr-ca.gigglefiber.com
  + [SukkaW Speedtest Servers International] 2c906a0d677f  DOMAIN,kmlpbcnu-speedtest-01.telus.com
  + [SukkaW Speedtest Servers International] 2ed4e4b680a5  DOMAIN,sptst1.ntua.net
  + [SukkaW Speedtest Servers International] 2ff46c1e7e09  DOMAIN,speedtesttucson.arkdnacloud.com
  + [SukkaW Speedtest Servers International] 31c231df84b9  DOMAIN,speedtest5.nmsurf.com
  + [SukkaW Speedtest Servers International] 328d6a694672  DOMAIN,riospeedtest.rconnects.com
  + [SukkaW Speedtest Servers International] 333696efac80  DOMAIN,speedtest.meghlink.com
  + [SukkaW Speedtest Servers International] 33607daf687c  DOMAIN,santaclara-speedtest.utopiafiber.com
  + [SukkaW Speedtest Servers International] 344541cfed53  DOMAIN,ookla-lyo.services.proxad.net
  + [SukkaW Speedtest Servers International] 365fc1f3200d  DOMAIN,speedtest3.sasknet.sk.ca
  + [SukkaW Speedtest Servers International] 36b21f97c505  DOMAIN,speedtest4.plateautel.net
  + [SukkaW Speedtest Servers International] 385ceaa782b7  DOMAIN,speedtest.csfibernet.in
  + [SukkaW Speedtest Servers International] 3a74920167e4  DOMAIN,teste.mwhtelecom.com.br
  + [SukkaW Speedtest Servers International] 3e5e286668c0  DOMAIN,speedtest.symbiosbroadband.net
  + [SukkaW Speedtest Servers International] 404a159ee121  DOMAIN,avspeedtest.apfutura.net
  + [SukkaW Speedtest Servers International] 4442ff60c35a  DOMAIN,speedtest.ftmojave.net
  + [SukkaW Speedtest Servers International] 451355c159de  DOMAIN,speedtest-az.bambroadband.com
  + [SukkaW Speedtest Servers International] 457c7c64a7cb  DOMAIN,prescott1.cabospeed.com
  + [SukkaW Speedtest Servers International] 4711a85a14ce  DOMAIN,speedtest.cdpalace.in
  + [SukkaW Speedtest Servers International] 497d447ac483  DOMAIN,speedtest.gilarivertel.com
  + [SukkaW Speedtest Servers International] 4c233c67db7d  DOMAIN,speed.laurensk.nl
  + [SukkaW Speedtest Servers International] 4c343b690433  DOMAIN,speedtest4.ezeefiber.net
  + [SukkaW Speedtest Servers International] 4ff867dabe73  DOMAIN,speedtestslg.alliancebroadband.in
  + [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  + [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  + [SukkaW Speedtest Servers International] 51ab10282432  DOMAIN,speedtest.infowest.com
  + [SukkaW Speedtest Servers International] 51cd85bbddab  DOMAIN,speedtest.fra.plusnet.de
  + [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  + [SukkaW Speedtest Servers International] 5356e4886192  DOMAIN,speedtesthost.sasknet.sk.ca
  + [SukkaW Speedtest Servers International] 53e6f989e749  DOMAIN,riorancho1.cabospeed.com
  + [SukkaW Speedtest Servers International] 56784b2201f6  DOMAIN,spd-phnhazva.wyyerd.io
  + [SukkaW Speedtest Servers International] 58514000804b  DOMAIN,slgrooklaspeed1.jioconnect.com
  + [SukkaW Speedtest Servers International] 58853cdc4bf0  DOMAIN,speedtest.thryve.com.au
  + [SukkaW Speedtest Servers International] 58a70fe3f134  DOMAIN,speedtest7.vodafone.com.tr
  + [SukkaW Speedtest Servers International] 58d5ea3bc911  DOMAIN,speedtest.gv.shawcable.net
  + [SukkaW Speedtest Servers International] 5ee6efe075b3  DOMAIN,speedtest.ngcbroadband.com
  + [SukkaW Speedtest Servers International] 5fbb145eb5ba  DOMAIN,speedtest.kouten.barcelona
  + [SukkaW Speedtest Servers International] 62a3774a6ad0  DOMAIN,velocimetro-rbo.virtua.com.br
  + [SukkaW Speedtest Servers International] 646f766c0f34  DOMAIN,speedtest.unmbroadbandservice.com
  + [SukkaW Speedtest Servers International] 64a7282a2dd7  DOMAIN,speed.coe.ad.jp
  + [SukkaW Speedtest Servers International] 658a714cbecd  DOMAIN,sp1.contilnet.net
  + [SukkaW Speedtest Servers International] 67a9c4720203  DOMAIN,speedtest.skaybroadband.com
  + [SukkaW Speedtest Servers International] 6992afbc4517  DOMAIN,phoenix1.cabospeed.com
  + [SukkaW Speedtest Servers International] 69eb17adddcb  DOMAIN,sp1.socen.com
  + [SukkaW Speedtest Servers International] 6b49fe0152c9  DOMAIN,spd49.claro.com.br
  + [SukkaW Speedtest Servers International] 6be2d4ce5009  DOMAIN,lv-ookla.geolinks.com
  + [SukkaW Speedtest Servers International] 7234c43482c2  DOMAIN,speedtest.ioflood.com
  + [SukkaW Speedtest Servers International] 723b77b1998b  DOMAIN,speedtestalbq.vexusfiber.com
  + [SukkaW Speedtest Servers International] 73e966caf50f  DOMAIN,spd-phnxaz19.wyyerd.io
  + [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 7737d7921c63  DOMAIN,sp2.semfronteiras.net.br
  + [SukkaW Speedtest Servers International] 7785c86daf50  DOMAIN,speedtest.sizatek.com
  + [SukkaW Speedtest Servers International] 77de3e0d51c6  DOMAIN,test.beamtelecom.com.br
  + [SukkaW Speedtest Servers International] 78bb50fdaca3  DOMAIN,velocimetro.govistabr.com.br
  + [SukkaW Speedtest Servers International] 7935cf977efe  DOMAIN,speedtest.wwfn.ca
  + [SukkaW Speedtest Servers International] 79fd2808f8ae  DOMAIN,speedtest-jgn.galaxynet.in
  + [SukkaW Speedtest Servers International] 7a26c3838cf7  DOMAIN,speedtest.centralnetprovedor.net.br
  + [SukkaW Speedtest Servers International] 7ad78e8435d7  DOMAIN,speed.ddbroadband.co.in
  + [SukkaW Speedtest Servers International] 7cbea7792619  DOMAIN,ookla-dc3.services.proxad.net
  + [SukkaW Speedtest Servers International] 7dbab91ba126  DOMAIN,urbanonet.brsserver.com.br
  + [SukkaW Speedtest Servers International] 7dca5c54a963  DOMAIN,sp2.janusnetworks.com
  + [SukkaW Speedtest Servers International] 801ce09cf1ca  DOMAIN,sp3.basinbroadband.ca
  + [SukkaW Speedtest Servers International] 802f6bb88d3d  DOMAIN,speedtestversatile.meghbelabroadband.in
  + [SukkaW Speedtest Servers International] 80c21f51b1f6  DOMAIN,hv1.juce.ca
  + [SukkaW Speedtest Servers International] 80cf33496fd0  DOMAIN,albuquerque-speedtest.sacredwindcommunications.com
  ... and 85 more
```

**Removed: 148** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 0009d45cc71f  DOMAIN,speedtest-gdrp.merit.edu
  - [SukkaW Speedtest Servers International] 00f2d0dd6105  DOMAIN,stmilton.rogers.com
  - [SukkaW Speedtest Servers International] 02d48045e4e3  DOMAIN,speed12.gonetspeed.com
  - [SukkaW Speedtest Servers International] 030afc0d216e  DOMAIN,sthamiltonwireless.rogers.com
  - [SukkaW Speedtest Servers International] 0561b044089c  DOMAIN,ran-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 0711f9d6046b  DOMAIN,cbpuspeed.aspensmart.net
  - [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  - [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  - [SukkaW Speedtest Servers International] 0f0435a45fac  DOMAIN,speedtest.oa.net
  - [SukkaW Speedtest Servers International] 0f923e75457a  DOMAIN,ookla-in.mercuryfiber.com
  - [SukkaW Speedtest Servers International] 134564537572  DOMAIN,speedtest.sycmilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 15ee8e1a505a  DOMAIN,speedtest.volo.net
  - [SukkaW Speedtest Servers International] 1683191aa4e7  DOMAIN,stwoodstock.rogers.com
  - [SukkaW Speedtest Servers International] 1753c7265a8d  DOMAIN,st1.ligtel.com
  - [SukkaW Speedtest Servers International] 180017a0d2ce  DOMAIN,stmiltonwireless.rogers.com
  - [SukkaW Speedtest Servers International] 1debbecee8c5  DOMAIN,speedtest.cstech.com
  - [SukkaW Speedtest Servers International] 22e17aa36c22  DOMAIN,speedtest-wc.truestreamfiber.us
  - [SukkaW Speedtest Servers International] 238c177c28d4  DOMAIN,speedtest.maisnetfibra.net.br
  - [SukkaW Speedtest Servers International] 27aa9cef1e30  DOMAIN,bytp-speedtest-1.123.net
  - [SukkaW Speedtest Servers International] 2893bfbf70c6  DOMAIN,speedtest.fibernetics.ca
  - [SukkaW Speedtest Servers International] 2a475faf88d3  DOMAIN,spdtst-southbend.fourway.net
  - [SukkaW Speedtest Servers International] 2b911d71aa37  DOMAIN,speedtest.i3broadband.com
  - [SukkaW Speedtest Servers International] 2c4e9bf40557  DOMAIN,velocity.softtelecom.net.br
  - [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  - [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  - [SukkaW Speedtest Servers International] 3556421114ed  DOMAIN,sthamilton.netcrawler.ca
  - [SukkaW Speedtest Servers International] 36366555a5b5  DOMAIN,ookla.mu.as6453.net
  - [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  - [SukkaW Speedtest Servers International] 3ddb6b00187f  DOMAIN,stoakville.rogers.com
  - [SukkaW Speedtest Servers International] 3e7fd288e9dc  DOMAIN,ookla.pgservicos.net.br
  - [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  - [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  - [SukkaW Speedtest Servers International] 45f4d00908d6  DOMAIN,speedtest-2.hynetwifi.it
  - [SukkaW Speedtest Servers International] 499c1e741ef8  DOMAIN,asanet1.brsserver.com.br
  - [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  - [SukkaW Speedtest Servers International] 4bc5bacc9435  DOMAIN,sp2.fibreair.in
  - [SukkaW Speedtest Servers International] 4c2f2196bc2e  DOMAIN,ookla.lunoxia.net
  - [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  - [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 4fa503514189  DOMAIN,speedtest.packetworks.net
  - [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  - [SukkaW Speedtest Servers International] 520fc7617d3b  DOMAIN,speed-oak.systemlifeline.com
  - [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  - [SukkaW Speedtest Servers International] 56ca52c088ca  DOMAIN,speedtest.cogeco.ca
  - [SukkaW Speedtest Servers International] 5a8191463e31  DOMAIN,stmississauga.netcrawler.ca
  - [SukkaW Speedtest Servers International] 5b59c5167680  DOMAIN,sqaookla.ddns.net
  - [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  - [SukkaW Speedtest Servers International] 5d91b2e1e426  DOMAIN,stgeorgetownwireless.rogers.com
  - [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  - [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  - [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  - [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  - [SukkaW Speedtest Servers International] 6382a86a4d91  DOMAIN,speed.telcomnetwork.net
  - [SukkaW Speedtest Servers International] 67fb222e7169  DOMAIN,stbrampton.rogers.com
  - [SukkaW Speedtest Servers International] 69cac5e64f73  DOMAIN,stbrantfordwireless.rogers.com
  - [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  - [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  - [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  - [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  - [SukkaW Speedtest Servers International] 6f3628eaf259  DOMAIN,stkitchener.rogers.com
  - [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  - [SukkaW Speedtest Servers International] 73112e9dc2cb  DOMAIN,speedtest01.adl1.spintel.net.au
  - [SukkaW Speedtest Servers International] 75e802499b21  DOMAIN,stbrampton.netcrawler.ca
  - [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  - [SukkaW Speedtest Servers International] 7b2b5f1619fb  DOMAIN,karnal.sitibroadband.co.in
  - [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 7d5bedcb3b73  DOMAIN,speedtest.routinger.com.br
  - [SukkaW Speedtest Servers International] 7dd1428b51c5  DOMAIN,speedtest-losangeles.ripplefiber.com
  - [SukkaW Speedtest Servers International] 7f8672568a56  DOMAIN,speed-miss.systemlifeline.com
  - [SukkaW Speedtest Servers International] 80caefa0c6bc  DOMAIN,speedtest.almatelecom.es
  - [SukkaW Speedtest Servers International] 81bf88adcc73  DOMAIN,speed.x-idleb.com
  - [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  - [SukkaW Speedtest Servers International] 8614924bdfcd  DOMAIN,speedtest.b3online.es
  - [SukkaW Speedtest Servers International] 87268ce3261b  DOMAIN,teste.routinger.com.br
  - [SukkaW Speedtest Servers International] 8764399208a4  DOMAIN,speedtest.msnetworks.in
  - [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  - [SukkaW Speedtest Servers International] 890fa3aca5ec  DOMAIN,speedtest.orixinet.com.br
  - [SukkaW Speedtest Servers International] 89d9c6207c68  DOMAIN,speedtest.nwlab.org
  - [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  - [SukkaW Speedtest Servers International] 8e36c5eb6ca2  DOMAIN,speedtest2.micronet.in
  - [SukkaW Speedtest Servers International] 8e65c38b8f44  DOMAIN,speedtest.execulink.ca
  - [SukkaW Speedtest Servers International] 8f062e512925  DOMAIN,speedtestsonipat.kkdbroadband.co.in
  - [SukkaW Speedtest Servers International] 92e005ab26ce  DOMAIN,medidor.nortelecom.com.br
  - [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 96692f154a26  DOMAIN,veloteste.mrjomar.com.br
  - [SukkaW Speedtest Servers International] 96de22a6ddc7  DOMAIN,st-rockford.sumofiber.com
  - [SukkaW Speedtest Servers International] 96e261bbbb9d  DOMAIN,speed.tnahosting.net
  - [SukkaW Speedtest Servers International] 9868c3f8fedf  DOMAIN,speedtest.s3rdv.com
  - [SukkaW Speedtest Servers International] 9d2342e15aaa  DOMAIN,stkingcity.netcrawler.ca
  - [SukkaW Speedtest Servers International] a0ed01f03a76  DOMAIN,sp2.realtel.in
  - [SukkaW Speedtest Servers International] a109426d3034  DOMAIN,sthamilton.rogers.com
  - [SukkaW Speedtest Servers International] a2002b5b2805  DOMAIN,speedtest.grr1-mi.incx.net
  - [SukkaW Speedtest Servers International] a31c0a6224a2  DOMAIN,storangeville.rogers.com
  - [SukkaW Speedtest Servers International] a54ecf0fe880  DOMAIN,stbrantford.rogers.com
  - [SukkaW Speedtest Servers International] a58610a5c00e  DOMAIN,mrutooklaspeed1.jioconnect.com
  - [SukkaW Speedtest Servers International] a5a39e69aa44  DOMAIN,speedtest.mhtc.net
  - [SukkaW Speedtest Servers International] a6376fd1ad4b  DOMAIN,st01.fynncloud.net
  ... and 48 more
```
