# Surge Rule Diff Report
Generated: 2026-10-04T05:02:59.255631

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 82 |
| Rules removed | 22 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China_IP.list | 11455 | 11510 | +57 | -2 | ~1 |
| Global.list | 24356 | 24362 | +6 | -0 | ~0 |
| Speedtest.list | 1688 | 1687 | +19 | -20 | ~0 |

## China_IP.list

**Added: 57** (showing first 57)
```
  + [blackmatrix7 China IPs] 01b0fb9fbfae  IP-CIDR6,2406:840:9680:7000::/52
  + [blackmatrix7 China IPs] 07752163a9e9  IP-CIDR6,2406:840:9680:6680::/57
  + [Loyalsoldier China CIDR] 0d56b4424cf4  IP-CIDR6,2406:840:96a0::/43
  + [Loyalsoldier China CIDR] 135213383958  IP-CIDR6,2a04:3e00:1001::/48
  + [blackmatrix7 China IPs] 1604fdcca8aa  IP-CIDR6,2406:840:9680:4000::/51
  + [blackmatrix7 China IPs] 17e96b3b7938  IP-CIDR6,2406:840:9680:6664::/63
  + [Loyalsoldier China CIDR] 1aea7d16cea6  IP-CIDR6,2a04:3e00:1400::/38
  + [blackmatrix7 China IPs] 1c883f0fd934  IP-CIDR6,2406:840:9680::/50
  + [Loyalsoldier China CIDR] 249e7f4e9f21  IP-CIDR6,2a04:3e00:400::/38
  + [Loyalsoldier China CIDR] 279bf8045e2c  IP-CIDR6,2a04:3e04::/30
  + [Loyalsoldier China CIDR] 2e8b86b4ca34  IP-CIDR6,2406:840:9690::/44
  + [blackmatrix7 China IPs] 30de483cf060  IP-CIDR,14.241.232.0/21
  + [Loyalsoldier China CIDR] 331b0969c1ef  IP-CIDR6,2a04:3e00:1040::/42
  + [blackmatrix7 China IPs] 3c685924f4d7  IP-CIDR6,2406:840:9680:6668::/61
  + [Loyalsoldier China CIDR] 43b1174fb168  IP-CIDR6,2a04:3e00:100::/40
  + [Loyalsoldier China CIDR] 444d29c523bd  IP-CIDR6,2a04:3e01::/32
  + [Loyalsoldier China CIDR] 4569755040c0  IP-CIDR6,2a04:3e00:1020::/43
  + [Loyalsoldier China CIDR] 4cc2277dfe01  IP-CIDR6,2a04:3e00:40::/42
  + [Loyalsoldier China CIDR] 533149645279  IP-CIDR6,2a0a:d681:f000::/37
  + [Loyalsoldier China CIDR] 5ca5427cd203  IP-CIDR6,2a04:3e00:1800::/37
  + [blackmatrix7 China IPs] 5dcb082708d8  IP-CIDR6,2406:840:9680:6000::/54
  + [Loyalsoldier China CIDR] 6aa7ab968de4  IP-CIDR6,2406:840:96c0::/42
  + [Loyalsoldier China CIDR] 6b12502356de  IP-CIDR6,2a04:3e00:1004::/46
  + [Loyalsoldier China CIDR] 6df583a7b469  IP-CIDR6,2a04:3e00:4::/46
  + [Loyalsoldier China CIDR] 7453a2fae9e1  IP-CIDR6,2a04:3e00:1100::/40
  + [Loyalsoldier China CIDR] 74562868bd0d  IP-CIDR6,2a04:3e00::/48
  + [blackmatrix7 China IPs] 7649b4de6a65  IP-CIDR6,2406:840:9688::/45
  + [Loyalsoldier China CIDR] 777390bbf085  IP-CIDR6,2a04:3e00:1010::/44
  + [blackmatrix7 China IPs] 780ad99e726e  IP-CIDR6,2406:840:9680:6667::/64
  + [blackmatrix7 China IPs] 80493c3e0273  IP-CIDR6,2406:840:9680:6700::/56
  + [Loyalsoldier China CIDR] 82dcca257a57  IP-CIDR6,2a04:3e00:1008::/45
  + [Loyalsoldier China CIDR] 891a8a49163a  IP-CIDR6,2a04:3e00:10::/44
  + [blackmatrix7 China IPs] 989eaec1aa63  IP-CIDR6,2406:840:9680:6800::/53
  + [Loyalsoldier China CIDR] 9ca74a3c1957  IP-CIDR6,2a04:3e00:800::/37
  + [blackmatrix7 China IPs] a5f5f885140b  IP-CIDR6,2406:840:9682::/47
  + [blackmatrix7 China IPs] a6513d18679a  IP-CIDR6,2406:840:9684::/46
  + [Loyalsoldier China CIDR] a846a13871dd  IP-CIDR6,2a04:3e00:80::/41
  + [blackmatrix7 China IPs] a8f5cfd315d2  IP-CIDR6,2406:840:9681::/48
  + [blackmatrix7 China IPs] abd576d1a1fe  IP-CIDR6,2406:840:9680:6640::/59
  + [blackmatrix7 China IPs] ad320719fe03  IP-CIDR6,2406:840:9680:6670::/60
  + [Loyalsoldier China CIDR] aef31d6458ed  IP-CIDR6,2a04:3e00:2::/47
  + [Loyalsoldier China CIDR] b0f96462470f  IP-CIDR6,2a04:3e00:200::/39
  + [blackmatrix7 China IPs] b854dd28fe9f  IP-CIDR6,2406:840:9680:6660::/62
  + [Loyalsoldier China CIDR] b9dd62f0d130  IP-CIDR6,2a04:3e00:1200::/39
  + [Loyalsoldier China CIDR] c2ba86c44a29  IP-CIDR6,2a04:3e00:2000::/35
  + [Loyalsoldier China CIDR] d237213c8960  IP-CIDR6,2a04:3e00:4000::/34
  + [Loyalsoldier China CIDR] d2ac6cf9826a  IP-CIDR6,2a0a:d681:fe00::/40
  + [blackmatrix7 China IPs] d9033493db54  IP-CIDR6,2406:840:9680:6400::/55
  + [Loyalsoldier China CIDR] dea61f60a849  IP-CIDR6,2a04:3e02::/31
  + [Loyalsoldier China CIDR] e15ba727e697  IP-CIDR6,2a04:3e00:8000::/33
  + [blackmatrix7 China IPs] e6842284f494  IP-CIDR6,2406:840:9680:8000::/49
  + [Loyalsoldier China CIDR] e8575b7c40b2  IP-CIDR6,2a0a:d681:f800::/38
  + [Loyalsoldier China CIDR] ede026ca986f  IP-CIDR6,2a04:3e00:1080::/41
  + [Loyalsoldier China CIDR] eefb00750729  IP-CIDR,43.241.100.0/23
  + [blackmatrix7 China IPs] ef34af8fc09c  IP-CIDR6,2406:840:9680:6600::/58
  + [Loyalsoldier China CIDR] f11328cd05af  IP-CIDR6,2a04:3e00:20::/43
  + [Loyalsoldier China CIDR] f5b131bf9b10  IP-CIDR6,2a04:3e00:8::/45
```

**Removed: 2** (showing first 2)
```
  - [Loyalsoldier China CIDR] 499280bfe0bb  IP-CIDR6,2406:840:9680::/41
  - [Loyalsoldier China CIDR] 5a0bd930d660  IP-CIDR6,2a0a:d681:f000::/36
```

**Source changed: 1**
```
  ~ 25a3f0f271e6: [Loyalsoldier China CIDR → blackmatrix7 China IPs]
```

## Global.list

**Added: 6** (showing first 6)
```
  + [blackmatrix7 Global] 0f160f7335e0  DOMAIN-SUFFIX,claude.dev
  + [blackmatrix7 Global] 2ee8b7b89090  DOMAIN-SUFFIX,opencode.ai
  + [blackmatrix7 Global] 439e1b134721  DOMAIN-SUFFIX,huarun.win
  + [blackmatrix7 Global] 74e7e6fdf692  DOMAIN-SUFFIX,wikifunctions.org
  + [blackmatrix7 Global] dd2346c70e99  DOMAIN-SUFFIX,wikispecies.org
  + [blackmatrix7 Global] f7dd7ecfc3b4  DOMAIN-SUFFIX,fuyin116.com
```

## Speedtest.list

**Added: 19** (showing first 19)
```
  + [SukkaW Speedtest Servers International] 238c177c28d4  DOMAIN,speedtest.maisnetfibra.net.br
  + [SukkaW Speedtest Servers International] 3d35921f1642  DOMAIN,clg-105-sptest.ncri.com
  + [SukkaW Speedtest Servers International] 4bcc76af4fdd  DOMAIN,speedt-mi.lakenetworks.it
  + [SukkaW Speedtest Servers International] 568acf2b5a83  DOMAIN,hiztesti.turbo.net.tr
  + [SukkaW Speedtest Servers International] 626849c0a751  DOMAIN,st1.worldfibernet.com
  + [SukkaW Speedtest Servers International] 6c2e3496898f  DOMAIN,nets-mad01.servihosting.net
  + [SukkaW Speedtest Servers International] 73e08feba45a  DOMAIN,velocimetro-spt.akto.com.br
  + [SukkaW Speedtest Servers International] 7feb23edc139  DOMAIN,speedtest.datonofibra.com
  + [SukkaW Speedtest Servers International] 858932c61824  DOMAIN,speed.mylink.co.in
  + [SukkaW Speedtest Servers International] 8614924bdfcd  DOMAIN,speedtest.b3online.es
  + [SukkaW Speedtest Servers International] 92279113a24c  DOMAIN,speedtest-de1.expresshost.cloud
  + [SukkaW Speedtest Servers International] a4b1daa2001c  DOMAIN,speedtest33.turk.net
  + [SukkaW Speedtest Servers International] afce71228313  DOMAIN,topnet.brsserver.com.br
  + [SukkaW Speedtest Servers International] bc49f1117ac4  DOMAIN,teste.jsnet.manaus.br
  + [SukkaW Speedtest Servers International] c3109cd31fc9  DOMAIN,srv02-sjdm.imj-wanklik.com
  + [SukkaW Speedtest Servers International] c99064cf48cb  DOMAIN,speedtest-mel-dn1.empower.net.au
  + [SukkaW Speedtest] cc497076f552  DOMAIN-SUFFIX,speedtest.sg
  + [SukkaW Speedtest Servers International] d47fe5fd7010  DOMAIN,speedtest-obd.redeconecta.com
  + [SukkaW Speedtest Servers International] f58e87febab1  DOMAIN,speedtest-net-fra.dispaisy.systems
```

**Removed: 20** (showing first 20)
```
  - [SukkaW Speedtest Servers International] 0a1ed9cd71bb  DOMAIN,speedtest.cadence.net.uk
  - [SukkaW Speedtest Servers International] 0a22eed90fb5  DOMAIN,testdevelocidadval.jazztel.com
  - [SukkaW Speedtest Servers International] 0d69972a0124  DOMAIN,speedtest.netpool.in
  - [SukkaW Speedtest Servers International] 1a8877cf854f  DOMAIN,vel.cabralnet.com.br
  - [SukkaW Speedtest Servers International] 1b11c45002fb  DOMAIN,speedtest-rz.vsm.sh
  - [SukkaW Speedtest Servers International] 2ddb34614d29  DOMAIN,speedtest2.digimobil.es
  - [SukkaW Speedtest Servers International] 3459aa77ed16  DOMAIN,speedtest.macapatelecom.net.br
  - [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  - [SukkaW Speedtest Servers International] 5457b4c37fd0  DOMAIN,speedtest.uv.es
  - [SukkaW Speedtest Servers International] 5b59c5167680  DOMAIN,sqaookla.ddns.net
  - [SukkaW Speedtest Servers International] 6382a86a4d91  DOMAIN,speed.telcomnetwork.net
  - [SukkaW Speedtest Servers International] 6aafcc1f0064  DOMAIN,speedtest.americatelecom.net.br
  - [SukkaW Speedtest Servers International] 73112e9dc2cb  DOMAIN,speedtest01.adl1.spintel.net.au
  - [SukkaW Speedtest Servers International] 91f667018cba  DOMAIN,speedtestfe.stel.it
  - [SukkaW Speedtest Servers International] 98f59894be21  DOMAIN,speedtestjmu.airtel.in
  - [SukkaW Speedtest Servers International] b43cd8b37520  DOMAIN,speedtest01.ehtel.ca
  - [SukkaW Speedtest Servers International] b7eef275cf2a  DOMAIN,speedtest.jetair.net.in
  - [SukkaW Speedtest Servers International] efeb5fbe32e3  DOMAIN,speedtest.webturbo.net.br
  - [SukkaW Speedtest Servers International] f67a07aca883  DOMAIN,qspt.technofiber.net
  - [SukkaW Speedtest Servers International] fc64f25abeb6  DOMAIN,speedtest.absolutevalidation.com
```
