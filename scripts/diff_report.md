# Surge Rule Diff Report
Generated: 2026-10-24T05:01:36.418127

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 128 |
| Rules removed | 74 |
| Source attribution changed | 6 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| CDN.list | 30 | 31 | +1 | -0 | ~0 |
| China_IP.list | 11846 | 11847 | +1 | -0 | ~6 |
| Speedtest.list | 1669 | 1721 | +126 | -74 | ~0 |

## CDN.list

**Added: 1** (showing first 1)
```
  + [SukkaW CDN] 9f985be945eb  DOMAIN-WILDCARD,cf-images.*.prod.boltdns.net
```

## China_IP.list

**Added: 1** (showing first 1)
```
  + [Loyalsoldier China CIDR] 36fe9004783e  IP-CIDR,45.119.42.0/23
```

**Source changed: 6**
```
  ~ 7f6313ff65fb: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ 756ea1a9855b: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 4bd08bfb3f64: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d58cf27ea800: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
  ~ 5fe5cd7eaa3c: [blackmatrix7 China IPs → Loyalsoldier China CIDR]
  ~ d2e2b66553d4: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Speedtest.list

**Added: 126** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 02b7b422882f  DOMAIN,speedtest.sentco.net
  + [SukkaW Speedtest Servers International] 04df25e28545  DOMAIN,speedtest.premieronline.net
  + [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  + [SukkaW Speedtest Servers International] 0cc435ecaed2  DOMAIN,teste.freedomnetwork.net.br
  + [SukkaW Speedtest Servers International] 12ca2bed9dbb  DOMAIN,speedtest.atccomm.net
  + [SukkaW Speedtest Servers International] 13dc2485ab95  DOMAIN,speedtest.heartofiowa.coop
  + [SukkaW Speedtest Servers International] 14696c5e4444  DOMAIN,speedtest.cmltelephone.com
  + [SukkaW Speedtest Servers International] 189c17014e83  DOMAIN,speedtest.amesiaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 1cfb48abbf36  DOMAIN,speedtest.grm.net
  + [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 1e9ede2ea46b  DOMAIN,speedtest.westianet.com
  + [SukkaW Speedtest Servers International] 2ab9b0da9911  DOMAIN,lcrs-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 304d2683e43f  DOMAIN,speedtest.skywaveconnect.com
  + [SukkaW Speedtest Servers International] 32b355be6336  DOMAIN,speedtest.bluevalley.net
  + [SukkaW Speedtest Servers International] 34d320d8b02f  DOMAIN,speedtest.mdtc.net
  + [SukkaW Speedtest Servers International] 3915020d9cf5  DOMAIN,spt-dal1.edgeuno.com
  + [SukkaW Speedtest Servers International] 3a92209ad6ba  DOMAIN,speedtest-01.omnitel.biz
  + [SukkaW Speedtest Servers International] 3a97abf4595c  DOMAIN,speedtest1.oma.nxlink.com
  + [SukkaW Speedtest Servers International] 3b0dc040ff61  DOMAIN,speed.nutelecom.com
  + [SukkaW Speedtest Servers International] 3f2a1255658c  DOMAIN,blfd-speed-01.gpcom.com
  + [SukkaW Speedtest Servers International] 3f4d8d5400bc  DOMAIN,spt-ist.edgeuno.com
  + [SukkaW Speedtest Servers International] 3f7075e220a1  DOMAIN,ksczks-speedtest-ookla-01.st.charter.com
  + [SukkaW Speedtest Servers International] 3f8306542a0b  DOMAIN,stsudburywireless.rogers.com
  + [SukkaW Speedtest Servers International] 41bc4d2333e5  DOMAIN,speedtest.cvalley.net
  + [SukkaW Speedtest Servers International] 42a36a3fbaf2  DOMAIN,speed.megasyy.com
  + [SukkaW Speedtest Servers International] 43f75ae5aa25  DOMAIN,speedtest.telbo.net
  + [SukkaW Speedtest Servers International] 45ed5f3bd479  DOMAIN,speedtest.tcaexpress.net
  + [SukkaW Speedtest Servers International] 48e2d32a2895  DOMAIN,speedtest.cascadecomm.com
  + [SukkaW Speedtest Servers International] 4bbf2a0a0fa3  DOMAIN,speedtest.mysmbs.com
  + [SukkaW Speedtest Servers International] 4bc2ef4606ca  DOMAIN,st-oma-1.binary.net
  + [SukkaW Speedtest Servers International] 4c8fd6b2f3f6  DOMAIN,ookla-ks.mercuryfiber.com
  + [SukkaW Speedtest Servers International] 4db3cbb342cd  DOMAIN,speedtest-lenexa.resoundnetworks.com
  + [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  + [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  + [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  + [SukkaW Speedtest Servers International] 565ea387b1e5  DOMAIN,speedtest.cfu.net
  + [SukkaW Speedtest Servers International] 58e6d169adef  DOMAIN,speedtest.esu5.org
  + [SukkaW Speedtest Servers International] 59b3f6172efc  DOMAIN,spt-jfk1.edgeuno.com
  + [SukkaW Speedtest Servers International] 59f0ec25e179  DOMAIN,blar-speed-01.gpcom.com
  + [SukkaW Speedtest Servers International] 5f3fcd920887  DOMAIN,speedtest.ncn.net
  + [SukkaW Speedtest Servers International] 605cfb35f522  DOMAIN,speedtest.mci.as1003.net
  + [SukkaW Speedtest Servers International] 645c547cce51  DOMAIN,speedtest.onetouchexpress.com
  + [SukkaW Speedtest Servers International] 6bd15d569f45  DOMAIN,velocidade.csrnetwork.com.br
  + [SukkaW Speedtest Servers International] 6ff5941eb406  DOMAIN,exc-speedtest.unitedfiber.com
  + [SukkaW Speedtest Servers International] 714a4168143c  DOMAIN,spt-lon1.edgeuno.com
  + [SukkaW Speedtest Servers International] 7590487e9734  DOMAIN,spt-lax1.edgeuno.com
  + [SukkaW Speedtest Servers International] 761a11540f93  DOMAIN,siouxcity1.cabospeed.com
  + [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 7935cf977efe  DOMAIN,speedtest.wwfn.ca
  + [SukkaW Speedtest Servers International] 79b4a7b648ff  DOMAIN,speedtest.cncbroadband.in
  + [SukkaW Speedtest Servers International] 7a4042ca0d6f  DOMAIN,stbarriewireless.rogers.com
  + [SukkaW Speedtest Servers International] 7a55e968bb85  DOMAIN,speedtest.unitedfiber.com
  + [SukkaW Speedtest Servers International] 7ad78e8435d7  DOMAIN,speed.ddbroadband.co.in
  + [SukkaW Speedtest Servers International] 7bdc14806a7c  DOMAIN,speedtest.wccta.com
  + [SukkaW Speedtest Servers International] 7ea92d713139  DOMAIN,speedtest.rochmnaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 809ed12ed910  DOMAIN,speedtest.nemr.net
  + [SukkaW Speedtest Servers International] 84b8446a854b  DOMAIN,speedtest10g.ics-llc.net
  + [SukkaW Speedtest Servers International] 86f4178b9153  DOMAIN,speedtest.fibercomm.net
  + [SukkaW Speedtest Servers International] 8c9d7c03fa30  DOMAIN,speedtest27.suddenlink.net
  + [SukkaW Speedtest Servers International] 8cfc393702b7  DOMAIN,speedtest.kc2.everfastfiber.com
  + [SukkaW Speedtest Servers International] 905125f73ee5  DOMAIN,speedtest.mvec.com
  + [SukkaW Speedtest Servers International] 9052a64cc3fd  DOMAIN,speedtest25.wiatel.com
  + [SukkaW Speedtest Servers International] 9073adefc65d  DOMAIN,speedtest.neitel.net
  + [SukkaW Speedtest Servers International] 93617c692bd8  DOMAIN,ookla.mci-1.serverforge.org
  + [SukkaW Speedtest Servers International] 945f6dd36368  DOMAIN,velocimetro.smartmovel.net
  + [SukkaW Speedtest Servers International] 991108b39981  DOMAIN,speedtest.mtctech.net
  + [SukkaW Speedtest Servers International] 99246723a229  DOMAIN,speedtest-mci-01.pdx.net.uk
  + [SukkaW Speedtest Servers International] 9ef50333ec52  DOMAIN,speedtestmoh1.airtelbroadband.in
  + [SukkaW Speedtest Servers International] 9fc768aebccf  DOMAIN,speedtest.nexgencom.com
  + [SukkaW Speedtest Servers International] a03e396de9e0  DOMAIN,mib-rst-sp1.mibroadband.com
  + [SukkaW Speedtest Servers International] a258e2019d32  DOMAIN,sp1.voyageurinternet.ca
  + [SukkaW Speedtest Servers International] a63f83296451  DOMAIN,speed.tritan-bb.net
  + [SukkaW Speedtest Servers International] a64508c249b0  DOMAIN,lnk-speedtest.networknebraska.net
  + [SukkaW Speedtest Servers International] a6619de300c2  DOMAIN,st2a.les.net
  + [SukkaW Speedtest Servers International] ab415fae2613  DOMAIN,speedtest.longlines.com
  + [SukkaW Speedtest Servers International] accaab45f3ac  DOMAIN,speedtest-dsm.cowboyhosting.com
  + [SukkaW Speedtest Servers International] adc92f2f9e63  DOMAIN,speedtest-1.apvinvestimenti.it
  + [SukkaW Speedtest Servers International] aecf28573fd6  DOMAIN,speedtest.heartlandtechnology.com
  + [SukkaW Speedtest Servers International] afce71228313  DOMAIN,topnet.brsserver.com.br
  + [SukkaW Speedtest Servers International] b0f72f833c9f  DOMAIN,ookla.araujotelecom.com.br
  + [SukkaW Speedtest Servers International] b7cba41d7626  DOMAIN,speedtest1.dsm1.ippathways.net
  + [SukkaW Speedtest Servers International] b8a0e7029ee0  DOMAIN,stosat-indp-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] b932b53593e0  DOMAIN,speed.srv.rent
  + [SukkaW Speedtest Servers International] ba48de7cf518  DOMAIN,speedtestve1.telecomitalia.it
  + [SukkaW Speedtest Servers International] bb37aed618a1  DOMAIN,speedtest.waterloofiber.com
  + [SukkaW Speedtest Servers International] bfafedcf989a  DOMAIN,iola-st-ookla.kwikom.com
  + [SukkaW Speedtest Servers International] c0ba82f0fb9d  DOMAIN,vanspeedtest.altimatel.com
  + [SukkaW Speedtest Servers International] c11b51d67b4a  DOMAIN,stbarrie.netcrawler.ca
  + [SukkaW Speedtest Servers International] c2222406ebe9  DOMAIN,speedtest.palmerone.com
  + [SukkaW Speedtest Servers International] c3109cd31fc9  DOMAIN,srv02-sjdm.imj-wanklik.com
  + [SukkaW Speedtest Servers International] c56b34c86c50  DOMAIN,stwinnipegwireless.rogers.com
  + [SukkaW Speedtest Servers International] c7316104a7b2  DOMAIN,speedtest.cltel.com
  + [SukkaW Speedtest Servers International] cb0ed23687a9  DOMAIN,speed.kansas.smishcraft.com
  + [SukkaW Speedtest Servers International] cf1403b737c5  DOMAIN,speedtest1.acentek.net
  + [SukkaW Speedtest Servers International] cf8895c26ec0  DOMAIN,lnk11-speedtest01.as15108.com
  + [SukkaW Speedtest Servers International] d003609144e4  DOMAIN,speedtest-mci-01.accuris.ca
  + [SukkaW Speedtest Servers International] d3bf9a607d1e  DOMAIN,speedtest-kc.conexonconnect.com
  + [SukkaW Speedtest Servers International] d7ef6a964002  DOMAIN,speedtest01.imon.net
  + [SukkaW Speedtest Servers International] d8fca8393d99  DOMAIN,us-central1-c.gcp.spd.synthesis.health
  + [SukkaW Speedtest Servers International] d980d4d61909  DOMAIN,imrteixeira.brsserver.com.br
  ... and 26 more
```

**Removed: 74** (showing first 74)
```
  - [SukkaW Speedtest Servers International] 0009d45cc71f  DOMAIN,speedtest-gdrp.merit.edu
  - [SukkaW Speedtest Servers International] 0561b044089c  DOMAIN,ran-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 0711f9d6046b  DOMAIN,cbpuspeed.aspensmart.net
  - [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  - [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  - [SukkaW Speedtest Servers International] 0f0435a45fac  DOMAIN,speedtest.oa.net
  - [SukkaW Speedtest Servers International] 0f923e75457a  DOMAIN,ookla-in.mercuryfiber.com
  - [SukkaW Speedtest Servers International] 134564537572  DOMAIN,speedtest.sycmilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 15ee8e1a505a  DOMAIN,speedtest.volo.net
  - [SukkaW Speedtest Servers International] 1753c7265a8d  DOMAIN,st1.ligtel.com
  - [SukkaW Speedtest Servers International] 22e17aa36c22  DOMAIN,speedtest-wc.truestreamfiber.us
  - [SukkaW Speedtest Servers International] 27aa9cef1e30  DOMAIN,bytp-speedtest-1.123.net
  - [SukkaW Speedtest Servers International] 2a475faf88d3  DOMAIN,spdtst-southbend.fourway.net
  - [SukkaW Speedtest Servers International] 2b911d71aa37  DOMAIN,speedtest.i3broadband.com
  - [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  - [SukkaW Speedtest Servers International] 3307fbfaba51  DOMAIN,st3.surajnetwork.com
  - [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  - [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  - [SukkaW Speedtest Servers International] 3697595f756d  DOMAIN,sp3.atcc-gns.net
  - [SukkaW Speedtest Servers International] 36b91e77e572  DOMAIN,st34ata.netspeed.tr
  - [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  - [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  - [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  - [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  - [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  - [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  - [SukkaW Speedtest Servers International] 5b0b7c47633d  DOMAIN,sirsa.softechinfosol.com
  - [SukkaW Speedtest Servers International] 5cb71d1b2142  DOMAIN,pri-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  - [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  - [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  - [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  - [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  - [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  - [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  - [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  - [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  - [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  - [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  - [SukkaW Speedtest Servers International] 85b7f8f6df4c  DOMAIN,spd79.claro.com.br
  - [SukkaW Speedtest Servers International] 8772dc923cf5  DOMAIN,speed-mix.dispaisy.systems
  - [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  - [SukkaW Speedtest Servers International] 91dd7903cffa  DOMAIN,speedtest.conectaamazonia.com.br
  - [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 96692f154a26  DOMAIN,veloteste.mrjomar.com.br
  - [SukkaW Speedtest Servers International] 96de22a6ddc7  DOMAIN,st-rockford.sumofiber.com
  - [SukkaW Speedtest Servers International] 96e261bbbb9d  DOMAIN,speed.tnahosting.net
  - [SukkaW Speedtest Servers International] 99050f480dac  DOMAIN,speedtest.flynet.it
  - [SukkaW Speedtest Servers International] 9d2342e15aaa  DOMAIN,stkingcity.netcrawler.ca
  - [SukkaW Speedtest Servers International] a2002b5b2805  DOMAIN,speedtest.grr1-mi.incx.net
  - [SukkaW Speedtest Servers International] a5a39e69aa44  DOMAIN,speedtest.mhtc.net
  - [SukkaW Speedtest Servers International] aa4b3246f9f9  DOMAIN,hiztesti.fiberim.com.tr
  - [SukkaW Speedtest Servers International] ae22d7a42288  DOMAIN,speedtest.supranet.net
  - [SukkaW Speedtest Servers International] b03528f13ca1  DOMAIN,speedtest.marshallfibernet.com
  - [SukkaW Speedtest Servers International] b2746e9de40c  DOMAIN,speedtest-net.hyprnode.de
  - [SukkaW Speedtest Servers International] b73df15da330  DOMAIN,stetobicoke.netcrawler.ca
  - [SukkaW Speedtest Servers International] c06caa39a296  DOMAIN,speedtest.lagrangeremcisp.net
  - [SukkaW Speedtest Servers International] c48494526129  DOMAIN,speedtest3.point-broadband.com
  - [SukkaW Speedtest Servers International] c95a22664ae8  DOMAIN,speedtest.kraus.jbarbieri.net
  - [SukkaW Speedtest Servers International] cb103aa8b7a1  DOMAIN,speedtest010.telecomitalia.it
  - [SukkaW Speedtest Servers International] d11b286bd2a4  DOMAIN,de-speedtest.digitalexample.com
  - [SukkaW Speedtest Servers International] d47fe5fd7010  DOMAIN,speedtest-obd.redeconecta.com
  - [SukkaW Speedtest Servers International] d77254c621cc  DOMAIN,speedtest3.myninestar.net
  - [SukkaW Speedtest Servers International] e1c9b22eab29  DOMAIN,speedtest.wnet.net.in
  - [SukkaW Speedtest Servers International] e7f15789e6d0  DOMAIN,speedtest.taylor.edu
  - [SukkaW Speedtest Servers International] eacb466cdf37  DOMAIN,kzspeedtest01.aunalytics.com
  - [SukkaW Speedtest Servers International] ec01ae8210c3  DOMAIN,speedtest.zivlinaa.metronetinc.com
  - [SukkaW Speedtest Servers International] ec456ca1f360  DOMAIN,speedtest1.ctstelecom.com
  - [SukkaW Speedtest Servers International] f2367bf1b8eb  DOMAIN,stvaughan.rogers.com
  - [SukkaW Speedtest Servers International] ff97ee6115e9  DOMAIN,btestmcp.vocetelecom.vc
```
