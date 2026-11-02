"""Generation targets an explicit directory and reports validation failures as results."""
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import generate_rules as generator

SPECS = {'AI.list': ('AI', [('AI', 'https://example.test/ai', None)])}


class GeneratorContextTests(unittest.TestCase):
    def test_process_rule_writes_only_to_the_given_directory(self):
        with tempfile.TemporaryDirectory() as default, tempfile.TemporaryDirectory() as target:
            with patch.object(generator, 'RULE_DIR', Path(default)), \
                    patch.object(generator, 'MANUAL_DIR', Path(default) / 'Manual'), \
                    patch.object(generator, 'fetch_source', return_value=['DOMAIN,a.example']), redirect_stdout(io.StringIO()):
                generator.process_rule('AI.list', 'AI', SPECS['AI.list'][1], rule_dir=Path(target))
            self.assertEqual(os.listdir(default), [])
            self.assertTrue((Path(target) / 'AI.list').is_file())
            self.assertTrue((Path(target) / '.sources' / 'AI.json').is_file())

    def test_validation_failure_returns_1_and_publishes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'AI.list').write_text('DOMAIN,old.example\n')
            out = io.StringIO()
            with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root / 'Manual'), \
                    patch.object(generator, 'RULE_SPECS', SPECS), \
                    patch.object(generator, 'fetch_source', return_value=['NOT-A-RULE,x.example']), redirect_stdout(out):
                self.assertEqual(generator.main(['--rulesets', 'AI.list']), 1)
            self.assertIn('VALIDATION FAILED for AI.list', out.getvalue())
            self.assertEqual((root / 'AI.list').read_text(), 'DOMAIN,old.example\n')
            self.assertFalse((root / '.sources').exists())


if __name__ == '__main__':
    unittest.main()
