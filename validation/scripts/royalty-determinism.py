#!/usr/bin/env python3
# Royalty determinism — specs/marketplace/royalties.md §2.2 and §3

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FIXTURE = REPO / 'validation/fixtures/royalty/lineage-fixture.json'
EXPECTED = REPO / 'validation/fixtures/royalty/expected-payout-plan.json'


def fail(message: str) -> None:
    print(f'ROYALTY DETERMINISM FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def collect_ancestors(node: dict, max_depth: int, depth: int = 1) -> list[tuple[int, str]]:
    if depth > max_depth:
        return []
    ancestors = []
    for parent in node.get('parents', []):
        ancestors.append((depth, parent['payout_target']))
        if parent.get('multi_hop', False):
            ancestors.extend(collect_ancestors(parent, max_depth, depth + 1))
    return ancestors


def apportion(total: int, weighted_targets: list[tuple[str, float, str]]) -> list[dict]:
    weight_sum = sum(weight for _, weight, _ in weighted_targets)
    raw = []
    allocated = 0
    for target, weight, reason in weighted_targets:
        exact = total * (weight / weight_sum)
        amount = int(exact)
        raw.append({'target': target, 'reason': reason, 'amount': amount, 'remainder_rank': exact - amount})
        allocated += amount
    leftover = total - allocated
    for item in sorted(raw, key=lambda item: (-item['remainder_rank'], item['target']))[:leftover]:
        item['amount'] += 1
    return [{'target': item['target'], 'reason': item['reason'], 'amount': item['amount']} for item in sorted(raw, key=lambda item: (item['reason'], item['target']))]


def build_plan(fixture: dict) -> dict:
    sale_amount = fixture['sale_amount']
    creator_amount = sale_amount * 70 // 100
    resonator_amount = sale_amount * 20 // 100
    protocol_amount = sale_amount - creator_amount - resonator_amount

    lineage = fixture['lineage']
    ancestors = collect_ancestors(lineage, fixture['graph_depth'])
    weighted_targets = []
    for depth, target in ancestors:
        weighted_targets.append((target, 1 / depth, f'ancestor-depth-{depth}'))
    if resonator_amount and not weighted_targets:
        fail('lineage has no ancestor payout targets for the resonator allocation slice')
    resonators = apportion(resonator_amount, weighted_targets) if weighted_targets else []

    allocations = resonators + [
        {'target': lineage['payout_target'], 'reason': 'creator', 'amount': creator_amount},
        {'target': fixture['protocol_target'], 'reason': 'protocol', 'amount': protocol_amount},
    ]
    allocations = sorted(allocations, key=lambda item: (item['reason'], item['target']))
    return {
        'sale_amount': sale_amount,
        'total_allocated': sum(item['amount'] for item in allocations),
        'allocations': allocations,
    }


def main() -> None:
    fixture = json.loads(FIXTURE.read_text(encoding='utf-8'))
    expected = json.loads(EXPECTED.read_text(encoding='utf-8'))
    first = build_plan(fixture)
    second = build_plan(fixture)
    if first != second:
        fail('same lineage input produced two different payout plans')
    if json.dumps(first, sort_keys=True) != json.dumps(expected, sort_keys=True):
        fail(f'computed payout plan does not match golden fixture: {json.dumps(first, indent=2)}')
    print('ROYALTY DETERMINISM PASS: identical lineage input produced a stable payout plan matching the golden fixture.')


if __name__ == '__main__':
    main()
