# HORCRX roadmap

ATLAS → CORPUS → HORCRX.

This roadmap turns the foundation mission into nine execution phases. Phase 0 is the foundation close; Phases 1–8 are implementation missions that should be spawned from `docs/roadmap/next-missions.md`.

## Phase 0 — foundation mission — complete

Deliverables:

- pnpm + Turbo monorepo scaffold.
- Research dossier in `research/`.
- Vessel format and protocol specs in `specs/vessel-format/` and `specs/protocol/`.
- Hermes binding in `specs/hermes-binding/`.
- Marketplace and IP architecture in `specs/marketplace/`.
- Infrastructure plan in `docs/infrastructure/`.
- Reference vessels in `examples/horcrx-001-candysoul/` and `examples/horcrx-002-orbel-pack/`.

Released `v0.1.0-foundation` 2026-05-26 and `v0.1.1` 2026-05-27.

## Mission A — horcrx-003-founder · spec-complete

Released as part of this mission. Adds the third numbered vessel (maker-not-trader, `$66.60` seed), extends vessel-format with `voice.md` / `mission.md` / `ledger.md` / `autonomy.md` slots, extends Hermes binding with the founder-vessel section, and resolves OQ-12..OQ-19. See:

- packet: `docs/roadmap/mission-A-horcrx-003-founder-vessel.md`
- vessel: `examples/horcrx-003-founder/`
- binding: `specs/hermes-binding/BINDING.md` §10

## Phase 1 — vessel CLI and Hermes export

Ship the first `horcrx` CLI: `pack`, `unpack`, `sign`, `verify`, `install`, and `graft`. Add Hermes export integration for `hermes profile export --as-vessel` and keep both reference vessels passing the manifest validator.

## Phase 2 — Base contracts, indexer, and Faremeter x402 wiring

Implement Base ownership contracts, royalty declarations, a local registry indexer, and Faremeter-compatible x402 challenge and verification flows.

## Phase 3 — web marketplace UI

Build the human marketplace surface using the inherited HORCRX design system, with embedded-wallet evaluation through Crossmint or Privy.

## Phase 4 — marketplace MCP and Hermes skill

Expose `horcrx-marketplace` as an MCP server and add the `vessel-marketplace` Hermes skill for agent-side search, preview, purchase approval, and install routing.

## Phase 5 — Solana adapter parity

Port Solana adapter behavior from the ATLAS `knowledge-horcrux` worktree into a first-class HORCRX adapter with Metaplex Core or cNFT evaluation retained.

## Phase 6 — fork graph and royalty propagation

Implement derivative lineage, parent CID tracking, royalty split resolution, and Story Protocol-style integration seams.

## Phase 7 — IP-preservation product surface

Add a notarization-first product surface for non-agent creators: code authors, writers, designers, and voice owners.

## Phase 8 — marketplace go-to-market

List HORCRX-compatible services on agentic.market Bazaar, publish the ORBEL pack as the first multi-vessel catalog item, and run partner pilot onboarding.

## Spec index for cross-area validation

- `specs/vessel-format/SPEC.md`
- `specs/vessel-format/manifest.schema.json`
- `specs/vessel-format/soul-md.schema.md`
- `specs/vessel-format/dreams-md.schema.md`
- `specs/vessel-format/intuition-md.schema.md`
- `specs/vessel-format/traces-format.md`
- `specs/vessel-format/memory-split.md`
- `specs/vessel-format/signing-and-lineage.md`
- `specs/vessel-format/compatibility-matrix.md`
- `specs/protocol/PROTOCOL.md`
- `specs/protocol/payment-layer.md`
- `specs/protocol/chain-adapters.md`
- `specs/protocol/identity-and-keys.md`
- `specs/protocol/registry-design.md`
- `specs/protocol/marketplace-flows.md`
- `specs/protocol/interop.md`
- `specs/hermes-binding/BINDING.md`
- `specs/hermes-binding/strip-and-rehydrate.md`
- `specs/hermes-binding/open-questions-resolved.md`
- `specs/marketplace/ARCHITECTURE.md`
- `specs/marketplace/ip-preservation.md`
- `specs/marketplace/royalties.md`
- `specs/marketplace/agent-economy-fit.md`
- `specs/marketplace/discovery-and-trust.md`
