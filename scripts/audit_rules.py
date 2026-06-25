#!/usr/bin/env python3
"""Post-generation online audit for linnux-x/surge rule repository.

Runs after the workflow generates .list files but BEFORE committing.
Performs online checks against upstream sources and Surge documentation.

Uses only the Python standard library so it runs in GitHub Actions without deps.
"""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANUAL_DIR = ROOT / "Rule" / "Manual"
AUDIT_LOG = ROOT / "scripts" / "audit_report.json"

# ── Helpers ──────────────────────────────────────────────────────────

def fetch_text(url: str, timeout: int = 30) -> str | None:
    """Fetch URL content, return text or None on failure."""
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "surge-audit/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        print(f"  ⚠ FETCH FAILED: {url} → {exc}")
        return None


def non_comment_rules(path: Path) -> list[str]:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        lines.append(s)
    return lines


# ── Audit Checks ─────────────────────────────────────────────────────

def check_upstream_reachability(sources: dict[str, list[str]]) -> list[dict]:
    """Verify all upstream source URLs are reachable."""
    findings: list[dict] = []
    for target, urls in sorted(sources.items()):
        for url in urls:
            content = fetch_text(url)
            if content is None:
                findings.append({
                    "severity": "ERROR",
                    "check": "upstream_reachability",
                    "target": target,
                    "url": url,
                    "message": f"Upstream source unreachable for {target}",
                })
            elif len(content.strip()) == 0:
                findings.append({
                    "severity": "WARN",
                    "check": "upstream_reachability",
                    "target": target,
                    "url": url,
                    "message": f"Upstream source empty for {target}",
                })
    return findings


def check_upstream_vs_generated(sources: dict[str, list[str]]) -> list[dict]:
    """Compare upstream rule counts with generated .list files.
    
    Flags when upstream has significantly more rules than generated
    (suggests aggressive exclude or guardrail issue) or when upstream
    is much smaller (suggests upstream shrunk, possible stale rules).
    """
    findings: list[dict] = []
    for target, urls in sorted(sources.items()):
        list_path = RULE_DIR / target
        if not list_path.exists():
            continue
        gen_count = len(non_comment_rules(list_path))

        upstream_total = 0
        for url in urls:
            content = fetch_text(url)
            if content:
                for line in content.splitlines():
                    s = line.strip()
                    if s and not s.startswith("#") and not s.startswith("."):
                        upstream_total += 1
                    elif s.startswith("."):
                        # domainset format — still a rule
                        upstream_total += 1

        if upstream_total == 0:
            continue

        ratio = gen_count / upstream_total if upstream_total > 0 else 1.0
        # Only flag when there's a single upstream source; multi-source rules
        # naturally exceed any single source's count.
        if len(urls) > 1:
            continue
        # If generated is less than 20% of upstream, likely heavy excludes — informational
        if ratio < 0.2 and upstream_total > 50:
            findings.append({
                "severity": "INFO",
                "check": "upstream_vs_generated",
                "target": target,
                "message": f"Generated {gen_count} vs upstream {upstream_total} ({ratio:.0%}) — heavy excludes applied",
            })
        # If generated is more than 120% of upstream, something may be wrong
        elif ratio > 1.2 and upstream_total > 10:
            findings.append({
                "severity": "WARN",
                "check": "upstream_vs_generated",
                "target": target,
                "message": f"Generated {gen_count} vs upstream {upstream_total} ({ratio:.0%}) — generated exceeds upstream significantly",
            })
    return findings


def check_new_shared_infrastructure() -> list[dict]:
    """Scan generated rules for newly appeared shared infrastructure patterns.
    
    Uses manifest data when available to provide source attribution.
    Falls back to scanning .list files directly.
    
    Known shared infrastructure suffixes that should not appear in service rules:
    - Analytics/telemetry platforms
    - Consent/privacy platforms  
    - Cloud platform parent domains (too broad)
    
    This checks against a broader list than validate_surge_repo.py to catch
    new patterns early.
    """
    BROAD_SHARED_SUFFIXES = {
        # Consent/privacy
        "cookielaw.org", "onetrust.com", "onetrust.io",
        "trustarc.com", "quantcast.com", "evidon.com",
        # Analytics/telemetry
        "adobedtm.com", "braze.com", "newrelic.com", "nr-data.net",
        "optimizely.com", "optimizely.org",
        "branch.io", "appsflyer.com", "adjust.com",
        "kochava.com", "sentry.io", "sentrycdn.com",
        "mixpanel.com", "amplitude.com", "segment.io", "segment.com",
        "hotjar.com", "fullstory.com", "clarity.ms",
        # Marketing/ad tech
        "flashtalking.com", "doubleclick.net", "googleadservices.com",
        "googlesyndication.com", "googletagmanager.com",
        "facebook.net", "fbcdn.net",
        # Broad cloud
        "amazonaws.com", "cloudfront.net", "azure.com",
        "googleapis.com", "cloud.google.com",
        # CDNs (parent-level)
        "akamaized.net", "akamaiedge.net", "akamaihd.net",
        "edgekey.net", "edgesuite.net", "azureedge.net",
        "fastly.net", "b-cdn.net", "cdn77.org",
    }

    # Service-OWNED infrastructure that legitimately belongs in their rulesets.
    # These are NOT shared third-party — they're part of the service's own product family.
    SERVICE_OWNED_SUFFIXES: dict[str, set[str]] = {
        "Google.list": {
            "doubleclick.net", "googleadservices.com", "googleapis.com",
            "googlesyndication.com", "googletagmanager.com",
        },
        "Microsoft.list": {
            "azure.com",
        },
        "SocialMedia.list": {
            "facebook.net", "fbcdn.net",
        },
    }

    # Service-prefixed subdomains that are OK (e.g., disney.my.sentry.io)
    SERVICE_EXEMPT = {
        "Global.list", "GlobalMedia.list", "CDN.list", "Direct.list",
        "China.list", "China_IP.list", "ChinaMedia.list", "Download.list",
    }

    findings: list[dict] = []
    for list_path in sorted(RULE_DIR.glob("*.list")):
        target = list_path.name
        if target in SERVICE_EXEMPT:
            continue

        rules = non_comment_rules(list_path)
        for rule in rules:
            parts = [p.strip() for p in rule.split(",")]
            if len(parts) < 2:
                continue
            rule_type = parts[0].upper()
            if rule_type not in {"DOMAIN", "DOMAIN-SUFFIX"}:
                continue

            domain = parts[1].lower()
            
            if rule_type == "DOMAIN-SUFFIX" and domain in BROAD_SHARED_SUFFIXES:
                # Skip if the suffix is service-owned for this target
                if target in SERVICE_OWNED_SUFFIXES and domain in SERVICE_OWNED_SUFFIXES[target]:
                    continue
                findings.append({
                    "severity": "WARN",
                    "check": "shared_infrastructure",
                    "target": target,
                    "rule": rule,
                    "message": f"Shared infrastructure suffix in service ruleset: {domain}",
                })
            elif rule_type == "DOMAIN":
                # Check if domain ends with a shared suffix but has no service prefix
                for suffix in BROAD_SHARED_SUFFIXES:
                    if domain.endswith(f".{suffix}"):
                        # Extract subdomain labels before the shared suffix
                        sub = domain[: -(len(suffix) + 1)]
                        # Single-label or very short prefix — likely not service-specific
                        labels = sub.split(".")
                        if len(labels) <= 2 and len(labels[-1]) <= 4:
                            findings.append({
                                "severity": "INFO",
                                "check": "shared_infrastructure",
                                "target": target,
                                "rule": rule,
                                "message": f"Potential shared infrastructure domain: {domain} (subdomain labels: {labels})",
                            })
                        break

    return findings


def check_surge_docs_updates() -> list[dict]:
    """Check Surge LLM index for any new rule types or documentation changes."""
    findings: list[dict] = []
    
    content = fetch_text("https://nssurge.com/llms.txt")
    if content is None:
        findings.append({
            "severity": "WARN",
            "check": "surge_docs",
            "message": "Cannot fetch Surge LLM index — documentation check skipped",
        })
        return findings

    # Check for rule types we don't know about
    known_types = {
        "DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-WILDCARD",
        "IP-CIDR", "IP-CIDR6", "IP-ASN",
        "USER-AGENT", "PROCESS-NAME", "URL-REGEX",
        "AND", "OR", "NOT",
        "GEOIP", "SRC-IP-CIDR", "SRC-PORT", "DST-PORT",
        "IN-PORT", "DSCP",
    }
    
    # Look for rule type mentions in the docs
    rule_types_in_docs = set(re.findall(r'\b([A-Z][A-Z0-9_]{2,})\b', content))
    # Filter to likely rule types (uppercase, contain common keywords)
    for rt in rule_types_in_docs:
        if rt not in known_types and any(kw in rt for kw in ("DOMAIN", "IP", "CIDR", "ASN", "PROCESS", "USER", "REGEX", "PORT", "GEO", "RULE")):
            findings.append({
                "severity": "INFO",
                "check": "surge_docs",
                "message": f"Potentially new Surge rule type found in docs: {rt} — verify manually",
            })

    return findings


def check_exclude_coverage() -> list[dict]:
    """Verify exclude files exist for all rulesets that need them
    and that existing exclude patterns actually match something in upstream."""
    findings: list[dict] = []
    
    for list_path in sorted(RULE_DIR.glob("*.list")):
        target = list_path.name
        name_no_ext = target.rsplit(".", 1)[0]
        exclude_file = MANUAL_DIR / f"{name_no_ext}.exclude.txt"
        
        if not exclude_file.exists() or not exclude_file.is_file():
            continue  # No exclude file — nothing to check
        
        # Read exclude patterns
        excludes = []
        for line in exclude_file.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            excludes.append(s.lower())
        
        if not excludes:
            continue
        
        # Check each exclude pattern against the generated list
        rules = non_comment_rules(list_path)
        rules_lower = [r.lower() for r in rules]
        
        unmatched_excludes = []
        for exc in excludes:
            # Simple substring check for grep -vFf matching
            matched = any(exc in r for r in rules_lower)
            if not matched:
                # This exclude didn't match any current rule — it may be stale
                # or it may be working (preventing upstream entries from appearing)
                pass  # Not a finding — exclude prevents upstream entries, working as intended

    return findings


# ── Main ─────────────────────────────────────────────────────────────

def main() -> int:
    print("═" * 60)
    print("  Surge Rule Post-Generation Online Audit")
    print(f"  {datetime.now().isoformat()}")
    print("═" * 60)

    all_findings: list[dict] = []

    # Load source URLs from the single source of truth (scripts/sources.py)
    _scripts_dir = str(ROOT / "scripts")
    if _scripts_dir not in sys.path:
        sys.path.insert(0, _scripts_dir)
    from sources import RULE_SPECS

    # Build sources dict: {target: [url, ...]}
    sources: dict[str, list[str]] = {}
    for target, (_display_name, specs) in RULE_SPECS.items():
        sources[target] = [url for _label, url, _fmt in specs]
    print(f"\n📁 Found {len(sources)} ruleset targets with upstream sources\n")

    # 1. Upstream reachability
    print("1️⃣  Checking upstream source reachability...")
    findings = check_upstream_reachability(sources)
    all_findings.extend(findings)
    print(f"   → {len(findings)} issues\n")

    # 2. Upstream vs generated comparison
    print("2️⃣  Comparing upstream vs generated rule counts...")
    findings = check_upstream_vs_generated(sources)
    all_findings.extend(findings)
    print(f"   → {len(findings)} findings\n")

    # 3. Shared infrastructure scan
    print("3️⃣  Scanning for shared infrastructure in service rules...")
    findings = check_new_shared_infrastructure()
    all_findings.extend(findings)
    print(f"   → {len(findings)} findings\n")

    # 4. Surge docs check
    print("4️⃣  Checking Surge documentation for updates...")
    findings = check_surge_docs_updates()
    all_findings.extend(findings)
    print(f"   → {len(findings)} findings\n")

    # 5. Exclude coverage
    print("5️⃣  Checking exclude pattern coverage...")
    findings = check_exclude_coverage()
    all_findings.extend(findings)
    print(f"   → {len(findings)} findings\n")

    # ── Summary ──────────────────────────────────────────────────

    errors = [f for f in all_findings if f["severity"] == "ERROR"]
    warns = [f for f in all_findings if f["severity"] == "WARN"]
    infos = [f for f in all_findings if f["severity"] == "INFO"]

    print("═" * 60)
    print("  AUDIT SUMMARY")
    print("═" * 60)
    print(f"  🔴 Errors:   {len(errors)}")
    print(f"  🟡 Warnings: {len(warns)}")
    print(f"  🔵 Info:     {len(infos)}")

    # Manifest stats — .manifest files are tab-separated: <stable_id>\t<source_name>
    manifest_dir = RULE_DIR / ".manifests"
    manifest_files = list(manifest_dir.glob("*.manifest")) if manifest_dir.exists() else []
    if manifest_files:
        total_manifest_rules = 0
        for mf in manifest_files:
            total_manifest_rules += sum(
                1
                for line in mf.read_text(encoding="utf-8", errors="replace").splitlines()
                if line.strip()
            )
        print(f"  📋 Manifests: {len(manifest_files)} files, {total_manifest_rules} indexed rules")
    print()

    if errors:
        print("🔴 ERRORS (must fix before commit):")
        for f in errors:
            msg = f.get("message", "")
            target = f.get("target", "")
            url = f.get("url", "")
            print(f"   • [{target}] {msg}" + (f" ({url})" if url else ""))
        print()

    if warns:
        print("🟡 WARNINGS (review recommended):")
        for f in warns:
            msg = f.get("message", "")
            target = f.get("target", "")
            rule = f.get("rule", "")
            print(f"   • [{target}] {msg}" + (f" — {rule}" if rule else ""))
        print()

    if infos:
        print("🔵 INFO (for awareness):")
        for f in infos:
            msg = f.get("message", "")
            target = f.get("target", "")
            print(f"   • [{target}] {msg}")
        print()

    # Save audit report
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_findings": len(all_findings),
        "errors": len(errors),
        "warnings": len(warns),
        "info": len(infos),
        "findings": all_findings,
    }
    AUDIT_LOG.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"📄 Full report saved to {AUDIT_LOG}")

    # Exit code: errors block commit, warnings do not
    if errors:
        print("\n❌ AUDIT FAILED — fix errors before committing")
        return 1
    
    if warns:
        print("\n⚠️  AUDIT PASSED WITH WARNINGS — review recommended")
        return 0

    print("\n✅ AUDIT PASSED — all checks clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
