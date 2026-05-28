#!/usr/bin/env python3
# GATE-HX-04 — specs/vessel-format/signing-and-lineage.md; specs/vessel-format/SPEC.md §5.1
"""Round-trip Ed25519 signing for canonical manifest and slot payloads.

The repo forbids committing private keys, so this gate generates an ephemeral Ed25519 keypair
at runtime for the sign/verify round-trip and separately validates that the declared reference
vessel public keys are decodable Ed25519 multibase keys with `manifest+slots`-compatible scope.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MANIFESTS = [
    REPO / 'examples/horcrx-001-candysoul/manifest.json',
    REPO / 'examples/horcrx-002-orbel-pack/manifest.json',
]
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def fail(message: str) -> None:
    print(f'GATE-HX-04 FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def canonical_bytes(payload: object) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def base58btc_decode(value: str) -> bytes:
    if not value.startswith('z'):
        fail(f'{value!r} is not base58btc multibase')
    number = 0
    for char in value[1:]:
        try:
            number = number * 58 + BASE58_ALPHABET.index(char)
        except ValueError as exc:
            fail(f'invalid base58btc character {char!r}: {exc}')
    raw = number.to_bytes((number.bit_length() + 7) // 8, 'big') if number else b''
    leading_zeros = len(value[1:]) - len(value[1:].lstrip('1'))
    return b'\x00' * leading_zeros + raw


def verify_declared_public_key(manifest: dict) -> None:
    author_keys = manifest.get('author_keys', [])
    if not author_keys:
        fail(f"{manifest['id']} declares no author keys")
    for author_key in author_keys:
        if author_key.get('algorithm') != 'Ed25519':
            fail(f"{manifest['id']} uses unexpected algorithm {author_key.get('algorithm')!r}")
        public_key = author_key.get('public_key_multibase')
        if not public_key:
            fail(f"{manifest['id']} is missing public_key_multibase")
        decoded = base58btc_decode(public_key)
        if len(decoded) != 34 or decoded[:2] != bytes.fromhex('ed01'):
            fail(f"{manifest['id']} public key does not decode to an ed25519-pub multicodec")
        if 'manifest' not in author_key.get('scope', ''):
            fail(f"{manifest['id']} key scope {author_key.get('scope')!r} does not cover manifest signing")


def manifest_payload(manifest: dict) -> dict:
    slot_summary = {}
    for slot_name in sorted(manifest['slots']):
        slot_summary[slot_name] = [
            {
                'cid': artifact['cid'],
                'digest': artifact['digest'],
                'path': artifact['path'],
                'signer_key_id': artifact['signer_key_id'],
            }
            for artifact in manifest['slots'][slot_name]['artifacts']
        ]
    return {
        'id': manifest['id'],
        'kind': manifest['kind'],
        'manifest_version': manifest['manifest_version'],
        'parent_cids': manifest['parent_cids'],
        'slots': slot_summary,
    }


def slot_payload(manifest: dict, slot_name: str, artifact: dict) -> dict:
    return {
        'manifest_id': manifest['id'],
        'slot': slot_name,
        'cid': artifact['cid'],
        'digest': artifact['digest'],
        'path': artifact['path'],
        'signer_key_id': artifact['signer_key_id'],
    }


def sign_and_verify(payload: bytes) -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        key = temp / 'key.pem'
        pub = temp / 'pub.pem'
        message = temp / 'message.bin'
        signature = temp / 'signature.bin'
        message.write_bytes(payload)
        subprocess.run(['openssl', 'genpkey', '-algorithm', 'Ed25519', '-out', str(key)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['openssl', 'pkey', '-in', str(key), '-pubout', '-out', str(pub)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['openssl', 'pkeyutl', '-sign', '-inkey', str(key), '-rawin', '-in', str(message), '-out', str(signature)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['openssl', 'pkeyutl', '-verify', '-pubin', '-inkey', str(pub), '-sigfile', str(signature), '-rawin', '-in', str(message)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def verify_artifact_digest(artifact: dict) -> None:
    artifact_path = REPO / 'examples' / artifact['path']
    if not artifact_path.exists():
        fail(f'missing artifact {artifact_path.relative_to(REPO)}')
    digest = sha256_bytes(artifact_path.read_bytes())
    expected_digest = artifact['digest'].split(':', 1)[1]
    expected_cid = artifact['cid'].split(':', 2)[2]
    if digest != expected_digest:
        fail(f'digest mismatch for {artifact_path.relative_to(REPO)}: {digest} != {expected_digest}')
    if digest != expected_cid:
        fail(f'cid mismatch for {artifact_path.relative_to(REPO)}: {digest} != {expected_cid}')


def main() -> None:
    checked_payloads = 0
    decoded_keys = []
    for manifest_path in MANIFESTS:
        manifest = load_json(manifest_path)
        verify_declared_public_key(manifest)
        decoded_keys.extend(key['key_id'] for key in manifest['author_keys'])
        sign_and_verify(canonical_bytes(manifest_payload(manifest)))
        checked_payloads += 1
        for slot_name, slot in sorted(manifest['slots'].items()):
            for artifact in slot['artifacts']:
                if not artifact.get('signer_key_id'):
                    fail(f"{manifest['id']}:{slot_name} is missing signer_key_id")
                verify_artifact_digest(artifact)
                sign_and_verify(canonical_bytes(slot_payload(manifest, slot_name, artifact)))
                checked_payloads += 1
    print(f'GATE-HX-04 PASS: verified {checked_payloads} canonical payload round-trips and decoded {len(decoded_keys)} declared Ed25519 public keys.')


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as exc:
        fail(f'openssl command failed: {exc}')
