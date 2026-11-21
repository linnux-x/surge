# Surge Rule Diff Report
Generated: 2026-11-21T12:25:36.754918

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 4 |
| Rules added | 33 |
| Rules removed | 18 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 123 | 136 | +27 | -14 | ~1 |
| Claude.list | 14 | 16 | +4 | -2 | ~0 |
| Global.list | 24603 | 24604 | +2 | -1 | ~0 |
| GlobalMedia.list | 2272 | 2271 | +0 | -1 | ~0 |

## AI.list

**Added: 27** (showing first 27)
```
  + [Manual Rules] 061dfb003b6e  DOMAIN,dialogflow.googleapis.com
  + [Manual Rules] 0855cda2afe9  DOMAIN,production-copilot-host-westus.webpubsub.azure.com
  + [Manual Rules] 1106c5f9daf7  DOMAIN,accounts.spacexsi.com
  + [Manual Rules] 120bba58c982  DOMAIN,auth.grokipedia.com
  + [Manual Rules] 13cb0a026009  DOMAIN,geminicloudassist.googleapis.com
  + [Manual Rules] 17539c1e8a11  DOMAIN-SUFFIX,claude.app
  + [Manual Rules] 17ed196cec02  DOMAIN,claude.new
  + [Manual Rules] 29914f328abf  DOMAIN,flow.google
  + [Manual Rules] 2be3f8e88ee3  DOMAIN,cloudaicompanion.googleapis.com
  + [Manual Rules] 36c22dea2502  DOMAIN,production-copilot-host-centralus-02.webpubsub.azure.com
  + [Manual Rules] 588b0ccdc796  DOMAIN,production-copilot-host-centralus.webpubsub.azure.com
  + [Manual Rules] 5cc7d26a9c9e  DOMAIN,production-copilot-host.webpubsub.azure.com
  + [Manual Rules] 7d590b3e2bb8  DOMAIN,auth.grokusercontent.com
  + [Manual Rules] 87f37fde06c3  DOMAIN,origin-tracker.githubusercontent.com
  + [Manual Rules] 8b4e3fbfdc52  DOMAIN-WILDCARD,*-aiplatform.googleapis.com
  + [Manual Rules] 913a4abec3ed  DOMAIN,production-copilot-host-eastasia.webpubsub.azure.com
  + [Manual Rules] a43bfc7e121c  DOMAIN,aiplatform.us.rep.googleapis.com
  + [Manual Rules] aa7c06c4981d  DOMAIN-WILDCARD,*-dialogflow.googleapis.com
  + [Manual Rules] bc574175298f  DOMAIN,production-copilot-host-austriaeast.webpubsub.azure.com
  + [Manual Rules] d11c097d9e3a  DOMAIN,www.claude.dev
  + [Manual Rules] d76ec7f661d8  DOMAIN,production-copilot-host-westus3.webpubsub.azure.com
  + [Manual Rules] d8490e753e46  DOMAIN,firebasevertexai.googleapis.com
  + [Manual Rules] e13c3efa411a  DOMAIN,aiplatform.eu.rep.googleapis.com
  + [Manual Rules] e6680e1bca06  DOMAIN,claude.dev
  + [Manual Rules] e9a5e2a03ea6  DOMAIN-SUFFIX,cursorvm.com
  + [Manual Rules] f320df6eb3fc  DOMAIN,api.app.prod.grazie.aws.intellij.net
  + [Manual Rules] f7a7c00abcf7  DOMAIN,copilot-proxy.githubusercontent.com
```

**Removed: 14** (showing first 14)
```
  - [Rabbit-Spec AIGC] 1dcc20d60a4b  DOMAIN-SUFFIX,featuregates.org
  - [Rabbit-Spec AIGC] 1fbfa047d8ad  DOMAIN-SUFFIX,client-api.arkoselabs.com
  - [Manual Rules] 395b4d02e503  DOMAIN,cdn.growthbook.io
  - [Manual Rules] 98593c22f427  DOMAIN-SUFFIX,proactivebackend-pa.googleapis.com
  - [Rabbit-Spec AIGC] aca2332538ad  DOMAIN-SUFFIX,turn.livekit.cloud
  - [Rabbit-Spec AIGC] b3f222fc947b  DOMAIN-SUFFIX,host.livekit.cloud
  - [Rabbit-Spec AIGC] c78d14def5ea  IP-CIDR,24.199.123.28/32,no-resolve
  - [Rabbit-Spec AIGC] d10d35b4e7dc  DOMAIN-SUFFIX,api.statsig.com
  - [Rabbit-Spec AIGC] d34d969f3f0b  IP-CIDR,64.23.132.171/32,no-resolve
  - [Rabbit-Spec AIGC] d757313477af  DOMAIN-SUFFIX,events.statsigapi.net
  - [Rabbit-Spec AIGC] df51702bd3a8  DOMAIN-SUFFIX,observeit.net
  - [Rabbit-Spec AIGC] e9456a7b7221  IP-CIDR,129.146.3.78/32,no-resolve
  - [Manual Rules] f1164ee3b6ff  URL-REGEX,https://www\.google\.com/.*continue=https://gemini\.google\.com.+
  - [Manual Rules] fbd8c01342b9  DOMAIN-SUFFIX,geller-pa.googleapis.com
```

**Source changed: 1**
```
  ~ 391d402853fb: [SukkaW AI → Manual Rules]
```

## Claude.list

**Added: 4** (showing first 4)
```
  + [Manual Rules] 17ed196cec02  DOMAIN,claude.new
  + [Manual Rules] 391d402853fb  DOMAIN,claude.site
  + [Manual Rules] d11c097d9e3a  DOMAIN,www.claude.dev
  + [Manual Rules] e6680e1bca06  DOMAIN,claude.dev
```

**Removed: 2** (showing first 2)
```
  - [Manual Rules] 395b4d02e503  DOMAIN,cdn.growthbook.io
  - [Manual Rules] b5c2d2041b5e  DOMAIN-SUFFIX,modelcontextprotocol.io
```

## Global.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 Global] aca2332538ad  DOMAIN-SUFFIX,turn.livekit.cloud
  + [blackmatrix7 Global] b3f222fc947b  DOMAIN-SUFFIX,host.livekit.cloud
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Global] e9a5e2a03ea6  DOMAIN-SUFFIX,cursorvm.com
```

## GlobalMedia.list

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 GlobalMedia] 0641c42114ae  DOMAIN-SUFFIX,grazie.aws.intellij.net
```
