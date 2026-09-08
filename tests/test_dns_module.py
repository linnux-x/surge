import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_dns_module import validate_text, RULESET_PREFIX, ROOT


class DNSModuleTests(unittest.TestCase):
    def test_current_module_passes(self):
        validate_text((ROOT / 'Module/DNS-Mapping.sgmodule').read_text())

    def test_indented_section_injection_is_rejected(self):
        base = '[Host]\nRULE-SET:' + RULESET_PREFIX + 'alibaba.conf = server:system\n'
        for section in ('[Script]', '[MITM]', '[URL Rewrite]', '[Host]'):
            with self.subTest(section=section), self.assertRaises(ValueError):
                validate_text(base + '  ' + section + '\nx = y\n')

    def test_allowed_reference_cannot_hide_unapproved_reference(self):
        base = '[Host]\nRULE-SET:' + RULESET_PREFIX + 'alibaba.conf = server:system\n'
        for url in ('https://example.test/rules.conf', RULESET_PREFIX + '../other.conf', RULESET_PREFIX + 'ok.conf?alternate=1'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_text(base + 'RULE-SET:' + url + ' = server:system\n')

    def test_missing_or_malformed_host_section(self):
        for text in ('', '[Host]\n', 'x = y\n[Host]\n', '[Host]\nx =\n'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                validate_text(text)
