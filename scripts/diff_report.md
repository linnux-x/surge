# Surge Rule Diff Report
Generated: 2026-11-28T05:00:42.915292

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 4 |
| Rules added | 293 |
| Rules removed | 252 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110667 | 110669 | +3 | -1 | ~0 |
| China_IP.list | 9665 | 9735 | +144 | -74 | ~0 |
| Download.list | 1614 | 1609 | +0 | -5 | ~0 |
| Speedtest.list | 1737 | 1711 | +146 | -172 | ~0 |

## China.list

**Added: 3** (showing first 3)
```
  + [Rabbit-Spec China] 3dafa3595514  DOMAIN-SUFFIX,fazhipro.com
  + [Rabbit-Spec China] 3fb8546f73ff  DOMAIN-SUFFIX,saasfz.com
  + [Rabbit-Spec China] c0dc7b92d1f2  DOMAIN-SUFFIX,echooai.com
```

**Removed: 1** (showing first 1)
```
  - [Rabbit-Spec China] 2a6a2c033ed3  DOMAIN-SUFFIX,xihuan
```

## China_IP.list

**Added: 144** (showing first 100)
```
  + [Loyalsoldier China CIDR] 0064a8e08e75  IP-CIDR,180.223.244.0/22
  + [Loyalsoldier China CIDR] 0473e97ce8e5  IP-CIDR6,2001:df7:d940::/48
  + [Loyalsoldier China CIDR] 06eff7cb4731  IP-CIDR6,2001:df0:d880::/48
  + [Loyalsoldier China CIDR] 0a384708cad6  IP-CIDR,103.73.0.0/19
  + [Loyalsoldier China CIDR] 10c3dde24872  IP-CIDR,223.123.198.0/23
  + [Loyalsoldier China CIDR] 10e546b63ffc  IP-CIDR6,2001:df0:2e80::/48
  + [Loyalsoldier China CIDR] 11b908b93c94  IP-CIDR,180.223.239.0/24
  + [Loyalsoldier China CIDR] 16351ef6a873  IP-CIDR,119.161.224.0/19
  + [Loyalsoldier China CIDR] 184284372fa5  IP-CIDR,180.223.20.0/22
  + [Loyalsoldier China CIDR] 1a7e9f27f37d  IP-CIDR,211.102.144.0/21
  + [Loyalsoldier China CIDR] 1b4dc4262f33  IP-CIDR6,2001:df4:4b80::/48
  + [Loyalsoldier China CIDR] 1e511fff4ddf  IP-CIDR6,2406:840:980d::/48
  + [Loyalsoldier China CIDR] 1e5cb5006b9b  IP-CIDR,150.248.176.0/20
  + [Loyalsoldier China CIDR] 2113d6e07c08  IP-CIDR6,2001:df0:ac40::/48
  + [Loyalsoldier China CIDR] 240ffe2a374c  IP-CIDR6,2001:df3:15c0::/48
  + [Loyalsoldier China CIDR] 241e11cc7cfc  IP-CIDR6,2001:df3:d0c0::/48
  + [Loyalsoldier China CIDR] 2786c9e287d2  IP-CIDR,222.126.192.0/18
  + [Loyalsoldier China CIDR] 28e8cc9c60c1  IP-CIDR,180.223.195.0/24
  + [Loyalsoldier China CIDR] 2b5ad0580ce8  IP-CIDR,222.126.160.0/21
  + [Loyalsoldier China CIDR] 2b9076e87ab6  IP-CIDR,180.223.236.0/23
  + [Loyalsoldier China CIDR] 2e19387609d1  IP-CIDR6,2a0a:d682:e000::/36
  + [Loyalsoldier China CIDR] 2f1da7a4f79c  IP-CIDR,103.150.214.0/24
  + [Loyalsoldier China CIDR] 2f8553f1d580  IP-CIDR,180.223.19.0/24
  + [Loyalsoldier China CIDR] 36ac628a3fba  IP-CIDR6,2001:678:12c4::/48
  + [Loyalsoldier China CIDR] 39b1596d4ec8  IP-CIDR,211.102.156.0/22
  + [Loyalsoldier China CIDR] 3b972f7efeb4  IP-CIDR,180.223.17.0/24
  + [Loyalsoldier China CIDR] 3cc0968447e4  IP-CIDR,202.149.224.0/19
  + [Loyalsoldier China CIDR] 3db2c5a7e54e  IP-CIDR6,2001:df0:9c0::/48
  + [Loyalsoldier China CIDR] 3ef69097e446  IP-CIDR6,2001:4510::/29
  + [Loyalsoldier China CIDR] 3f4199d50d79  IP-CIDR,180.223.28.0/23
  + [Loyalsoldier China CIDR] 426f60d8e780  IP-CIDR,103.132.166.0/23
  + [Loyalsoldier China CIDR] 436515e94536  IP-CIDR6,2001:df3:a680::/48
  + [Loyalsoldier China CIDR] 44e4484634fb  IP-CIDR6,2001:df1:d180::/48
  + [Loyalsoldier China CIDR] 4537cbb68f03  IP-CIDR6,2001:df2:5780::/48
  + [Loyalsoldier China CIDR] 459716f335f5  IP-CIDR6,2001:df0:bf80::/48
  + [Loyalsoldier China CIDR] 4669cef56389  IP-CIDR6,2001:df4:2780::/48
  + [Loyalsoldier China CIDR] 48e71c760e2f  IP-CIDR,180.223.187.0/24
  + [Loyalsoldier China CIDR] 49f3ae300b96  IP-CIDR6,2406:840:9974::/47
  + [Loyalsoldier China CIDR] 4a16ac2b3608  IP-CIDR,150.248.192.0/18
  + [Loyalsoldier China CIDR] 4b2d88c67377  IP-CIDR6,2406:840:980e::/47
  + [Loyalsoldier China CIDR] 532a1d679aae  IP-CIDR6,2001:678:12b8::/48
  + [Loyalsoldier China CIDR] 54f3586a667a  IP-CIDR6,2406:840:c69::/48
  + [Loyalsoldier China CIDR] 5656533361ea  IP-CIDR6,2001:df5:2fc0::/48
  + [Loyalsoldier China CIDR] 56a38f955918  IP-CIDR6,2001:67c:ebc::/48
  + [Loyalsoldier China CIDR] 57f810691820  IP-CIDR,180.223.53.0/24
  + [Loyalsoldier China CIDR] 591ca12309f2  IP-CIDR,180.223.170.0/24
  + [Loyalsoldier China CIDR] 596605201aec  IP-CIDR,183.91.49.0/24
  + [Loyalsoldier China CIDR] 59b6d870c0d1  IP-CIDR6,2001:df6:100::/48
  + [Loyalsoldier China CIDR] 5c271036fa57  IP-CIDR,202.55.27.0/24
  + [Loyalsoldier China CIDR] 5c7627545431  IP-CIDR,103.202.56.0/21
  + [Loyalsoldier China CIDR] 5e66d62df3e7  IP-CIDR6,2400:5a60::/41
  + [Loyalsoldier China CIDR] 61ecb3964b81  IP-CIDR,150.248.0.0/17
  + [Loyalsoldier China CIDR] 635d77a124a1  IP-CIDR6,2001:df4:2e80::/48
  + [Loyalsoldier China CIDR] 6393772a962f  IP-CIDR,180.223.25.0/24
  + [Loyalsoldier China CIDR] 64d4046d5035  IP-CIDR,180.223.178.0/24
  + [Loyalsoldier China CIDR] 661709c4ed56  IP-CIDR6,2001:df2:8bc0::/48
  + [Loyalsoldier China CIDR] 662d0ee1e16f  IP-CIDR6,2001:df6:6800::/48
  + [Loyalsoldier China CIDR] 66379660e08b  IP-CIDR6,2001:67c:a1c::/48
  + [Loyalsoldier China CIDR] 681c752d987c  IP-CIDR6,2001:df1:5280::/48
  + [Loyalsoldier China CIDR] 6afa5cc7f955  IP-CIDR6,2001:7fa:10::/48
  + [Loyalsoldier China CIDR] 6e76624b921e  IP-CIDR,103.104.198.0/23
  + [Loyalsoldier China CIDR] 6fea53611592  IP-CIDR6,2001:df1:6180::/48
  + [Loyalsoldier China CIDR] 707d4ff082d3  IP-CIDR6,2406:840:9978::/45
  + [Loyalsoldier China CIDR] 712112b1fceb  IP-CIDR6,2001:df2:c240::/48
  + [Loyalsoldier China CIDR] 7155e1a74f19  IP-CIDR6,2001:dd8:5::/48
  + [Loyalsoldier China CIDR] 7272254c23d9  IP-CIDR6,2001:df4:c580::/48
  + [Loyalsoldier China CIDR] 7363b93febd5  IP-CIDR6,2001:e80::/32
  + [Loyalsoldier China CIDR] 76eab61f2b48  IP-CIDR,103.202.152.0/21
  + [Loyalsoldier China CIDR] 77f8ab9935fa  IP-CIDR,180.223.180.0/23
  + [Loyalsoldier China CIDR] 781ed4d1a184  IP-CIDR,180.223.174.0/24
  + [Loyalsoldier China CIDR] 7b7538ef62ab  IP-CIDR,103.132.165.0/24
  + [Loyalsoldier China CIDR] 7b7dab27479c  IP-CIDR,180.223.191.0/24
  + [Loyalsoldier China CIDR] 7c954a4dae86  IP-CIDR6,2001:df5:5f80::/48
  + [Loyalsoldier China CIDR] 7cdaf9814a97  IP-CIDR,180.223.165.0/24
  + [Loyalsoldier China CIDR] 7d213268a2bc  IP-CIDR6,2406:840:e400::/39
  + [Loyalsoldier China CIDR] 7e103bbf2182  IP-CIDR6,2001:df0:25c0::/48
  + [Loyalsoldier China CIDR] 7e1ac14a8c72  IP-CIDR6,2001:df3:ef80::/48
  + [Loyalsoldier China CIDR] 7f0a1e6155c7  IP-CIDR6,2001:df7:6600::/48
  + [Loyalsoldier China CIDR] 830195c60280  IP-CIDR6,2001:df3:7440::/48
  + [Loyalsoldier China CIDR] 84e64397c5e4  IP-CIDR,180.223.172.0/24
  + [Loyalsoldier China CIDR] 85a4116df77c  IP-CIDR6,2001:df3:c680::/48
  + [Loyalsoldier China CIDR] 8698609d0ee3  IP-CIDR6,2001:4438::/32
  + [Loyalsoldier China CIDR] 89237248eb2e  IP-CIDR6,2001:df0:f8c0::/48
  + [Loyalsoldier China CIDR] 8a3efd84cc89  IP-CIDR6,2400:9380:9081::/48
  + [Loyalsoldier China CIDR] 8c94e7e404d8  IP-CIDR6,2001:df1:5b80::/48
  + [Loyalsoldier China CIDR] 8f03d65dc96e  IP-CIDR6,2001:df0:1bc0::/48
  + [Loyalsoldier China CIDR] 91143bf43a36  IP-CIDR,222.126.128.0/19
  + [Loyalsoldier China CIDR] 91f19c29c9cd  IP-CIDR6,2001:df2:a580::/48
  + [Loyalsoldier China CIDR] 92b4cef17d31  IP-CIDR6,2001:df4:4d80::/48
  + [Loyalsoldier China CIDR] 956bc2e5e66d  IP-CIDR,180.223.176.0/24
  + [Loyalsoldier China CIDR] 97ab8ceca4c6  IP-CIDR6,2001:daa::/32
  + [Loyalsoldier China CIDR] a6148d4bee83  IP-CIDR6,2406:840:feff::/48
  + [Loyalsoldier China CIDR] a683fd25782f  IP-CIDR,124.21.240.0/20
  + [Loyalsoldier China CIDR] a7133805b6d7  IP-CIDR6,2001:df6:5d00::/48
  + [Loyalsoldier China CIDR] a906fb436fb8  IP-CIDR6,2001:256::/32
  + [Loyalsoldier China CIDR] a9f8044a6dbd  IP-CIDR6,2400:9380:9281::/48
  + [Loyalsoldier China CIDR] aa3b5fbc4dfd  IP-CIDR,180.223.60.0/22
  + [Loyalsoldier China CIDR] aaaaa79eb195  IP-CIDR6,2406:840:9970::/46
  + [Loyalsoldier China CIDR] af765011c92d  IP-CIDR6,2001:f38::/32
  + [Loyalsoldier China CIDR] afdae8084549  IP-CIDR6,2001:df0:9d40::/48
  ... and 44 more
```

**Removed: 74** (showing first 74)
```
  - [Loyalsoldier China CIDR] 094dc62eaf48  IP-CIDR,202.55.31.0/24
  - [Loyalsoldier China CIDR] 0a5815ce98c1  IP-CIDR,202.149.248.0/22
  - [Loyalsoldier China CIDR] 0a7b1cac676f  IP-CIDR6,2406:bdc0::/32
  - [Loyalsoldier China CIDR] 111b92a2d561  IP-CIDR6,2001:daa:4::/47
  - [Loyalsoldier China CIDR] 12ba55493c56  IP-CIDR,103.132.161.0/24
  - [Loyalsoldier China CIDR] 24a7dbcbeeed  IP-CIDR6,2001:da8::/32
  - [Loyalsoldier China CIDR] 2a01002b5ec7  IP-CIDR,124.20.240.0/20
  - [Loyalsoldier China CIDR] 2ae66c22f717  IP-CIDR,103.202.154.0/23
  - [Loyalsoldier China CIDR] 2ce90221a350  IP-CIDR6,2400:5a60:40::/42
  - [Loyalsoldier China CIDR] 34994d6a7704  IP-CIDR6,2001:4510:400::/40
  - [Loyalsoldier China CIDR] 35365212d52b  IP-CIDR6,2406:840:e0ea::/47
  - [Loyalsoldier China CIDR] 3680f542e82f  IP-CIDR,103.73.12.0/22
  - [Loyalsoldier China CIDR] 381d7fa38547  IP-CIDR6,2001:daa:9::/48
  - [Loyalsoldier China CIDR] 394242117622  IP-CIDR6,2400:9380:9280::/47
  - [Loyalsoldier China CIDR] 3e95d2a1856f  IP-CIDR,202.55.24.0/22
  - [Loyalsoldier China CIDR] 3fac3daa6d89  IP-CIDR,183.91.52.0/22
  - [Loyalsoldier China CIDR] 42580c8ca649  IP-CIDR,223.123.196.0/22
  - [Loyalsoldier China CIDR] 447feac517e2  IP-CIDR6,2406:840:e560::/44
  - [Loyalsoldier China CIDR] 45a93a126955  IP-CIDR,202.55.18.0/23
  - [Loyalsoldier China CIDR] 4d26ef8cc1fd  IP-CIDR6,2001:daa:1::/48
  - [Loyalsoldier China CIDR] 4d6574e87223  IP-CIDR6,2406:840:e570::/45
  - [Loyalsoldier China CIDR] 4e81db150fc6  IP-CIDR,103.202.156.0/22
  - [Loyalsoldier China CIDR] 58d9ad8faba1  IP-CIDR,103.104.199.0/24
  - [Loyalsoldier China CIDR] 5a7ba7e659ee  IP-CIDR6,2406:840:e580::/41
  - [Loyalsoldier China CIDR] 5c2be7b88478  IP-CIDR,103.202.152.0/24
  - [Loyalsoldier China CIDR] 5d783f9a2c6e  IP-CIDR,103.73.16.0/20
  - [Loyalsoldier China CIDR] 620f03bd9bcc  IP-CIDR6,2406:840:980c::/46
  - [Loyalsoldier China CIDR] 6318d1a3e8de  IP-CIDR6,2400:5a60:20::/43
  - [Loyalsoldier China CIDR] 72617aa3658f  IP-CIDR6,2406:840:e500::/42
  - [Loyalsoldier China CIDR] 7670faf04ce1  IP-CIDR6,2406:840:e57f::/48
  - [Loyalsoldier China CIDR] 7ffb32aac84f  IP-CIDR6,2001:4511:1480::/41
  - [Loyalsoldier China CIDR] 8113ab73d9f6  IP-CIDR6,2400:5a60:3::/48
  - [Loyalsoldier China CIDR] 87990c3c47a9  IP-CIDR,150.248.0.0/16
  - [Loyalsoldier China CIDR] 8ef12687cce9  IP-CIDR,103.109.106.0/23
  - [Loyalsoldier China CIDR] 9053dd7fec9f  IP-CIDR6,2406:840:e578::/46
  - [Loyalsoldier China CIDR] 92e495c273c6  IP-CIDR6,2001:daa:2::/47
  - [Loyalsoldier China CIDR] 948170ddf5ea  IP-CIDR6,2406:840:9970::/44
  - [Loyalsoldier China CIDR] 95f0eae0020c  IP-CIDR,223.123.205.0/24
  - [Loyalsoldier China CIDR] 9d49eb84dc6e  IP-CIDR,183.91.50.0/24
  - [Loyalsoldier China CIDR] 9e927e1b28dd  IP-CIDR6,2001:4510:1480::/41
  - [Loyalsoldier China CIDR] a591000eeba0  IP-CIDR,124.21.224.0/20
  - [Loyalsoldier China CIDR] a63fdaffe832  IP-CIDR,222.126.128.0/17
  - [Loyalsoldier China CIDR] a748776179af  IP-CIDR6,2400:5a60:10::/44
  - [Loyalsoldier China CIDR] a83717b013e1  IP-CIDR,103.73.10.0/23
  - [Loyalsoldier China CIDR] a8e8998d3c19  IP-CIDR6,2001:daa:6::/48
  - [Loyalsoldier China CIDR] ae0d528cd193  IP-CIDR,103.99.62.0/24
  - [Loyalsoldier China CIDR] b0c9cb51e173  IP-CIDR,124.20.128.0/18
  - [Loyalsoldier China CIDR] b2f8ad9296f7  IP-CIDR,119.161.192.0/18
  - [Loyalsoldier China CIDR] b372851798c1  IP-CIDR6,2400:5a60:8::/45
  - [Loyalsoldier China CIDR] b40c6898caf5  IP-CIDR6,2406:840:e0e9::/48
  - [Loyalsoldier China CIDR] b630bde54621  IP-CIDR,142.86.255.0/24
  - [Loyalsoldier China CIDR] b7ae3d3fbe2d  IP-CIDR,103.202.56.0/22
  - [Loyalsoldier China CIDR] bf212c3c10bd  IP-CIDR,103.73.0.0/21
  - [Loyalsoldier China CIDR] c371e2e5381e  IP-CIDR,202.55.28.0/23
  - [Loyalsoldier China CIDR] c6fea9d78e64  IP-CIDR6,2400:5a60::/47
  - [Loyalsoldier China CIDR] c711c25e5a2e  IP-CIDR6,2400:5a60:4::/46
  - [Loyalsoldier China CIDR] cf6be2a6fdbc  IP-CIDR,117.120.196.0/22
  - [Loyalsoldier China CIDR] d009c539b896  IP-CIDR6,2406:840:e400::/40
  - [Loyalsoldier China CIDR] d40bb63ad56d  IP-CIDR6,2400:9380:9080::/47
  - [Loyalsoldier China CIDR] d4ac83b50008  IP-CIDR,202.55.4.0/24
  - [Loyalsoldier China CIDR] d8fcab0d1f16  IP-CIDR,202.55.20.0/22
  - [Loyalsoldier China CIDR] d90ed697bbed  IP-CIDR,202.149.255.0/24
  - [Loyalsoldier China CIDR] dd660b52963a  IP-CIDR,202.149.252.0/23
  - [Loyalsoldier China CIDR] dd9b29723b5c  IP-CIDR,211.102.144.0/20
  - [Loyalsoldier China CIDR] e0299ffa085c  IP-CIDR,103.202.60.0/24
  - [Loyalsoldier China CIDR] e1841060a97c  IP-CIDR6,2406:840:c68::/45
  - [Loyalsoldier China CIDR] e648b097d794  IP-CIDR,103.202.62.0/23
  - [Loyalsoldier China CIDR] e7f6c7330d8d  IP-CIDR6,2406:840:e57c::/47
  - [Loyalsoldier China CIDR] e8a61a9a4a15  IP-CIDR,183.91.48.0/23
  - [Loyalsoldier China CIDR] e8e102d81b04  IP-CIDR,202.149.240.0/21
  - [Loyalsoldier China CIDR] ec4c3b1e55cf  IP-CIDR,202.149.224.0/20
  - [Loyalsoldier China CIDR] f5680045601a  IP-CIDR6,2406:840:e540::/43
  - [Loyalsoldier China CIDR] f8c1e13a0ee9  IP-CIDR6,2406:840:e0ec::/46
  - [Loyalsoldier China CIDR] fcb83456c612  IP-CIDR,202.55.0.0/23
```

## Download.list

**Removed: 5** (showing first 5)
```
  - [SukkaW Download] 1b7d5112fbe9  DOMAIN,mirror.library.ucy.ac.cy
  - [SukkaW Download] 3e52baba9610  DOMAIN,ftp.ktug.org
  - [SukkaW Download] 9e30a9124083  DOMAIN,mirror.thunderhosting.cloud
  - [SukkaW Download] bea9c7cf8579  DOMAIN,mirror.netcologne.de.org
  - [SukkaW Download] ec081797a402  DOMAIN,cpan.mines-albi.fr
```

## Speedtest.list

**Added: 146** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 010770237191  DOMAIN,stscarborough.rogers.com
  + [SukkaW Speedtest Servers International] 01d06b461e5c  DOMAIN,speedtest.readingsd.org
  + [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  + [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  + [SukkaW Speedtest Servers International] 0d9b9f55b7a6  DOMAIN,lifitelecom.brsserver.com.br
  + [SukkaW Speedtest Servers International] 0df919f8f00e  DOMAIN,speedtest.nrflvaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 0ef16a17f7b4  DOMAIN,stbowmanville.rogers.com
  + [SukkaW Speedtest Servers International] 0f56643c702c  DOMAIN,stosat-crls-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] 1179f68f6982  DOMAIN,va-speed.magna5.com
  + [SukkaW Speedtest Servers International] 1239ddbeead0  DOMAIN,speed13.gonetspeed.com
  + [SukkaW Speedtest Servers International] 129fa7cf52e5  DOMAIN,speedtest-newjersey.ripplefiber.com
  + [SukkaW Speedtest Servers International] 16744b51f48f  DOMAIN,speedtest-ash.vts.bf
  + [SukkaW Speedtest Servers International] 181f2fd1cbb5  DOMAIN,speedtest.iad.fdcservers.net
  + [SukkaW Speedtest Servers International] 19d98c644b57  DOMAIN,speedtest-iad.sectrify.com
  + [SukkaW Speedtest Servers International] 1b53005476d3  DOMAIN,speedtest.nrbn.ca
  + [SukkaW Speedtest Servers International] 1dd706232871  DOMAIN,speed10.aitspl.in
  + [SukkaW Speedtest Servers International] 1e3705ee2fe6  DOMAIN,speedtest.oceansls.com
  + [SukkaW Speedtest Servers International] 23d5bd5a13bc  DOMAIN,speedtest.gretna.myriverstreet.net
  + [SukkaW Speedtest Servers International] 2c84bbbee93c  DOMAIN,ooklaserver.asbn.va.ogital.net
  + [SukkaW Speedtest Servers International] 30df7f1427c6  DOMAIN,speedtest.ette.biz
  + [SukkaW Speedtest Servers International] 32c503790c60  DOMAIN,speedtest3.ptd.net
  + [SukkaW Speedtest Servers International] 32e092b9546f  DOMAIN,ookla-london3.tropicalhosting.net
  + [SukkaW Speedtest Servers International] 33041c0f7fd7  DOMAIN,stbowmanville.netcrawler.ca
  + [SukkaW Speedtest Servers International] 33e4b49c77f9  DOMAIN,ookla.la.ca.sharktech.net
  + [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  + [SukkaW Speedtest Servers International] 369df213d503  DOMAIN,nycmetro-speedtest.reliablesite.net
  + [SukkaW Speedtest Servers International] 3a3a932c44e1  DOMAIN,speed.airwavesinternet.com
  + [SukkaW Speedtest Servers International] 3a8aec9cda98  DOMAIN,speedtest-zl-1.zoominternet.net
  + [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  + [SukkaW Speedtest Servers International] 3e7bf0bd143d  DOMAIN,speedtest1.ewr.nj.us.planet.net
  + [SukkaW Speedtest Servers International] 400b94581e4f  DOMAIN,test.eolo.it
  + [SukkaW Speedtest Servers International] 414c35bf776f  DOMAIN,speedtest.us.novoserve.com
  + [SukkaW Speedtest Servers International] 42db00569c58  DOMAIN,speedtest.getwireless.net
  + [SukkaW Speedtest Servers International] 43c9e647d2a9  DOMAIN,speedtest-adelaide.optusnet.com.au
  + [SukkaW Speedtest Servers International] 44e1fd099c78  DOMAIN,speedtest.sc1.loopinternet.com
  + [SukkaW Speedtest Servers International] 4502550a3a9c  DOMAIN,wpa-speed.magna5.com
  + [SukkaW Speedtest Servers International] 4571f1abe520  DOMAIN,speedtestmacapa.webflash.net.br
  + [SukkaW Speedtest Servers International] 473f9b45897a  DOMAIN,speedtest.winchesterwireless.com
  + [SukkaW Speedtest Servers International] 49f2fe815df7  DOMAIN,speed.markham.telmax.ca
  + [SukkaW Speedtest Servers International] 49ffc4a2950e  DOMAIN,stoshawa.netcrawler.ca
  + [SukkaW Speedtest Servers International] 4cdddfe9358b  DOMAIN,sp1.jdmbroadband.com
  + [SukkaW Speedtest Servers International] 4d3968c87aec  DOMAIN,stintl.ospot.in
  + [SukkaW Speedtest Servers International] 4f8818240273  DOMAIN,stosat-plfi-08p.sys.comcast.net
  + [SukkaW Speedtest Servers International] 5193c8145d68  DOMAIN,crls-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 52a89dbdad82  DOMAIN,speedtest.us-ny2.kamatera.com
  + [SukkaW Speedtest Servers International] 52ea711702a9  DOMAIN,speedtestnorthpointe.arkdnacloud.com
  + [SukkaW Speedtest Servers International] 5559912850cd  DOMAIN,speedtest.belmontcountygig.com
  + [SukkaW Speedtest Servers International] 55c0cb8dcbb9  DOMAIN,speedtest2.pa.mycci.net
  + [SukkaW Speedtest Servers International] 57cfe7333ea8  DOMAIN,fast.blackbearfiber.com
  + [SukkaW Speedtest Servers International] 5893bd721aca  DOMAIN,stnorthyork.netcrawler.ca
  + [SukkaW Speedtest Servers International] 589d7eeccf53  DOMAIN,ookla.mtt.as6453.net
  + [SukkaW Speedtest Servers International] 5ab2e37aaffc  DOMAIN,speedtest31.suddenlink.net
  + [SukkaW Speedtest Servers International] 60ac93c18792  DOMAIN,stscarborough.netcrawler.ca
  + [SukkaW Speedtest Servers International] 615ab422b360  DOMAIN,btlr-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 6240dc262b53  DOMAIN,speedtest1.whsdk12.net
  + [SukkaW Speedtest Servers International] 625966c841d3  DOMAIN,speedtest1.ric1.va.hostedbackbone.net
  + [SukkaW Speedtest Servers International] 6722a4f62ff8  DOMAIN,stbowmanvillewireless.rogers.com
  + [SukkaW Speedtest Servers International] 67382fe7fa61  DOMAIN,stoshawa.rogers.com
  + [SukkaW Speedtest Servers International] 68c6eb173f83  DOMAIN,asbn-speedtest.northstate.net
  + [SukkaW Speedtest Servers International] 698bcfb1bb21  DOMAIN,speedtest-preston-wv.prodigiwv.net
  + [SukkaW Speedtest Servers International] 6aafcc1f0064  DOMAIN,speedtest.americatelecom.net.br
  + [SukkaW Speedtest Servers International] 6b8f1c9f7c44  DOMAIN,stajax.rogers.com
  + [SukkaW Speedtest Servers International] 6ef5f28df61c  DOMAIN,ookla.aeq.as6453.net
  + [SukkaW Speedtest Servers International] 74a6d6e46908  DOMAIN,speedtest.wb1.loopinternet.com
  + [SukkaW Speedtest Servers International] 75bd11ea02e4  DOMAIN,speed-fra.laudat.org
  + [SukkaW Speedtest Servers International] 7625db817368  DOMAIN,speedtest1.iad1-us.gozfly.net
  + [SukkaW Speedtest Servers International] 77cb389996a6  DOMAIN,speedtest-bethlehem.greenlightnetworks.com
  + [SukkaW Speedtest Servers International] 77e56dc99c59  DOMAIN,cltn-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 7c4e62477d2e  DOMAIN,speedtest.zoominternet.net
  + [SukkaW Speedtest Servers International] 7de305557319  DOMAIN,altoonaspeedtest.crowsnestbb.net
  + [SukkaW Speedtest Servers International] 8141004af16b  DOMAIN,speedtest02.srv.prnynj.alticeusa.net
  + [SukkaW Speedtest Servers International] 81b8486c1e76  DOMAIN,qoeookla-rmnd-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] 83e830bbc65c  DOMAIN,speedtest4.point-broadband.com
  + [SukkaW Speedtest Servers International] 8487be6e6d95  DOMAIN,speedtest.mifflincountywireless.com
  + [SukkaW Speedtest Servers International] 85b7f8f6df4c  DOMAIN,spd79.claro.com.br
  + [SukkaW Speedtest Servers International] 8632dbc95ac0  DOMAIN,stnorthyorkwireless.rogers.com
  + [SukkaW Speedtest Servers International] 894527aa356c  DOMAIN,lsdspeed01.lsdops.net
  + [SukkaW Speedtest Servers International] 8fb9855a4808  DOMAIN,reikonteste.reikoninternet.com.br
  + [SukkaW Speedtest Servers International] 8fd05fb4ff7e  DOMAIN,speedtest19.suddenlink.net
  + [SukkaW Speedtest Servers International] 90617691e3af  DOMAIN,stwhitby.netcrawler.ca
  + [SukkaW Speedtest Servers International] 910cf0769104  DOMAIN,speedtest-nwrk-nj.wtsky.net
  + [SukkaW Speedtest Servers International] 9138c74c88d2  DOMAIN,vaspeedtest.rackdog.com
  + [SukkaW Speedtest Servers International] 91dd7903cffa  DOMAIN,speedtest.conectaamazonia.com.br
  + [SukkaW Speedtest Servers International] 9660747a5a08  DOMAIN,speed01.gonetspeed.com
  + [SukkaW Speedtest Servers International] 96e24c3aaac2  DOMAIN,stoshawawireless.rogers.com
  + [SukkaW Speedtest Servers International] 995889b17f13  DOMAIN,lsdspeed02.lsdops.net
  + [SukkaW Speedtest Servers International] 9b36e6ace41e  DOMAIN,phlph0001speedtestserver02.wiline.com
  + [SukkaW Speedtest Servers International] 9c36ab36b132  DOMAIN,phl01.screenshot.download
  + [SukkaW Speedtest Servers International] 9ee8a1734e62  DOMAIN,speedtest2.sistelfibra.es
  + [SukkaW Speedtest Servers International] 9f094a91d810  DOMAIN,ookla.micrologicwv.com
  + [SukkaW Speedtest Servers International] 9f6b30de3d0b  DOMAIN,speedtest-server-ash.starry.com
  + [SukkaW Speedtest Servers International] a933b6c67760  DOMAIN,speedtest.wsp.net.br
  + [SukkaW Speedtest Servers International] aeef367331bf  DOMAIN,speedtest.speednetmacapa.com.br
  + [SukkaW Speedtest Servers International] b01a9f97e3be  DOMAIN,sttorontowireless.rogers.com
  + [SukkaW Speedtest Servers International] b06e6a3b7c0f  DOMAIN,speedtest.philasd.org
  + [SukkaW Speedtest Servers International] b0cc745d6216  DOMAIN,stosat-balt-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] b28cbd1348be  DOMAIN,velocimetro.wspeednet.com.br
  + [SukkaW Speedtest Servers International] b39848e99989  DOMAIN,speedtest01.mel1.spintel.net.au
  + [SukkaW Speedtest Servers International] b4f4faf0a782  DOMAIN,speedtest.fiberlync.net
  + [SukkaW Speedtest Servers International] b577445ffd28  DOMAIN,ookla-mgw.wvnet.edu
  ... and 46 more
```

**Removed: 172** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 012b7f31586b  DOMAIN,ststratford.rogers.com
  - [SukkaW Speedtest Servers International] 02b7b422882f  DOMAIN,speedtest.sentco.net
  - [SukkaW Speedtest Servers International] 04df25e28545  DOMAIN,speedtest.premieronline.net
  - [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  - [SukkaW Speedtest Servers International] 0a21ac426b0c  DOMAIN,speedtest.octaplus.uk
  - [SukkaW Speedtest Servers International] 0ab0cf8a6ab9  DOMAIN,speedtest.novateldigital.com
  - [SukkaW Speedtest Servers International] 0bd6b487bcf7  DOMAIN,speedtest.inovewifi.com.br
  - [SukkaW Speedtest Servers International] 0cc435ecaed2  DOMAIN,teste.freedomnetwork.net.br
  - [SukkaW Speedtest Servers International] 0f9fc6befe00  DOMAIN,speed.idnet.net.br
  - [SukkaW Speedtest Servers International] 1204ab7c7137  DOMAIN,40gspeedtest.mnsi.net
  - [SukkaW Speedtest Servers International] 12ca2bed9dbb  DOMAIN,speedtest.atccomm.net
  - [SukkaW Speedtest Servers International] 1303e426ad0f  DOMAIN,speed-pd.dispaisy.systems
  - [SukkaW Speedtest Servers International] 13dc2485ab95  DOMAIN,speedtest.heartofiowa.coop
  - [SukkaW Speedtest Servers International] 14696c5e4444  DOMAIN,speedtest.cmltelephone.com
  - [SukkaW Speedtest Servers International] 14c7e265c3d8  DOMAIN,speedtest.ibertic.es
  - [SukkaW Speedtest Servers International] 189c17014e83  DOMAIN,speedtest.amesiaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 1cfb48abbf36  DOMAIN,speedtest.grm.net
  - [SukkaW Speedtest Servers International] 1debbecee8c5  DOMAIN,speedtest.cstech.com
  - [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  - [SukkaW Speedtest Servers International] 1e9ede2ea46b  DOMAIN,speedtest.westianet.com
  - [SukkaW Speedtest Servers International] 22d288599e8f  DOMAIN,speedtest01.bne1.spintel.net.au
  - [SukkaW Speedtest Servers International] 2785a4313085  DOMAIN,teste.suprainternet.com.br
  - [SukkaW Speedtest Servers International] 281c33e17703  DOMAIN,speedtest.ecmnet.com.br
  - [SukkaW Speedtest Servers International] 29a310f8327b  DOMAIN,speedtest.brooketel.coop
  - [SukkaW Speedtest Servers International] 2ab9b0da9911  DOMAIN,lcrs-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 2c1a5f959732  DOMAIN,speedtest-pd.wifiweb.it
  - [SukkaW Speedtest Servers International] 304d2683e43f  DOMAIN,speedtest.skywaveconnect.com
  - [SukkaW Speedtest Servers International] 32b355be6336  DOMAIN,speedtest.bluevalley.net
  - [SukkaW Speedtest Servers International] 3307fbfaba51  DOMAIN,st3.surajnetwork.com
  - [SukkaW Speedtest Servers International] 34d320d8b02f  DOMAIN,speedtest.mdtc.net
  - [SukkaW Speedtest Servers International] 358795b67fd5  DOMAIN,speedtest.mornington.ca
  - [SukkaW Speedtest Servers International] 37dae1757a6d  DOMAIN,stsaultstemariewireless.rogers.com
  - [SukkaW Speedtest Servers International] 394dff5a7003  DOMAIN,stwindsorwireless.rogers.com
  - [SukkaW Speedtest Servers International] 3a92209ad6ba  DOMAIN,speedtest-01.omnitel.biz
  - [SukkaW Speedtest Servers International] 3a97abf4595c  DOMAIN,speedtest1.oma.nxlink.com
  - [SukkaW Speedtest Servers International] 3b0dc040ff61  DOMAIN,speed.nutelecom.com
  - [SukkaW Speedtest Servers International] 3ea882635f75  DOMAIN,speed.sdmnet.com.br
  - [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 3f2a1255658c  DOMAIN,blfd-speed-01.gpcom.com
  - [SukkaW Speedtest Servers International] 3f7075e220a1  DOMAIN,ksczks-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 3f8306542a0b  DOMAIN,stsudburywireless.rogers.com
  - [SukkaW Speedtest Servers International] 41bc4d2333e5  DOMAIN,speedtest.cvalley.net
  - [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  - [SukkaW Speedtest Servers International] 45ed5f3bd479  DOMAIN,speedtest.tcaexpress.net
  - [SukkaW Speedtest Servers International] 48e2d32a2895  DOMAIN,speedtest.cascadecomm.com
  - [SukkaW Speedtest Servers International] 4bbf2a0a0fa3  DOMAIN,speedtest.mysmbs.com
  - [SukkaW Speedtest Servers International] 4bc2ef4606ca  DOMAIN,st-oma-1.binary.net
  - [SukkaW Speedtest Servers International] 4c8fd6b2f3f6  DOMAIN,ookla-ks.mercuryfiber.com
  - [SukkaW Speedtest Servers International] 4d517e99e743  DOMAIN,mns.i-systems.com
  - [SukkaW Speedtest Servers International] 4db3cbb342cd  DOMAIN,speedtest-lenexa.resoundnetworks.com
  - [SukkaW Speedtest Servers International] 4de50e12bd16  DOMAIN,speedtest.hay.net
  - [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  - [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  - [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  - [SukkaW Speedtest Servers International] 52138baf5666  DOMAIN,speedtest-mum.froze.in
  - [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  - [SukkaW Speedtest Servers International] 565ea387b1e5  DOMAIN,speedtest.cfu.net
  - [SukkaW Speedtest Servers International] 56e9dda42623  DOMAIN,speedteste.netfast.com.br
  - [SukkaW Speedtest Servers International] 58e6d169adef  DOMAIN,speedtest.esu5.org
  - [SukkaW Speedtest Servers International] 59f0ec25e179  DOMAIN,blar-speed-01.gpcom.com
  - [SukkaW Speedtest Servers International] 5b6c9723716c  DOMAIN,speedtest.syd.netsg.net.au
  - [SukkaW Speedtest Servers International] 5c69bf15997f  DOMAIN,sp1.speedy.bb-swrag.de
  - [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  - [SukkaW Speedtest Servers International] 5dc175d6c501  DOMAIN,teste.tstelecomltda.com.br
  - [SukkaW Speedtest Servers International] 5f3fcd920887  DOMAIN,speedtest.ncn.net
  - [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  - [SukkaW Speedtest Servers International] 605cfb35f522  DOMAIN,speedtest.mci.as1003.net
  - [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  - [SukkaW Speedtest Servers International] 6b8a034fa920  DOMAIN,speedtest.wifi4all.it
  - [SukkaW Speedtest Servers International] 6bd15d569f45  DOMAIN,velocidade.csrnetwork.com.br
  - [SukkaW Speedtest Servers International] 6db06cea3422  DOMAIN,speedtest.internetarribes.es
  - [SukkaW Speedtest Servers International] 6ff5941eb406  DOMAIN,exc-speedtest.unitedfiber.com
  - [SukkaW Speedtest Servers International] 72bb8c1b570f  DOMAIN,speedtest5.windtre.it
  - [SukkaW Speedtest Servers International] 73112e9dc2cb  DOMAIN,speedtest01.adl1.spintel.net.au
  - [SukkaW Speedtest Servers International] 761a11540f93  DOMAIN,siouxcity1.cabospeed.com
  - [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  - [SukkaW Speedtest Servers International] 76c205f9d894  DOMAIN,speedtest.linknetbv.com
  - [SukkaW Speedtest Servers International] 7935cf977efe  DOMAIN,speedtest.wwfn.ca
  - [SukkaW Speedtest Servers International] 7a4042ca0d6f  DOMAIN,stbarriewireless.rogers.com
  - [SukkaW Speedtest Servers International] 7a55e968bb85  DOMAIN,speedtest.unitedfiber.com
  - [SukkaW Speedtest Servers International] 7ad78e8435d7  DOMAIN,speed.ddbroadband.co.in
  - [SukkaW Speedtest Servers International] 7b2b5f1619fb  DOMAIN,karnal.sitibroadband.co.in
  - [SukkaW Speedtest Servers International] 7bdc14806a7c  DOMAIN,speedtest.wccta.com
  - [SukkaW Speedtest Servers International] 7ccc323c4514  DOMAIN,iperf-ams-nl.eranium.net
  - [SukkaW Speedtest Servers International] 7ea92d713139  DOMAIN,speedtest.rochmnaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 809ed12ed910  DOMAIN,speedtest.nemr.net
  - [SukkaW Speedtest Servers International] 84b8446a854b  DOMAIN,speedtest10g.ics-llc.net
  - [SukkaW Speedtest Servers International] 86b839ab050c  DOMAIN,velocidade.4wnet.com.br
  - [SukkaW Speedtest Servers International] 86f4178b9153  DOMAIN,speedtest.fibercomm.net
  - [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  - [SukkaW Speedtest Servers International] 8c67eca44a61  DOMAIN,velocidade.tecsattelecom.com.br
  - [SukkaW Speedtest Servers International] 8c9d7c03fa30  DOMAIN,speedtest27.suddenlink.net
  - [SukkaW Speedtest Servers International] 8cfc393702b7  DOMAIN,speedtest.kc2.everfastfiber.com
  - [SukkaW Speedtest Servers International] 905125f73ee5  DOMAIN,speedtest.mvec.com
  - [SukkaW Speedtest Servers International] 9052a64cc3fd  DOMAIN,speedtest25.wiatel.com
  - [SukkaW Speedtest Servers International] 9073adefc65d  DOMAIN,speedtest.neitel.net
  - [SukkaW Speedtest Servers International] 934ad5aa9642  DOMAIN,speedtest10g.bhm.as13760.net
  - [SukkaW Speedtest Servers International] 93617c692bd8  DOMAIN,ookla.mci-1.serverforge.org
  - [SukkaW Speedtest Servers International] 9868c3f8fedf  DOMAIN,speedtest.s3rdv.com
  - [SukkaW Speedtest Servers International] 991108b39981  DOMAIN,speedtest.mtctech.net
  ... and 72 more
```
