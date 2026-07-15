# Surge Rule Diff Report
Generated: 2026-07-16T05:01:10.628171

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 50 |
| Rules removed | 246 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 112141 | 111938 | +31 | -234 | ~0 |
| China_IP.list | 11431 | 11432 | +2 | -1 | ~0 |
| Download.list | 1693 | 1685 | +1 | -9 | ~0 |
| Global.list | 24123 | 24139 | +16 | -0 | ~0 |
| Microsoft_CDN.list | 83 | 81 | +0 | -2 | ~0 |

## China.list

**Added: 31** (showing first 31)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 2162474a6128  DOMAIN-SUFFIX,hcdns21.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 29f064775227  DOMAIN-SUFFIX,hainanyuyue.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 2a65b9509fa1  DOMAIN-SUFFIX,yichengwlkj.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 3d70dd31a3ad  DOMAIN-SUFFIX,jlcpcb.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 467b32f977ac  DOMAIN-SUFFIX,musiclemon.net
  + [blackmatrix7 ChinaMaxNoIP Domain] 4a2a9ff1b330  DOMAIN-SUFFIX,cfdns5.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 4e1e0d7484ce  DOMAIN-SUFFIX,okywqapp.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 5a8a1b901693  DOMAIN-SUFFIX,cfdns43.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 5e4396912c33  DOMAIN-SUFFIX,lemonedrum.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 6d9d343ab7ca  DOMAIN-SUFFIX,gaojidata.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 80a7b96adc0e  DOMAIN-SUFFIX,gzasc.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 859108b27411  DOMAIN-SUFFIX,arcadesos.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 9048a3b7a3d0  DOMAIN-SUFFIX,dulupay.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 933edbe18075  DOMAIN-SUFFIX,ibidmob.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 9a17a434e37b  DOMAIN-SUFFIX,manjuu.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 9c74a1786988  DOMAIN-SUFFIX,weboss.hk
  + [blackmatrix7 ChinaMaxNoIP Domain] 9f59493b3c02  DOMAIN-SUFFIX,rrsp.app
  + [blackmatrix7 ChinaMaxNoIP Domain] a60980b196aa  DOMAIN-SUFFIX,myndj.com
  + [blackmatrix7 ChinaMaxNoIP Domain] b2d60a89dafe  DOMAIN-SUFFIX,linbeigame.com
  + [blackmatrix7 ChinaMaxNoIP Domain] b6bf6a7bb49e  DOMAIN-SUFFIX,adglim.com
  + [blackmatrix7 ChinaMaxNoIP Domain] ba05659f4f07  DOMAIN-SUFFIX,ksepton.com
  + [blackmatrix7 ChinaMaxNoIP Domain] bff122ff5b8c  DOMAIN-SUFFIX,yzsgo.com
  + [blackmatrix7 ChinaMaxNoIP Domain] c953ffb7ee73  DOMAIN-SUFFIX,shortdramaop.com
  + [blackmatrix7 ChinaMaxNoIP Domain] d0f4f9241098  DOMAIN,live.qinyangtv.com
  + [blackmatrix7 ChinaMaxNoIP Domain] d2820e1f3119  DOMAIN-SUFFIX,tglsinsure.com
  + [blackmatrix7 ChinaMaxNoIP Domain] e14774959907  DOMAIN-SUFFIX,qwdjapp.com
  + [blackmatrix7 ChinaMaxNoIP Domain] e71bbcbab059  DOMAIN-SUFFIX,oldmanemu.org
  + [blackmatrix7 ChinaMaxNoIP Domain] f3b76afc3fb1  DOMAIN,developer.microsoft.com
  + [blackmatrix7 ChinaMaxNoIP Domain] f78b6002764e  DOMAIN-SUFFIX,goshare2.com
  + [blackmatrix7 ChinaMaxNoIP Domain] f8f11e234ffd  DOMAIN-SUFFIX,ytj9999.com
  + [blackmatrix7 ChinaMaxNoIP Domain] ffb0abafa609  DOMAIN-SUFFIX,szlcmb.com
```

**Removed: 234** (showing first 100)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 01c9935dd410  DOMAIN-SUFFIX,chinafilmhy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 01f9f7470b17  DOMAIN-SUFFIX,6786666.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 02dcc9ee491f  DOMAIN-SUFFIX,nomuaheridan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 031600e53eea  DOMAIN-SUFFIX,zizige.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 03b2def180da  DOMAIN-SUFFIX,to4f.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 04c688797d65  DOMAIN-SUFFIX,zhongjianyiliao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 05b405e50da4  DOMAIN-SUFFIX,136fc.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0666cc7ac9fc  DOMAIN-SUFFIX,ckqjyjq.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 078047d2fec0  DOMAIN-SUFFIX,jzmjtjn.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 0929667fb2bb  DOMAIN-SUFFIX,77dd23.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0b008cca05ed  DOMAIN-SUFFIX,sdcgc.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0c05572aa884  DOMAIN-SUFFIX,itdog-dns.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0ccbef1b0b2e  DOMAIN-SUFFIX,4399-xyx.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0d105a9769dc  DOMAIN-SUFFIX,ie57.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0d3edcc11694  DOMAIN-SUFFIX,20images10.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 10e53cc2b796  DOMAIN-SUFFIX,163cdn.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 138256afd69e  DOMAIN-SUFFIX,data4h.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 18a0abcf8029  DOMAIN-SUFFIX,hzgymd.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 18acec37586e  DOMAIN-SUFFIX,ssjljk.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 18c333153b5f  DOMAIN-SUFFIX,20images7.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1963fb80660a  DOMAIN-SUFFIX,52dy.tv
  - [blackmatrix7 ChinaMaxNoIP Domain] 1b0d7dabbe8a  DOMAIN-SUFFIX,sifangvideo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1b778a1bde4b  DOMAIN-SUFFIX,ddsiojf.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 1bce6c454487  DOMAIN-SUFFIX,yanglaotiandi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1c27a705e761  DOMAIN-SUFFIX,xvjhzuc.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1fba66109bdc  DOMAIN-SUFFIX,yzhejin.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 20205aa94108  DOMAIN-SUFFIX,0rz.ltd
  - [blackmatrix7 ChinaMaxNoIP Domain] 2029519196df  DOMAIN-SUFFIX,lazybios.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 203256729023  DOMAIN-SUFFIX,tjjinglang.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2307655e16dd  DOMAIN-SUFFIX,hkdzxs.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2382723ab5f2  DOMAIN-SUFFIX,03fugu.xin
  - [blackmatrix7 ChinaMaxNoIP Domain] 24b4f40e39da  DOMAIN-SUFFIX,dnstx88.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] 24b6fe7c3170  DOMAIN-SUFFIX,domp4.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 24e117a44522  DOMAIN-SUFFIX,yxad.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 24e52f5cce9d  DOMAIN-SUFFIX,yoohouse.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 250a0ed3f024  DOMAIN-SUFFIX,msjy123.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 289009bdcb33  DOMAIN-SUFFIX,wkkshu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2b086eab12dd  DOMAIN-SUFFIX,noomuuhapmav.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2b37bf96ab38  DOMAIN-SUFFIX,lzdymy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3047a8da33c7  DOMAIN-SUFFIX,ohqly.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3081b82e556b  DOMAIN-SUFFIX,yhdd365.shop
  - [blackmatrix7 ChinaMaxNoIP Domain] 31ab39f7f37f  DOMAIN-SUFFIX,sjxyx.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 31b8aa83150e  DOMAIN-SUFFIX,fzhlkx.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 31e273e703c1  DOMAIN-SUFFIX,xxxcsf.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3417fc5b3385  DOMAIN-SUFFIX,mgkjht.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 353e95f63905  DOMAIN-SUFFIX,eoofoo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 35f969bbcc68  DOMAIN-SUFFIX,qybhl.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3864757209b4  DOMAIN-SUFFIX,mouralanco.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3d402139fd2d  DOMAIN-SUFFIX,9377df.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3e6a9ddb5bac  DOMAIN-SUFFIX,quledu.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 3f490667b624  DOMAIN-SUFFIX,gugud.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3fe21be24e54  DOMAIN-SUFFIX,022shui.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4133528a7643  DOMAIN-SUFFIX,zixingxinwen.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 419e2e023afe  DOMAIN-SUFFIX,lricn.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 42da3dbf8eed  DOMAIN-SUFFIX,padao.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 435160e1aa9a  DOMAIN-SUFFIX,viyuan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 45aa60be31b0  DOMAIN-SUFFIX,ycpai.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4656ec0e5a05  DOMAIN-SUFFIX,whiee.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4665a214bfaa  DOMAIN-SUFFIX,0001700.xin
  - [blackmatrix7 ChinaMaxNoIP Domain] 4c8d11d58a82  DOMAIN-SUFFIX,20yy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4e29c8b7a0f7  DOMAIN-SUFFIX,yxgxz.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4e39a8007960  DOMAIN-SUFFIX,tynlwx.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4ebfc8a47561  DOMAIN-SUFFIX,cfrlr.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4f06f93549fe  DOMAIN-SUFFIX,fwqje67h.work
  - [blackmatrix7 ChinaMaxNoIP Domain] 51b180895724  DOMAIN-SUFFIX,shpyedu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 51c45c2a4bf6  DOMAIN-SUFFIX,jnryc.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 52fd57eebcb8  DOMAIN-SUFFIX,pting.club
  - [blackmatrix7 ChinaMaxNoIP Domain] 53512da2944b  DOMAIN-SUFFIX,xacg.info
  - [blackmatrix7 ChinaMaxNoIP Domain] 539db45293b7  DOMAIN-SUFFIX,pandafoundation.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 542219852c44  DOMAIN-SUFFIX,qysgf.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 56d76f132ded  DOMAIN-SUFFIX,lohasor.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 573014e40fe5  DOMAIN-SUFFIX,0range5.xin
  - [blackmatrix7 ChinaMaxNoIP Domain] 5a29693a152b  DOMAIN-SUFFIX,gczyg.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5b3fd91b1298  DOMAIN-SUFFIX,xxcmw.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5bbf5e96fc11  DOMAIN-SUFFIX,longxinli.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5e2e6e7a61d9  DOMAIN-SUFFIX,20images21.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5e536f18b796  DOMAIN-SUFFIX,zhenfangyuan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5efbcf36c661  DOMAIN-SUFFIX,1488.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6108b81c5d69  DOMAIN-SUFFIX,spoience.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6170db5df624  DOMAIN-SUFFIX,hsybyh.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 63233476a94a  DOMAIN-SUFFIX,mrhs.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] 6361e3c25532  DOMAIN-SUFFIX,nanguache.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 644897bdee84  DOMAIN-SUFFIX,hcwh.ltd
  - [blackmatrix7 ChinaMaxNoIP Domain] 66f2bb06d219  DOMAIN-SUFFIX,yilinweb.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6734f37e728e  DOMAIN-SUFFIX,ppthi-hoo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 68ff058a83e3  DOMAIN-SUFFIX,mouraeodor.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6bce794d6cd1  DOMAIN-SUFFIX,yetianzi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6c02cfa5d474  DOMAIN-SUFFIX,tceic.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6cab94af8536  DOMAIN-SUFFIX,bojie.bid
  - [blackmatrix7 ChinaMaxNoIP Domain] 6d1e068504df  DOMAIN-SUFFIX,pwjptdg.xyz
  - [blackmatrix7 ChinaMaxNoIP Domain] 6d49755462e2  DOMAIN-SUFFIX,gbeca.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 6dfcd3f96cfc  DOMAIN-SUFFIX,jnjszl.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6edc812ed335  DOMAIN-SUFFIX,jdtjy.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 7050f1770429  DOMAIN-SUFFIX,30888.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 70627f52d58e  DOMAIN-SUFFIX,ufo.club
  - [blackmatrix7 ChinaMaxNoIP Domain] 7152e3dfe596  DOMAIN-SUFFIX,zongxiankj.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 745a3063c093  DOMAIN-SUFFIX,xm002.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 74c8b86e0f2d  DOMAIN-SUFFIX,yingpengbz.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 74e6eb662995  DOMAIN-SUFFIX,hfxczj.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 7554ddadb435  DOMAIN-SUFFIX,gdfjsh.org
  ... and 134 more
```

## China_IP.list

**Added: 2** (showing first 2)
```
  + [blackmatrix7 China IPs] 1d61b0407e6a  IP-CIDR,218.252.64.0/19
  + [blackmatrix7 China IPs] 6a254dc81814  IP-CIDR,218.252.0.0/18
```

**Removed: 1** (showing first 1)
```
  - [blackmatrix7 China IPs] 3bd4e15197f2  IP-CIDR,218.252.0.0/17
```

## Download.list

**Added: 1** (showing first 1)
```
  + [SukkaW Download] 59dda76bf44a  DOMAIN,mirror1.hcgen.de
```

**Removed: 9** (showing first 9)
```
  - [SukkaW Download] 01229e54a3ca  DOMAIN,mirror1.hs-esslingen.de
  - [SukkaW Download] 45195290b21a  DOMAIN,mirror.its.dal.ca
  - [SukkaW Download] 510a92ae41a3  DOMAIN,cdn-ota.azureedge.net
  - [SukkaW Download] 6027e9f7c28d  DOMAIN,lug.mines.edu
  - [SukkaW Download] 728a8193da3f  DOMAIN,ftp.ludd.ltu.se
  - [SukkaW Download] 9a0c2f97c34e  DOMAIN,download.fosshub.com
  - [SukkaW Download] a86e7709f493  DOMAIN,mirror.kernel.ir
  - [SukkaW Download] b4cff2a7406a  DOMAIN,centos.nic.cz
  - [SukkaW Download] c8dc320aa324  DOMAIN,mirror.battern.eu
```

## Global.list

**Added: 16** (showing first 16)
```
  + [blackmatrix7 Global] 1161d286b9c2  DOMAIN-SUFFIX,likeevideo.ru
  + [blackmatrix7 Global] 163e49bddcfc  DOMAIN,agb9r0ad.qllfkl.com
  + [blackmatrix7 Global] 2369f2d55898  DOMAIN-SUFFIX,likeeapp.ru
  + [blackmatrix7 Global] 23b2b792b43a  DOMAIN-SUFFIX,bystys.tech
  + [blackmatrix7 Global] 2989e9f418ba  DOMAIN,hb4bbbbb.pmhcjk.com
  + [blackmatrix7 Global] 476f87adf3ae  DOMAIN,nbbb1bb7.pmhcjk.com
  + [blackmatrix7 Global] 5c924d0e24c8  DOMAIN-SUFFIX,yucf.top
  + [blackmatrix7 Global] 781521cb4ec3  DOMAIN,q676790b.pmhcjk.com
  + [blackmatrix7 Global] 7a24b93f8f0d  DOMAIN-SUFFIX,chatgpt.site
  + [blackmatrix7 Global] a1d4510cd8e3  DOMAIN-SUFFIX,owxd.xyz
  + [blackmatrix7 Global] b93335265657  DOMAIN-SUFFIX,kick.com
  + [blackmatrix7 Global] c476cde61a66  DOMAIN-SUFFIX,likeevideo.com
  + [blackmatrix7 Global] d190c8b9d7ef  DOMAIN-SUFFIX,bnxz.net
  + [blackmatrix7 Global] e6fe8862af5f  DOMAIN-SUFFIX,uxzw.club
  + [blackmatrix7 Global] ed924f47f50b  DOMAIN-SUFFIX,like-video.com
  + [blackmatrix7 Global] fcbce7a09cf3  DOMAIN-SUFFIX,likee.com
```

## Microsoft_CDN.list

**Removed: 2** (showing first 2)
```
  - [SukkaW Microsoft CDN] c553f70b78d2  DOMAIN-SUFFIX,shell.cdn.office.net
  - [SukkaW Microsoft CDN] f155cf54e0a9  DOMAIN-SUFFIX,developer.microsoft.com
```
