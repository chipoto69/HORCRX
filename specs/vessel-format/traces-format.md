# Traces format

Version: `v0.1-draft`

HORCRX traces are redacted NDJSON event logs. They are portable enough for audit, replay, and curation, but lighter and safer than raw runtime databases.

## File format

- one JSON object per line;
- every line MUST carry its own `schema_version`;
- UTF-8 encoded;
- LF line endings only;
- maximum encoded line size is **64 KiB** by default, and writers MUST reject lines beyond that limit before persistence;
- traces are **append-only**: writers MAY append new lines, but MUST NOT `UPDATE`, `DELETE`, or rewrite historical lines in place;
- default rotation is **one file per UTC day** using `YYYY-MM-DD.ndjson`; implementations MAY shard further as `YYYY-MM-DD--<run-id>.ndjson` so long as the day bucket remains explicit and append-only.

## NDJSON event schema

Each line MUST contain:

```json
{
  "schema_version": "1.0.0",
  "ts": "2026-05-26T20:00:00Z",
  "run_id": "run_01",
  "event_id": "evt_01",
  "stage": "observe|reason|tool|approval|result",
  "actor": "vessel|operator|peer|system",
  "summary": "short plain-language statement",
  "artifacts": ["cid:sha256:..."],
  "redaction": "none|partial|encrypted",
  "provenance": {
    "source": "dispatch|cron|workflow|manual",
    "host": "logical host label"
  }
}
```

Field rules:

- `schema_version` MUST be a semver string of the form `MAJOR.MINOR.PATCH`;
- `event_id` MUST be unique within the containing trace file;
- `summary` MUST remain plain-language and redactable;
- writers SHOULD emit stable key ordering for reproducible hashing and audit diffs.

Optional fields:

- `tool_name`
- `cost_usd`
- `token_in`
- `token_out`
- `approval_id`
- `error`
- `parent_event_id`

## Canonicalization and append-only invariant

Trace writers MUST treat the file as an immutable evidence log.

1. a line is validated and redacted **before** it is written;
2. once written, a line is historical evidence and MUST NOT be edited in place;
3. corrections, revocations, or clarifications append a new line that references the earlier `event_id`;
4. file compaction is not allowed on the canonical artifact path.

## Redaction rules

Redaction is mandatory when a trace contains:

- secrets,
- wallet seeds or private keys,
- raw OAuth material,
- private operator content that lacks export consent,
- host-internal network details.

Allowed redaction styles:

1. **inline partial redaction** — replace sensitive spans with markers;
2. **field omission** — drop the field and note why in `redaction_reason`;
3. **encrypted envelope** — keep only ciphertext references in the public trace index.

## Redaction-validator contract

Every candidate line MUST pass the repository redaction validator before write:

- validator entrypoint: `validation/scripts/redaction-validator.py`;
- minimum contract: redact sensitive spans and then assert no secret or PII pattern remains in the serialized line;
- failure mode: reject the write, do not append a partially redacted line;
- fixture coverage: `validation/fixtures/traces/` carries golden redaction cases with embedded secrets and PII.

## Encrypted envelope

When a trace line or artifact is encrypted, the public record keeps:

```json
{
  "redaction": "encrypted",
  "envelope": {
    "cipher_suite": "age|x25519-xsalsa20-poly1305",
    "recipient_key_ids": ["key_01"],
    "ciphertext_cid": "cid:sha256:...",
    "plaintext_digest": "sha256:..."
  }
}
```

`age` and `x25519-xsalsa20-poly1305` are both valid envelope suites. Repository KAT fixtures for both live under `validation/fixtures/aead/`.

## Relationship to Hermes and ATLAS

- Hermes already emits audit records through `dispatch()` and `state/audit.sqlite`.
- ATLAS already cares about transaction and payment provenance.
- HORCRX traces are the portable middle layer: structured enough to travel, but not a raw copy of `state.db`.

## Local source paths

- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/state/audit.sqlite`
