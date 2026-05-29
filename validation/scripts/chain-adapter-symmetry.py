#!/usr/bin/env python3
# H5 chain-adapter symmetry — specs/protocol/chain-adapters.md §1 and §4

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPEC = REPO / 'specs/protocol/chain-adapters.md'
REQUIRED_METHODS = {'publishRecord', 'transferRecord', 'revokeRecord', 'getRecord'}


def fail(message: str) -> None:
    print(f'CHAIN ADAPTER SYMMETRY FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    text = SPEC.read_text(encoding='utf-8')
    if '## 2. Base adapter' not in text or '## 3. Solana adapter' not in text:
        fail('Base and Solana adapter sections must both exist in chain-adapters.md')
    if 'both adapters must expose the same abstract operations' not in text:
        fail('symmetry rules no longer require both adapters to expose the same abstract operations')

    match = re.search(r'```ts\ninterface IChainAdapter \{\n(?P<body>.*?)\n\}\n```', text, re.S)
    if not match:
        fail('could not locate the IChainAdapter TypeScript interface block')

    methods: dict[str, tuple[str, int]] = {}
    for raw_line in match.group('body').splitlines():
        line = raw_line.strip()
        method_match = re.match(r'(\w+)\(([^)]*)\):\s*Promise<([^>]+)>;', line)
        if not method_match:
            continue
        name, params, returns = method_match.groups()
        param_count = 0 if not params.strip() else len([part for part in params.split(',') if part.strip()])
        methods[name] = (returns, param_count)

    missing = sorted(REQUIRED_METHODS - methods.keys())
    if missing:
        fail(f'required adapter operations missing from IChainAdapter: {", ".join(missing)}')

    for name in sorted(REQUIRED_METHODS):
        returns, param_count = methods[name]
        if param_count != 1:
            fail(f'{name} must accept exactly one typed input parameter, found {param_count}')
        if not returns:
            fail(f'{name} does not declare a Promise return type')

    print('CHAIN ADAPTER SYMMETRY PASS: Base and Solana share a single abstract interface exposing publishRecord, transferRecord, revokeRecord, and getRecord with matching one-input signatures.')


if __name__ == '__main__':
    main()
