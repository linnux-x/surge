"""Exclusion format and independent post-generation coverage regression tests."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import audit_rules
import validate_override_manifest as overrides
from source_transforms import filter_candidates
from exclusions import read_exclusions


class ExclusionTests(unittest.TestCase):
    def test_domain_options_case_and_type_boundaries(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'AI.exclude.txt'
            p.write_text('DOMAIN-SUFFIX,byteoversea.com\nIP-ASN,13335,no-resolve\n')
            retained = ['DOMAIN,byteoversea.com', 'DOMAIN-SUFFIX,child.byteoversea.com',
                        'DOMAIN-SUFFIX,notbyteoversea.com', 'IP-ASN,13335']
            excluded = ['DOMAIN-SUFFIX,byteoversea.com',
                        'DOMAIN-SUFFIX,ByteOversea.com,extended-matching',
                        'IP-ASN,13335,no-resolve']
            self.assertEqual(filter_candidates(excluded + retained, p), retained)

    def test_bare_or_invalid_entries_fail_before_filtering(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'Test.exclude.txt'
            for line in ['amazonaws.com', 'DOMAIN-SUFFIX,', 'BOGUS,example.com',
                         'DOMAIN,example.com,invalid-option']:
                with self.subTest(line=line):
                    p.write_text(line+'\n')
                    with self.assertRaises(ValueError):
                        filter_candidates(['DOMAIN,example.com'], p)

    def test_audit_detects_domain_variant_and_respects_manual_override(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); manual = root/'Manual'; manual.mkdir()
            (manual/'AI.exclude.txt').write_text('DOMAIN-SUFFIX,byteoversea.com\nDOMAIN,owned.example\n')
            (manual/'AI.txt').write_text('DOMAIN,owned.example\n')
            (root/'AI.list').write_text('DOMAIN-SUFFIX,byteoversea.com,extended-matching\nDOMAIN,owned.example\n')
            with patch.object(audit_rules, 'RULE_DIR', root), patch.object(audit_rules, 'MANUAL_DIR', manual):
                findings = audit_rules.check_exclude_coverage()
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0]['severity'], 'ERROR')
            self.assertIn('byteoversea.com', findings[0]['detail'])

    def test_ci_override_validator_rejects_bare_entry(self):
        import json
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); p = root/'Test.exclude.txt'; p.write_text('amazonaws.com\n')
            manifest = root/'override-manifest.json'
            manifest.write_text(json.dumps({'schema_version': 1, 'files': {
                p.name: {'action': 'exclude', 'reason': 'fixture', 'destination': 'Global'}}, 'entries': []}))
            with patch.object(overrides, 'MANUAL', root), patch.object(overrides, 'MANIFEST', manifest), patch.object(overrides, 'routing_test_domains', return_value=set()), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(overrides.main(), 1)
