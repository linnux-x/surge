"""Country selection and endpoint parsing must not widen DIRECT coverage."""
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from speedtest_sources import convert_speedtest, endpoint_rule


class SpeedtestSourceTests(unittest.TestCase):
    def servers(self, records, kind):
        return convert_speedtest([json.dumps(records)], 'speedtest-json-' + kind)

    def test_mainland_and_international_are_separated(self):
        records = [{'cc':cc, 'country':country, 'host':f'{cc.lower()}.example.com:8080'} for cc,country in [('CN','China'),('HK','Hong Kong'),('TW','Taiwan'),('US','United States')]]
        self.assertEqual(self.servers(records,'cn'), ['DOMAIN,cn.example.com'])
        self.assertEqual(self.servers(records,'international'), ['DOMAIN,hk.example.com','DOMAIN,tw.example.com','DOMAIN,us.example.com'])

    def test_conflicting_cn_label_never_becomes_direct(self):
        records = [{'cc':'CN','country':'Taiwan','host':'tw.example.com'}, {'cc':'CN','country':'China','host':'cn.example.com'}]
        self.assertEqual(self.servers(records,'cn'), ['DOMAIN,cn.example.com'])

    def test_url_and_server_host_both_kept_without_suffix_expansion(self):
        record = {'cc':'CN','country':'China','host':'a.example.com:8080','url':'https://b.example.com/upload'}
        self.assertEqual(self.servers([record],'cn'), ['DOMAIN,a.example.com','DOMAIN,b.example.com'])

    def test_csv_excludes_nonmainland_and_nonactive_rows(self):
        raw = ['host,country_code,province,active', 'ok.example.com:8080,CN,江苏,1', 'tw.example.com,CN,台湾,1', 'hk.example.com,HK,香港,1', 'off.example.com,CN,上海,0']
        self.assertEqual(convert_speedtest(raw,'speedtest-cn-csv'), ['DOMAIN,ok.example.com'])

    def test_bad_schema_or_empty_selection_blocks_replacement(self):
        for raw,fmt in [(['{}'],'speedtest-json-cn'), (['[]'],'speedtest-json-cn'), (['[{"host":"a.example.com"}]'],'speedtest-json-cn'), (['host,country','a.example.com,CN'],'speedtest-cn-csv')]:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                convert_speedtest(raw,fmt)

    def test_unsafe_endpoints_rejected(self):
        for host in ('*.example.com', 'user@example.com', 'example.com/path', 'example.com,REJECT', '127.0.0.1', '[::1]', 'host.example:99999'):
            with self.subTest(host=host), self.assertRaises(ValueError):
                endpoint_rule(host)

    def test_literal_ip_and_existing_underscore_names(self):
        self.assertEqual(endpoint_rule('1.1.1.1:8080'),'IP-CIDR,1.1.1.1/32,no-resolve')
        self.assertEqual(endpoint_rule('[2606:4700:4700::1111]:443'),'IP-CIDR6,2606:4700:4700::1111/128,no-resolve')
        self.assertEqual(endpoint_rule('a_b.example.com:443'),'DOMAIN,a_b.example.com')

    def test_both_geographic_views_share_one_fetch(self):
        import subprocess
        from unittest.mock import patch
        import generate_rules as generator
        generator.fetch_remote_source.cache_clear()
        try:
            with patch.object(generator.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'[]')) as fetch:
                generator.fetch_source('https://example.test/servers.json','speedtest-json-cn')
                generator.fetch_source('https://example.test/servers.json','speedtest-json-international')
                self.assertEqual(fetch.call_count,1)
        finally:
            generator.fetch_remote_source.cache_clear()
