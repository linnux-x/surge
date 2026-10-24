# Surge Rule Diff Report
Generated: 2026-10-25T05:01:46.989162

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 94 |
| Rules removed | 26 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110567 | 110569 | +2 | -0 | ~0 |
| China_IP.list | 11847 | 11850 | +6 | -3 | ~0 |
| Game.list | 557 | 572 | +15 | -0 | ~0 |
| Global.list | 24501 | 24549 | +51 | -3 | ~0 |
| Speedtest.list | 1721 | 1721 | +20 | -20 | ~0 |

## China.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 0beb4e68aca8  DOMAIN-SUFFIX,szu.app
  + [blackmatrix7 ChinaMaxNoIP Domain] 661e38c6264c  DOMAIN-SUFFIX,szu.moe
```

## China_IP.list

**Added: 6** (showing first 6)
```
  + [Loyalsoldier China CIDR] 2f48e72c65d7  IP-CIDR6,2406:840:a08::/45
  + [Loyalsoldier China CIDR] 49686a4afad0  IP-CIDR6,2406:840:a04::/46
  + [Loyalsoldier China CIDR] 6a882ad91609  IP-CIDR6,2406:840:a02::/47
  + [Loyalsoldier China CIDR] 8cf19744f406  IP-CIDR,103.189.197.0/24
  + [Loyalsoldier China CIDR] a238b5194cfd  IP-CIDR6,2406:840:a01::/48
  + [blackmatrix7 China IPs] b2fae35d1872  IP-CIDR,202.92.4.0/22
```

**Removed: 3** (showing first 3)
```
  - [blackmatrix7 China IPs] 5120e1427596  IP-CIDR6,2406:840:a00::/44
  - [blackmatrix7 China IPs] 756ea1a9855b  IP-CIDR6,2804:1e48:9002::/48
  - [blackmatrix7 China IPs] d2e2b66553d4  IP-CIDR6,2620:57:4004::/47
```

## Game.list

**Added: 15** (showing first 15)
```
  + [blackmatrix7 Game] 0dc6272e2320  IP-CIDR,146.66.152.0/24,no-resolve
  + [blackmatrix7 Game] 22eb9ee5ae32  DOMAIN-SUFFIX,steamconnecttest.com
  + [blackmatrix7 Game] 29b7fbdd84ba  IP-CIDR,185.25.180.0/22,no-resolve
  + [blackmatrix7 Game] 2dddd9622b49  DOMAIN-SUFFIX,valve.net
  + [blackmatrix7 Game] 541605214e11  IP-CIDR,155.133.224.0/19,no-resolve
  + [blackmatrix7 Game] 5e7fe3b2cc45  IP-CIDR,205.196.6.0/24,no-resolve
  + [blackmatrix7 Game] 799f9bd518cd  IP-CIDR,192.69.96.0/22,no-resolve
  + [blackmatrix7 Game] 89543d081621  IP-CIDR,146.66.155.0/24,no-resolve
  + [blackmatrix7 Game] 90e9864b280a  IP-CIDR,208.78.164.0/22,no-resolve
  + [blackmatrix7 Game] ae25ae664de9  IP-CIDR,103.28.54.0/24,no-resolve
  + [blackmatrix7 Game] af3f950dd1ca  IP-CIDR,208.64.200.0/22,no-resolve
  + [blackmatrix7 Game] b60c386ae7cd  IP-CIDR,45.121.184.0/24,no-resolve
  + [blackmatrix7 Game] be4594037c2d  IP-CIDR,103.10.124.0/23,no-resolve
  + [blackmatrix7 Game] c91db11d8bbf  DOMAIN-SUFFIX,dota2.com
  + [blackmatrix7 Game] fa94b9481a02  IP-CIDR,162.254.192.0/21,no-resolve
```

## Global.list

**Added: 51** (showing first 51)
```
  + [blackmatrix7 Global] 01716db95003  DOMAIN-SUFFIX,mts-link.ru
  + [blackmatrix7 Global] 17539c1e8a11  DOMAIN-SUFFIX,claude.app
  + [blackmatrix7 Global] 1dc81100773e  DOMAIN-SUFFIX,kurs.expert
  + [blackmatrix7 Global] 1f69942d4d82  DOMAIN-SUFFIX,delets.cash
  + [blackmatrix7 Global] 2a339b017ad3  DOMAIN-SUFFIX,fluxer.app
  + [blackmatrix7 Global] 31be7c314ca5  DOMAIN-SUFFIX,blockchair.com
  + [blackmatrix7 Global] 326e37c0b5c9  DOMAIN-SUFFIX,thunderstore.org
  + [blackmatrix7 Global] 33b9b586341e  DOMAIN-SUFFIX,glitchprod.com
  + [blackmatrix7 Global] 37bab4576af1  DOMAIN-SUFFIX,r2modman.com
  + [blackmatrix7 Global] 3a2ac9daf1c4  DOMAIN-SUFFIX,tgtime.store
  + [blackmatrix7 Global] 3cf405f136f0  DOMAIN-SUFFIX,makeship.com
  + [blackmatrix7 Global] 44780cd58bac  DOMAIN-SUFFIX,avito.com
  + [blackmatrix7 Global] 4755e13b1ec8  DOMAIN-SUFFIX,thunderstore.io
  + [blackmatrix7 Global] 4b3491a1725d  DOMAIN-SUFFIX,ant.dev
  + [blackmatrix7 Global] 4e5ffac971f7  DOMAIN-SUFFIX,24.place
  + [blackmatrix7 Global] 520ff39e1655  DOMAIN-SUFFIX,youtooz.com
  + [blackmatrix7 Global] 54dd096e0300  DOMAIN-SUFFIX,fluxer.media
  + [blackmatrix7 Global] 58892081deec  DOMAIN-SUFFIX,fluxer.gift
  + [blackmatrix7 Global] 595e4f906856  DOMAIN-SUFFIX,fluxer.gg
  + [blackmatrix7 Global] 596e72bfc3fa  DOMAIN-SUFFIX,tmimgcdn.com
  + [blackmatrix7 Global] 5d56f5c04432  DOMAIN-SUFFIX,worldofwarships.asia
  + [blackmatrix7 Global] 62e2c669c0ad  DOMAIN-SUFFIX,ownaj.com
  + [blackmatrix7 Global] 6679657a0f98  DOMAIN-SUFFIX,postman.com
  + [blackmatrix7 Global] 6977721987e6  DOMAIN-SUFFIX,glitchproductions.store
  + [blackmatrix7 Global] 6ffb7a5a5e56  DOMAIN-SUFFIX,fluxer.tools
  + [blackmatrix7 Global] 7c5a019f1cba  DOMAIN-SUFFIX,craftifyx.com
  + [blackmatrix7 Global] 7e93d3ffdc92  DOMAIN-SUFFIX,fluxerstatus.com
  + [blackmatrix7 Global] 8f91e9035389  DOMAIN-SUFFIX,fluxerusercontent.com
  + [blackmatrix7 Global] 9464ee13b59d  DOMAIN-SUFFIX,chatbotclaude.com
  + [blackmatrix7 Global] 95db48fd44c2  DOMAIN-SUFFIX,fluxerstatic.com
  + [blackmatrix7 Global] 9e0c06d6cebc  DOMAIN-SUFFIX,fluxerapp.com
  + [blackmatrix7 Global] 9e49db6e06dc  DOMAIN-SUFFIX,anthropic.team
  + [blackmatrix7 Global] 9e938dc5c9c2  DOMAIN-SUFFIX,antspace.dev
  + [blackmatrix7 Global] a48406c13b84  DOMAIN-SUFFIX,getsafety.com
  + [blackmatrix7 Global] afc9b5b725ff  DOMAIN-SUFFIX,blockchair.net
  + [blackmatrix7 Global] b849525a4e78  DOMAIN-SUFFIX,claudeacademy.com
  + [blackmatrix7 Global] b91e0a4f7036  DOMAIN-SUFFIX,steamos.cloud
  + [blackmatrix7 Global] b9b9b7f4d5f1  DOMAIN-SUFFIX,cryptoid.info
  + [blackmatrix7 Global] bde927d4d8f4  DOMAIN-SUFFIX,claude.site
  + [blackmatrix7 Global] be438016a88f  DOMAIN-SUFFIX,avito.tech
  + [blackmatrix7 Global] c37c28a8bf4f  DOMAIN-SUFFIX,funko.com
  + [blackmatrix7 Global] c892b656fb03  DOMAIN-SUFFIX,gamebanana.com
  + [blackmatrix7 Global] d1cc30b16fd2  DOMAIN-SUFFIX,fluxer.dev
  + [blackmatrix7 Global] d28539aeacfb  DOMAIN-SUFFIX,safetycli.com
  + [blackmatrix7 Global] d37d92eaaf15  DOMAIN-SUFFIX,claudepages.dev
  + [blackmatrix7 Global] e5a203127750  DOMAIN-SUFFIX,claude.new
  + [blackmatrix7 Global] e698c655d4d8  DOMAIN-SUFFIX,pyup.io
  + [blackmatrix7 Global] e6b18e67eefa  DOMAIN-SUFFIX,magnific.com
  + [blackmatrix7 Global] ec8dcbe65712  DOMAIN-SUFFIX,claudestudio.com
  + [blackmatrix7 Global] f8efd3034c59  DOMAIN-SUFFIX,fluxer.com
  + [blackmatrix7 Global] ff8d72f0e776  DOMAIN-SUFFIX,fanfiction.net
```

**Removed: 3** (showing first 3)
```
  - [blackmatrix7 Global] 22eb9ee5ae32  DOMAIN-SUFFIX,steamconnecttest.com
  - [blackmatrix7 Global] 2dddd9622b49  DOMAIN-SUFFIX,valve.net
  - [blackmatrix7 Global] c91db11d8bbf  DOMAIN-SUFFIX,dota2.com
```

## Speedtest.list

**Added: 20** (showing first 20)
```
  + [SukkaW Speedtest Servers International] 09ea1f14ec9f  DOMAIN,ooklatins.redeconexaonet.com
  + [SukkaW Speedtest Servers International] 1303e426ad0f  DOMAIN,speed-pd.dispaisy.systems
  + [SukkaW Speedtest Servers International] 175aff7a92bb  DOMAIN,speedbng.n-tel.in
  + [SukkaW Speedtest Servers International] 29b41f696150  DOMAIN,speedtest.xxlnet.nl
  + [SukkaW Speedtest Servers International] 3307fbfaba51  DOMAIN,st3.surajnetwork.com
  + [SukkaW Speedtest Servers International] 36b91e77e572  DOMAIN,st34ata.netspeed.tr
  + [SukkaW Speedtest Servers International] 41d750ea2dcd  DOMAIN,speedtest.jvswifi.com.br
  + [SukkaW Speedtest Servers International] 52603f0438ce  DOMAIN,speedtest-geelong.optusnet.com.au
  + [SukkaW Speedtest Servers International] 5308f37ea9ca  DOMAIN,speedtest.thyrakles.de
  + [SukkaW Speedtest Servers International] 5b0b7c47633d  DOMAIN,sirsa.softechinfosol.com
  + [SukkaW Speedtest Servers International] 6ee345273f50  DOMAIN,ookla.lodestarnetworks.co.uk
  + [SukkaW Speedtest Servers International] 8fb9855a4808  DOMAIN,reikonteste.reikoninternet.com.br
  + [SukkaW Speedtest Servers International] 91dd7903cffa  DOMAIN,speedtest.conectaamazonia.com.br
  + [SukkaW Speedtest Servers International] 96692f154a26  DOMAIN,veloteste.mrjomar.com.br
  + [SukkaW Speedtest Servers International] 99050f480dac  DOMAIN,speedtest.flynet.it
  + [SukkaW Speedtest Servers International] 99d636115e4d  DOMAIN,speedtest.kdatacenter.com
  + [SukkaW Speedtest Servers International] a0e06516e4c5  DOMAIN,speedtest2.rainbowtel.net
  + [SukkaW Speedtest Servers International] b0a1806dd49f  DOMAIN,st1.anonet.in
  + [SukkaW Speedtest Servers International] d47fe5fd7010  DOMAIN,speedtest-obd.redeconecta.com
  + [SukkaW Speedtest Servers International] e1c9b22eab29  DOMAIN,speedtest.wnet.net.in
```

**Removed: 20** (showing first 20)
```
  - [SukkaW Speedtest Servers International] 0a21ac426b0c  DOMAIN,speedtest.octaplus.uk
  - [SukkaW Speedtest Servers International] 42a36a3fbaf2  DOMAIN,speed.megasyy.com
  - [SukkaW Speedtest Servers International] 6c0f5905df91  DOMAIN,speedmum.n-tel.in
  - [SukkaW Speedtest Servers International] 945f6dd36368  DOMAIN,velocimetro.smartmovel.net
  - [SukkaW Speedtest Servers International] a8249c53ba8a  DOMAIN,speedtest.thn.uk.syntura.io
  - [SukkaW Speedtest Servers International] aa2d41e1a749  DOMAIN,speedtest.infortectelecom.net.br
  - [SukkaW Speedtest Servers International] adc92f2f9e63  DOMAIN,speedtest-1.apvinvestimenti.it
  - [SukkaW Speedtest Servers International] aee975c2f9ab  DOMAIN,speedtest.sesfiber.com.br
  - [SukkaW Speedtest Servers International] afce71228313  DOMAIN,topnet.brsserver.com.br
  - [SukkaW Speedtest Servers International] b53cf08ac2c7  DOMAIN,ncc-speed.kbro.com.tw
  - [SukkaW Speedtest Servers International] ba48de7cf518  DOMAIN,speedtestve1.telecomitalia.it
  - [SukkaW Speedtest Servers International] c0e084187c09  DOMAIN,syd.speedtest.pttnz.net
  - [SukkaW Speedtest Servers International] cf8895c26ec0  DOMAIN,lnk11-speedtest01.as15108.com
  - [SukkaW Speedtest Servers International] d303e7e5e1a8  DOMAIN,speedtest10.haashnet.com
  - [SukkaW Speedtest Servers International] d980d4d61909  DOMAIN,imrteixeira.brsserver.com.br
  - [SukkaW Speedtest Servers International] dbeb82c9b2d7  DOMAIN,spdt.lanxus.com.br
  - [SukkaW Speedtest Servers International] f31da10a05fc  DOMAIN,speedtest.kappenhagen.tech
  - [SukkaW Speedtest Servers International] faeb8d45f2a1  DOMAIN,speedtest9200.sea.acsalaska.net
  - [SukkaW Speedtest Servers International] fb0c61831deb  DOMAIN,spdgnet.gnetserver.com.br
  - [SukkaW Speedtest Servers International] fc64f25abeb6  DOMAIN,speedtest.absolutevalidation.com
```
