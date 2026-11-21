# Surge Rule Diff Report
Generated: 2026-11-21T18:57:34.283023

## Summary

| Metric | Count |
|--------|-------|
| Files changed | 3 |
| Rules added | 9 |
| Rules removed | 6 |
| Source attribution changed | 0 |

## Per-File Changes

| File | Prev | Curr | Added | Removed | Source Δ |
|------|------|------|-------|---------|----------|
| China.list | 110647 | 110648 | +1 | -0 | ~0 |
| Global.list | 24636 | 24637 | +1 | -0 | ~0 |
| PayPal.list | 233 | 234 | +7 | -6 | ~0 |

## China.list

**Added: 1** (showing first 1)
```
  + [Manual Rules] 2d1b25bf57f7  DOMAIN-SUFFIX,paypal.cn
```

## Global.list

**Added: 1** (showing first 1)
```
  + [blackmatrix7 Global] 6adaa541866e  DOMAIN-SUFFIX,krakenjs.com
```

## PayPal.list

**Added: 7** (showing first 7)
```
  + [Manual Rules] 0e2e1386dd3e  DOMAIN-SUFFIX,zettle.com
  + [Manual Rules] 76fca66aab16  DOMAIN,venmo.s3.amazonaws.com
  + [Manual Rules] 833c3a25fa60  DOMAIN,payments.sandbox.braintree-api.com
  + [Manual Rules] 853c4ca4402e  DOMAIN,payments.braintree-api.com
  + [Manual Rules] 9981688f620c  DOMAIN-SUFFIX,hyperwallet.com
  + [Manual Rules] cac8a0d39048  DOMAIN-SUFFIX,izettle.com
  + [Manual Rules] f70c54274709  DOMAIN-SUFFIX,paylution.com
```

**Removed: 6** (showing first 6)
```
  - [blackmatrix7 PayPal] 359882143efe  DOMAIN-SUFFIX,venmo.info
  - [blackmatrix7 PayPal] 5441dcd9756d  USER-AGENT,PayPal*
  - [blackmatrix7 PayPal] 5d27ff730b23  DOMAIN-SUFFIX,paypal-referral.com
  - [blackmatrix7 PayPal] 6adaa541866e  DOMAIN-SUFFIX,krakenjs.com
  - [blackmatrix7 PayPal] 6b8c31e4e694  DOMAIN-SUFFIX,venmo.s3.amazonaws.com
  - [blackmatrix7 PayPal] bb60771a2e67  DOMAIN-SUFFIX,paypal.info
```
