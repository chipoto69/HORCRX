# HORCRX next missions

ATLAS → CORPUS → HORCRX.

Each section below is scoped to be spawnable without re-mining the foundation research. All missions inherit the universal off-limits: no live Hermes-profile writes, no ATLAS worktree writes, no secrets in repo files, no remote push unless the mission explicitly assigns publishing.

## Phase 1 — vessel CLI and Hermes export

### Mission
Build the `horcrx` CLI for folder ↔ bundle workflows and integrate Hermes export/import seams without modifying existing profiles in place.

### Acceptance criteria
- `horcrx pack`, `unpack`, `sign`, `verify`, `install`, and `graft` exist with fixture tests.
- `hermes profile export --as-vessel <name>` produces a manifest-valid folder or `.horcrx` bundle with secrets stripped.
- Both reference vessels validate against `specs/vessel-format/manifest.schema.json`.
- Install writes a new profile target and defaults cron jobs to disabled.
- The iteration-budget tension flagged by F03 is explicitly resolved: mission doctrine says subagents share the parent budget per Hermes constraint #12, while `~/.hermes/hermes-agent/agent/iteration_budget.py` currently documents independent per-subagent caps that can exceed the parent's total. Phase 1 must decide whether HORCRX follows mission doctrine, mirrors current upstream runtime behavior, or lands an upstream Hermes patch; the current foundation ADR 11 chooses shared effective caps as HORCRX policy and requires Phase 1 to verify or patch runtime behavior accordingly.
- Audit item: expand or preserve `specs/hermes-binding/BINDING.md` §9 as a 14-row table matching the §8 hard-constraints table, with each row confirming or flagging the vessel spec for audit-friendliness.

### Off-limits
- Do not mutate any existing Hermes profile; export is read-only and import creates a new profile target.
- Do not write credentials into fixtures or generated bundles.
- Do not deploy contracts or publish packages.

### Recommended worker topology
- Builder: CLI implementation and packaging.
- Hermes specialist: export/import/graft integration review.
- Evaluator/evolver: fixture round-trip, secret-stripping, and manifest validation.

## Phase 2 — Base contracts, indexer, and Faremeter x402 wiring

### Mission
Implement the Base adapter baseline: ERC-721 ownership, ERC-2981 royalties, local registry projection, and Faremeter-compatible x402 payment challenge verification.

### Acceptance criteria
- Local anvil flow publishes, lists, transfers, and revokes a vessel record.
- Royalty metadata is queryable through the adapter boundary.
- Faremeter-style challenge and verify flow records nonces and receipts.
- Indexer separates on-chain pointer state from off-chain manifest content.

### Off-limits
- No mainnet or testnet deploy.
- No paid RPC dependency.
- No Solana implementation beyond adapter-interface parity tests.

### Recommended worker topology
- Contract worker.
- Indexer/payment worker.
- Security reviewer for replay and royalty edge cases.

## Phase 3 — web marketplace UI

### Mission
Build the human-facing marketplace UI using the inherited design system without redesigning brand assets.

### Acceptance criteria
- Browse, detail, preview, and purchase-intent screens exist.
- UI consumes manifest and listing fixtures from the Phase 2 indexer.
- Crossmint or Privy integration is evaluated behind a mock adapter before live keys exist.
- Accessibility and brand-voice review passes.

### Off-limits
- Do not edit inherited design-system canon except through explicit brand tasks.
- Do not connect live wallets or live payment keys.

### Recommended worker topology
- Frontend builder.
- Design-system reviewer.
- QA/browser validator.

## Phase 4 — marketplace MCP and Hermes skill

### Mission
Expose vessel discovery to agents through an MCP server and a Hermes skill.

### Acceptance criteria
- `horcrx-marketplace` MCP supports search, view, preview, and purchase-intent tools.
- `vessel-marketplace` skill routes irreversible purchases through approval and dispatch audit.
- Agent-side install calls the Phase 1 CLI rather than writing profile files directly.

### Off-limits
- No autonomous purchase without approval.
- No bypass around Hermes `dispatch()` audit.

### Recommended worker topology
- MCP builder.
- Hermes skill builder.
- Audit/security validator.

## Phase 5 — Solana adapter parity

### Mission
Port the Solana adapter surface from the ATLAS prototype while keeping Base/Solana symmetry.

### Acceptance criteria
- Local `solana-test-validator` flow publishes or updates a registry/provenance record.
- Metaplex Core baseline and cNFT extension remain documented and test-covered.
- x402 proof verification handles Solana transaction and memo nonce semantics.
- `knowledge-horcrux` Solana modules are ported only through clean HORCRX package boundaries.

### Off-limits
- No devnet/mainnet deploy.
- Do not modify the ATLAS prototype worktree.

### Recommended worker topology
- Solana adapter builder.
- Protocol parity reviewer.
- Replay/security validator.

## Phase 6 — fork graph and royalty propagation

### Mission
Implement lineage graph persistence, derivative-pays-parent settlement, and Story Protocol-style integration seams.

### Acceptance criteria
- Forked manifests preserve parent CIDs.
- Royalty resolution supports default 70/20/10 and custom splits.
- Dispute and revocation events do not delete history.
- Story Protocol option remains adapter-level, not mandatory core protocol.

### Off-limits
- No final tokenomics decision without operator sign-off.
- No irreversible royalty contract deploy.

### Recommended worker topology
- Lineage/indexer builder.
- Economics reviewer.
- Protocol/security validator.

## Phase 7 — IP-preservation product surface

### Mission
Create the preservation-only surface for human creative work using the same vessel primitive.

### Acceptance criteria
- Notarization-only flow accepts writing, design, code, and voice artifacts as preservation manifests.
- Content-addressed storage and optional ZK ownership proof seams are present.
- Takedown and dispute workflow is documented and testable.
- Agent-vessel and human-work flows share registry primitives without collapsing their product language.

### Off-limits
- No legal claims beyond recorded provenance and policy text.
- No paid permanent-storage writes by default.

### Recommended worker topology
- Product/backend builder.
- Policy reviewer.
- UX validator.

## Phase 8 — marketplace go-to-market

### Mission
Prepare HORCRX for first public listings and partner pilots.

### Acceptance criteria
- ORBEL pack is listed as the first multi-vessel catalog item.
- agentic.market Bazaar integration path is exercised for service discovery without fragmenting the canonical HORCRX registry.
- Partner-pilot checklist covers onboarding, risk review, support, and rollback.
- Metrics distinguish vessel sales, service activations, forks, and preservation-only notarizations.

### Off-limits
- No public launch without operator approval.
- No claims of production readiness unless Phase 1–7 validators are green.

### Recommended worker topology
- Marketplace operator.
- Partnerships/docs worker.
- Launch-risk evaluator.
