"""Regression coverage for policy routing, upstream freshness and reviewed releases."""
import base64
import copy
import sys
import unittest
import tempfile
import subprocess
import os
from unittest.mock import patch
from zipfile import ZipFile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_upstream_updates import has_changed
import reviewed_release as release
from reviewed_release import digest, validate
from test_routing_order import match_domain, matches_expected, simulate_routing


class RoutingTests(unittest.TestCase):
    def test_wrong_policy_fails_even_when_ruleset_matches(self):
        actual = simulate_routing('api.openai.com', [('AI.list', 'DIRECT')],
                                  {'AI.list': {'domain-suffix,openai.com'}})
        self.assertFalse(matches_expected(actual, 'AI.list', 'AI'))
        self.assertTrue(matches_expected('AI.list→AI', 'AI.list', 'AI'))
        self.assertFalse(matches_expected('AI.list→AI', 'AI.list', ''))

    def test_literal_cidr_addresses(self):
        rules = {'ip-cidr,1.2.3.0/24,no-resolve', 'ip-cidr6,2001:db8::/32,no-resolve'}
        for address in ('1.2.3.4', '2001:db8::1'):
            self.assertTrue(match_domain(address, rules))
        for address in ('1.2.4.1', '2001:db9::1', 'example.com'):
            self.assertFalse(match_domain(address, rules))

    def test_root_dot_and_case(self):
        self.assertTrue(match_domain('API.OpenAI.com.', {'domain-suffix,openai.com'}))
        self.assertFalse(match_domain('notopenai.com', {'domain-suffix,openai.com'}))


class UpstreamTests(unittest.TestCase):
    def test_length_is_not_a_version(self):
        info = {'source_available': True, 'content_length': '1'}
        self.assertTrue(has_changed(info, info))

    def test_etag_and_outage_behavior_preserved(self):
        cached = {'source_available': True, 'etag': 'a'}
        self.assertFalse(has_changed(cached, cached))
        self.assertTrue(has_changed(dict(cached, etag='b'), cached))
        self.assertFalse(has_changed({'source_available': False}, cached))


class ReleaseTests(unittest.TestCase):
    def bundle(self):
        payload = {'schema': 1, 'base_sha': 'base', 'repository': 'owner/repo',
                   'run_id': '123', 'files': {
                       'Module/DNS-Mapping.sgmodule': base64.b64encode(b'[Host]\nx = 1.2.3.4\n').decode(),
                       'Rule/old.list': None}}
        return {'payload': payload, 'sha256': digest(payload)}

    def test_module_bytes_and_deletions_are_preserved(self):
        files = validate(self.bundle(), 'base', 'owner/repo', '123')
        self.assertEqual(files['Module/DNS-Mapping.sgmodule'], b'[Host]\nx = 1.2.3.4\n')
        self.assertIsNone(files['Rule/old.list'])

    def test_tampered_module_rejected(self):
        bundle = self.bundle()
        bundle['payload']['files']['Module/DNS-Mapping.sgmodule'] = 'Yg=='
        with self.assertRaises(ValueError):
            validate(bundle, 'base', 'owner/repo', '123')

    def test_other_base_or_run_rejected(self):
        for base, repo, run in [('other', 'owner/repo', '123'), ('base', 'other/repo', '123'), ('base', 'owner/repo', '456')]:
            with self.assertRaises(ValueError):
                validate(self.bundle(), base, repo, run)

    def test_paths_cannot_escape_publish_scope(self):
        for name in ('../outside', 'Rule/../../outside', '/tmp/outside', '.github/workflows/ci.yml'):
            bundle = copy.deepcopy(self.bundle())
            bundle['payload']['files'][name] = 'Yg=='
            bundle['sha256'] = digest(bundle['payload'])
            with self.assertRaises(ValueError):
                validate(bundle, 'base', 'owner/repo', '123')

    def test_capture_restore_roundtrip(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(['git', 'init', '-q', directory], check=True)
            (root / 'Module').mkdir()
            module = root / 'Module/DNS.sgmodule'
            module.write_bytes(b'[Host]\nexample.test = 1.2.3.4\n')
            subprocess.run(['git', '-C', directory, 'add', '.'], check=True)
            subprocess.run(['git', '-C', directory, '-c', 'user.name=Test',
                            '-c', 'user.email=test@example.test', 'commit', '-qm', 'base'], check=True)
            with patch.object(release, 'ROOT', root), patch.dict(os.environ, {
                    'GITHUB_REPOSITORY': 'owner/repo', 'GITHUB_RUN_ID': '123'}):
                bundle = root / 'reviewed-release.json'
                release.capture(bundle)
                module.write_bytes(b'changed after review')
                archive = root / 'release.zip'
                with ZipFile(archive, 'w') as zf:
                    zf.write(bundle, release.BUNDLE_NAME)
                release.restore(archive, '123')
                self.assertEqual(module.read_bytes(), b'[Host]\nexample.test = 1.2.3.4\n')
