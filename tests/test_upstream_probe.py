"""Probe fallback contract and response lifetime, without network access."""
import io
from pathlib import Path
import sys
import unittest
import urllib.error
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_upstream_updates as checker


class Response(io.BytesIO):
    def __init__(self, body=b'payload'):
        super().__init__(body)
        self.headers = {'ETag': 'version', 'Last-Modified': 'date', 'Content-Length': '1'}
        self.reads = 0

    def read(self, *args):
        self.reads += 1
        return super().read(*args)


class UpstreamProbeTests(unittest.TestCase):
    def test_fallback_order_headers_body_and_closure(self):
        for failures in range(3):
            with self.subTest(failures=failures):
                response = Response()
                errors = [urllib.error.URLError('unavailable') for _ in range(failures)]
                with patch.object(checker.urllib.request, 'urlopen', side_effect=errors + [response]) as fetch:
                    result = checker.fetch_upstream_info('https://example.test/rules')
                self.assertEqual(result, {'etag': 'version', 'last_modified': 'date', 'content_length': '7' if failures == 2 else '1', 'source_available': True})
                self.assertEqual([c.args[0].method for c in fetch.call_args_list], ['HEAD', 'GET', 'GET'][:failures+1])
                for index, call in enumerate(fetch.call_args_list):
                    self.assertEqual(call.args[0].get_header('Range'), 'bytes=0-0' if index == 1 else None)
                    self.assertEqual(call.kwargs['timeout'], checker.REQUEST_TIMEOUT)
                    self.assertEqual(call.args[0].get_header('User-agent'), checker.REQUEST_HEADERS['User-Agent'])
                self.assertEqual(response.reads, int(failures == 2))
                self.assertTrue(response.closed)

    def test_http_errors_are_closed_and_outage_result_preserved(self):
        bodies = [Response() for _ in range(3)]
        errors = [urllib.error.HTTPError('https://example.test', 403, 'blocked', {}, body) for body in bodies]
        with patch.object(checker.urllib.request, 'urlopen', side_effect=errors):
            result = checker.fetch_upstream_info('https://example.test/rules')
        self.assertEqual(result, {'etag': None, 'last_modified': None, 'content_length': None, 'source_available': False})
        self.assertTrue(all(body.closed for body in bodies))

    def test_full_read_failure_closes_response(self):
        response = Response()
        with patch.object(response, 'read', side_effect=OSError('read failed')), patch.object(checker.urllib.request, 'urlopen', side_effect=[OSError(), OSError(), response]):
            self.assertFalse(checker.fetch_upstream_info('https://example.test/rules')['source_available'])
        self.assertTrue(response.closed)
