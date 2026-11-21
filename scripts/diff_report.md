# Surge Rule Diff Report
Generated: 2026-11-21T08:55:06.587785

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 6 |
| Rules added | 20 |
| Rules removed | 210 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 127 | 123 | +0 | -4 | ~0 |
| Apple.list | 1552 | 1380 | +8 | -180 | ~0 |
| AppleMedia.list | 0 | 11 | +11 | -0 | ~0 |
| Apple_AI.list | 24 | 20 | +0 | -4 | ~0 |
| Apple_CN.list | 230 | 225 | +1 | -6 | ~0 |
| GlobalMedia.list | 2288 | 2272 | +0 | -16 | ~0 |

## AI.list

**Removed: 4** (showing first 4)
```
  - [Rabbit-Spec AIGC] 1e902f6f0f29  DOMAIN-SUFFIX,guzzoni.apple.com
  - [Rabbit-Spec AIGC] 23d8a46c106a  DOMAIN-SUFFIX,apple-relay.fastly-edge.com
  - [Rabbit-Spec AIGC] c3b7ae332522  DOMAIN-SUFFIX,gspe1-ssl.ls.apple.com
  - [Rabbit-Spec AIGC] eb9c099dc8eb  DOMAIN-SUFFIX,cp4.cloudflare.com
```

## Apple.list

**Added: 8** (showing first 8)
```
  + [Manual Rules] 4c34a6fc1ad5  DOMAIN,crl4.digicert.com
  + [Manual Rules] 89b4c7619f52  DOMAIN-SUFFIX,apple.com.akadns.net
  + [Manual Rules] 95dfdd170967  DOMAIN-SUFFIX,apple-support.akadns.net
  + [Manual Rules] aebe0efcfe6a  DOMAIN,app-site-association.networking.apple
  + [Manual Rules] b6929201bfca  DOMAIN-SUFFIX,apple.com.edgekey.net
  + [Manual Rules] d9733c43937d  DOMAIN,ocsp.digicert.com
  + [Manual Rules] ebd53c2b5637  DOMAIN,crl3.digicert.com
  + [Manual Rules] fb10b053fdf7  DOMAIN-SUFFIX,icloud.com.akadns.net
```

**Removed: 180** (showing first 100)
```
  - [blackmatrix7 Apple] 00aab0c87218  PROCESS-NAME,apsd
  - [blackmatrix7 Apple] 015431791526  DOMAIN-SUFFIX,leecountytimes.com
  - [blackmatrix7 Apple] 047266f5a490  DOMAIN-SUFFIX,wholesalediscountpurses.com
  - [blackmatrix7 Apple] 07af8d4ba938  DOMAIN-SUFFIX,salecheaphandbags.com
  - [blackmatrix7 Apple] 081e0cfc3efd  DOMAIN-SUFFIX,aanaan.com
  - [blackmatrix7 Apple] 08e39fe79f62  DOMAIN-SUFFIX,detaliczny.com
  - [blackmatrix7 Apple] 095161a77384  DOMAIN-SUFFIX,tradevip1.com
  - [blackmatrix7 Apple] 0b0f4c799b91  DOMAIN-SUFFIX,ajtalk.com
  - [blackmatrix7 Apple] 0b11e642aaba  DOMAIN-SUFFIX,ogameblog.com
  - [blackmatrix7 Apple] 0b4990cfa516  DOMAIN-KEYWORD,apple-support.akadns.net
  - [blackmatrix7 Apple] 0baa7200461f  PROCESS-NAME,fmfd
  - [blackmatrix7 Apple] 0bf418ebb073  DOMAIN-SUFFIX,v-has.com
  - [blackmatrix7 Apple] 0c0a253e8f92  DOMAIN-SUFFIX,vipshoes2.com
  - [blackmatrix7 Apple] 0e627ecaab13  DOMAIN-SUFFIX,specialtyheadphones.com
  - [blackmatrix7 Apple] 10db618defc9  DOMAIN-SUFFIX,buyshoponly.com
  - [blackmatrix7 Apple] 13f4109c6b4e  USER-AGENT,FindMyiPhone*
  - [blackmatrix7 Apple] 1935ca3cd42e  USER-AGENT,com.apple.news*
  - [blackmatrix7 Apple] 196278ff3ab1  DOMAIN-SUFFIX,mallheadphone.com
  - [blackmatrix7 Apple] 1b0428bb2999  DOMAIN-SUFFIX,wasdj.com
  - [blackmatrix7 Apple] 1b61555ce982  DOMAIN-SUFFIX,brandelectronic.com
  - [blackmatrix7 Apple] 1bab20a5ed4c  USER-AGENT,com.apple.Maps
  - [blackmatrix7 Apple] 1d0ac2f63207  DOMAIN-SUFFIX,businesswebwise.com
  - [blackmatrix7 Apple] 1dd2433f8252  DOMAIN-SUFFIX,onsaletrend.com
  - [blackmatrix7 Apple] 1eed7669ca62  DOMAIN-SUFFIX,theuab.net
  - [blackmatrix7 Apple] 21f53873227c  DOMAIN-SUFFIX,iphonecase2013.com
  - [blackmatrix7 Apple] 23a3e97cf892  DOMAIN-SUFFIX,sanvaras.com
  - [blackmatrix7 Apple] 2653e7cc556f  DOMAIN-SUFFIX,goodsdunk.net
  - [blackmatrix7 Apple] 2a074d11c377  DOMAIN-SUFFIX,crashlytics.com
  - [blackmatrix7 Apple] 2a3f31b111eb  DOMAIN-SUFFIX,biitii.com
  - [blackmatrix7 Apple] 2bb4fa79115e  DOMAIN-SUFFIX,lexuemei.com
  - [blackmatrix7 Apple] 2c3dec734fab  DOMAIN-SUFFIX,monsterproduct.net
  - [blackmatrix7 Apple] 2c6bde85d1fd  DOMAIN-SUFFIX,digicert.com
  - [blackmatrix7 Apple] 2d578e698146  DOMAIN-KEYWORD,smp-device
  - [blackmatrix7 Apple] 300e04160997  DOMAIN-SUFFIX,ebuyheadphones.com
  - [blackmatrix7 Apple] 304b4b6fa217  DOMAIN-SUFFIX,worldcoinpay.com
  - [blackmatrix7 Apple] 329db94df164  DOMAIN-SUFFIX,cheapshoesvip.com
  - [blackmatrix7 Apple] 3340240a8937  DOMAIN-SUFFIX,pocketbiketrader.com
  - [blackmatrix7 Apple] 386547a1be4f  DOMAIN-SUFFIX,bossae.com
  - [blackmatrix7 Apple] 3b61ae8ba877  DOMAIN-SUFFIX,micstl.com
  - [blackmatrix7 Apple] 3b6352c732ef  DOMAIN-SUFFIX,personeelsland.com
  - [blackmatrix7 Apple] 41660cfe51d9  DOMAIN-SUFFIX,headset987.com
  - [blackmatrix7 Apple] 460615972d4a  DOMAIN-SUFFIX,wholesalefine.com
  - [blackmatrix7 Apple] 4611b86fbda4  DOMAIN-SUFFIX,newlysprung.net
  - [blackmatrix7 Apple] 465d262c3f62  USER-AGENT,*FindMyiPhone?
  - [blackmatrix7 Apple] 4a3f4d61bd32  DOMAIN-SUFFIX,wholesale-exporter1.com
  - [blackmatrix7 Apple] 4a9360de83e1  DOMAIN-SUFFIX,cheerwholesale.us
  - [blackmatrix7 Apple] 4cfcc2f071c7  DOMAIN-SUFFIX,bbestmall.com
  - [blackmatrix7 Apple] 4ff3eaa43fba  USER-AGENT,com.apple.tv*
  - [blackmatrix7 Apple] 502e7f4a15c2  USER-AGENT,AppleTV*
  - [blackmatrix7 Apple] 513ede60f74f  DOMAIN-SUFFIX,sneaker666.com
  - [blackmatrix7 Apple] 518fb85ff4e1  DOMAIN-SUFFIX,samebags.com
  - [blackmatrix7 Apple] 525b098da897  DOMAIN-SUFFIX,nicesshop.net
  - [blackmatrix7 Apple] 534c23ee38fe  USER-AGENT,com.apple.trustd*
  - [blackmatrix7 Apple] 5382b860213a  DOMAIN-SUFFIX,begin-trade.com
  - [blackmatrix7 Apple] 56461ff926d9  DOMAIN-SUFFIX,earphonescheapest.com
  - [blackmatrix7 Apple] 567e29a2c206  DOMAIN-SUFFIX,honawalaan.com
  - [blackmatrix7 Apple] 5828fbb4fbf9  DOMAIN-SUFFIX,wholesaleonlinemart.com
  - [blackmatrix7 Apple] 5b12571be605  DOMAIN-SUFFIX,repswing.com
  - [blackmatrix7 Apple] 5b679897ad6f  DOMAIN-SUFFIX,incentivetravelgifts.com
  - [blackmatrix7 Apple] 5ba01fd39a1e  USER-AGENT,passd*
  - [blackmatrix7 Apple] 5cf204c52151  PROCESS-NAME,mapspushd
  - [blackmatrix7 Apple] 5f5e8a215a9b  DOMAIN-SUFFIX,dtsell.com
  - [blackmatrix7 Apple] 5f64d3bbed7f  DOMAIN-SUFFIX,airmay.com
  - [blackmatrix7 Apple] 5f768a02bfc8  DOMAIN-SUFFIX,shopping-days.net
  - [blackmatrix7 Apple] 60bdcb46260f  DOMAIN-KEYWORD,testflight
  - [blackmatrix7 Apple] 6157703e7cef  PROCESS-NAME,CoreLocationAgent
  - [Manual Rules] 658e11e0300f  DOMAIN,apple.com.akadns.net
  - [blackmatrix7 Apple] 65a2e9abd285  DOMAIN-SUFFIX,nflhotsalejerseys.com
  - [blackmatrix7 Apple] 676803873eaa  DOMAIN,lookup-api.apple.com.edgekey.net
  - [blackmatrix7 Apple] 67d5809d81b7  IP-CIDR,205.180.175.0/24,no-resolve
  - [blackmatrix7 Apple] 6a116c691846  USER-AGENT,FindMyFriends*
  - [blackmatrix7 Apple] 6a303646802e  DOMAIN-SUFFIX,headphonepubs.com
  - [blackmatrix7 Apple] 6c76a23089d2  DOMAIN-SUFFIX,ciattackers.com
  - [blackmatrix7 Apple] 6d0a05bc2ab0  DOMAIN-SUFFIX,spiritclubs.com
  - [blackmatrix7 Apple] 6f6f0d08c179  DOMAIN-SUFFIX,paulsimon-music.com
  - [blackmatrix7 Apple] 70246e47119a  DOMAIN-SUFFIX,aeasyshop.com
  - [blackmatrix7 Apple] 71671ed20875  DOMAIN-SUFFIX,baxsound.com
  - [blackmatrix7 Apple] 72cbe4690b2b  DOMAIN-SUFFIX,headphonezip.com
  - [blackmatrix7 Apple] 77b77aea8f85  DOMAIN-SUFFIX,takegoto.com
  - [blackmatrix7 Apple] 77f118c7d3b8  DOMAIN-SUFFIX,buzzardflapper.com
  - [blackmatrix7 Apple] 783a2c68a104  USER-AGENT,Maps*
  - [blackmatrix7 Apple] 7a634e04a4bb  DOMAIN-SUFFIX,shoppinguheadphones.com
  - [blackmatrix7 Apple] 7be11428de7c  DOMAIN-SUFFIX,etheadphones.com
  - [blackmatrix7 Apple] 7cbaca590950  DOMAIN-SUFFIX,free-aa.com
  - [blackmatrix7 Apple] 7cfec1555fbf  DOMAIN-KEYWORD,apple.com.akadns.net
  - [blackmatrix7 Apple] 7d88d71fee1b  PROCESS-NAME,com.apple.Maps
  - [blackmatrix7 Apple] 7deffae610f3  PROCESS-NAME,LookupViewService
  - [blackmatrix7 Apple] 836392881fd0  DOMAIN-KEYWORD,buy.itunes.apple.com
  - [blackmatrix7 Apple] 83721b8acc50  USER-AGENT,fmflocatord*
  - [blackmatrix7 Apple] 84849125f149  DOMAIN-SUFFIX,neborder.com
  - [blackmatrix7 Apple] 851e3c338142  DOMAIN-SUFFIX,cuffiesaldi.com
  - [blackmatrix7 Apple] 85d9869ad31c  DOMAIN-SUFFIX,makeeu.com
  - [blackmatrix7 Apple] 85e79da4a2f3  DOMAIN-SUFFIX,repsneakermall.com
  - [blackmatrix7 Apple] 862f90e5bcf6  DOMAIN-SUFFIX,free-sns.com
  - [blackmatrix7 Apple] 8698cdcb7cfa  PROCESS-NAME,netbiosd
  - [blackmatrix7 Apple] 882299d7a4ad  DOMAIN-SUFFIX,chihair-straightener.com
  - [blackmatrix7 Apple] 88df64b2d635  DOMAIN-SUFFIX,sulwerphoto.com
  - [blackmatrix7 Apple] 8b576ff0a96d  PROCESS-NAME,com.apple.geod
  - [blackmatrix7 Apple] 8c5089bf55f9  DOMAIN-SUFFIX,picknicekicks.net
  - [blackmatrix7 Apple] 8fa27141a919  DOMAIN-SUFFIX,brandproducts1688.com
  ... and 80 more
```

## AppleMedia.list

**Added: 11** (showing first 11)
```
  + [Manual Rules] 1a701cc95975  DOMAIN,ocvideo.apple.com
  + [Manual Rules] 40351eaeef07  DOMAIN,news-client.apple.com
  + [Manual Rules] 683b705c9f90  DOMAIN,play-edge.itunes.apple.com
  + [Manual Rules] 6f3442a07e6f  DOMAIN-SUFFIX,tv.apple.com
  + [Manual Rules] 793a02b5a263  DOMAIN,uts-api.itunes.apple.com
  + [Manual Rules] 80918f01dda4  DOMAIN,news-events.apple.com
  + [Manual Rules] a5936a80af05  DOMAIN,hls.itunes.apple.com
  + [Manual Rules] ab649c510245  DOMAIN-SUFFIX,apple.news
  + [Manual Rules] b3b71b9361b2  DOMAIN,news-edge.apple.com
  + [Manual Rules] c26a6a6b519d  DOMAIN,np-edge.itunes.apple.com
  + [Manual Rules] f9ef3e5a225c  DOMAIN,hls-amt.itunes.apple.com
```

## Apple_AI.list

**Removed: 4** (showing first 4)
```
  - [RocM301 Apple-AI] c3b7ae332522  DOMAIN-SUFFIX,gspe1-ssl.ls.apple.com
  - [RocM301 Apple-AI] d5d02abafd94  DOMAIN,wps.apple.com
  - [Manual Rules] ec57b182d328  DOMAIN-SUFFIX,gsp64-ssl.ls.apple.com
  - [RocM301 Apple-AI] efede8aee155  DOMAIN-SUFFIX,gateway.icloud.com
```

## Apple_CN.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] d8bfb4642536  DOMAIN-SUFFIX,apzones.com
```

**Removed: 6** (showing first 6)
```
  - [SukkaW Apple CDN] 0aa154923468  DOMAIN-SUFFIX,seed-sequoia.siri.apple.com
  - [SukkaW Apple CDN] 139ff6396d14  DOMAIN-SUFFIX,guzzoni.smoot.apple.com
  - [SukkaW Apple CDN] 1695f9cea76f  DOMAIN-SUFFIX,probe.siri.apple.com
  - [SukkaW Apple CDN] 1e902f6f0f29  DOMAIN-SUFFIX,guzzoni.apple.com
  - [SukkaW Apple CDN] 2800ce39f023  DOMAIN-SUFFIX,seed.siri.apple.com
  - [SukkaW Apple CDN] 51b5c71a3e77  DOMAIN-SUFFIX,seed-swallow.siri.apple.com
```

## GlobalMedia.list

**Removed: 16** (showing first 16)
```
  - [blackmatrix7 GlobalMedia] 1a701cc95975  DOMAIN,ocvideo.apple.com
  - [blackmatrix7 GlobalMedia] 40351eaeef07  DOMAIN,news-client.apple.com
  - [blackmatrix7 GlobalMedia] 4ff3eaa43fba  USER-AGENT,com.apple.tv*
  - [blackmatrix7 GlobalMedia] 502e7f4a15c2  USER-AGENT,AppleTV*
  - [SukkaW Stream] 683b705c9f90  DOMAIN,play-edge.itunes.apple.com
  - [blackmatrix7 GlobalMedia] 6f3442a07e6f  DOMAIN-SUFFIX,tv.apple.com
  - [SukkaW Stream] 793a02b5a263  DOMAIN,uts-api.itunes.apple.com
  - [blackmatrix7 GlobalMedia] 80918f01dda4  DOMAIN,news-events.apple.com
  - [SukkaW Stream] 99f59529614f  PROCESS-NAME,tv
  - [SukkaW Stream] a5936a80af05  DOMAIN,hls.itunes.apple.com
  - [blackmatrix7 GlobalMedia] ab649c510245  DOMAIN-SUFFIX,apple.news
  - [blackmatrix7 GlobalMedia] ad1e7dd22ac1  DOMAIN-SUFFIX,applemusic.com
  - [blackmatrix7 GlobalMedia] b3b71b9361b2  DOMAIN,news-edge.apple.com
  - [SukkaW Stream] c26a6a6b519d  DOMAIN,np-edge.itunes.apple.com
  - [blackmatrix7 GlobalMedia] dd2c581817a8  DOMAIN,apple.comscoreresearch.com
  - [SukkaW Stream] f9ef3e5a225c  DOMAIN,hls-amt.itunes.apple.com
```
