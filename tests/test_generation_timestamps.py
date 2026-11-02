"""Unchanged rulesets keep their bytes; --check reports changes without publishing."""
import os
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import generate_rules as generator

SPECS = {'AI.list': ('AI', [('AI', 'https://example.test/ai', None)])}
HEADER = '# NAME: AI\n# AUTHOR: a\n# REPO: r\n# UPDATED: {}\n# FORMAT: Surge Ruleset\n# TOTAL: 1\n\n'


def clock(hour):
    class FixedClock(datetime):
        @classmethod
        def now(cls, tz=None):
            return datetime(2026, 11, 2, hour, 0, 0, tzinfo=ZoneInfo('Asia/Shanghai'))
    return FixedClock


class ContentChangedTests(unittest.TestCase):
    def test_timestamp_only_difference_is_not_a_change(self):
        old = HEADER.format('2026-11-01 05:00:00 +0800').encode() + b'DOMAIN,a.example\n'
        new = HEADER.format('2026-11-02 05:00:00 +0800').encode() + b'DOMAIN,a.example\n'
        self.assertFalse(generator.content_changed(old, new))

    def test_body_or_total_difference_is_a_change(self):
        old = HEADER.format('t1').encode() + b'DOMAIN,a.example\n'
        self.assertTrue(generator.content_changed(old, HEADER.format('t2').encode() + b'DOMAIN,b.example\n'))
        self.assertTrue(generator.content_changed(old, HEADER.format('t1').replace('TOTAL: 1', 'TOTAL: 2').encode()
                                                  + b'DOMAIN,a.example\n'))
        self.assertTrue(generator.content_changed(None, old))

    def test_updated_text_outside_header_is_content(self):
        old = HEADER.format('t').encode() + b'# UPDATED: manual note one\nDOMAIN,a.example\n'
        new = HEADER.format('t').encode() + b'# UPDATED: manual note two\nDOMAIN,a.example\n'
        self.assertTrue(generator.content_changed(old, new))


class GenerationTimestampTests(unittest.TestCase):
    def run_main(self, root, upstream, hour, argv=None):
        with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root / 'Manual'), \
                patch.object(generator, 'RULE_SPECS', SPECS), patch.object(generator, 'datetime', clock(hour)), \
                patch.object(generator, 'fetch_source', return_value=upstream), \
                patch.dict(os.environ, {'CHANGED_RULESETS': '["AI.list"]', 'GITHUB_EVENT_NAME': ''}):
            return generator.main(argv)

    def test_regeneration_without_content_change_keeps_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.assertEqual(self.run_main(root, ['DOMAIN,a.example'], 5), 0)
            first = (root / 'AI.list').read_bytes()
            self.assertIn(b'# UPDATED: 2026-11-02 05:00:00 +0800', first)
            self.assertEqual(self.run_main(root, ['DOMAIN,a.example'], 6), 0)
            self.assertEqual((root / 'AI.list').read_bytes(), first)
            self.run_main(root, ['DOMAIN,b.example'], 7)
            self.assertIn(b'# UPDATED: 2026-11-02 07:00:00 +0800', (root / 'AI.list').read_bytes())

    def test_check_reports_changes_without_publishing(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.run_main(root, ['DOMAIN,a.example'], 5)
            published = (root / 'AI.list').read_bytes()
            self.assertEqual(self.run_main(root, ['DOMAIN,a.example'], 6, ['--check']), 0)
            self.assertEqual(self.run_main(root, ['DOMAIN,b.example'], 6, ['--check']), 1)
            self.assertEqual((root / 'AI.list').read_bytes(), published)
            self.assertEqual(sorted(p.name for p in root.iterdir() if p.name != 'Manual'), ['AI.list'])


if __name__ == '__main__':
    unittest.main()
