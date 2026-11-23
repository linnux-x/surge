# Surge Rule Diff Report
Generated: 2026-11-23T10:13:55.252506

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 9 |
| Rules added | 17 |
| Rules removed | 32 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Binance.list | 4 | 5 | +1 | -0 | ~0 |
| China.list | 110661 | 110661 | +1 | -1 | ~0 |
| Disney.list | 151 | 142 | +0 | -9 | ~0 |
| Global.list | 24666 | 24680 | +14 | -0 | ~0 |
| GlobalMedia.list | 2153 | 2138 | +0 | -15 | ~0 |
| Google.list | 684 | 685 | +1 | -0 | ~0 |
| JPMedia.list | 25 | 21 | +0 | -4 | ~0 |
| SocialMedia.list | 663 | 662 | +0 | -1 | ~0 |
| USMedia.list | 35 | 33 | +0 | -2 | ~0 |

## Binance.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 3fc32e9101b0  DOMAIN,bpay.binanceapi.com
```

## China.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] da3020d97154  DOMAIN-SUFFIX,223789.xyz
```

**Removed: 1** (showing first 1)
```
  - [Manual Rules] 914c64de3e00  DOMAIN-KEYWORD,223789
```

## Disney.list

**Removed: 9** (showing first 9)
```
  - [blackmatrix7 Disney] 0b1888a69cb7  DOMAIN-SUFFIX,disneytermsofuse.com
  - [blackmatrix7 Disney] 16b0add3e301  DOMAIN-SUFFIX,disneyiejobs.com
  - [blackmatrix7 Disney] 2ee95d576c87  DOMAIN-SUFFIX,disneyprivacycenter.com
  - [blackmatrix7 Disney] 4616a58c8504  DOMAIN-SUFFIX,disneyaulani.com
  - [blackmatrix7 Disney] 4b35db4e200f  DOMAIN-SUFFIX,disneyadsales.com
  - [blackmatrix7 Disney] 95faee2bd95f  DOMAIN-SUFFIX,disneytickets.co.uk
  - [blackmatrix7 Disney] a8c430f84ae9  DOMAIN-SUFFIX,disneytvajobs.com
  - [blackmatrix7 Disney] c25eec2e0599  DOMAIN-SUFFIX,adventuresbydisney.com
  - [blackmatrix7 Disney] f92d06a553bf  DOMAIN-SUFFIX,natgeomaps.com
```

## Global.list

**Added: 14** (showing first 14)
```
  + [Manual Rules] 0b1888a69cb7  DOMAIN-SUFFIX,disneytermsofuse.com
  + [Manual Rules] 16b0add3e301  DOMAIN-SUFFIX,disneyiejobs.com
  + [Manual Rules] 2ee95d576c87  DOMAIN-SUFFIX,disneyprivacycenter.com
  + [Manual Rules] 3d790edffb68  DOMAIN-SUFFIX,aboutamazon.com
  + [Manual Rules] 4616a58c8504  DOMAIN-SUFFIX,disneyaulani.com
  + [Manual Rules] 4b35db4e200f  DOMAIN-SUFFIX,disneyadsales.com
  + [Manual Rules] 95faee2bd95f  DOMAIN-SUFFIX,disneytickets.co.uk
  + [Manual Rules] a5a7cb0036a7  DOMAIN-SUFFIX,amebame.com
  + [Manual Rules] a8c430f84ae9  DOMAIN-SUFFIX,disneytvajobs.com
  + [Manual Rules] c25eec2e0599  DOMAIN-SUFFIX,adventuresbydisney.com
  + [Manual Rules] c320245b083c  DOMAIN-SUFFIX,dokusho-ojikan.jp
  + [Manual Rules] eaf7d709883e  DOMAIN-SUFFIX,ameblo.jp
  + [Manual Rules] f92d06a553bf  DOMAIN-SUFFIX,natgeomaps.com
  + [Manual Rules] fd491b97deef  DOMAIN-SUFFIX,ameba.jp
```

## GlobalMedia.list

**Removed: 15** (showing first 15)
```
  - [blackmatrix7 GlobalMedia] 16b0add3e301  DOMAIN-SUFFIX,disneyiejobs.com
  - [blackmatrix7 GlobalMedia] 3d790edffb68  DOMAIN-SUFFIX,aboutamazon.com
  - [blackmatrix7 GlobalMedia] 4616a58c8504  DOMAIN-SUFFIX,disneyaulani.com
  - [blackmatrix7 GlobalMedia] 4b35db4e200f  DOMAIN-SUFFIX,disneyadsales.com
  - [blackmatrix7 GlobalMedia] 533741016741  URL-REGEX,^https?:\/\/www\.amazon\.com\/(Amazon-Video|gp\/video)\/
  - [blackmatrix7 GlobalMedia] 95faee2bd95f  DOMAIN-SUFFIX,disneytickets.co.uk
  - [blackmatrix7 GlobalMedia] a5a7cb0036a7  DOMAIN-SUFFIX,amebame.com
  - [blackmatrix7 GlobalMedia] a8c430f84ae9  DOMAIN-SUFFIX,disneytvajobs.com
  - [blackmatrix7 GlobalMedia] c25eec2e0599  DOMAIN-SUFFIX,adventuresbydisney.com
  - [blackmatrix7 GlobalMedia] c320245b083c  DOMAIN-SUFFIX,dokusho-ojikan.jp
  - [Manual Rules] e3e69d38a1c3  DOMAIN-KEYWORD,023168
  - [blackmatrix7 GlobalMedia] eaf7d709883e  DOMAIN-SUFFIX,ameblo.jp
  - [SukkaW Stream] f59249b2f580  PROCESS-NAME,music
  - [blackmatrix7 GlobalMedia] f92d06a553bf  DOMAIN-SUFFIX,natgeomaps.com
  - [blackmatrix7 GlobalMedia] fd491b97deef  DOMAIN-SUFFIX,ameba.jp
```

## Google.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 6dad89470664  IP-CIDR,108.177.8.0/21,no-resolve
```

## JPMedia.list

**Removed: 4** (showing first 4)
```
  - [SukkaW Stream JP] a5a7cb0036a7  DOMAIN-SUFFIX,amebame.com
  - [SukkaW Stream JP] c320245b083c  DOMAIN-SUFFIX,dokusho-ojikan.jp
  - [SukkaW Stream JP] eaf7d709883e  DOMAIN-SUFFIX,ameblo.jp
  - [SukkaW Stream JP] fd491b97deef  DOMAIN-SUFFIX,ameba.jp
```

## SocialMedia.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Facebook] 6dad89470664  IP-CIDR,108.177.8.0/21,no-resolve
```

## USMedia.list

**Removed: 2** (showing first 2)
```
  - [SukkaW Stream US] 02aa3604bb50  DOMAIN-SUFFIX,uplynk.com
  - [SukkaW Stream US] c31dce063d32  DOMAIN-SUFFIX,theplatform.com
```
