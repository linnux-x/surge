#!/usr/bin/env python3
"""Surge daily job preflight; readiness is never reported as maintenance success."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from datetime import datetime

@dataclass(frozen=True)
class Config:
    workspace: Path
    state_dir: Path
    fallback_receipt: Path
    disabled_scheduler_config: Path | None = None
    contract_script: Path | None = None
    expected_origin: str = 'https://github.com/linnux-x/surge.git'


class PreflightError(ValueError):
    """A fixed public finding code, safe to include in receipts."""


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise ValueError('receipt must not be a symlink')
    fd, name = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def verify(config: Config) -> str:
    if config.disabled_scheduler_config and config.disabled_scheduler_config.exists():
        text = config.disabled_scheduler_config.read_text()
        if not re.search(r'^status\s*=\s*"PAUSED"\s*$', text, re.M):
            raise PreflightError('DUPLICATE_SCHEDULER')
    for name in ('SOURCE_OF_TRUTH.md', 'CONTRIBUTING.md', 'scripts/README.md'):
        (config.workspace / name).read_bytes()
    if config.contract_script:
        config.contract_script.read_bytes()
    def git(*args):
        return subprocess.check_output(
            ['git', '--no-optional-locks', '-C', str(config.workspace), *args],
            text=True, stderr=subprocess.PIPE, timeout=20,
        ).strip()
    if git('remote', 'get-url', 'origin') != config.expected_origin:
        raise PreflightError('UNEXPECTED_ORIGIN')
    if git('status', '--porcelain'):
        raise PreflightError('WORKTREE_DIRTY')
    head = git('rev-parse', 'HEAD')
    # Read the existing receipt too: creating a new file alone does not prove
    # access to pre-existing Desktop files under macOS privacy permissions.
    receipt = config.state_dir / 'last-run.json'
    if receipt.exists():
        receipt.read_bytes()
    with tempfile.TemporaryDirectory(prefix='.preflight-', dir=config.state_dir) as directory:
        probe = Path(directory) / 'receipt.json'
        atomic_json(probe, {'probe': 1})
        atomic_json(probe, {'probe': 2})
        if json.loads(probe.read_text()) != {'probe': 2}:
            raise PreflightError('ATOMIC_REPLACE_FAILED')
    return head


def run(config: Config) -> int:
    observed = datetime.now().astimezone().isoformat(timespec='seconds')
    try:
        head = verify(config)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        # Report only category/errno; subprocess stderr can include private data.
        detail = str(exc) if isinstance(exc, PreflightError) else type(exc).__name__
        if isinstance(exc, OSError):
            detail += f' errno={exc.errno}'
        record = {
            'schema': 'surge-codex-daily/v1', 'scheduler': 'hermes',
            'status': 'failed', 'checked_at': observed, 'base_sha': None,
            'head_sha': None, 'merge_sha': None, 'pr_url': None,
            'summary': f'前置检查失败（{detail}），未进入上游生成或发布。',
        }
        try:
            atomic_json(config.state_dir / 'last-run.json', record)
            primary_written = True
        except (OSError, ValueError):
            primary_written = False
        atomic_json(config.fallback_receipt, {**record, 'primary_receipt_written': primary_written})
        print('[CRON_FAILURE]')
        print(record['summary'])
        print(f'primary_receipt_written={primary_written}; fallback={config.fallback_receipt}')
        return 2
    record = {'schema': 'surge-daily-preflight/v1', 'scheduler': 'hermes',
              'status': 'ready', 'checked_at': observed, 'head_sha': head,
              'summary': '仅前置访问与原子替换检查通过；本轮维护尚未完成。'}
    atomic_json(config.fallback_receipt, record)
    print(json.dumps(record, ensure_ascii=False))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--state-dir', required=True, type=Path)
    parser.add_argument('--fallback-receipt', required=True, type=Path)
    parser.add_argument('--disabled-scheduler-config', type=Path)
    parser.add_argument('--contract-script', type=Path)
    parser.add_argument('--expected-origin', default='https://github.com/linnux-x/surge.git')
    args = parser.parse_args()
    return run(Config(**vars(args)))


if __name__ == '__main__':
    raise SystemExit(main())
