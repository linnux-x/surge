#!/usr/bin/env python3
"""Snapshot upstreams and quantify within-ruleset contribution without editing rules.

--refresh fetches every URL once; otherwise replay the immutable local cache.
Coverage is conservative: exact rules, DOMAIN-SUFFIX containment and CIDR union.
It does not infer ASN, keyword/wildcard containment or real traffic benefit.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import ipaddress
import json
from pathlib import Path
import subprocess

from speedtest_sources import convert_speedtest
from sources import RULE_SPECS, SUKKA_ENTRYPOINT_PATHS, SUKKA, SUKKA_SOURCE
from generate_rules import clean_source, convert_domainset, convert_cidr, filter_candidates, apply_project_guardrails

ROOT = Path(__file__).resolve().parents[1]
LEGACY_SUKKA = SUKKA_SOURCE + '/'
SUKKA_DISTRIBUTION = SUKKA + '/'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def snapshot(url: str, cache: Path, refresh: bool) -> dict:
    key = sha(url.encode())
    metadata = cache / (key + '.json')
    body = cache / (key + '.txt')
    if not refresh:
        record = json.loads(metadata.read_text())
        if record.get('url') != url:
            raise ValueError('Snapshot URL mismatch: ' + url)
        if record.get('sha256') and sha(body.read_bytes()) != record['sha256']:
            raise ValueError('Snapshot body hash mismatch: ' + url)
        return record
    record = {'url': url, 'checked_at': datetime.now(timezone.utc).isoformat(), 'status': 'unavailable'}
    result = subprocess.run(['curl', '-fLsS', '--connect-timeout', '10', '--max-time', '60', '--retry', '1', url],
                            capture_output=True, timeout=140)
    if result.returncode == 0:
        content = result.stdout
        record['status'] = 'live'
    else:
        content = None
        record['fetch_exit'] = result.returncode
    if content is not None:
        body.write_bytes(content)
        record.update(sha256=sha(content), bytes=len(content), cache_file=body.name)
    metadata.write_text(json.dumps(record, indent=2) + '\n')
    return record


def normalize(target: str, fmt: str | None, content: str, manual: bool = False) -> set[str]:
    lines = (convert_speedtest(content.splitlines(), fmt) if fmt and fmt.startswith("speedtest-") else clean_source(content.splitlines()))
    if fmt == 'domainset':
        lines = convert_domainset(lines)
    elif fmt == 'cidr':
        lines = convert_cidr(lines)
    if not manual:
        lines = filter_candidates(lines, ROOT / 'Rule/Manual' / (target[:-5] + '.exclude.txt'))
    lines = apply_project_guardrails(target, lines)
    return {line.lower() for line in lines if line.strip() and not line.startswith('#')}


def merge_intervals(intervals):
    out = []
    for lo, hi in sorted(intervals):
        if out and lo <= out[-1][1] + 1:
            out[-1] = (out[-1][0], max(hi, out[-1][1]))
        else:
            out.append((lo, hi))
    return out


class Coverage:
    def __init__(self, rules: set[str]):
        self.exact = rules
        self.suffixes = set()
        self.ranges = {}
        for rule in rules:
            parts = rule.split(',')
            if len(parts) < 2:
                continue
            kind, value, *options = parts
            opts = tuple(sorted(options))
            if kind == 'domain-suffix':
                self.suffixes.add((value, opts))
            elif kind in ('ip-cidr', 'ip-cidr6'):
                net = ipaddress.ip_network(value, strict=False)
                self.ranges.setdefault((net.version, opts), []).append((int(net.network_address), int(net.broadcast_address)))
        self.ranges = {key: merge_intervals(values) for key, values in self.ranges.items()}
        self.starts = {key: [a for a, _ in values] for key, values in self.ranges.items()}

    def residual(self, rule: str) -> list[str]:
        if rule in self.exact:
            return []
        kind, value, *options = rule.split(',')
        opts = tuple(sorted(options))
        if kind in ('domain', 'domain-suffix'):
            labels = value.split('.')
            if any(('.'.join(labels[i:]), opts) in self.suffixes for i in range(len(labels))):
                return []
        elif kind in ('ip-cidr', 'ip-cidr6'):
            net = ipaddress.ip_network(value, strict=False)
            lo, hi = int(net.network_address), int(net.broadcast_address)
            key = (net.version, opts)
            ranges = self.ranges.get(key, [])
            start = max(0, bisect_right(self.starts.get(key, []), lo) - 1)
            uncovered = []
            cursor = lo
            for a, b in ranges[start:]:
                if a > hi:
                    break
                if b < cursor:
                    continue
                if a > cursor:
                    uncovered.append((cursor, a - 1))
                cursor = max(cursor, b + 1)
                if cursor > hi:
                    break
            if cursor <= hi:
                uncovered.append((cursor, hi))
            address = ipaddress.IPv4Address if net.version == 4 else ipaddress.IPv6Address
            tail = ',' + ','.join(options) if options else ''
            return [kind + ',' + str(n) + tail for a, b in uncovered
                    for n in ipaddress.summarize_address_range(address(a), address(b))]
        return [rule]


def contribution(rules: set[str], peers: set[str]) -> dict:
    coverage = Coverage(peers)
    residual = sorted({r for rule in rules for r in coverage.residual(rule)})
    ip_counts = {4: 0, 6: 0}
    ip_networks = {4: [], 6: []}
    for rule in residual:
        kind, value, *_ = rule.split(',')
        if kind in ('ip-cidr', 'ip-cidr6'):
            net = ipaddress.ip_network(value, strict=False)
            ip_networks[net.version].append(net)
    for version, nets in ip_networks.items():
        ip_counts[version] = sum(n.num_addresses for n in ipaddress.collapse_addresses(nets))
    return {'normalized_rules': len(rules), 'exact_shared_rules': len(rules & peers),
            'fully_covered_rules': sum(not coverage.residual(rule) for rule in rules),
            'residual_rules': residual,
            'residual_ipv4_addresses': str(ip_counts[4]), 'residual_ipv6_addresses': str(ip_counts[6])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    if args.refresh and args.cache.exists() and any(args.cache.iterdir()):
        parser.error('--refresh requires a new empty cache directory; existing snapshots are immutable')
    args.cache.mkdir(parents=True, exist_ok=True)
    args.output.mkdir(parents=True, exist_ok=True)
    urls = {url for _, specs in RULE_SPECS.values() for _, url, _ in specs}
    candidates = {LEGACY_SUKKA + path: SUKKA_DISTRIBUTION + path for path in SUKKA_ENTRYPOINT_PATHS.values()}
    urls |= set(candidates) | set(candidates.values())
    with ThreadPoolExecutor(max_workers=6) as pool:
        records = dict(zip(sorted(urls), pool.map(lambda u: snapshot(u, args.cache, args.refresh), sorted(urls))))
    report = {'schema': 1, 'sources_sha256': sha((ROOT / 'scripts/sources.py').read_bytes()), 'manual_sha256': {p.name: sha(p.read_bytes()) for p in sorted((ROOT / 'Rule/Manual').glob('*.txt'))}, 'records': records, 'contributions': [], 'entrypoint_comparisons': []}
    for target, (_, specs) in RULE_SPECS.items():
        sources = {}
        for label, url, fmt in specs:
            record = records[url]
            if not record.get('sha256'):
                raise SystemExit('Unavailable source; contribution is not safely measurable: ' + url)
            sources[label] = normalize(target, fmt, (args.cache / record['cache_file']).read_text())
            if label in SUKKA_ENTRYPOINT_PATHS:
                old_url = LEGACY_SUKKA + SUKKA_ENTRYPOINT_PATHS[label]
                new_url = candidates[old_url]
                old_record = records[old_url]
                if not old_record.get("sha256"):
                    raise SystemExit("Unavailable comparison source: " + old_url)
                old_rules = normalize(target, fmt, (args.cache / old_record["cache_file"]).read_text())
                new = records[new_url]
                if new.get('sha256'):
                    candidate = normalize(target, fmt, (args.cache / new['cache_file']).read_text())
                    report['entrypoint_comparisons'].append({'target': target, 'source': label,
                        'old_url': old_url, 'new_url': new_url, 'adopted': url == new_url,
                        'old_rules': len(old_rules), 'new_rules': len(candidate),
                        'added': sorted(candidate - old_rules), 'removed': sorted(old_rules - candidate)})
                else:
                    raise SystemExit('Unavailable comparison candidate: ' + new_url)
        manual = ROOT / 'Rule/Manual' / (target[:-5] + '.txt')
        if manual.exists():
            sources['Manual'] = normalize(target, None, manual.read_text(), manual=True)
        for label, rules in sources.items():
            peers = set().union(*(values for name, values in sources.items() if name != label))
            report['contributions'].append({'target': target, 'source': label, **contribution(rules, peers)})
    (args.output / 'upstream-contributions.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    lines = ['# Upstream contribution snapshot', '',
             'Conservative coverage within each ruleset, including Manual. Residual does not imply observed traffic benefit.',
             'CIDR residual counts may split one input into several ranges. ASN/keyword/wildcard semantic containment is not inferred.', '',
             '| Ruleset | Source | Normalized | Exact shared | Fully covered | Residual fragments | Unique IPv4 addresses |',
             '|---|---|---:|---:|---:|---:|---:|']
    for r in report['contributions']:
        lines.append(f"| {r['target']} | {r['source']} | {r['normalized_rules']} | {r['exact_shared_rules']} | {r['fully_covered_rules']} | {len(r['residual_rules'])} | {r['residual_ipv4_addresses']} |")
    lines += ['', '## Entrypoint candidates', '', '| Ruleset | Old | Candidate | Added | Removed |', '|---|---:|---:|---:|---:|']
    for r in report['entrypoint_comparisons']:
        lines.append(f"| {r['target']} | {r['old_rules']} | {r['new_rules']} | {len(r['added'])} | {len(r['removed'])} |")
    (args.output / 'upstream-contributions.md').write_text('\n'.join(lines) + '\n')
    print(f"Audited {len(records)} URLs; {len(report['contributions'])} source contributions; {len(candidates)} entrypoint candidates")


if __name__ == '__main__':
    main()
