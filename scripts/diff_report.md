# Surge Rule Diff Report
Generated: 2026-11-23T09:17:11.677760

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 33 |
| Rules removed | 38 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Disney.list | 165 | 151 | +3 | -17 | ~0 |
| Global.list | 24648 | 24666 | +19 | -1 | ~0 |
| GlobalMedia.list | 2158 | 2153 | +9 | -14 | ~0 |
| Netflix.list | 31 | 28 | +1 | -4 | ~0 |
| Spotify.list | 30 | 29 | +1 | -2 | ~0 |

## Disney.list

**Added: 3** (showing first 3)
```
  + [Manual Rules] 075c1321a44d  DOMAIN-SUFFIX,registerdisney.go.com
  + [Manual Rules] db4822c89873  DOMAIN-SUFFIX,abc.go.com
  + [Manual Rules] ff86a3ff1520  DOMAIN-SUFFIX,espn.go.com
```

**Removed: 17** (showing first 17)
```
  - [blackmatrix7 Disney] 012cd74eb82a  DOMAIN-SUFFIX,abcnews.com
  - [blackmatrix7 Disney] 11b62698a902  DOMAIN-SUFFIX,hotstar-cdn.net
  - [blackmatrix7 Disney] 2a2bcb0868f2  DOMAIN-SUFFIX,marvel.com
  - [blackmatrix7 Disney] 2f84d4fa8900  DOMAIN-SUFFIX,disneycruisebrasil.com
  - [blackmatrix7 Disney] 3cd00a6d0988  DOMAIN-SUFFIX,thewaltdisneycompany.com
  - [blackmatrix7 Disney] 4a04c2846ddc  DOMAIN-SUFFIX,shops-disney.com
  - [blackmatrix7 Disney] 65bc2859fcf9  DOMAIN-SUFFIX,hotstar.com
  - [blackmatrix7 Disney] 6cedad3c2887  DOMAIN-SUFFIX,hotstarext.com
  - [blackmatrix7 Disney] 7cfd085f44a4  DOMAIN-SUFFIX,disneystore.com
  - [blackmatrix7 Disney] 82dfaa20c3c6  DOMAIN-SUFFIX,disneyworld-go.com
  - [blackmatrix7 Disney] 9880c9f7fac9  DOMAIN-SUFFIX,disneylandparis.com
  - [blackmatrix7 Disney] ae0c096b14ee  DOMAIN-SUFFIX,shopdisney.com
  - [blackmatrix7 Disney] b9289d990f46  DOMAIN-SUFFIX,go-disneyworldgo.com
  - [blackmatrix7 Disney] e0a044f5aabe  DOMAIN-SUFFIX,abcnews.edgesuite.net
  - [blackmatrix7 Disney] e473622036b6  DOMAIN-SUFFIX,hotstar-labs.com
  - [blackmatrix7 Disney] f7cf4449225c  DOMAIN-SUFFIX,go.com
  - [blackmatrix7 Disney] ffcb8be16f85  DOMAIN-SUFFIX,disneycareers.com
```

## Global.list

**Added: 19** (showing first 19)
```
  + [Manual Rules] 012cd74eb82a  DOMAIN-SUFFIX,abcnews.com
  + [Manual Rules] 0b6944d722d8  DOMAIN-SUFFIX,netflixstudios.com
  + [Manual Rules] 2a2bcb0868f2  DOMAIN-SUFFIX,marvel.com
  + [Manual Rules] 2f84d4fa8900  DOMAIN-SUFFIX,disneycruisebrasil.com
  + [Manual Rules] 3cd00a6d0988  DOMAIN-SUFFIX,thewaltdisneycompany.com
  + [Manual Rules] 4a04c2846ddc  DOMAIN-SUFFIX,shops-disney.com
  + [Manual Rules] 7cfd085f44a4  DOMAIN-SUFFIX,disneystore.com
  + [Manual Rules] 82dfaa20c3c6  DOMAIN-SUFFIX,disneyworld-go.com
  + [Manual Rules] 9880c9f7fac9  DOMAIN-SUFFIX,disneylandparis.com
  + [Manual Rules] a4cf7f444838  IP-CIDR,35.186.224.47/32,no-resolve
  + [Manual Rules] ae0c096b14ee  DOMAIN-SUFFIX,shopdisney.com
  + [Manual Rules] b23fa77e9c63  DOMAIN-SUFFIX,netflixinvestor.com
  + [Manual Rules] b9289d990f46  DOMAIN-SUFFIX,go-disneyworldgo.com
  + [Manual Rules] c14226df3691  IP-CIDR,104.154.127.126/32,no-resolve
  + [Manual Rules] dc19217a9dbd  DOMAIN-SUFFIX,netflixtechblog.com
  + [Manual Rules] e0a044f5aabe  DOMAIN-SUFFIX,abcnews.edgesuite.net
  + [Manual Rules] f7cf4449225c  DOMAIN-SUFFIX,go.com
  + [blackmatrix7 Global] fdef0c3d66c1  DOMAIN-SUFFIX,netflix.net
  + [Manual Rules] ffcb8be16f85  DOMAIN-SUFFIX,disneycareers.com
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Global] 7592ce589a44  DOMAIN-SUFFIX,spotify.link
```

## GlobalMedia.list

**Added: 9** (showing first 9)
```
  + [Manual Rules] 075c1321a44d  DOMAIN-SUFFIX,registerdisney.go.com
  + [Manual Rules] 11b62698a902  DOMAIN-SUFFIX,hotstar-cdn.net
  + [Manual Rules] 65bc2859fcf9  DOMAIN-SUFFIX,hotstar.com
  + [Manual Rules] 6cedad3c2887  DOMAIN-SUFFIX,hotstarext.com
  + [Manual Rules] 7592ce589a44  DOMAIN-SUFFIX,spotify.link
  + [Manual Rules] a3f928d03110  AND,((DOMAIN-SUFFIX,netflix.net),(NOT,((DOMAIN-SUFFIX,ir.netflix.net))))
  + [Manual Rules] db4822c89873  DOMAIN-SUFFIX,abc.go.com
  + [Manual Rules] e473622036b6  DOMAIN-SUFFIX,hotstar-labs.com
  + [Manual Rules] ff86a3ff1520  DOMAIN-SUFFIX,espn.go.com
```

**Removed: 14** (showing first 14)
```
  - [blackmatrix7 GlobalMedia] 0b6944d722d8  DOMAIN-SUFFIX,netflixstudios.com
  - [blackmatrix7 GlobalMedia] 2a2bcb0868f2  DOMAIN-SUFFIX,marvel.com
  - [blackmatrix7 GlobalMedia] 2f84d4fa8900  DOMAIN-SUFFIX,disneycruisebrasil.com
  - [blackmatrix7 GlobalMedia] 4a04c2846ddc  DOMAIN-SUFFIX,shops-disney.com
  - [blackmatrix7 GlobalMedia] 7cfd085f44a4  DOMAIN-SUFFIX,disneystore.com
  - [blackmatrix7 GlobalMedia] 82dfaa20c3c6  DOMAIN-SUFFIX,disneyworld-go.com
  - [blackmatrix7 GlobalMedia] a4cf7f444838  IP-CIDR,35.186.224.47/32,no-resolve
  - [blackmatrix7 GlobalMedia] ae0c096b14ee  DOMAIN-SUFFIX,shopdisney.com
  - [blackmatrix7 GlobalMedia] b23fa77e9c63  DOMAIN-SUFFIX,netflixinvestor.com
  - [blackmatrix7 GlobalMedia] b9289d990f46  DOMAIN-SUFFIX,go-disneyworldgo.com
  - [blackmatrix7 GlobalMedia] dc19217a9dbd  DOMAIN-SUFFIX,netflixtechblog.com
  - [blackmatrix7 GlobalMedia] f7cf4449225c  DOMAIN-SUFFIX,go.com
  - [blackmatrix7 GlobalMedia] fdef0c3d66c1  DOMAIN-SUFFIX,netflix.net
  - [blackmatrix7 GlobalMedia] ffcb8be16f85  DOMAIN-SUFFIX,disneycareers.com
```

## Netflix.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] a3f928d03110  AND,((DOMAIN-SUFFIX,netflix.net),(NOT,((DOMAIN-SUFFIX,ir.netflix.net))))
```

**Removed: 4** (showing first 4)
```
  - [blackmatrix7 Netflix] 0b6944d722d8  DOMAIN-SUFFIX,netflixstudios.com
  - [blackmatrix7 Netflix] b23fa77e9c63  DOMAIN-SUFFIX,netflixinvestor.com
  - [blackmatrix7 Netflix] dc19217a9dbd  DOMAIN-SUFFIX,netflixtechblog.com
  - [blackmatrix7 Netflix] fdef0c3d66c1  DOMAIN-SUFFIX,netflix.net
```

## Spotify.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 7592ce589a44  DOMAIN-SUFFIX,spotify.link
```

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 Spotify] a4cf7f444838  IP-CIDR,35.186.224.47/32,no-resolve
  - [blackmatrix7 Spotify] c14226df3691  IP-CIDR,104.154.127.126/32,no-resolve
```
