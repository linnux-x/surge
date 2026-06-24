# Validate Script Enhancement Pattern

When adding new semantic exclude patterns to `Rule/Manual/*.exclude.txt`, always add matching invariant checks to `scripts/validate_surge_repo.py`. The validate script catches regressions that manual review misses.

## Workflow

1. Identify the pattern class (e.g., "shared third-party infrastructure in service rulesets").
2. Add exclude entries to `Rule/Manual/<Name>.exclude.txt`.
3. Add invariant checks to `validate_surge_repo.py`:
   - Define the pattern set as a constant (e.g., `SHARED_THIRD_PARTY_SUFFIXES`).
   - Define exempt rulesets where the pattern is allowed (e.g., `Global.list`, `CDN.list`).
   - Add the check in `validate_rule_file()` alongside existing project-policy checks.
4. Run validate — confirm it catches current violations.
5. Run workflow to regenerate `.list` files with excludes applied.
6. Run validate again — confirm all violations are resolved.

## Concrete Checks Added (2026-06)

### SHARED_THIRD_PARTY_SUFFIXES / SHARED_THIRD_PARTY_DOMAINS

Shared third-party infrastructure that should not appear in service-specific rulesets:

- `cookielaw.org` — OneTrust cookie consent (thousands of sites)
- `onetrust.com` — OneTrust privacy platform (thousands of sites)
- `adobedtm.com` — Adobe Tag Manager
- `braze.com` — Marketing/engagement platform
- `newrelic.com` — New Relic APM
- `nr-data.net` — New Relic data collection
- `optimizely.com` — A/B testing
- `segment.io` — Customer Data Platform
- `sentry.io` — Error tracking platform
- `js-agent.newrelic.com` — New Relic JS agent (exact domain)

**Discovery:** The `optimizely.com` check caught `DOMAIN-SUFFIX,optimizely.com` in `Microsoft.list` that manual audit of all 23 rulesets had missed. The `segment.io` and `sentry.io` checks caught opaque Sentry ingest endpoints in `AI.list`. This validates the pattern — automate the check, don't rely on human review alone.

Exempt rulesets: Global, GlobalMedia, CDN, Direct, China, China_IP, ChinaMedia, Download.

### DOMAIN-SUFFIX Subdomain Check for Shared Suffixes

Added in 2026-06. Extends the shared suffix check from exact matches to subdomains under shared suffixes:

```python
elif rule_type == "DOMAIN-SUFFIX":
    for suffix in SHARED_THIRD_PARTY_SUFFIXES:
        if domain_val.endswith(f".{suffix}"):
            # Allow if the subdomain has a clear service/brand prefix
            sub = domain_val[: -(len(suffix) + 1)]
            first_label = sub.split(".")[0].lower()
            # Opaque IDs are NOT service prefixes
            is_opaque = (
                first_label.isdigit()
                or all(c in "0123456789abcdef" for c in first_label)
                or (len(first_label) <= 6 and any(c.isdigit() for c in first_label) and not first_label.isalpha())
            )
            if is_opaque:
                errors.append(...)
```

This catches `DOMAIN-SUFFIX,o207216.ingest.sentry.io` as shared infrastructure while allowing `DOMAIN-SUFFIX,disney.my.sentry.io` through.

### PAYPAL_CN_DOMAINS

PayPal China domestic domains that should be in `China.list`, not `PayPal.list`:

anfutong.cn, anfutong.com, anfutong.com.cn, beibao.cn, beibao.com, beibao.com.cn, paypal.cn, paypal.com.cn, paypal.net.cn, paypal.org.cn, paypal-corp.cn, paypal-corp.com.cn, paypal-notice.cn, paypal-notice.com.cn, paypalcommunity.cn, paypalhere.cn, paypalhere.com.cn, paypalobjects.cn, paypalobjects.com.cn, xoom.net.cn, xn--bnq297cix3a.cn.

### SERVICE_OWNED_SUFFIXES Exemption

Some suffixes that look like shared infrastructure are actually owned by the service that the ruleset is named after. These must be exempted from the shared suffix check:

| Ruleset | Owned Suffixes |
|---------|---------------|
| `Google.list` | `doubleclick.net`, `googleadservices.com`, `googleapis.com`, `googlesyndication.com`, `googletagmanager.com`, `googleanalytics.com` |
| `Microsoft.list` | `azure.com`, `live.com`, `msn.com`, `microsoftonline.com`, `office.com`, `office365.com` |
| `SocialMedia.list` (Meta) | `facebook.net`, `fbcdn.net`, `fbsbx.com`, `instagram.com` |
| `Apple.list` | `apple.com` |
| `Apple_CN.list` | `apple.com` |

Implementation in audit_rules.py and validate_surge_repo.py: a dict mapping target filename → set of owned suffixes:

```python
SERVICE_OWNED_SUFFIXES = {
    "Google.list": {"doubleclick.net", "googleadservices.com", "googleapis.com", ...},
    "Microsoft.list": {"azure.com", "live.com", "msn.com", ...},
    ...
}
```

Before flagging a shared suffix, check if the current target is in `SERVICE_OWNED_SUFFIXES` and the suffix is in that target's owned set. If so, skip the warning.

### Prefix Heuristic for Service-Specific Subdomains

When checking shared third-party suffixes, `DOMAIN` rules whose value is a subdomain of a shared suffix are treated with a prefix heuristic: if the subdomain has an explicit service/brand prefix (e.g., `disney.my.sentry.io`, `disney-portal.my.onetrust.com`), it is considered service-specific and not flagged. The validate script currently allows these through — they should be reviewed manually if they appear.

The DOMAIN-SUFFIX subdomain check (above) extends this to DOMAIN-SUFFIX type rules, adding the opaque-ID heuristic to distinguish brand prefixes from random/hex identifiers.

## Pattern: Exclude File → Validate Check → Workflow Regenerate

| Step | Action | Verification |
|---|---|---|
| 1 | Add exclude entries | `cat Rule/Manual/<Name>.exclude.txt` |
| 2 | Add validate checks | `python3 scripts/validate_surge_repo.py` shows violations |
| 3 | Run workflow | `gh workflow run auto-rules.yml` |
| 4 | Pull & validate | `git pull && python3 scripts/validate_surge_repo.py` passes |
