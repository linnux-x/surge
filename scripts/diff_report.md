# Surge Rule Diff Report
Generated: 2026-10-09T05:02:20.328895

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 47 |
| Rules removed | 14 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| CDN.list | 29 | 30 | +1 | -0 | ~0 |
| China_IP.list | 11510 | 11509 | +0 | -1 | ~0 |
| Download.list | 1694 | 1695 | +1 | -0 | ~0 |
| Global.list | 24364 | 24391 | +27 | -0 | ~0 |
| Speedtest.list | 1679 | 1684 | +18 | -13 | ~0 |

## CDN.list

**Added: 1** (showing first 1)
```
  + [SukkaW CDN] b28668ed791b  DOMAIN-WILDCARD,rum-ingest.*.signalfx.com
```

## China_IP.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 China IPs] c84dcaf98027  IP-CIDR,103.144.244.0/23
```

## Download.list

**Added: 1** (showing first 1)
```
  + [SukkaW Download] b77d489d4fc1  DOMAIN,releases.claude.com
```

## Global.list

**Added: 27** (showing first 27)
```
  + [blackmatrix7 Global] 019fb00e275d  DOMAIN-SUFFIX,csc.com.tw
  + [blackmatrix7 Global] 0c78eac744cd  DOMAIN-SUFFIX,eximbank.com.tw
  + [blackmatrix7 Global] 161495c48359  DOMAIN-SUFFIX,hanimeone.me
  + [blackmatrix7 Global] 21475448cb05  DOMAIN-SUFFIX,dh.net
  + [blackmatrix7 Global] 22d5cf86298a  DOMAIN-SUFFIX,nationthailand.com
  + [blackmatrix7 Global] 2ccbd0ee89ab  DOMAIN-SUFFIX,ttl.com.tw
  + [blackmatrix7 Global] 39c631f533c0  DOMAIN-SUFFIX,matichon.co.th
  + [blackmatrix7 Global] 58a2c0da52b1  DOMAIN-SUFFIX,aidc.com.tw
  + [blackmatrix7 Global] 593786a69ee5  DOMAIN-SUFFIX,cangku.moe
  + [blackmatrix7 Global] 59b2ac654f19  DOMAIN-SUFFIX,rocmgov.org
  + [blackmatrix7 Global] 6adff2eac69f  DOMAIN-SUFFIX,cpc.com.tw
  + [blackmatrix7 Global] 73958cb9dee2  DOMAIN-SUFFIX,icdf.org.tw
  + [blackmatrix7 Global] 8d017a8c22a3  DOMAIN-SUFFIX,vscc.org.tw
  + [blackmatrix7 Global] 8defe3000ac1  DOMAIN-SUFFIX,mirdc.org.tw
  + [blackmatrix7 Global] 8e9a8a3376ea  DOMAIN-SUFFIX,khc.edu.tw
  + [blackmatrix7 Global] 919e2d97a32d  DOMAIN-SUFFIX,hanime1.com
  + [blackmatrix7 Global] 9a849ab2edb7  DOMAIN-SUFFIX,poland.tw
  + [blackmatrix7 Global] a3c76b8c9404  DOMAIN-SUFFIX,javchu.com
  + [blackmatrix7 Global] a5ca4279d050  DOMAIN-SUFFIX,xx.net
  + [blackmatrix7 Global] ba11adbfb041  DOMAIN-SUFFIX,tfd.org.tw
  + [blackmatrix7 Global] c065045e93af  DOMAIN-SUFFIX,tybio.com.tw
  + [blackmatrix7 Global] c42f1db3bb0d  DOMAIN-SUFFIX,nstc.org.tw
  + [blackmatrix7 Global] d8795b9e4f9b  DOMAIN-SUFFIX,ipac.global
  + [blackmatrix7 Global] dedbe846e7f6  DOMAIN-SUFFIX,blue-plus.net
  + [blackmatrix7 Global] e74275efa566  DOMAIN-SUFFIX,twfhcsec.com.tw
  + [blackmatrix7 Global] fad29c86197c  DOMAIN-SUFFIX,landbank.com.tw
  + [blackmatrix7 Global] fb068e021653  DOMAIN-SUFFIX,moeli-desu.com
```

## Speedtest.list

**Added: 18** (showing first 18)
```
  + [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  + [SukkaW Speedtest Servers International] 1c1d5c307d85  DOMAIN,nl.itdatatelecom.ro
  + [SukkaW Speedtest Servers International] 25cf64244b53  DOMAIN,speedtest.dacomfibra.com
  + [SukkaW Speedtest Servers International] 29b41f696150  DOMAIN,speedtest.xxlnet.nl
  + [SukkaW Speedtest Servers International] 48f59ad9b4a6  DOMAIN,speedtest.mum.vodafoneidea.com
  + [SukkaW Speedtest Servers International] 6382a86a4d91  DOMAIN,speed.telcomnetwork.net
  + [SukkaW Speedtest Servers International] 89d9c6207c68  DOMAIN,speedtest.nwlab.org
  + [SukkaW Speedtest Servers International] 9ef50333ec52  DOMAIN,speedtestmoh1.airtelbroadband.in
  + [SukkaW Speedtest Servers International] a8249c53ba8a  DOMAIN,speedtest.thn.uk.syntura.io
  + [SukkaW Speedtest Servers International] ad7927355047  DOMAIN,speedtest-lon1.elite.net.uk
  + [SukkaW Speedtest Servers International] afce71228313  DOMAIN,topnet.brsserver.com.br
  + [SukkaW Speedtest Servers International] bd3e66b0c432  DOMAIN,ookla.fibraleste.com.br
  + [SukkaW Speedtest Servers International] cb103aa8b7a1  DOMAIN,speedtest010.telecomitalia.it
  + [SukkaW Speedtest Servers International] d013141bb6ce  DOMAIN,wrlcc.synology.me
  + [SukkaW Speedtest Servers International] d980d4d61909  DOMAIN,imrteixeira.brsserver.com.br
  + [SukkaW Speedtest Servers International] eacb466cdf37  DOMAIN,kzspeedtest01.aunalytics.com
  + [SukkaW Speedtest Servers International] f67a07aca883  DOMAIN,qspt.technofiber.net
  + [SukkaW Speedtest Servers International] f99d165584ae  DOMAIN,ookla.devitalia.it
```

**Removed: 13** (showing first 13)
```
  - [SukkaW Speedtest Servers International] 04035c8d3237  DOMAIN,speedtest.sonepat.softechinfosol.com
  - [SukkaW Speedtest Servers International] 0578ed72ddf9  DOMAIN,speedtest-1.keyubu.com
  - [SukkaW Speedtest Servers International] 2ddb34614d29  DOMAIN,speedtest2.digimobil.es
  - [SukkaW Speedtest Servers International] 4055c8ae0867  DOMAIN,speedtest.hk210.hkg.cn.ctcsci.com
  - [SukkaW Speedtest Servers International] 6fbf06a1c59f  DOMAIN,speedtest.hynetwifi.it
  - [SukkaW Speedtest Servers International] 826511526ca4  DOMAIN,hiztesti2.ondiso.io
  - [SukkaW Speedtest Servers International] 8772dc923cf5  DOMAIN,speed-mix.dispaisy.systems
  - [SukkaW Speedtest Servers International] 8c8abdf2d7dc  DOMAIN,speed.weendeavor.com
  - [SukkaW Speedtest Servers International] bbccfc3e3b0e  DOMAIN,speedtest.matrixtelecon.com.br
  - [SukkaW Speedtest Servers International] c851b7d78393  DOMAIN,purtel39.purtel.com
  - [SukkaW Speedtest Servers International] f44b573b95ed  DOMAIN,velocidade.phinfortelecom.com.br
  - [SukkaW Speedtest Servers International] f790bbddbc94  DOMAIN,speed.cable-giant.com.tw
  - [SukkaW Speedtest Servers International] ff97ee6115e9  DOMAIN,btestmcp.vocetelecom.vc
```
