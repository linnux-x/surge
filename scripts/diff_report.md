# Surge Rule Diff Report
Generated: 2026-11-21T17:59:02.197259

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 427 |
| Rules removed | 8 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 140 | 560 | +425 | -5 | ~0 |
| Download.list | 1611 | 1612 | +1 | -0 | ~0 |
| Global.list | 24638 | 24636 | +1 | -3 | ~0 |

## AI.list

**Added: 425** (showing first 100)
```
  + [OpenAI ChatGPT Voice] 003db6211d33  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.25.136.71/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0067f5836b50  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.151.125.58/32,no-resolve))
  + [OpenAI ChatGPT Voice] 010f7a23069e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.168.16.99/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0227523d3db5  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,57.154.51.173/32,no-resolve))
  + [OpenAI ChatGPT Voice] 039eeff95b08  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.165.158.214/32,no-resolve))
  + [OpenAI ChatGPT Voice] 04d9b409ff1a  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.118.36.228/32,no-resolve))
  + [OpenAI ChatGPT Voice] 04f499370cdf  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,138.91.23.93/32,no-resolve))
  + [OpenAI ChatGPT Voice] 054017db361c  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.201.104.14/32,no-resolve))
  + [OpenAI ChatGPT Voice] 05a3188ea936  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.211.100.168/32,no-resolve))
  + [OpenAI ChatGPT Voice] 05f4ca2527fd  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.151.200.38/32,no-resolve))
  + [OpenAI ChatGPT Voice] 066b5dd965a0  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.125.138.65/32,no-resolve))
  + [OpenAI ChatGPT Voice] 071276f09dcb  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.204.26.187/32,no-resolve))
  + [OpenAI ChatGPT Voice] 07426844093a  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,191.232.190.216/32,no-resolve))
  + [OpenAI ChatGPT Voice] 07887c6eea1d  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.219.124.186/32,no-resolve))
  + [OpenAI ChatGPT Voice] 08533a4a0e9e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,74.7.32.33/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0a55b9e9f925  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.203.144.245/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0a5e49d4905c  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.197.185.255/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0a760c4238f1  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,52.243.62.231/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0ab19081873e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.69.27.102/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0b270a477f15  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,134.138.48.99/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0ba4031674f0  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.215.51.56/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0c46b12537cf  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.204.26.194/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0cda6d95a685  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,158.158.35.12/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0da01a5bd008  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.98.94.72/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0fad01020a15  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.66.44.126/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0fd0d46604e5  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.173.91.17/32,no-resolve))
  + [OpenAI ChatGPT Voice] 0fe17eb7930e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,52.140.124.30/32,no-resolve))
  + [OpenAI ChatGPT Voice] 10c2d4e04824  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.160.163.154/32,no-resolve))
  + [OpenAI ChatGPT Voice] 12df60c4d103  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.242.133.59/32,no-resolve))
  + [OpenAI ChatGPT Voice] 131a82953220  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.203.39.49/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1376c1b1eaa1  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,52.237.113.253/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1416b2ceec7b  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.61.69.127/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1444232bd9fd  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.213.73.163/32,no-resolve))
  + [OpenAI ChatGPT Voice] 14c813c11f0e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.197.177.17/32,no-resolve))
  + [OpenAI ChatGPT Voice] 15388702eeec  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,70.153.147.96/32,no-resolve))
  + [OpenAI ChatGPT Voice] 169173e87152  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.219.109.3/32,no-resolve))
  + [OpenAI ChatGPT Voice] 179ef1a52a12  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.194.216.186/32,no-resolve))
  + [OpenAI ChatGPT Voice] 186dbb59a15f  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.160.35.238/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1a5a68c2e18e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,68.155.152.41/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1ace2eee6ae4  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,51.116.89.102/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1b37b22076ac  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.202.23.232/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1b3a480dd93f  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.89.101.223/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1b49988575dd  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,13.71.25.29/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1b6b90d91e6f  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.9.6.44/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1e8c90e51c50  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.196.195.248/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1ebd66a3e569  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,74.248.120.121/32,no-resolve))
  + [OpenAI ChatGPT Voice] 1fbe96922dc8  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.205.94.184/32,no-resolve))
  + [OpenAI ChatGPT Voice] 213cba52221d  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.155.146.196/32,no-resolve))
  + [OpenAI ChatGPT Voice] 21b781bf6085  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.225.156.200/32,no-resolve))
  + [OpenAI ChatGPT Voice] 21fd845e331a  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,85.211.193.130/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2200419be158  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.205.159.128/32,no-resolve))
  + [OpenAI ChatGPT Voice] 22049bf7c02d  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,51.57.68.153/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2212385cfc2a  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.184.136.176/32,no-resolve))
  + [OpenAI ChatGPT Voice] 223217497295  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.234.111.90/32,no-resolve))
  + [OpenAI ChatGPT Voice] 223661aedfb6  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.204.24.194/32,no-resolve))
  + [OpenAI ChatGPT Voice] 230e52d8afce  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,51.107.168.125/32,no-resolve))
  + [OpenAI ChatGPT Voice] 232efd68fbd9  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,134.138.48.156/32,no-resolve))
  + [OpenAI ChatGPT Voice] 23338e5cc0ba  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.171.138.58/32,no-resolve))
  + [OpenAI ChatGPT Voice] 23e483c741c1  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.113.195.227/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2472e1a80e51  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,52.150.164.49/32,no-resolve))
  + [OpenAI ChatGPT Voice] 248cfea80942  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,130.131.242.81/32,no-resolve))
  + [OpenAI ChatGPT Voice] 25382918f424  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.205.159.144/32,no-resolve))
  + [OpenAI ChatGPT Voice] 254319ebd51e  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.205.234.64/32,no-resolve))
  + [OpenAI ChatGPT Voice] 259c26bcdc2b  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.205.94.183/32,no-resolve))
  + [OpenAI ChatGPT Voice] 25db7a43739a  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,72.146.20.246/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2683ce40adb9  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,134.138.49.186/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2751c22cd6bb  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,158.158.96.28/32,no-resolve))
  + [OpenAI ChatGPT Voice] 27d89da8f512  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.113.199.182/32,no-resolve))
  + [OpenAI ChatGPT Voice] 29975eeedade  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.211.207.196/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2a2a1867bccd  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,68.221.176.216/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2aea9e03b279  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,85.211.195.125/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2b308370fbb0  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.125.96.144/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2b701e465c2f  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.166.108.88/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2c361b78199b  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,9.205.248.42/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2c8ce2407d20  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.236.64.56/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2d5a060dd0a5  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,52.253.109.199/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2dd1623fdcbf  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.215.254.178/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2def2ea1d511  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.89.130.145/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2e03985dd1ff  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.226.89.95/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2e2751df9ced  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.42.209.232/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2e5f8cdbe69a  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,128.24.89.254/32,no-resolve))
  + [OpenAI ChatGPT Voice] 2f90b97043fb  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.207.202.126/32,no-resolve))
  + [OpenAI ChatGPT Voice] 315cf1f0160b  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,85.211.247.9/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3250017c2c52  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.168.48.117/32,no-resolve))
  + [OpenAI ChatGPT Voice] 327fe8306c22  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.151.178.112/32,no-resolve))
  + [OpenAI ChatGPT Voice] 33784d8ab23c  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,134.138.48.201/32,no-resolve))
  + [OpenAI ChatGPT Voice] 349367ed5460  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,52.148.5.163/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3645fc27640f  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.214.225.136/32,no-resolve))
  + [OpenAI ChatGPT Voice] 37bcc11a8496  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.207.197.123/32,no-resolve))
  + [OpenAI ChatGPT Voice] 380ca8d2d6c8  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.246.114.35/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3897a682082d  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.225.200.166/32,no-resolve))
  + [OpenAI ChatGPT Voice] 395686c30728  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.219.100.169/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3b1ddeedffbd  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,13.78.198.12/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3c563bb9ea23  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.151.204.68/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3c95ddef5563  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.200.47.199/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3d97ddfa7429  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,85.211.180.16/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3ef81e052db1  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,74.248.35.102/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3f30f648e81f  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.215.219.87/32,no-resolve))
  + [OpenAI ChatGPT Voice] 3faca9fcd699  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,4.218.14.95/32,no-resolve))
  + [OpenAI ChatGPT Voice] 40b09d3b1ad3  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.118.174.239/32,no-resolve))
  ... and 325 more
```

**Removed: 5** (showing first 5)
```
  - [SukkaW AI] 008b9f4f529d  DOMAIN,inference.codeium.com
  - [SukkaW AI] 1c7247bf5d58  DOMAIN,server.self-serve.windsurf.com
  - [SukkaW AI] 2ac458b39d5e  DOMAIN,server.codeium.com
  - [SukkaW AI] 7c41d7205568  DOMAIN-SUFFIX,sora.com
  - [ConnersHua AI] 97841db724f6  DOMAIN-SUFFIX,zed.dev
```

## Download.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 4e884bf59743  DOMAIN,update.windsurf.com
```

## Global.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 Global] 7c41d7205568  DOMAIN-SUFFIX,sora.com
```

**Removed: 3** (showing first 3)
```
  - [blackmatrix7 Global] c55c2b010c2c  DOMAIN-SUFFIX,codeiumdata.com
  - [blackmatrix7 Global] cb6008a15c2b  DOMAIN-SUFFIX,windsurf.com
  - [blackmatrix7 Global] e85b1a3db0b5  DOMAIN-SUFFIX,codeium.com
```
