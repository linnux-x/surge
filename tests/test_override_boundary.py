"""The public-boundary scan blocks secrets without flagging ordinary hostnames."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_override_manifest import FORBIDDEN


class PublicBoundaryPatternTests(unittest.TestCase):
    def test_secret_like_values_are_blocked(self):
        for text in ('sk-abc123', 'key sk-abc123', 'token=abc', 'ghp_abc', 'IP-CIDR,192.168.1.0/24'):
            with self.subTest(text=text):
                self.assertTrue(FORBIDDEN.search(text))

    def test_hostnames_containing_sk_dash_are_allowed(self):
        # "mask-" contains "sk-"; Apple Private Relay hosts must not trip the API-key check.
        for text in ('DOMAIN,mask-boot.icloud.com', 'DOMAIN,mask-api.fe2.apple-dns.net', 'DOMAIN,desk-app.example'):
            with self.subTest(text=text):
                self.assertFalse(FORBIDDEN.search(text))


if __name__ == '__main__':
    unittest.main()
