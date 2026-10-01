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
from source_transforms import apply_project_guardrails, clean_source, convert_source, filter_candidates

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/generation-baseline.json').read_text())


class FixedTime:
    @staticmethod
    def now(tz):
        return datetime(2026, 9, 8, tzinfo=tz)


class SourceTransformTests(unittest.TestCase):
    def test_ai_exclusions_use_complete_rules_for_both_upstream_formats(self):
        exclude = Path(__file__).resolve().parents[1] / 'Rule/Manual/AI.exclude.txt'
        shared_hosts = [
            'api.github.com', 'api.msn.com', 'assets.msn.com',
            'location.microsoft.com', 'odc.officeapps.live.com', 'r.bing.com',
            'self.events.data.microsoft.com', 'www.bing.com', 'api.microsoftapp.net',
            'static.cloudflareinsights.com', 'api.revenuecat.com',
            'challenges.cloudflare.com', 'clients6.google.com',
            'firebaseinstallations.googleapis.com',
        ]
        candidates = [f'{kind},{host}' for host in shared_hosts
                      for kind in ('DOMAIN', 'DOMAIN-SUFFIX')]
        ai_specific = [
            'DOMAIN,copilot.microsoft.com', 'DOMAIN,api.openai.com',
            'DOMAIN,gateway.ai.cloudflare.com',
            'DOMAIN-KEYWORD,alkalimakersuite-pa.clients6.google.com',
        ]
        self.assertEqual(filter_candidates(candidates + ai_specific, exclude), ai_specific)

    def test_ai_shared_network_exclusions_preserve_anthropic_asn(self):
        exclude = Path(__file__).resolve().parents[1] / 'Rule/Manual/AI.exclude.txt'
        upstream = [
            'IP-ASN,13335,no-resolve',
            'IP-ASN,20473,no-resolve',
            'IP-ASN,399358,no-resolve',
            'DOMAIN-SUFFIX,pool.ntp.org',
            'DOMAIN-SUFFIX,chat.openai.com',
        ]
        self.assertEqual(
            filter_candidates(upstream, exclude),
            ['IP-ASN,399358,no-resolve', 'DOMAIN-SUFFIX,chat.openai.com'],
        )

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
