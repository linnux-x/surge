#!/usr/bin/env python3
"""Replay legacy/current/all-distribution entrypoints from a frozen audit cache.

Only affected rulesets and Global are regenerated in temporary directories;
other rulesets retain the checkout baseline. No network or production writes.
"""
from __future__ import annotations
import argparse
import contextlib
import json
import os
from pathlib import Path
import shutil
import tempfile
from unittest.mock import patch

import generate_rules as generator
from audit_upstream_sources import ROOT, snapshot, sha
from sources import RULE_SPECS, SUKKA_ENTRYPOINT_PATHS, SUKKA, SUKKA_SOURCE
from test_routing_order import load_ruleset


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    cache, output = args.cache.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    def fetch(url, fmt):
        record = snapshot(url, cache, False)
        if not record.get('sha256'):
            raise ValueError('Unavailable snapshot: ' + url)
        return (cache / record['cache_file']).read_text().splitlines()

    targets = [name for name, (_, specs) in RULE_SPECS.items()
               if any(label in SUKKA_ENTRYPOINT_PATHS for label, _, _ in specs)]
    if 'Global.list' not in targets:
        targets.append('Global.list')
    results = {}
    previous = Path.cwd()
    try:
        with tempfile.TemporaryDirectory(prefix='surge-entrypoints-') as temp:
            for mode in ('legacy', 'adopted', 'distribution'):
                work = Path(temp) / mode
                shutil.copytree(ROOT / 'Rule', work / 'Rule')
                os.chdir(work)
                with patch.object(generator, 'fetch_source', fetch), (output / (mode + '.log')).open('w') as log, contextlib.redirect_stdout(log):
                    for target in targets:
                        display, specs = RULE_SPECS[target]
                        selected = []
                        for label, url, fmt in specs:
                            if label in SUKKA_ENTRYPOINT_PATHS and mode != 'adopted':
                                url = (SUKKA_SOURCE if mode == 'legacy' else SUKKA) + '/' + SUKKA_ENTRYPOINT_PATHS[label]
                            selected.append((label, url, fmt))
                        generator.process_rule(target, display, selected)
                    generator.prune_global_first_match_overlaps()
                results[mode] = {p.name: load_ruleset(p) for p in (work / 'Rule').glob('*.list')}
                os.chdir(previous)
    finally:
        os.chdir(previous)
    report = {'sources_sha256': sha((ROOT / 'scripts/sources.py').read_bytes()),
              'scope': 'Frozen upstreams; affected rulesets and Global regenerated; other rulesets retain checkout baseline; comments and order excluded.',
              'baseline_sha256': {p.name: sha(p.read_bytes()) for p in sorted((ROOT / 'Rule').glob('*.list'))},
              'comparisons': {}}
    for mode in ('adopted', 'distribution'):
        changes = {}
        for name, old in results['legacy'].items():
            new = results[mode][name]
            if old != new:
                changes[name] = {'added': sorted(new - old), 'removed': sorted(old - new)}
        report['comparisons'][mode] = changes
    (output / 'entrypoint-rule-diff.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({mode: {name: {key: len(value) for key, value in diff.items()}
          for name, diff in changes.items()} for mode, changes in report['comparisons'].items()}))


if __name__ == '__main__':
    main()
