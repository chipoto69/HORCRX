# Marketplace architecture

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

HORCRX marketplace architecture treats the **vessel** as the product and treats discovery, payment, and trust as supporting surfaces around a content-addressed manifest CID. The marketplace therefore sits above the protocol objects in `specs/protocol/PROTOCOL.md`, preserves the x402-first payment posture in `specs/protocol/payment-layer.md`, and keeps the canonical HORCRX registry separate from external service mirrors such as Bazaar. Sources: `specs/protocol/PROTOCOL.md`, `specs/protocol/payment-layer.md`, `specs/protocol/interop.md`, `research/03-competitive-positioning.md`.

## 1. Design goals

1. Sell and fork **portable vessels**, not just hosted endpoints.
2. Preserve manifest-CID authority even when listings are mirrored elsewhere.
3. Support both **agent-native** and **human-facing** buying flows.
4. Keep payment, lineage, and trust evidence auditable enough for later Hermes install and royalty attribution.

These goals inherit the local split between service discovery and vessel packaging, the x402 settlement thesis, and the Hermes audit requirement. Sources: `research/02-prior-art.md`, `research/04-economic-thesis.md`, `specs/hermes-binding/BINDING.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`.

## 2. Service map

| Service | Primary responsibility | Key inputs | Key outputs |
|---|---|---|---|
| **registry indexer** | ingest on-chain ownership and listing pointer events into a queryable registry mirror | adapter events, manifest CID, owner reference | searchable registry rows, listing state, provenance cache |
| **content gateway** | resolve and cache slot payloads from IPFS, Arweave, or future CESS mirrors | manifest CID, slot CID, access policy | redacted previews, bundle fetches, cache receipts |
| **signing service** | verify Ed25519 and secp256k1 signatures across manifests, slots, attestations, and review badges | manifests, slot blobs, attestation payloads | verification verdicts, signer metadata, provenance warnings |
| **payment gateway** | run x402-compatible challenge, verification, and purchase evidence recording across Base and Solana adapters | listing ID, payer, settlement proof | purchase receipt, access grant, audit evidence |
| **fork/royalty resolver** | compute derivative-pays-parent obligations from `parent_cids[]` and royalty policy | manifest lineage, sale event, royalty graph | payout plan, lineage proof, payable destinations |
| **search/discovery** | offer semantic, faceted, and trust-aware browse/search over vessels and preservation artifacts | registry rows, tags, embeddings, reviews, badges | ranked results, filters, discovery analytics |
| **web UI** | human-facing listing, purchase, fork, dispute, and preservation workflows | search results, previews, wallet or checkout state | listing pages, checkout flows, account history |
| **MCP server `horcrx-marketplace`** | runtime-safe discovery and preview surface for agents | query, capability filters, signer filters | search results, preview metadata, purchase intent handoff |

The named services match the expected milestone deliverables and are drawn from the existing ATLAS marketplace shape, the protocol specs, and the mission architecture requirements. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`, `specs/protocol/marketplace-flows.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`.

## 3. Service boundaries

### 3.1 Registry indexer

The registry indexer is the read-optimized projection of canonical ownership and listing state. It does **not** replace the chain adapter or the HORCRX registry record. Its job is to make discovery fast by projecting chain events, signer facts, royalty references, and revocation state into a search-friendly store. Sources: `specs/protocol/registry-design.md`, `specs/protocol/chain-adapters.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`.

### 3.2 Content gateway

The content gateway fetches manifest and slot data from content-addressed backends, applies redaction policy, and emits preview-safe payloads. It must support public slots, encrypted slots, and preservation artifacts whose full payload is only released after payment or authorization. The gateway may hot-cache blobs, but the manifest CID remains authoritative. Sources: `specs/vessel-format/SPEC.md`, `specs/protocol/registry-design.md`, `research/05-risks-and-tensions.md`.

### 3.3 Signing service

The signing service is a verification boundary, not a custody boundary. It checks bundle signatures, per-slot signatures, trust-badge attestations, and review receipts while keeping signer identity separate from runtime installation identity. That separation is required to resist deepfake and impersonation failures. Sources: `specs/vessel-format/signing-and-lineage.md`, `research/05-risks-and-tensions.md`, `specs/hermes-binding/BINDING.md`.

### 3.4 Payment gateway

The payment gateway speaks x402-first semantics: payment challenge, proof verification, nonce/expiry enforcement, chain-adapter verification, and purchase evidence binding to manifest CID. It should inherit the client-initiated pattern already visible in the ATLAS marketplace rather than introduce subscription-style charging. Sources: `specs/protocol/payment-layer.md`, `research/02-prior-art.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`.

### 3.5 Fork/royalty resolver

The fork/royalty resolver watches derivative sales and derivative forks, computes obligations from the lineage graph, and prepares settlement instructions without mutating historical manifests. This is the service boundary where Story Protocol-style reasoning can be plugged in without making Story mandatory for the whole marketplace. Sources: `specs/protocol/PROTOCOL.md`, `research/02-prior-art.md`, `research/04-economic-thesis.md`.

### 3.6 Search/discovery

Search/discovery ranks vessels by capability, price model, signer reputation, review quality, lineage, and policy flags. It inherits practical domain vocabulary from the ATLAS marketplace backend, but adds manifest-aware filters such as fork depth, royalty target, encrypted-slot disclosure, and preservation-artifact type. Sources: `research/03-competitive-positioning.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`.

### 3.7 Web UI

The web UI is the human surface for browsing, paying, disputing, and preserving. It should consume the inherited HORCRX design system once `packages/design-system/` exists, but must remain thin over the protocol-facing services above. Human checkout may use embedded wallets or fiat-assisted rails later; the underlying listing, receipt, and lineage model stays the same. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`, `research/04-economic-thesis.md`, `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`.

### 3.8 MCP server `horcrx-marketplace`

The MCP server is the agent-facing discovery surface. It exposes read-safe methods such as `search`, `browse`, `preview`, `view-royalty-policy`, and `prepare-purchase`, while deferring irreversible payment and install steps to a host runtime approval layer such as Hermes. Sources: `specs/protocol/interop.md`, `specs/hermes-binding/BINDING.md`, `specs/protocol/marketplace-flows.md`.

## 4. End-to-end flow

```text
author / creator
  -> signing service verifies manifest + slots
  -> registry indexer records ownership pointer + listing projection
  -> search/discovery ranks and exposes result
  -> buyer reaches listing through web UI or MCP server
  -> payment gateway verifies x402 settlement
  -> content gateway releases bundle or authorized payload
  -> fork/royalty resolver attaches downstream obligations
  -> Hermes or another runtime installs with audit evidence
```

This flow preserves the distinction between publishing, paying, fetching, and installing so that payment proofs, content proofs, and runtime proofs remain independently auditable. Sources: `specs/protocol/marketplace-flows.md`, `specs/hermes-binding/BINDING.md`, `research/05-risks-and-tensions.md`.

## 5. Trust boundaries

1. **Signer authenticity** is checked by the signing service.
2. **Ownership authority** is checked by the registry and chain adapter.
3. **Payment finality** is checked by the payment gateway.
4. **Content availability** is checked by the content gateway.
5. **Derivative obligations** are checked by the fork/royalty resolver.
6. **Install provenance** is checked by the runtime audit layer.

The architecture keeps these boundaries separate because collapsing them is how replay, forgery, and persona confusion spread across the market surface. Sources: `research/05-risks-and-tensions.md`, `specs/protocol/PROTOCOL.md`, `specs/hermes-binding/BINDING.md`.

## Source paths

- `specs/protocol/PROTOCOL.md`
- `specs/protocol/payment-layer.md`
- `specs/protocol/marketplace-flows.md`
- `specs/protocol/registry-design.md`
- `specs/protocol/chain-adapters.md`
- `specs/protocol/interop.md`
- `specs/vessel-format/SPEC.md`
- `specs/vessel-format/signing-and-lineage.md`
- `specs/hermes-binding/BINDING.md`
- `research/02-prior-art.md`
- `research/03-competitive-positioning.md`
- `research/04-economic-thesis.md`
- `research/05-risks-and-tensions.md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`
- `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`
