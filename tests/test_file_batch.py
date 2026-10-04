"""Failure injection for batch replacement, deletion and rollback."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import file_batch


class FileBatchTests(unittest.TestCase):
    def test_success_preserves_modes_and_deletes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); a = root/'a'; b = root/'b'; c = root/'sub/c'
            a.write_bytes(b'old'); a.chmod(0o600); b.write_bytes(b'delete')
            file_batch.publish_files(root, {a: b'new', b: None, c: b'created'})
            self.assertEqual(a.read_bytes(), b'new')
            self.assertEqual(a.stat().st_mode & 0o777, 0o600)
            self.assertFalse(b.exists()); self.assertEqual(c.read_bytes(), b'created')
            self.assertFalse(list(root.glob('.publish-*')))

    def test_late_replace_failure_restores_old_new_and_deleted_files(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); a = root/'a'; b = root/'b'; c = root/'c'; last = root/'last'
            a.write_bytes(b'old'); b.write_bytes(b'deleted'); last.write_bytes(b'last-old')
            replace = os.replace
            def fail_once(src, dst):
                if dst == last and str(src).endswith('.new'):
                    raise OSError('injected publish failure')
                return replace(src, dst)
            with patch.object(file_batch.os, 'replace', side_effect=fail_once):
                with self.assertRaises(OSError):
                    file_batch.publish_files(root, {a: b'new', b: None, c: b'created', last: b'new'})
            self.assertEqual(a.read_bytes(), b'old'); self.assertEqual(b.read_bytes(), b'deleted')
            self.assertFalse(c.exists()); self.assertEqual(last.read_bytes(), b'last-old')
            self.assertFalse(list(root.glob('.publish-*')))

    def test_staging_failure_cannot_touch_destinations(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); a = root/'a'; a.write_bytes(b'old')
            with patch.object(file_batch.os, 'fsync', side_effect=OSError('disk full')):
                with self.assertRaises(OSError): file_batch.publish_files(root, {a: b'new'})
            self.assertEqual(a.read_bytes(), b'old')

    def test_rollback_failure_retains_recovery_material(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); a = root/'a'; b = root/'b'
            a.write_bytes(b'old-a'); b.write_bytes(b'old-b')
            replace = os.replace
            def fail(src, dst):
                if dst == b or str(src).endswith('.old'): raise OSError('disk error')
                return replace(src, dst)
            with patch.object(file_batch.os, 'replace', side_effect=fail):
                with self.assertRaisesRegex(RuntimeError, 'recovery retained'):
                    file_batch.publish_files(root, {a: b'new-a', b: b'new-b'})
            staging, = root.glob('.publish-*')
            self.assertEqual((staging/'0.old').read_bytes(), b'old-a')
            self.assertTrue((staging/'recovery.json').exists())
