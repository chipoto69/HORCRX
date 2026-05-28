#!/usr/bin/env python3
# H5 marketplace-envelope KATs — specs/marketplace/ARCHITECTURE.md §3.2; validation/fixtures/envelopes/

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

REPO = Path(__file__).resolve().parents[2]
ENVELOPES = REPO / 'validation/fixtures/envelopes'
AGE_WRAPPER = ENVELOPES / 'operator-slot-body.age.json'
BOX_WRAPPER = ENVELOPES / 'per-buyer-envelope.x25519-xsalsa20-poly1305.json'
AGE_CHUNK_SIZE = 64 * 1024
AGE_TAG_SIZE = 16


def fail(message: str) -> None:
    print(f'MARKETPLACE ENVELOPE KATS FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def increment_age_nonce(counter: bytearray) -> None:
    for i in range(10, -1, -1):
        counter[i] = (counter[i] + 1) & 0xFF
        if counter[i] != 0:
            return
    fail('age stream chunk counter wrapped unexpectedly')


def derive_age_stream_key(file_key: bytes, nonce: bytes) -> bytes:
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=nonce, info=b'payload')
    return hkdf.derive(file_key)


def age_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    aead = ChaCha20Poly1305(key)
    plaintext = bytearray()
    counter = bytearray(12)
    offset = 0
    while offset < len(ciphertext):
        remaining = len(ciphertext) - offset
        take = AGE_CHUNK_SIZE + AGE_TAG_SIZE
        if remaining < take:
            take = remaining
        chunk = ciphertext[offset: offset + take]
        nonce = bytes(counter)
        try:
            part = aead.decrypt(nonce, chunk, None)
        except Exception:
            last_nonce = bytearray(counter)
            last_nonce[-1] = 0x01
            part = aead.decrypt(bytes(last_nonce), chunk, None)
        plaintext.extend(part)
        increment_age_nonce(counter)
        offset += take
    return bytes(plaintext)


def verify_operator_slot_body() -> None:
    wrapper = load_json(AGE_WRAPPER)
    source = load_json((AGE_WRAPPER.parent / wrapper['source_fixture']).resolve())
    file_key = bytes.fromhex(source['file_key_hex'])
    nonce = bytes.fromhex(source['nonce_hex'])
    ciphertext = bytes.fromhex(source['ciphertext_hex'])
    key = derive_age_stream_key(file_key, nonce)
    plaintext = age_decrypt(ciphertext, key)
    actual_hash = hashlib.sha256(plaintext).hexdigest()
    if actual_hash != wrapper['expected_payload_sha256']:
        fail('operator slot-body payload hash mismatch')
    if wrapper['recipient_role'] != 'operator':
        fail('operator slot-body wrapper must target the operator recipient role')


def verify_per_buyer_envelope() -> None:
    wrapper = load_json(BOX_WRAPPER)
    source = load_json((BOX_WRAPPER.parent / wrapper['source_fixture']).resolve())
    try:
        from nacl import bindings
    except ModuleNotFoundError as exc:
        fail(f'PyNaCl is required for marketplace envelope KATs: {exc}')

    message = bytes.fromhex(source['message_hex'])
    nonce = bytes.fromhex(source['nonce_hex'])
    public_key = bytes.fromhex(source['bob_public_key_hex'])
    secret_key = bytes.fromhex(source['alice_scalar_hex'])
    ciphertext = bindings.crypto_box(message, nonce, public_key, secret_key)

    if hashlib.sha256(message).hexdigest() != wrapper['expected_message_sha256']:
        fail('buyer envelope message hash mismatch')
    if hashlib.sha256(ciphertext).hexdigest() != wrapper['expected_ciphertext_sha256']:
        fail('buyer envelope ciphertext hash mismatch')


def main() -> None:
    verify_operator_slot_body()
    verify_per_buyer_envelope()
    print('MARKETPLACE ENVELOPE KATS PASS: operator age slot-body and per-buyer x25519-xsalsa20-poly1305 envelopes matched their golden vectors.')


if __name__ == '__main__':
    main()
