# Worker F03 — hermes-binding — Completion Report

## Branch
foundation/hermes-binding

## Changed files (absolute paths)
- /Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md
- /Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md
- /Users/rudlord/HORCRX/specs/hermes-binding/open-questions-resolved.md
- /Users/rudlord/HORCRX/specs/hermes-binding/WORKER-COMPLETE.md

## Assertions claimed
- VAL-HERMES-01
- VAL-HERMES-02
- VAL-HERMES-03
- VAL-HERMES-04
- VAL-HERMES-05
- VAL-HERMES-06
- VAL-HERMES-07
- VAL-HERMES-08
- VAL-HERMES-09
- VAL-HERMES-10
- VAL-VESSEL-13

## Acceptance criteria met
- [x] Promoted the Hermes binding recon into canonical binding docs under `specs/hermes-binding/`.
- [x] Defined export, import, graft, provenance, royalty, and Hermes-as-marketplace-client paths.
- [x] Authored exact strip / rehydrate rules for Hermes profile surfaces.
- [x] Resolved the 10 open binding questions as ADRs with pending operator HITL status.
- [x] Stated explicitly that HORCRX does not modify any existing Hermes profile or fork.
- [x] Listed all 14 Hermes hard constraints verbatim with citation paths and cross-checked them against the vessel spec.

## Known risks / unresolved
- Operator HITL is still required to move the ten ADRs from `accepted-pending-HITL` to fully accepted.
- The mission recon treats iteration budget as shared with subagents, while the current upstream `iteration_budget.py` documents independent per-subagent caps; downstream implementation should preserve the mission doctrine and confirm the exact runtime behavior before CLI work begins.

## HITL required before next stage
- Confirm the ten ADR decisions in `open-questions-resolved.md`.
- Confirm whether any future implementation should offer an opt-in normalized session export surface beyond curated canon and redacted traces.

## Blocking findings (if any)
- None.

## Source dossier read
- /Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md
- /Users/rudlord/HORCRX/research/09-hermes-binding-recon.md
- /Users/rudlord/HORCRX/specs/vessel-format/SPEC.md
- /Users/rudlord/HORCRX/specs/vessel-format/memory-split.md
- /Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md
- /Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md
- /Users/rudlord/.hermes/config.yaml
- /Users/rudlord/.hermes/hermes-agent/AGENTS.md
- /Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py

## Next worker hand-off
- F04 should consume the provenance, royalty, and marketplace-client sections in `BINDING.md` when defining marketplace architecture.
- F07 should reference every file under `specs/hermes-binding/` from root docs and include the ADR HITL follow-up in roadmap planning.
- Any Phase 1 CLI worker should implement `hermes profile export --as-vessel`, `horcrx install`, and `horcrx graft` exactly as specified here unless operator-approved ADR changes land first.
