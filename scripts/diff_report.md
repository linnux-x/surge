# Surge Rule Diff Report
Generated: 2026-09-19T11:40:43.360236

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 226 |
| Rules removed | 172 |
| Source attribution changed | 69 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 111138 | 111137 | +0 | -1 | ~1 |
| China_IP.list | 11498 | 11510 | +15 | -3 | ~68 |
| Download.list | 1687 | 1689 | +2 | -0 | ~0 |
| Global.list | 24335 | 24339 | +4 | -0 | ~0 |
| Speedtest.list | 1685 | 1722 | +205 | -168 | ~0 |

## China.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 5d465bfe29fd  DOMAIN-SUFFIX,spst2.com
```

**Source changed: 1**
```
  ~ 1e6f02564601: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
```

## China_IP.list

**Added: 15** (showing first 15)
```
  + [Loyalsoldier China CIDR] 1a4dd508b287  IP-CIDR6,2406:840:a33::/48
  + [Loyalsoldier China CIDR] 241e11cc7cfc  IP-CIDR6,2001:df3:d0c0::/48
  + [Loyalsoldier China CIDR] 36ac628a3fba  IP-CIDR6,2001:678:12c4::/48
  + [blackmatrix7 China IPs] 37671048987d  IP-CIDR,14.238.34.0/24
  + [Loyalsoldier China CIDR] 3ff6cc72f451  IP-CIDR6,2402:73e0::/32
  + [Loyalsoldier China CIDR] 532a1d679aae  IP-CIDR6,2001:678:12b8::/48
  + [Loyalsoldier China CIDR] 5656533361ea  IP-CIDR6,2001:df5:2fc0::/48
  + [Loyalsoldier China CIDR] 56a38f955918  IP-CIDR6,2001:67c:ebc::/48
  + [Loyalsoldier China CIDR] 6f78e22de263  IP-CIDR6,2620:57:4004::/48
  + [Loyalsoldier China CIDR] d03f4dac7df6  IP-CIDR6,2001:df4:e142::/47
  + [Loyalsoldier China CIDR] d2d91a77adf5  IP-CIDR6,2001:df4:e140::/48
  + [Loyalsoldier China CIDR] d3b7af67c4ad  IP-CIDR6,2001:67c:2c1c::/48
  + [Loyalsoldier China CIDR] e3fb171f5a81  IP-CIDR6,2001:df5:4cc0::/48
  + [Loyalsoldier China CIDR] f77fdd53d05b  IP-CIDR6,2001:678:12cc::/48
  + [Loyalsoldier China CIDR] f7ab32b6c196  IP-CIDR,163.52.108.0/23
```

**Removed: 3** (showing first 3)
```
  - [Loyalsoldier China CIDR] 02949a5ef7ac  IP-CIDR6,2c0f:f7a8:9220::/48
  - [Loyalsoldier China CIDR] 679c832e8fec  IP-CIDR6,2406:840:a32::/47
  - [Loyalsoldier China CIDR] b009f9866230  IP-CIDR6,2c0f:f7a8:9020::/48
```

**Source changed: 68**
```
  ~ 8698609d0ee3: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 7f0a1e6155c7: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ dc19540e45a5: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 300385b26f2f: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7272254c23d9: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 712112b1fceb: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 459716f335f5: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d4e2c9295d61: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ cde87914fb5f: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 8c94e7e404d8: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d5af719b5939: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ f9b394cd416a: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ af765011c92d: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ bcf3a4955435: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ fb25eb56def0: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 10e546b63ffc: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 1b4dc4262f33: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 66379660e08b: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 6153db767c2d: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ ba58d46995db: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d0c1f0d4b70a: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 240ffe2a374c: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 7e103bbf2182: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 2113d6e07c08: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 97ab8ceca4c6: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 830195c60280: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ f87a9f222cdd: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 662d0ee1e16f: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 06eff7cb4731: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 7e1ac14a8c72: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ de1e716e741c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 7c954a4dae86: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 4669cef56389: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 4537cbb68f03: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ afdae8084549: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 7781a662df7c: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 635d77a124a1: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 8f03d65dc96e: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 6fea53611592: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 3ef69097e446: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d440c3027fe4: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 89237248eb2e: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 59b6d870c0d1: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 661709c4ed56: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ ac3f837b684c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 25f40c794153: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ a906fb436fb8: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ dff7a70835e1: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ b2e4edd4b5f6: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 91f19c29c9cd: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ... and 18 more
```

## Download.list

**Added: 2** (showing first 2)
```
  + [SukkaW Download] 0734c757c0a3  DOMAIN,repo.xtom.com
  + [SukkaW Download] 8baf1fc112ea  DOMAIN,dl.gl-inet.com
```

## Global.list

**Added: 4** (showing first 4)
```
  + [blackmatrix7 Global] 2b454852452e  DOMAIN-SUFFIX,stripe.dev
  + [blackmatrix7 Global] 4b1466d7f70c  DOMAIN-SUFFIX,stripe.global
  + [blackmatrix7 Global] 6f3e9d859498  DOMAIN-SUFFIX,quakemachinex.com
  + [blackmatrix7 Global] e8a2a4c4fc5c  DOMAIN-SUFFIX,stripe.events
```

## Speedtest.list

**Added: 205** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 01795d9e086e  DOMAIN,speedtest.mvdsl.com
  + [SukkaW Speedtest Servers International] 026e44155485  DOMAIN,stnanaimowireless.rogers.com
  + [SukkaW Speedtest Servers International] 06233ead16e3  DOMAIN,speedtest.phoenix.xiber.net
  + [SukkaW Speedtest Servers International] 0694bb696659  DOMAIN,speedtest005.telecomitalia.it
  + [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  + [SukkaW Speedtest Servers International] 07f2b6f071b3  DOMAIN,speedtest.conectnorte.com.br
  + [SukkaW Speedtest Servers International] 0800ee424fae  DOMAIN,speedtest.frontlineinternetservices.com
  + [SukkaW Speedtest Servers International] 094cf4e8e364  DOMAIN,speedtest02.coppernet.net
  + [SukkaW Speedtest Servers International] 0a62b057e9d6  DOMAIN,speedtest.ak4digital.com.br
  + [SukkaW Speedtest Servers International] 0bd6b487bcf7  DOMAIN,speedtest.inovewifi.com.br
  + [SukkaW Speedtest Servers International] 0cc435ecaed2  DOMAIN,teste.freedomnetwork.net.br
  + [SukkaW Speedtest Servers International] 0d0d03558cd2  DOMAIN,speed1.tij.attmex.mx
  + [SukkaW Speedtest Servers International] 0d3dfe4cb10b  DOMAIN,speedtest.valleycom.com
  + [SukkaW Speedtest Servers International] 0d69972a0124  DOMAIN,speedtest.netpool.in
  + [SukkaW Speedtest Servers International] 0da9f0879dcc  DOMAIN,speedtestbirpara.meghbelabroadband.in
  + [SukkaW Speedtest Servers International] 0dbbbe7da5ea  DOMAIN,speedtest.wnmc.com
  + [SukkaW Speedtest Servers International] 0f0b324eafca  DOMAIN,speed.webseitenserver.com
  + [SukkaW Speedtest Servers International] 120ef88aa2bc  DOMAIN,stsurreywireless.rogers.com
  + [SukkaW Speedtest Servers International] 15c5e928553f  DOMAIN,spd1.m5hosting.com
  + [SukkaW Speedtest Servers International] 16a73583ad03  DOMAIN,speedtest.ams14.usenet.farm
  + [SukkaW Speedtest Servers International] 179230a805a0  DOMAIN,speedtest.tularosa.net
  + [SukkaW Speedtest Servers International] 18669947d48d  DOMAIN,speedtest.ed.shawcable.net
  + [SukkaW Speedtest Servers International] 186aee23db73  DOMAIN,teste.wsfibra.com.br
  + [SukkaW Speedtest Servers International] 188233ec18b6  DOMAIN,laxir0008speedtestserver01.wiline.com
  + [SukkaW Speedtest Servers International] 196d8e7f4c77  DOMAIN,lsv11-speedtest01.as15108.com
  + [SukkaW Speedtest Servers International] 1aab8ac0b3c7  DOMAIN,speedtest-sd-da1.scalematrix.com
  + [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  + [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 209956ca6491  DOMAIN,speedtest-mumbai.scify.co.in
  + [SukkaW Speedtest Servers International] 20b5384a3b6f  DOMAIN,stlethbridgewireless.rogers.com
  + [SukkaW Speedtest Servers International] 2287e9ddefd2  DOMAIN,stcalgarywireless.rogers.com
  + [SukkaW Speedtest Servers International] 22a64e3ce5a5  DOMAIN,speedtest.skybbservices.com
  + [SukkaW Speedtest Servers International] 22ba33ffb1f2  DOMAIN,acrenettecnologia.brsserver.com.br
  + [SukkaW Speedtest Servers International] 23ab4abca32e  DOMAIN,speedtest.phoenixnap.com
  + [SukkaW Speedtest Servers International] 23b5aa93110d  DOMAIN,sp1.semfronteiras.net.br
  + [SukkaW Speedtest Servers International] 246e115e5220  DOMAIN,srv1297868.hstgr.cloud
  + [SukkaW Speedtest Servers International] 289a44e7222d  DOMAIN,speedtest.sea.aixxycode.id
  + [SukkaW Speedtest Servers International] 296c2479f156  DOMAIN,speedtest.3dprintingduo.ca
  + [SukkaW Speedtest Servers International] 297f9b1bd0a2  DOMAIN,speedtest.server.battern.eu
  + [SukkaW Speedtest Servers International] 2b2178711627  DOMAIN,speedtest.sinetonline.net
  + [SukkaW Speedtest Servers International] 2b71ebccbca0  DOMAIN,speedtest.jackrabbitwireless.com
  + [SukkaW Speedtest Servers International] 2bf6e39176af  DOMAIN,spd01-monr-ca.gigglefiber.com
  + [SukkaW Speedtest Servers International] 2c906a0d677f  DOMAIN,kmlpbcnu-speedtest-01.telus.com
  + [SukkaW Speedtest Servers International] 2ff46c1e7e09  DOMAIN,speedtesttucson.arkdnacloud.com
  + [SukkaW Speedtest Servers International] 31c231df84b9  DOMAIN,speedtest5.nmsurf.com
  + [SukkaW Speedtest Servers International] 33607daf687c  DOMAIN,santaclara-speedtest.utopiafiber.com
  + [SukkaW Speedtest Servers International] 35c15da72c7b  DOMAIN,spd53.claro.com.br
  + [SukkaW Speedtest Servers International] 365fc1f3200d  DOMAIN,speedtest3.sasknet.sk.ca
  + [SukkaW Speedtest Servers International] 368920dec267  DOMAIN,speedtest-1.somvera.cat
  + [SukkaW Speedtest Servers International] 36b21f97c505  DOMAIN,speedtest4.plateautel.net
  + [SukkaW Speedtest Servers International] 385ceaa782b7  DOMAIN,speedtest.csfibernet.in
  + [SukkaW Speedtest Servers International] 3e5e286668c0  DOMAIN,speedtest.symbiosbroadband.net
  + [SukkaW Speedtest Servers International] 404a159ee121  DOMAIN,avspeedtest.apfutura.net
  + [SukkaW Speedtest Servers International] 435df8f008e0  DOMAIN,speedtest.respawnhost.com
  + [SukkaW Speedtest Servers International] 4442ff60c35a  DOMAIN,speedtest.ftmojave.net
  + [SukkaW Speedtest Servers International] 451355c159de  DOMAIN,speedtest-az.bambroadband.com
  + [SukkaW Speedtest Servers International] 457c7c64a7cb  DOMAIN,prescott1.cabospeed.com
  + [SukkaW Speedtest Servers International] 4711a85a14ce  DOMAIN,speedtest.cdpalace.in
  + [SukkaW Speedtest Servers International] 497d447ac483  DOMAIN,speedtest.gilarivertel.com
  + [SukkaW Speedtest Servers International] 49b9326423c6  DOMAIN,a-speedtest.brasildigital.net.br
  + [SukkaW Speedtest Servers International] 4c343b690433  DOMAIN,speedtest4.ezeefiber.net
  + [SukkaW Speedtest Servers International] 4db07187683d  DOMAIN,speedtest.ollatelecom.com.br
  + [SukkaW Speedtest Servers International] 4f2fad74fb12  DOMAIN,stosat-chic-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] 4ff867dabe73  DOMAIN,speedtestslg.alliancebroadband.in
  + [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  + [SukkaW Speedtest Servers International] 50eaac06d8c4  DOMAIN,st-mersin-1.turksatkablo.com.tr
  + [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  + [SukkaW Speedtest Servers International] 51ab10282432  DOMAIN,speedtest.infowest.com
  + [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  + [SukkaW Speedtest Servers International] 5356e4886192  DOMAIN,speedtesthost.sasknet.sk.ca
  + [SukkaW Speedtest Servers International] 53e6f989e749  DOMAIN,riorancho1.cabospeed.com
  + [SukkaW Speedtest Servers International] 56784b2201f6  DOMAIN,spd-phnhazva.wyyerd.io
  + [SukkaW Speedtest Servers International] 58514000804b  DOMAIN,slgrooklaspeed1.jioconnect.com
  + [SukkaW Speedtest Servers International] 58d5ea3bc911  DOMAIN,speedtest.gv.shawcable.net
  + [SukkaW Speedtest Servers International] 5ad130cfadf0  DOMAIN,speedtest.miriquidi-net.works
  + [SukkaW Speedtest Servers International] 5b59c5167680  DOMAIN,sqaookla.ddns.net
  + [SukkaW Speedtest Servers International] 5e30d73d204d  DOMAIN,speedtest.conectjadns.com.br
  + [SukkaW Speedtest Servers International] 5e342aaaae72  DOMAIN,speedtest.gorkhainfotech.in
  + [SukkaW Speedtest Servers International] 5ee6efe075b3  DOMAIN,speedtest.ngcbroadband.com
  + [SukkaW Speedtest Servers International] 5fbb145eb5ba  DOMAIN,speedtest.kouten.barcelona
  + [SukkaW Speedtest Servers International] 62a3774a6ad0  DOMAIN,velocimetro-rbo.virtua.com.br
  + [SukkaW Speedtest Servers International] 646f766c0f34  DOMAIN,speedtest.unmbroadbandservice.com
  + [SukkaW Speedtest Servers International] 658a714cbecd  DOMAIN,sp1.contilnet.net
  + [SukkaW Speedtest Servers International] 66733127c989  DOMAIN,speedtest.nikhilnetworksolution.in
  + [SukkaW Speedtest Servers International] 67981197c2f4  DOMAIN,speedtest.ipvolume.net
  + [SukkaW Speedtest Servers International] 67a9c4720203  DOMAIN,speedtest.skaybroadband.com
  + [SukkaW Speedtest Servers International] 6992afbc4517  DOMAIN,phoenix1.cabospeed.com
  + [SukkaW Speedtest Servers International] 69eb17adddcb  DOMAIN,sp1.socen.com
  + [SukkaW Speedtest Servers International] 6b49fe0152c9  DOMAIN,spd49.claro.com.br
  + [SukkaW Speedtest Servers International] 6be2d4ce5009  DOMAIN,lv-ookla.geolinks.com
  + [SukkaW Speedtest Servers International] 6c2700158660  DOMAIN,speed.fgtelecom.com.br
  + [SukkaW Speedtest Servers International] 70b3b41d196f  DOMAIN,speedtestro.vtal.net.br
  + [SukkaW Speedtest Servers International] 71329f904b4a  DOMAIN,stczs.norteultrafibra.com.br
  + [SukkaW Speedtest Servers International] 7234c43482c2  DOMAIN,speedtest.ioflood.com
  + [SukkaW Speedtest Servers International] 723b77b1998b  DOMAIN,speedtestalbq.vexusfiber.com
  + [SukkaW Speedtest Servers International] 73e966caf50f  DOMAIN,spd-phnxaz19.wyyerd.io
  + [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 7737d7921c63  DOMAIN,sp2.semfronteiras.net.br
  + [SukkaW Speedtest Servers International] 7785c86daf50  DOMAIN,speedtest.sizatek.com
  + [SukkaW Speedtest Servers International] 77de3e0d51c6  DOMAIN,test.beamtelecom.com.br
  ... and 105 more
```

**Removed: 168** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 0009d45cc71f  DOMAIN,speedtest-gdrp.merit.edu
  - [SukkaW Speedtest Servers International] 00f2d0dd6105  DOMAIN,stmilton.rogers.com
  - [SukkaW Speedtest Servers International] 030afc0d216e  DOMAIN,sthamiltonwireless.rogers.com
  - [SukkaW Speedtest Servers International] 04035c8d3237  DOMAIN,speedtest.sonepat.softechinfosol.com
  - [SukkaW Speedtest Servers International] 0561b044089c  DOMAIN,ran-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 0711f9d6046b  DOMAIN,cbpuspeed.aspensmart.net
  - [SukkaW Speedtest Servers International] 07a422190a83  DOMAIN,velocimetro.stylosnet.com.br
  - [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  - [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  - [SukkaW Speedtest Servers International] 0a22eed90fb5  DOMAIN,testdevelocidadval.jazztel.com
  - [SukkaW Speedtest Servers International] 0c4796b1b7c0  DOMAIN,sp1.hcetelecom.com
  - [SukkaW Speedtest Servers International] 0f0435a45fac  DOMAIN,speedtest.oa.net
  - [SukkaW Speedtest Servers International] 0f923e75457a  DOMAIN,ookla-in.mercuryfiber.com
  - [SukkaW Speedtest Servers International] 10b70122f1cf  DOMAIN,speedtest.airsip.net
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
  - [SukkaW Speedtest Servers International] 2ca7f6ca150a  DOMAIN,speedtest.lax1.nitelusa.net
  - [SukkaW Speedtest Servers International] 307576fe3a3c  DOMAIN,speedtest.ld7.fdcservers.net
  - [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  - [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  - [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  - [SukkaW Speedtest Servers International] 3556421114ed  DOMAIN,sthamilton.netcrawler.ca
  - [SukkaW Speedtest Servers International] 357b92f115d8  DOMAIN,speed.sparcs.net
  - [SukkaW Speedtest Servers International] 358f08550b7a  DOMAIN,spd-pub-rm-01-01.fastwebnet.it
  - [SukkaW Speedtest Servers International] 39effaab36a6  DOMAIN,velocidade.hrcfiber.com
  - [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  - [SukkaW Speedtest Servers International] 3ddb6b00187f  DOMAIN,stoakville.rogers.com
  - [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  - [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  - [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  - [SukkaW Speedtest Servers International] 4571f1abe520  DOMAIN,speedtestmacapa.webflash.net.br
  - [SukkaW Speedtest Servers International] 499c1e741ef8  DOMAIN,asanet1.brsserver.com.br
  - [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  - [SukkaW Speedtest Servers International] 4bc5bacc9435  DOMAIN,sp2.fibreair.in
  - [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  - [SukkaW Speedtest Servers International] 4d1a0ae1e138  DOMAIN,speedtest.dongfong.com.tw
  - [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 4fa503514189  DOMAIN,speedtest.packetworks.net
  - [SukkaW Speedtest Servers International] 50b8b3905b2f  DOMAIN,speedtest.absenterprises.co.in
  - [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  - [SukkaW Speedtest Servers International] 520fc7617d3b  DOMAIN,speed-oak.systemlifeline.com
  - [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 5457b4c37fd0  DOMAIN,speedtest.uv.es
  - [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  - [SukkaW Speedtest Servers International] 56ca52c088ca  DOMAIN,speedtest.cogeco.ca
  - [SukkaW Speedtest Servers International] 5a8191463e31  DOMAIN,stmississauga.netcrawler.ca
  - [SukkaW Speedtest Servers International] 5b632554813d  DOMAIN,speed.ultranetrr.com.br
  - [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  - [SukkaW Speedtest Servers International] 5d91b2e1e426  DOMAIN,stgeorgetownwireless.rogers.com
  - [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  - [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  - [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  - [SukkaW Speedtest Servers International] 626849c0a751  DOMAIN,st1.worldfibernet.com
  - [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  - [SukkaW Speedtest Servers International] 6382a86a4d91  DOMAIN,speed.telcomnetwork.net
  - [SukkaW Speedtest Servers International] 66b82b637c97  DOMAIN,test.geocity.co.in
  - [SukkaW Speedtest Servers International] 67fb222e7169  DOMAIN,stbrampton.rogers.com
  - [SukkaW Speedtest Servers International] 69cac5e64f73  DOMAIN,stbrantfordwireless.rogers.com
  - [SukkaW Speedtest Servers International] 6aafcc1f0064  DOMAIN,speedtest.americatelecom.net.br
  - [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  - [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  - [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  - [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  - [SukkaW Speedtest Servers International] 6f3628eaf259  DOMAIN,stkitchener.rogers.com
  - [SukkaW Speedtest Servers International] 6fbf06a1c59f  DOMAIN,speedtest.hynetwifi.it
  - [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  - [SukkaW Speedtest Servers International] 75e802499b21  DOMAIN,stbrampton.netcrawler.ca
  - [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  - [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 7f8672568a56  DOMAIN,speed-miss.systemlifeline.com
  - [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  - [SukkaW Speedtest Servers International] 85b7f8f6df4c  DOMAIN,spd79.claro.com.br
  - [SukkaW Speedtest Servers International] 8764399208a4  DOMAIN,speedtest.msnetworks.in
  - [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  - [SukkaW Speedtest Servers International] 890fa3aca5ec  DOMAIN,speedtest.orixinet.com.br
  - [SukkaW Speedtest Servers International] 8c8abdf2d7dc  DOMAIN,speed.weendeavor.com
  - [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  - [SukkaW Speedtest Servers International] 8e36c5eb6ca2  DOMAIN,speedtest2.micronet.in
  - [SukkaW Speedtest Servers International] 8f062e512925  DOMAIN,speedtestsonipat.kkdbroadband.co.in
  - [SukkaW Speedtest Servers International] 8fda1d8fef4c  DOMAIN,lmb1-ookla.perf.fastedge.it
  - [SukkaW Speedtest Servers International] 905125f73ee5  DOMAIN,speedtest.mvec.com
  - [SukkaW Speedtest Servers International] 91dd7903cffa  DOMAIN,speedtest.conectaamazonia.com.br
  - [SukkaW Speedtest Servers International] 92e005ab26ce  DOMAIN,medidor.nortelecom.com.br
  - [SukkaW Speedtest Servers International] 934ad5aa9642  DOMAIN,speedtest10g.bhm.as13760.net
  - [SukkaW Speedtest Servers International] 938f4673095b  DOMAIN,speedtest.cloudwifi.ca
  - [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 96692f154a26  DOMAIN,veloteste.mrjomar.com.br
  ... and 68 more
```
