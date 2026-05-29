#!/usr/bin/env python3
# H5 preview-integrity — specs/marketplace/ARCHITECTURE.md §3.2 content gateway; specs/marketplace/ip-preservation.md §5

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FIXTURE = REPO / 'validation/fixtures/previews/preview-integrity.json'


def fail(message: str) -> None:
    print(f'PREVIEW INTEGRITY FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def digest(payload: str) -> str:
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def verify_fetch(payload: str, expected_sha256: str) -> bool:
    return digest(payload) == expected_sha256


def main() -> None:
    fixture = json.loads(FIXTURE.read_text(encoding='utf-8'))
    expected = fixture['expected_sha256']
    if digest(fixture['original_text']) != expected:
        fail('golden preview fixture hash does not match the recorded digest')
    if not verify_fetch(fixture['honest_fetch_text'], expected):
        fail('honest gateway fetch should have matched the recorded preview hash')
    if verify_fetch(fixture['tampered_text'], expected):
        fail('tampered gateway fetch unexpectedly matched the recorded preview hash')

    print('PREVIEW INTEGRITY PASS: honest fetch matched the stored hash and tampered preview bytes were rejected on re-hash.')


if __name__ == '__main__':
    main()
