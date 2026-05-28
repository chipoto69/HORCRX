#!/usr/bin/env python3
# H5 payout-target format — specs/registry/listing.schema.json; specs/marketplace/ip-preservation.md §5.1

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCHEMA = REPO / 'specs/registry/listing.schema.json'
VALID = REPO / 'validation/fixtures/payout-target-format/valid.json'
INVALID = REPO / 'validation/fixtures/payout-target-format/invalid.json'


def fail(message: str) -> None:
    print(f'PAYOUT TARGET FORMAT FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def load_cases(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding='utf-8'))
    return payload['cases']


def main() -> None:
    schema = json.loads(SCHEMA.read_text(encoding='utf-8'))
    pattern = schema['$defs']['chainTypedIdentifier']['pattern']
    matcher = re.compile(pattern)

    description = schema['properties']['payout_target']['description']
    if 'chain-typed' not in description:
        fail('listing schema no longer documents payout_target as a chain-typed identifier')

    for case in load_cases(VALID):
        if matcher.fullmatch(case['value']) is None:
            fail(f"expected valid target to pass: {case['name']} -> {case['value']}")

    for case in load_cases(INVALID):
        if matcher.fullmatch(case['value']) is not None:
            fail(f"expected invalid target to fail: {case['name']} -> {case['value']}")

    print('PAYOUT TARGET FORMAT PASS: schema regex accepted all valid fixtures and rejected all invalid fixtures.')


if __name__ == '__main__':
    main()
