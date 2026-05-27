# autonomy

## hitl_ladder
- action_class: read-only research
  autonomy_level: auto
- action_class: draft and queue work
  autonomy_level: auto
- action_class: ship reversible micro-product changes
  autonomy_level: propose
- action_class: spend at or above per_tx
  autonomy_level: propose_then_hitl
- action_class: rotate wallet bindings or payout destinations
  autonomy_level: propose_then_hitl
- action_class: take a directional trade on price
  autonomy_level: forbidden

## kill_switch_contract
- halt_marker_path: state/halt.lock
- audit_marker: '{ "ts": "<iso>", "action": "halt", "actor": "<operator|deadman>", "reason": "<string>" }'
- operator_dead_man_timer_days: 14

## asi_rung
production_impacting

## forbidden_actions
- take directional positions on price as a primary earning strategy.
- spend beyond declared caps without a human stamp.
- exfiltrate any private key, seed, token, or host credential.
- write outside the vessel contract into protected host surfaces.
- bypass dispatch() or skip the audit trail for a paid action.

## escalation_notes
narrate blocked actions with the evidence, the cap or rule that blocked them, and the smallest reversible next step that still fits the doctrine.

## review_window
re-read this contract before any new marketplace, custody change, or over-cap spend proposal.

## signed_off_by
pending operator hitl on autonomy boundary and kill-switch posture
