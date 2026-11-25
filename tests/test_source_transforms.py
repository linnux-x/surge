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
from rule_validator import validate_rule_file
from source_transforms import apply_project_guardrails, clean_source, convert_source, filter_candidates
from test_routing_order import match_domain

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/generation-baseline.json').read_text())


class FixedTime:
    @staticmethod
    def now(tz):
        return datetime(2026, 9, 8, tzinfo=tz)


class SourceTransformTests(unittest.TestCase):
    def test_chatgpt_voice_matches_only_listed_prefixes_on_udp_3478(self):
        lines = [json.dumps({"prefixes": [
            {"ipv6Prefix": "2606:4700:4700::1111/128"},
            {"ipv4Prefix": "1.2.3.4/32"},
            {"ipv4Prefix": "1.2.3.4/32"},
        ]})]
        rules = convert_source(lines, "chatgpt-voice-json")
        self.assertEqual(len(rules), 2)
        self.assertEqual(validate_rule_file(rules, "AI.list"), [])
        self.assertTrue(validate_rule_file(rules, "Download.list"))
        for address in ("1.2.3.4", "2606:4700:4700::1111"):
            with self.subTest(address=address):
                self.assertTrue(match_domain(address, set(rules), port=3478, protocol="UDP"))
                self.assertFalse(match_domain(address, set(rules), port=3478))
                self.assertFalse(match_domain(address, set(rules), port=443, protocol="UDP"))
        self.assertFalse(match_domain("1.2.3.5", set(rules), port=3478, protocol="UDP"))

    def test_chatgpt_voice_rejects_malformed_or_local_prefixes(self):
        for prefixes in ([], [{}], [{"ipv4Prefix": "192.168.0.0/24"}],
                         [{"ipv6Prefix": "1.2.3.4/32"}], [{"ipv4Prefix": 1}]):
            with self.subTest(prefixes=prefixes), self.assertRaises(ValueError):
                convert_source([json.dumps({"prefixes": prefixes})], "chatgpt-voice-json")

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
            'DOMAIN,alkalimakersuite-pa.clients6.google.com',
        ]
        self.assertEqual(filter_candidates(candidates + ai_specific, exclude), ai_specific)

    def test_grammarly_upstream_cannot_capture_existing_cdn_route(self):
        exclude = Path(__file__).resolve().parents[1] / 'Rule/Manual/AI.exclude.txt'
        # 上游曾用整个根后缀抢占 CDN；同时覆盖精确类型和选项变体。
        upstream = [f'{kind},{host}{option}'
                    for host in ('grammarly.com', 'static.grammarly.com')
                    for kind in ('DOMAIN', 'DOMAIN-SUFFIX')
                    for option in ('', ',extended-matching')]
        retained = ['DOMAIN,api.openai.com', 'DOMAIN-SUFFIX,notgrammarly.com']
        self.assertEqual(filter_candidates(upstream + retained, exclude), retained)

    def test_ai_keeps_cross_product_bytedapm_in_global(self):
        exclude = Path(__file__).resolve().parents[1] / 'Rule/Manual/AI.exclude.txt'
        candidates = [f'{kind},sf16-short-sg.bytedapm.com{option}'
                      for kind in ('DOMAIN', 'DOMAIN-SUFFIX')
                      for option in ('', ',extended-matching')]
        retained = ['DOMAIN-SUFFIX,byteoversea.net', 'DOMAIN,api.openai.com']
        self.assertEqual(filter_candidates(candidates + retained, exclude), retained)

    def test_ai_excludes_shared_meta_rules_and_keeps_muse(self):
        exclude = Path(__file__).resolve().parents[1] / 'Rule/Manual/AI.exclude.txt'
        upstream = [
            'DOMAIN,graph.facebook.com',
            'DOMAIN-WILDCARD,scontent-*.xx.fbcdn.net,extended-matching',
            'DOMAIN-SUFFIX,muse.ai',
        ]
        self.assertEqual(filter_candidates(upstream, exclude), ['DOMAIN-SUFFIX,muse.ai'])

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

    def test_guardrails_strip_shared_parent_suffixes_from_service_rulesets(self):
        lines = [
            'DOMAIN,anthropic.auth0.com',
            'DOMAIN-SUFFIX,auth0.com',
            'DOMAIN-SUFFIX,segment.io',
            'DOMAIN-SUFFIX,sentry.io',
        ]
        self.assertEqual(
            apply_project_guardrails('AI.list', lines),
            ['DOMAIN,anthropic.auth0.com'],
        )
        self.assertEqual(apply_project_guardrails('Global.list', lines), lines)

    def test_media_matchers_cannot_return_through_global_fallback(self):
        unscoped = ['user-agent,Argo*', 'DOMAIN-KEYWORD,ttvnw']
        scoped = ['DOMAIN-SUFFIX,ttvnw.net', 'PROCESS-NAME,tv.twitch.android.app']
        for target in ('GlobalMedia.list', 'Global.list', 'ChinaMedia.list', 'Netflix.list'):
            with self.subTest(target=target):
                self.assertEqual(apply_project_guardrails(target, unscoped + scoped), scoped)
                self.assertEqual(len(validate_rule_file(unscoped, target)), len(unscoped))

    def test_china_requires_a_destination_for_direct_routing(self):
        unscoped = ['USER-AGENT,TeslaMap', 'USER-AGENT,%E4%BC%98%E9%85%B7*', 'DOMAIN-KEYWORD,223789']
        scoped = ['DOMAIN-SUFFIX,223789.xyz', 'DOMAIN-SUFFIX,taobao.com']
        self.assertEqual(apply_project_guardrails('China.list', unscoped + scoped), scoped)
        self.assertEqual(len(validate_rule_file(unscoped, 'China.list')), len(unscoped))

    def test_media_allows_video_children_of_general_portals(self):
        broad = ['DOMAIN-SUFFIX,naver.com', 'DOMAIN-SUFFIX,kakao.com', 'DOMAIN,daum.net']
        video = ['DOMAIN-SUFFIX,tv.naver.com', 'DOMAIN-SUFFIX,tv.kakao.com']
        self.assertEqual(apply_project_guardrails('GlobalMedia.list', broad + video), video)
        self.assertEqual(len(validate_rule_file(broad, 'GlobalMedia.list')), len(broad))

    def test_ai_rejects_shared_provider_hosts_and_unreviewed_ip_rules(self):
        shared = [
            'DOMAIN,api.cloudflare.com', 'DOMAIN-SUFFIX,storage.googleapis.com',
            'DOMAIN,in.appcenter.ms', 'DOMAIN,developer.meta.com',
            'DOMAIN-SUFFIX,lf3-static.bytednsdoc.com', 'IP-ASN,14061',
            'IP-CIDR,160.79.104.0/21,no-resolve', 'IP-CIDR6,2604:f20::/32,no-resolve',
            'DOMAIN-SUFFIX,awsapps.com', 'DOMAIN-SUFFIX,sso.amazonaws.com',
            'DOMAIN,cognito-identity.us-east-1.amazonaws.com', 'DOMAIN,oidc.eu-west-1.api.aws',
        ]
        reviewed = [
            'DOMAIN-SUFFIX,muse.ai', 'DOMAIN,ai.meta.com',
            'DOMAIN,gateway.ai.cloudflare.com', 'IP-ASN,399358,no-resolve',
            'AND,((PROTOCOL,UDP),(DEST-PORT,3478),(IP-CIDR,1.2.3.4/32,no-resolve))',
        ]
        self.assertEqual(apply_project_guardrails('AI.list', shared + reviewed), reviewed)
        self.assertTrue(all(validate_rule_file([rule], 'AI.list') for rule in shared))
        self.assertEqual(validate_rule_file(reviewed, 'AI.list'), [])

    def test_netflix_does_not_inherit_shared_ip_ranges(self):
        unverified = ['IP-CIDR,108.128.160.0/23,no-resolve', 'IP-ASN,16509,no-resolve']
        verified = ['IP-ASN,2906,no-resolve', 'IP-ASN,40027,no-resolve']
        self.assertEqual(apply_project_guardrails('Netflix.list', unverified + verified), verified)
        self.assertEqual(validate_rule_file(verified, 'Netflix.list'), [])
        self.assertEqual(len(validate_rule_file(unverified, 'Netflix.list')), len(unverified))

    def test_china_guardrail_filters_known_overseas_media_and_shared_cdn(self):
        lines = [
            'DOMAIN-SUFFIX,snssdk.com',
            'DOMAIN-SUFFIX,kwaicdn.com',
            'DOMAIN,rthklive2-lh.akamaihd.net',
            'DOMAIN-SUFFIX,akadns.net',
            'DOMAIN-SUFFIX,stat-nba.com',
            'DOMAIN-SUFFIX,tobsnssdk.com',
        ]
        self.assertEqual(
            apply_project_guardrails('China.list', lines),
            ['DOMAIN-SUFFIX,snssdk.com', 'DOMAIN-SUFFIX,stat-nba.com', 'DOMAIN-SUFFIX,tobsnssdk.com'],
        )
        # snssdk.com is Douyin's domestic API (2026-11-08 history review), so it stays in China.

    def test_process_rule_filters_shared_suffixes_before_strict_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manual = root / 'Manual'
            manual.mkdir()
            upstream = [
                'DOMAIN,anthropic.auth0.com',
                'DOMAIN-SUFFIX,auth0.com',
                'DOMAIN-SUFFIX,segment.io',
                'DOMAIN-SUFFIX,sentry.io',
            ]
            with (
                patch.object(generator, 'RULE_DIR', root),
                patch.object(generator, 'MANUAL_DIR', manual),
                patch.object(generator, 'fetch_source', return_value=upstream),
                patch.object(generator, 'datetime', FixedTime),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                generator.process_rule('AI.list', 'AI', [('Fixture', 'https://example.test/rules', None)])
            rules = (root / 'AI.list').read_text().splitlines()
            self.assertIn('DOMAIN,anthropic.auth0.com', rules)
            self.assertNotIn('DOMAIN-SUFFIX,auth0.com', rules)
            self.assertNotIn('DOMAIN-SUFFIX,segment.io', rules)
            self.assertNotIn('DOMAIN-SUFFIX,sentry.io', rules)

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
