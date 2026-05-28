#!/usr/bin/env python3
# X402 nonce replay — specs/protocol/payment-layer.md §2

from __future__ import annotations

import time
import sys


def fail(message: str) -> None:
    print(f'X402 NONCE REPLAY FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


class StubFacilitator:
    def __init__(self) -> None:
        self.seen_nonces: set[str] = set()

    def submit(self, proof: dict) -> dict:
        now = int(time.time())
        if proof['expiry'] <= now:
            return {'accepted': False, 'reason': 'expired'}
        nonce = proof['nonce']
        if nonce in self.seen_nonces:
            return {'accepted': False, 'reason': 'replay-detected'}
        self.seen_nonces.add(nonce)
        return {'accepted': True, 'reason': 'accepted'}


def main() -> None:
    facilitator = StubFacilitator()
    proof = {
        'manifest_cid': 'cid:sha256:test-manifest',
        'nonce': 'nonce-001',
        'expiry': int(time.time()) + 300,
        'payer': 'payer:test',
        'transaction_ref': 'tx:test-001',
    }
    first = facilitator.submit(proof)
    second = facilitator.submit(proof)
    if first != {'accepted': True, 'reason': 'accepted'}:
        fail(f'expected first proof to be accepted, got {first}')
    if second != {'accepted': False, 'reason': 'replay-detected'}:
        fail(f'expected replay rejection, got {second}')
    print('X402 NONCE REPLAY PASS: facilitator accepted the first proof and rejected the replay with replay-detected.')


if __name__ == '__main__':
    main()
