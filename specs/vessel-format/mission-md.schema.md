# `mission.md` schema

Version: `v0.1-draft`

`mission.md` is the vessel's declared mission contract. It exists so the earning arc, abort posture, and termination state can travel with the vessel as portable doctrine.

## Purpose

- bind the seed and earning posture to one auditable slot,
- make success and abort conditions inspectable,
- declare the termination state before runtime activation.

## Required fields

| field | requirement |
|---|---|
| `seed_amount` | currency-prefixed string such as `"$66.60"` |
| `earning_posture` | one short block describing how the vessel earns; founder vessels MUST carry a clear "maker, not trader" sentiment |
| `success_ladder` | array of at least 3 rungs; each rung carries `name` and `criterion` |
| `abort_criteria` | array of at least 3 strings; founder vessels MUST include a line covering drift into directional trading |
| `termination_state` | single sentence describing the state that ends the mission |
| `signed_off_by` | operator HITL stamp, or a placeholder showing that HITL is still pending |

## Optional fields

| field | use |
|---|---|
| `review_window` | how often the mission contract should be re-read or re-stamped |
| `source_recon` | citations or dossier references that justify the ladder or abort posture |

## Validation rules

1. `seed_amount` MUST be a string, not a computed field or raw number.
2. `earning_posture` MUST stay declarative; do not embed shell commands, wallets, or runtime secrets.
3. `success_ladder` MUST have at least 3 rungs, and every rung MUST name both the milestone and the observable criterion.
4. `abort_criteria` MUST have at least 3 entries, and founder vessels MUST explicitly call out drift into directional trading.
5. `termination_state` MUST be one sentence so the close condition stays crisp.
6. `signed_off_by` MAY remain a placeholder at authoring time, but the placeholder must make the missing HITL state obvious.

## Minimal outline

```markdown
# mission

## seed_amount
$66.60

## earning_posture
maker, not trader.

## success_ladder
- name: ...
  criterion: ...

## abort_criteria
- ...

## termination_state
...

## signed_off_by
pending operator hitl
```

## Local source paths

- `/Users/rudlord/HORCRX/docs/roadmap/mission-A-horcrx-003-founder-vessel.md`
- `/Users/rudlord/HORCRX/research/10-rags-to-riches-recon.md`
- `/Users/rudlord/HORCRX/research/11-harness-landscape.md`
