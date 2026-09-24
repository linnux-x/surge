# Surge Rule Diff Report
Generated: 2026-09-25T05:03:03.122177

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 191 |
| Rules removed | 200 |
| Source attribution changed | 77 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 111146 | 111147 | +1 | -0 | ~0 |
| China_IP.list | 11509 | 11508 | +1 | -2 | ~74 |
| Global.list | 24344 | 24346 | +2 | -0 | ~0 |
| Speedtest.list | 1718 | 1707 | +187 | -198 | ~0 |
| Speedtest_China.list | 53 | 53 | +0 | -0 | ~3 |

## China.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] d73bdd57d04e  DOMAIN-SUFFIX,sjfls6.com
```

## China_IP.list

**Added: 1** (showing first 1)
```
  + [Loyalsoldier China CIDR] d2e2b66553d4  IP-CIDR6,2620:57:4004::/47
```

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 China IPs] 37671048987d  IP-CIDR,14.238.34.0/24
  - [Loyalsoldier China CIDR] 6f78e22de263  IP-CIDR6,2620:57:4004::/48
```

**Source changed: 74**
```
  ~ 74b68a3ab24c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ d2d91a77adf5: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ cb563de8a4cd: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 40b363948096: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 3db2c5a7e54e: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7e103bbf2182: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 66379660e08b: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ de827ff46765: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 8c94e7e404d8: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7c954a4dae86: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ dc19540e45a5: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 56a38f955918: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 681c752d987c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ dff7a70835e1: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 8f03d65dc96e: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ f4d311f3a5cd: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 3ef69097e446: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 92b4cef17d31: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 2113d6e07c08: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ d1e863934eed: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ ba58d46995db: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 97ab8ceca4c6: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ b2e4edd4b5f6: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ c500984b6326: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 459716f335f5: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ e1fbd674c0cc: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7e1ac14a8c72: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7e57261b1b2d: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 10e546b63ffc: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 44e4484634fb: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ d3b7af67c4ad: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 6e76624b921e: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 5656533361ea: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ d90c3862c1e1: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ d5af719b5939: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7155e1a74f19: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 6afa5cc7f955: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 59b6d870c0d1: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 06eff7cb4731: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 89237248eb2e: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 36ac628a3fba: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7363b93febd5: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ afdae8084549: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 25a3f0f271e6: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 6153db767c2d: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 830195c60280: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ af765011c92d: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7272254c23d9: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 436515e94536: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 712112b1fceb: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ... and 24 more
```

## Global.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 Global] a38e3de06fca  DOMAIN-SUFFIX,note.com
  + [blackmatrix7 Global] dab926ae2ae0  DOMAIN-SUFFIX,chineseposters.net
```

## Speedtest.list

**Added: 187** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 00f2d0dd6105  DOMAIN,stmilton.rogers.com
  + [SukkaW Speedtest Servers International] 010770237191  DOMAIN,stscarborough.rogers.com
  + [SukkaW Speedtest Servers International] 01d06b461e5c  DOMAIN,speedtest.readingsd.org
  + [SukkaW Speedtest Servers International] 02d48045e4e3  DOMAIN,speed12.gonetspeed.com
  + [SukkaW Speedtest Servers International] 030afc0d216e  DOMAIN,sthamiltonwireless.rogers.com
  + [SukkaW Speedtest Servers International] 04035c8d3237  DOMAIN,speedtest.sonepat.softechinfosol.com
  + [SukkaW Speedtest Servers International] 0694bb696659  DOMAIN,speedtest005.telecomitalia.it
  + [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  + [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  + [SukkaW Speedtest Servers International] 0c4796b1b7c0  DOMAIN,sp1.hcetelecom.com
  + [SukkaW Speedtest Servers International] 0df919f8f00e  DOMAIN,speedtest.nrflvaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 0ef16a17f7b4  DOMAIN,stbowmanville.rogers.com
  + [SukkaW Speedtest Servers International] 0f56643c702c  DOMAIN,stosat-crls-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] 1179f68f6982  DOMAIN,va-speed.magna5.com
  + [SukkaW Speedtest Servers International] 1239ddbeead0  DOMAIN,speed13.gonetspeed.com
  + [SukkaW Speedtest Servers International] 129fa7cf52e5  DOMAIN,speedtest-newjersey.ripplefiber.com
  + [SukkaW Speedtest Servers International] 166d738a2294  DOMAIN,speedtest.toshamisp.com
  + [SukkaW Speedtest Servers International] 16744b51f48f  DOMAIN,speedtest-ash.vts.bf
  + [SukkaW Speedtest Servers International] 180017a0d2ce  DOMAIN,stmiltonwireless.rogers.com
  + [SukkaW Speedtest Servers International] 181f2fd1cbb5  DOMAIN,speedtest.iad.fdcservers.net
  + [SukkaW Speedtest Servers International] 19d98c644b57  DOMAIN,speedtest-iad.sectrify.com
  + [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  + [SukkaW Speedtest Servers International] 1b53005476d3  DOMAIN,speedtest.nrbn.ca
  + [SukkaW Speedtest Servers International] 1dd706232871  DOMAIN,speed10.aitspl.in
  + [SukkaW Speedtest Servers International] 1e3705ee2fe6  DOMAIN,speedtest.oceansls.com
  + [SukkaW Speedtest Servers International] 23d5bd5a13bc  DOMAIN,speedtest.gretna.myriverstreet.net
  + [SukkaW Speedtest Servers International] 2893bfbf70c6  DOMAIN,speedtest.fibernetics.ca
  + [SukkaW Speedtest Servers International] 2c4e9bf40557  DOMAIN,velocity.softtelecom.net.br
  + [SukkaW Speedtest Servers International] 2ddb34614d29  DOMAIN,speedtest2.digimobil.es
  + [SukkaW Speedtest Servers International] 30df7f1427c6  DOMAIN,speedtest.ette.biz
  + [SukkaW Speedtest Servers International] 31b44124210f  DOMAIN,stosat-smil-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] 3263111286ae  DOMAIN,speedtest-zion.fireflyva.com
  + [SukkaW Speedtest Servers International] 32c503790c60  DOMAIN,speedtest3.ptd.net
  + [SukkaW Speedtest Servers International] 33041c0f7fd7  DOMAIN,stbowmanville.netcrawler.ca
  + [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  + [SukkaW Speedtest Servers International] 3556421114ed  DOMAIN,sthamilton.netcrawler.ca
  + [SukkaW Speedtest Servers International] 369df213d503  DOMAIN,nycmetro-speedtest.reliablesite.net
  + [SukkaW Speedtest Servers International] 3787edaca5f8  DOMAIN,emr1-ookla.perf.fastedge.it
  + [SukkaW Speedtest Servers International] 3a8aec9cda98  DOMAIN,speedtest-zl-1.zoominternet.net
  + [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  + [SukkaW Speedtest Servers International] 3ddb6b00187f  DOMAIN,stoakville.rogers.com
  + [SukkaW Speedtest Servers International] 3e7bf0bd143d  DOMAIN,speedtest1.ewr.nj.us.planet.net
  + [SukkaW Speedtest Servers International] 414c35bf776f  DOMAIN,speedtest.us.novoserve.com
  + [SukkaW Speedtest Servers International] 42db00569c58  DOMAIN,speedtest.getwireless.net
  + [SukkaW Speedtest Servers International] 43f75ae5aa25  DOMAIN,speedtest.telbo.net
  + [SukkaW Speedtest Servers International] 44e1fd099c78  DOMAIN,speedtest.sc1.loopinternet.com
  + [SukkaW Speedtest Servers International] 4502550a3a9c  DOMAIN,wpa-speed.magna5.com
  + [SukkaW Speedtest Servers International] 4571f1abe520  DOMAIN,speedtestmacapa.webflash.net.br
  + [SukkaW Speedtest Servers International] 473f9b45897a  DOMAIN,speedtest.winchesterwireless.com
  + [SukkaW Speedtest Servers International] 499c1e741ef8  DOMAIN,asanet1.brsserver.com.br
  + [SukkaW Speedtest Servers International] 49f2fe815df7  DOMAIN,speed.markham.telmax.ca
  + [SukkaW Speedtest Servers International] 49ffc4a2950e  DOMAIN,stoshawa.netcrawler.ca
  + [SukkaW Speedtest Servers International] 4bc5bacc9435  DOMAIN,sp2.fibreair.in
  + [SukkaW Speedtest Servers International] 4f8818240273  DOMAIN,stosat-plfi-08p.sys.comcast.net
  + [SukkaW Speedtest Servers International] 50b8b3905b2f  DOMAIN,speedtest.absenterprises.co.in
  + [SukkaW Speedtest Servers International] 5193c8145d68  DOMAIN,crls-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 520fc7617d3b  DOMAIN,speed-oak.systemlifeline.com
  + [SukkaW Speedtest Servers International] 52a89dbdad82  DOMAIN,speedtest.us-ny2.kamatera.com
  + [SukkaW Speedtest Servers International] 52ea711702a9  DOMAIN,speedtestnorthpointe.arkdnacloud.com
  + [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  + [SukkaW Speedtest Servers International] 5559912850cd  DOMAIN,speedtest.belmontcountygig.com
  + [SukkaW Speedtest Servers International] 55c0cb8dcbb9  DOMAIN,speedtest2.pa.mycci.net
  + [SukkaW Speedtest Servers International] 56ca52c088ca  DOMAIN,speedtest.cogeco.ca
  + [SukkaW Speedtest Servers International] 57cfe7333ea8  DOMAIN,fast.blackbearfiber.com
  + [SukkaW Speedtest Servers International] 5893bd721aca  DOMAIN,stnorthyork.netcrawler.ca
  + [SukkaW Speedtest Servers International] 5a8191463e31  DOMAIN,stmississauga.netcrawler.ca
  + [SukkaW Speedtest Servers International] 5ab2e37aaffc  DOMAIN,speedtest31.suddenlink.net
  + [SukkaW Speedtest Servers International] 5d91b2e1e426  DOMAIN,stgeorgetownwireless.rogers.com
  + [SukkaW Speedtest Servers International] 60ac93c18792  DOMAIN,stscarborough.netcrawler.ca
  + [SukkaW Speedtest Servers International] 615ab422b360  DOMAIN,btlr-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 6240dc262b53  DOMAIN,speedtest1.whsdk12.net
  + [SukkaW Speedtest Servers International] 625966c841d3  DOMAIN,speedtest1.ric1.va.hostedbackbone.net
  + [SukkaW Speedtest Servers International] 6722a4f62ff8  DOMAIN,stbowmanvillewireless.rogers.com
  + [SukkaW Speedtest Servers International] 67382fe7fa61  DOMAIN,stoshawa.rogers.com
  + [SukkaW Speedtest Servers International] 680ff27e9506  DOMAIN,redeultramf.net.br
  + [SukkaW Speedtest Servers International] 6846a38f9372  DOMAIN,speedtest.asbn.va.wtsky.net
  + [SukkaW Speedtest Servers International] 68c6eb173f83  DOMAIN,asbn-speedtest.northstate.net
  + [SukkaW Speedtest Servers International] 698bcfb1bb21  DOMAIN,speedtest-preston-wv.prodigiwv.net
  + [SukkaW Speedtest Servers International] 69cac5e64f73  DOMAIN,stbrantfordwireless.rogers.com
  + [SukkaW Speedtest Servers International] 6aafcc1f0064  DOMAIN,speedtest.americatelecom.net.br
  + [SukkaW Speedtest Servers International] 6b8f1c9f7c44  DOMAIN,stajax.rogers.com
  + [SukkaW Speedtest Servers International] 6ef5f28df61c  DOMAIN,ookla.aeq.as6453.net
  + [SukkaW Speedtest Servers International] 6f3628eaf259  DOMAIN,stkitchener.rogers.com
  + [SukkaW Speedtest Servers International] 71121272f40a  DOMAIN,stceuti1.borecom.com
  + [SukkaW Speedtest Servers International] 74a6d6e46908  DOMAIN,speedtest.wb1.loopinternet.com
  + [SukkaW Speedtest Servers International] 7625db817368  DOMAIN,speedtest1.iad1-us.gozfly.net
  + [SukkaW Speedtest Servers International] 77cb389996a6  DOMAIN,speedtest-bethlehem.greenlightnetworks.com
  + [SukkaW Speedtest Servers International] 77e56dc99c59  DOMAIN,cltn-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 7badd291943b  DOMAIN,speedtestbir.airjaldi.net
  + [SukkaW Speedtest Servers International] 7c4e62477d2e  DOMAIN,speedtest.zoominternet.net
  + [SukkaW Speedtest Servers International] 7de305557319  DOMAIN,altoonaspeedtest.crowsnestbb.net
  + [SukkaW Speedtest Servers International] 7f8672568a56  DOMAIN,speed-miss.systemlifeline.com
  + [SukkaW Speedtest Servers International] 8141004af16b  DOMAIN,speedtest02.srv.prnynj.alticeusa.net
  + [SukkaW Speedtest Servers International] 83e830bbc65c  DOMAIN,speedtest4.point-broadband.com
  + [SukkaW Speedtest Servers International] 8487be6e6d95  DOMAIN,speedtest.mifflincountywireless.com
  + [SukkaW Speedtest Servers International] 85b7f8f6df4c  DOMAIN,spd79.claro.com.br
  + [SukkaW Speedtest Servers International] 8632dbc95ac0  DOMAIN,stnorthyorkwireless.rogers.com
  + [SukkaW Speedtest Servers International] 8764399208a4  DOMAIN,speedtest.msnetworks.in
  + [SukkaW Speedtest Servers International] 8772dc923cf5  DOMAIN,speed-mix.dispaisy.systems
  + [SukkaW Speedtest Servers International] 890fa3aca5ec  DOMAIN,speedtest.orixinet.com.br
  ... and 87 more
```

**Removed: 198** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 012b7f31586b  DOMAIN,ststratford.rogers.com
  - [SukkaW Speedtest Servers International] 01795d9e086e  DOMAIN,speedtest.mvdsl.com
  - [SukkaW Speedtest Servers International] 026e44155485  DOMAIN,stnanaimowireless.rogers.com
  - [SukkaW Speedtest Servers International] 06233ead16e3  DOMAIN,speedtest.phoenix.xiber.net
  - [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  - [SukkaW Speedtest Servers International] 0800ee424fae  DOMAIN,speedtest.frontlineinternetservices.com
  - [SukkaW Speedtest Servers International] 094cf4e8e364  DOMAIN,speedtest02.coppernet.net
  - [SukkaW Speedtest Servers International] 0ab0cf8a6ab9  DOMAIN,speedtest.novateldigital.com
  - [SukkaW Speedtest Servers International] 0bd6b487bcf7  DOMAIN,speedtest.inovewifi.com.br
  - [SukkaW Speedtest Servers International] 0d0d03558cd2  DOMAIN,speed1.tij.attmex.mx
  - [SukkaW Speedtest Servers International] 0d3dfe4cb10b  DOMAIN,speedtest.valleycom.com
  - [SukkaW Speedtest Servers International] 0da9f0879dcc  DOMAIN,speedtestbirpara.meghbelabroadband.in
  - [SukkaW Speedtest Servers International] 0dbbbe7da5ea  DOMAIN,speedtest.wnmc.com
  - [SukkaW Speedtest Servers International] 0f0b324eafca  DOMAIN,speed.webseitenserver.com
  - [SukkaW Speedtest Servers International] 0f9fc6befe00  DOMAIN,speed.idnet.net.br
  - [SukkaW Speedtest Servers International] 1088911f2f25  DOMAIN,test-mi.netoip.com
  - [SukkaW Speedtest Servers International] 1204ab7c7137  DOMAIN,40gspeedtest.mnsi.net
  - [SukkaW Speedtest Servers International] 120ef88aa2bc  DOMAIN,stsurreywireless.rogers.com
  - [SukkaW Speedtest Servers International] 15c5e928553f  DOMAIN,spd1.m5hosting.com
  - [SukkaW Speedtest Servers International] 179230a805a0  DOMAIN,speedtest.tularosa.net
  - [SukkaW Speedtest Servers International] 18669947d48d  DOMAIN,speedtest.ed.shawcable.net
  - [SukkaW Speedtest Servers International] 188233ec18b6  DOMAIN,laxir0008speedtestserver01.wiline.com
  - [SukkaW Speedtest Servers International] 196d8e7f4c77  DOMAIN,lsv11-speedtest01.as15108.com
  - [SukkaW Speedtest Servers International] 1aab8ac0b3c7  DOMAIN,speedtest-sd-da1.scalematrix.com
  - [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  - [SukkaW Speedtest Servers International] 1efe837aa65e  DOMAIN,yms-speed.kbro.com.tw
  - [SukkaW Speedtest Servers International] 20b5384a3b6f  DOMAIN,stlethbridgewireless.rogers.com
  - [SukkaW Speedtest Servers International] 2287e9ddefd2  DOMAIN,stcalgarywireless.rogers.com
  - [SukkaW Speedtest Servers International] 22a64e3ce5a5  DOMAIN,speedtest.skybbservices.com
  - [SukkaW Speedtest Servers International] 22ba33ffb1f2  DOMAIN,acrenettecnologia.brsserver.com.br
  - [SukkaW Speedtest Servers International] 23ab4abca32e  DOMAIN,speedtest.phoenixnap.com
  - [SukkaW Speedtest Servers International] 23b5aa93110d  DOMAIN,sp1.semfronteiras.net.br
  - [SukkaW Speedtest Servers International] 246e115e5220  DOMAIN,srv1297868.hstgr.cloud
  - [SukkaW Speedtest Servers International] 296c2479f156  DOMAIN,speedtest.3dprintingduo.ca
  - [SukkaW Speedtest Servers International] 297f9b1bd0a2  DOMAIN,speedtest.server.battern.eu
  - [SukkaW Speedtest Servers International] 29a310f8327b  DOMAIN,speedtest.brooketel.coop
  - [SukkaW Speedtest Servers International] 2b2178711627  DOMAIN,speedtest.sinetonline.net
  - [SukkaW Speedtest Servers International] 2b71ebccbca0  DOMAIN,speedtest.jackrabbitwireless.com
  - [SukkaW Speedtest Servers International] 2bf6e39176af  DOMAIN,spd01-monr-ca.gigglefiber.com
  - [SukkaW Speedtest Servers International] 2c906a0d677f  DOMAIN,kmlpbcnu-speedtest-01.telus.com
  - [SukkaW Speedtest Servers International] 2ff46c1e7e09  DOMAIN,speedtesttucson.arkdnacloud.com
  - [SukkaW Speedtest Servers International] 31c231df84b9  DOMAIN,speedtest5.nmsurf.com
  - [SukkaW Speedtest Servers International] 33607daf687c  DOMAIN,santaclara-speedtest.utopiafiber.com
  - [SukkaW Speedtest Servers International] 358795b67fd5  DOMAIN,speedtest.mornington.ca
  - [SukkaW Speedtest Servers International] 35c15da72c7b  DOMAIN,spd53.claro.com.br
  - [SukkaW Speedtest Servers International] 365fc1f3200d  DOMAIN,speedtest3.sasknet.sk.ca
  - [SukkaW Speedtest Servers International] 368920dec267  DOMAIN,speedtest-1.somvera.cat
  - [SukkaW Speedtest Servers International] 36b21f97c505  DOMAIN,speedtest4.plateautel.net
  - [SukkaW Speedtest Servers International] 37dae1757a6d  DOMAIN,stsaultstemariewireless.rogers.com
  - [SukkaW Speedtest Servers International] 385ceaa782b7  DOMAIN,speedtest.csfibernet.in
  - [SukkaW Speedtest Servers International] 394dff5a7003  DOMAIN,stwindsorwireless.rogers.com
  - [SukkaW Speedtest Servers International] 3ce95bd82973  DOMAIN,speedtest9.vodafone.com.tr
  - [SukkaW Speedtest Servers International] 3e5e286668c0  DOMAIN,speedtest.symbiosbroadband.net
  - [SukkaW Speedtest Servers International] 3ea882635f75  DOMAIN,speed.sdmnet.com.br
  - [SukkaW Speedtest Servers International] 3fc707025f25  DOMAIN,speedtest.cdlan.net
  - [SukkaW Speedtest Servers International] 404a159ee121  DOMAIN,avspeedtest.apfutura.net
  - [SukkaW Speedtest Servers International] 4442ff60c35a  DOMAIN,speedtest.ftmojave.net
  - [SukkaW Speedtest Servers International] 451355c159de  DOMAIN,speedtest-az.bambroadband.com
  - [SukkaW Speedtest Servers International] 457c7c64a7cb  DOMAIN,prescott1.cabospeed.com
  - [SukkaW Speedtest Servers International] 4711a85a14ce  DOMAIN,speedtest.cdpalace.in
  - [SukkaW Speedtest Servers International] 497d447ac483  DOMAIN,speedtest.gilarivertel.com
  - [SukkaW Speedtest Servers International] 4b2bec89b1bd  DOMAIN,speedtest.vacastelecom.net
  - [SukkaW Speedtest Servers International] 4c343b690433  DOMAIN,speedtest4.ezeefiber.net
  - [SukkaW Speedtest Servers International] 4de50e12bd16  DOMAIN,speedtest.hay.net
  - [SukkaW Speedtest Servers International] 4ff867dabe73  DOMAIN,speedtestslg.alliancebroadband.in
  - [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  - [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  - [SukkaW Speedtest Servers International] 51ab10282432  DOMAIN,speedtest.infowest.com
  - [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  - [SukkaW Speedtest Servers International] 5356e4886192  DOMAIN,speedtesthost.sasknet.sk.ca
  - [SukkaW Speedtest Servers International] 53e6f989e749  DOMAIN,riorancho1.cabospeed.com
  - [SukkaW Speedtest Servers International] 56784b2201f6  DOMAIN,spd-phnhazva.wyyerd.io
  - [SukkaW Speedtest Servers International] 58514000804b  DOMAIN,slgrooklaspeed1.jioconnect.com
  - [SukkaW Speedtest Servers International] 58d5ea3bc911  DOMAIN,speedtest.gv.shawcable.net
  - [SukkaW Speedtest Servers International] 5c69bf15997f  DOMAIN,sp1.speedy.bb-swrag.de
  - [SukkaW Speedtest Servers International] 5e342aaaae72  DOMAIN,speedtest.gorkhainfotech.in
  - [SukkaW Speedtest Servers International] 5ee6efe075b3  DOMAIN,speedtest.ngcbroadband.com
  - [SukkaW Speedtest Servers International] 5fbb145eb5ba  DOMAIN,speedtest.kouten.barcelona
  - [SukkaW Speedtest Servers International] 62a3774a6ad0  DOMAIN,velocimetro-rbo.virtua.com.br
  - [SukkaW Speedtest Servers International] 646f766c0f34  DOMAIN,speedtest.unmbroadbandservice.com
  - [SukkaW Speedtest Servers International] 658a714cbecd  DOMAIN,sp1.contilnet.net
  - [SukkaW Speedtest Servers International] 67a9c4720203  DOMAIN,speedtest.skaybroadband.com
  - [SukkaW Speedtest Servers International] 6992afbc4517  DOMAIN,phoenix1.cabospeed.com
  - [SukkaW Speedtest Servers International] 69eb17adddcb  DOMAIN,sp1.socen.com
  - [SukkaW Speedtest Servers International] 6b49fe0152c9  DOMAIN,spd49.claro.com.br
  - [SukkaW Speedtest Servers International] 6be2d4ce5009  DOMAIN,lv-ookla.geolinks.com
  - [SukkaW Speedtest Servers International] 6fbf06a1c59f  DOMAIN,speedtest.hynetwifi.it
  - [SukkaW Speedtest Servers International] 71329f904b4a  DOMAIN,stczs.norteultrafibra.com.br
  - [SukkaW Speedtest Servers International] 7234c43482c2  DOMAIN,speedtest.ioflood.com
  - [SukkaW Speedtest Servers International] 723b77b1998b  DOMAIN,speedtestalbq.vexusfiber.com
  - [SukkaW Speedtest Servers International] 73e966caf50f  DOMAIN,spd-phnxaz19.wyyerd.io
  - [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  - [SukkaW Speedtest Servers International] 7737d7921c63  DOMAIN,sp2.semfronteiras.net.br
  - [SukkaW Speedtest Servers International] 7785c86daf50  DOMAIN,speedtest.sizatek.com
  - [SukkaW Speedtest Servers International] 77de3e0d51c6  DOMAIN,test.beamtelecom.com.br
  - [SukkaW Speedtest Servers International] 78bb50fdaca3  DOMAIN,velocimetro.govistabr.com.br
  - [SukkaW Speedtest Servers International] 7935cf977efe  DOMAIN,speedtest.wwfn.ca
  - [SukkaW Speedtest Servers International] 79fd2808f8ae  DOMAIN,speedtest-jgn.galaxynet.in
  - [SukkaW Speedtest Servers International] 7a26c3838cf7  DOMAIN,speedtest.centralnetprovedor.net.br
  - [SukkaW Speedtest Servers International] 7ad78e8435d7  DOMAIN,speed.ddbroadband.co.in
  ... and 98 more
```

## Speedtest_China.list

**Source changed: 3**
```
  ~ 6184144f6695: [SukkaW Speedtest Servers China → spiritLHLS Speedtest.cn China]
  ~ f5a2ed9ad227: [SukkaW Speedtest Servers China → spiritLHLS Speedtest.cn China]
  ~ f153e08b4850: [SukkaW Speedtest Servers China → spiritLHLS Speedtest.cn China]
```
