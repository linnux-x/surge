#!/usr/bin/env python3
"""Validate the narrow Host-only contract of the distributed DNS mapping module."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RULESET_PREFIX = 'https://ruleset.skk.moe/Modules/Rules/sukka_local_dns_mapping/'


def validate_text(text: str) -> None:
    sections = 0
    rulesets = 0
    for number, raw in enumerate(text.lstrip('\ufeff').splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith(('#', '//', ';')):
            continue
        if line.startswith('['):
            if line != '[Host]':
                raise ValueError(f'Line {number}: only the [Host] section is permitted')
            sections += 1
            continue
        if sections != 1 or '=' not in line:
            raise ValueError(f'Line {number}: expected a Host assignment inside one [Host] section')
        host, value = (part.strip() for part in line.split('=', 1))
        if not host or not value:
            raise ValueError(f'Line {number}: empty Host assignment')
        if host.upper().startswith('RULE-SET:'):
            if not re.fullmatch(re.escape('RULE-SET:' + RULESET_PREFIX) + r'[A-Za-z0-9_-]+\.conf', host):
                raise ValueError(f'Line {number}: unapproved DNS mapping ruleset URL')
            rulesets += 1
    if sections != 1 or rulesets == 0:
        raise ValueError('DNS module requires exactly one [Host] section and an approved ruleset reference')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path, default=ROOT / 'Module/DNS-Mapping.sgmodule')
    args = parser.parse_args()
    validate_text(args.path.read_text(encoding='utf-8'))
    print('DNS mapping module contract passed')


if __name__ == '__main__':
    main()
