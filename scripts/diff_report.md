# Surge Rule Diff Report
Generated: 2026-11-21T19:32:47.767687

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 4 |
| Rules added | 47 |
| Rules removed | 34 |
| Source attribution changed | 2 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110648 | 110668 | +21 | -1 | ~2 |
| Global.list | 24640 | 24641 | +4 | -3 | ~0 |
| Microsoft.list | 484 | 473 | +18 | -29 | ~0 |
| Microsoft_CDN.list | 79 | 82 | +4 | -1 | ~0 |

## China.list

**Added: 21** (showing first 21)
```
  + [Manual Rules] 00e1b64449ab  DOMAIN-SUFFIX,sovcloud-mx.cn
  + [Manual Rules] 01ece7944d66  DOMAIN-SUFFIX,sovcloud-static.cn
  + [Manual Rules] 04a23b5f2cbd  DOMAIN-SUFFIX,sovcloud-usercontent.cn
  + [Manual Rules] 04f028cf0b56  DOMAIN-SUFFIX,sovcloud.cn
  + [Manual Rules] 15cc7e632177  DOMAIN-SUFFIX,msauthimages.cn
  + [Manual Rules] 1dee34f65686  DOMAIN-SUFFIX,windowsazure.cn
  + [Manual Rules] 3c7ad76f6a48  DOMAIN-SUFFIX,chinacloudapi.cn
  + [Manual Rules] 4dd9d5abcaa5  DOMAIN-SUFFIX,partner.office365.cn
  + [Manual Rules] 53ed8e83ec62  DOMAIN,collector.azure.cn
  + [Manual Rules] 6c5bd2109452  DOMAIN,attachments.office365-net.cn
  + [Manual Rules] 8bf2410f522f  DOMAIN-SUFFIX,msftauthimages.cn
  + [Manual Rules] a2d5dd519d82  DOMAIN-SUFFIX,auth.microsoft.cn
  + [Manual Rules] a96c8d575eb3  DOMAIN-SUFFIX,msftauth.cn
  + [Manual Rules] b09ec36eb75f  DOMAIN-SUFFIX,aadrm.cn
  + [Manual Rules] b3d96b7698a9  DOMAIN-SUFFIX,partner.microsoftonline-p.cn
  + [Manual Rules] bb81d8ba6c1a  DOMAIN-SUFFIX,azure-mobile.cn
  + [Manual Rules] bd56664ae1b2  DOMAIN-SUFFIX,msauth.cn
  + [Manual Rules] d53d610886f2  DOMAIN-SUFFIX,microsoftonline.cn
  + [Manual Rules] d5a33127236b  DOMAIN-SUFFIX,onmschina.cn
  + [Manual Rules] dd810d85b1b0  DOMAIN,loki.office365.cn
  + [Manual Rules] fd63281a0be6  DOMAIN-SUFFIX,chinacloud-mobile.cn
```

**Removed: 1** (showing first 1)
```
  - [Rabbit-Spec China] a020b6a6694e  DOMAIN-SUFFIX,windows.net
```

**Source changed: 2**
```
  ~ 7ddb17ee1688: [SukkaW Domestic → Manual Rules]
  ~ 5311c188fb80: [SukkaW Domestic → Manual Rules]
```

## Global.list

**Added: 4** (showing first 4)
```
  + [blackmatrix7 Global] 18fd1fe3e686  DOMAIN-SUFFIX,azurewebsites.net
  + [blackmatrix7 Global] 2a09bc80657c  DOMAIN-SUFFIX,azurefd.net
  + [blackmatrix7 Global] e77abcada295  DOMAIN-SUFFIX,cloudapp.net
  + [blackmatrix7 Global] f181245620d4  DOMAIN-SUFFIX,trafficmanager.net
```

**Removed: 3** (showing first 3)
```
  - [blackmatrix7 Global] 4486741450cb  DOMAIN-SUFFIX,onenote.com
  - [blackmatrix7 Global] 9804de830843  DOMAIN-SUFFIX,streaming.mediaservices.windows.net
  - [blackmatrix7 Global] c0374368d4e0  DOMAIN,vscode.search.windows.net
```

## Microsoft.list

**Added: 18** (showing first 18)
```
  + [Manual Rules] 1006b23f9469  DOMAIN,sts.windows.net
  + [Manual Rules] 1c33e176159a  DOMAIN-SUFFIX,powerapps.com
  + [Manual Rules] 41a448977dc7  DOMAIN-SUFFIX,clipchamp.com
  + [Manual Rules] 4486741450cb  DOMAIN-SUFFIX,onenote.com
  + [Manual Rules] 54f7045bd259  DOMAIN,redemptionservices.accesscontrol.windows.net
  + [Manual Rules] 68f47450232b  DOMAIN,accounts.accesscontrol.windows.net
  + [Manual Rules] 72397593ae33  DOMAIN-SUFFIX,keydelivery.mediaservices.windows.net
  + [Manual Rules] 7c982ac9a4e3  DOMAIN,enterpriseregistration.windows.net
  + [Manual Rules] 93738c2ba10d  DOMAIN,management.core.windows.net
  + [Manual Rules] 95456a8b49f2  DOMAIN-SUFFIX,microsoftusercontent.com
  + [Manual Rules] 970eb96bf8fb  DOMAIN,posarprodcssservice.accesscontrol.windows.net
  + [Manual Rules] 9804de830843  DOMAIN-SUFFIX,streaming.mediaservices.windows.net
  + [Manual Rules] 9a02605dc101  DOMAIN,graph.windows.net
  + [Manual Rules] a36982b5ed52  AND,((PROTOCOL,UDP),(DEST-PORT,3478-3481),(IP-CIDR,52.112.0.0/14,no-resolve))
  + [Manual Rules] af79a24d5137  AND,((PROTOCOL,UDP),(DEST-PORT,3478-3481),(IP-CIDR,52.122.0.0/15,no-resolve))
  + [Manual Rules] b45c085ef879  AND,((PROTOCOL,UDP),(DEST-PORT,3478-3481),(IP-CIDR6,2603:1063::/38,no-resolve))
  + [Manual Rules] b59bc2c48fb7  DOMAIN,login.windows.net
  + [Manual Rules] c0374368d4e0  DOMAIN,vscode.search.windows.net
```

**Removed: 29** (showing first 29)
```
  - [blackmatrix7 Microsoft] 00b2645fb2e7  DOMAIN-SUFFIX,office365tw.com
  - [blackmatrix7 Microsoft] 18fd1fe3e686  DOMAIN-SUFFIX,azurewebsites.net
  - [blackmatrix7 Microsoft] 1c5dfe19aee6  DOMAIN-SUFFIX,microsofteca.com
  - [blackmatrix7 Microsoft] 1f0cf387224c  DOMAIN-SUFFIX,bluehatnights.com
  - [blackmatrix7 Microsoft] 2a09bc80657c  DOMAIN-SUFFIX,azurefd.net
  - [blackmatrix7 Microsoft] 3b2c0846ecad  DOMAIN-SUFFIX,office365love.com
  - [blackmatrix7 Microsoft] 4440f67468bf  USER-AGENT,OneDrive*
  - [blackmatrix7 Microsoft] 493fb427ac1d  DOMAIN-SUFFIX,sankie.net
  - [blackmatrix7 Microsoft] 4abb1fedd0e1  DOMAIN-KEYWORD,onedrive
  - [blackmatrix7 Microsoft] 55b49d757786  DOMAIN-SUFFIX,microsoft.red
  - [blackmatrix7 Microsoft] 5baf7a7375cc  USER-AGENT,Microsoft*
  - [blackmatrix7 Microsoft] 6286437f1578  DOMAIN-SUFFIX,opentranslatorstothings.org
  - [blackmatrix7 Microsoft] 693291bfdab1  DOMAIN-SUFFIX,microsoft.com.nsatc.net
  - [blackmatrix7 Microsoft] 700822201997  DOMAIN-SUFFIX,microsoftlinc.com
  - [blackmatrix7 Microsoft] 7e18cbda3159  DOMAIN-SUFFIX,microsoftsiteselection.com
  - [blackmatrix7 Microsoft] 8ffeaeeb292f  DOMAIN-SUFFIX,msignitechina.com
  - [blackmatrix7 Microsoft] 95b6dc718714  DOMAIN-SUFFIX,microsoftmxfilantropia.com
  - [blackmatrix7 Microsoft] a020b6a6694e  DOMAIN-SUFFIX,windows.net
  - [blackmatrix7 Microsoft] a50b632125b6  DOMAIN-SUFFIX,windowscommunity.net
  - [blackmatrix7 Microsoft] b07bddf87073  DOMAIN-SUFFIX,livingyourambition.com
  - [blackmatrix7 Microsoft] c18f7e01cc9e  PROCESS-NAME,OneDriveUpdater
  - [blackmatrix7 Microsoft] c87d739be064  DOMAIN-SUFFIX,meetyourdevices.com
  - [blackmatrix7 Microsoft] c9404e07a9e3  PROCESS-NAME,OneDrive
  - [blackmatrix7 Microsoft] ccd6a15512c4  USER-AGENT,OneDriveiOSApp*
  - [blackmatrix7 Microsoft] d80da49f96c0  DOMAIN-SUFFIX,msn.com.nsatc.net
  - [blackmatrix7 Microsoft] e77abcada295  DOMAIN-SUFFIX,cloudapp.net
  - [blackmatrix7 Microsoft] ec73faa5cf41  DOMAIN-KEYWORD,skydrive
  - [blackmatrix7 Microsoft] ee9184d16201  DOMAIN-SUFFIX,msudalosti.com
  - [blackmatrix7 Microsoft] f181245620d4  DOMAIN-SUFFIX,trafficmanager.net
```

## Microsoft_CDN.list

**Added: 4** (showing first 4)
```
  + [Manual Rules] 1c28733c6f52  DOMAIN,cdn.odc.officeapps.live.com
  + [Manual Rules] 278d948ad8d6  DOMAIN,otelrules.azureedge.net
  + [Manual Rules] 5aa54ba2b261  DOMAIN-SUFFIX,static.microsoft
  + [Manual Rules] 7462b1999b84  DOMAIN,cdn.uci.officeapps.live.com
```

**Removed: 1** (showing first 1)
```
  - [Manual Rules] 95456a8b49f2  DOMAIN-SUFFIX,microsoftusercontent.com
```
