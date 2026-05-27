# `ledger.md` schema

Version: `v0.1-draft`

`ledger.md` is the vessel's declarative treasury posture. It exists so spend caps, earning knobs, custody, and respend policy remain inspectable without exposing keys.

## Purpose

- declare what the vessel may propose spending,
- declare what earning surfaces it may work on,
- state the custody and respend posture in portable form.

## Required fields

| field | requirement |
|---|---|
| `custody_posture` | one of `vessel_signs` or `host_signs_vessel_proposes` |
| `spend_knobs` | object carrying `per_tx`, `daily`, `weekly`, `cooldown`, `hitl_threshold`, `allowlist` |
| `earn_knobs` | object carrying `allowed_marketplaces`, `min_job_size`, `evidence_schema`, `payout_addresses_by_chain` |
| `spend_mix_ratios` | object carrying `earliness`, `making`, `overhead` |
| `revenue_respend_policy` | one short block that references the accepted OQ-19 posture |

## Optional fields

| field | use |
|---|---|
| `treasury_notes` | clarifies why a cap or ratio exists without changing the cap itself |
| `review_triggers` | events that force a manual review of the ledger posture |

## Validation rules

1. `allowlist` entries MUST be chain-typed identifiers such as `evm:0x...`; `[]` is valid and means HITL allowlisting is required.
2. `allowed_marketplaces` MUST reference entries declared in `plugins/marketplaces.json`.
3. `payout_addresses_by_chain` MUST be public-only addresses or `{}`; never place private keys or seeds here.
4. `spend_mix_ratios` MUST document the constraint that `earliness + overhead <= 50`.
5. `revenue_respend_policy` SHOULD name the policy in words, not hide it in an external script or executable recipe.

## Minimal outline

```markdown
# ledger

## custody_posture
host_signs_vessel_proposes

## spend_knobs
- per_tx: ...
- daily: ...
- weekly: ...
- cooldown: ...
- hitl_threshold: ...
- allowlist: []

## earn_knobs
- allowed_marketplaces: [...]
- min_job_size: ...
- evidence_schema: ...
- payout_addresses_by_chain: {}

## spend_mix_ratios
- earliness: ...
- making: ...
- overhead: ...

## revenue_respend_policy
...
```

## Local source paths

- `/Users/rudlord/HORCRX/docs/roadmap/mission-A-horcrx-003-founder-vessel.md`
- `/Users/rudlord/HORCRX/research/10-rags-to-riches-recon.md`
- `/Users/rudlord/HORCRX/research/11-harness-landscape.md`
