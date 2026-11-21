# Surge Rule Diff Report
Generated: 2026-11-21T13:03:34.157088

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 33 |
| Rules removed | 61 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Download.list | 1663 | 1611 | +8 | -60 | ~0 |
| Global.list | 24611 | 24635 | +24 | -0 | ~0 |
| Speedtest.list | 1725 | 1725 | +1 | -1 | ~0 |

## Download.list

**Added: 8** (showing first 8)
```
  + [SukkaW Download] 0b58b00de4c5  DOMAIN,cursor.blob.core.windows.net
  + [Manual Rules] 19e47f4f08d2  DOMAIN,openaicomproductionae4b.blob.core.windows.net
  + [Manual Rules] 4354295a201e  DOMAIN,repo.packagist.org
  + [SukkaW Download] 8d203a523ba0  DOMAIN,comaps-cdn.s3-website.cloud.ru
  + [Manual Rules] a161b1485d96  DOMAIN,registry.k8s.io
  + [Manual Rules] aaaad232dd33  URL-REGEX,^https?://(?i:(?:[a-z0-9-]+\.)+gvt[0-9]\.com)(?::(?:80|443))?/edgedl(?:[/?#]|$)
  + [Manual Rules] bd47d108964a  DOMAIN,dl.k8s.io
  + [Manual Rules] d9da39fc97c0  DOMAIN,registry.yarnpkg.com
```

**Removed: 60** (showing first 60)
```
  - [SukkaW Download] 027d1891be4a  DOMAIN-SUFFIX,archive.org
  - [SukkaW Download] 041f7f32160d  DOMAIN-SUFFIX,delivery.mp.microsoft.com
  - [SukkaW Download] 0b139f2b7c99  DOMAIN,download.visualstudio.microsoft.com
  - [SukkaW Download] 10ca1b18b457  DOMAIN-SUFFIX,oss-me-east-1.aliyuncs.com
  - [SukkaW Download] 1c06aca13d54  DOMAIN-SUFFIX,packagist.org
  - [SukkaW Download] 26e13be287f0  DOMAIN-SUFFIX,cloud-object-storage.appdomain.cloud
  - [SukkaW Download] 27f6608344c9  DOMAIN-SUFFIX,update.microsoft.com
  - [SukkaW Download] 2cb60a187bcf  DOMAIN-SUFFIX,oss-cn-hongkong.aliyuncs.com
  - [SukkaW Download] 31d72ebbc5a8  DOMAIN-SUFFIX,mvnrepository.com
  - [SukkaW Download] 3719e9e63413  DOMAIN-SUFFIX,yarnpkg.com
  - [SukkaW Download] 373ff12a8c11  DOMAIN-SUFFIX,s3.us-west-2.amazonaws.com
  - [SukkaW Download] 376124cdf626  DOMAIN-SUFFIX,s3.us-west-002.backblazeb2.com
  - [SukkaW Download] 3a2911a0bc5e  DOMAIN-SUFFIX,oss-ap-southeast-1.aliyuncs.com
  - [SukkaW Download] 3c6f50070ba9  DOMAIN-SUFFIX,oss-eu-west-1.aliyuncs.com
  - [SukkaW Download] 3fa1754954af  DOMAIN-SUFFIX,oss-accelerate-overseas.aliyuncs.com
  - [SukkaW Download] 411f4937dd4a  DOMAIN-SUFFIX,digitaloceanspaces.com
  - [SukkaW Download] 4e6d80706095  DOMAIN-SUFFIX,oss-ap-southeast-7.aliyuncs.com
  - [SukkaW Download] 616d7bde6a2b  DOMAIN-SUFFIX,cdn77-storage.com
  - [SukkaW Download] 621af019fe98  DOMAIN-SUFFIX,ks3-cn-hk-1.ksyuncs.com
  - [SukkaW Download] 64411357da80  DOMAIN-SUFFIX,cos.ap-singapore.myqcloud.com
  - [SukkaW Download] 6515cc4ef57a  DOMAIN-SUFFIX,linodeobjects.com
  - [SukkaW Download] 6718182ccbcd  DOMAIN-SUFFIX,oss-ap-southeast-5.aliyuncs.com
  - [SukkaW Download] 6a48ccc330a1  DOMAIN-SUFFIX,oss-ap-south-1.aliyuncs.com
  - [SukkaW Download] 6ce39dd537bd  DOMAIN-SUFFIX,file.core.windows.net
  - [SukkaW Download] 6ea2d13fa2f0  DOMAIN-SUFFIX,oss-ap-southeast-3.aliyuncs.com
  - [SukkaW Download] 6ee962633cbf  DOMAIN-SUFFIX,cos.ap-hongkong.myqcloud.com
  - [SukkaW Download] 6fd5d788737a  DOMAIN-SUFFIX,public.blob.vercel-storage.com
  - [SukkaW Download] 72132f50aca9  DOMAIN-SUFFIX,cos.na-ashburn.myqcloud.com
  - [SukkaW Download] 7a3affbfca8a  DOMAIN-SUFFIX,s3-accelerate.amazonaws.com
  - [SukkaW Download] 7adb29ab8867  DOMAIN-SUFFIX,cos.ap-jakarta.myqcloud.com
  - [SukkaW Download] 7b9d15e9ff24  DOMAIN-SUFFIX,cos.na-siliconvalley.myqcloud.com
  - [SukkaW Download] 7c5f6fd9507a  DOMAIN-SUFFIX,ks3-rus.ksyuncs.com
  - [SukkaW Download] 817045286df0  DOMAIN-SUFFIX,ftp-master.debian.org
  - [SukkaW Download] 829608e54e2b  DOMAIN-SUFFIX,ks3-sgp.ksyuncs.com
  - [SukkaW Download] 82af49c6764b  DOMAIN-SUFFIX,oss-ap-southeast-2.aliyuncs.com
  - [SukkaW Download] 8ca6e89921fa  DOMAIN-SUFFIX,oss-us-west-1.aliyuncs.com
  - [SukkaW Download] 8ecb8ab62d13  DOMAIN-SUFFIX,oss-eu-central-1.aliyuncs.com
  - [SukkaW Download] 8f9ee973981d  DOMAIN-SUFFIX,vultrobjects.com
  - [SukkaW Download] 92979802935e  DOMAIN-SUFFIX,cos.eu-frankfurt.myqcloud.com
  - [SukkaW Download] 9330cb7dcd51  DOMAIN-SUFFIX,oss-us-east-1.aliyuncs.com
  - [SukkaW Download] 93602f2474f8  DOMAIN-SUFFIX,r2.dev
  - [SukkaW Download] 9712d3dcbebb  DOMAIN-SUFFIX,s3-website.cloud.ru
  - [SukkaW Download] a42b6d19981b  DOMAIN,ctldl.windowsupdate.com
  - [SukkaW Download] a4a7b4527a18  DOMAIN-SUFFIX,oss-ap-northeast-2.aliyuncs.com
  - [SukkaW Download] a70ba85c4ff3  DOMAIN-SUFFIX,cos.sa-saopaulo.myqcloud.com
  - [SukkaW Download] af2d32761982  DOMAIN-SUFFIX,t3.storageapi.dev
  - [SukkaW Download] b062e6b5dd90  DOMAIN-SUFFIX,blob.core.windows.net
  - [SukkaW Download] b14484db25d5  DOMAIN-SUFFIX,s3.yandex.net
  - [Manual Rules] b204346e4e3a  URL-REGEX,^http://(.+)\.gvt\d\.com/edgedl
  - [SukkaW Download] b8e01898952c  DOMAIN-SUFFIX,cos.ap-tokyo.myqcloud.com
  - [SukkaW Download] bd656192f417  DOMAIN-SUFFIX,oss-ap-southeast-6.aliyuncs.com
  - [SukkaW Download] bfd3dd0df044  DOMAIN-SUFFIX,oss-ap-northeast-1.aliyuncs.com
  - [SukkaW Download] d0fa282992af  DOMAIN-SUFFIX,cloudflarestorage.com
  - [SukkaW Download] d6297d60f87f  DOMAIN-SUFFIX,k8s.io
  - [SukkaW Download] da7444cc0bdb  DOMAIN-SUFFIX,cos.na-toronto.myqcloud.com
  - [SukkaW Download] db40e07ba0c3  DOMAIN,officecdn-microsoft-com.akamaized.net
  - [SukkaW Download] ec7bdda70712  DOMAIN-SUFFIX,cos.ap-bangkok.myqcloud.com
  - [SukkaW Download] f95af05fdbf9  DOMAIN-SUFFIX,cos.ap-mumbai.myqcloud.com
  - [SukkaW Download] fd533d082636  DOMAIN-SUFFIX,cos.ap-seoul.myqcloud.com
  - [SukkaW Download] ff258dfa8b1b  DOMAIN-SUFFIX,s3-global.amazonaws.com
```

## Global.list

**Added: 24** (showing first 24)
```
  + [blackmatrix7 Global] 027d1891be4a  DOMAIN-SUFFIX,archive.org
  + [blackmatrix7 Global] 10ca1b18b457  DOMAIN-SUFFIX,oss-me-east-1.aliyuncs.com
  + [blackmatrix7 Global] 1c06aca13d54  DOMAIN-SUFFIX,packagist.org
  + [blackmatrix7 Global] 2cb60a187bcf  DOMAIN-SUFFIX,oss-cn-hongkong.aliyuncs.com
  + [blackmatrix7 Global] 31d72ebbc5a8  DOMAIN-SUFFIX,mvnrepository.com
  + [blackmatrix7 Global] 3719e9e63413  DOMAIN-SUFFIX,yarnpkg.com
  + [blackmatrix7 Global] 3a2911a0bc5e  DOMAIN-SUFFIX,oss-ap-southeast-1.aliyuncs.com
  + [blackmatrix7 Global] 3c6f50070ba9  DOMAIN-SUFFIX,oss-eu-west-1.aliyuncs.com
  + [blackmatrix7 Global] 411f4937dd4a  DOMAIN-SUFFIX,digitaloceanspaces.com
  + [blackmatrix7 Global] 4e6d80706095  DOMAIN-SUFFIX,oss-ap-southeast-7.aliyuncs.com
  + [blackmatrix7 Global] 6718182ccbcd  DOMAIN-SUFFIX,oss-ap-southeast-5.aliyuncs.com
  + [blackmatrix7 Global] 6a48ccc330a1  DOMAIN-SUFFIX,oss-ap-south-1.aliyuncs.com
  + [blackmatrix7 Global] 6ea2d13fa2f0  DOMAIN-SUFFIX,oss-ap-southeast-3.aliyuncs.com
  + [blackmatrix7 Global] 82af49c6764b  DOMAIN-SUFFIX,oss-ap-southeast-2.aliyuncs.com
  + [blackmatrix7 Global] 8ca6e89921fa  DOMAIN-SUFFIX,oss-us-west-1.aliyuncs.com
  + [blackmatrix7 Global] 8ecb8ab62d13  DOMAIN-SUFFIX,oss-eu-central-1.aliyuncs.com
  + [blackmatrix7 Global] 9330cb7dcd51  DOMAIN-SUFFIX,oss-us-east-1.aliyuncs.com
  + [blackmatrix7 Global] 93602f2474f8  DOMAIN-SUFFIX,r2.dev
  + [blackmatrix7 Global] a4a7b4527a18  DOMAIN-SUFFIX,oss-ap-northeast-2.aliyuncs.com
  + [blackmatrix7 Global] b062e6b5dd90  DOMAIN-SUFFIX,blob.core.windows.net
  + [blackmatrix7 Global] bd656192f417  DOMAIN-SUFFIX,oss-ap-southeast-6.aliyuncs.com
  + [blackmatrix7 Global] bfd3dd0df044  DOMAIN-SUFFIX,oss-ap-northeast-1.aliyuncs.com
  + [blackmatrix7 Global] d0fa282992af  DOMAIN-SUFFIX,cloudflarestorage.com
  + [blackmatrix7 Global] d6297d60f87f  DOMAIN-SUFFIX,k8s.io
```

## Speedtest.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 84a1bcca8116  URL-REGEX,^http://mirror\.nforce\.com:8080/speedtest(?:[/?#]|$)
```

**Removed: 1** (showing first 1)
```
  - [SukkaW Speedtest Servers International] 54bf5777c659  DOMAIN,mirror.nforce.com
```
