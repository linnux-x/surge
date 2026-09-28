"""Failure receipts survive an inaccessible workspace; readiness is not success."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import automation_preflight as task


class PreflightTests(unittest.TestCase):
    def test_denial_records_failure_without_overwriting_inaccessible_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = task.Config(root / 'repo', root / 'state', root / 'fallback.json')
            config.state_dir.mkdir()
            receipt = config.state_dir / 'last-run.json'
            receipt.write_text('{"status":"ok"}')
            real_write = task.atomic_json
            def write(path, data):
                if path == receipt:
                    raise PermissionError(1, 'injected desktop denial')
                real_write(path, data)
            with patch.object(task, 'verify', side_effect=PermissionError(1, 'injected desktop denial')), patch.object(task, 'atomic_json', side_effect=write), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(task.run(config), 2)
            record = json.loads(config.fallback_receipt.read_text())
            self.assertEqual(record['status'], 'failed')
            self.assertFalse(record['primary_receipt_written'])
            self.assertEqual(receipt.read_text(), '{"status":"ok"}')
            self.assertTrue(output.getvalue().startswith('[CRON_FAILURE]\n'))
            self.assertEqual(config.fallback_receipt.stat().st_mode & 0o777, 0o600)

    def test_real_git_and_atomic_access_ready_then_dirty_and_scheduler_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / 'repo'; repo.mkdir()
            state = root / 'state'; state.mkdir()
            scheduler = root / 'automation.toml'
            scheduler.write_text('status = "PAUSED"\n')
            config = task.Config(repo, state, root / 'fallback.json', scheduler)
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            for name in ('SOURCE_OF_TRUTH.md', 'CONTRIBUTING.md', 'scripts/README.md'):
                path = repo / name; path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('fixture\n')
            def git(*args):
                return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()
            git('remote', 'add', 'origin', config.expected_origin)
            git('add', '.')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.test', 'commit', '-qm', 'base')
            receipt = state / 'last-run.json'; receipt.write_text('{"status":"failed"}')
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(task.run(config), 0)
                self.assertEqual(receipt.read_text(), '{"status":"failed"}')
                ready = json.loads(config.fallback_receipt.read_text())
                self.assertEqual((ready['status'], ready['head_sha']), ('ready', git('rev-parse', 'HEAD')))
                self.assertEqual(list(state.glob('.preflight-*')), [])
                (repo / 'CONTRIBUTING.md').write_text('dirty\n')
                self.assertEqual(task.run(config), 2)
                self.assertIn('WORKTREE_DIRTY', json.loads(receipt.read_text())['summary'])
                scheduler.write_text('status = "ACTIVE"\n')
                self.assertEqual(task.run(config), 2)
                self.assertIn('DUPLICATE_SCHEDULER', json.loads(receipt.read_text())['summary'])
