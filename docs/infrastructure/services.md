---
title: Infrastructure services
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Infrastructure services

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

HORCRX infrastructure should stay deliberately small in the first implementation phase: a thin set of services around a content-addressed vessel manifest, with trust-sensitive signing and secret mediation kept separate from public fetch and discovery surfaces. The goal is not to recreate ATLAS' entire runtime, but to project just enough registry, payment, storage, and search infrastructure to publish, buy, verify, and install vessels safely. Sources: `specs/marketplace/ARCHITECTURE.md`, `specs/protocol/payment-layer.md`, `specs/hermes-binding/BINDING.md`, `research/02-prior-art.md`, `research/05-risks-and-tensions.md`.

## 1. Design rules

1. **Registry truth stays split.** On-chain ownership and listing pointers remain canonical; the registry indexer is a read-optimized projection only. Sources: `specs/protocol/registry-design.md`, `specs/protocol/chain-adapters.md`.
2. **Content is CID-first.** Gateways may cache or pin, but bundle integrity is always re-checked against manifest CID and slot CIDs. Sources: `specs/vessel-format/SPEC.md`, `specs/vessel-format/signing-and-lineage.md`.
3. **Signer, payer, and installer stay distinct.** A vessel author, a marketplace buyer, and a Hermes runtime installer are separate actors with separate audit surfaces. Sources: `specs/hermes-binding/BINDING.md`, `research/05-risks-and-tensions.md`.
4. **Secrets never live in vessel infrastructure by default.** The signing surface can verify signatures; the gateway can serve bundles; neither should become a generic secret store. Sources: `~/wiki/raw/downloads/2026-04-10/root/system-map.md`, `~/wiki/_meta/hermes-stack/hermes-content-os.md`. <!-- wiki source -->

## 2. Service catalog

| Service | Purpose | Key inputs | Key outputs | Dependencies | Scaling notes |
|---|---|---|---|---|---|
| **registry indexer** | Project Base and Solana ownership/listing events into a queryable store for search, listing pages, and royalty resolution. | adapter events, manifest CID, owner reference, revocation events | normalized listing rows, ownership cache, lineage lookup rows | Base adapter, Solana adapter, sqlite/postgres store, search index | Start with one writer + one read replica pattern; split chain ingestion workers only after event volume grows. Sources: `specs/protocol/registry-design.md`, `specs/protocol/chain-adapters.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py` |
| **content gateway** | Resolve manifests and slot blobs from IPFS, Arweave, and future mirrors while enforcing preview/redaction policy. | manifest CID, slot CID, access policy, cache key | preview metadata, authorized bundle download, cache receipt | IPFS pinning provider, Arweave/Irys mirror, R2 hot cache | Keep stateless if possible; scale horizontally behind CDN/cache. Sources: `specs/marketplace/ARCHITECTURE.md`, `specs/vessel-format/SPEC.md`, `research/02-prior-art.md` |
| **IPFS pinning surface** | Keep hot-path bundle data reachable through managed pinning while preserving content addressing. Preferred early providers: `web3.storage` or Pinata. | bundle or slot blobs, retention policy, billing metadata | pin status, provider object IDs, retrieval gateway hints | content gateway, operator billing account | Treat provider choice as replaceable; never encode provider IDs into manifest semantics. Sources: `research/02-prior-art.md`, `https://web3.storage/pricing/`, `https://pinata.cloud/pricing` |
| **Arweave bundler** | Push final signed bundles or preservation artifacts into permanent storage via Irys-backed uploads. | signed bundle, manifest CID, retention class, funder identity | permanent transaction reference, mirror receipt | Irys, content gateway, signing workflow | Low write frequency but high durability importance; isolate retries and funding state. Sources: `research/02-prior-art.md`, `https://irys.xyz/`, `https://docs.irys.xyz/build/d/guides/uploading-nfts` |
| **signing service** | Verify manifest and slot signatures and optionally mediate detached signing in an isolated trust boundary. | manifest bytes, slot blobs, signer metadata, attestation request | verification verdict, signer fingerprint, signed digest record | key custody boundary, audit sink, transparency-log adapter (optional) | Keep small and isolated; scale reads separately from privileged signing operations. Sources: `specs/vessel-format/signing-and-lineage.md`, `specs/hermes-binding/BINDING.md`, `research/05-risks-and-tensions.md` |
| **x402 facilitator** | Serve payment challenge/verify flows and produce purchase evidence compatible with Base and Solana adapters. Faremeter is the first TS helper to evaluate. | listing ID, manifest CID, payer identity, settlement proof, nonce/expiry | purchase receipt, verification status, replay-protection state | chain adapters, registry indexer, audit sink | Mostly compute-light but latency-sensitive; keep nonce store durable and low-latency. Sources: `specs/protocol/payment-layer.md`, `research/02-prior-art.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`, `~/wiki/raw/reader/Index - Faremeter*.md` | <!-- wiki source -->
| **search / embedding index** | Support faceted and semantic vessel discovery over registry rows, reviews, tags, lineage, and policy flags. | normalized listings, text metadata, trust badges, review events | ranked search results, related-vessel suggestions, trust filters | registry indexer, content gateway preview metadata, embedding worker | Start with sqlite or Postgres FTS plus optional embeddings; split embedding jobs from online queries. Sources: `specs/marketplace/ARCHITECTURE.md`, `research/03-competitive-positioning.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/openapi.json` |
| **CESS evaluation lane** | Evaluate whether CESS becomes a secondary decentralized mirror for large bundles or human-IP archives. | bundle size profile, durability target, retrieval SLO, legal region constraints | go / no-go recommendation, mirror policy, cost comparison | content gateway, registry metadata, future storage adapter | Keep out of the first shipping path; treat as a storage policy experiment until retrieval and tooling maturity are proven. Sources: `research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md` |

## 3. Recommended first implementation topology

### 3.1 Public plane

These can face the internet behind CDN or WAF controls:

- registry indexer read API
- content gateway
- search/discovery API
- web UI and brand site

### 3.2 Controlled service plane

These should stay behind private networking or operator-only access:

- signing service
- x402 facilitator admin surface
- indexer write workers
- Arweave/Irys upload worker

### 3.3 Trust-sensitive boundaries

These must stay isolated from general browsing and preview traffic:

- signing keys
- payment nonce and replay-protection store
- export/import approval logic for Hermes-hosted installs

This split follows the system-map doctrine that the runtime mind, the public interaction plane, and the secret boundary must not collapse into one host process. Sources: `~/wiki/raw/downloads/2026-04-10/root/system-map.md`, `~/wiki/_meta/hermes-stack/hermes-content-os.md`. <!-- wiki source -->

## 4. CESS position

CESS should be framed as an **optional mirror tier**, not a required first release dependency.

Use it only if all three conditions become true:

1. bundle sizes grow enough that multi-provider redundancy materially lowers risk,
2. retrieval latency is acceptable for preview and install flows, and
3. operational tooling is stable enough that a future worker can document it without inventing a bespoke storage stack.

Until then, HORCRX can ship with the simpler split:

- IPFS pinning for the hot path,
- Arweave/Irys for permanent anchoring,
- R2 for fast cache and edge delivery.

## Source paths

- `specs/marketplace/ARCHITECTURE.md`
- `specs/protocol/payment-layer.md`
- `specs/protocol/registry-design.md`
- `specs/protocol/chain-adapters.md`
- `specs/vessel-format/SPEC.md`
- `specs/vessel-format/signing-and-lineage.md`
- `specs/hermes-binding/BINDING.md`
- `research/02-prior-art.md`
- `research/03-competitive-positioning.md`
- `research/05-risks-and-tensions.md`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/openapi.json`
- `~/wiki/raw/downloads/2026-04-10/root/system-map.md` <!-- wiki source -->
- `~/wiki/_meta/hermes-stack/hermes-content-os.md` <!-- wiki source -->
- `~/wiki/raw/reader/Index - Faremeter*.md` <!-- wiki source -->
- `https://www.hetzner.com/cloud/regular-performance`
- `https://web3.storage/pricing/`
- `https://pinata.cloud/pricing`
- `https://irys.xyz/`
- `https://docs.irys.xyz/build/d/guides/uploading-nfts`
