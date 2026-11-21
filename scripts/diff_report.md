# Surge Rule Diff Report
Generated: 2026-11-21T15:12:36.902026

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 6 |
| Rules added | 10 |
| Rules removed | 3 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Download.list | 1610 | 1611 | +1 | -0 | ~0 |
| Global.list | 24636 | 24638 | +2 | -0 | ~0 |
| GlobalMedia.list | 2253 | 2254 | +1 | -0 | ~0 |
| Netflix.list | 1115 | 1116 | +1 | -0 | ~0 |
| Speedtest.list | 1725 | 1726 | +4 | -3 | ~0 |
| Speedtest_China.list | 53 | 54 | +1 | -0 | ~0 |

## Download.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 003de57ede77  DOMAIN,desktop.wifiman.com
```

## Global.list

**Added: 2** (showing first 2)
```
  + [Manual Rules] 0a47195526ee  DOMAIN,stealth.net
  + [blackmatrix7 Global] db567d161c84  DOMAIN-SUFFIX,wifiman.com
```

## GlobalMedia.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] d646c37a3d0d  DOMAIN-SUFFIX,fast.com
```

## Netflix.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] d646c37a3d0d  DOMAIN-SUFFIX,fast.com
```

## Speedtest.list

**Added: 4** (showing first 4)
```
  + [Manual Rules] 132d80b1cad3  DOMAIN,wifiman.com
  + [Manual Rules] 3a526b67044b  AND,((DOMAIN,stealth.net),(DEST-PORT,8080))
  + [Manual Rules] a80e7d0edd8d  DOMAIN,speedtest.ubncloud.com
  + [Manual Rules] bb16ef6ead4a  DOMAIN,www.wifiman.com
```

**Removed: 3** (showing first 3)
```
  - [SukkaW Speedtest Servers International] 0a47195526ee  DOMAIN,stealth.net
  - [Manual Rules] d646c37a3d0d  DOMAIN-SUFFIX,fast.com
  - [SukkaW Speedtest] db567d161c84  DOMAIN-SUFFIX,wifiman.com
```

## Speedtest_China.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 696287a8d603  DOMAIN,api-v3.speedtest.cn
```
