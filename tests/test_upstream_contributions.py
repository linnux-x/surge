"""Coverage metrics must distinguish text overlap from address/domain coverage."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_upstream_sources import Coverage, contribution


class ContributionTests(unittest.TestCase):
    def test_suffix_covers_exact_and_subsuffix_but_not_sibling(self):
        c = Coverage({'domain-suffix,example.com'})
        self.assertEqual(c.residual('domain,api.example.com'), [])
        self.assertEqual(c.residual('domain-suffix,api.example.com'), [])
        self.assertEqual(c.residual('domain,notexample.com'), ['domain,notexample.com'])

    def test_exact_domain_does_not_cover_subdomains(self):
        c = Coverage({'domain,example.com'})
        self.assertEqual(c.residual('domain-suffix,example.com'), ['domain-suffix,example.com'])

    def test_options_are_not_silently_weakened(self):
        c = Coverage({'domain-suffix,example.com'})
        self.assertTrue(c.residual('domain,api.example.com,extended-matching'))

    def test_union_of_small_cidrs_covers_larger_cidr(self):
        c = Coverage({'ip-cidr,10.0.0.0/25', 'ip-cidr,10.0.0.128/25'})
        self.assertEqual(c.residual('ip-cidr,10.0.0.0/24'), [])

    def test_partial_cidr_and_unique_address_count(self):
        r = contribution({'ip-cidr,10.0.0.0/24'}, {'ip-cidr,10.0.0.0/25'})
        self.assertEqual(r['residual_rules'], ['ip-cidr,10.0.0.128/25'])
        self.assertEqual(r['residual_ipv4_addresses'], '128')
        self.assertEqual(r['fully_covered_rules'], 0)

    def test_overlapping_own_ranges_do_not_double_count_addresses(self):
        r = contribution({'ip-cidr,10.0.0.0/24', 'ip-cidr,10.0.0.0/25'}, set())
        self.assertEqual(r['residual_ipv4_addresses'], '256')

    def test_ipv6_and_ipv4_are_separate(self):
        r = contribution({'ip-cidr6,2001:db8::/126'}, {'ip-cidr6,2001:db8::/127', 'ip-cidr,0.0.0.0/0'})
        self.assertEqual(r['residual_ipv6_addresses'], '2')
        self.assertEqual(r['residual_ipv4_addresses'], '0')

    def test_keyword_coverage_is_not_inferred(self):
        c = Coverage({'domain-keyword,example'})
        self.assertEqual(c.residual('domain,example.com'), ['domain,example.com'])
