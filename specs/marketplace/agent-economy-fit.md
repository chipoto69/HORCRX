# Agent-economy fit

Version: `v0.1-draft`

ATLAS → ORACLE → HORCRX.

HORCRX belongs in a three-layer stack already implied by the mission and the local lineage:

- **ATLAS** = knowledge supply,
- **ORACLE** = capital deployment,
- **HORCRX** = vessel supply chain.

The point of this document is to place HORCRX precisely enough that later workers do not accidentally build a second service directory, a second payment SDK, or a generic "AI marketplace" with no distinct product boundary. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`, `research/01-lineage.md`, `research/03-competitive-positioning.md`.

## 1. Stack placement

### 1.1 ATLAS — knowledge supply

ATLAS already supplies the knowledge and market substrate: x402 billing rails, registry concepts, AgentCard identity, cNFT reputation, and an existing marketplace backend. In stack terms, ATLAS is where knowledge, identity, and payment vocabulary are made legible. Sources: `research/01-lineage.md`, `research/06-local-modules-inventory.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/`.

### 1.2 ORACLE — capital deployment

ORACLE is the portfolio and capital-allocation layer implied by the mission's "capital deployment" language. It is where attention, spend, and strategy decide which knowledge assets or vessels deserve funding, distribution, or downstream automation. HORCRX should not absorb that job; it should expose vessel inventory that ORACLE-like systems can finance, license, or route toward markets. Source: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`.

### 1.3 HORCRX — vessel supply chain

HORCRX packages the tradeable unit itself: preserved agent state, preserved creative work, lineage metadata, fork rules, and portability across runtimes. It is therefore the supply chain for agent vessels and preservation artifacts, not the whole economy. Sources: `research/03-competitive-positioning.md`, `research/04-economic-thesis.md`, `specs/vessel-format/SPEC.md`.

## 2. Why this placement matters

Without the stack distinction:

- ATLAS risks being duplicated as another registry and payment surface,
- ORACLE risks being reduced to checkout logic,
- and HORCRX risks degenerating into a generic services marketplace.

With the distinction:

- ATLAS discovers and names value,
- ORACLE allocates capital toward value,
- HORCRX packages value into portable, forkable artifacts.

Sources: `research/01-lineage.md`, `research/04-economic-thesis.md`.

## 3. Positioning matrix

| Surface | What it sells or enables | Where HORCRX differs |
|---|---|---|
| **agentic.market / Bazaar** | live agent and service discovery | HORCRX sells the vessel itself; Bazaar can mirror or host services instantiated from that vessel |
| **CodeVault** | monetized code access and AI extraction toll-booth | HORCRX generalizes the pattern from code-only access to full creator or vessel preservation |
| **Faremeter** | x402-compatible payment implementation gravity | HORCRX consumes payment rails; it is not the payment rail |
| **Story Protocol** | derivative rights and licensing graph | HORCRX may attach Story-backed rights while remaining the vessel packaging and runtime-portability layer |
| **ATLAS marketplace** | current local market vocabulary and backend shape | HORCRX inherits the economic grammar but changes the product from service/item to vessel primitive |

Sources: `research/02-prior-art.md`, `research/03-competitive-positioning.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`, `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`.

## 4. Marketplace implication

Because HORCRX sits at the vessel layer:

1. one vessel can back many hosted services,
2. one purchase can unlock later runtime installs,
3. one fork can create a new supply node in the vessel economy,
4. and one preservation artifact can outlive any single UI or runtime.

That is why the marketplace architecture centers manifest CID, lineage, and trust proof instead of endpoint uptime or SaaS seat assignment. Sources: `specs/marketplace/ARCHITECTURE.md`, `specs/protocol/marketplace-flows.md`, `research/03-competitive-positioning.md`.

## 5. Economic implication

The economic thesis becomes cleaner in this stack:

- ATLAS creates legible demand through knowledge and discovery,
- ORACLE decides where capital and distribution effort go,
- HORCRX creates a tradable asset that can actually receive payment, preserve provenance, and propagate royalties.

This matches the local thesis that consumption pricing, derivative economics, and IP-as-cost-structure all need a portable asset to settle against. Sources: `research/04-economic-thesis.md`, `specs/marketplace/royalties.md`.

## Source paths

- `research/01-lineage.md`
- `research/02-prior-art.md`
- `research/03-competitive-positioning.md`
- `research/04-economic-thesis.md`
- `research/06-local-modules-inventory.md`
- `specs/vessel-format/SPEC.md`
- `specs/protocol/marketplace-flows.md`
- `specs/marketplace/ARCHITECTURE.md`
- `specs/marketplace/royalties.md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`
- `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`
