# Surge Rule Diff Report
Generated: 2026-11-04T05:02:35.614560

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 2 |
| Rules added | 209 |
| Rules removed | 578 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China_IP.list | 10012 | 9662 | +70 | -420 | ~0 |
| Speedtest.list | 1722 | 1703 | +139 | -158 | ~0 |

## China_IP.list

**Added: 70** (showing first 70)
```
  + [Loyalsoldier China CIDR] 00229ba7ff7f  IP-CIDR6,2408:4000::/40
  + [Loyalsoldier China CIDR] 00cf9fe18cf2  IP-CIDR,203.107.32.0/19
  + [Loyalsoldier China CIDR] 02d6c52c3b18  IP-CIDR,140.210.64.0/18
  + [Loyalsoldier China CIDR] 065bb3fcfbe4  IP-CIDR6,2408:4000:100::/47
  + [Loyalsoldier China CIDR] 1172714f4bad  IP-CIDR,110.42.0.0/20
  + [Loyalsoldier China CIDR] 16a7674231f5  IP-CIDR6,2408:4000:200::/39
  + [Loyalsoldier China CIDR] 2150fa96c12d  IP-CIDR6,2408:4000:1000::/36
  + [Loyalsoldier China CIDR] 292934061a62  IP-CIDR,110.42.24.0/21
  + [Loyalsoldier China CIDR] 299a17200e6c  IP-CIDR,103.19.235.0/24
  + [Loyalsoldier China CIDR] 2d26648bb2d6  IP-CIDR6,2408:4000:4000::/34
  + [Loyalsoldier China CIDR] 305988ed5f55  IP-CIDR,103.74.124.0/24
  + [Loyalsoldier China CIDR] 343222885d82  IP-CIDR,27.98.202.0/23
  + [Loyalsoldier China CIDR] 36d4d23ba088  IP-CIDR6,2408:4000:400::/38
  + [Loyalsoldier China CIDR] 382911332e23  IP-CIDR,140.210.32.0/19
  + [Loyalsoldier China CIDR] 38ad7586d095  IP-CIDR,203.107.4.0/22
  + [Loyalsoldier China CIDR] 3984f480afa4  IP-CIDR6,2408:4004::/30
  + [Loyalsoldier China CIDR] 3a8289a53d4c  IP-CIDR,203.107.72.0/21
  + [Loyalsoldier China CIDR] 3e901f7cf3b8  IP-CIDR,163.223.72.0/23
  + [Loyalsoldier China CIDR] 40b8880f8cf0  IP-CIDR,203.107.8.0/21
  + [Loyalsoldier China CIDR] 41859d985081  IP-CIDR,45.113.204.0/22
  + [Loyalsoldier China CIDR] 45070fa9add2  IP-CIDR,203.107.70.0/23
  + [Loyalsoldier China CIDR] 45ba304bac69  IP-CIDR,203.107.69.0/24
  + [Loyalsoldier China CIDR] 46004a8bdb58  IP-CIDR6,2406:840:eb0a::/48
  + [Loyalsoldier China CIDR] 4cb726ab9456  IP-CIDR,203.107.96.0/19
  + [Loyalsoldier China CIDR] 5673ce7c2ef4  IP-CIDR6,2408:4000:103::/48
  + [Loyalsoldier China CIDR] 56b34d0e62be  IP-CIDR,202.144.196.0/23
  + [Loyalsoldier China CIDR] 59baacfabb93  IP-CIDR6,2408:4008::/29
  + [Loyalsoldier China CIDR] 621c14fe9107  IP-CIDR,103.53.126.0/24
  + [Loyalsoldier China CIDR] 629c0c855a51  IP-CIDR6,2408:4000:108::/45
  + [Loyalsoldier China CIDR] 652864d06415  IP-CIDR,103.53.124.0/23
  + [Loyalsoldier China CIDR] 654a3bfda6d2  IP-CIDR,110.40.0.0/15
  + [Loyalsoldier China CIDR] 65f8a2370264  IP-CIDR,140.210.0.0/20
  + [Loyalsoldier China CIDR] 6927fc09f6ff  IP-CIDR,140.210.16.0/23
  + [Loyalsoldier China CIDR] 6db35373e75e  IP-CIDR,203.107.80.0/20
  + [Loyalsoldier China CIDR] 6f57909299b6  IP-CIDR6,2408:4000:2000::/35
  + [Loyalsoldier China CIDR] 6fba91932dc7  IP-CIDR6,2a0a:d685:502::/47
  + [Loyalsoldier China CIDR] 71b0dc38a665  IP-CIDR6,2408:4000:104::/46
  + [Loyalsoldier China CIDR] 72b3fa5dc160  IP-CIDR,45.113.202.0/24
  + [Loyalsoldier China CIDR] 7c73a002ae8d  IP-CIDR6,2408:4001::/32
  + [Loyalsoldier China CIDR] 8379639719e9  IP-CIDR,110.42.32.0/19
  + [Loyalsoldier China CIDR] 851860037e47  IP-CIDR6,2402:8160::/32
  + [Loyalsoldier China CIDR] 8b48be24a34c  IP-CIDR6,2a0a:d685:500::/48
  + [Loyalsoldier China CIDR] 8d77ad5f55a0  IP-CIDR,110.42.16.0/24
  + [Loyalsoldier China CIDR] 91005c049978  IP-CIDR,202.144.198.0/24
  + [Loyalsoldier China CIDR] 9471d9e0d43f  IP-CIDR,110.42.64.0/18
  + [Loyalsoldier China CIDR] 9917b2b55b99  IP-CIDR,110.42.20.0/22
  + [Loyalsoldier China CIDR] 99c9da5cbe5c  IP-CIDR,203.107.16.0/20
  + [Loyalsoldier China CIDR] 9ee332727c94  IP-CIDR6,2408:4000:8000::/33
  + [Loyalsoldier China CIDR] a11ce8c35f05  IP-CIDR,203.107.0.0/23
  + [Loyalsoldier China CIDR] a1b486bcc4eb  IP-CIDR,110.42.18.0/23
  + [Loyalsoldier China CIDR] a9c12b62e09d  IP-CIDR,223.122.29.0/24
  + [Loyalsoldier China CIDR] aaa18628d130  IP-CIDR,140.210.20.0/22
  + [Loyalsoldier China CIDR] adfb3b95ab3a  IP-CIDR,203.107.2.0/24
  + [Loyalsoldier China CIDR] af7c760e21ef  IP-CIDR6,2406:840:c00::/48
  + [Loyalsoldier China CIDR] b3dbe41a0569  IP-CIDR,103.81.184.0/23
  + [Loyalsoldier China CIDR] c00659a70998  IP-CIDR,140.210.18.0/24
  + [Loyalsoldier China CIDR] c2f3b47241fd  IP-CIDR6,2408:4000:110::/44
  + [Loyalsoldier China CIDR] c4f7d9d5bd2f  IP-CIDR6,2408:4000:800::/37
  + [Loyalsoldier China CIDR] c7cf7680afaa  IP-CIDR,110.43.0.0/16
  + [Loyalsoldier China CIDR] c8f531302a9e  IP-CIDR6,2a0a:d685:504::/48
  + [Loyalsoldier China CIDR] d398bdd7da3f  IP-CIDR,140.210.24.0/21
  + [Loyalsoldier China CIDR] d5b20dbed552  IP-CIDR,110.42.128.0/17
  + [Loyalsoldier China CIDR] d74a2af14df3  IP-CIDR6,2408:4000:120::/43
  + [Loyalsoldier China CIDR] da638880a116  IP-CIDR6,2408:4002::/31
  + [Loyalsoldier China CIDR] df83091e0362  IP-CIDR6,2408:4000:180::/41
  + [Loyalsoldier China CIDR] e1cbfb3273f2  IP-CIDR6,2408:4000:140::/42
  + [Loyalsoldier China CIDR] e1db4c44bae9  IP-CIDR,45.113.200.0/23
  + [Loyalsoldier China CIDR] e55a04398d21  IP-CIDR,206.109.71.0/24
  + [Loyalsoldier China CIDR] f4324bee3a63  IP-CIDR,140.210.128.0/17
  + [Loyalsoldier China CIDR] f6b4e28dca98  IP-CIDR6,2a0a:d685:506::/47
```

**Removed: 420** (showing first 100)
```
  - [Loyalsoldier China CIDR] 02035bd5d851  IP-CIDR,43.96.80.0/23
  - [Loyalsoldier China CIDR] 021d872078f8  IP-CIDR,170.33.136.0/23
  - [Loyalsoldier China CIDR] 023a65fa0295  IP-CIDR,198.11.128.0/20
  - [Loyalsoldier China CIDR] 0371d7c0ed16  IP-CIDR,47.89.84.0/24
  - [Loyalsoldier China CIDR] 03a4e9468281  IP-CIDR,8.212.0.0/18
  - [Loyalsoldier China CIDR] 03bff4aedd02  IP-CIDR,8.220.176.0/20
  - [Loyalsoldier China CIDR] 042c6d58af98  IP-CIDR,47.246.84.0/22
  - [Loyalsoldier China CIDR] 04db2ac3c2ee  IP-CIDR,8.220.96.0/20
  - [Loyalsoldier China CIDR] 05347ca60f60  IP-CIDR,47.77.96.0/20
  - [Loyalsoldier China CIDR] 0540391c04a3  IP-CIDR,47.235.8.0/22
  - [Loyalsoldier China CIDR] 05b2fd575278  IP-CIDR,47.80.0.0/14
  - [Loyalsoldier China CIDR] 05f11067c460  IP-CIDR,47.246.122.0/23
  - [Loyalsoldier China CIDR] 06116f5d3d9c  IP-CIDR,43.108.0.0/16
  - [Loyalsoldier China CIDR] 0714d9a34244  IP-CIDR,139.95.16.0/22
  - [Loyalsoldier China CIDR] 081d35289161  IP-CIDR,8.218.0.0/15
  - [Loyalsoldier China CIDR] 08ccecb030d3  IP-CIDR,8.221.144.0/21
  - [Loyalsoldier China CIDR] 0959c92f89e0  IP-CIDR6,240b:4002:8000::/33
  - [Loyalsoldier China CIDR] 097eca69d164  IP-CIDR,170.33.130.0/23
  - [Loyalsoldier China CIDR] 0a0c736fbe8f  IP-CIDR,156.236.17.0/24
  - [Loyalsoldier China CIDR] 0ae045dedca5  IP-CIDR,47.89.90.0/24
  - [Loyalsoldier China CIDR] 0ae706b44a64  IP-CIDR6,240b:400c::/30
  - [Loyalsoldier China CIDR] 0b5b67ccaef2  IP-CIDR,47.237.128.0/18
  - [Loyalsoldier China CIDR] 0b795a78bd32  IP-CIDR,43.96.103.0/24
  - [Loyalsoldier China CIDR] 0cafff9471fc  IP-CIDR,47.87.32.0/19
  - [Loyalsoldier China CIDR] 0d1f2138e52c  IP-CIDR,116.251.64.0/18
  - [Loyalsoldier China CIDR] 0e107318debe  IP-CIDR,8.208.144.0/20
  - [Loyalsoldier China CIDR] 0e52bb251e1f  IP-CIDR,47.57.128.0/18
  - [Loyalsoldier China CIDR] 0eb698cba11f  IP-CIDR,43.96.126.0/24
  - [Loyalsoldier China CIDR] 0eff9ebbabc2  IP-CIDR,14.1.112.0/22
  - [Loyalsoldier China CIDR] 0f02ef47e587  IP-CIDR,47.89.96.0/20
  - [Loyalsoldier China CIDR] 11038c6ff91e  IP-CIDR,149.129.16.0/21
  - [Loyalsoldier China CIDR] 11c1fbc1543c  IP-CIDR,8.212.104.0/21
  - [Loyalsoldier China CIDR] 1299029ba5c9  IP-CIDR,47.251.136.0/21
  - [Loyalsoldier China CIDR] 13620af244de  IP-CIDR,47.246.72.0/21
  - [Loyalsoldier China CIDR] 13ecd2212095  IP-CIDR,43.112.0.0/15
  - [Loyalsoldier China CIDR] 14d43665240e  IP-CIDR,8.220.232.0/22
  - [Loyalsoldier China CIDR] 15214cea6e12  IP-CIDR,43.96.92.0/22
  - [Loyalsoldier China CIDR] 15680e99e598  IP-CIDR,8.211.232.0/21
  - [Loyalsoldier China CIDR] 15b5de0749be  IP-CIDR6,240b:4002:1100::/40
  - [Loyalsoldier China CIDR] 15f3a542a769  IP-CIDR,47.237.0.0/17
  - [Loyalsoldier China CIDR] 1686913eea3a  IP-CIDR,47.246.91.0/24
  - [Loyalsoldier China CIDR] 18f56acd4438  IP-CIDR,139.95.64.0/23
  - [Loyalsoldier China CIDR] 1a06a98216e2  IP-CIDR,139.95.96.0/22
  - [Loyalsoldier China CIDR] 1ab7f7ffc509  IP-CIDR,170.33.192.0/23
  - [Loyalsoldier China CIDR] 1afef130d660  IP-CIDR,139.95.128.0/17
  - [Loyalsoldier China CIDR] 1b0d8baddb74  IP-CIDR,43.96.77.131/32
  - [Loyalsoldier China CIDR] 1b65088bead1  IP-CIDR,8.222.0.0/15
  - [Loyalsoldier China CIDR] 1b684a9faa15  IP-CIDR6,2404:2280:1000::/36
  - [Loyalsoldier China CIDR] 1ca7f1ab8abf  IP-CIDR,8.209.36.0/22
  - [Loyalsoldier China CIDR] 1cc63e17d4fc  IP-CIDR,139.95.40.0/23
  - [Loyalsoldier China CIDR] 1d0b252ef665  IP-CIDR,43.97.0.0/17
  - [Loyalsoldier China CIDR] 1d0e0fa94db9  IP-CIDR6,240b:400b::/32
  - [Loyalsoldier China CIDR] 1d9590f9a971  IP-CIDR,43.90.0.0/16
  - [Loyalsoldier China CIDR] 1dac5c029933  IP-CIDR,43.96.8.0/22
  - [Loyalsoldier China CIDR] 1e6bc3967f86  IP-CIDR,170.33.64.0/23
  - [Loyalsoldier China CIDR] 1fb9320d9874  IP-CIDR,43.116.160.0/24
  - [Loyalsoldier China CIDR] 2177e521e5dc  IP-CIDR,47.57.200.0/21
  - [Loyalsoldier China CIDR] 21d28b383b2b  IP-CIDR,8.208.0.0/17
  - [Loyalsoldier China CIDR] 2231de14ac16  IP-CIDR,8.211.0.0/17
  - [Loyalsoldier China CIDR] 223cf2800b20  IP-CIDR,103.19.234.0/23
  - [Loyalsoldier China CIDR] 2366dc149a49  IP-CIDR,5.181.224.0/23
  - [Loyalsoldier China CIDR] 2476352a3b01  IP-CIDR,47.246.131.0/24
  - [Loyalsoldier China CIDR] 2489f9568f8a  IP-CIDR,47.236.0.0/17
  - [Loyalsoldier China CIDR] 24956b770edc  IP-CIDR,47.87.144.0/21
  - [Loyalsoldier China CIDR] 24a4a07c7b77  IP-CIDR,8.214.164.0/22
  - [Loyalsoldier China CIDR] 256a2b090cc3  IP-CIDR,47.77.24.0/22
  - [Loyalsoldier China CIDR] 260ba2bc2f34  IP-CIDR6,2404:2280:2000::/35
  - [Loyalsoldier China CIDR] 2635e32da172  IP-CIDR,8.208.160.0/19
  - [Loyalsoldier China CIDR] 27025cd904a1  IP-CIDR,43.124.0.0/16
  - [Loyalsoldier China CIDR] 272859d67e8e  IP-CIDR,43.96.122.0/24
  - [Loyalsoldier China CIDR] 28f443d1e57b  IP-CIDR,43.92.0.0/15
  - [Loyalsoldier China CIDR] 29043c807dc1  IP-CIDR,47.246.135.0/24
  - [Loyalsoldier China CIDR] 2938af393a14  IP-CIDR,8.212.80.0/21
  - [Loyalsoldier China CIDR] 299edd6b0ad2  IP-CIDR,43.96.64.0/21
  - [Loyalsoldier China CIDR] 29fd14d72818  IP-CIDR,43.96.2.130/32
  - [Loyalsoldier China CIDR] 2a24a8de60e6  IP-CIDR,8.221.0.0/17
  - [Loyalsoldier China CIDR] 2a26903fbbb6  IP-CIDR,47.238.32.0/19
  - [Loyalsoldier China CIDR] 2b19a4c5a359  IP-CIDR,47.251.224.0/19
  - [Loyalsoldier China CIDR] 2c328b3f4eee  IP-CIDR,47.246.32.0/22
  - [Loyalsoldier China CIDR] 2c83751a78ff  IP-CIDR,43.123.0.0/17
  - [Loyalsoldier China CIDR] 2e5700b57a2e  IP-CIDR,43.96.4.0/22
  - [Loyalsoldier China CIDR] 2eb6c0a1fddf  IP-CIDR6,240b:4002:1080::/41
  - [Loyalsoldier China CIDR] 30a216ae0450  IP-CIDR,47.251.132.0/22
  - [Loyalsoldier China CIDR] 31323f9a79a5  IP-CIDR,156.245.1.0/24
  - [Loyalsoldier China CIDR] 314fdd0641ec  IP-CIDR6,2404:2280:4000::/36
  - [Loyalsoldier China CIDR] 317aef7bde52  IP-CIDR,149.129.0.0/20
  - [Loyalsoldier China CIDR] 318d0fbe3a0e  IP-CIDR,43.96.116.0/24
  - [Loyalsoldier China CIDR] 31ba7a119d50  IP-CIDR,47.56.0.0/16
  - [Loyalsoldier China CIDR] 322c1ac0c9bd  IP-CIDR,47.246.136.0/21
  - [Loyalsoldier China CIDR] 326dc654a6f1  IP-CIDR,8.208.140.0/22
  - [Loyalsoldier China CIDR] 32b92483689c  IP-CIDR,8.212.192.0/18
  - [Loyalsoldier China CIDR] 33239b5b7080  IP-CIDR,47.236.192.0/20
  - [Loyalsoldier China CIDR] 36734f7d2746  IP-CIDR,47.57.192.0/22
  - [Loyalsoldier China CIDR] 382f692c1385  IP-CIDR,43.96.16.130/32
  - [Loyalsoldier China CIDR] 3876a32b10cb  IP-CIDR,47.90.128.0/19
  - [Loyalsoldier China CIDR] 39cf394b2a98  IP-CIDR,8.220.160.0/21
  - [Loyalsoldier China CIDR] 3b38081bef28  IP-CIDR,147.139.240.0/21
  - [Loyalsoldier China CIDR] 3b7ff0339420  IP-CIDR,47.237.192.0/19
  - [Loyalsoldier China CIDR] 3bf412e9f733  IP-CIDR,47.238.16.0/21
  - [Loyalsoldier China CIDR] 3bfba9fe5db8  IP-CIDR,47.246.92.0/23
  ... and 320 more
```

## Speedtest.list

**Added: 139** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 010770237191  DOMAIN,stscarborough.rogers.com
  + [SukkaW Speedtest Servers International] 01d06b461e5c  DOMAIN,speedtest.readingsd.org
  + [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  + [SukkaW Speedtest Servers International] 0cc435ecaed2  DOMAIN,teste.freedomnetwork.net.br
  + [SukkaW Speedtest Servers International] 0df919f8f00e  DOMAIN,speedtest.nrflvaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 0ef16a17f7b4  DOMAIN,stbowmanville.rogers.com
  + [SukkaW Speedtest Servers International] 0f56643c702c  DOMAIN,stosat-crls-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] 1179f68f6982  DOMAIN,va-speed.magna5.com
  + [SukkaW Speedtest Servers International] 129fa7cf52e5  DOMAIN,speedtest-newjersey.ripplefiber.com
  + [SukkaW Speedtest Servers International] 16744b51f48f  DOMAIN,speedtest-ash.vts.bf
  + [SukkaW Speedtest Servers International] 181f2fd1cbb5  DOMAIN,speedtest.iad.fdcservers.net
  + [SukkaW Speedtest Servers International] 19d98c644b57  DOMAIN,speedtest-iad.sectrify.com
  + [SukkaW Speedtest Servers International] 1b11c45002fb  DOMAIN,speedtest-rz.vsm.sh
  + [SukkaW Speedtest Servers International] 1b53005476d3  DOMAIN,speedtest.nrbn.ca
  + [SukkaW Speedtest Servers International] 1dd706232871  DOMAIN,speed10.aitspl.in
  + [SukkaW Speedtest Servers International] 1e3705ee2fe6  DOMAIN,speedtest.oceansls.com
  + [SukkaW Speedtest Servers International] 23d5bd5a13bc  DOMAIN,speedtest.gretna.myriverstreet.net
  + [SukkaW Speedtest Servers International] 30df7f1427c6  DOMAIN,speedtest.ette.biz
  + [SukkaW Speedtest Servers International] 32c503790c60  DOMAIN,speedtest3.ptd.net
  + [SukkaW Speedtest Servers International] 33041c0f7fd7  DOMAIN,stbowmanville.netcrawler.ca
  + [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  + [SukkaW Speedtest Servers International] 36366555a5b5  DOMAIN,ookla.mu.as6453.net
  + [SukkaW Speedtest Servers International] 369df213d503  DOMAIN,nycmetro-speedtest.reliablesite.net
  + [SukkaW Speedtest Servers International] 3a8aec9cda98  DOMAIN,speedtest-zl-1.zoominternet.net
  + [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  + [SukkaW Speedtest Servers International] 3e7bf0bd143d  DOMAIN,speedtest1.ewr.nj.us.planet.net
  + [SukkaW Speedtest Servers International] 3f834173887b  DOMAIN,speedtest.hnd.fdcservers.net
  + [SukkaW Speedtest Servers International] 414c35bf776f  DOMAIN,speedtest.us.novoserve.com
  + [SukkaW Speedtest Servers International] 42db00569c58  DOMAIN,speedtest.getwireless.net
  + [SukkaW Speedtest Servers International] 43f75ae5aa25  DOMAIN,speedtest.telbo.net
  + [SukkaW Speedtest Servers International] 44e1fd099c78  DOMAIN,speedtest.sc1.loopinternet.com
  + [SukkaW Speedtest Servers International] 4502550a3a9c  DOMAIN,wpa-speed.magna5.com
  + [SukkaW Speedtest Servers International] 4571f1abe520  DOMAIN,speedtestmacapa.webflash.net.br
  + [SukkaW Speedtest Servers International] 473f9b45897a  DOMAIN,speedtest.winchesterwireless.com
  + [SukkaW Speedtest Servers International] 49f2fe815df7  DOMAIN,speed.markham.telmax.ca
  + [SukkaW Speedtest Servers International] 49ffc4a2950e  DOMAIN,stoshawa.netcrawler.ca
  + [SukkaW Speedtest Servers International] 4f8818240273  DOMAIN,stosat-plfi-08p.sys.comcast.net
  + [SukkaW Speedtest Servers International] 5186f86137c0  DOMAIN,cns-speedtest.duckdns.org
  + [SukkaW Speedtest Servers International] 5193c8145d68  DOMAIN,crls-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 52a89dbdad82  DOMAIN,speedtest.us-ny2.kamatera.com
  + [SukkaW Speedtest Servers International] 52ea711702a9  DOMAIN,speedtestnorthpointe.arkdnacloud.com
  + [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  + [SukkaW Speedtest Servers International] 5559912850cd  DOMAIN,speedtest.belmontcountygig.com
  + [SukkaW Speedtest Servers International] 55c0cb8dcbb9  DOMAIN,speedtest2.pa.mycci.net
  + [SukkaW Speedtest Servers International] 57cfe7333ea8  DOMAIN,fast.blackbearfiber.com
  + [SukkaW Speedtest Servers International] 5893bd721aca  DOMAIN,stnorthyork.netcrawler.ca
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
  + [SukkaW Speedtest Servers International] 6dfa403b0c42  DOMAIN,speedtest.geniusnetwork.in
  + [SukkaW Speedtest Servers International] 6ef5f28df61c  DOMAIN,ookla.aeq.as6453.net
  + [SukkaW Speedtest Servers International] 74a6d6e46908  DOMAIN,speedtest.wb1.loopinternet.com
  + [SukkaW Speedtest Servers International] 74a7bcdf6ba3  DOMAIN,speed.open.ad.jp
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
  + [SukkaW Speedtest Servers International] 8a039e9d08ba  DOMAIN,speedtest.interligpro.com.br
  + [SukkaW Speedtest Servers International] 8fd05fb4ff7e  DOMAIN,speedtest19.suddenlink.net
  + [SukkaW Speedtest Servers International] 90617691e3af  DOMAIN,stwhitby.netcrawler.ca
  + [SukkaW Speedtest Servers International] 910cf0769104  DOMAIN,speedtest-nwrk-nj.wtsky.net
  + [SukkaW Speedtest Servers International] 9138c74c88d2  DOMAIN,vaspeedtest.rackdog.com
  + [SukkaW Speedtest Servers International] 948613aff3c2  DOMAIN,speedtest.slbcloud.fr
  + [SukkaW Speedtest Servers International] 96e24c3aaac2  DOMAIN,stoshawawireless.rogers.com
  + [SukkaW Speedtest Servers International] 995889b17f13  DOMAIN,lsdspeed02.lsdops.net
  + [SukkaW Speedtest Servers International] 99d636115e4d  DOMAIN,speedtest.kdatacenter.com
  + [SukkaW Speedtest Servers International] 9a0066f1ffcb  DOMAIN,speedtest.vanberkelgroep.nl
  + [SukkaW Speedtest Servers International] 9b36e6ace41e  DOMAIN,phlph0001speedtestserver02.wiline.com
  + [SukkaW Speedtest Servers International] 9c36ab36b132  DOMAIN,phl01.screenshot.download
  + [SukkaW Speedtest Servers International] 9ee8a1734e62  DOMAIN,speedtest2.sistelfibra.es
  + [SukkaW Speedtest Servers International] 9f094a91d810  DOMAIN,ookla.micrologicwv.com
  + [SukkaW Speedtest Servers International] 9f6b30de3d0b  DOMAIN,speedtest-server-ash.starry.com
  + [SukkaW Speedtest Servers International] a8249c53ba8a  DOMAIN,speedtest.thn.uk.syntura.io
  + [SukkaW Speedtest Servers International] b06e6a3b7c0f  DOMAIN,speedtest.philasd.org
  + [SukkaW Speedtest Servers International] b0cc745d6216  DOMAIN,stosat-balt-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] b4f4faf0a782  DOMAIN,speedtest.fiberlync.net
  + [SukkaW Speedtest Servers International] b577445ffd28  DOMAIN,ookla-mgw.wvnet.edu
  + [SukkaW Speedtest Servers International] b7070e1bfc5d  DOMAIN,speedtest.internetsubway.com
  + [SukkaW Speedtest Servers International] b73df15da330  DOMAIN,stetobicoke.netcrawler.ca
  + [SukkaW Speedtest Servers International] b7ea0351589f  DOMAIN,speedtest.revolutionbroadband.net
  + [SukkaW Speedtest Servers International] b7ff9d48bf4d  DOMAIN,ststcatharineswireless.rogers.com
  + [SukkaW Speedtest Servers International] b8002d9cf7f6  DOMAIN,ookla1.talkiefiber.com
  + [SukkaW Speedtest Servers International] b868fcdc5518  DOMAIN,ookla01.citynet.net
  + [SukkaW Speedtest Servers International] be5af7e0a364  DOMAIN,stpickering.netcrawler.ca
  ... and 39 more
```

**Removed: 158** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 012b7f31586b  DOMAIN,ststratford.rogers.com
  - [SukkaW Speedtest Servers International] 02b7b422882f  DOMAIN,speedtest.sentco.net
  - [SukkaW Speedtest Servers International] 04df25e28545  DOMAIN,speedtest.premieronline.net
  - [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  - [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  - [SukkaW Speedtest Servers International] 0bd6b487bcf7  DOMAIN,speedtest.inovewifi.com.br
  - [SukkaW Speedtest Servers International] 0f9fc6befe00  DOMAIN,speed.idnet.net.br
  - [SukkaW Speedtest Servers International] 115915794824  DOMAIN,speedtestmrd1.airtel.in
  - [SukkaW Speedtest Servers International] 1204ab7c7137  DOMAIN,40gspeedtest.mnsi.net
  - [SukkaW Speedtest Servers International] 12ca2bed9dbb  DOMAIN,speedtest.atccomm.net
  - [SukkaW Speedtest Servers International] 13dc2485ab95  DOMAIN,speedtest.heartofiowa.coop
  - [SukkaW Speedtest Servers International] 14696c5e4444  DOMAIN,speedtest.cmltelephone.com
  - [SukkaW Speedtest Servers International] 14c7e265c3d8  DOMAIN,speedtest.ibertic.es
  - [SukkaW Speedtest Servers International] 189c17014e83  DOMAIN,speedtest.amesiaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 1cfb48abbf36  DOMAIN,speedtest.grm.net
  - [SukkaW Speedtest Servers International] 1debbecee8c5  DOMAIN,speedtest.cstech.com
  - [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  - [SukkaW Speedtest Servers International] 1e9ede2ea46b  DOMAIN,speedtest.westianet.com
  - [SukkaW Speedtest Servers International] 218ed97989d5  DOMAIN,ookla.jgainterlinktelecom.com.br
  - [SukkaW Speedtest Servers International] 277377269adc  DOMAIN,wrbg-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 29a310f8327b  DOMAIN,speedtest.brooketel.coop
  - [SukkaW Speedtest Servers International] 2ab9b0da9911  DOMAIN,lcrs-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 304d2683e43f  DOMAIN,speedtest.skywaveconnect.com
  - [SukkaW Speedtest Servers International] 32b355be6336  DOMAIN,speedtest.bluevalley.net
  - [SukkaW Speedtest Servers International] 32c4df87be80  DOMAIN,speed-syd.gigacomm.net.au
  - [SukkaW Speedtest Servers International] 34d320d8b02f  DOMAIN,speedtest.mdtc.net
  - [SukkaW Speedtest Servers International] 358795b67fd5  DOMAIN,speedtest.mornington.ca
  - [SukkaW Speedtest Servers International] 37dae1757a6d  DOMAIN,stsaultstemariewireless.rogers.com
  - [SukkaW Speedtest Servers International] 394dff5a7003  DOMAIN,stwindsorwireless.rogers.com
  - [SukkaW Speedtest Servers International] 3a92209ad6ba  DOMAIN,speedtest-01.omnitel.biz
  - [SukkaW Speedtest Servers International] 3a97abf4595c  DOMAIN,speedtest1.oma.nxlink.com
  - [SukkaW Speedtest Servers International] 3b0dc040ff61  DOMAIN,speed.nutelecom.com
  - [SukkaW Speedtest Servers International] 3ea882635f75  DOMAIN,speed.sdmnet.com.br
  - [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 3f7075e220a1  DOMAIN,ksczks-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 3f8306542a0b  DOMAIN,stsudburywireless.rogers.com
  - [SukkaW Speedtest Servers International] 41bc4d2333e5  DOMAIN,speedtest.cvalley.net
  - [SukkaW Speedtest Servers International] 45ed5f3bd479  DOMAIN,speedtest.tcaexpress.net
  - [SukkaW Speedtest Servers International] 45f4d00908d6  DOMAIN,speedtest-2.hynetwifi.it
  - [SukkaW Speedtest Servers International] 48e2d32a2895  DOMAIN,speedtest.cascadecomm.com
  - [SukkaW Speedtest Servers International] 4b2bec89b1bd  DOMAIN,speedtest.vacastelecom.net
  - [SukkaW Speedtest Servers International] 4bbf2a0a0fa3  DOMAIN,speedtest.mysmbs.com
  - [SukkaW Speedtest Servers International] 4bc2ef4606ca  DOMAIN,st-oma-1.binary.net
  - [SukkaW Speedtest Servers International] 4c8fd6b2f3f6  DOMAIN,ookla-ks.mercuryfiber.com
  - [SukkaW Speedtest Servers International] 4db3cbb342cd  DOMAIN,speedtest-lenexa.resoundnetworks.com
  - [SukkaW Speedtest Servers International] 4de50e12bd16  DOMAIN,speedtest.hay.net
  - [SukkaW Speedtest Servers International] 4fa503514189  DOMAIN,speedtest.packetworks.net
  - [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  - [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  - [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  - [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  - [SukkaW Speedtest Servers International] 565ea387b1e5  DOMAIN,speedtest.cfu.net
  - [SukkaW Speedtest Servers International] 58e6d169adef  DOMAIN,speedtest.esu5.org
  - [SukkaW Speedtest Servers International] 5c69bf15997f  DOMAIN,sp1.speedy.bb-swrag.de
  - [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  - [SukkaW Speedtest Servers International] 5f3fcd920887  DOMAIN,speedtest.ncn.net
  - [SukkaW Speedtest Servers International] 605cfb35f522  DOMAIN,speedtest.mci.as1003.net
  - [SukkaW Speedtest Servers International] 67fb222e7169  DOMAIN,stbrampton.rogers.com
  - [SukkaW Speedtest Servers International] 6a256fc6c285  DOMAIN,speedtest.naturalwireless.com
  - [SukkaW Speedtest Servers International] 6ff5941eb406  DOMAIN,exc-speedtest.unitedfiber.com
  - [SukkaW Speedtest Servers International] 72bb8c1b570f  DOMAIN,speedtest5.windtre.it
  - [SukkaW Speedtest Servers International] 75e802499b21  DOMAIN,stbrampton.netcrawler.ca
  - [SukkaW Speedtest Servers International] 75f76f006b77  DOMAIN,speedtest.58243.as
  - [SukkaW Speedtest Servers International] 761a11540f93  DOMAIN,siouxcity1.cabospeed.com
  - [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  - [SukkaW Speedtest Servers International] 7935cf977efe  DOMAIN,speedtest.wwfn.ca
  - [SukkaW Speedtest Servers International] 7a4042ca0d6f  DOMAIN,stbarriewireless.rogers.com
  - [SukkaW Speedtest Servers International] 7a55e968bb85  DOMAIN,speedtest.unitedfiber.com
  - [SukkaW Speedtest Servers International] 7ad78e8435d7  DOMAIN,speed.ddbroadband.co.in
  - [SukkaW Speedtest Servers International] 7bdc14806a7c  DOMAIN,speedtest.wccta.com
  - [SukkaW Speedtest Servers International] 7ea92d713139  DOMAIN,speedtest.rochmnaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 809ed12ed910  DOMAIN,speedtest.nemr.net
  - [SukkaW Speedtest Servers International] 84b8446a854b  DOMAIN,speedtest10g.ics-llc.net
  - [SukkaW Speedtest Servers International] 86f4178b9153  DOMAIN,speedtest.fibercomm.net
  - [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  - [SukkaW Speedtest Servers International] 8b40d9ed9e30  DOMAIN,speedtestvlc.zafirotelecom.com
  - [SukkaW Speedtest Servers International] 8c67eca44a61  DOMAIN,velocidade.tecsattelecom.com.br
  - [SukkaW Speedtest Servers International] 8c9d7c03fa30  DOMAIN,speedtest27.suddenlink.net
  - [SukkaW Speedtest Servers International] 8cfc393702b7  DOMAIN,speedtest.kc2.everfastfiber.com
  - [SukkaW Speedtest Servers International] 8fb9855a4808  DOMAIN,reikonteste.reikoninternet.com.br
  - [SukkaW Speedtest Servers International] 905125f73ee5  DOMAIN,speedtest.mvec.com
  - [SukkaW Speedtest Servers International] 9052a64cc3fd  DOMAIN,speedtest25.wiatel.com
  - [SukkaW Speedtest Servers International] 9073adefc65d  DOMAIN,speedtest.neitel.net
  - [SukkaW Speedtest Servers International] 93617c692bd8  DOMAIN,ookla.mci-1.serverforge.org
  - [SukkaW Speedtest Servers International] 9868c3f8fedf  DOMAIN,speedtest.s3rdv.com
  - [SukkaW Speedtest Servers International] 991108b39981  DOMAIN,speedtest.mtctech.net
  - [SukkaW Speedtest Servers International] 99246723a229  DOMAIN,speedtest-mci-01.pdx.net.uk
  - [SukkaW Speedtest Servers International] 9fc768aebccf  DOMAIN,speedtest.nexgencom.com
  - [SukkaW Speedtest Servers International] a03e396de9e0  DOMAIN,mib-rst-sp1.mibroadband.com
  - [SukkaW Speedtest Servers International] a0e06516e4c5  DOMAIN,speedtest2.rainbowtel.net
  - [SukkaW Speedtest Servers International] a258e2019d32  DOMAIN,sp1.voyageurinternet.ca
  - [SukkaW Speedtest Servers International] a31c0a6224a2  DOMAIN,storangeville.rogers.com
  - [SukkaW Speedtest Servers International] a64508c249b0  DOMAIN,lnk-speedtest.networknebraska.net
  - [SukkaW Speedtest Servers International] a6619de300c2  DOMAIN,st2a.les.net
  - [SukkaW Speedtest Servers International] a6687b2369f5  DOMAIN,stwaterloo.rogers.com
  - [SukkaW Speedtest Servers International] ab415fae2613  DOMAIN,speedtest.longlines.com
  - [SukkaW Speedtest Servers International] ac4166a2750e  DOMAIN,speedtestfdk.angelbroadband.com
  - [SukkaW Speedtest Servers International] accaab45f3ac  DOMAIN,speedtest-dsm.cowboyhosting.com
  - [SukkaW Speedtest Servers International] accdf3f5dcf1  DOMAIN,stsarniawireless.rogers.com
  - [SukkaW Speedtest Servers International] aecf28573fd6  DOMAIN,speedtest.heartlandtechnology.com
  ... and 58 more
```
