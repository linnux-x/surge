# Surge Rule Diff Report
Generated: 2026-11-21T13:09:59.718853

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 1 |
| Rules added | 1 |
| Rules removed | 1 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Speedtest.list | 1725 | 1725 | +1 | -1 | ~0 |

## Speedtest.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 25420bcdd9d7  AND,((DOMAIN,mirror.nforce.com),(DEST-PORT,8080))
```

**Removed: 1** (showing first 1)
```
  - [Manual Rules] 84a1bcca8116  URL-REGEX,^http://mirror\.nforce\.com:8080/speedtest(?:[/?#]|$)
```
