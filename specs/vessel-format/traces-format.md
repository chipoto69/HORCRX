# Traces format

Version: `v0.1-draft`

HORCRX traces are redacted NDJSON event logs. They are portable enough for audit, replay, and curation, but lighter and safer than raw runtime databases.

## File format

- one JSON object per line,
- UTF-8 encoded,
- LF line endings,
- filename pattern: `YYYY-MM-DDTHHMMSSZ--<run-id>.ndjson`.

## NDJSON event schema

Each line MUST contain:

```json
{
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

Optional fields:

- `tool_name`
- `cost_usd`
- `token_in`
- `token_out`
- `approval_id`
- `error`
- `parent_event_id`

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

## Relationship to Hermes and ATLAS

- Hermes already emits audit records through `dispatch()` and `state/audit.sqlite`.
- ATLAS already cares about transaction and payment provenance.
- HORCRX traces are the portable middle layer: structured enough to travel, but not a raw copy of `state.db`.

## Local source paths

- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/state/audit.sqlite`
