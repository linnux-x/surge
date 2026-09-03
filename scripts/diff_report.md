# Surge Rule Diff Report
Generated: 2026-09-04T05:01:18.601462

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 32 |
| Rules removed | 145 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| Apple_CN.list | 229 | 230 | +1 | -0 | ~0 |
| CDN.list | 31 | 29 | +0 | -2 | ~0 |
| China.list | 111213 | 111100 | +29 | -142 | ~0 |
| Download.list | 1685 | 1687 | +2 | -0 | ~0 |
| Microsoft_CDN.list | 81 | 80 | +0 | -1 | ~0 |

## Apple_CN.list

**Added: 1** (showing first 1)
```
  + [SukkaW Apple CDN] 6854f39d4d53  DOMAIN-SUFFIX,gspe11-2-cn-ssl.ls.apple.com
```

## CDN.list

**Removed: 2** (showing first 2)
```
  - [SukkaW CDN] b87208ee0739  DOMAIN-KEYWORD,fonts.hanime1
  - [SukkaW CDN] e04968ef2a45  DOMAIN-KEYWORD,vdownload.hanime1
```

## China.list

**Added: 29** (showing first 29)
```
  + [blackmatrix7 ChinaMaxNoIP Domain] 00dc05b5a8e2  DOMAIN-SUFFIX,kyxinli.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 22af82fa4f76  DOMAIN-SUFFIX,qimyu.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 258261aa070a  DOMAIN-SUFFIX,ftj003.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 2b8fa683b6cb  DOMAIN-SUFFIX,bartender-cn.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 2cf83f6878a4  DOMAIN-SUFFIX,dadacart.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 3002f8c578d9  DOMAIN-SUFFIX,cloudflvare.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 325fcc7efe74  DOMAIN-SUFFIX,echartnow.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 3e6df89047a6  DOMAIN-SUFFIX,zxc123zxc123.xyz
  + [blackmatrix7 ChinaMaxNoIP Domain] 4e655f91d5d5  DOMAIN-SUFFIX,ydkkej.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 6441879d8134  DOMAIN-SUFFIX,quhaotui.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 70a6e7c8bf4c  DOMAIN-SUFFIX,qflyinc.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 7e1cb137124f  DOMAIN-SUFFIX,wrilab.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 81a06dc5ca7b  DOMAIN-SUFFIX,huayin99.com
  + [blackmatrix7 ChinaMaxNoIP Domain] 8c886e0c39aa  DOMAIN-SUFFIX,888fk.cc
  + [blackmatrix7 ChinaMaxNoIP Domain] 98f2a01a2d23  DOMAIN-SUFFIX,969mak.com
  + [blackmatrix7 ChinaMaxNoIP Domain] a1b7e3f81d15  DOMAIN-SUFFIX,suifengy.com
  + [blackmatrix7 ChinaMaxNoIP Domain] a4da7d842e57  DOMAIN-SUFFIX,bhjh168.com
  + [blackmatrix7 ChinaMaxNoIP Domain] c324db3befab  DOMAIN-SUFFIX,tgalileo.com
  + [blackmatrix7 ChinaMaxNoIP Domain] c32e77b7b6e5  DOMAIN-SUFFIX,evhzzh.com
  + [blackmatrix7 ChinaMaxNoIP Domain] c634e3562ca8  DOMAIN-SUFFIX,gdyfxx.com
  + [blackmatrix7 ChinaMaxNoIP Domain] c87fd48c75a0  DOMAIN-SUFFIX,w0028.cc
  + [blackmatrix7 ChinaMaxNoIP Domain] ce89de9404bd  DOMAIN-SUFFIX,jlmy.com
  + [blackmatrix7 ChinaMaxNoIP Domain] d0075b9d6274  DOMAIN-SUFFIX,jwangzhong.com
  + [blackmatrix7 ChinaMaxNoIP Domain] dd4ce930b17d  DOMAIN-SUFFIX,bsbsb.xyz
  + [blackmatrix7 ChinaMaxNoIP Domain] df6356709b4e  DOMAIN-SUFFIX,bkd898.com
  + [blackmatrix7 ChinaMaxNoIP Domain] e2555455a644  DOMAIN-SUFFIX,longcat.chat
  + [blackmatrix7 ChinaMaxNoIP Domain] edb55894cec0  DOMAIN-SUFFIX,jdo2c.com
  + [blackmatrix7 ChinaMaxNoIP Domain] f0890c890286  DOMAIN-SUFFIX,czsvip.com
  + [blackmatrix7 ChinaMaxNoIP Domain] f24fb211c5c1  DOMAIN-SUFFIX,scqbyy.com
```

**Removed: 142** (showing first 100)
```
  - [blackmatrix7 ChinaMaxNoIP Domain] 0169c35ae137  DOMAIN-SUFFIX,s1blseclvira.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0325ec41d27c  DOMAIN-SUFFIX,51gowan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0787e1cdbbe6  DOMAIN-SUFFIX,yulins.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0890934bdb1a  DOMAIN-SUFFIX,iwatch365.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0d8b31d8a327  DOMAIN-SUFFIX,ccsfuchan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0db687e510b9  DOMAIN-SUFFIX,7fa973f8c7bdcddb.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0e56a2826b7a  DOMAIN-SUFFIX,aai07260mu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0ebd4b1e0f3e  DOMAIN-SUFFIX,iquhuo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 0f3fbd93f1d3  DOMAIN-SUFFIX,ebb6ea72919edea2.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 12f04df2b38f  DOMAIN-SUFFIX,zz2024.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1376ad2161ca  DOMAIN-SUFFIX,51jinkang.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1c01a6eaf208  DOMAIN-SUFFIX,c944748d38bcc258.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1d876d09369f  DOMAIN-SUFFIX,0olut8.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1e302197a8e1  DOMAIN-SUFFIX,890bf715220716f3.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1e4dc22e3927  DOMAIN-SUFFIX,24dab50b3223e582.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 1f2cb9793768  DOMAIN-SUFFIX,2dffbc61dea7ca0a.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 20f75c0a7780  DOMAIN-SUFFIX,2026cname.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 24de2d0cc344  DOMAIN-SUFFIX,rcswo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2584b0f5e723  DOMAIN-SUFFIX,d8e8664c05df452c.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 27f4dd04f1cf  DOMAIN-SUFFIX,6d576388add270c5.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2b175578da09  DOMAIN-SUFFIX,henri.ren
  - [blackmatrix7 ChinaMaxNoIP Domain] 2d3071e94d0c  DOMAIN-SUFFIX,b19a352d2336941a.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2d3dd7ba40fc  DOMAIN-SUFFIX,ab839c2562b8ae05.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2de66a7ce915  DOMAIN-SUFFIX,tech2ipo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 2fd09cc25b88  DOMAIN-SUFFIX,guangxipubeihuaheng.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 307bac587125  DOMAIN-SUFFIX,a42c6d113874e1f3.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3149a71c6b17  DOMAIN-SUFFIX,e307586127f21050.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 360f75fbce1e  DOMAIN-SUFFIX,lyrics.run
  - [blackmatrix7 ChinaMaxNoIP Domain] 36394beb3060  DOMAIN-SUFFIX,chenhui.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 3ab31cb70c27  DOMAIN-SUFFIX,fulltech.work
  - [blackmatrix7 ChinaMaxNoIP Domain] 3b644e1af0eb  DOMAIN-SUFFIX,430d6eba715dabb4.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3cfa9e698aba  DOMAIN-SUFFIX,92jzh.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3d1b3c5a0226  DOMAIN-SUFFIX,kunlunce.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 3ee0c344aac4  DOMAIN-SUFFIX,01be6bfabbd3024a.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4008e6fef4b5  DOMAIN-SUFFIX,sb1secapply4.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 40da5c957ebc  DOMAIN-SUFFIX,6b3cfa277bae3b4b.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4226a4780ba5  DOMAIN-SUFFIX,f8167007e7bf667d.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 42279ecda17e  DOMAIN-SUFFIX,9c0c0433602d188a.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 42cdf66a5662  DOMAIN-SUFFIX,gdtcoin.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 47d520d2f535  DOMAIN-SUFFIX,qiluhr.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 48a4d42c2495  DOMAIN-SUFFIX,cnnbsa.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 48b523546a2c  DOMAIN-SUFFIX,czhjs.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 499caa9ae002  DOMAIN-SUFFIX,dalwiakieyne.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4cdc0936fd4b  DOMAIN-SUFFIX,dalwiaresham.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4dd66e3546b8  DOMAIN-SUFFIX,a0fca7a55be096ef.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4e96720eee36  DOMAIN-SUFFIX,8243d76487f3a834.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 4f7f73feda03  DOMAIN-SUFFIX,0264032a252fcf53.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 525bc463e8d6  DOMAIN-SUFFIX,netinfi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 54d579a9f8eb  DOMAIN-SUFFIX,ca91a5eb7ed4495e.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 595b47a58b94  DOMAIN-SUFFIX,nativosink.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 59de240f9f16  DOMAIN-SUFFIX,gxtianmiao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5b3fbf6cd8e3  DOMAIN-SUFFIX,juyutube.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5b9af1274291  DOMAIN-SUFFIX,radiowar.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 5d2a97b9654e  DOMAIN-SUFFIX,xiangauto.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 5d3078ea6211  DOMAIN-SUFFIX,ec6056a95386f752.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 60181b32ad30  DOMAIN-SUFFIX,gaoyawang.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 60842601d3bb  DOMAIN-SUFFIX,mskoo.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 663a96ccf6d1  DOMAIN-SUFFIX,72d3bb672f4a6997.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 68dd4ad61c75  DOMAIN-SUFFIX,ma3office.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6a20de4d5ffa  DOMAIN-SUFFIX,closertb.site
  - [blackmatrix7 ChinaMaxNoIP Domain] 6b5f61154b56  DOMAIN-SUFFIX,anyskygame.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6bcc34666b78  DOMAIN-SUFFIX,junshencm.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6c5481507b97  DOMAIN-SUFFIX,americachineselife.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6c9ac97ea2dc  DOMAIN-SUFFIX,imeyahair.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6e0d141a40da  DOMAIN-SUFFIX,youkexueyuan.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 6e52c5b4981f  DOMAIN-SUFFIX,word666.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 70ce5ee52541  DOMAIN-SUFFIX,code-by.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 70dc05baf200  DOMAIN-SUFFIX,2c5bf25c11b8dc3e.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 726c413d281c  DOMAIN-SUFFIX,dachaoshan.org
  - [blackmatrix7 ChinaMaxNoIP Domain] 74a38547e3d0  DOMAIN-SUFFIX,5185.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] 750dd1f3eecf  DOMAIN-SUFFIX,qaqa555.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 75e39382afed  DOMAIN-SUFFIX,d65fee3222cbaf80.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 77469da121cd  DOMAIN-SUFFIX,s1blsecgerto.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 7a35b5f37fd6  DOMAIN-SUFFIX,3774cd2332503d45.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 7bcd1eec4d95  DOMAIN-SUFFIX,aai07251mu.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 87506a7da5f4  DOMAIN-SUFFIX,8333dhz.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 8889ae2c80a7  DOMAIN-SUFFIX,ceniiat.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 8af757425823  DOMAIN-SUFFIX,pioneernews.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] 8cbc692fa15e  DOMAIN-SUFFIX,zbczce.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 8d40884ff784  DOMAIN-SUFFIX,68e5fc2c1344afb8.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 8e8eaaa21012  DOMAIN-SUFFIX,wanghaifeng.net
  - [blackmatrix7 ChinaMaxNoIP Domain] 90acf826e5a7  DOMAIN-SUFFIX,jijijijin.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 97f7fbeade61  DOMAIN-SUFFIX,along96.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 98713940e086  DOMAIN-SUFFIX,lianshun.cc
  - [blackmatrix7 ChinaMaxNoIP Domain] 98bc924fd6d7  DOMAIN-SUFFIX,669167d4fc316421.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 99c8af6e3b4a  DOMAIN-SUFFIX,abtpaper.com
  - [blackmatrix7 ChinaMaxNoIP Domain] 9b4d1f9e1f90  DOMAIN-SUFFIX,3d503a99384e0d4c.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a094a4800744  DOMAIN-SUFFIX,objccn.io
  - [blackmatrix7 ChinaMaxNoIP Domain] a21d6d2d5275  DOMAIN-SUFFIX,3feb063cbf96bd40.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a58b964cf4a1  DOMAIN-SUFFIX,gxzhentao.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a62112d22e23  DOMAIN-SUFFIX,mouratoriousi.com
  - [blackmatrix7 ChinaMaxNoIP Domain] a6c777f1e85f  DOMAIN-SUFFIX,xacyyxq.com
  - [blackmatrix7 ChinaMaxNoIP Domain] aa42dfa94a8a  DOMAIN-SUFFIX,shaaidata.com
  - [blackmatrix7 ChinaMaxNoIP Domain] ab33c8719ba3  DOMAIN-SUFFIX,dzvv.com
  - [blackmatrix7 ChinaMaxNoIP Domain] ac53357b876d  DOMAIN-SUFFIX,0616a9dbe68fac9c.com
  - [blackmatrix7 ChinaMaxNoIP Domain] ae0060eb4d60  DOMAIN-SUFFIX,orangesgame.com
  - [blackmatrix7 ChinaMaxNoIP Domain] af560dce1a4f  DOMAIN-SUFFIX,tly.cloud
  - [blackmatrix7 ChinaMaxNoIP Domain] b12c632cb6e2  DOMAIN-SUFFIX,ltesting.net
  - [blackmatrix7 ChinaMaxNoIP Domain] b6e887b268cf  DOMAIN-SUFFIX,fjvs.org
  - [blackmatrix7 ChinaMaxNoIP Domain] bcb8094c7613  DOMAIN-SUFFIX,gxwenyutech.com
  ... and 42 more
```

## Download.list

**Added: 2** (showing first 2)
```
  + [SukkaW Download] b7adf4e6e59c  DOMAIN,cdn.dyn.com
  + [SukkaW Download] bea3077b638f  DOMAIN,assets-tcpviewer.proxyman.com
```

## Microsoft_CDN.list

**Removed: 1** (showing first 1)
```
  - [SukkaW Microsoft CDN] 132a9ff4fd2e  DOMAIN-SUFFIX,cn.windowssearch.com
```
