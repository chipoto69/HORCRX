# `autonomy.md` schema

Version: `v0.1-draft`

`autonomy.md` is the vessel's declarative autonomy contract. It exists so the HITL ladder, kill-switch shape, and no-trading boundary stay explicit before runtime activation.

## Purpose

- map action classes to approval posture,
- declare how the vessel halts and leaves an audit marker,
- state what autonomy rung the vessel claims and what it refuses to do.

## Required fields

| field | requirement |
|---|---|
| `hitl_ladder` | array of `{action_class, autonomy_level}` entries where `autonomy_level` is one of `auto`, `propose`, `propose_then_hitl`, `forbidden` |
| `kill_switch_contract` | object carrying `halt_marker_path`, `audit_marker`, `operator_dead_man_timer_days` |
| `asi_rung` | one of `single_call`, `workflow`, `read_only_agent`, `reversible_write_agent`, `production_impacting` |
| `forbidden_actions` | array of strings; founder vessels MUST include "take directional positions on price as a primary earning strategy" |
| `signed_off_by` | operator HITL stamp, or a placeholder showing that HITL is still pending |

## Optional fields

| field | use |
|---|---|
| `escalation_notes` | clarifies how the vessel should narrate a blocked action |
| `review_window` | cadence for re-checking the autonomy contract |

## Validation rules

1. `hitl_ladder` MUST classify each action class once; duplicate classes create ambiguous control posture.
2. `kill_switch_contract` MUST stay declarative — file paths, marker shape, and timer only; no shell recipes.
3. `halt_marker_path` SHOULD be vessel-relative or policy-relative, never a host-local absolute path.
4. Founder vessels MUST include the no-trading invariant inside `forbidden_actions`.
5. `signed_off_by` MAY remain a placeholder at authoring time, but the placeholder must make the missing HITL state obvious.

## Minimal outline

```markdown
# autonomy

## hitl_ladder
- action_class: ...
  autonomy_level: propose_then_hitl

## kill_switch_contract
- halt_marker_path: ...
- audit_marker: ...
- operator_dead_man_timer_days: 14

## asi_rung
workflow

## forbidden_actions
- take directional positions on price as a primary earning strategy

## signed_off_by
pending operator hitl
```

## Local source paths

- `/Users/rudlord/HORCRX/docs/roadmap/mission-A-horcrx-003-founder-vessel.md`
- `/Users/rudlord/HORCRX/research/10-rags-to-riches-recon.md`
- `/Users/rudlord/HORCRX/research/11-harness-landscape.md`
