# Surge Rule Diff Report
Generated: 2026-11-21T19:22:03.493080

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 4 |
| Rules removed | 18 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Apple.list | 1380 | 1362 | +0 | -18 | ~0 |
| Apple_CN.list | 225 | 226 | +1 | -0 | ~0 |
| Global.list | 24637 | 24640 | +3 | -0 | ~0 |

## Apple.list

**Removed: 18** (showing first 18)
```
  - [blackmatrix7 Apple] 0cafcaa18f73  DOMAIN-SUFFIX,wpewebkit.org
  - [blackmatrix7 Apple] 33d343ffa5dc  DOMAIN-SUFFIX,cdn-apple-mapkit.com
  - [Manual Rules] 4c34a6fc1ad5  DOMAIN,crl4.digicert.com
  - [blackmatrix7 Apple] 5645e49b1076  DOMAIN-SUFFIX,webkitgtk.org
  - [blackmatrix7 Apple] 567aab9d4572  IP-CIDR,192.35.50.0/24,no-resolve
  - [blackmatrix7 Apple] 5afbd21653de  DOMAIN-SUFFIX,app0le.com
  - [blackmatrix7 Apple] 5e1009e78fd0  DOMAIN-SUFFIX,appleantilles.com
  - [blackmatrix7 Apple] 6039ff66f85f  DOMAIN-SUFFIX,appleclassicipod.com
  - [blackmatrix7 Apple] 71a60a358daa  DOMAIN-SUFFIX,appleafrica.com
  - [blackmatrix7 Apple] 7d120be1985c  IP-CIDR,63.92.224.0/19,no-resolve
  - [blackmatrix7 Apple] 7d2d6627f589  DOMAIN-SUFFIX,servicetalk.io
  - [Manual Rules] aebe0efcfe6a  DOMAIN,app-site-association.networking.apple
  - [blackmatrix7 Apple] ca5b26100dfe  DOMAIN-SUFFIX,xn--gtvz22d.wang
  - [blackmatrix7 Apple] d773877636d4  DOMAIN-SUFFIX,applecom.com
  - [Manual Rules] d9733c43937d  DOMAIN,ocsp.digicert.com
  - [Manual Rules] ebd53c2b5637  DOMAIN,crl3.digicert.com
  - [blackmatrix7 Apple] f81dcfa229d9  DOMAIN-SUFFIX,aplleipods.com
  - [blackmatrix7 Apple] ff5e1c4767e5  IP-CIDR,198.183.17.0/24,no-resolve
```

## Apple_CN.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] aebe0efcfe6a  DOMAIN,app-site-association.networking.apple
```

## Global.list

**Added: 3** (showing first 3)
```
  + [blackmatrix7 Global] 0cafcaa18f73  DOMAIN-SUFFIX,wpewebkit.org
  + [blackmatrix7 Global] 5645e49b1076  DOMAIN-SUFFIX,webkitgtk.org
  + [blackmatrix7 Global] 7d2d6627f589  DOMAIN-SUFFIX,servicetalk.io
```
