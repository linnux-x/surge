"""Convert country-labelled server metadata into narrow, policy-free rules."""
from __future__ import annotations
import csv
import io
import ipaddress
import json
import re
from urllib.parse import urlsplit

MAINLAND_PROVINCES = set('北京 天津 河北 山西 内蒙古 辽宁 吉林 黑龙江 上海 江苏 浙江 安徽 福建 江西 山东 河南 湖北 湖南 广东 广西 海南 重庆 四川 贵州 云南 西藏 陕西 甘肃 青海 宁夏 新疆'.split())
MAINLAND_PROVINCES |= {p + suffix for p in list(MAINLAND_PROVINCES) for suffix in ('省', '市')}
MAINLAND_PROVINCES |= {'内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区'}


def endpoint_rule(value: str, *, url: bool = False) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Missing Speedtest host')
    value = value.strip()
    parsed = urlsplit(value if url else 'http://' + value)
    if parsed.scheme not in ('http', 'https') or parsed.username or parsed.password:
        raise ValueError('Invalid Speedtest endpoint scheme or credentials')
    if not url and (parsed.path or parsed.query or parsed.fragment):
        raise ValueError('Speedtest host must not contain a path, query or fragment')
    if parsed.port is not None and not 1 <= parsed.port <= 65535:
        raise ValueError('Invalid Speedtest endpoint port')
    host = (parsed.hostname or '').lower().rstrip('.')
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        if len(host) > 253 or '.' not in host or any(not re.fullmatch(r'[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?', p) for p in host.split('.')):
            raise ValueError('Invalid Speedtest hostname')
        return 'DOMAIN,' + host
    if not address.is_global:
        raise ValueError('Speedtest endpoint must not use a private or reserved address')
    return f"{'IP-CIDR' if address.version == 4 else 'IP-CIDR6'},{address}/{address.max_prefixlen},no-resolve"


def convert_speedtest(raw: list[str], source_format: str) -> list[str]:
    rules: set[str] = set()
    text = '\n'.join(raw)
    if source_format in ('speedtest-json-cn', 'speedtest-json-international'):
        records = json.loads(text)
        if not isinstance(records, list) or not records:
            raise ValueError('Speedtest metadata must be a non-empty JSON array')
        for record in records:
            if not isinstance(record, dict) or not isinstance(record.get('country'), str) or not record['country'] or not re.fullmatch('[A-Z]{2}', str(record.get('cc', ''))):
                raise ValueError('Missing Speedtest country metadata')
            mainland = record['cc'] == 'CN' and record['country'] == 'China'
            # Inconsistent labels must not create DIRECT rules or be reclassified by guesswork.
            if (record['cc'] == 'CN') != (record['country'] == 'China'):
                continue
            if mainland != (source_format == 'speedtest-json-cn'):
                continue
            endpoints = []
            if record.get('host'):
                endpoints.append(endpoint_rule(record['host']))
            if record.get('url'):
                endpoints.append(endpoint_rule(record['url'], url=True))
            if not endpoints:
                raise ValueError('Speedtest server has no endpoint')
            rules.update(endpoints)
    elif source_format == 'speedtest-cn-csv':
        reader = csv.DictReader(io.StringIO(text))
        if not {'host', 'country_code', 'province', 'active'}.issubset(reader.fieldnames or []):
            raise ValueError('Speedtest CSV schema mismatch')
        for row in reader:
            if row.get('country_code') == 'CN' and row.get('province') in MAINLAND_PROVINCES and row.get('active') == '1':
                rules.add(endpoint_rule(row['host']))
    else:
        raise ValueError('Unknown Speedtest source format: ' + source_format)
    if not rules:
        raise ValueError('Speedtest source has no eligible endpoints; refusing an empty replacement')
    return sorted(rules)
