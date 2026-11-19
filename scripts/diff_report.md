# Surge Rule Diff Report
Generated: 2026-11-19T16:52:32.737243

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 4 |
| Rules added | 30 |
| Rules removed | 59 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Game.list | 572 | 571 | +0 | -1 | ~0 |
| Global.list | 24573 | 24603 | +30 | -0 | ~0 |
| GlobalMedia.list | 2317 | 2288 | +0 | -29 | ~0 |
| Netflix.list | 1152 | 1123 | +0 | -29 | ~0 |

## Game.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Game] b25529c3b353  IP-CIDR,35.192.0.0/12,no-resolve
```

## Global.list

**Added: 30** (showing first 30)
```
  + [Manual Rules] 055606dbb40e  IP-CIDR,35.160.0.0/13,no-resolve
  + [Manual Rules] 2600179c8d50  IP-CIDR,44.224.0.0/16,no-resolve
  + [Manual Rules] 35da20afb652  IP-CIDR,52.24.0.0/14,no-resolve
  + [Manual Rules] 36037930c1e6  IP-CIDR,54.86.0.0/16,no-resolve
  + [Manual Rules] 46ced1bdc84d  IP-CIDR,52.88.0.0/15,no-resolve
  + [Manual Rules] 472391a19f8f  IP-CIDR,52.7.0.0/16,no-resolve
  + [Manual Rules] 51445668f420  IP-CIDR,52.0.0.0/15,no-resolve
  + [Manual Rules] 5736528d220e  IP-CIDR,34.208.0.0/12,no-resolve
  + [Manual Rules] 5d886892d914  IP-CIDR,54.188.0.0/15,no-resolve
  + [Manual Rules] 642691050e99  IP-CIDR,52.12.0.0/15,no-resolve
  + [Manual Rules] 671150735b98  IP-CIDR,54.68.0.0/15,no-resolve
  + [Manual Rules] 6ebdb466539e  IP-CIDR,44.230.0.0/16,no-resolve
  + [Manual Rules] 80a824700e7b  IP-CIDR,34.192.0.0/16,no-resolve
  + [Manual Rules] 9777e36916f7  IP-CIDR,54.85.0.0/16,no-resolve
  + [Manual Rules] a01f0147efa3  IP-CIDR,52.72.0.0/16,no-resolve
  + [Manual Rules] aafecc20b009  IP-CIDR,54.76.0.0/15,no-resolve
  + [Manual Rules] b25529c3b353  IP-CIDR,35.192.0.0/12,no-resolve
  + [Manual Rules] b2dc02a8cbb8  IP-CIDR,52.54.0.0/16,no-resolve
  + [Manual Rules] b608596f32d6  IP-CIDR,52.40.0.0/14,no-resolve
  + [Manual Rules] b9e627e6b40a  IP-CIDR,52.32.0.0/14,no-resolve
  + [Manual Rules] bb7ff2760e2c  IP-CIDR,54.213.0.0/16,no-resolve
  + [Manual Rules] d52192ef8b65  IP-CIDR,54.186.0.0/15,no-resolve
  + [Manual Rules] db7f76e81374  IP-CIDR,54.74.0.0/15,no-resolve
  + [Manual Rules] e0e3cd1b1b82  IP-CIDR,52.22.0.0/16,no-resolve
  + [Manual Rules] e2bb4e1d79c2  IP-CIDR,52.48.0.0/14,no-resolve
  + [Manual Rules] e43b97188e8f  IP-CIDR,54.148.0.0/15,no-resolve
  + [Manual Rules] eb5afd986b3f  IP-CIDR,54.175.0.0/16,no-resolve
  + [Manual Rules] f60bfb7ea19a  IP-CIDR,34.248.0.0/13,no-resolve
  + [Manual Rules] fa17e65971cc  IP-CIDR,52.10.0.0/15,no-resolve
  + [Manual Rules] fb88e4884fbc  IP-CIDR,52.5.0.0/16,no-resolve
```

## GlobalMedia.list

**Removed: 29** (showing first 29)
```
  - [blackmatrix7 GlobalMedia] 055606dbb40e  IP-CIDR,35.160.0.0/13,no-resolve
  - [blackmatrix7 GlobalMedia] 2600179c8d50  IP-CIDR,44.224.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 35da20afb652  IP-CIDR,52.24.0.0/14,no-resolve
  - [blackmatrix7 GlobalMedia] 36037930c1e6  IP-CIDR,54.86.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 46ced1bdc84d  IP-CIDR,52.88.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] 472391a19f8f  IP-CIDR,52.7.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 51445668f420  IP-CIDR,52.0.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] 5736528d220e  IP-CIDR,34.208.0.0/12,no-resolve
  - [blackmatrix7 GlobalMedia] 5d886892d914  IP-CIDR,54.188.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] 642691050e99  IP-CIDR,52.12.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] 671150735b98  IP-CIDR,54.68.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] 6ebdb466539e  IP-CIDR,44.230.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 80a824700e7b  IP-CIDR,34.192.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] 9777e36916f7  IP-CIDR,54.85.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] a01f0147efa3  IP-CIDR,52.72.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] aafecc20b009  IP-CIDR,54.76.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] b2dc02a8cbb8  IP-CIDR,52.54.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] b608596f32d6  IP-CIDR,52.40.0.0/14,no-resolve
  - [blackmatrix7 GlobalMedia] b9e627e6b40a  IP-CIDR,52.32.0.0/14,no-resolve
  - [blackmatrix7 GlobalMedia] bb7ff2760e2c  IP-CIDR,54.213.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] d52192ef8b65  IP-CIDR,54.186.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] db7f76e81374  IP-CIDR,54.74.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] e0e3cd1b1b82  IP-CIDR,52.22.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] e2bb4e1d79c2  IP-CIDR,52.48.0.0/14,no-resolve
  - [blackmatrix7 GlobalMedia] e43b97188e8f  IP-CIDR,54.148.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] eb5afd986b3f  IP-CIDR,54.175.0.0/16,no-resolve
  - [blackmatrix7 GlobalMedia] f60bfb7ea19a  IP-CIDR,34.248.0.0/13,no-resolve
  - [blackmatrix7 GlobalMedia] fa17e65971cc  IP-CIDR,52.10.0.0/15,no-resolve
  - [blackmatrix7 GlobalMedia] fb88e4884fbc  IP-CIDR,52.5.0.0/16,no-resolve
```

## Netflix.list

**Removed: 29** (showing first 29)
```
  - [blackmatrix7 Netflix] 055606dbb40e  IP-CIDR,35.160.0.0/13,no-resolve
  - [blackmatrix7 Netflix] 2600179c8d50  IP-CIDR,44.224.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 35da20afb652  IP-CIDR,52.24.0.0/14,no-resolve
  - [blackmatrix7 Netflix] 36037930c1e6  IP-CIDR,54.86.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 46ced1bdc84d  IP-CIDR,52.88.0.0/15,no-resolve
  - [blackmatrix7 Netflix] 472391a19f8f  IP-CIDR,52.7.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 51445668f420  IP-CIDR,52.0.0.0/15,no-resolve
  - [blackmatrix7 Netflix] 5736528d220e  IP-CIDR,34.208.0.0/12,no-resolve
  - [blackmatrix7 Netflix] 5d886892d914  IP-CIDR,54.188.0.0/15,no-resolve
  - [blackmatrix7 Netflix] 642691050e99  IP-CIDR,52.12.0.0/15,no-resolve
  - [blackmatrix7 Netflix] 671150735b98  IP-CIDR,54.68.0.0/15,no-resolve
  - [blackmatrix7 Netflix] 6ebdb466539e  IP-CIDR,44.230.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 80a824700e7b  IP-CIDR,34.192.0.0/16,no-resolve
  - [blackmatrix7 Netflix] 9777e36916f7  IP-CIDR,54.85.0.0/16,no-resolve
  - [blackmatrix7 Netflix] a01f0147efa3  IP-CIDR,52.72.0.0/16,no-resolve
  - [blackmatrix7 Netflix] aafecc20b009  IP-CIDR,54.76.0.0/15,no-resolve
  - [blackmatrix7 Netflix] b2dc02a8cbb8  IP-CIDR,52.54.0.0/16,no-resolve
  - [blackmatrix7 Netflix] b608596f32d6  IP-CIDR,52.40.0.0/14,no-resolve
  - [blackmatrix7 Netflix] b9e627e6b40a  IP-CIDR,52.32.0.0/14,no-resolve
  - [blackmatrix7 Netflix] bb7ff2760e2c  IP-CIDR,54.213.0.0/16,no-resolve
  - [blackmatrix7 Netflix] d52192ef8b65  IP-CIDR,54.186.0.0/15,no-resolve
  - [blackmatrix7 Netflix] db7f76e81374  IP-CIDR,54.74.0.0/15,no-resolve
  - [blackmatrix7 Netflix] e0e3cd1b1b82  IP-CIDR,52.22.0.0/16,no-resolve
  - [blackmatrix7 Netflix] e2bb4e1d79c2  IP-CIDR,52.48.0.0/14,no-resolve
  - [blackmatrix7 Netflix] e43b97188e8f  IP-CIDR,54.148.0.0/15,no-resolve
  - [blackmatrix7 Netflix] eb5afd986b3f  IP-CIDR,54.175.0.0/16,no-resolve
  - [blackmatrix7 Netflix] f60bfb7ea19a  IP-CIDR,34.248.0.0/13,no-resolve
  - [blackmatrix7 Netflix] fa17e65971cc  IP-CIDR,52.10.0.0/15,no-resolve
  - [blackmatrix7 Netflix] fb88e4884fbc  IP-CIDR,52.5.0.0/16,no-resolve
```
