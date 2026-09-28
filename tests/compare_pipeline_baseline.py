#!/usr/bin/env python3
"""Offline old/new comparison on the current public rule corpus; no writes to Rule/."""
from __future__ import annotations

import argparse
import contextlib
from datetime import datetime
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
BASE = '716da36709816751da26abd22a400ea650956ba9'


class FixedTime:
    @staticmethod
    def now(tz):
        return datetime(2026, 9, 27, tzinfo=tz)


def worker(scripts: Path) -> None:
    sys.path.insert(0, str(scripts))
    import generate_rules as generator
    import rule_validator as validator
    import sources

    result = {'specs': sources.RULE_SPECS, 'files': {}}
    started = time.perf_counter()
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        shutil.copytree(ROOT / 'Rule/Manual', root / 'Manual')
        for path in sorted((ROOT / 'Rule').glob('*.list')):
            raw = path.read_text().splitlines()
            target = root / path.name
            target.write_bytes(path.read_bytes())
            with contextlib.redirect_stdout(io.StringIO()) as log:
                generator.prune_redundant_cidr(target)
            pruned = target.read_text()
            prune_log = log.getvalue()
            errors = validator.validate_rule_file(validator.non_comment_rules(raw), path.name)
            with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root / 'Manual'), patch.object(generator, 'datetime', FixedTime), patch.object(generator, 'fetch_source', return_value=raw), patch.object(generator, 'REPO_URL', 'https://github.com/linnux-x/surge'), patch.object(generator, 'AUTHOR_NAME', 'linnux-x'), contextlib.redirect_stdout(io.StringIO()) as log:
                generator.process_rule(path.name, path.stem, [('Replay', 'https://example.test', None)])
            result['files'][path.name] = {
                'pruned': pruned, 'prune_log': prune_log, 'errors': errors,
                'generated': target.read_text(), 'generation_log': log.getvalue(),
            }
        # Exercise the Global post-pass against the same fully generated tree.
        with patch.object(generator, 'RULE_DIR', root), contextlib.redirect_stdout(io.StringIO()) as log:
            generator.prune_global_first_match_overlaps()
        result['global'] = (root / 'Global.list').read_text()
        result['global_log'] = log.getvalue()
        # Empty input and Unicode separators preserve the former file round-trip.
        (root / 'Manual/Edge.txt').write_text('DOMAIN,one.test\u2028DOMAIN,two.test\n')
        result['edge_cases'] = {}
        for name in ('Empty.list', 'Edge.list'):
            with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root / 'Manual'), patch.object(generator, 'datetime', FixedTime), patch.object(generator, 'REPO_URL', 'https://github.com/linnux-x/surge'), patch.object(generator, 'AUTHOR_NAME', 'linnux-x'), contextlib.redirect_stdout(io.StringIO()):
                generator.process_rule(name, name, [])
            result['edge_cases'][name] = (root / name).read_text()
    print(json.dumps({'elapsed_seconds': time.perf_counter() - started, 'result': result}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default=BASE, help='trusted Git revision to compare')
    parser.add_argument('--worker', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        worker(args.worker)
        return
    with tempfile.TemporaryDirectory() as directory:
        old_scripts = Path(directory) / 'scripts'
        old_scripts.mkdir()
        paths = subprocess.check_output(
            ['git', 'ls-tree', '-r', '--name-only', args.base, '--', 'scripts'], cwd=ROOT, text=True,
        ).splitlines()
        for name in paths:
            if name.endswith('.py'):
                (old_scripts / Path(name).name).write_bytes(subprocess.check_output(
                    ['git', 'show', f'{args.base}:{name}'], cwd=ROOT,
                ))
        observations = [json.loads(subprocess.check_output(
            [sys.executable, '-B', str(Path(__file__).resolve()), '--worker', str(scripts)],
            cwd=ROOT, text=True,
        )) for scripts in (old_scripts, ROOT / 'scripts')]
    before, after = observations
    if before['result'] != after['result']:
        raise SystemExit('FAIL: old/new generated content, diagnostics or source specifications differ')
    digest = hashlib.sha256(json.dumps(after['result'], sort_keys=True).encode()).hexdigest()
    print(json.dumps({
        'base': args.base, 'rulesets': len(after['result']['files']),
        'identical': True, 'result_sha256': digest,
        'baseline_seconds': round(before['elapsed_seconds'], 3),
        'current_seconds': round(after['elapsed_seconds'], 3),
        'timing_scope': 'one local offline replay, excludes network and publishing',
    }, indent=2))


if __name__ == '__main__':
    main()
