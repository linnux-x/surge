# Surge Rule Diff Report
Generated: 2026-10-15T05:31:39.621533

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 138 |
| Rules removed | 930 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 125 | 123 | +5 | -7 | ~1 |
| China.list | 111711 | 110938 | +10 | -783 | ~0 |
| Download.list | 1695 | 1696 | +1 | -0 | ~0 |
| Global.list | 24479 | 24480 | +1 | -0 | ~0 |
| Speedtest.list | 1702 | 1683 | +121 | -140 | ~0 |

## AI.list

**Added: 5** (showing first 5)
```
  + [Rabbit-Spec AIGC] 1e902f6f0f29  DOMAIN-SUFFIX,guzzoni.apple.com
  + [Rabbit-Spec AIGC] 23d8a46c106a  DOMAIN-SUFFIX,apple-relay.fastly-edge.com
  + [Rabbit-Spec AIGC] b6557a0d4b7b  DOMAIN-SUFFIX,apis.google.com
  + [Rabbit-Spec AIGC] c3b7ae332522  DOMAIN-SUFFIX,gspe1-ssl.ls.apple.com
  + [Rabbit-Spec AIGC] eb9c099dc8eb  DOMAIN-SUFFIX,cp4.cloudflare.com
```

**Removed: 7** (showing first 7)
```
  - [Rabbit-Spec AIGC] 24c4c865cd81  DOMAIN-SUFFIX,featureassets.org
  - [Rabbit-Spec AIGC] 5767d6cf048c  IP-CIDR6,2607:6BC0::/32,no-resolve
  - [Rabbit-Spec AIGC] 634e92c7b9c0  IP-CIDR,160.79.104.0/21,no-resolve
  - [ConnersHua AI] 6e9128c725fe  DOMAIN,cp4.cloudflare.com
  - [Rabbit-Spec AIGC] 7da74b7ef7be  IP-ASN,399358,no-resolve
  - [Rabbit-Spec AIGC] a620b2872683  DOMAIN-SUFFIX,ct.sendgrid.net
  - [Rabbit-Spec AIGC] fc9bbc2a1f72  DOMAIN-SUFFIX,prodregistryv2.org
```

**Source changed: 1**
```
  ~ 9d0ff2f30280: [Rabbit-Spec AIGC → ConnersHua AI]
```

## China.list

**Added: 10** (showing first 10)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 3c8df0f72dac  DOMAIN-SUFFIX,pcelves.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 4c330c986237  DOMAIN,api.blipsandchitz.me
  + [blackmatrix7 ChinaMaxNoIP Domain] 55a53ba7b57d  DOMAIN-SUFFIX,aibilun.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 65dbc6a1f9a9  DOMAIN-SUFFIX,lewl88.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 781071e21088  DOMAIN-SUFFIX,cfdns46.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 838dce609761  DOMAIN-SUFFIX,alizch.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 957e0ae415fc  DOMAIN-SUFFIX,qlgfdns.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 9d2475088f25  DOMAIN-SUFFIX,dnski.com
  + [blackmatrix7 ChinaMaxNoIP Domain] c599e70a73cf  DOMAIN-SUFFIX,workbuddy.ai
  + [blackmatrix7 ChinaMaxNoIP Domain] e20b6de1ef59  DOMAIN-SUFFIX,codebuddy.ai
```

**Removed: 783** (showing first 100)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 0043f766b3b9  DOMAIN-SUFFIX,9898jh2.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 01308b1f881a  DOMAIN-SUFFIX,44481.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 015d13128fd4  DOMAIN-SUFFIX,5e17fc2cca2967e2.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0171e67ff457  DOMAIN-SUFFIX,fc3e2b88fc5254c9.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 018c8d13692c  DOMAIN-SUFFIX,jiweichengzhu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 01be8dda8f93  DOMAIN-SUFFIX,ctvrd.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 022fcdcda430  DOMAIN-SUFFIX,baijiudl.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0236f471e8ed  DOMAIN-SUFFIX,4pf6hb.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 023d53d51fdd  DOMAIN-SUFFIX,9iwz.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 0266ff12ba59  DOMAIN-SUFFIX,78104.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 029319438998  DOMAIN-SUFFIX,tuchuangs.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 02b4400f8bb4  DOMAIN-SUFFIX,62ca01745cf46371.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 02dbe7e8a401  DOMAIN-SUFFIX,china-cloud.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0333b5e067b5  DOMAIN-SUFFIX,xueche.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 038be2502548  DOMAIN-SUFFIX,jm2046.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 03d386452b4f  DOMAIN-SUFFIX,jinfan-keji.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 03dc27510cc0  DOMAIN-SUFFIX,youlianghz.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0461b0e48b08  DOMAIN-SUFFIX,hnsyhj.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 04d524bfd7fe  DOMAIN-SUFFIX,rcbc888.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 04d7a848bb2c  DOMAIN-SUFFIX,yinguobing.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 05b59442bd80  DOMAIN-SUFFIX,chuanshanjia.work
  - [blackmatrix7 ChinaMaxNoIP Domain] 05f09152c688  DOMAIN-SUFFIX,4hpy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 06244b2e93ff  DOMAIN-SUFFIX,zhongguoditu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 062a1b16689b  DOMAIN-SUFFIX,ootu.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] 06ac2ad25d02  DOMAIN-SUFFIX,27512.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 06bc293fe203  DOMAIN-SUFFIX,ebfb8c1c2f714608.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 07043bc014ab  DOMAIN-SUFFIX,bbecpsc.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 073e73aa5dd4  DOMAIN-SUFFIX,acdnrvh.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0762fe8b72e8  DOMAIN-SUFFIX,jsz.asia
  - [blackmatrix7 ChinaMaxNoIP Domain] 07677b770b8c  DOMAIN-SUFFIX,frgsupps.store
  - [blackmatrix7 ChinaMaxNoIP Domain] 080f0522fe5b  DOMAIN-SUFFIX,nxlayer2.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 08e578eb765c  DOMAIN-SUFFIX,jszyyguoji.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 09437d7c830c  DOMAIN-SUFFIX,eltmall.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 099441cde008  DOMAIN-SUFFIX,4546.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 09b2b984c6ca  DOMAIN-SUFFIX,cosedm.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 09e287d99bda  DOMAIN-SUFFIX,078bdd796e8b4b12.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0a2b1aca0c4e  DOMAIN-SUFFIX,080e068141ea500e.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0a3751e3ca5f  DOMAIN-SUFFIX,babaimi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0a4280d5a247  DOMAIN-SUFFIX,5dc0af35081be08e.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0a9c064da71b  DOMAIN-SUFFIX,cc7m.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0aae0cbd20fe  DOMAIN-SUFFIX,58416.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 0b3e6210dbcb  DOMAIN-SUFFIX,50915.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 0bb867391e20  DOMAIN-SUFFIX,76831.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 0bcb00937826  DOMAIN-SUFFIX,wlnkaep.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 0bd9b79a41ea  DOMAIN-SUFFIX,9942.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 0c6aecd7ee24  DOMAIN-SUFFIX,98945.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 0c82fb25b33f  DOMAIN-SUFFIX,gbhome.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0ce5e06f39b9  DOMAIN-SUFFIX,tengchu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0ceb72e24f83  DOMAIN-SUFFIX,gdcsgj.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0d548146495d  DOMAIN-SUFFIX,xzuan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0e4e80bcac36  DOMAIN-SUFFIX,8866316apt.work
  - [blackmatrix7 ChinaMaxNoIP Domain] 0e5858832f27  DOMAIN-SUFFIX,8475.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 0ee1f77a9a66  DOMAIN-SUFFIX,owulia.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0efc82eb8147  DOMAIN-SUFFIX,58142404237055.icu
  - [blackmatrix7 ChinaMaxNoIP Domain] 0f474650a403  DOMAIN-SUFFIX,cineplexsn.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 107c3aa8f3a2  DOMAIN-SUFFIX,56ad2ddadaebfb59.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1116fb9020a9  DOMAIN-SUFFIX,3f9b37df0629ada1.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 11b0d4939f40  DOMAIN-SUFFIX,023zp.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 11bc16920f19  DOMAIN-SUFFIX,f8e772f41348c086.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 124543f307da  DOMAIN-SUFFIX,tsingpost.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 12bc0aca5418  DOMAIN-SUFFIX,malifuke.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 12f8a2b29359  DOMAIN-SUFFIX,73864.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 13b970d36ee3  DOMAIN-SUFFIX,ruchu.club
  - [blackmatrix7 ChinaMaxNoIP Domain] 13e0c001aeb2  DOMAIN-SUFFIX,28ce6d14004bae01.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 144e30e109a1  DOMAIN-SUFFIX,be7076f2b2ff2953.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 14ad52b9e7a9  DOMAIN-SUFFIX,vip360.work
  - [blackmatrix7 ChinaMaxNoIP Domain] 14e98a83daae  DOMAIN-SUFFIX,95659.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 150e128df343  DOMAIN-SUFFIX,qqscb.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 15500da27ab4  DOMAIN-SUFFIX,qzclfc.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 15bb52713330  DOMAIN-SUFFIX,gxgswlhy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 15c4b21e5eff  DOMAIN-SUFFIX,patekphilippe.website
  - [blackmatrix7 ChinaMaxNoIP Domain] 16cd6d0ca92d  DOMAIN-SUFFIX,qzsx168.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 16d25fcabde7  DOMAIN-SUFFIX,uslawchina.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 16dd6972cb21  DOMAIN-SUFFIX,scitycase.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 176987c93f14  DOMAIN-SUFFIX,taopxx.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 177abaee8f02  DOMAIN-SUFFIX,872872.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 18041fa8980e  DOMAIN-SUFFIX,dpd-hul.cfd
  - [blackmatrix7 ChinaMaxNoIP Domain] 181f51ef42ae  DOMAIN-SUFFIX,utoppromo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 190932034403  DOMAIN-SUFFIX,yongche.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 1940509f4041  DOMAIN-SUFFIX,debao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 196f712a6f47  DOMAIN-SUFFIX,jehudf.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 197dc13790e5  DOMAIN-SUFFIX,hyper3d.ai
  - [blackmatrix7 ChinaMaxNoIP Domain] 1994847dae95  DOMAIN-SUFFIX,tingfun.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 1a088004947a  DOMAIN-SUFFIX,wyyve.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1a2ebbb90631  DOMAIN-SUFFIX,weijq.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1a5de96a0ed1  DOMAIN-SUFFIX,dedeeims.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1a84b0f0adf8  DOMAIN-SUFFIX,gwzhinan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1add6d80dcfb  DOMAIN-SUFFIX,94113162.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 1b9db2530ea0  DOMAIN-SUFFIX,cfunctions.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1bc6ccda6d02  DOMAIN-SUFFIX,huawei-eu.store
  - [blackmatrix7 ChinaMaxNoIP Domain] 1c36e5e96300  DOMAIN-SUFFIX,yywords.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1c3901a928a5  DOMAIN-SUFFIX,kowa-dental.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1c9eeaaf7f50  DOMAIN-SUFFIX,nnzdbz.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1cd33458f44d  DOMAIN-SUFFIX,ip-hercules.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1da904abc214  DOMAIN-SUFFIX,luoxue.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1dd3eed92f2e  DOMAIN-SUFFIX,ec45f2d84111f960.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1ded53f9c0b3  DOMAIN-SUFFIX,hljgwy.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 1e022013693c  DOMAIN-SUFFIX,diandanbao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1e5c427da4ae  DOMAIN-SUFFIX,0000f0deb5f4e6c3.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1e97ef32e0e8  DOMAIN-SUFFIX,neznanskyphoto.com
  ... and 683 more
```

## Download.list

**Added: 1** (showing first 1)
```
  + [SukkaW Download] 68167a312594  DOMAIN,releases.openai.com
```

## Global.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 Global] a1a92c4e8192  DOMAIN-SUFFIX,91short.com
```

## Speedtest.list

**Added: 121** (showing first 100)
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
  + [SukkaW Speedtest Servers International] 13ec769f6db0  DOMAIN,speedtest.bakcom.in
  + [SukkaW Speedtest Servers International] 14c7e265c3d8  DOMAIN,speedtest.ibertic.es
  + [SukkaW Speedtest Servers International] 15ee8e1a505a  DOMAIN,speedtest.volo.net
  + [SukkaW Speedtest Servers International] 1753c7265a8d  DOMAIN,st1.ligtel.com
  + [SukkaW Speedtest Servers International] 1debbecee8c5  DOMAIN,speedtest.cstech.com
  + [SukkaW Speedtest Servers International] 203eca7e3de6  DOMAIN,speed-ams.bouwhuisit.nl
  + [SukkaW Speedtest Servers International] 22e17aa36c22  DOMAIN,speedtest-wc.truestreamfiber.us
  + [SukkaW Speedtest Servers International] 27aa9cef1e30  DOMAIN,bytp-speedtest-1.123.net
  + [SukkaW Speedtest Servers International] 29a310f8327b  DOMAIN,speedtest.brooketel.coop
  + [SukkaW Speedtest Servers International] 2a18c247ac08  DOMAIN,ookla.argsment.com
  + [SukkaW Speedtest Servers International] 2a475faf88d3  DOMAIN,spdtst-southbend.fourway.net
  + [SukkaW Speedtest Servers International] 2b911d71aa37  DOMAIN,speedtest.i3broadband.com
  + [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  + [SukkaW Speedtest Servers International] 3307fbfaba51  DOMAIN,st3.surajnetwork.com
  + [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  + [SukkaW Speedtest Servers International] 358795b67fd5  DOMAIN,speedtest.mornington.ca
  + [SukkaW Speedtest Servers International] 37dae1757a6d  DOMAIN,stsaultstemariewireless.rogers.com
  + [SukkaW Speedtest Servers International] 394dff5a7003  DOMAIN,stwindsorwireless.rogers.com
  + [SukkaW Speedtest Servers International] 3c163d104b6b  DOMAIN,spd-100g-ookla.stelogy.io
  + [SukkaW Speedtest Servers International] 3ea882635f75  DOMAIN,speed.sdmnet.com.br
  + [SukkaW Speedtest Servers International] 3ee34e80fced  DOMAIN,speedtest.dvnpiaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  + [SukkaW Speedtest Servers International] 42a36a3fbaf2  DOMAIN,speed.megasyy.com
  + [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  + [SukkaW Speedtest Servers International] 45f4d00908d6  DOMAIN,speedtest-2.hynetwifi.it
  + [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  + [SukkaW Speedtest Servers International] 4b2bec89b1bd  DOMAIN,speedtest.vacastelecom.net
  + [SukkaW Speedtest Servers International] 4c2f2196bc2e  DOMAIN,ookla.lunoxia.net
  + [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  + [SukkaW Speedtest Servers International] 4de50e12bd16  DOMAIN,speedtest.hay.net
  + [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 4fa503514189  DOMAIN,speedtest.packetworks.net
  + [SukkaW Speedtest Servers International] 51219317246c  DOMAIN,speedtest.gmtel.net
  + [SukkaW Speedtest Servers International] 53a654213f1d  DOMAIN,ct-speed.kbro.com.tw
  + [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  + [SukkaW Speedtest Servers International] 5b59c5167680  DOMAIN,sqaookla.ddns.net
  + [SukkaW Speedtest Servers International] 5c69bf15997f  DOMAIN,sp1.speedy.bb-swrag.de
  + [SukkaW Speedtest Servers International] 5c6e09ea3600  DOMAIN,speedtest.stradacomm.com
  + [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  + [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  + [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  + [SukkaW Speedtest Servers International] 626849c0a751  DOMAIN,st1.worldfibernet.com
  + [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  + [SukkaW Speedtest Servers International] 63d6e53c5598  DOMAIN,speed-ens.bouwhuisit.nl
  + [SukkaW Speedtest Servers International] 67fb222e7169  DOMAIN,stbrampton.rogers.com
  + [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  + [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  + [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  + [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  + [SukkaW Speedtest Servers International] 71329f904b4a  DOMAIN,stczs.norteultrafibra.com.br
  + [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  + [SukkaW Speedtest Servers International] 73112e9dc2cb  DOMAIN,speedtest01.adl1.spintel.net.au
  + [SukkaW Speedtest Servers International] 75e802499b21  DOMAIN,stbrampton.netcrawler.ca
  + [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  + [SukkaW Speedtest Servers International] 7b2b5f1619fb  DOMAIN,karnal.sitibroadband.co.in
  + [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 81bf88adcc73  DOMAIN,speed.x-idleb.com
  + [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  + [SukkaW Speedtest Servers International] 8772dc923cf5  DOMAIN,speed-mix.dispaisy.systems
  + [SukkaW Speedtest Servers International] 87a9233f0df1  DOMAIN,383-2speedtest.wightman.ca
  + [SukkaW Speedtest Servers International] 8891940f5fa0  DOMAIN,speedtestmum.mahabalnet.in
  + [SukkaW Speedtest Servers International] 8c67eca44a61  DOMAIN,velocidade.tecsattelecom.com.br
  + [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  + [SukkaW Speedtest Servers International] 90b9b141fa75  DOMAIN,nty-speed.kbro.com.tw
  + [SukkaW Speedtest Servers International] 91dd7903cffa  DOMAIN,speedtest.conectaamazonia.com.br
  + [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  + [SukkaW Speedtest Servers International] 96de22a6ddc7  DOMAIN,st-rockford.sumofiber.com
  + [SukkaW Speedtest Servers International] 96e261bbbb9d  DOMAIN,speed.tnahosting.net
  + [SukkaW Speedtest Servers International] 9868c3f8fedf  DOMAIN,speedtest.s3rdv.com
  + [SukkaW Speedtest Servers International] 9d2342e15aaa  DOMAIN,stkingcity.netcrawler.ca
  + [SukkaW Speedtest Servers International] a2002b5b2805  DOMAIN,speedtest.grr1-mi.incx.net
  + [SukkaW Speedtest Servers International] a2f7f5ad3231  DOMAIN,speedtest.gigazone.in
  + [SukkaW Speedtest Servers International] a31c0a6224a2  DOMAIN,storangeville.rogers.com
  + [SukkaW Speedtest Servers International] a5a39e69aa44  DOMAIN,speedtest.mhtc.net
  + [SukkaW Speedtest Servers International] a6687b2369f5  DOMAIN,stwaterloo.rogers.com
  + [SukkaW Speedtest Servers International] accdf3f5dcf1  DOMAIN,stsarniawireless.rogers.com
  + [SukkaW Speedtest Servers International] ad84593408bf  DOMAIN,st2-msn.5nines.com
  + [SukkaW Speedtest Servers International] ae22d7a42288  DOMAIN,speedtest.supranet.net
  + [SukkaW Speedtest Servers International] b03528f13ca1  DOMAIN,speedtest.marshallfibernet.com
  + [SukkaW Speedtest Servers International] b366228f3322  DOMAIN,ststratfordwireless.rogers.com
  + [SukkaW Speedtest Servers International] b43cd8b37520  DOMAIN,speedtest01.ehtel.ca
  + [SukkaW Speedtest Servers International] b84a68df407f  DOMAIN,speedtest.gosfieldtel.ca
  + [SukkaW Speedtest Servers International] bdb150f52525  DOMAIN,speedtest2.hurontel.on.ca
  + [SukkaW Speedtest Servers International] c06caa39a296  DOMAIN,speedtest.lagrangeremcisp.net
  + [SukkaW Speedtest Servers International] c48494526129  DOMAIN,speedtest3.point-broadband.com
  + [SukkaW Speedtest Servers International] c95a22664ae8  DOMAIN,speedtest.kraus.jbarbieri.net
  + [SukkaW Speedtest Servers International] c962e20b6a7d  DOMAIN,speedtest7.windtre.it
  + [SukkaW Speedtest Servers International] ce3540a348be  DOMAIN,speedtest.geneseo.com
  ... and 21 more
```

**Removed: 140** (showing first 100)
```
  - [SukkaW Speedtest Servers International] 010770237191  DOMAIN,stscarborough.rogers.com
  - [SukkaW Speedtest Servers International] 01d06b461e5c  DOMAIN,speedtest.readingsd.org
  - [SukkaW Speedtest Servers International] 0578ed72ddf9  DOMAIN,speedtest-1.keyubu.com
  - [SukkaW Speedtest Servers International] 0694bb696659  DOMAIN,speedtest005.telecomitalia.it
  - [SukkaW Speedtest Servers International] 0df919f8f00e  DOMAIN,speedtest.nrflvaaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 0ef16a17f7b4  DOMAIN,stbowmanville.rogers.com
  - [SukkaW Speedtest Servers International] 0f56643c702c  DOMAIN,stosat-crls-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] 10777c66c525  DOMAIN,speedtest.atln.ga.wtsky.net
  - [SukkaW Speedtest Servers International] 1179f68f6982  DOMAIN,va-speed.magna5.com
  - [SukkaW Speedtest Servers International] 1239ddbeead0  DOMAIN,speed13.gonetspeed.com
  - [SukkaW Speedtest Servers International] 129fa7cf52e5  DOMAIN,speedtest-newjersey.ripplefiber.com
  - [SukkaW Speedtest Servers International] 166d738a2294  DOMAIN,speedtest.toshamisp.com
  - [SukkaW Speedtest Servers International] 16744b51f48f  DOMAIN,speedtest-ash.vts.bf
  - [SukkaW Speedtest Servers International] 181f2fd1cbb5  DOMAIN,speedtest.iad.fdcservers.net
  - [SukkaW Speedtest Servers International] 19d98c644b57  DOMAIN,speedtest-iad.sectrify.com
  - [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  - [SukkaW Speedtest Servers International] 1b53005476d3  DOMAIN,speedtest.nrbn.ca
  - [SukkaW Speedtest Servers International] 1dd706232871  DOMAIN,speed10.aitspl.in
  - [SukkaW Speedtest Servers International] 1e3705ee2fe6  DOMAIN,speedtest.oceansls.com
  - [SukkaW Speedtest Servers International] 23d5bd5a13bc  DOMAIN,speedtest.gretna.myriverstreet.net
  - [SukkaW Speedtest Servers International] 30df7f1427c6  DOMAIN,speedtest.ette.biz
  - [SukkaW Speedtest Servers International] 319266a22a4b  DOMAIN,karapinar.flix.net.tr
  - [SukkaW Speedtest Servers International] 31b44124210f  DOMAIN,stosat-smil-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] 3263111286ae  DOMAIN,speedtest-zion.fireflyva.com
  - [SukkaW Speedtest Servers International] 32c4df87be80  DOMAIN,speed-syd.gigacomm.net.au
  - [SukkaW Speedtest Servers International] 32c503790c60  DOMAIN,speedtest3.ptd.net
  - [SukkaW Speedtest Servers International] 33041c0f7fd7  DOMAIN,stbowmanville.netcrawler.ca
  - [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  - [SukkaW Speedtest Servers International] 369df213d503  DOMAIN,nycmetro-speedtest.reliablesite.net
  - [SukkaW Speedtest Servers International] 3787edaca5f8  DOMAIN,emr1-ookla.perf.fastedge.it
  - [SukkaW Speedtest Servers International] 3a8aec9cda98  DOMAIN,speedtest-zl-1.zoominternet.net
  - [SukkaW Speedtest Servers International] 3e7bf0bd143d  DOMAIN,speedtest1.ewr.nj.us.planet.net
  - [SukkaW Speedtest Servers International] 414c35bf776f  DOMAIN,speedtest.us.novoserve.com
  - [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  - [SukkaW Speedtest Servers International] 42db00569c58  DOMAIN,speedtest.getwireless.net
  - [SukkaW Speedtest Servers International] 43f75ae5aa25  DOMAIN,speedtest.telbo.net
  - [SukkaW Speedtest Servers International] 44e1fd099c78  DOMAIN,speedtest.sc1.loopinternet.com
  - [SukkaW Speedtest Servers International] 4502550a3a9c  DOMAIN,wpa-speed.magna5.com
  - [SukkaW Speedtest Servers International] 473f9b45897a  DOMAIN,speedtest.winchesterwireless.com
  - [SukkaW Speedtest Servers International] 49f2fe815df7  DOMAIN,speed.markham.telmax.ca
  - [SukkaW Speedtest Servers International] 49ffc4a2950e  DOMAIN,stoshawa.netcrawler.ca
  - [SukkaW Speedtest Servers International] 4f8818240273  DOMAIN,stosat-plfi-08p.sys.comcast.net
  - [SukkaW Speedtest Servers International] 50b8b3905b2f  DOMAIN,speedtest.absenterprises.co.in
  - [SukkaW Speedtest Servers International] 5193c8145d68  DOMAIN,crls-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 51942fed27fc  DOMAIN,speedtest.twl-kom.de
  - [SukkaW Speedtest Servers International] 52a89dbdad82  DOMAIN,speedtest.us-ny2.kamatera.com
  - [SukkaW Speedtest Servers International] 52ea711702a9  DOMAIN,speedtestnorthpointe.arkdnacloud.com
  - [SukkaW Speedtest Servers International] 5559912850cd  DOMAIN,speedtest.belmontcountygig.com
  - [SukkaW Speedtest Servers International] 55c0cb8dcbb9  DOMAIN,speedtest2.pa.mycci.net
  - [SukkaW Speedtest Servers International] 57cfe7333ea8  DOMAIN,fast.blackbearfiber.com
  - [SukkaW Speedtest Servers International] 5893bd721aca  DOMAIN,stnorthyork.netcrawler.ca
  - [SukkaW Speedtest Servers International] 5ab2e37aaffc  DOMAIN,speedtest31.suddenlink.net
  - [SukkaW Speedtest Servers International] 60ac93c18792  DOMAIN,stscarborough.netcrawler.ca
  - [SukkaW Speedtest Servers International] 615ab422b360  DOMAIN,btlr-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 6240dc262b53  DOMAIN,speedtest1.whsdk12.net
  - [SukkaW Speedtest Servers International] 625966c841d3  DOMAIN,speedtest1.ric1.va.hostedbackbone.net
  - [SukkaW Speedtest Servers International] 6722a4f62ff8  DOMAIN,stbowmanvillewireless.rogers.com
  - [SukkaW Speedtest Servers International] 67382fe7fa61  DOMAIN,stoshawa.rogers.com
  - [SukkaW Speedtest Servers International] 6846a38f9372  DOMAIN,speedtest.asbn.va.wtsky.net
  - [SukkaW Speedtest Servers International] 68c6eb173f83  DOMAIN,asbn-speedtest.northstate.net
  - [SukkaW Speedtest Servers International] 698bcfb1bb21  DOMAIN,speedtest-preston-wv.prodigiwv.net
  - [SukkaW Speedtest Servers International] 6a6f44221018  DOMAIN,txg-speedtest.infinirc.com
  - [SukkaW Speedtest Servers International] 6aafcc1f0064  DOMAIN,speedtest.americatelecom.net.br
  - [SukkaW Speedtest Servers International] 6b8f1c9f7c44  DOMAIN,stajax.rogers.com
  - [SukkaW Speedtest Servers International] 6ef5f28df61c  DOMAIN,ookla.aeq.as6453.net
  - [SukkaW Speedtest Servers International] 74a6d6e46908  DOMAIN,speedtest.wb1.loopinternet.com
  - [SukkaW Speedtest Servers International] 7625db817368  DOMAIN,speedtest1.iad1-us.gozfly.net
  - [SukkaW Speedtest Servers International] 76abfa7b0ce2  DOMAIN,speedtest-mel.vic.au.hostuniversal.com.au
  - [SukkaW Speedtest Servers International] 77cb389996a6  DOMAIN,speedtest-bethlehem.greenlightnetworks.com
  - [SukkaW Speedtest Servers International] 77e56dc99c59  DOMAIN,cltn-speedtest-02.brightspeed.com
  - [SukkaW Speedtest Servers International] 7c4e62477d2e  DOMAIN,speedtest.zoominternet.net
  - [SukkaW Speedtest Servers International] 7de305557319  DOMAIN,altoonaspeedtest.crowsnestbb.net
  - [SukkaW Speedtest Servers International] 8141004af16b  DOMAIN,speedtest02.srv.prnynj.alticeusa.net
  - [SukkaW Speedtest Servers International] 83e830bbc65c  DOMAIN,speedtest4.point-broadband.com
  - [SukkaW Speedtest Servers International] 8487be6e6d95  DOMAIN,speedtest.mifflincountywireless.com
  - [SukkaW Speedtest Servers International] 8632dbc95ac0  DOMAIN,stnorthyorkwireless.rogers.com
  - [SukkaW Speedtest Servers International] 894527aa356c  DOMAIN,lsdspeed01.lsdops.net
  - [SukkaW Speedtest Servers International] 8fd05fb4ff7e  DOMAIN,speedtest19.suddenlink.net
  - [SukkaW Speedtest Servers International] 90617691e3af  DOMAIN,stwhitby.netcrawler.ca
  - [SukkaW Speedtest Servers International] 910cf0769104  DOMAIN,speedtest-nwrk-nj.wtsky.net
  - [SukkaW Speedtest Servers International] 9138c74c88d2  DOMAIN,vaspeedtest.rackdog.com
  - [SukkaW Speedtest Servers International] 91f667018cba  DOMAIN,speedtestfe.stel.it
  - [SukkaW Speedtest Servers International] 945f6dd36368  DOMAIN,velocimetro.smartmovel.net
  - [SukkaW Speedtest Servers International] 9660747a5a08  DOMAIN,speed01.gonetspeed.com
  - [SukkaW Speedtest Servers International] 96e24c3aaac2  DOMAIN,stoshawawireless.rogers.com
  - [SukkaW Speedtest Servers International] 9805c3888ee2  DOMAIN,speedtest.taifo.com.tw
  - [SukkaW Speedtest Servers International] 995889b17f13  DOMAIN,lsdspeed02.lsdops.net
  - [SukkaW Speedtest Servers International] 99d636115e4d  DOMAIN,speedtest.kdatacenter.com
  - [SukkaW Speedtest Servers International] 9b36e6ace41e  DOMAIN,phlph0001speedtestserver02.wiline.com
  - [SukkaW Speedtest Servers International] 9be25423b741  DOMAIN,servidor.speedplay.com.br
  - [SukkaW Speedtest Servers International] 9c36ab36b132  DOMAIN,phl01.screenshot.download
  - [SukkaW Speedtest Servers International] 9ee8a1734e62  DOMAIN,speedtest2.sistelfibra.es
  - [SukkaW Speedtest Servers International] 9f094a91d810  DOMAIN,ookla.micrologicwv.com
  - [SukkaW Speedtest Servers International] 9f6b30de3d0b  DOMAIN,speedtest-server-ash.starry.com
  - [SukkaW Speedtest Servers International] a0546159a969  DOMAIN,speedtest.quickqc.nl
  - [SukkaW Speedtest Servers International] af96649eed17  DOMAIN,speedtest.auratelecom.com.br
  - [SukkaW Speedtest Servers International] b053213fa908  DOMAIN,speedtest4.lepida.it
  - [SukkaW Speedtest Servers International] b06e6a3b7c0f  DOMAIN,speedtest.philasd.org
  - [SukkaW Speedtest Servers International] b0cc745d6216  DOMAIN,stosat-balt-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] b4f4faf0a782  DOMAIN,speedtest.fiberlync.net
  ... and 40 more
```
