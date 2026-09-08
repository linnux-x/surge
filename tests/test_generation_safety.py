"""Failure cases must preserve rule semantics and the last valid file."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import generate_rules as generator


class GenerationSafetyTests(unittest.TestCase):
    def test_cidr_with_different_options_is_retained(self):
        for kind, parent, child in [('IP-CIDR', '203.0.113.0/24', '203.0.113.0/25'),
                                    ('IP-CIDR6', '2001:db8::/32', '2001:db8:1::/48')]:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as d:
                p = Path(d) / 'rules.list'
                original = f'{kind},{parent},no-resolve\n{kind},{child}\n'
                p.write_text(original)
                generator.prune_redundant_cidr(p)
                self.assertEqual(p.read_text(), original)

    def test_same_option_cidr_still_pruned(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'rules.list'
            p.write_text('IP-CIDR,203.0.113.0/24,no-resolve\nIP-CIDR,203.0.113.0/25,no-resolve\n')
            generator.prune_redundant_cidr(p)
            self.assertEqual(p.read_text(), 'IP-CIDR,203.0.113.0/24,no-resolve\n')

    def run_invalid_source(self, lines, exception):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            target = root / 'Test.list'
            original = '# known valid\nDOMAIN,previous.example\n'
            target.write_text(original)
            with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root / 'Manual'), patch.object(generator, 'fetch_source', return_value=lines):
                with self.assertRaises(exception):
                    generator.process_rule('Test.list', 'Test', [('Test upstream', 'https://example.test/rules', None)])
            self.assertEqual(target.read_text(), original)
            self.assertEqual(list(root.glob('*.tmp')), [])

    def test_empty_upstream_aborts_without_replacing_valid_output(self):
        self.run_invalid_source(['# empty upstream'], ValueError)

    def test_invalid_rules_do_not_overwrite_valid_output(self):
        self.run_invalid_source(['NOT-A-RULE,example.test'], SystemExit)

    def test_validator_preserves_option_distinction(self):
        from rule_validator import validate_rule_file
        rules = ['IP-CIDR,203.0.113.0/24,no-resolve', 'IP-CIDR,203.0.113.0/25']
        self.assertFalse(any('redundant CIDR' in e for e in validate_rule_file(rules, 'Test.list')))
        self.assertTrue(any('redundant CIDR' in e for e in validate_rule_file([rules[0], rules[1]+',no-resolve'], 'Test.list')))

    def test_invalid_incremental_input_fails_before_generation(self):
        import os
        for value in ('[', 'null', '{}', '"AI.list"', '["missing.list"]', '[1]'):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as d:
                root = Path(d)
                with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root/'Manual'), patch.object(generator, 'process_rule') as process, patch.dict(os.environ, {'CHANGED_RULESETS': value}):
                    with self.assertRaises(ValueError):
                        generator.main()
                    process.assert_not_called()

    def test_global_validation_failure_preserves_file(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            p = root/'Global.list'
            content = '# TOTAL: 2\nDOMAIN,shared.example\nNOT-A-RULE,broken\n'
            p.write_text(content)
            (root/'AI.list').write_text('DOMAIN,shared.example\n')
            with patch.object(generator, 'RULE_DIR', root), self.assertRaises(SystemExit):
                generator.prune_global_first_match_overlaps()
            self.assertEqual(p.read_text(), content)
