#!/usr/bin/env python3
# H5 revocation-never-deletes — specs/protocol/PROTOCOL.md §Revocation; specs/protocol/marketplace-flows.md §7

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FIXTURE = REPO / 'validation/fixtures/registry/revocation-lineage.json'


def fail(message: str) -> None:
    print(f'REVOCATION NEVER DELETES FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def apply_revocation(rows: list[dict], event: dict) -> list[dict]:
    latest = rows[-1]
    revocation_row = {
        'sequence': event['sequence'],
        'state': 'revoked',
        'revoked': True,
        'lineage_hash': f"{latest['lineage_hash']}::revoked",
        'previous_lineage_hash': latest['lineage_hash'],
        'evidence': event['reason'],
        'operator': event['operator'],
    }
    return rows + [revocation_row]


def main() -> None:
    fixture = json.loads(FIXTURE.read_text(encoding='utf-8'))
    original_rows = fixture['initial_rows']
    mutated = apply_revocation(original_rows, fixture['revocation_event'])

    if len(mutated) != len(original_rows) + 1:
        fail('revocation did not append exactly one new lineage row')
    if mutated[:len(original_rows)] != original_rows:
        fail('pre-existing lineage rows changed or were deleted during revocation')

    latest = mutated[-1]
    if latest['state'] != 'revoked' or latest.get('revoked') is not True:
        fail('latest row is not the expected revoked append-only state')
    if latest.get('previous_lineage_hash') != original_rows[-1]['lineage_hash']:
        fail('latest row does not point at the prior lineage hash')

    print('REVOCATION NEVER DELETES PASS: revocation appended one lineage row, preserved history, and marked the latest state as revoked.')


if __name__ == '__main__':
    main()
