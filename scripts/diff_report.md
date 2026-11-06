# Surge Rule Diff Report
Generated: 2026-11-07T05:02:13.867880

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 2 |
| Rules added | 72 |
| Rules removed | 96 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China_IP.list | 9662 | 9647 | +47 | -62 | ~0 |
| Speedtest.list | 1717 | 1708 | +25 | -34 | ~0 |

## China_IP.list

**Added: 47** (showing first 47)
```
  + [Loyalsoldier China CIDR] 078540775f91  IP-CIDR,124.21.160.0/19
  + [Loyalsoldier China CIDR] 0bf9d7080e36  IP-CIDR,124.21.208.0/20
  + [Loyalsoldier China CIDR] 0d363900fbf6  IP-CIDR,124.21.144.0/20
  + [Loyalsoldier China CIDR] 0e43f3a8305f  IP-CIDR,103.115.19.0/24
  + [Loyalsoldier China CIDR] 181ad1b5690a  IP-CIDR6,2406:840:ff20::/43
  + [Loyalsoldier China CIDR] 193fdffca9e0  IP-CIDR,124.20.64.0/19
  + [Loyalsoldier China CIDR] 19cdb102106c  IP-CIDR,124.21.224.0/19
  + [Loyalsoldier China CIDR] 206e90f2a20a  IP-CIDR,163.223.216.0/24
  + [Loyalsoldier China CIDR] 24b301586587  IP-CIDR,151.158.123.0/24
  + [Loyalsoldier China CIDR] 2a01002b5ec7  IP-CIDR,124.20.240.0/20
  + [Loyalsoldier China CIDR] 300385b26f2f  IP-CIDR,59.107.0.0/16
  + [Loyalsoldier China CIDR] 36e0afc144a8  IP-CIDR,95.82.8.0/23
  + [Loyalsoldier China CIDR] 46df95fd2698  IP-CIDR6,2406:840:ff80::/41
  + [Loyalsoldier China CIDR] 4815755cca3f  IP-CIDR,122.0.224.0/20
  + [Loyalsoldier China CIDR] 511026d3f575  IP-CIDR,211.149.44.0/22
  + [Loyalsoldier China CIDR] 5b1828c6b0b1  IP-CIDR6,2400:3f60::/32
  + [Loyalsoldier China CIDR] 5d5f0beeab5e  IP-CIDR,122.0.160.0/19
  + [Loyalsoldier China CIDR] 618774bc96d5  IP-CIDR,124.20.192.0/19
  + [Loyalsoldier China CIDR] 68b397f32db9  IP-CIDR,124.21.80.0/20
  + [Loyalsoldier China CIDR] 6b02d611855f  IP-CIDR,8.168.0.0/14
  + [Loyalsoldier China CIDR] 6cdb3cc33a31  IP-CIDR6,2a06:9801:20::/48
  + [Loyalsoldier China CIDR] 74ed651fa01f  IP-CIDR6,2405:6c0:1::/48
  + [Loyalsoldier China CIDR] 813b6b0d981f  IP-CIDR,124.20.96.0/20
  + [Loyalsoldier China CIDR] 8372704c1c61  IP-CIDR,178.236.38.0/23
  + [Loyalsoldier China CIDR] 8387c53d522f  IP-CIDR,103.177.136.0/24
  + [Loyalsoldier China CIDR] 8a9f4994f2e0  IP-CIDR6,2406:840:c02::/47
  + [Loyalsoldier China CIDR] 8c949b6c2b86  IP-CIDR,124.21.96.0/19
  + [Loyalsoldier China CIDR] 8cbd3b8ae176  IP-CIDR6,2406:840:e270::/45
  + [Loyalsoldier China CIDR] 8f6fe5d1a185  IP-CIDR,178.236.233.0/24
  + [Loyalsoldier China CIDR] 948170ddf5ea  IP-CIDR6,2406:840:9970::/44
  + [Loyalsoldier China CIDR] 95f0eae0020c  IP-CIDR,223.123.205.0/24
  + [Loyalsoldier China CIDR] a2bc400280e8  IP-CIDR6,2403:6380:36::/47
  + [Loyalsoldier China CIDR] a6148d4bee83  IP-CIDR6,2406:840:feff::/48
  + [Loyalsoldier China CIDR] ac3f837b684c  IP-CIDR,58.66.0.0/15
  + [Loyalsoldier China CIDR] acd3fd98f2dd  IP-CIDR,223.123.206.0/23
  + [Loyalsoldier China CIDR] b0c9cb51e173  IP-CIDR,124.20.128.0/18
  + [Loyalsoldier China CIDR] b9c6c14bbe4f  IP-CIDR,122.0.192.0/19
  + [Loyalsoldier China CIDR] d471ee60d283  IP-CIDR,124.20.32.0/19
  + [Loyalsoldier China CIDR] dce370e615cc  IP-CIDR,218.30.40.0/21
  + [Loyalsoldier China CIDR] dd9b29723b5c  IP-CIDR,211.102.144.0/20
  + [Loyalsoldier China CIDR] de1e716e741c  IP-CIDR,124.172.0.0/14
  + [Loyalsoldier China CIDR] e0a816dcf28e  IP-CIDR6,2406:840:8000::/36
  + [Loyalsoldier China CIDR] e4307db075c0  IP-CIDR6,2406:840:e0e8::/45
  + [Loyalsoldier China CIDR] e4cb18afb105  IP-CIDR6,2406:840:ff40::/42
  + [Loyalsoldier China CIDR] e63a50b6f9f0  IP-CIDR,178.236.237.0/24
  + [Loyalsoldier China CIDR] f415780c10d4  IP-CIDR,223.123.176.0/21
  + [Loyalsoldier China CIDR] fc85503132c6  IP-CIDR,140.210.17.0/24
```

**Removed: 62** (showing first 62)
```
  - [Loyalsoldier China CIDR] 0a50f1a38f5e  IP-CIDR6,2400:3f60:200::/39
  - [Loyalsoldier China CIDR] 1375834f087f  IP-CIDR,124.173.64.0/18
  - [Loyalsoldier China CIDR] 14783780ad0f  IP-CIDR6,2406:840:c03::/48
  - [Loyalsoldier China CIDR] 1a7e9f27f37d  IP-CIDR,211.102.144.0/21
  - [Loyalsoldier China CIDR] 21d671bde19d  IP-CIDR6,2406:840:e272::/47
  - [Loyalsoldier China CIDR] 282a570a5ca1  IP-CIDR,122.0.128.0/17
  - [Loyalsoldier China CIDR] 2e238cfb12ba  IP-CIDR6,2400:3f60:1000::/36
  - [Loyalsoldier China CIDR] 35365212d52b  IP-CIDR6,2406:840:e0ea::/47
  - [Loyalsoldier China CIDR] 36126d447e1e  IP-CIDR6,2400:3f60:400::/38
  - [Loyalsoldier China CIDR] 3a6cf89a29f9  IP-CIDR6,2400:3f60:800::/37
  - [Loyalsoldier China CIDR] 3affd6d5cb0c  IP-CIDR,124.172.88.0/23
  - [Loyalsoldier China CIDR] 3ede32f0ef24  IP-CIDR6,2400:3f60:20::/43
  - [Loyalsoldier China CIDR] 444ddf610bb8  IP-CIDR,124.21.64.0/18
  - [Loyalsoldier China CIDR] 48244bc12953  IP-CIDR6,2400:3f60:8000::/33
  - [Loyalsoldier China CIDR] 49f3ae300b96  IP-CIDR6,2406:840:9974::/47
  - [Loyalsoldier China CIDR] 4b334904e64b  IP-CIDR,59.107.255.0/24
  - [Loyalsoldier China CIDR] 4e2243746e8d  IP-CIDR,124.172.128.0/17
  - [Loyalsoldier China CIDR] 54286f76142e  IP-CIDR6,2400:3f60:6::/47
  - [Loyalsoldier China CIDR] 658727c33551  IP-CIDR6,2400:3f60:4000::/34
  - [Loyalsoldier China CIDR] 65d970822da5  IP-CIDR6,2406:840:ff00::/40
  - [Loyalsoldier China CIDR] 6896b2180baf  IP-CIDR6,2400:3f60:40::/42
  - [Loyalsoldier China CIDR] 6927fc09f6ff  IP-CIDR,140.210.16.0/23
  - [Loyalsoldier China CIDR] 6ab0698e1b24  IP-CIDR,59.107.0.0/17
  - [Loyalsoldier China CIDR] 707d4ff082d3  IP-CIDR6,2406:840:9978::/45
  - [Loyalsoldier China CIDR] 7ea066325970  IP-CIDR6,2400:3f60:80::/41
  - [Loyalsoldier China CIDR] 83678ef1b033  IP-CIDR,218.30.46.0/23
  - [Loyalsoldier China CIDR] 888248bcba33  IP-CIDR,124.172.87.0/24
  - [Loyalsoldier China CIDR] 89052b3d23fc  IP-CIDR6,2400:3f60:2000::/35
  - [Loyalsoldier China CIDR] 89cdfe90c1b0  IP-CIDR6,2406:840:8200::/39
  - [Loyalsoldier China CIDR] 8b0c837fd2bf  IP-CIDR6,2406:840:8400::/38
  - [Loyalsoldier China CIDR] 8bed670d5cab  IP-CIDR,218.30.45.0/24
  - [Loyalsoldier China CIDR] 8e5faa50dc62  IP-CIDR6,2400:3f60:13::/48
  - [Loyalsoldier China CIDR] 8eb60d0b4997  IP-CIDR,151.158.122.0/23
  - [Loyalsoldier China CIDR] 8f197cdbaa65  IP-CIDR,124.172.91.0/24
  - [Loyalsoldier China CIDR] 9297b22162c5  IP-CIDR6,2403:6380:34::/46
  - [Loyalsoldier China CIDR] 938c19c6e338  IP-CIDR,124.21.128.0/17
  - [Loyalsoldier China CIDR] 97c210ec304f  IP-CIDR,124.20.0.0/16
  - [Loyalsoldier China CIDR] 9e065e06bfba  IP-CIDR,223.123.204.0/22
  - [Loyalsoldier China CIDR] a126ee9813a5  IP-CIDR6,2406:840:e271::/48
  - [Loyalsoldier China CIDR] a31992d4b93c  IP-CIDR,58.67.128.0/17
  - [Loyalsoldier China CIDR] aaaaa79eb195  IP-CIDR6,2406:840:9970::/46
  - [Loyalsoldier China CIDR] acc7cf2e8726  IP-CIDR,124.172.93.0/24
  - [Loyalsoldier China CIDR] aee22715672a  IP-CIDR6,2400:3f60:8::/45
  - [Loyalsoldier China CIDR] b24a577ccc82  IP-CIDR,124.174.0.0/15
  - [Loyalsoldier China CIDR] b40c6898caf5  IP-CIDR6,2406:840:e0e9::/48
  - [Loyalsoldier China CIDR] bb5024669c07  IP-CIDR6,2400:3f60:5::/48
  - [Loyalsoldier China CIDR] c18b944084ab  IP-CIDR,103.118.210.0/23
  - [Loyalsoldier China CIDR] c38fb4e7a22f  IP-CIDR6,2406:840:8800::/37
  - [Loyalsoldier China CIDR] cd756de0cc1f  IP-CIDR6,2400:3f60:18::/45
  - [Loyalsoldier China CIDR] d12057752693  IP-CIDR,59.107.226.0/24
  - [Loyalsoldier China CIDR] d9a81a14e06c  IP-CIDR,8.168.0.0/15
  - [Loyalsoldier China CIDR] dcbcbe983883  IP-CIDR,218.30.40.0/22
  - [Loyalsoldier China CIDR] df083bc46ea7  IP-CIDR,124.173.205.0/24
  - [Loyalsoldier China CIDR] df287917cc7f  IP-CIDR6,2400:3f60:14::/46
  - [Loyalsoldier China CIDR] e55a04398d21  IP-CIDR,206.109.71.0/24
  - [Loyalsoldier China CIDR] e8da74a8eb94  IP-CIDR6,2400:3f60::/46
  - [Loyalsoldier China CIDR] ec17aacd9d08  IP-CIDR6,2400:3f60:100::/40
  - [Loyalsoldier China CIDR] ec5fb9fb99c5  IP-CIDR,124.173.128.0/18
  - [Loyalsoldier China CIDR] ef6f85f9144e  IP-CIDR6,2406:840:9976::/48
  - [Loyalsoldier China CIDR] f8c1e13a0ee9  IP-CIDR6,2406:840:e0ec::/46
  - [Loyalsoldier China CIDR] fbfa977876e8  IP-CIDR6,2406:840:8000::/40
  - [Loyalsoldier China CIDR] fd40264f0743  IP-CIDR6,2406:840:e274::/46
```

## Speedtest.list

**Added: 25** (showing first 25)
```
  + [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  + [SukkaW Speedtest Servers International] 201eccf0042e  DOMAIN,speedtest.dreamnetgigafiber.com
  + [SukkaW Speedtest Servers International] 36366555a5b5  DOMAIN,ookla.mu.as6453.net
  + [SukkaW Speedtest Servers International] 404e271d98c9  DOMAIN,speedtest1-phnyazjv.as20055.net
  + [SukkaW Speedtest Servers International] 43c9e647d2a9  DOMAIN,speedtest-adelaide.optusnet.com.au
  + [SukkaW Speedtest Servers International] 48547dce691f  DOMAIN,speedtest.rtm.t-mobile.nl
  + [SukkaW Speedtest Servers International] 6382a86a4d91  DOMAIN,speed.telcomnetwork.net
  + [SukkaW Speedtest Servers International] 7737d7921c63  DOMAIN,sp2.semfronteiras.net.br
  + [SukkaW Speedtest Servers International] 83d43cf9e206  DOMAIN,spd01-adl.au.superloop.com
  + [SukkaW Speedtest Servers International] 8b40d9ed9e30  DOMAIN,speedtestvlc.zafirotelecom.com
  + [SukkaW Speedtest Servers International] 8edae2065263  DOMAIN,speedtest2.honeybroadband.com
  + [SukkaW Speedtest Servers International] 8f062e512925  DOMAIN,speedtestsonipat.kkdbroadband.co.in
  + [SukkaW Speedtest Servers International] 91f667018cba  DOMAIN,speedtestfe.stel.it
  + [SukkaW Speedtest Servers International] 99d636115e4d  DOMAIN,speedtest.kdatacenter.com
  + [SukkaW Speedtest Servers International] a9914783cc20  DOMAIN,speedtest-din.rapidnet.co.in
  + [SukkaW Speedtest Servers International] adc92f2f9e63  DOMAIN,speedtest-1.apvinvestimenti.it
  + [SukkaW Speedtest Servers International] aef5e069d6f5  DOMAIN,ooklaserver.dlls.tx.ogital.net
  + [SukkaW Speedtest Servers International] ba48de7cf518  DOMAIN,speedtestve1.telecomitalia.it
  + [SukkaW Speedtest Servers International] baf9b1ccd504  DOMAIN,speed.airmaxbroadband.com
  + [SukkaW Speedtest Servers International] c8ac7b0a4421  DOMAIN,nms.bhrbroadband.com
  + [SukkaW Speedtest Servers International] da91fee54771  DOMAIN,speedtest31.turk.net
  + [SukkaW Speedtest Servers International] de6f094d3a37  DOMAIN,speedtest-1.manchester.network.as212655.net
  + [SukkaW Speedtest Servers International] eaa8b55eb335  DOMAIN,speedtest.telecaravaca.com
  + [SukkaW Speedtest Servers International] f72a70c92ec0  DOMAIN,speedtest.4isp.it
  + [SukkaW Speedtest Servers International] fd46d06e06ef  DOMAIN,qoeookla-seat-01.sys.comcast.net
```

**Removed: 34** (showing first 34)
```
  - [SukkaW Speedtest Servers International] 0d59b329464a  DOMAIN,speedtestshriganganagar.777network.net
  - [SukkaW Speedtest Servers International] 1741f4b2f889  DOMAIN,speed1.spitfireuk.net
  - [SukkaW Speedtest Servers International] 43f75ae5aa25  DOMAIN,speedtest.telbo.net
  - [SukkaW Speedtest Servers International] 46d4a0bcb050  DOMAIN,speedtest.miplhr.com
  - [SukkaW Speedtest Servers International] 4b2bec89b1bd  DOMAIN,speedtest.vacastelecom.net
  - [SukkaW Speedtest Servers International] 4cdddfe9358b  DOMAIN,sp1.jdmbroadband.com
  - [SukkaW Speedtest Servers International] 4d3968c87aec  DOMAIN,stintl.ospot.in
  - [SukkaW Speedtest Servers International] 5b3a88dbb571  DOMAIN,speedtestmera.vs.mythic-beasts.com
  - [SukkaW Speedtest Servers International] 5b6c9723716c  DOMAIN,speedtest.syd.netsg.net.au
  - [SukkaW Speedtest Servers International] 622740dd56c6  DOMAIN,stmontreal.netcrawler.ca
  - [SukkaW Speedtest Servers International] 626849c0a751  DOMAIN,st1.worldfibernet.com
  - [SukkaW Speedtest Servers International] 684a67fa6607  DOMAIN,speedtest.lucas.company
  - [SukkaW Speedtest Servers International] 699e0d05d032  DOMAIN,speedtest.nl.novoserve.com
  - [SukkaW Speedtest Servers International] 6a6f44221018  DOMAIN,txg-speedtest.infinirc.com
  - [SukkaW Speedtest Servers International] 83686b01d39b  DOMAIN,speedtest-pd.flynet.it
  - [SukkaW Speedtest Servers International] 95587bfbecca  DOMAIN,speedtest.crystalclearnetwork.co.in
  - [SukkaW Speedtest Servers International] 99050f480dac  DOMAIN,speedtest.flynet.it
  - [SukkaW Speedtest Servers International] 9ba53f21e73d  DOMAIN,speedtest.vodafone.it
  - [SukkaW Speedtest Servers International] a2df120d65aa  DOMAIN,speedtest.willaegis.in
  - [SukkaW Speedtest Servers International] a91aa2354179  DOMAIN,fibertest.soipl.co.in
  - [SukkaW Speedtest Servers International] b80d74e1e5b7  DOMAIN,speed.giganet.com.tr
  - [SukkaW Speedtest Servers International] c1ddb625657f  DOMAIN,ookla.apuacom.it
  - [SukkaW Speedtest Servers International] c94b51e1691c  DOMAIN,str.seyfert.in
  - [SukkaW Speedtest Servers International] d599d4ae986c  DOMAIN,speedtest.rpworld.co.in
  - [SukkaW Speedtest Servers International] d61fe183473e  DOMAIN,testdebitpublic.vialis.net
  - [SukkaW Speedtest Servers International] de0bab9a4272  DOMAIN,phoenixim-speedtest.commnetbroadband.com
  - [SukkaW Speedtest Servers International] ecc3d65b919e  DOMAIN,ns2.peer.net.in
  - [SukkaW Speedtest Servers International] ee88b39fc599  DOMAIN,speedtest.impactusnet.net.br
  - [SukkaW Speedtest Servers International] f018ba0720a8  DOMAIN,testdebit.vialis.net
  - [SukkaW Speedtest Servers International] f1eebe03ec88  DOMAIN,speedtest.correggio.netandwork.net
  - [SukkaW Speedtest Servers International] f4777355d914  DOMAIN,speedtest1.co-fi.es
  - [SukkaW Speedtest Servers International] f70d1c340eec  DOMAIN,izmit-speed.tbtnet.com.tr
  - [SukkaW Speedtest Servers International] f9afc6861226  DOMAIN,speedtestsk.airjaldi.net
  - [SukkaW Speedtest Servers International] ffab702885b4  DOMAIN,speedtest.witcom.cloud
```
