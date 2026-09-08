"""Characterization fixtures captured from d84c77e before extracting transforms."""
import contextlib
from datetime import datetime
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import generate_rules as generator
import audit_upstream_sources as audit
from source_transforms import apply_project_guardrails, clean_source, convert_source

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/generation-baseline.json').read_text())


class FixedTime:
    @staticmethod
    def now(tz):
        return datetime(2026, 9, 8, tzinfo=tz)


class SourceTransformTests(unittest.TestCase):
    def test_all_target_guardrails_match_pre_refactor_results(self):
        for target, expected in FIXTURE['guardrails'].items():
            with self.subTest(target=target):
                self.assertEqual(apply_project_guardrails(target, clean_source(FIXTURE['guardrail_input'])), expected)

    def test_six_formats_generate_identical_file_bytes(self):
        for case in FIXTURE['generation']:
            with self.subTest(fmt=case['format']), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manual = root / 'Manual'
                manual.mkdir()
                (manual / 'Test.txt').write_text('DOMAIN,manual.example\n')
                (manual / 'Test.exclude.txt').write_text('DOMAIN,excluded.example\n')
                with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', manual), patch.object(generator, 'fetch_source', return_value=case['input']), patch.object(generator, 'datetime', FixedTime), patch.object(generator, 'REPO_URL', 'https://github.com/linnux-x/surge'), patch.object(generator, 'AUTHOR_NAME', 'linnux-x'), contextlib.redirect_stdout(io.StringIO()):
                    generator.process_rule('Test.list', 'Test', [('Fixture', 'https://example.test/rules', case['format'])])
                self.assertEqual((root / 'Test.list').read_bytes(), case['output'].encode())

    def test_conversion_does_not_mutate_shared_response(self):
        for case in FIXTURE['generation']:
            original = case['input'][:]
            convert_source(case['input'], case['format'])
            self.assertEqual(case['input'], original)

    def test_audit_manual_bypasses_exclusions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manual = root / 'Rule/Manual'
            manual.mkdir(parents=True)
            (manual / 'Test.exclude.txt').write_text('DOMAIN,excluded.example\n')
            with patch.object(audit, 'ROOT', root):
                self.assertEqual(audit.normalize('Test.list', None, 'DOMAIN,excluded.example'), set())
                self.assertEqual(audit.normalize('Test.list', None, 'DOMAIN,excluded.example', manual=True), {'domain,excluded.example'})

    def test_empty_text_remains_valid_audit_input(self):
        self.assertEqual(convert_source(['# empty'], None), [])
        self.assertEqual(audit.normalize('Test.list', None, '# empty'), set())
