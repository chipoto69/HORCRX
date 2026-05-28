# Memory graft provenance

Version: `v0.1-draft`

Memory grafts are portable canon with stricter lineage and consent rules than ordinary slot files. A graft MAY travel, but it must always explain where it came from, who signed it, what consent posture applies, and how long any consent evidence must be retained.

## Record shape

Every exported `memory/grafts/*.md` artifact MUST carry a provenance record with the following fields.

| Field | Type | Meaning |
|---|---|---|
| `parent_cid` | string | content-addressed CID of the parent vessel or parent graft source |
| `signed_by` | string | Ed25519 public-key reference to the parent vessel authoring key that signed the graftable memory surface |
| `consent_envelope` | object | consent metadata for the grafted memory payload |
| `retention` | integer or string | consent-evidence retention period in days, or the literal string `indefinite` |

## Consent envelope

`consent_envelope` is a tagged union with exactly one of the following shapes.

### 1. Encrypted explicit-consent record

Use this form when the export carries a machine-verifiable consent artifact.

```json
{
  "cipher_suite": "age|x25519-xsalsa20-poly1305",
  "recipient_key_ids": ["key_01"],
  "ciphertext_cid": "cid:sha256:..."
}
```

Rules:

- `cipher_suite` MUST name one of the supported envelope suites.
- `recipient_key_ids` MUST list the keys allowed to open the consent artifact.
- `ciphertext_cid` MUST point to the encrypted consent record, not plaintext consent text.

### 2. Inline consent status

Use this form when no encrypted consent artifact ships with the graft.

```json
{
  "consent_status": "explicit|implicit|denied"
}
```

Rules:

- `explicit` means the operator or human source directly approved export.
- `implicit` means export is allowed by an already-declared policy boundary.
- `denied` means the graft MUST NOT be exported, installed, or merged into portable canon.

## Retention

`retention` governs how long the consent evidence must remain auditable.

- integer values mean UTC days from export time;
- `indefinite` means the consent record is part of permanent lineage evidence;
- `0` is invalid;
- a graft with `consent_status: denied` MUST still retain the denial record long enough to explain the rejection path.

## Validation rules

1. `parent_cid` MUST be non-empty and content-addressed.
2. `signed_by` MUST resolve to an Ed25519 authoring key declared by the parent vessel.
3. Exactly one consent-envelope shape is allowed: encrypted record **or** inline `consent_status`.
4. Grafts containing `memories/USER.md`-class material MUST NOT use `implicit` consent unless a higher-order policy explicitly permits it.
5. Install and graft tooling MUST reject any provenance record with `consent_status: denied`.

## Example

```json
{
  "parent_cid": "cid:sha256:2f8e6d6d5f0f5db3f5f1d8b779fd7d1b2d8f6b35c91f0af43718c9ab3f6bc091",
  "signed_by": "author_keys.parent-ed25519",
  "consent_envelope": {
    "cipher_suite": "age",
    "recipient_key_ids": ["operator-consent-key-01"],
    "ciphertext_cid": "cid:sha256:4d2425d66cf8d3d374d4f74ab3ea49ad9f0c8c57d8e3f08d0d90a0d5dfdb4fd3"
  },
  "retention": "indefinite"
}
```

## Local source paths

- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/signing-and-lineage.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/research/12-hardening-recon.md`
