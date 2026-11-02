"""Pinned upstream snapshots let a Manual edit be rebuilt offline without upstream drift."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import generate_rules as generator
import source_cache

SPECS = {'AI.list': ('AI', [('AI', 'https://example.test/ai', None)])}


class SourceCacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = tempfile.TemporaryDirectory()
        self.env = patch.dict(os.environ, {'SURGE_SOURCE_CACHE': self.cache.name})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.cache.cleanup()

    def test_round_trip_and_missing_snapshot(self):
        raw = ['# header', 'DOMAIN,a.example', '']
        source_cache.put('https://example.test/a', raw, 'converted-1')
        self.assertEqual(source_cache.get('https://example.test/a', 'converted-1'), raw)
        with self.assertRaises(source_cache.SnapshotMissing):
            source_cache.get('https://example.test/a', 'converted-2')

    def test_old_snapshots_are_pruned_per_url(self):
        for i in range(source_cache.KEEP_PER_URL + 2):
            source_cache.put('https://example.test/a', [f'DOMAIN,{i}.example'], f'c{i}')
        blobs = list((Path(self.cache.name) / 'blobs').iterdir())
        self.assertEqual(len(blobs), source_cache.KEEP_PER_URL)
        with self.assertRaises(source_cache.SnapshotMissing):
            source_cache.get('https://example.test/a', 'c0')
        self.assertEqual(source_cache.get('https://example.test/a', 'c11'), ['DOMAIN,11.example'])


class OfflineGenerationTests(unittest.TestCase):
    def setUp(self):
        self.cache = tempfile.TemporaryDirectory()
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        (self.root / 'Manual').mkdir()
        self.env = patch.dict(os.environ, {'SURGE_SOURCE_CACHE': self.cache.name,
                                           'CHANGED_RULESETS': '[]', 'GITHUB_EVENT_NAME': ''})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.cache.cleanup()
        self.dir.cleanup()

    def run_main(self, argv, upstream=None):
        fetch = (patch.object(generator, 'fetch_remote_source', return_value=tuple(upstream))
                 if upstream is not None else
                 patch.object(generator, 'fetch_remote_source', side_effect=AssertionError('network used')))
        with patch.object(generator, 'RULE_DIR', self.root), patch.object(generator, 'MANUAL_DIR', self.root / 'Manual'), \
                patch.object(generator, 'RULE_SPECS', SPECS), fetch:
            return generator.main(argv)

    def body(self):
        return [l for l in (self.root / 'AI.list').read_text().splitlines() if l and not l.startswith('#')]

    def test_removed_exclusion_is_restored_offline(self):
        exclude = self.root / 'Manual' / 'AI.exclude.txt'
        exclude.write_text('DOMAIN,b.example\n')
        self.run_main(['--rulesets', 'AI.list'], ['# upstream 2026-11-01', 'DOMAIN,a.example', 'DOMAIN,b.example'])
        self.assertEqual(self.body(), ['DOMAIN,a.example'])
        record = json.loads((self.root / '.sources' / 'AI.json').read_text())
        self.assertEqual([s['label'] for s in record['sources']], ['AI'])
        exclude.unlink()
        self.assertEqual(self.run_main(['--offline', '--rulesets', 'AI.list']), 0)
        self.assertEqual(self.body(), ['DOMAIN,a.example', 'DOMAIN,b.example'])

    def test_offline_without_record_fails_and_keeps_files(self):
        (self.root / 'AI.list').write_text('DOMAIN,old.example\n')
        with self.assertRaises(source_cache.SnapshotMissing):
            self.run_main(['--offline', '--rulesets', 'AI.list'])
        self.assertEqual((self.root / 'AI.list').read_text(), 'DOMAIN,old.example\n')
        self.assertFalse((self.root / '.sources').exists())

    def test_unchanged_output_backfills_but_never_moves_pin(self):
        upstream = ['DOMAIN,a.example']
        self.run_main(['--rulesets', 'AI.list'], upstream)
        record = self.root / '.sources' / 'AI.json'
        published, pinned = (self.root / 'AI.list').read_bytes(), record.read_bytes()
        record.unlink()
        self.assertEqual(self.run_main(['--check', '--rulesets', 'AI.list'], upstream), 0)
        self.assertFalse(record.exists())
        self.run_main(['--rulesets', 'AI.list'], upstream)
        self.assertEqual(record.read_bytes(), pinned)
        (self.root / 'Manual' / 'AI.exclude.txt').write_text('DOMAIN,z.example\n')
        self.run_main(['--rulesets', 'AI.list'], upstream + ['DOMAIN,z.example'])
        self.assertEqual((self.root / 'AI.list').read_bytes(), published)
        self.assertEqual(record.read_bytes(), pinned)

    def test_unknown_ruleset_argument_is_rejected(self):
        with self.assertRaises(ValueError):
            self.run_main(['--rulesets', 'Missing.list'])


class SnapshotRecordValidationTests(unittest.TestCase):
    def check(self, files):
        import validate_surge_repo as repo
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'Rule' / '.sources').mkdir(parents=True)
            (root / 'Rule' / 'AI.list').write_text('DOMAIN,a.example\n')
            for name, data in files.items():
                (root / 'Rule' / '.sources' / name).write_text(json.dumps(data))
            errors = []
            with patch.object(repo, 'ROOT', root), patch.object(repo, 'RULE_DIR', root / 'Rule'), \
                    patch.dict('sources.RULE_SPECS', SPECS, clear=True):
                repo.check_source_snapshots(errors)
            return errors

    def record(self, **changes):
        source = {'label': 'AI', 'url': 'https://example.test/ai', 'format': None, 'sha256': 'a' * 64}
        source.update(changes)
        return {'ruleset': 'AI.list', 'sources': [source]}

    def test_matching_record_passes(self):
        self.assertEqual(self.check({'AI.json': self.record()}), [])

    def test_stale_or_orphaned_records_fail(self):
        self.assertTrue(self.check({'AI.json': self.record(url='https://example.test/old')}))
        self.assertTrue(self.check({'AI.json': self.record(sha256='xyz')}))
        self.assertTrue(self.check({'Gone.json': {'ruleset': 'Gone.list', 'sources': []}}))
        self.assertTrue(self.check({'AI.json': {'sources': 'broken'}}))


if __name__ == '__main__':
    unittest.main()
