# Worker F02 — protocol-spec — Completion Report

## Branch
foundation/protocol

## Changed files (absolute paths)
- /Users/rudlord/HORCRX/specs/vessel-format/SPEC.md
- /Users/rudlord/HORCRX/specs/vessel-format/manifest.schema.json
- /Users/rudlord/HORCRX/specs/vessel-format/soul-md.schema.md
- /Users/rudlord/HORCRX/specs/vessel-format/dreams-md.schema.md
- /Users/rudlord/HORCRX/specs/vessel-format/intuition-md.schema.md
- /Users/rudlord/HORCRX/specs/vessel-format/traces-format.md
- /Users/rudlord/HORCRX/specs/vessel-format/memory-split.md
- /Users/rudlord/HORCRX/specs/vessel-format/signing-and-lineage.md
- /Users/rudlord/HORCRX/specs/vessel-format/compatibility-matrix.md
- /Users/rudlord/HORCRX/specs/protocol/PROTOCOL.md
- /Users/rudlord/HORCRX/specs/protocol/payment-layer.md
- /Users/rudlord/HORCRX/specs/protocol/chain-adapters.md
- /Users/rudlord/HORCRX/specs/protocol/identity-and-keys.md
- /Users/rudlord/HORCRX/specs/protocol/registry-design.md
- /Users/rudlord/HORCRX/specs/protocol/marketplace-flows.md
- /Users/rudlord/HORCRX/specs/protocol/interop.md
- /Users/rudlord/HORCRX/examples/horcrx-001-candysoul/...
- /Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/...
- /Users/rudlord/HORCRX/WORKER-COMPLETE.md

## Assertions claimed
- VAL-VESSEL-01
- VAL-VESSEL-02
- VAL-VESSEL-03
- VAL-VESSEL-04
- VAL-VESSEL-05
- VAL-VESSEL-06
- VAL-VESSEL-07
- VAL-VESSEL-08
- VAL-VESSEL-09
- VAL-VESSEL-10
- VAL-VESSEL-11
- VAL-VESSEL-12
- VAL-VESSEL-14
- VAL-PROTOCOL-01
- VAL-PROTOCOL-02
- VAL-PROTOCOL-03
- VAL-PROTOCOL-04
- VAL-PROTOCOL-05
- VAL-PROTOCOL-06
- VAL-PROTOCOL-07
- VAL-PROTOCOL-08
- VAL-PROTOCOL-09
- VAL-PROTOCOL-10

## Acceptance criteria met
- [x] Authored canonical vessel-format specs covering folder and `.horcrx` bundle representations.
- [x] Authored manifest JSON Schema extending the AgentCard surface rather than replacing it.
- [x] Authored protocol specs for abstract lifecycle, payments, chain adapters, identity, registry design, flows, and interop.
- [x] Created conformant reference examples for `HORCRX #001 · candysoul` and `HORCRX #002 · orbel-pack`.
- [x] Kept the abstract protocol chain-agnostic while giving Base and Solana symmetric adapter treatment.

## Known risks / unresolved
- F03 still needs to lock the exact Hermes export/import/graft commands and resolve the 10 open binding ADRs before any implementation phase freezes behavior.
- The pack example is intentionally minimal; later workers may want richer child slots once Hermes binding and marketplace specs are canonized.

## HITL required before next stage
- Confirm whether the default derivative royalty split remains 70/20/10 or becomes a different policy before contract implementation.
- Confirm whether Sigstore transparency logging is optional for v1 or required for public marketplace publication.

## Blocking findings (if any)
- None.

## Source dossier read
- /Users/rudlord/HORCRX/research/INDEX.md
- /Users/rudlord/HORCRX/research/00-vault-recon.md
- /Users/rudlord/HORCRX/research/01-lineage.md
- /Users/rudlord/HORCRX/research/02-prior-art.md
- /Users/rudlord/HORCRX/research/03-competitive-positioning.md
- /Users/rudlord/HORCRX/research/04-economic-thesis.md
- /Users/rudlord/HORCRX/research/05-risks-and-tensions.md
- /Users/rudlord/HORCRX/research/06-local-modules-inventory.md
- /Users/rudlord/HORCRX/research/07-skill-ecosystem-inventory.md
- /Users/rudlord/HORCRX/research/08-knowledge-graph-context.md
- /Users/rudlord/HORCRX/research/09-hermes-binding-recon.md
- /Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md

## Next worker hand-off
- F03 should cross-check every vessel slot and example against the 14 Hermes hard constraints and finalize the strip/rehydrate contract.
- F04 should reuse `specs/protocol/payment-layer.md`, `specs/protocol/marketplace-flows.md`, and the example manifests when defining marketplace architecture.
- F07 should wire root docs and roadmap references to every file created in `specs/` and `examples/` during cross-area validation.
