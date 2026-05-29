#!/usr/bin/env python3
# H5 royalty split sum gate — specs/registry/listing.schema.json; specs/marketplace/royalties.md §5

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_FIXTURES = sorted((REPO / 'examples/listings').glob('*.json'))


def fail(message: str) -> None:
    print(f'ROYALTY SPLIT SUM FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def load_listing(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        fail(f'{path.relative_to(REPO)} is not valid JSON: {exc}')


def validate_basis_points(path: Path, index: int, basis_points: object) -> int:
    field = f'{path.relative_to(REPO)} royalty_split[{index}].basis_points'
    if type(basis_points) is not int:
        fail(f'{field} must be an integer')
    if basis_points < 0:
        fail(f'{field} must be greater than or equal to 0')
    if basis_points > 10000:
        fail(f'{field} must be less than or equal to 10000')
    return basis_points


def main() -> None:
    listing_paths = [Path(arg).resolve() for arg in sys.argv[1:]] or DEFAULT_FIXTURES
    if not listing_paths:
        fail('no listing fixtures found to validate')

    checked = 0
    for path in listing_paths:
        listing = load_listing(path)
        royalty_split = listing.get('royalty_split')
        if not isinstance(royalty_split, list) or not royalty_split:
            fail(f"{path.relative_to(REPO)} is missing a non-empty royalty_split array")

        total = 0
        for index, share in enumerate(royalty_split):
            if not isinstance(share, dict):
                fail(f'{path.relative_to(REPO)} royalty_split[{index}] must be an object')
            total += validate_basis_points(path, index, share.get('basis_points'))

        if total != 10000:
            fail(f'{path.relative_to(REPO)} royalty_split totals {total} basis points; expected exactly 10000')
        checked += 1

    print(f'ROYALTY SPLIT SUM PASS: validated aggregate royalty_split totals for {checked} listing fixture(s).')


if __name__ == '__main__':
    main()
