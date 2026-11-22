# Surge Rule Diff Report
Generated: 2026-11-22T16:41:52.357446

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 28 |
| Rules removed | 45 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Global.list | 24646 | 24652 | +6 | -0 | ~0 |
| GlobalMedia.list | 2254 | 2242 | +0 | -12 | ~0 |
| Google.list | 687 | 684 | +16 | -19 | ~0 |
| Telegram.list | 39 | 39 | +1 | -1 | ~0 |
| YouTube.list | 187 | 179 | +5 | -13 | ~0 |

## Global.list

**Added: 6** (showing first 6)
```
  + [Manual Rules] 54b39dcebe9a  DOMAIN-SUFFIX,firebaseio.com
  + [Manual Rules] 5a30ebe8123f  DOMAIN-SUFFIX,firebaseapp.com
  + [Manual Rules] 7df93f3679c6  DOMAIN-SUFFIX,appspot.com
  + [Manual Rules] b5b00f6a07d1  DOMAIN-SUFFIX,cloudfunctions.net
  + [Manual Rules] bed8ccaf5201  DOMAIN-SUFFIX,run.app
  + [Manual Rules] e6fc4b14adfa  DOMAIN-SUFFIX,web.app
```

## GlobalMedia.list

**Removed: 12** (showing first 12)
```
  - [blackmatrix7 GlobalMedia] 117bfdcdc37b  USER-AGENT,YouTube*
  - [blackmatrix7 GlobalMedia] 1acbd919549f  USER-AGENT,com.google.ios.youtube*
  - [blackmatrix7 GlobalMedia] 2ef8d5d1fc40  DOMAIN-SUFFIX,youtubego.co.id
  - [blackmatrix7 GlobalMedia] 30ff465a05a9  DOMAIN-SUFFIX,youtubego.in
  - [blackmatrix7 GlobalMedia] 4614e2585a8a  DOMAIN-SUFFIX,youtubego.id
  - [blackmatrix7 GlobalMedia] 47908cb42760  USER-AGENT,YouTubeMusic*
  - [blackmatrix7 GlobalMedia] 54b39dcebe9a  DOMAIN-SUFFIX,firebaseio.com
  - [blackmatrix7 GlobalMedia] 939c8566838e  USER-AGENT,*com.google.ios.youtubemusic*
  - [blackmatrix7 GlobalMedia] b247be74d620  USER-AGENT,com.google.ios.youtubemusic*
  - [blackmatrix7 GlobalMedia] b38203651afd  DOMAIN-SUFFIX,youtubego.co.in
  - [blackmatrix7 GlobalMedia] b481ba0e2e8f  USER-AGENT,*youtube*
  - [blackmatrix7 GlobalMedia] bbec51ab900d  USER-AGENT,*YouTubeMusic*
```

## Google.list

**Added: 16** (showing first 16)
```
  + [Manual Rules] 401a61a4c991  DOMAIN-SUFFIX,ggpht.com
  + [Manual Rules] 470aa108b6f1  IP-CIDR6,2001:4860:4860::8844/128,no-resolve
  + [Manual Rules] 4b5256e914c2  DOMAIN,accounts.youtube.com
  + [Manual Rules] 4e82154d42aa  IP-CIDR,8.8.8.8/32,no-resolve
  + [Manual Rules] 4f148b275435  DOMAIN,gweb-gettingstartedguide.appspot.com
  + [Manual Rules] 7899e85c407b  DOMAIN,chromiumdash.appspot.com
  + [Manual Rules] 78eea33cd004  DOMAIN,cros-omahaproxy.appspot.com
  + [Manual Rules] 8ae7d4a44818  IP-CIDR6,2001:4860:4860::8888/128,no-resolve
  + [Manual Rules] 9d6e2f9a787d  IP-CIDR6,2001:4860:4864:6::/64,no-resolve
  + [Manual Rules] b6c88281a32b  DOMAIN,meet.turns.goog
  + [Manual Rules] b9ce6ccd7981  DOMAIN,omahaproxy.appspot.com
  + [Manual Rules] bec001d19e3d  IP-CIDR6,2001:4860:4864:4:8000::/128,no-resolve
  + [Manual Rules] c8ae64e3d9ea  IP-CIDR6,2001:4860:4864:5::/64,no-resolve
  + [Manual Rules] dc845dab5cb4  IP-CIDR,8.8.4.4/32,no-resolve
  + [Manual Rules] e81fbb92671e  IP-CIDR,142.250.82.0/24,no-resolve
  + [Manual Rules] ed2787ec16b4  DOMAIN,workspace.turns.goog
```

**Removed: 19** (showing first 19)
```
  - [blackmatrix7 Google] 34dc06430476  DOMAIN-KEYWORD,appspot
  - [blackmatrix7 Google] 3759b93c14f2  PROCESS-NAME,com.google.android.gms
  - [blackmatrix7 Google] 42ad2d1519fd  USER-AGENT,Google.Drive*
  - [blackmatrix7 Google] 54b39dcebe9a  DOMAIN-SUFFIX,firebaseio.com
  - [blackmatrix7 Google] 5a30ebe8123f  DOMAIN-SUFFIX,firebaseapp.com
  - [blackmatrix7 Google] 736594470b2a  DOMAIN-SUFFIX,certificate-transparency.dev
  - [blackmatrix7 Google] 7af741f8072a  DOMAIN-SUFFIX,app-measurement.net
  - [blackmatrix7 Google] 7df93f3679c6  DOMAIN-SUFFIX,appspot.com
  - [blackmatrix7 Google] 843fbc9e5651  PROCESS-NAME,com.android.vending
  - [blackmatrix7 Google] 959f6a001910  DOMAIN-KEYWORD,blogspot
  - [blackmatrix7 Google] a9f7a710ad3c  PROCESS-NAME,BackupandSync
  - [blackmatrix7 Google] b589aac848f7  USER-AGENT,*com.google.Drive*
  - [blackmatrix7 Google] b5b00f6a07d1  DOMAIN-SUFFIX,cloudfunctions.net
  - [blackmatrix7 Google] bcfb11b92ebf  USER-AGENT,%E4%BA%91%E7%AB%AF%E7%A1%AC%E7%9B%98*
  - [blackmatrix7 Google] bed8ccaf5201  DOMAIN-SUFFIX,run.app
  - [blackmatrix7 Google] e6fc4b14adfa  DOMAIN-SUFFIX,web.app
  - [Manual Rules] e748554de8c0  IP-ASN,15169,no-resolve
  - [blackmatrix7 Google] edce5c67442b  PROCESS-NAME,com.google.android.play.games
  - [blackmatrix7 Google] ff67f6d80942  PROCESS-NAME,com.google.android.gsf
```

## Telegram.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] b00bf63e31ac  AND,((PROCESS-NAME,telegram-desktop),(NOT,((OR,((DOMAIN,dns.google),(DOMAIN,dns.google.com),(IP-CIDR,8.8.8.8/32,no-resolve),(IP-CIDR,8.8.4.4/32,no-resolve),(IP-CIDR6,2001:4860:4860::8888/128,no-resolve),(IP-CIDR6,2001:4860:4860::8844/128,no-resolve))))))
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 Telegram] 4252b94245de  PROCESS-NAME,telegram-desktop
```

## YouTube.list

**Added: 5** (showing first 5)
```
  + [Manual Rules] 80ad3ee66314  DOMAIN,youtubereporting.googleapis.com
  + [Manual Rules] 84f64f31dc71  DOMAIN,yt3.ggpht.com
  + [Manual Rules] 8f60ec856ad2  AND,((DOMAIN-SUFFIX,youtube.com),(NOT,((DOMAIN,accounts.youtube.com))))
  + [Manual Rules] a07d8e52a9c9  DOMAIN,youtubeanalytics.googleapis.com
  + [Manual Rules] c8601b07916c  DOMAIN,yt3.googleusercontent.com
```

**Removed: 13** (showing first 13)
```
  - [blackmatrix7 YouTube] 117bfdcdc37b  USER-AGENT,YouTube*
  - [blackmatrix7 YouTube] 1acbd919549f  USER-AGENT,com.google.ios.youtube*
  - [blackmatrix7 YouTube] 2ef8d5d1fc40  DOMAIN-SUFFIX,youtubego.co.id
  - [blackmatrix7 YouTube] 30ff465a05a9  DOMAIN-SUFFIX,youtubego.in
  - [blackmatrix7 YouTube] 401a61a4c991  DOMAIN-SUFFIX,ggpht.com
  - [blackmatrix7 YouTube] 4614e2585a8a  DOMAIN-SUFFIX,youtubego.id
  - [blackmatrix7 YouTube] 47908cb42760  USER-AGENT,YouTubeMusic*
  - [blackmatrix7 YouTube] 939c8566838e  USER-AGENT,*com.google.ios.youtubemusic*
  - [blackmatrix7 YouTube] b247be74d620  USER-AGENT,com.google.ios.youtubemusic*
  - [blackmatrix7 YouTube] b38203651afd  DOMAIN-SUFFIX,youtubego.co.in
  - [blackmatrix7 YouTube] b481ba0e2e8f  USER-AGENT,*youtube*
  - [blackmatrix7 YouTube] bbec51ab900d  USER-AGENT,*YouTubeMusic*
  - [blackmatrix7 YouTube] ff14637482cd  DOMAIN-SUFFIX,youtube.com
```
