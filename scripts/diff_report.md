# Surge Rule Diff Report
Generated: 2026-11-21T05:00:22.734098

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 196 |
| Rules removed | 124 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 126 | 127 | +1 | -0 | ~0 |
| China_IP.list | 9640 | 9665 | +74 | -49 | ~0 |
| Speedtest.list | 1679 | 1725 | +121 | -75 | ~0 |

## AI.list

**Added: 1** (showing first 1)
```
  + [SukkaW AI] 391d402853fb  DOMAIN,claude.site
```

## China_IP.list

**Added: 74** (showing first 74)
```
  + [Loyalsoldier China CIDR] 024eae47dd7e  IP-CIDR6,2406:840:4c0::/42
  + [Loyalsoldier China CIDR] 025a9e45311f  IP-CIDR6,2406:840:9814::/46
  + [Loyalsoldier China CIDR] 044a97e2f486  IP-CIDR6,2402:8260::/37
  + [Loyalsoldier China CIDR] 061245f65268  IP-CIDR,123.49.224.0/21
  + [Loyalsoldier China CIDR] 0de88af97af3  IP-CIDR6,2406:840:9812::/47
  + [Loyalsoldier China CIDR] 13016706cdcd  IP-CIDR,123.49.198.0/23
  + [Loyalsoldier China CIDR] 17b5ac6401ca  IP-CIDR,223.252.160.0/21
  + [Loyalsoldier China CIDR] 212f1fdca58d  IP-CIDR,117.120.152.0/22
  + [Loyalsoldier China CIDR] 2404bd317ba7  IP-CIDR6,2402:8260:4d00::/40
  + [Loyalsoldier China CIDR] 24b301586587  IP-CIDR,151.158.123.0/24
  + [Loyalsoldier China CIDR] 26f862365cbc  IP-CIDR6,2a0a:d685:700::/40
  + [Loyalsoldier China CIDR] 29f0da7a53b8  IP-CIDR,111.119.112.0/20
  + [Loyalsoldier China CIDR] 2ce613d78f3e  IP-CIDR6,2406:840:4a0::/43
  + [Loyalsoldier China CIDR] 2ce90221a350  IP-CIDR6,2400:5a60:40::/42
  + [Loyalsoldier China CIDR] 35365212d52b  IP-CIDR6,2406:840:e0ea::/47
  + [Loyalsoldier China CIDR] 3aeeb5eadb64  IP-CIDR,59.153.174.0/23
  + [Loyalsoldier China CIDR] 3dd50f386bc6  IP-CIDR,123.49.232.0/22
  + [Loyalsoldier China CIDR] 3f52a9fb30dc  IP-CIDR,103.5.194.0/24
  + [Loyalsoldier China CIDR] 3f76a44c0627  IP-CIDR6,2a13:7100::/29
  + [Loyalsoldier China CIDR] 433ba978c748  IP-CIDR,103.5.192.0/23
  + [Loyalsoldier China CIDR] 4e0318410e63  IP-CIDR,124.20.192.0/20
  + [Loyalsoldier China CIDR] 511026d3f575  IP-CIDR,211.149.44.0/22
  + [Loyalsoldier China CIDR] 58d675a32dee  IP-CIDR6,2402:8260:900::/40
  + [Loyalsoldier China CIDR] 5ad2012349cd  IP-CIDR,111.119.64.0/19
  + [Loyalsoldier China CIDR] 5c8febf80bfe  IP-CIDR,122.14.136.0/21
  + [Loyalsoldier China CIDR] 6318d1a3e8de  IP-CIDR6,2400:5a60:20::/43
  + [Loyalsoldier China CIDR] 64b93ed75c32  IP-CIDR,122.14.134.0/23
  + [Loyalsoldier China CIDR] 67c0e297438f  IP-CIDR,117.120.160.0/19
  + [Loyalsoldier China CIDR] 6d5e3236a94c  IP-CIDR6,2402:8260:8000::/33
  + [Loyalsoldier China CIDR] 6e6b7e1be16b  IP-CIDR6,2402:8260:2000::/35
  + [Loyalsoldier China CIDR] 741b80a1aa15  IP-CIDR6,2402:8260:4000::/37
  + [Loyalsoldier China CIDR] 76d826891e7e  IP-CIDR,59.153.168.0/22
  + [Loyalsoldier China CIDR] 7730f75cdc37  IP-CIDR6,2406:840:482::/47
  + [Loyalsoldier China CIDR] 7871ed847b45  IP-CIDR,122.14.133.0/24
  + [Loyalsoldier China CIDR] 7929a3a51e92  IP-CIDR,59.153.173.0/24
  + [Loyalsoldier China CIDR] 7fbe0ac904f5  IP-CIDR,117.120.128.0/20
  + [Loyalsoldier China CIDR] 8113ab73d9f6  IP-CIDR6,2400:5a60:3::/48
  + [Loyalsoldier China CIDR] 831f703ae224  IP-CIDR6,2406:840:484::/46
  + [Loyalsoldier China CIDR] 86d33e41de0f  IP-CIDR,124.20.48.0/20
  + [Loyalsoldier China CIDR] 87d3284cd1e5  IP-CIDR6,2402:8260:b00::/40
  + [Loyalsoldier China CIDR] 87f03b29d614  IP-CIDR,103.181.165.0/24
  + [Loyalsoldier China CIDR] 8a143e3977ac  IP-CIDR6,2406:840:490::/44
  + [Loyalsoldier China CIDR] 90b58c061d66  IP-CIDR6,2402:8260:4800::/38
  + [Loyalsoldier China CIDR] 948170ddf5ea  IP-CIDR6,2406:840:9970::/44
  + [Loyalsoldier China CIDR] 962a79f9e66c  IP-CIDR,223.252.176.0/20
  + [Loyalsoldier China CIDR] a591000eeba0  IP-CIDR,124.21.224.0/20
  + [Loyalsoldier China CIDR] a5b3363dacd2  IP-CIDR6,2402:8260:5000::/36
  + [Loyalsoldier China CIDR] a748776179af  IP-CIDR6,2400:5a60:10::/44
  + [Loyalsoldier China CIDR] b372851798c1  IP-CIDR6,2400:5a60:8::/45
  + [Loyalsoldier China CIDR] b40c6898caf5  IP-CIDR6,2406:840:e0e9::/48
  + [Loyalsoldier China CIDR] b7e257878ce6  IP-CIDR,117.120.144.0/21
  + [Loyalsoldier China CIDR] b7f9e38abc8e  IP-CIDR,223.252.174.0/23
  + [Loyalsoldier China CIDR] ba673f69b10d  IP-CIDR6,2402:8260:4e00::/39
  + [Loyalsoldier China CIDR] c42fecba7083  IP-CIDR,111.119.96.0/21
  + [Loyalsoldier China CIDR] c527b812d983  IP-CIDR6,2406:840:481::/48
  + [Loyalsoldier China CIDR] c6fea9d78e64  IP-CIDR6,2400:5a60::/47
  + [Loyalsoldier China CIDR] c711c25e5a2e  IP-CIDR6,2400:5a60:4::/46
  + [Loyalsoldier China CIDR] ce8c27b5d379  IP-CIDR,123.49.236.0/24
  + [Loyalsoldier China CIDR] d2e2b66553d4  IP-CIDR6,2620:57:4004::/47
  + [Loyalsoldier China CIDR] d45a35893f27  IP-CIDR6,2402:8260:c00::/38
  + [Loyalsoldier China CIDR] d5dbba7b6932  IP-CIDR,211.149.32.0/22
  + [Loyalsoldier China CIDR] db58c1048ae6  IP-CIDR,122.14.128.0/22
  + [Loyalsoldier China CIDR] dc48256c1bfc  IP-CIDR,223.252.192.0/18
  + [Loyalsoldier China CIDR] dca52062fa21  IP-CIDR,223.252.128.0/19
  + [Loyalsoldier China CIDR] e0a7075a1b13  IP-CIDR,141.229.21.0/24
  + [Loyalsoldier China CIDR] e0de8704e0e8  IP-CIDR6,2406:840:488::/45
  + [Loyalsoldier China CIDR] e37fdfb6372a  IP-CIDR6,2402:8260:6000::/35
  + [Loyalsoldier China CIDR] e81ead731437  IP-CIDR,223.252.172.0/24
  + [Loyalsoldier China CIDR] eb9467b807f8  IP-CIDR6,2406:840:9811::/48
  + [Loyalsoldier China CIDR] f559f52e4e17  IP-CIDR,223.252.168.0/22
  + [Loyalsoldier China CIDR] f5fc73af7506  IP-CIDR6,2402:8260:1000::/36
  + [Loyalsoldier China CIDR] f8c1e13a0ee9  IP-CIDR6,2406:840:e0ec::/46
  + [Loyalsoldier China CIDR] fc2c18fa81f0  IP-CIDR,43.239.176.0/22
  + [Loyalsoldier China CIDR] fc7c1827ab42  IP-CIDR,123.49.197.0/24
```

**Removed: 49** (showing first 49)
```
  - [Loyalsoldier China CIDR] 19cdb102106c  IP-CIDR,124.21.224.0/19
  - [Loyalsoldier China CIDR] 1b487d2e2f37  IP-CIDR,211.149.34.0/23
  - [Loyalsoldier China CIDR] 206e90f2a20a  IP-CIDR,163.223.216.0/24
  - [Loyalsoldier China CIDR] 226f09f6b6c5  IP-CIDR,211.149.33.0/24
  - [Loyalsoldier China CIDR] 29427252e06c  IP-CIDR,160.202.210.0/23
  - [Loyalsoldier China CIDR] 305988ed5f55  IP-CIDR,103.74.124.0/24
  - [Loyalsoldier China CIDR] 35aebcbd8847  IP-CIDR,122.8.76.0/22
  - [Loyalsoldier China CIDR] 40e9b8d2a4b4  IP-CIDR,122.8.116.0/22
  - [Loyalsoldier China CIDR] 4815755cca3f  IP-CIDR,122.0.224.0/20
  - [Loyalsoldier China CIDR] 49f3ae300b96  IP-CIDR6,2406:840:9974::/47
  - [Loyalsoldier China CIDR] 56dd3524e7ce  IP-CIDR,117.120.184.0/21
  - [Loyalsoldier China CIDR] 5c5dd81e1b53  IP-CIDR6,2406:840:fd58::/48
  - [Loyalsoldier China CIDR] 5d1f33855f8f  IP-CIDR,43.239.176.0/23
  - [Loyalsoldier China CIDR] 5e66d62df3e7  IP-CIDR6,2400:5a60::/41
  - [Loyalsoldier China CIDR] 5e7161e9b8df  IP-CIDR,103.74.126.0/23
  - [Loyalsoldier China CIDR] 618774bc96d5  IP-CIDR,124.20.192.0/19
  - [Loyalsoldier China CIDR] 6c6716bdf3c7  IP-CIDR6,2406:840:fd48::/48
  - [Loyalsoldier China CIDR] 6c84599d7800  IP-CIDR,223.252.128.0/17
  - [Loyalsoldier China CIDR] 6fceedcdd8e5  IP-CIDR,206.109.75.0/24
  - [Loyalsoldier China CIDR] 707d4ff082d3  IP-CIDR6,2406:840:9978::/45
  - [Loyalsoldier China CIDR] 7709dc3ce14c  IP-CIDR,151.158.14.0/23
  - [Loyalsoldier China CIDR] 8eb60d0b4997  IP-CIDR,151.158.122.0/23
  - [Loyalsoldier China CIDR] 910d7e4af099  IP-CIDR,117.120.164.0/22
  - [Loyalsoldier China CIDR] 933280acba0c  IP-CIDR,103.177.44.0/23
  - [Loyalsoldier China CIDR] 9591e9f39227  IP-CIDR,119.27.224.0/20
  - [Loyalsoldier China CIDR] a6148d4bee83  IP-CIDR6,2406:840:feff::/48
  - [Loyalsoldier China CIDR] a72947463d05  IP-CIDR,141.229.15.0/24
  - [Loyalsoldier China CIDR] aaaaa79eb195  IP-CIDR6,2406:840:9970::/46
  - [Loyalsoldier China CIDR] ac3241b8b526  IP-CIDR,103.5.192.0/22
  - [Loyalsoldier China CIDR] b47f60a08fad  IP-CIDR,111.119.64.0/18
  - [Loyalsoldier China CIDR] b4d53169f4fe  IP-CIDR6,2406:840:fd88::/48
  - [Loyalsoldier China CIDR] b4fafd5d140e  IP-CIDR,117.120.148.0/22
  - [Loyalsoldier China CIDR] b82f8b5b0069  IP-CIDR6,2406:840:480::/41
  - [Loyalsoldier China CIDR] ba7ed4353618  IP-CIDR6,2406:840:9810::/45
  - [Loyalsoldier China CIDR] bf899d039f5c  IP-CIDR,122.8.68.0/22
  - [Loyalsoldier China CIDR] c39f32890d14  IP-CIDR,123.49.224.0/20
  - [Loyalsoldier China CIDR] c994e7a1413b  IP-CIDR6,2a0a:d685:600::/39
  - [Loyalsoldier China CIDR] d471ee60d283  IP-CIDR,124.20.32.0/19
  - [Loyalsoldier China CIDR] e21607e0650a  IP-CIDR,103.116.150.0/24
  - [Loyalsoldier China CIDR] e2fa3caf83f1  IP-CIDR6,2406:840:fd68::/48
  - [Loyalsoldier China CIDR] e4307db075c0  IP-CIDR6,2406:840:e0e8::/45
  - [Loyalsoldier China CIDR] eb7b20acda57  IP-CIDR6,2406:840:fd78::/48
  - [Loyalsoldier China CIDR] ece66ecb9303  IP-CIDR,43.239.179.0/24
  - [Loyalsoldier China CIDR] eeedabed1c0f  IP-CIDR6,2402:8260::/32
  - [Loyalsoldier China CIDR] ef6f85f9144e  IP-CIDR6,2406:840:9976::/48
  - [Loyalsoldier China CIDR] efcea301227d  IP-CIDR,123.49.196.0/22
  - [Loyalsoldier China CIDR] f18096d7a15e  IP-CIDR,122.14.128.0/20
  - [Loyalsoldier China CIDR] fb25eb56def0  IP-CIDR,59.153.168.0/21
  - [Loyalsoldier China CIDR] ff2e6fd96275  IP-CIDR,122.8.52.0/22
```

## Speedtest.list

**Added: 121** (showing first 100)
```
  + [SukkaW Speedtest Servers International] 02b7b422882f  DOMAIN,speedtest.sentco.net
  + [SukkaW Speedtest Servers International] 02d48045e4e3  DOMAIN,speed12.gonetspeed.com
  + [SukkaW Speedtest Servers International] 04df25e28545  DOMAIN,speedtest.premieronline.net
  + [SukkaW Speedtest Servers International] 078081ad0b3d  DOMAIN,speedtest.rfnow.net
  + [SukkaW Speedtest Servers International] 12ca2bed9dbb  DOMAIN,speedtest.atccomm.net
  + [SukkaW Speedtest Servers International] 1303e426ad0f  DOMAIN,speed-pd.dispaisy.systems
  + [SukkaW Speedtest Servers International] 13dc2485ab95  DOMAIN,speedtest.heartofiowa.coop
  + [SukkaW Speedtest Servers International] 14696c5e4444  DOMAIN,speedtest.cmltelephone.com
  + [SukkaW Speedtest Servers International] 1599cf0b34d9  DOMAIN,fetml1.seed.net.tw
  + [SukkaW Speedtest Servers International] 189c17014e83  DOMAIN,speedtest.amesiaaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 1cfb48abbf36  DOMAIN,speedtest.grm.net
  + [SukkaW Speedtest Servers International] 1df38b0ae240  DOMAIN,speedtest1.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 1e9ede2ea46b  DOMAIN,speedtest.westianet.com
  + [SukkaW Speedtest Servers International] 2785a4313085  DOMAIN,teste.suprainternet.com.br
  + [SukkaW Speedtest Servers International] 2ab9b0da9911  DOMAIN,lcrs-speedtest-02.brightspeed.com
  + [SukkaW Speedtest Servers International] 304d2683e43f  DOMAIN,speedtest.skywaveconnect.com
  + [SukkaW Speedtest Servers International] 32b355be6336  DOMAIN,speedtest.bluevalley.net
  + [SukkaW Speedtest Servers International] 34d320d8b02f  DOMAIN,speedtest.mdtc.net
  + [SukkaW Speedtest Servers International] 3a92209ad6ba  DOMAIN,speedtest-01.omnitel.biz
  + [SukkaW Speedtest Servers International] 3a97abf4595c  DOMAIN,speedtest1.oma.nxlink.com
  + [SukkaW Speedtest Servers International] 3b0dc040ff61  DOMAIN,speed.nutelecom.com
  + [SukkaW Speedtest Servers International] 3f2a1255658c  DOMAIN,blfd-speed-01.gpcom.com
  + [SukkaW Speedtest Servers International] 3f7075e220a1  DOMAIN,ksczks-speedtest-ookla-01.st.charter.com
  + [SukkaW Speedtest Servers International] 3f8306542a0b  DOMAIN,stsudburywireless.rogers.com
  + [SukkaW Speedtest Servers International] 41bc4d2333e5  DOMAIN,speedtest.cvalley.net
  + [SukkaW Speedtest Servers International] 45ed5f3bd479  DOMAIN,speedtest.tcaexpress.net
  + [SukkaW Speedtest Servers International] 45f4d00908d6  DOMAIN,speedtest-2.hynetwifi.it
  + [SukkaW Speedtest Servers International] 48e2d32a2895  DOMAIN,speedtest.cascadecomm.com
  + [SukkaW Speedtest Servers International] 4bbf2a0a0fa3  DOMAIN,speedtest.mysmbs.com
  + [SukkaW Speedtest Servers International] 4bc2ef4606ca  DOMAIN,st-oma-1.binary.net
  + [SukkaW Speedtest Servers International] 4c8fd6b2f3f6  DOMAIN,ookla-ks.mercuryfiber.com
  + [SukkaW Speedtest Servers International] 4cdddfe9358b  DOMAIN,sp1.jdmbroadband.com
  + [SukkaW Speedtest Servers International] 4db3cbb342cd  DOMAIN,speedtest-lenexa.resoundnetworks.com
  + [SukkaW Speedtest Servers International] 507325cf0478  DOMAIN,speedtest.merlin.mb.ca
  + [SukkaW Speedtest Servers International] 50b8b3905b2f  DOMAIN,speedtest.absenterprises.co.in
  + [SukkaW Speedtest Servers International] 5180d71261b9  DOMAIN,speedtest.pimcommcorp.com
  + [SukkaW Speedtest Servers International] 52d0a6f0b307  DOMAIN,speedtest.45networks.ca
  + [SukkaW Speedtest Servers International] 565ea387b1e5  DOMAIN,speedtest.cfu.net
  + [SukkaW Speedtest Servers International] 56e9dda42623  DOMAIN,speedteste.netfast.com.br
  + [SukkaW Speedtest Servers International] 58e6d169adef  DOMAIN,speedtest.esu5.org
  + [SukkaW Speedtest Servers International] 59f0ec25e179  DOMAIN,blar-speed-01.gpcom.com
  + [SukkaW Speedtest Servers International] 5f3fcd920887  DOMAIN,speedtest.ncn.net
  + [SukkaW Speedtest Servers International] 605cfb35f522  DOMAIN,speedtest.mci.as1003.net
  + [SukkaW Speedtest Servers International] 6fbf06a1c59f  DOMAIN,speedtest.hynetwifi.it
  + [SukkaW Speedtest Servers International] 6ff5941eb406  DOMAIN,exc-speedtest.unitedfiber.com
  + [SukkaW Speedtest Servers International] 761a11540f93  DOMAIN,siouxcity1.cabospeed.com
  + [SukkaW Speedtest Servers International] 7666539d8d51  DOMAIN,speedtest2.valleyfiber.ca
  + [SukkaW Speedtest Servers International] 78d6268a6297  DOMAIN,speedtest.didimnet.com.tr
  + [SukkaW Speedtest Servers International] 7935cf977efe  DOMAIN,speedtest.wwfn.ca
  + [SukkaW Speedtest Servers International] 7a4042ca0d6f  DOMAIN,stbarriewireless.rogers.com
  + [SukkaW Speedtest Servers International] 7a55e968bb85  DOMAIN,speedtest.unitedfiber.com
  + [SukkaW Speedtest Servers International] 7ad78e8435d7  DOMAIN,speed.ddbroadband.co.in
  + [SukkaW Speedtest Servers International] 7bdc14806a7c  DOMAIN,speedtest.wccta.com
  + [SukkaW Speedtest Servers International] 7ea92d713139  DOMAIN,speedtest.rochmnaa.metronetinc.com
  + [SukkaW Speedtest Servers International] 7f1d4cde7674  DOMAIN,speedtest.net360.cloud
  + [SukkaW Speedtest Servers International] 809ed12ed910  DOMAIN,speedtest.nemr.net
  + [SukkaW Speedtest Servers International] 84b8446a854b  DOMAIN,speedtest10g.ics-llc.net
  + [SukkaW Speedtest Servers International] 86f4178b9153  DOMAIN,speedtest.fibercomm.net
  + [SukkaW Speedtest Servers International] 8c9d7c03fa30  DOMAIN,speedtest27.suddenlink.net
  + [SukkaW Speedtest Servers International] 8cfc393702b7  DOMAIN,speedtest.kc2.everfastfiber.com
  + [SukkaW Speedtest Servers International] 905125f73ee5  DOMAIN,speedtest.mvec.com
  + [SukkaW Speedtest Servers International] 9052a64cc3fd  DOMAIN,speedtest25.wiatel.com
  + [SukkaW Speedtest Servers International] 9073adefc65d  DOMAIN,speedtest.neitel.net
  + [SukkaW Speedtest Servers International] 93617c692bd8  DOMAIN,ookla.mci-1.serverforge.org
  + [SukkaW Speedtest Servers International] 991108b39981  DOMAIN,speedtest.mtctech.net
  + [SukkaW Speedtest Servers International] 99246723a229  DOMAIN,speedtest-mci-01.pdx.net.uk
  + [SukkaW Speedtest Servers International] 9be25423b741  DOMAIN,servidor.speedplay.com.br
  + [SukkaW Speedtest Servers International] 9cbc5181b52f  DOMAIN,speedtest.ddps.jp
  + [SukkaW Speedtest Servers International] 9fc768aebccf  DOMAIN,speedtest.nexgencom.com
  + [SukkaW Speedtest Servers International] a03e396de9e0  DOMAIN,mib-rst-sp1.mibroadband.com
  + [SukkaW Speedtest Servers International] a0e06516e4c5  DOMAIN,speedtest2.rainbowtel.net
  + [SukkaW Speedtest Servers International] a258e2019d32  DOMAIN,sp1.voyageurinternet.ca
  + [SukkaW Speedtest Servers International] a63f83296451  DOMAIN,speed.tritan-bb.net
  + [SukkaW Speedtest Servers International] a64508c249b0  DOMAIN,lnk-speedtest.networknebraska.net
  + [SukkaW Speedtest Servers International] a6619de300c2  DOMAIN,st2a.les.net
  + [SukkaW Speedtest Servers International] ab415fae2613  DOMAIN,speedtest.longlines.com
  + [SukkaW Speedtest Servers International] accaab45f3ac  DOMAIN,speedtest-dsm.cowboyhosting.com
  + [SukkaW Speedtest Servers International] acefb905644c  DOMAIN,seednet-hc1.seed.net.tw
  + [SukkaW Speedtest Servers International] adbebc476e13  DOMAIN,speedtest.unlimitednet.us
  + [SukkaW Speedtest Servers International] aecf28573fd6  DOMAIN,speedtest.heartlandtechnology.com
  + [SukkaW Speedtest Servers International] b7cba41d7626  DOMAIN,speedtest1.dsm1.ippathways.net
  + [SukkaW Speedtest Servers International] b8a0e7029ee0  DOMAIN,stosat-indp-01.sys.comcast.net
  + [SukkaW Speedtest Servers International] bb37aed618a1  DOMAIN,speedtest.waterloofiber.com
  + [SukkaW Speedtest Servers International] bfafedcf989a  DOMAIN,iola-st-ookla.kwikom.com
  + [SukkaW Speedtest Servers International] c0ba82f0fb9d  DOMAIN,vanspeedtest.altimatel.com
  + [SukkaW Speedtest Servers International] c2222406ebe9  DOMAIN,speedtest.palmerone.com
  + [SukkaW Speedtest Servers International] c56b34c86c50  DOMAIN,stwinnipegwireless.rogers.com
  + [SukkaW Speedtest Servers International] c65d0fb54ff1  DOMAIN,speedtest-central.eastlink.ca
  + [SukkaW Speedtest Servers International] c7316104a7b2  DOMAIN,speedtest.cltel.com
  + [SukkaW Speedtest Servers International] cb0ed23687a9  DOMAIN,speed.kansas.smishcraft.com
  + [SukkaW Speedtest Servers International] cce8869a397d  DOMAIN,speedtest3a.socket.net
  + [SukkaW Speedtest Servers International] cf1403b737c5  DOMAIN,speedtest1.acentek.net
  + [SukkaW Speedtest Servers International] cf8895c26ec0  DOMAIN,lnk11-speedtest01.as15108.com
  + [SukkaW Speedtest Servers International] d3bf9a607d1e  DOMAIN,speedtest-kc.conexonconnect.com
  + [SukkaW Speedtest Servers International] d735e6630f0c  DOMAIN,seednet-ntp2.seed.net.tw
  + [SukkaW Speedtest Servers International] d7ef6a964002  DOMAIN,speedtest01.imon.net
  + [SukkaW Speedtest Servers International] d8fca8393d99  DOMAIN,us-central1-c.gcp.spd.synthesis.health
  + [SukkaW Speedtest Servers International] d9a6af3b3da3  DOMAIN,speedtest.fortdodgefiber.net
  + [SukkaW Speedtest Servers International] db82d40a73a2  DOMAIN,speedtest2-kc.kanren.net
  + [SukkaW Speedtest Servers International] e05fce41365e  DOMAIN,cmrn-speedtest-02.brightspeed.com
  ... and 21 more
```

**Removed: 75** (showing first 75)
```
  - [SukkaW Speedtest Servers International] 0009d45cc71f  DOMAIN,speedtest-gdrp.merit.edu
  - [SukkaW Speedtest Servers International] 0561b044089c  DOMAIN,ran-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 06cad1c28a6c  DOMAIN,speedtest.aabroadband.in
  - [SukkaW Speedtest Servers International] 0711f9d6046b  DOMAIN,cbpuspeed.aspensmart.net
  - [SukkaW Speedtest Servers International] 0811cb3546c0  DOMAIN,stwellandpelhamwireless.rogers.com
  - [SukkaW Speedtest Servers International] 0f0435a45fac  DOMAIN,speedtest.oa.net
  - [SukkaW Speedtest Servers International] 0f923e75457a  DOMAIN,ookla-in.mercuryfiber.com
  - [SukkaW Speedtest Servers International] 134564537572  DOMAIN,speedtest.sycmilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 15ee8e1a505a  DOMAIN,speedtest.volo.net
  - [SukkaW Speedtest Servers International] 1753c7265a8d  DOMAIN,st1.ligtel.com
  - [SukkaW Speedtest Servers International] 22e17aa36c22  DOMAIN,speedtest-wc.truestreamfiber.us
  - [SukkaW Speedtest Servers International] 269efd4a6679  DOMAIN,stosat-rvlt-01.sys.comcast.net
  - [SukkaW Speedtest Servers International] 27aa9cef1e30  DOMAIN,bytp-speedtest-1.123.net
  - [SukkaW Speedtest Servers International] 2a475faf88d3  DOMAIN,spdtst-southbend.fourway.net
  - [SukkaW Speedtest Servers International] 2b911d71aa37  DOMAIN,speedtest.i3broadband.com
  - [SukkaW Speedtest Servers International] 2c4e9bf40557  DOMAIN,velocity.softtelecom.net.br
  - [SukkaW Speedtest Servers International] 30afe4b85368  DOMAIN,speedtest.chi.gigenet.com
  - [SukkaW Speedtest Servers International] 31e8ffa70b1a  DOMAIN,speedtest.pnb.vodafoneidea.com
  - [SukkaW Speedtest Servers International] 34ed756fe9e2  DOMAIN,speedtest2.mfbroadband.com
  - [SukkaW Speedtest Servers International] 4243e89e8727  DOMAIN,speedtest.tcom.purdue.edu
  - [SukkaW Speedtest Servers International] 4491b544431a  DOMAIN,speedtest.as53597.net
  - [SukkaW Speedtest Servers International] 49f2fe815df7  DOMAIN,speed.markham.telmax.ca
  - [SukkaW Speedtest Servers International] 4a3866e24ddd  DOMAIN,min-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 4b114200a609  DOMAIN,speedtest.cirbn.net
  - [SukkaW Speedtest Servers International] 4ca06efd9c0c  DOMAIN,speedtest-srv-a.homeworks.org
  - [SukkaW Speedtest Servers International] 4ef30d7df14c  DOMAIN,speedtest.bltnilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 5423fa711e1c  DOMAIN,sul-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  - [SukkaW Speedtest Servers International] 5b59c5167680  DOMAIN,sqaookla.ddns.net
  - [SukkaW Speedtest Servers International] 5b6c9723716c  DOMAIN,speedtest.syd.netsg.net.au
  - [SukkaW Speedtest Servers International] 5cb71d1b2142  DOMAIN,pri-r450-speedtest.metrocomm.com
  - [SukkaW Speedtest Servers International] 5ea0d4b206fe  DOMAIN,speedtest2.acentek.net
  - [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  - [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  - [SukkaW Speedtest Servers International] 631ceedda77e  DOMAIN,speed.mei.net
  - [SukkaW Speedtest Servers International] 6ab9d9e27f4c  DOMAIN,speedtest.connectjasper.com
  - [SukkaW Speedtest Servers International] 6aead9c0f08f  DOMAIN,testmyspeed.urbancom.net
  - [SukkaW Speedtest Servers International] 6ba54f697247  DOMAIN,randomlake-speedtest1.as36001.net
  - [SukkaW Speedtest Servers International] 6bd3e7deffb5  DOMAIN,st-kenosha.sumofiber.com
  - [SukkaW Speedtest Servers International] 70b5747c0d2b  DOMAIN,speedtest3nl.quickqc.nl
  - [SukkaW Speedtest Servers International] 7180f9019e99  DOMAIN,speedtest.springcom.com
  - [SukkaW Speedtest Servers International] 72bb8c1b570f  DOMAIN,speedtest5.windtre.it
  - [SukkaW Speedtest Servers International] 794da782a134  DOMAIN,ookla-mispeed.rackgenius.com
  - [SukkaW Speedtest Servers International] 7d204e853068  DOMAIN,speedtest.oswgilaa.metronetinc.com
  - [SukkaW Speedtest Servers International] 856a8514303c  DOMAIN,speedtest.btc-bci.com
  - [SukkaW Speedtest Servers International] 890fa3aca5ec  DOMAIN,speedtest.orixinet.com.br
  - [SukkaW Speedtest Servers International] 8c8abdf2d7dc  DOMAIN,speed.weendeavor.com
  - [SukkaW Speedtest Servers International] 8d2554d731e3  DOMAIN,st1.stratusnet.com
  - [SukkaW Speedtest Servers International] 945b9be2fb40  DOMAIN,aldlmi-speedtest-ookla-01.st.charter.com
  - [SukkaW Speedtest Servers International] 96e261bbbb9d  DOMAIN,speed.tnahosting.net
  - [SukkaW Speedtest Servers International] 9bf7f0647b9f  DOMAIN,speedtest.duocast.net
  - [SukkaW Speedtest Servers International] 9d2342e15aaa  DOMAIN,stkingcity.netcrawler.ca
  - [SukkaW Speedtest Servers International] 9ef50333ec52  DOMAIN,speedtestmoh1.airtelbroadband.in
  - [SukkaW Speedtest Servers International] a1b9d99a6b53  DOMAIN,speedtestus.pvdatanet.com
  - [SukkaW Speedtest Servers International] a2002b5b2805  DOMAIN,speedtest.grr1-mi.incx.net
  - [SukkaW Speedtest Servers International] a5a39e69aa44  DOMAIN,speedtest.mhtc.net
  - [SukkaW Speedtest Servers International] ae22d7a42288  DOMAIN,speedtest.supranet.net
  - [SukkaW Speedtest Servers International] b03528f13ca1  DOMAIN,speedtest.marshallfibernet.com
  - [SukkaW Speedtest Servers International] b73df15da330  DOMAIN,stetobicoke.netcrawler.ca
  - [SukkaW Speedtest Servers International] b8610cd69e74  DOMAIN,speed.lordnet.net
  - [SukkaW Speedtest Servers International] b989fde83935  DOMAIN,st1.digitalglobe.it
  - [SukkaW Speedtest Servers International] c06caa39a296  DOMAIN,speedtest.lagrangeremcisp.net
  - [SukkaW Speedtest Servers International] c48494526129  DOMAIN,speedtest3.point-broadband.com
  - [SukkaW Speedtest Servers International] c7730d38d8d7  DOMAIN,speedtest001.bfinetworks.com
  - [SukkaW Speedtest Servers International] c95a22664ae8  DOMAIN,speedtest.kraus.jbarbieri.net
  - [SukkaW Speedtest Servers International] d0b106fcb347  DOMAIN,speedtest2.il.mycci.net
  - [SukkaW Speedtest Servers International] d47fe5fd7010  DOMAIN,speedtest-obd.redeconecta.com
  - [SukkaW Speedtest Servers International] d77254c621cc  DOMAIN,speedtest3.myninestar.net
  - [SukkaW Speedtest Servers International] e41fcdf67e6f  DOMAIN,speedtest.bemol.com.br
  - [SukkaW Speedtest Servers International] e7f15789e6d0  DOMAIN,speedtest.taylor.edu
  - [SukkaW Speedtest Servers International] ea0071580a1d  DOMAIN,speedtest.heartland-fiber.com
  - [SukkaW Speedtest Servers International] eacb466cdf37  DOMAIN,kzspeedtest01.aunalytics.com
  - [SukkaW Speedtest Servers International] ec01ae8210c3  DOMAIN,speedtest.zivlinaa.metronetinc.com
  - [SukkaW Speedtest Servers International] ec456ca1f360  DOMAIN,speedtest1.ctstelecom.com
  - [SukkaW Speedtest Servers International] f2367bf1b8eb  DOMAIN,stvaughan.rogers.com
```
