#!/usr/bin/env python3
"""Post-generation online audit for linnux-x/surge rule repository.

Runs after the workflow generates .list files but BEFORE committing.
Performs online checks against upstream sources and Surge documentation.

Uses only the Python standard library so it runs in GitHub Actions without deps.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Ensure scripts/ is on the path so sibling module imports work
_scripts_dir = str(Path(__file__).resolve().parent)
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)

from http_util import fetch_text
from speedtest_sources import convert_speedtest
from sources import RULE_SPECS
from policy import BROAD_SHARED_SUFFIXES, SHARED_INFRA_EXEMPT_FILES

ROOT = Path(__file__).resolve().parents[1]
RULE_DIR = ROOT / "Rule"
MANUAL_DIR = ROOT / "Rule" / "Manual"
AUDIT_LOG = ROOT / "scripts" / "audit_report.json"

# ── Helpers ──────────────────────────────────────────────────────────

def fetch_all_sources(sources: dict[str, list[str]]) -> dict[str, str | None]:
    """Fetch every unique source once for reachability and count checks."""
    return {url: fetch_text(url) for url in sorted({u for urls in sources.values() for u in urls})}


def non_comment_rules(path: Path) -> list[str]:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        lines.append(s)
    return lines


# ── Audit Checks ─────────────────────────────────────────────────────

def check_upstream_reachability(
    sources: dict[str, list[str]],
    contents: dict[str, str | None],
) -> list[dict]:
    """Verify all upstream source URLs are reachable (using prefetched content)."""
    findings: list[dict] = []
    for target, urls in sorted(sources.items()):
        for url in urls:
            content = contents.get(url)
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


def check_upstream_vs_generated(
    sources: dict[str, list[str]],
    contents: dict[str, str | None],
) -> list[dict]:
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

        # Manual append rules (Rule/Manual/<name>.txt) are merged into the
        # generated file on top of upstream content. Subtract them before the
        # ratio comparison, otherwise every file with manual additions
        # permanently exceeds its upstream count and warns on every run.
        manual_file = MANUAL_DIR / f"{target.rsplit('.', 1)[0]}.txt"
        if manual_file.is_file():
            manual_count = len(non_comment_rules(manual_file))
            gen_count = max(gen_count - manual_count, 0)

        upstream_total = 0
        for url in urls:
            content = contents.get(url)
            if content:
                fmt = next((fmt for _, source_url, fmt in RULE_SPECS[target][1] if source_url == url), None)
                if fmt and fmt.startswith("speedtest-"):
                    upstream_total += len(convert_speedtest(content.splitlines(), fmt))
                    continue
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
    
    This checks against a broader list (policy.BROAD_SHARED_SUFFIXES) than
    the strict commit-blocking tier to catch new patterns early.
    """
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

    # Aggregate rulesets exempt from this scan (shared with rule_validator)
    SERVICE_EXEMPT = SHARED_INFRA_EXEMPT_FILES

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


GFW_LIST_URL = "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/gfw.txt"


def parse_domain_set(text: str) -> set[str]:
    """Parse a Surge DOMAIN-SET body into bare lower-case suffixes."""
    out: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.add(line.lstrip(".").lower())
    return out


def china_direct_blocked_entries(blocked: set[str], china_rules: list[str],
                                 route) -> list[tuple[str, str]]:
    """China.list DOMAIN/DOMAIN-SUFFIX entries that a blocklist covers and
    that still resolve to China.list under first-match order.

    ``route(domain)`` returns the simulated ``"<ruleset>→<policy>"`` result.
    Entries already caught by an earlier proxy rule are not reported.
    """
    leaks: list[tuple[str, str]] = []
    for rule in china_rules:
        parts = [part.strip() for part in rule.split(",")]
        if len(parts) < 2 or parts[0].upper() not in {"DOMAIN", "DOMAIN-SUFFIX"}:
            continue
        domain = parts[1].lower()
        labels = domain.split(".")
        hit = next((".".join(labels[i:]) for i in range(len(labels) - 1)
                    if ".".join(labels[i:]) in blocked), None)
        if hit and route(domain).startswith("China.list"):
            leaks.append((rule, hit))
    return leaks


def check_china_direct_vs_gfw() -> list[dict]:
    """A blocked overseas domain must never fall through to China/DIRECT.

    ChinaMaxNoIP is a broad crawled list; the GFW list is an independent
    signal that an entry cannot work over a direct connection.
    """
    text = fetch_text(GFW_LIST_URL)
    if text is None:
        return [{"severity": "WARN", "check": "china_gfw",
                 "message": "Cannot fetch GFW list — China direct leak check skipped"}]
    import test_routing_order as routing
    order = routing.load_routing_order()
    rulesets = {path.name: routing.load_ruleset(path) for path in RULE_DIR.glob("*.list")}
    leaks = china_direct_blocked_entries(
        parse_domain_set(text), non_comment_rules(RULE_DIR / "China.list"),
        lambda domain: routing.simulate_routing(domain, order, rulesets),
    )
    return [{"severity": "ERROR", "check": "china_gfw",
             "message": f"China.list routes GFW-listed {hit} DIRECT via {rule}; "
                        "exclude it in Rule/Manual/China.exclude.txt"}
            for rule, hit in leaks]


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
    """Independently reject malformed exclusions and leaked rule identities.

    Explicit Manual includes override upstream exclusions. Domain options cannot
    bypass exclusion; non-domain rules retain exact-line option semantics.
    """
    findings: list[dict] = []

    for list_path in sorted(RULE_DIR.glob("*.list")):
        target = list_path.name
        name_no_ext = target.rsplit(".", 1)[0]
        exclude_file = MANUAL_DIR / f"{name_no_ext}.exclude.txt"

        if not exclude_file.exists() or not exclude_file.is_file():
            continue

        # Read exclude patterns
        excludes = []
        for line in exclude_file.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            excludes.append(s)

        if not excludes:
            continue

        # Independent post-generation check: domain identity ignores options,
        # other rule types retain their full-line semantics. Manual includes
        # deliberately override upstream exclusions and are checked separately.
        rules = non_comment_rules(list_path)
        manual = MANUAL_DIR / f"{name_no_ext}.txt"
        included = set(non_comment_rules(manual)) if manual.exists() else set()
        rules = [rule for rule in rules if rule not in included]

        leaking_excludes = []
        for exc in excludes:
            parts = exc.split(',')
            if len(parts) < 2:
                findings.append({'severity': 'ERROR', 'check': 'exclude_coverage',
                                 'target': target, 'detail': f'排除条目缺少规则类型: {exc}'})
                continue
            if parts[0] in {'DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD', 'DOMAIN-WILDCARD'}:
                matched = any([p.lower() for p in r.split(',')[:2]] == [p.lower() for p in parts[:2]] for r in rules)
            else:
                matched = exc in rules
            if matched:
                leaking_excludes.append(exc)

        if leaking_excludes:
            for exc in leaking_excludes:
                findings.append({
                    "severity": "ERROR",
                    "check": "exclude_coverage",
                    "target": target,
                    "detail": f"排除条目在生成文件中仍存在（排除未生效）: {exc}",
                })

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

    # 0. Prefetch every unique upstream URL once (shared by checks 1 and 2)
    print("0️⃣  Prefetching upstream sources (single pass)...")
    contents = fetch_all_sources(sources)
    print(f"   → {len(contents)} unique URLs fetched\n")

    # 1. Upstream reachability
    print("1️⃣  Checking upstream source reachability...")
    findings = check_upstream_reachability(sources, contents)
    all_findings.extend(findings)
    print(f"   → {len(findings)} issues\n")

    # 2. Upstream vs generated comparison
    print("2️⃣  Comparing upstream vs generated rule counts...")
    findings = check_upstream_vs_generated(sources, contents)
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

    # 6. GFW-listed domains must not reach China/DIRECT
    print("6️⃣  Checking China.list against the GFW list...")
    findings = check_china_direct_vs_gfw()
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
