# Surge Rule Diff Report
Generated: 2026-10-04T22:00:17.627825

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 5 |
| Rules added | 2 |
| Rules removed | 61 |
| Source attribution changed | 1 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 133 | 122 | +1 | -12 | ~1 |
| Global.list | 24362 | 24363 | +1 | -0 | ~0 |
| GlobalMedia.list | 2263 | 2255 | +0 | -8 | ~0 |
| Google.list | 692 | 689 | +0 | -3 | ~0 |
| Microsoft.list | 523 | 485 | +0 | -38 | ~0 |

## AI.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 271c0173f174  DOMAIN-SUFFIX,labs.google
```

**Removed: 12** (showing first 12)
```
  - [ConnersHua AI] 0a4269c42bbe  DOMAIN-KEYWORD,labs.google
  - [Rabbit-Spec AIGC] 14c7000710f6  DOMAIN,browser-intake-datadoghq.com
  - [ConnersHua AI] 2cf758f67bca  DOMAIN-KEYWORD,notebooklm.google
  - [Manual Rules] 3e42093c1938  DOMAIN-KEYWORD,alkalimakersuite-pa.clients6.google.com
  - [Rabbit-Spec AIGC] 4de2dc35a0b8  DOMAIN,cdn.usefathom.com
  - [ConnersHua AI] 5761b933cd74  DOMAIN-SUFFIX,byteoversea.com,extended-matching
  - [Rabbit-Spec AIGC] 6eb10dad15dd  DOMAIN,browser-intake-us5-datadoghq.com
  - [ConnersHua AI] 758624e99bed  DOMAIN-KEYWORD,openaicom
  - [Rabbit-Spec AIGC] b1e6274c779e  DOMAIN-SUFFIX,rum.browser-intake-datadoghq.com
  - [SukkaW AI] b5afdc25db21  DOMAIN-KEYWORD,openai
  - [ConnersHua AI] da68fa05a4f6  DOMAIN-KEYWORD,openaiapi
  - [Rabbit-Spec AIGC] fe8ff5859ba9  DOMAIN-SUFFIX,algolia.net
```

**Source changed: 1**
```
  ~ bb5d4970bdae: [ConnersHua AI → Manual Rules]
```

## Global.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 Global] 8701edd46b0f  DOMAIN-SUFFIX,amazonaws.com
```

## GlobalMedia.list

**Removed: 8** (showing first 8)
```
  - [blackmatrix7 GlobalMedia] 0e5270cc211a  DOMAIN-SUFFIX,youtu.be
  - [blackmatrix7 GlobalMedia] 12c52d1b2fbc  DOMAIN-SUFFIX,gvt1.com
  - [blackmatrix7 GlobalMedia] 215f8b6d6410  DOMAIN-KEYWORD,youtube
  - [blackmatrix7 GlobalMedia] 63641960dc63  DOMAIN-SUFFIX,ggpht.cn
  - [blackmatrix7 GlobalMedia] 8701edd46b0f  DOMAIN-SUFFIX,amazonaws.com
  - [blackmatrix7 GlobalMedia] 96f22dc6e127  DOMAIN-SUFFIX,gvt2.com
  - [blackmatrix7 GlobalMedia] abcfa2afe5aa  DOMAIN-SUFFIX,video.google.com
  - [blackmatrix7 GlobalMedia] dc55c5390b0e  DOMAIN-SUFFIX,googlevideo.com
```

## Google.list

**Removed: 3** (showing first 3)
```
  - [blackmatrix7 Google] 1dbeb15d7a34  DOMAIN-SUFFIX,dialogflow.com
  - [blackmatrix7 Google] 67a0812c4e74  DOMAIN-SUFFIX,api.ai
  - [blackmatrix7 Google] 95632f44db15  DOMAIN-SUFFIX,deepmind.com
```

## Microsoft.list

**Removed: 38** (showing first 38)
```
  - [blackmatrix7 Microsoft] 0617f6dd57be  DOMAIN-SUFFIX,gamepass.com
  - [blackmatrix7 Microsoft] 0859ea00dbd5  DOMAIN-SUFFIX,xbx.lv
  - [blackmatrix7 Microsoft] 0a959499384e  DOMAIN-SUFFIX,xbox.com
  - [blackmatrix7 Microsoft] 127c071123ba  DOMAIN-SUFFIX,xbox.co
  - [blackmatrix7 Microsoft] 16ccf3554a3f  DOMAIN-SUFFIX,bethesda.net
  - [blackmatrix7 Microsoft] 2d577aa9de12  DOMAIN-SUFFIX,msgamestudios.com
  - [blackmatrix7 Microsoft] 2f3e5f25789a  DOMAIN-SUFFIX,xbox360.co
  - [blackmatrix7 Microsoft] 35a63a3379d5  DOMAIN-SUFFIX,xboxab.com
  - [blackmatrix7 Microsoft] 3e727fa1c0f2  DOMAIN-SUFFIX,minecraftshop.com
  - [blackmatrix7 Microsoft] 470c090bbf19  DOMAIN-SUFFIX,tellmewhygame.com
  - [blackmatrix7 Microsoft] 4d958be07128  DOMAIN-SUFFIX,mojang.com
  - [blackmatrix7 Microsoft] 55bb82183fd0  DOMAIN-SUFFIX,forzaracingchampionship.com
  - [blackmatrix7 Microsoft] 59ed0b40d3ac  DOMAIN-SUFFIX,xbox.eu
  - [blackmatrix7 Microsoft] 5b9a966f0135  DOMAIN-SUFFIX,forzarc.com
  - [blackmatrix7 Microsoft] 64cb9274d544  DOMAIN-SUFFIX,beth.games
  - [blackmatrix7 Microsoft] 6775cf4e0450  DOMAIN-SUFFIX,bethsoft.com
  - [blackmatrix7 Microsoft] 7073056ca41a  DOMAIN-SUFFIX,doom.com
  - [blackmatrix7 Microsoft] 739ce028757a  DOMAIN-SUFFIX,bethesdagamestudios.com
  - [blackmatrix7 Microsoft] 7936fa1901f3  DOMAIN-SUFFIX,helpshift.com
  - [blackmatrix7 Microsoft] 7f20c5a9cfa4  DOMAIN-SUFFIX,forzamotorsport.net
  - [blackmatrix7 Microsoft] 866f65244b88  DOMAIN-SUFFIX,xboxone.co
  - [blackmatrix7 Microsoft] 8df7d0842ff8  DOMAIN-SUFFIX,xbox360.org
  - [blackmatrix7 Microsoft] 9157caa7d53d  DOMAIN-SUFFIX,xbox360.com
  - [blackmatrix7 Microsoft] 93a1e41d5bf7  DOMAIN-SUFFIX,xboxplayanywhere.com
  - [blackmatrix7 Microsoft] 981ccfcbcf65  DOMAIN-SUFFIX,renovacionxboxlive.com
  - [blackmatrix7 Microsoft] 9cbdfbf627b7  DOMAIN-SUFFIX,xbox360.eu
  - [blackmatrix7 Microsoft] a1d822994ed8  DOMAIN-SUFFIX,callersbane.com
  - [blackmatrix7 Microsoft] a3acf1dd3622  DOMAIN-SUFFIX,xboxone.com
  - [blackmatrix7 Microsoft] af437c96e637  DOMAIN-SUFFIX,xboxgamepass.com
  - [blackmatrix7 Microsoft] bc1574cec70c  DOMAIN-SUFFIX,elderscrolls.com
  - [blackmatrix7 Microsoft] bcbb46b3c2ed  DOMAIN-SUFFIX,xboxgamestudios.com
  - [blackmatrix7 Microsoft] d29b2893b1af  DOMAIN-SUFFIX,xboxone.eu
  - [blackmatrix7 Microsoft] ddcb45918450  DOMAIN-SUFFIX,xboxlive.com
  - [blackmatrix7 Microsoft] df2feb01983f  DOMAIN-SUFFIX,minecraft.net
  - [blackmatrix7 Microsoft] e9db19ec13b9  DOMAIN-SUFFIX,orithegame.com
  - [blackmatrix7 Microsoft] efdf2ffe8424  DOMAIN-SUFFIX,xboxstudios.com
  - [blackmatrix7 Microsoft] f88c2949c9ba  DOMAIN-SUFFIX,xbox.org
  - [blackmatrix7 Microsoft] fc0e76e48ef1  DOMAIN-SUFFIX,xboxservices.com
```
