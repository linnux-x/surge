# Surge Rule Diff Report
Generated: 2026-09-23T05:03:54.650732

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 131 |
| Rules removed | 134 |
| Source attribution changed | 2 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 111137 | 111146 | +10 | -1 | ~1 |
| China_IP.list | 11508 | 11509 | +1 | -0 | ~0 |
| Global.list | 24339 | 24344 | +5 | -0 | ~0 |
| Speedtest.list | 1711 | 1693 | +115 | -133 | ~0 |
| Speedtest_China.list | 53 | 53 | +0 | -0 | ~1 |

## China.list

**Added: 10** (showing first 10)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 1fa4cbfd48cd  DOMAIN-SUFFIX,youbianku.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 2c89ea3f960c  DOMAIN-SUFFIX,qudian.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 359dd456ae93  DOMAIN-SUFFIX,vxhcm.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 3f911024f817  DOMAIN-SUFFIX,zhongliujie.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 5e2ca10b5cb1  DOMAIN-SUFFIX,mddclass.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 605261501f0b  DOMAIN-SUFFIX,gongniukaiguan.net
  + [blackmatrix7 ChinaMaxNoIP Domain] 94de73922516  DOMAIN-SUFFIX,zuiyou.tv
  + [blackmatrix7 ChinaMaxNoIP Domain] a2230f628c05  DOMAIN-SUFFIX,uboxs.com
  + [blackmatrix7 ChinaMaxNoIP Domain] dae5c108b236  DOMAIN-SUFFIX,fnrrc.com
  + [SukkaW Domestic] f6ac42ebd3c6  DOMAIN-WILDCARD,qhimgs?.com
```

**Removed: 1** (showing first 1)
```
  - [SukkaW Domestic] 964786a7afb4  DOMAIN-WILDCARD,*.qhimgs?.com
```

**Source changed: 1**
```
  ~ 9cb2567c6ecd: [blackmatrix7 ChinaMaxNoIP Domain → SukkaW Domestic]
```

## China_IP.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 China IPs] 33e36774643b  IP-CIDR,64.96.5.0/24
```

## Global.list

**Added: 5** (showing first 5)
```
  + [blackmatrix7 Global] 21cb89f624a9  DOMAIN-SUFFIX,firefox-portal-detection.com
  + [blackmatrix7 Global] 36abe13ac548  DOMAIN-SUFFIX,codebuff.com
  + [blackmatrix7 Global] bb09f352fcf6  DOMAIN-SUFFIX,tfbnw.net
  + [blackmatrix7 Global] c6b2a2b1607e  DOMAIN-SUFFIX,firebase.dev
  + [blackmatrix7 Global] dec9de69bdad  DOMAIN-SUFFIX,freebuff.com
```

## Speedtest.list

**Added: 115** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 0009d45cc71f  DOMAIN,speedtest-gdrp.merit.edu
  + [SukkaW Speedtest Servers International] 012b7f31586b  DOMAIN,ststratford.rogers.com
  + [SukkaW Speedtest Servers International] 0561b044089c  DOMAIN,ran-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 0711f9d6046b  DOMAIN,cbpuspeed.aspensmart.net
  + [SukkaW Speedtest Servers International] 0ab0cf8a6ab9  DOMAIN,speedtest.novateldigital.com
  + [SukkaW Speedtest Servers International] 0bd6b487bcf7  DOMAIN,speedtest.inovewifi.com.br
  + [SukkaW Speedtest Servers International] 0f0435a45fac  DOMAIN,speedtest.oa.net
  + [SukkaW Speedtest Servers International] 0f923e75457a  DOMAIN,ookla-in.mercuryfiber.com
  + [SukkaW Speedtest Servers International] 0f9fc6befe00  DOMAIN,speed.idnet.net.br
  + [SukkaW Speedtest Servers International] 1204ab7c7137  DOMAIN,40gspeedtest.mnsi.net
  + [SukkaW Speedtest Servers International] 134564537572  DOMAIN,speedtest.sycmilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 15ee8e1a505a  DOMAIN,speedtest.volo.net
  + [SukkaW Speedtest Servers International] 1753c7265a8d  DOMAIN,st1.ligtel.com
  + [SukkaW Speedtest Servers International] 1debbecee8c5  DOMAIN,speedtest.cstech.com
  + [SukkaW Speedtest Servers International] 22e17aa36c22  DOMAIN,speedtest-wc.truestreamfiber.us
  + [SukkaW Speedtest Servers International] 27aa9cef1e30  DOMAIN,bytp-speedtest-1.123.net
  + [SukkaW Speedtest Servers International] 29a310f8327b  DOMAIN,speedtest.brooketel.coop
  + [SukkaW Speedtest Servers International] 2a475faf88d3  DOMAIN,spdtst-southbend.fourway.net
  + [SukkaW Speedtest Servers International] 2a68dd8ff300  DOMAIN,spd-pub-mi-01-01.fastwebnet.it
  + [SukkaW Speedtest Servers International] 2b911d71aa37  DOMAIN,speedtest.i3broadband.com
  + [SukkaW Speedtest Servers International] 2f2ddb2266d4  DOMAIN,speedtest.anksoft.net
  + [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  + [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  + [SukkaW Speedtest Servers International] 358795b67fd5  DOMAIN,speedtest.mornington.ca
  + [SukkaW Speedtest Servers International] 358f08550b7a  DOMAIN,spd-pub-rm-01-01.fastwebnet.it
  + [SukkaW Speedtest Servers International] 37dae1757a6d  DOMAIN,stsaultstemariewireless.rogers.com
  + [SukkaW Speedtest Servers International] 394dff5a7003  DOMAIN,stwindsorwireless.rogers.com
  + [SukkaW Speedtest Servers International] 3cf83babff85  DOMAIN,ber.wsqm.telekom-dienste.de
  + [SukkaW Speedtest Servers International] 3e7fd288e9dc  DOMAIN,ookla.pgservicos.net.br
  + [SukkaW Speedtest Servers International] 3ea882635f75  DOMAIN,speed.sdmnet.com.br
  + [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  + [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  + [SukkaW Speedtest Servers International] 45f4d00908d6  DOMAIN,speedtest-2.hynetwifi.it
  + [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  + [SukkaW Speedtest Servers International] 4b2bec89b1bd  DOMAIN,speedtest.vacastelecom.net
  + [SukkaW Speedtest Servers International] 4ba664914d15  DOMAIN,speedtest.tinp.net.tw
  + [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  + [SukkaW Speedtest Servers International] 4de50e12bd16  DOMAIN,speedtest.hay.net
  + [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 4fa503514189  DOMAIN,speedtest.packetworks.net
  + [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  + [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 58853cdc4bf0  DOMAIN,speedtest.thryve.com.au
  + [SukkaW Speedtest Servers International] 5c69bf15997f  DOMAIN,sp1.speedy.bb-swrag.de
  + [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  + [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  + [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  + [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  + [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  + [SukkaW Speedtest Servers International] 67fb222e7169  DOMAIN,stbrampton.rogers.com
  + [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  + [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  + [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  + [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  + [SukkaW Speedtest Servers International] 71329f904b4a  DOMAIN,stczs.norteultrafibra.com.br
  + [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  + [SukkaW Speedtest Servers International] 75e802499b21  DOMAIN,stbrampton.netcrawler.ca
  + [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  + [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  + [SukkaW Speedtest Servers International] 879002fbb65d  DOMAIN,yyz-speedtest.xplore.ca
  + [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  + [SukkaW Speedtest Servers International] 8c67eca44a61  DOMAIN,velocidade.tecsattelecom.com.br
  + [SukkaW Speedtest Servers International] 8c8abdf2d7dc  DOMAIN,speed.weendeavor.com
  + [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  + [SukkaW Speedtest Servers International] 8fda1d8fef4c  DOMAIN,lmb1-ookla.perf.fastedge.it
  + [SukkaW Speedtest Servers International] 905125f73ee5  DOMAIN,speedtest.mvec.com
  + [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  + [SukkaW Speedtest Servers International] 96de22a6ddc7  DOMAIN,st-rockford.sumofiber.com
  + [SukkaW Speedtest Servers International] 96e261bbbb9d  DOMAIN,speed.tnahosting.net
  + [SukkaW Speedtest Servers International] 9868c3f8fedf  DOMAIN,speedtest.s3rdv.com
  + [SukkaW Speedtest Servers International] 9d2342e15aaa  DOMAIN,stkingcity.netcrawler.ca
  + [SukkaW Speedtest Servers International] a2002b5b2805  DOMAIN,speedtest.grr1-mi.incx.net
  + [SukkaW Speedtest Servers International] a31c0a6224a2  DOMAIN,storangeville.rogers.com
  + [SukkaW Speedtest Servers International] a5a39e69aa44  DOMAIN,speedtest.mhtc.net
  + [SukkaW Speedtest Servers International] a62caff2b1f9  DOMAIN,speedtest-mel0.encoo.com.au
  + [SukkaW Speedtest Servers International] a91aa2354179  DOMAIN,fibertest.soipl.co.in
  + [SukkaW Speedtest Servers International] accdf3f5dcf1  DOMAIN,stsarniawireless.rogers.com
  + [SukkaW Speedtest Servers International] ad84593408bf  DOMAIN,st2-msn.5nines.com
  + [SukkaW Speedtest Servers International] ae22d7a42288  DOMAIN,speedtest.supranet.net
  + [SukkaW Speedtest Servers International] b03528f13ca1  DOMAIN,speedtest.marshallfibernet.com
  + [SukkaW Speedtest Servers International] b366228f3322  DOMAIN,ststratfordwireless.rogers.com
  + [SukkaW Speedtest Servers International] b43cd8b37520  DOMAIN,speedtest01.ehtel.ca
  + [SukkaW Speedtest Servers International] b84a68df407f  DOMAIN,speedtest.gosfieldtel.ca
  + [SukkaW Speedtest Servers International] bdb150f52525  DOMAIN,speedtest2.hurontel.on.ca
  + [SukkaW Speedtest Servers International] be25db6f77aa  DOMAIN,sl-04.wemacom.net
  + [SukkaW Speedtest Servers International] c06caa39a296  DOMAIN,speedtest.lagrangeremcisp.net
  + [SukkaW Speedtest Servers International] c48494526129  DOMAIN,speedtest3.point-broadband.com
  + [SukkaW Speedtest Servers International] c95a22664ae8  DOMAIN,speedtest.kraus.jbarbieri.net
  + [SukkaW Speedtest Servers International] ce3540a348be  DOMAIN,speedtest.geneseo.com
  + [SukkaW Speedtest Servers International] d0b106fcb347  DOMAIN,speedtest2.il.mycci.net
  + [SukkaW Speedtest Servers International] d11b286bd2a4  DOMAIN,de-speedtest.digitalexample.com
  + [SukkaW Speedtest Servers International] d1b50484694b  DOMAIN,uc-speed.kbro.com.tw
  + [SukkaW Speedtest Servers International] d43014812cdf  DOMAIN,speedtest.systemlifeline.com
  + [SukkaW Speedtest Servers International] d46b7ceff48c  DOMAIN,speedtest.host-unlimited.de
  + [SukkaW Speedtest Servers International] d77254c621cc  DOMAIN,speedtest3.myninestar.net
  + [SukkaW Speedtest Servers International] d89ef3067d92  DOMAIN,storangevillewireless.rogers.com
  + [SukkaW Speedtest Servers International] da8f08a15e16  DOMAIN,speedtest.fbc-tele.com
  ... and 15 more
```

**Removed: 133** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 010770237191  DOMAIN,stscarborough.rogers.com
  - [SukkaW Speedtest Servers International] 01d06b461e5c  DOMAIN,speedtest.readingsd.org
  - [SukkaW Speedtest Servers International] 0694bb696659  DOMAIN,speedtest005.telecomitalia.it
  - [SukkaW Speedtest Servers International] 0df919f8f00e  DOMAIN,speedtest.nrflvaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 0ef16a17f7b4  DOMAIN,stbowmanville.rogers.com
  - [SukkaW Speedtest Servers International] 0f56643c702c  DOMAIN,stosat-crls-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] 1179f68f6982  DOMAIN,va-speed.magna5.com
  - [SukkaW Speedtest Servers International] 1239ddbeead0  DOMAIN,speed13.gonetspeed.com
  - [SukkaW Speedtest Servers International] 129fa7cf52e5  DOMAIN,speedtest-newjersey.ripplefiber.com
  - [SukkaW Speedtest Servers International] 147ba9dcee0e  DOMAIN,mtcspeedtest.catskill.net
  - [SukkaW Speedtest Servers International] 16744b51f48f  DOMAIN,speedtest-ash.vts.bf
  - [SukkaW Speedtest Servers International] 181f2fd1cbb5  DOMAIN,speedtest.iad.fdcservers.net
  - [SukkaW Speedtest Servers International] 19d98c644b57  DOMAIN,speedtest-iad.sectrify.com
  - [SukkaW Speedtest Servers International] 1b53005476d3  DOMAIN,speedtest.nrbn.ca
  - [SukkaW Speedtest Servers International] 1bd6834185f4  DOMAIN,speedtest-stm.redeconecta.com
  - [SukkaW Speedtest Servers International] 1dd706232871  DOMAIN,speed10.aitspl.in
  - [SukkaW Speedtest Servers International] 1e3705ee2fe6  DOMAIN,speedtest.oceansls.com
  - [SukkaW Speedtest Servers International] 23d5bd5a13bc  DOMAIN,speedtest.gretna.myriverstreet.net
  - [SukkaW Speedtest Servers International] 30df7f1427c6  DOMAIN,speedtest.ette.biz
  - [SukkaW Speedtest Servers International] 31b44124210f  DOMAIN,stosat-smil-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] 3263111286ae  DOMAIN,speedtest-zion.fireflyva.com
  - [SukkaW Speedtest Servers International] 32c503790c60  DOMAIN,speedtest3.ptd.net
  - [SukkaW Speedtest Servers International] 33041c0f7fd7  DOMAIN,stbowmanville.netcrawler.ca
  - [SukkaW Speedtest Servers International] 367595cbeedc  DOMAIN,velocimetrostm.interlig.net
  - [SukkaW Speedtest Servers International] 369df213d503  DOMAIN,nycmetro-speedtest.reliablesite.net
  - [SukkaW Speedtest Servers International] 3a8aec9cda98  DOMAIN,speedtest-zl-1.zoominternet.net
  - [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  - [SukkaW Speedtest Servers International] 3e7bf0bd143d  DOMAIN,speedtest1.ewr.nj.us.planet.net
  - [SukkaW Speedtest Servers International] 414c35bf776f  DOMAIN,speedtest.us.novoserve.com
  - [SukkaW Speedtest Servers International] 42db00569c58  DOMAIN,speedtest.getwireless.net
  - [SukkaW Speedtest Servers International] 44e1fd099c78  DOMAIN,speedtest.sc1.loopinternet.com
  - [SukkaW Speedtest Servers International] 4502550a3a9c  DOMAIN,wpa-speed.magna5.com
  - [SukkaW Speedtest Servers International] 473f9b45897a  DOMAIN,speedtest.winchesterwireless.com
  - [SukkaW Speedtest Servers International] 49ffc4a2950e  DOMAIN,stoshawa.netcrawler.ca
  - [SukkaW Speedtest Servers International] 4f8818240273  DOMAIN,stosat-plfi-08p.sys.comcast.net
  - [SukkaW Speedtest Servers International] 5193c8145d68  DOMAIN,crls-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 52a89dbdad82  DOMAIN,speedtest.us-ny2.kamatera.com
  - [SukkaW Speedtest Servers International] 52ea711702a9  DOMAIN,speedtestnorthpointe.arkdnacloud.com
  - [SukkaW Speedtest Servers International] 5559912850cd  DOMAIN,speedtest.belmontcountygig.com
  - [SukkaW Speedtest Servers International] 55c0cb8dcbb9  DOMAIN,speedtest2.pa.mycci.net
  - [SukkaW Speedtest Servers International] 57cfe7333ea8  DOMAIN,fast.blackbearfiber.com
  - [SukkaW Speedtest Servers International] 5893bd721aca  DOMAIN,stnorthyork.netcrawler.ca
  - [SukkaW Speedtest Servers International] 5942f53f5374  DOMAIN,velocidadestm.amazonett.com.br
  - [SukkaW Speedtest Servers International] 5ab2e37aaffc  DOMAIN,speedtest31.suddenlink.net
  - [SukkaW Speedtest Servers International] 5b59c5167680  DOMAIN,sqaookla.ddns.net
  - [SukkaW Speedtest Servers International] 60ac93c18792  DOMAIN,stscarborough.netcrawler.ca
  - [SukkaW Speedtest Servers International] 615ab422b360  DOMAIN,btlr-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 6240dc262b53  DOMAIN,speedtest1.whsdk12.net
  - [SukkaW Speedtest Servers International] 625966c841d3  DOMAIN,speedtest1.ric1.va.hostedbackbone.net
  - [SukkaW Speedtest Servers International] 6722a4f62ff8  DOMAIN,stbowmanvillewireless.rogers.com
  - [SukkaW Speedtest Servers International] 67382fe7fa61  DOMAIN,stoshawa.rogers.com
  - [SukkaW Speedtest Servers International] 680ff27e9506  DOMAIN,redeultramf.net.br
  - [SukkaW Speedtest Servers International] 6846a38f9372  DOMAIN,speedtest.asbn.va.wtsky.net
  - [SukkaW Speedtest Servers International] 68c6eb173f83  DOMAIN,asbn-speedtest.northstate.net
  - [SukkaW Speedtest Servers International] 698bcfb1bb21  DOMAIN,speedtest-preston-wv.prodigiwv.net
  - [SukkaW Speedtest Servers International] 6b8f1c9f7c44  DOMAIN,stajax.rogers.com
  - [SukkaW Speedtest Servers International] 6ca65a0b3161  DOMAIN,speedtest.pcibroadband.in
  - [SukkaW Speedtest Servers International] 6ef5f28df61c  DOMAIN,ookla.aeq.as6453.net
  - [SukkaW Speedtest Servers International] 71121272f40a  DOMAIN,stceuti1.borecom.com
  - [SukkaW Speedtest Servers International] 74a6d6e46908  DOMAIN,speedtest.wb1.loopinternet.com
  - [SukkaW Speedtest Servers International] 7625db817368  DOMAIN,speedtest1.iad1-us.gozfly.net
  - [SukkaW Speedtest Servers International] 77cb389996a6  DOMAIN,speedtest-bethlehem.greenlightnetworks.com
  - [SukkaW Speedtest Servers International] 77e56dc99c59  DOMAIN,cltn-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 7c4e62477d2e  DOMAIN,speedtest.zoominternet.net
  - [SukkaW Speedtest Servers International] 7de305557319  DOMAIN,altoonaspeedtest.crowsnestbb.net
  - [SukkaW Speedtest Servers International] 8141004af16b  DOMAIN,speedtest02.srv.prnynj.alticeusa.net
  - [SukkaW Speedtest Servers International] 81fca2acd321  DOMAIN,speedtest.skyplay.app
  - [SukkaW Speedtest Servers International] 83d43cf9e206  DOMAIN,spd01-adl.au.superloop.com
  - [SukkaW Speedtest Servers International] 83e830bbc65c  DOMAIN,speedtest4.point-broadband.com
  - [SukkaW Speedtest Servers International] 8487be6e6d95  DOMAIN,speedtest.mifflincountywireless.com
  - [SukkaW Speedtest Servers International] 8632dbc95ac0  DOMAIN,stnorthyorkwireless.rogers.com
  - [SukkaW Speedtest Servers International] 894527aa356c  DOMAIN,lsdspeed01.lsdops.net
  - [SukkaW Speedtest Servers International] 8fb9855a4808  DOMAIN,reikonteste.reikoninternet.com.br
  - [SukkaW Speedtest Servers International] 8fd05fb4ff7e  DOMAIN,speedtest19.suddenlink.net
  - [SukkaW Speedtest Servers International] 90617691e3af  DOMAIN,stwhitby.netcrawler.ca
  - [SukkaW Speedtest Servers International] 910cf0769104  DOMAIN,speedtest-nwrk-nj.wtsky.net
  - [SukkaW Speedtest Servers International] 9138c74c88d2  DOMAIN,vaspeedtest.rackdog.com
  - [SukkaW Speedtest Servers International] 9660747a5a08  DOMAIN,speed01.gonetspeed.com
  - [SukkaW Speedtest Servers International] 96e24c3aaac2  DOMAIN,stoshawawireless.rogers.com
  - [SukkaW Speedtest Servers International] 995889b17f13  DOMAIN,lsdspeed02.lsdops.net
  - [SukkaW Speedtest Servers International] 9b36e6ace41e  DOMAIN,phlph0001speedtestserver02.wiline.com
  - [SukkaW Speedtest Servers International] 9c36ab36b132  DOMAIN,phl01.screenshot.download
  - [SukkaW Speedtest Servers International] 9d56ad0a505c  DOMAIN,speedtest.dme.fdcservers.net
  - [SukkaW Speedtest Servers International] 9ee8a1734e62  DOMAIN,speedtest2.sistelfibra.es
  - [SukkaW Speedtest Servers International] 9ef50333ec52  DOMAIN,speedtestmoh1.airtelbroadband.in
  - [SukkaW Speedtest Servers International] 9f094a91d810  DOMAIN,ookla.micrologicwv.com
  - [SukkaW Speedtest Servers International] 9f6b30de3d0b  DOMAIN,speedtest-server-ash.starry.com
  - [SukkaW Speedtest Servers International] a933b6c67760  DOMAIN,speedtest.wsp.net.br
  - [SukkaW Speedtest Servers International] ad7927355047  DOMAIN,speedtest-lon1.elite.net.uk
  - [SukkaW Speedtest Servers International] b053213fa908  DOMAIN,speedtest4.lepida.it
  - [SukkaW Speedtest Servers International] b06e6a3b7c0f  DOMAIN,speedtest.philasd.org
  - [SukkaW Speedtest Servers International] b0cc745d6216  DOMAIN,stosat-balt-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] b4f4faf0a782  DOMAIN,speedtest.fiberlync.net
  - [SukkaW Speedtest Servers International] b577445ffd28  DOMAIN,ookla-mgw.wvnet.edu
  - [SukkaW Speedtest Servers International] b7070e1bfc5d  DOMAIN,speedtest.internetsubway.com
  - [SukkaW Speedtest Servers International] b7ea0351589f  DOMAIN,speedtest.revolutionbroadband.net
  - [SukkaW Speedtest Servers International] b7ff9d48bf4d  DOMAIN,ststcatharineswireless.rogers.com
  - [SukkaW Speedtest Servers International] b8002d9cf7f6  DOMAIN,ookla1.talkiefiber.com
  - [SukkaW Speedtest Servers International] b868fcdc5518  DOMAIN,ookla01.citynet.net
  - [SukkaW Speedtest Servers International] be5af7e0a364  DOMAIN,stpickering.netcrawler.ca
  ... and 33 more
```

## Speedtest_China.list

**Source changed: 1**
```
  ~ 6184144f6695: [spiritLHLS Speedtest.cn China → SukkaW Speedtest Servers China]
```
