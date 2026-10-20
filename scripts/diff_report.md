# Surge Rule Diff Report
Generated: 2026-10-21T05:01:36.116867

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 141 |
| Rules removed | 196 |
| Source attribution changed | 6 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110567 | 110567 | +0 | -0 | ~1 |
| China_IP.list | 11843 | 11846 | +5 | -2 | ~5 |
| Download.list | 1696 | 1695 | +0 | -1 | ~0 |
| Global.list | 24486 | 24501 | +17 | -2 | ~0 |
| Speedtest.list | 1708 | 1636 | +119 | -191 | ~0 |

## China.list

**Source changed: 1**
```
  ~ 156a1d2371f5: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
```

## China_IP.list

**Added: 5** (showing first 5)
```
  + [Loyalsoldier China CIDR] 29427252e06c  IP-CIDR,160.202.210.0/23
  + [Loyalsoldier China CIDR] 350f861ed6d7  IP-CIDR,192.140.244.0/23
  + [Loyalsoldier China CIDR] 659c84571f09  IP-CIDR6,2402:7ee0::/32
  + [Loyalsoldier China CIDR] a6db9978c34b  IP-CIDR6,240b:4006:1100::/44
  + [Loyalsoldier China CIDR] de20c68d3293  IP-CIDR,47.246.216.0/22
```

**Removed: 2** (showing first 2)
```
  - [Loyalsoldier China CIDR] 1a14e69654ba  IP-CIDR6,240b:4006:1100::/45
  - [Loyalsoldier China CIDR] 44ca3346e359  IP-CIDR6,240b:4006:110c::/46
```

**Source changed: 5**
```
  ~ aa20a14a3676: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 7f6313ff65fb: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 5120e1427596: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 4bd08bfb3f64: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 5fe5cd7eaa3c: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Download.list

**Removed: 1** (showing first 1)
```
  - [SukkaW Download] 68167a312594  DOMAIN,releases.openai.com
```

## Global.list

**Added: 17** (showing first 17)
```
  + [blackmatrix7 Global] 12b6fbfa1397  DOMAIN-SUFFIX,timewebcloud.kz
  + [blackmatrix7 Global] 25d79c5d30b5  DOMAIN-SUFFIX,bget.ru
  + [blackmatrix7 Global] 34c6019681a0  DOMAIN-SUFFIX,timeweb.tech
  + [blackmatrix7 Global] 3ca619387909  DOMAIN-SUFFIX,beserver.ru
  + [blackmatrix7 Global] 4204575bf5f9  DOMAIN-SUFFIX,xn--90aefb9d.xn--p1ai
  + [blackmatrix7 Global] 472514fb5743  DOMAIN-SUFFIX,beget.de
  + [blackmatrix7 Global] 48edac17660f  DOMAIN-SUFFIX,schwabcdn.com
  + [blackmatrix7 Global] 66621031ad89  DOMAIN-SUFFIX,openai.org
  + [blackmatrix7 Global] 87a78acd451e  DOMAIN-SUFFIX,beget.app
  + [blackmatrix7 Global] 905c2e09a434  DOMAIN-SUFFIX,sprut.io
  + [blackmatrix7 Global] 9c1e83ead256  DOMAIN-SUFFIX,typesafe.ai
  + [blackmatrix7 Global] b35c8d992742  DOMAIN-SUFFIX,beget.hosting
  + [blackmatrix7 Global] bdc81e04bcec  DOMAIN-SUFFIX,beget.tech
  + [blackmatrix7 Global] c79a4173e7c6  DOMAIN-SUFFIX,begetcdn.cloud
  + [blackmatrix7 Global] e9a5e2a03ea6  DOMAIN-SUFFIX,cursorvm.com
  + [blackmatrix7 Global] f41789621bc1  DOMAIN-SUFFIX,beget.pro
  + [blackmatrix7 Global] ff8edc949825  DOMAIN-SUFFIX,beget.cloud
```

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 Global] 22bb370915a5  DOMAIN-SUFFIX,flightsimulator.com
  - [blackmatrix7 Global] 89f7d54ff962  DOMAIN-SUFFIX,asobostudio.com
```

## Speedtest.list

**Added: 119** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 0009d45cc71f  DOMAIN,speedtest-gdrp.merit.edu
  + [SukkaW Speedtest Servers International] 012b7f31586b  DOMAIN,ststratford.rogers.com
  + [SukkaW Speedtest Servers International] 0561b044089c  DOMAIN,ran-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 0711f9d6046b  DOMAIN,cbpuspeed.aspensmart.net
  + [SukkaW Speedtest Servers International] 0ab0cf8a6ab9  DOMAIN,speedtest.novateldigital.com
  + [SukkaW Speedtest Servers International] 0bd6b487bcf7  DOMAIN,speedtest.inovewifi.com.br
  + [SukkaW Speedtest Servers International] 0e2647e5d386  DOMAIN,speedtest.kos.net
  + [SukkaW Speedtest Servers International] 0f0435a45fac  DOMAIN,speedtest.oa.net
  + [SukkaW Speedtest Servers International] 0f923e75457a  DOMAIN,ookla-in.mercuryfiber.com
  + [SukkaW Speedtest Servers International] 0f9fc6befe00  DOMAIN,speed.idnet.net.br
  + [SukkaW Speedtest Servers International] 1204ab7c7137  DOMAIN,40gspeedtest.mnsi.net
  + [SukkaW Speedtest Servers International] 134564537572  DOMAIN,speedtest.sycmilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 14c7e265c3d8  DOMAIN,speedtest.ibertic.es
  + [SukkaW Speedtest Servers International] 15ee8e1a505a  DOMAIN,speedtest.volo.net
  + [SukkaW Speedtest Servers International] 16699495d33c  DOMAIN,speed.uberlinktelecom.com.br
  + [SukkaW Speedtest Servers International] 1753c7265a8d  DOMAIN,st1.ligtel.com
  + [SukkaW Speedtest Servers International] 1debbecee8c5  DOMAIN,speedtest.cstech.com
  + [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 22e17aa36c22  DOMAIN,speedtest-wc.truestreamfiber.us
  + [SukkaW Speedtest Servers International] 2785a4313085  DOMAIN,teste.suprainternet.com.br
  + [SukkaW Speedtest Servers International] 27aa9cef1e30  DOMAIN,bytp-speedtest-1.123.net
  + [SukkaW Speedtest Servers International] 29a310f8327b  DOMAIN,speedtest.brooketel.coop
  + [SukkaW Speedtest Servers International] 2a475faf88d3  DOMAIN,spdtst-southbend.fourway.net
  + [SukkaW Speedtest Servers International] 2b911d71aa37  DOMAIN,speedtest.i3broadband.com
  + [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  + [SukkaW Speedtest Servers International] 3307fbfaba51  DOMAIN,st3.surajnetwork.com
  + [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  + [SukkaW Speedtest Servers International] 358795b67fd5  DOMAIN,speedtest.mornington.ca
  + [SukkaW Speedtest Servers International] 36366555a5b5  DOMAIN,ookla.mu.as6453.net
  + [SukkaW Speedtest Servers International] 37dae1757a6d  DOMAIN,stsaultstemariewireless.rogers.com
  + [SukkaW Speedtest Servers International] 394dff5a7003  DOMAIN,stwindsorwireless.rogers.com
  + [SukkaW Speedtest Servers International] 3ea882635f75  DOMAIN,speed.sdmnet.com.br
  + [SukkaW Speedtest Servers International] 3ed1349b322f  DOMAIN,speedtest.lakelandnetworks.com
  + [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 3f8306542a0b  DOMAIN,stsudburywireless.rogers.com
  + [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  + [SukkaW Speedtest Servers International] 42a36a3fbaf2  DOMAIN,speed.megasyy.com
  + [SukkaW Speedtest Servers International] 43f75ae5aa25  DOMAIN,speedtest.telbo.net
  + [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  + [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  + [SukkaW Speedtest Servers International] 4b2bec89b1bd  DOMAIN,speedtest.vacastelecom.net
  + [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  + [SukkaW Speedtest Servers International] 4de50e12bd16  DOMAIN,speedtest.hay.net
  + [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  + [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  + [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  + [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 5c69bf15997f  DOMAIN,sp1.speedy.bb-swrag.de
  + [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  + [SukkaW Speedtest Servers International] 5cb71d1b2142  DOMAIN,pri-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 5d91b2e1e426  DOMAIN,stgeorgetownwireless.rogers.com
  + [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  + [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  + [SukkaW Speedtest Servers International] 69cac5e64f73  DOMAIN,stbrantfordwireless.rogers.com
  + [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  + [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  + [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  + [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  + [SukkaW Speedtest Servers International] 6e3c74aed01b  DOMAIN,speedtest.mtl.telkel.ca
  + [SukkaW Speedtest Servers International] 71329f904b4a  DOMAIN,stczs.norteultrafibra.com.br
  + [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  + [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  + [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 825eef1b0dd9  DOMAIN,speedtest.hearstconnect.com
  + [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  + [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  + [SukkaW Speedtest Servers International] 8c67eca44a61  DOMAIN,velocidade.tecsattelecom.com.br
  + [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  + [SukkaW Speedtest Servers International] 91f667018cba  DOMAIN,speedtestfe.stel.it
  + [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  + [SukkaW Speedtest Servers International] 96de22a6ddc7  DOMAIN,st-rockford.sumofiber.com
  + [SukkaW Speedtest Servers International] 96e261bbbb9d  DOMAIN,speed.tnahosting.net
  + [SukkaW Speedtest Servers International] 9868c3f8fedf  DOMAIN,speedtest.s3rdv.com
  + [SukkaW Speedtest Servers International] a2002b5b2805  DOMAIN,speedtest.grr1-mi.incx.net
  + [SukkaW Speedtest Servers International] a258e2019d32  DOMAIN,sp1.voyageurinternet.ca
  + [SukkaW Speedtest Servers International] a31c0a6224a2  DOMAIN,storangeville.rogers.com
  + [SukkaW Speedtest Servers International] a5a39e69aa44  DOMAIN,speedtest.mhtc.net
  + [SukkaW Speedtest Servers International] a6619de300c2  DOMAIN,st2a.les.net
  + [SukkaW Speedtest Servers International] accdf3f5dcf1  DOMAIN,stsarniawireless.rogers.com
  + [SukkaW Speedtest Servers International] ad84593408bf  DOMAIN,st2-msn.5nines.com
  + [SukkaW Speedtest Servers International] ae22d7a42288  DOMAIN,speedtest.supranet.net
  + [SukkaW Speedtest Servers International] b03528f13ca1  DOMAIN,speedtest.marshallfibernet.com
  + [SukkaW Speedtest Servers International] b366228f3322  DOMAIN,ststratfordwireless.rogers.com
  + [SukkaW Speedtest Servers International] b7ff9d48bf4d  DOMAIN,ststcatharineswireless.rogers.com
  + [SukkaW Speedtest Servers International] b84a68df407f  DOMAIN,speedtest.gosfieldtel.ca
  + [SukkaW Speedtest Servers International] bdb150f52525  DOMAIN,speedtest2.hurontel.on.ca
  + [SukkaW Speedtest Servers International] be25db6f77aa  DOMAIN,sl-04.wemacom.net
  + [SukkaW Speedtest Servers International] c06caa39a296  DOMAIN,speedtest.lagrangeremcisp.net
  + [SukkaW Speedtest Servers International] c0ba82f0fb9d  DOMAIN,vanspeedtest.altimatel.com
  + [SukkaW Speedtest Servers International] c48494526129  DOMAIN,speedtest3.point-broadband.com
  + [SukkaW Speedtest Servers International] c56b34c86c50  DOMAIN,stwinnipegwireless.rogers.com
  + [SukkaW Speedtest Servers International] c95a22664ae8  DOMAIN,speedtest.kraus.jbarbieri.net
  + [SukkaW Speedtest Servers International] ce3540a348be  DOMAIN,speedtest.geneseo.com
  + [SukkaW Speedtest Servers International] d11b286bd2a4  DOMAIN,de-speedtest.digitalexample.com
  + [SukkaW Speedtest Servers International] d3ff3dfef96e  DOMAIN,stguelphwireless.rogers.com
  + [SukkaW Speedtest Servers International] d46b7ceff48c  DOMAIN,speedtest.host-unlimited.de
  + [SukkaW Speedtest Servers International] d46d3cd6527d  DOMAIN,stwoodstockwireless.rogers.com
  ... and 19 more
```

**Removed: 191** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 010770237191  DOMAIN,stscarborough.rogers.com
  - [SukkaW Speedtest Servers International] 01d06b461e5c  DOMAIN,speedtest.readingsd.org
  - [SukkaW Speedtest Servers International] 02d48045e4e3  DOMAIN,speed12.gonetspeed.com
  - [SukkaW Speedtest Servers International] 03cda3145e17  DOMAIN,t4y-toronto-ca-osts1.ser.tek4you.ca
  - [SukkaW Speedtest Servers International] 05bf0d7776f4  DOMAIN,spdtst.xenyth.net
  - [SukkaW Speedtest Servers International] 09a7a31e8861  DOMAIN,spt1.seed.net.tw
  - [SukkaW Speedtest Servers International] 0a26a7a1d012  DOMAIN,speedtest.zetrikcloud.com
  - [SukkaW Speedtest Servers International] 0df919f8f00e  DOMAIN,speedtest.nrflvaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 0e792152524f  DOMAIN,speedtest-syr.northland.net
  - [SukkaW Speedtest Servers International] 0ef16a17f7b4  DOMAIN,stbowmanville.rogers.com
  - [SukkaW Speedtest Servers International] 0f56643c702c  DOMAIN,stosat-crls-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] 1179f68f6982  DOMAIN,va-speed.magna5.com
  - [SukkaW Speedtest Servers International] 1239ddbeead0  DOMAIN,speed13.gonetspeed.com
  - [SukkaW Speedtest Servers International] 129fa7cf52e5  DOMAIN,speedtest-newjersey.ripplefiber.com
  - [SukkaW Speedtest Servers International] 16744b51f48f  DOMAIN,speedtest-ash.vts.bf
  - [SukkaW Speedtest Servers International] 181f2fd1cbb5  DOMAIN,speedtest.iad.fdcservers.net
  - [SukkaW Speedtest Servers International] 19d98c644b57  DOMAIN,speedtest-iad.sectrify.com
  - [SukkaW Speedtest Servers International] 1b53005476d3  DOMAIN,speedtest.nrbn.ca
  - [SukkaW Speedtest Servers International] 1bc6d1800d19  DOMAIN,fetyl1.seed.net.tw
  - [SukkaW Speedtest Servers International] 1d587f02e00d  DOMAIN,speed.toronto.telmax.ca
  - [SukkaW Speedtest Servers International] 1dd706232871  DOMAIN,speed10.aitspl.in
  - [SukkaW Speedtest Servers International] 1e3705ee2fe6  DOMAIN,speedtest.oceansls.com
  - [SukkaW Speedtest Servers International] 1edb8c41bb13  DOMAIN,speedtest.ca-tr.kamatera.com
  - [SukkaW Speedtest Servers International] 23d5bd5a13bc  DOMAIN,speedtest.gretna.myriverstreet.net
  - [SukkaW Speedtest Servers International] 2492c8ea3e95  DOMAIN,speedtest01.srv.hcvlny.alticeusa.net
  - [SukkaW Speedtest Servers International] 2b19b011f3f3  DOMAIN,speedtest1.innsys.ca
  - [SukkaW Speedtest Servers International] 2edfae58f54e  DOMAIN,speedtest.ca1.colobix.com
  - [SukkaW Speedtest Servers International] 30df7f1427c6  DOMAIN,speedtest.ette.biz
  - [SukkaW Speedtest Servers International] 3263111286ae  DOMAIN,speedtest-zion.fireflyva.com
  - [SukkaW Speedtest Servers International] 32c503790c60  DOMAIN,speedtest3.ptd.net
  - [SukkaW Speedtest Servers International] 33041c0f7fd7  DOMAIN,stbowmanville.netcrawler.ca
  - [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  - [SukkaW Speedtest Servers International] 369df213d503  DOMAIN,nycmetro-speedtest.reliablesite.net
  - [SukkaW Speedtest Servers International] 3a8aec9cda98  DOMAIN,speedtest-zl-1.zoominternet.net
  - [SukkaW Speedtest Servers International] 3d38488c4edb  DOMAIN,falcon.its.utoronto.ca
  - [SukkaW Speedtest Servers International] 3dbdcf661272  DOMAIN,speed06.gonetspeed.com
  - [SukkaW Speedtest Servers International] 3e7bf0bd143d  DOMAIN,speedtest1.ewr.nj.us.planet.net
  - [SukkaW Speedtest Servers International] 414c35bf776f  DOMAIN,speedtest.us.novoserve.com
  - [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  - [SukkaW Speedtest Servers International] 421b127dab27  DOMAIN,speedtest.unlimitedfiber.com
  - [SukkaW Speedtest Servers International] 42be4c6f36e1  DOMAIN,speedtest-buffalo.greenlightnetworks.com
  - [SukkaW Speedtest Servers International] 42db00569c58  DOMAIN,speedtest.getwireless.net
  - [SukkaW Speedtest Servers International] 44e1fd099c78  DOMAIN,speedtest.sc1.loopinternet.com
  - [SukkaW Speedtest Servers International] 4502550a3a9c  DOMAIN,wpa-speed.magna5.com
  - [SukkaW Speedtest Servers International] 4571f1abe520  DOMAIN,speedtestmacapa.webflash.net.br
  - [SukkaW Speedtest Servers International] 459c21e05348  DOMAIN,nycny-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 45f4d00908d6  DOMAIN,speedtest-2.hynetwifi.it
  - [SukkaW Speedtest Servers International] 473f9b45897a  DOMAIN,speedtest.winchesterwireless.com
  - [SukkaW Speedtest Servers International] 49f2fe815df7  DOMAIN,speed.markham.telmax.ca
  - [SukkaW Speedtest Servers International] 49ffc4a2950e  DOMAIN,stoshawa.netcrawler.ca
  - [SukkaW Speedtest Servers International] 4ea2234b848a  DOMAIN,speedtest.aattizen.net
  - [SukkaW Speedtest Servers International] 4f8818240273  DOMAIN,stosat-plfi-08p.sys.comcast.net
  - [SukkaW Speedtest Servers International] 504311aa0547  DOMAIN,speedtest.massivemesh.com
  - [SukkaW Speedtest Servers International] 5078d86d990d  DOMAIN,speedtest-ad-1.zoominternet.net
  - [SukkaW Speedtest Servers International] 5193c8145d68  DOMAIN,crls-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 51cd85bbddab  DOMAIN,speedtest.fra.plusnet.de
  - [SukkaW Speedtest Servers International] 52a89dbdad82  DOMAIN,speedtest.us-ny2.kamatera.com
  - [SukkaW Speedtest Servers International] 52ea711702a9  DOMAIN,speedtestnorthpointe.arkdnacloud.com
  - [SukkaW Speedtest Servers International] 533727d6d031  DOMAIN,speedtest-utc.northland.net
  - [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  - [SukkaW Speedtest Servers International] 5559912850cd  DOMAIN,speedtest.belmontcountygig.com
  - [SukkaW Speedtest Servers International] 55c0cb8dcbb9  DOMAIN,speedtest2.pa.mycci.net
  - [SukkaW Speedtest Servers International] 57cfe7333ea8  DOMAIN,fast.blackbearfiber.com
  - [SukkaW Speedtest Servers International] 5893bd721aca  DOMAIN,stnorthyork.netcrawler.ca
  - [SukkaW Speedtest Servers International] 589d7eeccf53  DOMAIN,ookla.mtt.as6453.net
  - [SukkaW Speedtest Servers International] 590ef6087499  DOMAIN,nyc1-speedtest.webnx.com
  - [SukkaW Speedtest Servers International] 592a7dd8f5c9  DOMAIN,speedtest.xcdtelecom.com
  - [SukkaW Speedtest Servers International] 59b3f6172efc  DOMAIN,spt-jfk1.edgeuno.com
  - [SukkaW Speedtest Servers International] 5a8191463e31  DOMAIN,stmississauga.netcrawler.ca
  - [SukkaW Speedtest Servers International] 5ab2e37aaffc  DOMAIN,speedtest31.suddenlink.net
  - [SukkaW Speedtest Servers International] 5c48edeaf786  DOMAIN,sttoronto.rogers.com
  - [SukkaW Speedtest Servers International] 5c82f672493f  DOMAIN,netspeed.empireaccess.com
  - [SukkaW Speedtest Servers International] 5de72a66d994  DOMAIN,speedtest.sercomm.com
  - [SukkaW Speedtest Servers International] 60ac93c18792  DOMAIN,stscarborough.netcrawler.ca
  - [SukkaW Speedtest Servers International] 614fc5f34997  DOMAIN,speed.haefeleconnect.com
  - [SukkaW Speedtest Servers International] 615ab422b360  DOMAIN,btlr-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 622740dd56c6  DOMAIN,stmontreal.netcrawler.ca
  - [SukkaW Speedtest Servers International] 6240dc262b53  DOMAIN,speedtest1.whsdk12.net
  - [SukkaW Speedtest Servers International] 625966c841d3  DOMAIN,speedtest1.ric1.va.hostedbackbone.net
  - [SukkaW Speedtest Servers International] 63065aa229b2  DOMAIN,speedtest03.srv.whplny.alticeusa.net
  - [SukkaW Speedtest Servers International] 6450ad79b27e  DOMAIN,speedtest5.fybercom.net
  - [SukkaW Speedtest Servers International] 6722a4f62ff8  DOMAIN,stbowmanvillewireless.rogers.com
  - [SukkaW Speedtest Servers International] 67382fe7fa61  DOMAIN,stoshawa.rogers.com
  - [SukkaW Speedtest Servers International] 67fb222e7169  DOMAIN,stbrampton.rogers.com
  - [SukkaW Speedtest Servers International] 6846a38f9372  DOMAIN,speedtest.asbn.va.wtsky.net
  - [SukkaW Speedtest Servers International] 68c6eb173f83  DOMAIN,asbn-speedtest.northstate.net
  - [SukkaW Speedtest Servers International] 698bcfb1bb21  DOMAIN,speedtest-preston-wv.prodigiwv.net
  - [SukkaW Speedtest Servers International] 6aafcc1f0064  DOMAIN,speedtest.americatelecom.net.br
  - [SukkaW Speedtest Servers International] 6b8f1c9f7c44  DOMAIN,stajax.rogers.com
  - [SukkaW Speedtest Servers International] 6bd15d569f45  DOMAIN,velocidade.csrnetwork.com.br
  - [SukkaW Speedtest Servers International] 6ed781ee2831  DOMAIN,tor-speedtest.net.sangoma.net
  - [SukkaW Speedtest Servers International] 6ef5f28df61c  DOMAIN,ookla.aeq.as6453.net
  - [SukkaW Speedtest Servers International] 73ae62b70286  DOMAIN,seednet-tc1.seed.net.tw
  - [SukkaW Speedtest Servers International] 74a6d6e46908  DOMAIN,speedtest.wb1.loopinternet.com
  - [SukkaW Speedtest Servers International] 754c25a0d2ab  DOMAIN,tdc01-speedtest.whipcord.com
  - [SukkaW Speedtest Servers International] 75e802499b21  DOMAIN,stbrampton.netcrawler.ca
  - [SukkaW Speedtest Servers International] 7625db817368  DOMAIN,speedtest1.iad1-us.gozfly.net
  - [SukkaW Speedtest Servers International] 77cb389996a6  DOMAIN,speedtest-bethlehem.greenlightnetworks.com
  - [SukkaW Speedtest Servers International] 77e56dc99c59  DOMAIN,cltn-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 7c4e62477d2e  DOMAIN,speedtest.zoominternet.net
  ... and 91 more
```
