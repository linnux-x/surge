# Surge Rule Diff Report
Generated: 2026-11-18T11:23:37.332819

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 1 |
| Rules removed | 31 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Download.list | 1684 | 1665 | +1 | -20 | ~0 |
| Google.list | 688 | 687 | +0 | -1 | ~0 |
| TWMedia.list | 36 | 26 | +0 | -10 | ~0 |

## Download.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 053bc948ce74  DOMAIN,s3.amazonaws.com
```

**Removed: 20** (showing first 20)
```
  - [Manual Rules] 0a3540c64661  PROCESS-NAME,BitComet
  - [Manual Rules] 0d9ec9c0a022  PROCESS-NAME,qbittorrent*
  - [Manual Rules] 48f7d672131d  PROCESS-NAME,transmission-daemon
  - [Manual Rules] 4ef9673f88bb  PROCESS-NAME,transmission-qt
  - [Manual Rules] 521dc4f1fe66  PROCESS-NAME,NetTransport
  - [SukkaW Download] 53fc9fe4a82f  DOMAIN-SUFFIX,s3.amazonaws.com
  - [Manual Rules] 66c4779e3049  PROCESS-NAME,fdm
  - [Manual Rules] 845016eb88b5  PROCESS-NAME,ThunderVIP
  - [Manual Rules] 9148ca32607d  PROCESS-NAME,aria2c
  - [Manual Rules] a0ab0e7dcde9  PROCESS-NAME,Folx
  - [Manual Rules] afb23b943a89  PROCESS-NAME,uTorrent
  - [Manual Rules] b68ec029ad16  PROCESS-NAME,Thunder
  - [Manual Rules] b6ceda7bc95f  PROCESS-NAME,BaiduNetdisk_mac
  - [Manual Rules] bd7ab610b008  PROCESS-NAME,qbittorrent-nox
  - [Manual Rules] c27c3c6e28d1  PROCESS-NAME,amuled
  - [Manual Rules] cf6e44f5b5d6  PROCESS-NAME,qBittorrent
  - [Manual Rules] f2aacca36b7d  PROCESS-NAME,Transmission
  - [Manual Rules] fbeb9cf30e0e  PROCESS-NAME,WebTorrent Helper
  - [Manual Rules] fce34a1a3e7b  PROCESS-NAME,WebTorrent
  - [Manual Rules] fdc5fbcedadb  PROCESS-NAME,DownloadService
```

## Google.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Google] 5dddce620527  DOMAIN-SUFFIX,oasisfeng.com
```

## TWMedia.list

**Removed: 10** (showing first 10)
```
  - [SukkaW Stream TW] 0773ddeb1396  DOMAIN,hbounify-prod.evergent.com
  - [SukkaW Stream TW] 2f434ac89572  DOMAIN-SUFFIX,hbogoasia.tw
  - [SukkaW Stream TW] 3c422020c048  DOMAIN,44wilhpljf.execute-api.ap-southeast-1.amazonaws.com
  - [SukkaW Stream TW] 4af641450bb7  DOMAIN-SUFFIX,hboasia.com
  - [SukkaW Stream TW] 4b6815c84297  DOMAIN-SUFFIX,hbogoasia.sg
  - [SukkaW Stream TW] b6c2c6b5f906  DOMAIN-SUFFIX,hbogoasia.id
  - [SukkaW Stream TW] d66ecc4059bf  DOMAIN-SUFFIX,hbogoasia.com
  - [SukkaW Stream TW] d834ff40274d  DOMAIN,hbolb.onwardsmg.com
  - [SukkaW Stream TW] e4b4239d74f3  DOMAIN-SUFFIX,hbogoasia.ph
  - [SukkaW Stream TW] f3831052cbdd  DOMAIN-SUFFIX,hbogoasia.hk
```
