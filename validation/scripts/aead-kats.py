#!/usr/bin/env python3
# H4 AEAD KATs — age/CCTV payload vector + libsodium crypto_box vector

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

REPO = Path(__file__).resolve().parents[2]
AEAD_DIR = REPO / "validation/fixtures/aead"
AGE_FIXTURE = AEAD_DIR / "age-cctv-x25519.json"
BOX_FIXTURE = AEAD_DIR / "x25519-xsalsa20-poly1305-libsodium.json"
AGE_CHUNK_SIZE = 64 * 1024
AGE_TAG_SIZE = 16


def fail(message: str) -> None:
    print(f"AEAD KATS FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_fixture(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def increment_age_nonce(counter: bytearray) -> None:
    for i in range(10, -1, -1):
        counter[i] = (counter[i] + 1) & 0xFF
        if counter[i] != 0:
            return
    fail("age stream chunk counter wrapped unexpectedly")


def derive_age_stream_key(file_key: bytes, nonce: bytes) -> bytes:
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=nonce,
        info=b"payload",
    )
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
        chunk = ciphertext[offset : offset + take]

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


def age_encrypt(plaintext: bytes, key: bytes) -> bytes:
    aead = ChaCha20Poly1305(key)
    ciphertext = bytearray()
    counter = bytearray(12)
    remaining = plaintext

    while True:
        chunk = remaining[:AGE_CHUNK_SIZE]
        remaining = remaining[AGE_CHUNK_SIZE:]
        nonce = bytearray(counter)
        if not remaining:
            nonce[-1] = 0x01
        ciphertext.extend(aead.encrypt(bytes(nonce), chunk, None))
        increment_age_nonce(counter)
        if not remaining:
            break

    return bytes(ciphertext)


def verify_age_vector() -> None:
    fixture = load_fixture(AGE_FIXTURE)
    file_key = bytes.fromhex(fixture["file_key_hex"])
    nonce = bytes.fromhex(fixture["nonce_hex"])
    ciphertext = bytes.fromhex(fixture["ciphertext_hex"])
    expected_hash = fixture["payload_sha256"]

    key = derive_age_stream_key(file_key, nonce)
    plaintext = age_decrypt(ciphertext, key)
    actual_hash = hashlib.sha256(plaintext).hexdigest()
    if actual_hash != expected_hash:
        fail(f"age payload hash mismatch: expected {expected_hash}, got {actual_hash}")

    roundtrip = age_encrypt(plaintext, key)
    if roundtrip != ciphertext:
        fail("age STREAM ciphertext did not round-trip to the CCTV x25519 vector")


def verify_crypto_box_vector() -> None:
    fixture = load_fixture(BOX_FIXTURE)
    try:
        from nacl import bindings
    except ModuleNotFoundError as exc:
        fail(
            "PyNaCl is required for the x25519-xsalsa20-poly1305 vector; "
            "install it before running this validator"
        )

    message = bytes.fromhex(fixture["message_hex"])
    nonce = bytes.fromhex(fixture["nonce_hex"])
    public_key = bytes.fromhex(fixture["bob_public_key_hex"])
    secret_key = bytes.fromhex(fixture["alice_secret_key_hex"])
    expected_ciphertext = bytes.fromhex(fixture["ciphertext_hex"])

    ciphertext = bindings.crypto_box(message, nonce, public_key, secret_key)
    if ciphertext != expected_ciphertext:
        fail("libsodium crypto_box vector mismatch")

    shared_key = bindings.crypto_box_beforenm(public_key, secret_key)
    afternm_ciphertext = bindings.crypto_box_afternm(message, nonce, shared_key)
    if afternm_ciphertext != expected_ciphertext:
        fail("libsodium crypto_box_afternm vector mismatch")


def main() -> None:
    verify_age_vector()
    verify_crypto_box_vector()
    print(
        "AEAD KATS PASS: age CCTV payload vector and libsodium "
        "x25519-xsalsa20-poly1305 vector both matched their golden ciphertext."
    )


if __name__ == "__main__":
    main()
