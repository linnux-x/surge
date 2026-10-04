"""Explicit upstream exclusion contract; Manual includes remain authoritative."""
from pathlib import Path
import re
from rule_validator import ALLOWED_TYPES, DOMAIN_VALUE_RE, DOMAIN_WILDCARD_VALUE_RE

DOMAIN_TYPES = {'DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD', 'DOMAIN-WILDCARD'}


def exclusion_key(rule: str) -> str:
    parts = rule.strip().split(',')
    # Only domain identity is case-insensitive. Do not discard IP options or
    # lowercase regex/process values whose semantics can be case-sensitive.
    if parts[0].upper() in DOMAIN_TYPES and len(parts) >= 2:
        return ','.join(part.lower() for part in parts[:2])
    return rule.strip()


def read_exclusions(path: Path) -> list[str]:
    rules = []
    for number, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        rule = raw.strip()
        if not rule or rule.startswith('#'):
            continue
        parts = rule.split(',')
        if len(parts) < 2 or parts[0] not in ALLOWED_TYPES or not parts[1]:
            raise ValueError(f'{path.name}:{number}: exclusion requires an explicit rule type and value')
        if parts[0] in DOMAIN_TYPES:
            pattern = (re.compile(r'[a-z0-9._-]+') if parts[0] == 'DOMAIN-KEYWORD' else
                       DOMAIN_WILDCARD_VALUE_RE if parts[0] == 'DOMAIN-WILDCARD' else DOMAIN_VALUE_RE)
            if not pattern.fullmatch(parts[1].lower()) or any(p != 'extended-matching' for p in parts[2:]):
                raise ValueError(f'{path.name}:{number}: invalid domain exclusion')
        rules.append(rule)
    return rules
