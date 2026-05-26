# Worker F04 — marketplace-ip — Completion Report

## Branch
foundation/marketplace

## Changed files (absolute paths)
- /Users/rudlord/HORCRX/specs/marketplace/ARCHITECTURE.md
- /Users/rudlord/HORCRX/specs/marketplace/ip-preservation.md
- /Users/rudlord/HORCRX/specs/marketplace/royalties.md
- /Users/rudlord/HORCRX/specs/marketplace/agent-economy-fit.md
- /Users/rudlord/HORCRX/specs/marketplace/discovery-and-trust.md
- /Users/rudlord/HORCRX/WORKER-COMPLETE.md

## Assertions claimed
- VAL-MARKETPLACE-01
- VAL-MARKETPLACE-02
- VAL-MARKETPLACE-03
- VAL-MARKETPLACE-04
- VAL-MARKETPLACE-05
- VAL-MARKETPLACE-06

## Acceptance criteria met
- [x] Authored `specs/marketplace/ARCHITECTURE.md` covering registry indexer, content gateway, signing service, payment gateway, fork/royalty resolver, search/discovery, web UI, and MCP server.
- [x] Authored `specs/marketplace/ip-preservation.md` covering both human creative work and agent-vessel preservation with notarization, content-addressing, optional ZK proof, and dispute workflow.
- [x] Authored `specs/marketplace/royalties.md` covering fork lineage tracking, derivative-pays-parent rules, default 70/20/10 split, and optional Story Protocol integration.
- [x] Authored `specs/marketplace/agent-economy-fit.md` placing HORCRX in the ATLAS → ORACLE → HORCRX stack and positioning it against adjacent surfaces.
- [x] Authored `specs/marketplace/discovery-and-trust.md` covering review flows, inherited reputation cNFTs, trust badges, and anti-deepfake controls.

## Known risks / unresolved
- F07 still needs to wire top-level README and roadmap references so the new marketplace specs are surfaced in cross-area navigation.
- The ORACLE layer is mission-defined but not yet canonized in a dedicated repo-local spec, so later roadmap work should preserve this placement language consistently.

## HITL required before next stage
- Confirm whether 70/20/10 remains the implementation default or becomes a different business default before contract work starts.
- Confirm whether KYC-light trust controls should ship in the first public marketplace phase or stay enterprise-only.

## Blocking findings (if any)
- None.

## Source dossier read
- /Users/rudlord/HORCRX/research/02-prior-art.md
- /Users/rudlord/HORCRX/research/03-competitive-positioning.md
- /Users/rudlord/HORCRX/research/04-economic-thesis.md
- /Users/rudlord/HORCRX/research/05-risks-and-tensions.md
- /Users/rudlord/HORCRX/specs/protocol/PROTOCOL.md
- /Users/rudlord/HORCRX/specs/protocol/payment-layer.md
- /Users/rudlord/HORCRX/specs/protocol/marketplace-flows.md
- /Users/rudlord/HORCRX/specs/protocol/interop.md
- /Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md
- /Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py
- /Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/reputation/cnft.py
- /Users/rudlord/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md
- /Users/rudlord/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md

## Next worker hand-off
- F05 should reuse the marketplace service boundaries and trust model when writing infrastructure and security docs.
- F07 should link every file in `specs/marketplace/` from repo-level navigation and cross-area validation artifacts.
- Future implementation workers should keep ATLAS reputation badges and x402 payment semantics inherited rather than inventing replacement systems.
