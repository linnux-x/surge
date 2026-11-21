# Surge Rule Diff Report
Generated: 2026-11-21T15:28:33.977690

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 2 |
| Rules added | 3 |
| Rules removed | 14 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Global.list | 24638 | 24638 | +2 | -2 | ~0 |
| Telegram.list | 50 | 39 | +1 | -12 | ~0 |

## Global.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 Global] 500ff550e2db  DOMAIN-SUFFIX,usercontent.dev
  + [blackmatrix7 Global] 8346585bd226  DOMAIN-SUFFIX,telegramdownload.com
```

**Removed: 2** (showing first 2)
```
  - [blackmatrix7 Global] 851cd3e1caf2  IP-CIDR,91.108.0.0/16,no-resolve
  - [blackmatrix7 Global] a591070ebd50  IP-CIDR,109.239.140.0/24,no-resolve
```

## Telegram.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 47b06d84de59  DOMAIN,nicegram.me
```

**Removed: 12** (showing first 12)
```
  - [blackmatrix7 Telegram] 33da75575e17  IP-ASN,59930,no-resolve
  - [blackmatrix7 Telegram] 48316b9e289f  IP-ASN,62041,no-resolve
  - [blackmatrix7 Telegram] 500ff550e2db  DOMAIN-SUFFIX,usercontent.dev
  - [blackmatrix7 Telegram] 66c54932bbee  PROCESS-NAME,nekox.messenger
  - [blackmatrix7 Telegram] 6885c9fe32bc  IP-ASN,62014,no-resolve
  - [blackmatrix7 Telegram] 8346585bd226  DOMAIN-SUFFIX,telegramdownload.com
  - [blackmatrix7 Telegram] b1ed9a20e836  PROCESS-NAME,tw.nekomimi.nekogram
  - [blackmatrix7 Telegram] c0eadeef8dbb  DOMAIN-KEYWORD,nicegram
  - [blackmatrix7 Telegram] c46c920e38dc  PROCESS-NAME,org.telegram.messenger
  - [blackmatrix7 Telegram] caa214068069  IP-ASN,211157,no-resolve
  - [blackmatrix7 Telegram] d713bceb75ec  PROCESS-NAME,xyz.nextalone.nagram
  - [blackmatrix7 Telegram] ee2fa33500c1  IP-ASN,44907,no-resolve
```
