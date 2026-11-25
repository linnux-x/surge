# Surge Rule Diff Report
Generated: 2026-11-26T05:56:38.335837

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 4 |
| Rules added | 259 |
| Rules removed | 115 |
| Source attribution changed | 7 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| AI.list | 562 | 751 | +218 | -29 | ~7 |
| China.list | 110661 | 110667 | +6 | -0 | ~0 |
| Global.list | 24680 | 24618 | +0 | -62 | ~0 |
| Speedtest.list | 1726 | 1737 | +35 | -24 | ~0 |

## AI.list

**Added: 218** (showing first 100)
```
  + [Rabbit-Spec AIGC] 0008c650028f  DOMAIN-SUFFIX,comfyregistry.org
  + [Rabbit-Spec AIGC] 00ec72a6045d  DOMAIN-SUFFIX,robinfrontend-pa.googleapis.com
  + [OpenAI ChatGPT Voice] 040160cb39b2  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.196.43.61/32,no-resolve))
  + [Rabbit-Spec AIGC] 0641c42114ae  DOMAIN-SUFFIX,grazie.aws.intellij.net
  + [Rabbit-Spec AIGC] 077a3f9e3ec1  DOMAIN-SUFFIX,civitai.com
  + [Rabbit-Spec AIGC] 08dbd846d0a7  DOMAIN-SUFFIX,heygen.com
  + [Rabbit-Spec AIGC] 094355df1ecb  DOMAIN-SUFFIX,replit.com
  + [Rabbit-Spec AIGC] 098538b69eaf  DOMAIN-SUFFIX,qoder.com
  + [Rabbit-Spec AIGC] 09992d928ec2  DOMAIN,aws-language-servers.us-east-1.amazonaws.com
  + [Rabbit-Spec AIGC] 0a6f66a7c22e  DOMAIN,codewhisperer.us-east-1.amazonaws.com
  + [Rabbit-Spec AIGC] 0b0ed9433bc9  DOMAIN-SUFFIX,grok.x.com
  + [Rabbit-Spec AIGC] 0b2abfd79e07  DOMAIN-SUFFIX,commandcode.ai
  + [Rabbit-Spec AIGC] 0b5042f9439f  DOMAIN-SUFFIX,firefly.adobe.io
  + [Rabbit-Spec AIGC] 0cfa38a820bd  DOMAIN-SUFFIX,elevenlabsusercontent.com
  + [Rabbit-Spec AIGC] 0d07a72900e6  DOMAIN,appsgenaiserver-pa.clients6.google.com
  + [Rabbit-Spec AIGC] 0d795a7eab07  DOMAIN-SUFFIX,lmstudio.ai
  + [Rabbit-Spec AIGC] 0dc1e449f52c  DOMAIN-SUFFIX,interface.feedback
  + [Rabbit-Spec AIGC] 0e764216738c  DOMAIN-SUFFIX,windsurf.build
  + [Rabbit-Spec AIGC] 0e80e8feab61  DOMAIN-SUFFIX,kilo.ai
  + [Rabbit-Spec AIGC] 0f160f7335e0  DOMAIN-SUFFIX,claude.dev
  + [Rabbit-Spec AIGC] 0fa4bf1171df  DOMAIN-SUFFIX,notebook.google.com
  + [Rabbit-Spec AIGC] 10a5cafc7cf6  DOMAIN-SUFFIX,starling.zijieapi.com
  + [OpenAI ChatGPT Voice] 131328ae9781  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.127.120.244/32,no-resolve))
  + [Rabbit-Spec AIGC] 1578f20db917  DOMAIN,webchannel-alkalimakersuite-pa.clients6.google.com
  + [Rabbit-Spec AIGC] 163299f9bab3  DOMAIN,copilotprodattachments.blob.core.windows.net
  + [Rabbit-Spec AIGC] 18357c2e145c  DOMAIN-SUFFIX,trae.ai
  + [Rabbit-Spec AIGC] 190b735b8d93  DOMAIN-SUFFIX,crewai.com
  + [Rabbit-Spec AIGC] 1973799cf09a  DOMAIN-SUFFIX,lmarena.ai
  + [Rabbit-Spec AIGC] 1a178acbd995  DOMAIN-SUFFIX,duck.ai
  + [Rabbit-Spec AIGC] 1c83b1e6987f  DOMAIN-SUFFIX,q.us-east-1.amazonaws.com
  + [Rabbit-Spec AIGC] 1e890e4bf12d  DOMAIN,aws-toolkit-language-servers.amazonaws.com
  + [Rabbit-Spec AIGC] 219ea3d92bab  DOMAIN-SUFFIX,chutes.ai
  + [OpenAI ChatGPT Voice] 2700baab159d  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,51.105.39.183/32,no-resolve))
  + [Rabbit-Spec AIGC] 2bf354c75852  DOMAIN-SUFFIX,openclaw.ai
  + [Rabbit-Spec AIGC] 2cfc30e96392  DOMAIN-SUFFIX,continue.dev
  + [Rabbit-Spec AIGC] 2d56e78f2391  DOMAIN-SUFFIX,gemini.gstatic.com
  + [Rabbit-Spec AIGC] 2ee8b7b89090  DOMAIN-SUFFIX,opencode.ai
  + [Rabbit-Spec AIGC] 3363fad5b3c6  DOMAIN-SUFFIX,runwayml.com
  + [Rabbit-Spec AIGC] 3658017d5749  DOMAIN-SUFFIX,ai.google.dev
  + [Rabbit-Spec AIGC] 37bf29a75ca0  DOMAIN-SUFFIX,labstailwind.pa.googleapis.com
  + [Rabbit-Spec AIGC] 390f15ee6e48  DOMAIN-SUFFIX,descript.com
  + [Rabbit-Spec AIGC] 399674e3eff9  DOMAIN-SUFFIX,notebook.google
  + [Rabbit-Spec AIGC] 3eba7e5ecf3d  DOMAIN,gateway.bingviz.microsoftapp.net
  + [Rabbit-Spec AIGC] 3fd9b76387e7  DOMAIN-SUFFIX,antigravity.google.com
  + [Rabbit-Spec AIGC] 41d76d67ae8c  DOMAIN-SUFFIX,cici.com
  + [OpenAI ChatGPT Voice] 423394c806b2  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.124.193.23/32,no-resolve))
  + [Rabbit-Spec AIGC] 43e0778cfa9d  DOMAIN-SUFFIX,bolt.new
  + [OpenAI ChatGPT Voice] 45360c62beff  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,57.156.64.73/32,no-resolve))
  + [Rabbit-Spec AIGC] 45e12299ff7b  DOMAIN-SUFFIX,tron-sg.bytelemon.com
  + [Rabbit-Spec AIGC] 479d797dc5ef  DOMAIN-SUFFIX,h2o.ai
  + [Rabbit-Spec AIGC] 49f05aa0823e  DOMAIN-SUFFIX,repl.it
  + [Rabbit-Spec AIGC] 4b3491a1725d  DOMAIN-SUFFIX,ant.dev
  + [Rabbit-Spec AIGC] 4c6c24bb567e  DOMAIN-SUFFIX,manuscdn.com
  + [Rabbit-Spec AIGC] 4d5713126265  DOMAIN-SUFFIX,you.com
  + [Rabbit-Spec AIGC] 4e4eab776be9  DOMAIN,idetoolkits-hostedfiles.amazonaws.com
  + [Rabbit-Spec AIGC] 4f045bbc358e  DOMAIN-SUFFIX,perplexity.com
  + [Rabbit-Spec AIGC] 4ff7dc804988  DOMAIN-SUFFIX,character.ai
  + [Rabbit-Spec AIGC] 51e8dc0f9a64  DOMAIN-SUFFIX,jetbrains.ai
  + [Rabbit-Spec AIGC] 52952258f996  DOMAIN-SUFFIX,gemma.ai
  + [Rabbit-Spec AIGC] 54c6d2db1509  DOMAIN-SUFFIX,crixet.com
  + [Rabbit-Spec AIGC] 561cfb9d1361  DOMAIN-SUFFIX,replit.dev
  + [Rabbit-Spec AIGC] 571eaf32d448  DOMAIN-SUFFIX,v0.dev
  + [Rabbit-Spec AIGC] 58b7a5b7d6fe  DOMAIN-SUFFIX,edgeservices.bing.com
  + [Rabbit-Spec AIGC] 58c9e9711972  DOMAIN-SUFFIX,midjourney.com
  + [OpenAI ChatGPT Voice] 590dad9ffd92  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.175.112.94/32,no-resolve))
  + [OpenAI ChatGPT Voice] 591d986e60b3  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.78.168.55/32,no-resolve))
  + [Rabbit-Spec AIGC] 5ceaf0badd01  DOMAIN-SUFFIX,langchain.com
  + [Rabbit-Spec AIGC] 602c7788cdd7  DOMAIN-SUFFIX,synthesia.io
  + [Rabbit-Spec AIGC] 619167cf7180  DOMAIN-SUFFIX,cohere.com
  + [Rabbit-Spec AIGC] 61a4c4f18289  DOMAIN,ppl-ai-file-upload.s3.amazonaws.com
  + [OpenAI ChatGPT Voice] 643bcce596ac  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.213.235.219/32,no-resolve))
  + [OpenAI ChatGPT Voice] 64de5d3f5b34  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,172.172.179.197/32,no-resolve))
  + [Rabbit-Spec AIGC] 659d472b6743  DOMAIN-SUFFIX,abtestvm-sg.bytedance.com
  + [Rabbit-Spec AIGC] 66621031ad89  DOMAIN-SUFFIX,openai.org
  + [Rabbit-Spec AIGC] 67bfb69a3112  DOMAIN,appsgenaiserver-pa.clients.google.com
  + [Rabbit-Spec AIGC] 6a3fbd144de1  DOMAIN-SUFFIX,aida.googleapis.com
  + [Rabbit-Spec AIGC] 6af257303e51  DOMAIN,copilot-workspace.githubnext.com
  + [Rabbit-Spec AIGC] 6b2b4ee2e589  DOMAIN-SUFFIX,anthropic.com.cn
  + [Rabbit-Spec AIGC] 6b99969f7bb8  DOMAIN-SUFFIX,leonardo.ai
  + [OpenAI ChatGPT Voice] 6c07fc15c1a3  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,74.152.66.187/32,no-resolve))
  + [Rabbit-Spec AIGC] 6de19f0b7fbd  DOMAIN-SUFFIX,tabnine.com
  + [Rabbit-Spec AIGC] 6f1edbdba9e4  DOMAIN-SUFFIX,mcpservertest.online
  + [Rabbit-Spec AIGC] 704dc7551c92  DOMAIN-SUFFIX,ciciaicdn.com
  + [Rabbit-Spec AIGC] 7210faa9eac6  DOMAIN,ai.developer.meta.com
  + [Rabbit-Spec AIGC] 722ea69a4728  DOMAIN-SUFFIX,cody.dev
  + [Rabbit-Spec AIGC] 7454c2190801  DOMAIN-SUFFIX,youmind.com
  + [Rabbit-Spec AIGC] 7490702e4d65  DOMAIN-SUFFIX,muthos.com
  + [Rabbit-Spec AIGC] 754423811481  DOMAIN-SUFFIX,suno.ai
  + [Rabbit-Spec AIGC] 75fa2c809f68  DOMAIN-SUFFIX,llamameta.net
  + [Rabbit-Spec AIGC] 77f698d29ea2  DOMAIN,client-telemetry.us-east-1.amazonaws.com
  + [OpenAI ChatGPT Voice] 7c80df553966  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.165.191.7/32,no-resolve))
  + [Rabbit-Spec AIGC] 7da74b7ef7be  IP-ASN,399358,no-resolve
  + [Rabbit-Spec AIGC] 7e5f1f5fd6bb  DOMAIN-SUFFIX,lumalabs.ai
  + [Rabbit-Spec AIGC] 80769d1c6add  DOMAIN-SUFFIX,otter.ai
  + [Rabbit-Spec AIGC] 812b8b8bc9f9  DOMAIN-SUFFIX,youmind.ai
  + [Rabbit-Spec AIGC] 81bfa50350f5  DOMAIN-SUFFIX,ai.studio
  + [OpenAI ChatGPT Voice] 846de140d696  AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,20.200.182.97/32,no-resolve))
  + [Rabbit-Spec AIGC] 85745039dfce  DOMAIN-SUFFIX,ampcode.com
  + [Rabbit-Spec AIGC] 87aa5d797529  DOMAIN-SUFFIX,modelcontextprotocol.net
  + [Rabbit-Spec AIGC] 87daba4d3d94  DOMAIN-SUFFIX,v0.app
  ... and 118 more
```

**Removed: 29** (showing first 29)
```
  - [Manual Rules] 047cc5f8bd4d  DOMAIN,antigravity.google
  - [Manual Rules] 107f612efba1  DOMAIN,antigravity-unleash.goog
  - [Manual Rules] 120bba58c982  DOMAIN,auth.grokipedia.com
  - [Manual Rules] 17ed196cec02  DOMAIN,claude.new
  - [Manual Rules] 29914f328abf  DOMAIN,flow.google
  - [Manual Rules] 2abac546c15e  DOMAIN,trae-api-sg.mchost.guru
  - [Manual Rules] 3767ca234c2e  DOMAIN,robinfrontend-pa.googleapis.com
  - [Manual Rules] 391d402853fb  DOMAIN,claude.site
  - [Rabbit-Spec AIGC] 405fda27adf6  DOMAIN,chat.openai.com.cdn.cloudflare.net
  - [Manual Rules] 46ac15f42c69  DOMAIN,ai.google.dev
  - [Manual Rules] 619d261c2c90  DOMAIN,aida.googleapis.com
  - [Manual Rules] 61bd93b136ea  DOMAIN,api.together.ai
  - [Manual Rules] 68aa8ae76307  DOMAIN,www.claude.new
  - [Manual Rules] 783c8c8ed09b  DOMAIN,www.claudeacademy.com
  - [Manual Rules] 7c0d5c855aef  DOMAIN,opencode.ai
  - [Manual Rules] 95705d1d523a  DOMAIN,api.devin.ai
  - [Manual Rules] aad2bbc989a4  DOMAIN,claudeacademy.com
  - [Manual Rules] b8318f06bb26  DOMAIN,router.huggingface.co
  - [Manual Rules] c393b4a65a75  DOMAIN,static.devin.ai
  - [SukkaW AI] c882ca09b881  DOMAIN,api.jetbrains.ai
  - [Manual Rules] d11c097d9e3a  DOMAIN,www.claude.dev
  - [Manual Rules] d2b4d957442c  DOMAIN,jules.google.com
  - [Manual Rules] da97cad3b7e3  DOMAIN,aisandbox-pa.googleapis.com
  - [SukkaW AI] dbc5d5f95763  DOMAIN,gateway.ai.cloudflare.com
  - [Manual Rules] e6680e1bca06  DOMAIN,claude.dev
  - [Manual Rules] f1e1338d0af6  DOMAIN,app.devin.ai
  - [Manual Rules] f1eb0f6db67e  DOMAIN,api.together.xyz
  - [Manual Rules] f320df6eb3fc  DOMAIN,api.app.prod.grazie.aws.intellij.net
  - [Manual Rules] ffa6365b4993  DOMAIN,devin.ai
```

**Source changed: 7**
```
  ~ 4c96ae31dbf1: [ConnersHua AI → Rabbit-Spec AIGC]
  ~ 6cf089f4f159: [ConnersHua AI → Rabbit-Spec AIGC]
  ~ d68cabdb1f69: [ConnersHua AI → Rabbit-Spec AIGC]
  ~ 9d0ff2f30280: [ConnersHua AI → Rabbit-Spec AIGC]
  ~ 54faa00968bf: [ConnersHua AI → Rabbit-Spec AIGC]
  ~ ce9f29ed7edf: [ConnersHua AI → Rabbit-Spec AIGC]
  ~ 2fd8b3258bd3: [ConnersHua AI → Rabbit-Spec AIGC]
```

## China.list

**Added: 6** (showing first 6)
```
  + [Rabbit-Spec China] 3ad9f264f759  DOMAIN-SUFFIX,lujincaifu.com
  + [Rabbit-Spec China] 5846578138e0  DOMAIN-SUFFIX,lenovofuturecenter.com
  + [Rabbit-Spec China] 67c401020726  DOMAIN-SUFFIX,qpmcn.com
  + [Rabbit-Spec China] 771d9a2cd3b6  DOMAIN-SUFFIX,yqbmall.com
  + [Rabbit-Spec China] 8e9f8ca9928f  DOMAIN-SUFFIX,zhaoliangjipc.com
  + [Rabbit-Spec China] c814c8c003f3  DOMAIN-SUFFIX,172.com
```

## Global.list

**Removed: 62** (showing first 62)
```
  - [blackmatrix7 Global] 0008c650028f  DOMAIN-SUFFIX,comfyregistry.org
  - [blackmatrix7 Global] 077a3f9e3ec1  DOMAIN-SUFFIX,civitai.com
  - [blackmatrix7 Global] 0d795a7eab07  DOMAIN-SUFFIX,lmstudio.ai
  - [blackmatrix7 Global] 0e764216738c  DOMAIN-SUFFIX,windsurf.build
  - [blackmatrix7 Global] 0f160f7335e0  DOMAIN-SUFFIX,claude.dev
  - [blackmatrix7 Global] 18357c2e145c  DOMAIN-SUFFIX,trae.ai
  - [blackmatrix7 Global] 190b735b8d93  DOMAIN-SUFFIX,crewai.com
  - [blackmatrix7 Global] 1973799cf09a  DOMAIN-SUFFIX,lmarena.ai
  - [blackmatrix7 Global] 1a178acbd995  DOMAIN-SUFFIX,duck.ai
  - [blackmatrix7 Global] 219ea3d92bab  DOMAIN-SUFFIX,chutes.ai
  - [blackmatrix7 Global] 2bf354c75852  DOMAIN-SUFFIX,openclaw.ai
  - [blackmatrix7 Global] 2ee8b7b89090  DOMAIN-SUFFIX,opencode.ai
  - [blackmatrix7 Global] 41d76d67ae8c  DOMAIN-SUFFIX,cici.com
  - [blackmatrix7 Global] 479d797dc5ef  DOMAIN-SUFFIX,h2o.ai
  - [blackmatrix7 Global] 4b3491a1725d  DOMAIN-SUFFIX,ant.dev
  - [blackmatrix7 Global] 4d5713126265  DOMAIN-SUFFIX,you.com
  - [blackmatrix7 Global] 4f045bbc358e  DOMAIN-SUFFIX,perplexity.com
  - [blackmatrix7 Global] 4ff7dc804988  DOMAIN-SUFFIX,character.ai
  - [blackmatrix7 Global] 51e8dc0f9a64  DOMAIN-SUFFIX,jetbrains.ai
  - [blackmatrix7 Global] 54c6d2db1509  DOMAIN-SUFFIX,crixet.com
  - [blackmatrix7 Global] 58c9e9711972  DOMAIN-SUFFIX,midjourney.com
  - [blackmatrix7 Global] 5ceaf0badd01  DOMAIN-SUFFIX,langchain.com
  - [blackmatrix7 Global] 619167cf7180  DOMAIN-SUFFIX,cohere.com
  - [blackmatrix7 Global] 66621031ad89  DOMAIN-SUFFIX,openai.org
  - [blackmatrix7 Global] 6b99969f7bb8  DOMAIN-SUFFIX,leonardo.ai
  - [blackmatrix7 Global] 7454c2190801  DOMAIN-SUFFIX,youmind.com
  - [blackmatrix7 Global] 754423811481  DOMAIN-SUFFIX,suno.ai
  - [blackmatrix7 Global] 812b8b8bc9f9  DOMAIN-SUFFIX,youmind.ai
  - [blackmatrix7 Global] 81bfa50350f5  DOMAIN-SUFFIX,ai.studio
  - [blackmatrix7 Global] 87e39872b847  DOMAIN-SUFFIX,kiro.dev
  - [blackmatrix7 Global] 8df36186079e  DOMAIN-SUFFIX,hf.space
  - [blackmatrix7 Global] 91df6fe07412  DOMAIN-SUFFIX,cohere.ai
  - [blackmatrix7 Global] 9287be9bdfa1  DOMAIN-SUFFIX,huggingface.co
  - [blackmatrix7 Global] 93c47fe0a183  DOMAIN-SUFFIX,youmind.site
  - [blackmatrix7 Global] 9464ee13b59d  DOMAIN-SUFFIX,chatbotclaude.com
  - [blackmatrix7 Global] 95033fd92bc9  DOMAIN-SUFFIX,ciciai.com
  - [blackmatrix7 Global] 96c9f6104d50  DOMAIN-SUFFIX,atmeta.com
  - [blackmatrix7 Global] 9cadc89307f6  DOMAIN-SUFFIX,comfy.org
  - [blackmatrix7 Global] 9cec67cbe61c  DOMAIN-SUFFIX,cerebras.ai
  - [blackmatrix7 Global] 9e49db6e06dc  DOMAIN-SUFFIX,anthropic.team
  - [blackmatrix7 Global] 9e938dc5c9c2  DOMAIN-SUFFIX,antspace.dev
  - [blackmatrix7 Global] 9f98d08cfd51  DOMAIN-SUFFIX,llama.com
  - [blackmatrix7 Global] a1a1d525ce1e  DOMAIN-SUFFIX,coze.com
  - [blackmatrix7 Global] b214bcdbbc6b  DOMAIN-SUFFIX,marscode.com
  - [blackmatrix7 Global] b368b38efee1  DOMAIN-SUFFIX,manus.im
  - [blackmatrix7 Global] b849525a4e78  DOMAIN-SUFFIX,claudeacademy.com
  - [blackmatrix7 Global] b94593f2dc7e  DOMAIN-SUFFIX,hf.co
  - [blackmatrix7 Global] bdcf2ee30a7f  DOMAIN-SUFFIX,suno.com
  - [blackmatrix7 Global] bde927d4d8f4  DOMAIN-SUFFIX,claude.site
  - [blackmatrix7 Global] cc4a87dd21d6  DOMAIN-SUFFIX,sourcegraph.com
  - [blackmatrix7 Global] cced77d62e90  DOMAIN-SUFFIX,diabrowser.com
  - [blackmatrix7 Global] d34f2571e86c  DOMAIN-SUFFIX,devin.ai
  - [blackmatrix7 Global] d37d92eaaf15  DOMAIN-SUFFIX,claudepages.dev
  - [blackmatrix7 Global] d71c4ffcdcc0  DOMAIN-SUFFIX,coderabbit.ai
  - [blackmatrix7 Global] d779b23c6b10  DOMAIN-SUFFIX,ollama.com
  - [blackmatrix7 Global] dcbc72e64ba6  DOMAIN-SUFFIX,elevenlabs.io
  - [blackmatrix7 Global] e5a203127750  DOMAIN-SUFFIX,claude.new
  - [blackmatrix7 Global] ec8dcbe65712  DOMAIN-SUFFIX,claudestudio.com
  - [blackmatrix7 Global] f754d54caeb3  DOMAIN-SUFFIX,grokipedia.com
  - [blackmatrix7 Global] fbf53c3240ba  DOMAIN-SUFFIX,diabrowser.engineering
  - [blackmatrix7 Global] fcf2426bc57d  DOMAIN-SUFFIX,elevenlabs.com
  - [blackmatrix7 Global] fddb16e749d7  DOMAIN-SUFFIX,lovart.ai
```

## Speedtest.list

**Added: 35** (showing first 35)
```
  + [SukkaW Speedtest Servers International] 0ab0cf8a6ab9  DOMAIN,speedtest.novateldigital.com
  + [SukkaW Speedtest Servers International] 16699495d33c  DOMAIN,speed.uberlinktelecom.com.br
  + [SukkaW Speedtest Servers International] 26f9e3f546b4  DOMAIN,speedtest.ilitha.com
  + [SukkaW Speedtest Servers International] 2c4e9bf40557  DOMAIN,velocity.softtelecom.net.br
  + [SukkaW Speedtest Servers International] 31e8ffa70b1a  DOMAIN,speedtest.pnb.vodafoneidea.com
  + [SukkaW Speedtest Servers International] 4347ba8f1b04  DOMAIN,lhr.speedtest.rustbanned.net
  + [SukkaW Speedtest Servers International] 5540cc8e3bac  DOMAIN,stetobicoke.rogers.com
  + [SukkaW Speedtest Servers International] 559412db0709  DOMAIN,stpanipat.softechinfosol.com
  + [SukkaW Speedtest Servers International] 5b6c9723716c  DOMAIN,speedtest.syd.netsg.net.au
  + [SukkaW Speedtest Servers International] 5ffb4d6de1c7  DOMAIN,stvaughan.netcrawler.ca
  + [SukkaW Speedtest Servers International] 616c6bffe17f  DOMAIN,stkingcity.rogers.com
  + [SukkaW Speedtest Servers International] 6a42e55feb6b  DOMAIN,speedtest.hk.aixxycode.id
  + [SukkaW Speedtest Servers International] 72bb8c1b570f  DOMAIN,speedtest5.windtre.it
  + [SukkaW Speedtest Servers International] 830bf10487c6  DOMAIN,gisho.work
  + [SukkaW Speedtest Servers International] 890fa3aca5ec  DOMAIN,speedtest.orixinet.com.br
  + [SukkaW Speedtest Servers International] 8921715d28d7  DOMAIN,speedtest2.tmg.net.id
  + [SukkaW Speedtest Servers International] 8e36c5eb6ca2  DOMAIN,speedtest2.micronet.in
  + [SukkaW Speedtest Servers International] 934ad5aa9642  DOMAIN,speedtest10g.bhm.as13760.net
  + [SukkaW Speedtest Servers International] 96692f154a26  DOMAIN,veloteste.mrjomar.com.br
  + [SukkaW Speedtest Servers International] 9bf7f0647b9f  DOMAIN,speedtest.duocast.net
  + [SukkaW Speedtest Servers International] 9d2342e15aaa  DOMAIN,stkingcity.netcrawler.ca
  + [SukkaW Speedtest Servers International] 9ef50333ec52  DOMAIN,speedtestmoh1.airtelbroadband.in
  + [SukkaW Speedtest Servers International] a1b9d99a6b53  DOMAIN,speedtestus.pvdatanet.com
  + [SukkaW Speedtest Servers International] a1bec4214ce1  DOMAIN,fetdl2.seed.net.tw
  + [SukkaW Speedtest Servers International] b683bdd82f27  DOMAIN,st02.mtnsat.net
  + [SukkaW Speedtest Servers International] b73df15da330  DOMAIN,stetobicoke.netcrawler.ca
  + [SukkaW Speedtest Servers International] bfe7445158e5  DOMAIN,st04.mtnsat.net
  + [SukkaW Speedtest Servers International] c11b51d67b4a  DOMAIN,stbarrie.netcrawler.ca
  + [SukkaW Speedtest Servers International] c7730d38d8d7  DOMAIN,speedtest001.bfinetworks.com
  + [SukkaW Speedtest Servers International] e40a990fb123  DOMAIN,kc.speedtest.rustbanned.net
  + [SukkaW Speedtest Servers International] e41fcdf67e6f  DOMAIN,speedtest.bemol.com.br
  + [SukkaW Speedtest Servers International] f1d4ed4013f8  DOMAIN,bpwoippy.vialis.net
  + [SukkaW Speedtest Servers International] f2367bf1b8eb  DOMAIN,stvaughan.rogers.com
  + [SukkaW Speedtest Servers International] f4122684bf9e  DOMAIN,speedtest-ams.retn.net
  + [SukkaW Speedtest Servers International] ffd9e1eeef68  DOMAIN,speedtest1.tmg.net.id
```

**Removed: 24** (showing first 24)
```
  - [SukkaW Speedtest Servers International] 0d9b9f55b7a6  DOMAIN,lifitelecom.brsserver.com.br
  - [SukkaW Speedtest Servers International] 1b2d33f3bf55  DOMAIN,speedtest4.ekowebtech.net
  - [SukkaW Speedtest Servers International] 33e4b49c77f9  DOMAIN,ookla.la.ca.sharktech.net
  - [SukkaW Speedtest Servers International] 3a3a932c44e1  DOMAIN,speed.airwavesinternet.com
  - [SukkaW Speedtest Servers International] 400b94581e4f  DOMAIN,test.eolo.it
  - [SukkaW Speedtest Servers International] 435df8f008e0  DOMAIN,speedtest.respawnhost.com
  - [SukkaW Speedtest Servers International] 43c9e647d2a9  DOMAIN,speedtest-adelaide.optusnet.com.au
  - [SukkaW Speedtest Servers International] 499c1e741ef8  DOMAIN,asanet1.brsserver.com.br
  - [SukkaW Speedtest Servers International] 4cdddfe9358b  DOMAIN,sp1.jdmbroadband.com
  - [SukkaW Speedtest Servers International] 4d8a0b572a38  DOMAIN,speed.isrcomunicaciones.es
  - [SukkaW Speedtest Servers International] 589d7eeccf53  DOMAIN,ookla.mtt.as6453.net
  - [SukkaW Speedtest Servers International] 645c547cce51  DOMAIN,speedtest.onetouchexpress.com
  - [SukkaW Speedtest Servers International] 678f7dfca317  DOMAIN,speedtest-par.flowhardware.ch
  - [SukkaW Speedtest Servers International] 8a039e9d08ba  DOMAIN,speedtest.interligpro.com.br
  - [SukkaW Speedtest Servers International] 9549a51bac8f  DOMAIN,ookla.mln.as6453.net
  - [SukkaW Speedtest Servers International] a74e0e560bca  DOMAIN,speedt-mi.skycdn.it
  - [SukkaW Speedtest Servers International] a8249c53ba8a  DOMAIN,speedtest.thn.uk.syntura.io
  - [SukkaW Speedtest Servers International] b28cbd1348be  DOMAIN,velocimetro.wspeednet.com.br
  - [SukkaW Speedtest Servers International] b8439ac0d8f2  DOMAIN,speedtest.chi.sharktech.net
  - [SukkaW Speedtest Servers International] c3109cd31fc9  DOMAIN,srv02-sjdm.imj-wanklik.com
  - [SukkaW Speedtest Servers International] cce8869a397d  DOMAIN,speedtest3a.socket.net
  - [SukkaW Speedtest Servers International] d0647073e22a  DOMAIN,airspeed.airwavesinternet.com
  - [SukkaW Speedtest Servers International] f72f656d309d  DOMAIN,speedtest.apexbroadband.in
  - [SukkaW Speedtest Servers International] fc64f25abeb6  DOMAIN,speedtest.absolutevalidation.com
```
