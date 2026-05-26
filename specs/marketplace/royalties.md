# Royalties

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

HORCRX royalties are downstream consequences of vessel lineage, not separate metadata bolted on after the fact. Every derivative sale or paid fork starts from `parent_cids[]`, resolves a royalty policy, and produces settlement evidence that later installs and audits can trace back to the same manifest family. Sources: `specs/protocol/PROTOCOL.md`, `specs/vessel-format/manifest.schema.json`, `research/04-economic-thesis.md`.

## 1. Principles

1. **Fork lineage tracking** is mandatory for paid derivatives.
2. **Derivative-pays-parent** is the default economic rule.
3. Revenue splits are configurable, but the marketplace ships a documented default.
4. Royalty resolution should work without Story Protocol, while remaining compatible with Story when stronger IP rails are desired.
5. Registry and runtime history remain append-only; payouts are derived from evidence rather than historical mutation.

These principles directly answer the local economic and IP-preservation thesis that portable assets need explicit derivative economics or they collapse into unpaid scraping. Sources: `research/04-economic-thesis.md`, `research/05-risks-and-tensions.md`, `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`.

## 2. Lineage model

### 2.1 Parent CIDs

Each derivative vessel carries one or more `parent_cids[]` in its manifest. That list is the minimum proof needed to:

- attribute ancestry,
- determine which creators are in the payout path,
- and explain why a derivative owes a royalty at all.

The parent list may represent:

- a clean one-parent fork,
- a multi-parent graft or pack,
- or a transformed preservation artifact that remixes human and agent-originated material.

Sources: `specs/vessel-format/manifest.schema.json`, `specs/vessel-format/signing-and-lineage.md`, `specs/protocol/PROTOCOL.md`.

### 2.2 Royalty graph

The marketplace materializes a royalty graph from:

- child manifest CID,
- immediate `parent_cids[]`,
- each node's royalty policy,
- each node's payout target,
- optional graph-depth cap,
- and any explicit exclusions permitted by policy.

The resolver should default to paying the direct parent path first, then continue upward only when the relevant policy says multi-hop propagation is allowed. That avoids infinite or surprising payout chains. Sources: `specs/marketplace/ARCHITECTURE.md`, `research/05-risks-and-tensions.md`.

## 3. Default split

The documented default is **70/20/10**:

- **70% creator** — primary author or immediate vessel seller,
- **20% resonators** — upstream contributors, curators, or direct lineage participants named by policy,
- **10% protocol** — marketplace and preservation infrastructure.

This 70/20/10 split comes from the sorrywecan precedent surfaced in the research and should be treated as a default starting point, not an immutable law. A listing may override the percentages so long as:

- the override is disclosed before purchase,
- the payout graph is machine-readable,
- and derivative obligations remain explicit.

Sources: `research/04-economic-thesis.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md`.

## 4. Settlement events

Royalty resolution is triggered by:

1. **primary sale** of a paid vessel or preservation artifact,
2. **paid transfer** where the active policy charges resale royalties,
3. **fork creation fee** when a licensed derivative is minted,
4. **usage-linked payout** when a hosted derivative routes x402-metered revenue back to ancestors.

Not every vessel needs every event class. The important rule is that the chosen event classes are declared in policy and evaluated consistently. Sources: `research/04-economic-thesis.md`, `specs/protocol/payment-layer.md`.

## 5. Configurable policy surface

Each royalty policy should minimally declare:

| Field | Meaning |
|---|---|
| `policy_id` | stable identifier for the royalty rule |
| `payout_target` | default destination or split contract root |
| `derivative_pays_parent` | boolean or explicit mode |
| `graph_depth` | number of ancestor hops eligible for payout |
| `sale_events` | which marketplace events trigger payout |
| `split_override` | optional alternative to 70/20/10 |
| `exclusions` | allowed exceptions such as zero-fee archival transfers |
| `story_binding` | optional external Story Protocol reference |

This keeps a clear seam between protocol-level lineage facts and marketplace-level payout behavior. Sources: `specs/protocol/PROTOCOL.md`, `specs/marketplace/ARCHITECTURE.md`.

## 6. Story Protocol integration option

Story Protocol is an **optional** licensing rail for creators who want stronger legal and ecosystem integration around derivative rights. When enabled:

- the HORCRX manifest CID remains the vessel authority,
- the Story record acts as a linked rights graph,
- and the marketplace can use Story references during dispute resolution or payout verification.

When disabled, HORCRX still supports native royalty policies using its own lineage graph and x402-compatible purchase evidence. Story therefore adds weight; it does not become a hard dependency. Sources: `research/02-prior-art.md`, `research/03-competitive-positioning.md`, `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`.

## 7. Chain realization

### Base

Base-side settlement should prefer a standard royalty-aware surface such as ERC-2981 paired with split-routing logic similar to 0xSplits-style distribution. This keeps the public ownership surface legible while still paying multiple recipients. Sources: `specs/protocol/chain-adapters.md`, `research/02-prior-art.md`.

### Solana

Solana-side settlement should use a compressed or lightweight split-account pattern so derivative payouts remain cheap relative to small x402-mediated purchase amounts. This matters more for high-volume, lower-ticket preservation and agent-commerce flows. Sources: `specs/protocol/chain-adapters.md`, `research/02-prior-art.md`.

## 8. Runtime attribution

If a purchased vessel is later installed into Hermes or another runtime, install and audit records should preserve:

- installed vessel CID,
- ancestor CIDs,
- payout target,
- and the policy ID used at the moment of purchase or graft.

That creates a clean bridge between marketplace economics and runtime provenance. Sources: `specs/hermes-binding/BINDING.md`, `specs/marketplace/ARCHITECTURE.md`.

## Source paths

- `research/02-prior-art.md`
- `research/03-competitive-positioning.md`
- `research/04-economic-thesis.md`
- `research/05-risks-and-tensions.md`
- `specs/protocol/PROTOCOL.md`
- `specs/protocol/payment-layer.md`
- `specs/protocol/chain-adapters.md`
- `specs/vessel-format/manifest.schema.json`
- `specs/vessel-format/signing-and-lineage.md`
- `specs/hermes-binding/BINDING.md`
- `specs/marketplace/ARCHITECTURE.md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md`
- `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`
