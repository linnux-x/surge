# Surge Rule Diff Report
Generated: 2026-11-22T17:06:41.893367

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 27 |
| Rules removed | 53 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| CDN.list | 31 | 32 | +21 | -20 | ~0 |
| China.list | 110664 | 110664 | +0 | -0 | ~1 |
| Global.list | 24652 | 24625 | +6 | -33 | ~0 |

## CDN.list

**Added: 21** (showing first 21)
```
  + [Manual Rules] 011195f4b467  DOMAIN-WILDCARD,*-cdn.eporner.com
  + [Manual Rules] 0ef90856a50d  DOMAIN-WILDCARD,*-res.cloudinary.com
  + [Manual Rules] 2bfe727c782d  DOMAIN,cdn.signalfx.com
  + [Manual Rules] 50bc2d32b20f  DOMAIN,cdn.trustpilot.net
  + [Manual Rules] 55dbb353791a  DOMAIN,static.trustpilot.com
  + [Manual Rules] 5de1dd7f5cef  DOMAIN-WILDCARD,*-thumbs.worldsex.com
  + [Manual Rules] 67d4a664b4b4  DOMAIN,assets.trustpilot.net
  + [Manual Rules] 6f034ad2a04b  DOMAIN,cdnjs.cloudflare.com
  + [Manual Rules] 76a8fd6df672  DOMAIN,scripts.trustpilot.com
  + [Manual Rules] 77d1ad0b2e71  DOMAIN,images.trustpilot.com
  + [Manual Rules] 8db0fd8720ee  DOMAIN,esm.run
  + [Manual Rules] 8e13224f1db1  DOMAIN-WILDCARD,*-thumbs.pornhost.com
  + [Manual Rules] ad724a0b0631  DOMAIN,cdn.observability.splunkcloud.com
  + [Manual Rules] baa46d43cd06  DOMAIN,web-assets.zendesk.com
  + [Manual Rules] c2dd64f3b8d4  DOMAIN,res.cloudinary.com
  + [Manual Rules] c8036a6b7ef1  DOMAIN,static.zdassets.com
  + [Manual Rules] cbd1aa7dbfd0  DOMAIN-WILDCARD,*-assets.worldsex.com
  + [Manual Rules] d5bac6c9c58b  DOMAIN,cdn.adultempire.com
  + [Manual Rules] ddc68c70ebcf  DOMAIN,assets.zendesk.com
  + [Manual Rules] f349930e8a57  DOMAIN,images.trustpilot.net
  + [Manual Rules] f62d952fae1b  DOMAIN-WILDCARD,*vod-adaptive.akamaized.net
```

**Removed: 20** (showing first 20)
```
  - [SukkaW CDN] 072823502153  DOMAIN-KEYWORD,scripts.trustpilot.com
  - [SukkaW CDN] 1b41adb53c3f  DOMAIN-KEYWORD,web-assets.zendesk
  - [SukkaW CDN] 36a9bfde01dc  DOMAIN-KEYWORD,images.trustpilot.com
  - [SukkaW CDN] 3ad31346eb51  DOMAIN-WILDCARD,cdn.*.dmm.co.jp
  - [SukkaW CDN] 3c3bcb6111cb  DOMAIN-KEYWORD,cdn.trustpilot.net
  - [SukkaW CDN] 3f6236a0d7bc  DOMAIN-KEYWORD,vod-adaptive.akamaized.net
  - [SukkaW CDN] 5b289e32b16d  DOMAIN-KEYWORD,-cdn.eporner.com
  - [SukkaW CDN] 5f2d6d392282  DOMAIN-KEYWORD,-thumbs.pornhost.com
  - [SukkaW CDN] 840292ed5b7e  DOMAIN-KEYWORD,-assets.dmm.co.jp
  - [SukkaW CDN] a1f0899f899f  DOMAIN-KEYWORD,-res.cloudinary.com
  - [SukkaW CDN] ae75a9271dc4  DOMAIN-KEYWORD,dsn.algolia.net
  - [SukkaW CDN] b28668ed791b  DOMAIN-WILDCARD,rum-ingest.*.signalfx.com
  - [SukkaW CDN] cc7d471c332a  DOMAIN-KEYWORD,-images.disco-api.com
  - [SukkaW CDN] d32d436c9bfa  DOMAIN-KEYWORD,static.trustpilot.com
  - [SukkaW CDN] daedc7693708  DOMAIN-KEYWORD,99avcdn
  - [SukkaW CDN] df6a96fceb77  DOMAIN-KEYWORD,-assets.worldsex.com
  - [SukkaW CDN] e2362183e816  DOMAIN-KEYWORD,-thumbs.worldsex.com
  - [SukkaW CDN] e54ab9f514dc  DOMAIN-KEYWORD,cdn.adultempire.com
  - [SukkaW CDN] ed456503e3a6  DOMAIN-KEYWORD,images.trustpilot.net
  - [SukkaW CDN] fd09997cde97  DOMAIN-KEYWORD,assets.trustpilot.net
```

## China.list

**Source changed: 1**
```
  ~ 53867080ef6c: [blackmatrix7 ChinaMaxNoIP Domain → Manual Rules]
```

## Global.list

**Added: 6** (showing first 6)
```
  + [Manual Rules] 3dd4448916d7  AND,((DOMAIN-SUFFIX,samsung.com),(NOT,((DOMAIN-SUFFIX,support-cn.samsung.com))))
  + [Manual Rules] 78b56aa32ffa  DOMAIN-SUFFIX,observability.splunkcloud.com
  + [Manual Rules] 7a0093b8d8ff  DOMAIN-SUFFIX,algolianet.com
  + [Manual Rules] a04f365940ee  DOMAIN-SUFFIX,algolianet.net
  + [Manual Rules] f8994ce14d80  DOMAIN-SUFFIX,signalfx.com
  + [Manual Rules] fe8ff5859ba9  DOMAIN-SUFFIX,algolia.net
```

**Removed: 33** (showing first 33)
```
  - [blackmatrix7 Global] 166c570679e2  DOMAIN-KEYWORD,dlercloud
  - [blackmatrix7 Global] 198334c38af5  IP-CIDR,220.181.174.34/32,no-resolve
  - [blackmatrix7 Global] 22a2f1a3d720  USER-AGENT,battleroyale*
  - [blackmatrix7 Global] 390968e3deba  IP-CIDR,180.163.150.162/32,no-resolve
  - [blackmatrix7 Global] 3976487e8c9a  IP-CIDR,120.253.253.226/32,no-resolve
  - [blackmatrix7 Global] 40b8c9b65f22  DOMAIN-KEYWORD,telegram
  - [blackmatrix7 Global] 411905b527a6  DOMAIN-KEYWORD,twimg
  - [blackmatrix7 Global] 43bf12c382bd  DOMAIN-SUFFIX,samsung.com
  - [blackmatrix7 Global] 50f6377d7b93  IP-CIDR,120.253.255.98/32,no-resolve
  - [blackmatrix7 Global] 68f1ea2abcdc  IP-CIDR,120.232.181.162/32,no-resolve
  - [blackmatrix7 Global] 6a969a1320ae  DOMAIN-SUFFIX,gouhuo.qq.com
  - [blackmatrix7 Global] 7326ffd7bdb8  DOMAIN-KEYWORD,dropbox
  - [blackmatrix7 Global] 747c02eaac2e  DOMAIN-KEYWORD,1e100
  - [blackmatrix7 Global] 83df1e86b55a  IP-CIDR,120.253.255.162/32,no-resolve
  - [blackmatrix7 Global] 8dbe42df2679  DOMAIN-KEYWORD,abema
  - [blackmatrix7 Global] 8e057bbaa44a  USER-AGENT,WhatsApp*
  - [blackmatrix7 Global] 9aeed80f57b2  IP-CIDR,180.163.151.162/32,no-resolve
  - [blackmatrix7 Global] a2c05805d4ae  IP-CIDR6,2001:b28:f23c::/47,no-resolve
  - [blackmatrix7 Global] aebb8f790cb8  IP-CIDR,120.241.147.226/32,no-resolve
  - [blackmatrix7 Global] b2613e738c98  IP-CIDR,180.163.151.34/32,no-resolve
  - [blackmatrix7 Global] b268ab5f93b9  IP-CIDR,220.181.174.226/32,no-resolve
  - [blackmatrix7 Global] c015fc82b571  DOMAIN-KEYWORD,wikileaks
  - [blackmatrix7 Global] c7d32587de1b  IP-CIDR,120.253.255.34/32,no-resolve
  - [blackmatrix7 Global] ca6b0ac05563  DOMAIN-KEYWORD,sci-hub
  - [blackmatrix7 Global] d2afdd5780cf  USER-AGENT,Duolingo*
  - [blackmatrix7 Global] f00e17bcb0ee  IP-CIDR,220.181.174.162/32,no-resolve
  - [blackmatrix7 Global] f01c8aa716f1  DOMAIN-KEYWORD,beetalk
  - [blackmatrix7 Global] f32b519641c9  USER-AGENT,Roam*
  - [blackmatrix7 Global] f6dc15ff3cfa  USER-AGENT,TwDramas
  - [blackmatrix7 Global] f8cb43c325db  DOMAIN-KEYWORD,appledaily
  - [blackmatrix7 Global] f95908b5788d  IP-CIDR,17.252.156.0/23,no-resolve
  - [blackmatrix7 Global] fc14c3596273  IP-CIDR,180.163.150.34/32,no-resolve
  - [blackmatrix7 Global] fcc6f525ef7a  DOMAIN-KEYWORD,pinterest
```
