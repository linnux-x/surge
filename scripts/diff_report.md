# Surge Rule Diff Report
Generated: 2026-11-21T15:52:28.450662

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 1 |
| Rules added | 6 |
| Rules removed | 7 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Apple_AI.list | 20 | 19 | +6 | -7 | ~0 |

## Apple_AI.list

**Added: 6** (showing first 6)
```
  + [Manual Rules] 2ebcc8481ab6  DOMAIN,apple-relay.cloudflare.com
  + [Manual Rules] 6e9128c725fe  DOMAIN,cp4.cloudflare.com
  + [Manual Rules] 90301f35c67e  DOMAIN,mask.icloud.com
  + [Manual Rules] a97fbc8f931a  DOMAIN,apple-relay.fastly-edge.com
  + [Manual Rules] e1bb003bb23f  DOMAIN,apple-relay.apple.com
  + [Manual Rules] fac6e094ccd4  DOMAIN,mask-h2.icloud.com
```

**Removed: 7** (showing first 7)
```
  - [RocM301 Apple-AI] 21c16ccce25d  DOMAIN-SUFFIX,mask.icloud.com
  - [RocM301 Apple-AI] 23d8a46c106a  DOMAIN-SUFFIX,apple-relay.fastly-edge.com
  - [RocM301 Apple-AI] 4183bc428f62  DOMAIN-SUFFIX,apple-relay.apple.com
  - [RocM301 Apple-AI] 8a6b70b9c294  DOMAIN-SUFFIX,mask-h2.icloud.com
  - [RocM301 Apple-AI] e86b51bf363c  DOMAIN-SUFFIX,apple-relay.cloudflare.com
  - [RocM301 Apple-AI] eb9c099dc8eb  DOMAIN-SUFFIX,cp4.cloudflare.com
  - [RocM301 Apple-AI] f7be4981ca92  DOMAIN,mask-api.fe.apple-dns.net
```
