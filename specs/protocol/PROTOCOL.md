# HORCRX Protocol v0.1

Version: `v0.1`

ATLAS → CORPUS → HORCRX.

HORCRX is a chain-agnostic protocol for identifying, transferring, forking, and attesting to portable vessels. The abstract protocol describes invariants and lifecycle verbs without hardcoding Base-only or Solana-only assumptions.

## 1. Protocol objects

- **vessel** — a signed manifest plus its slot bodies.
- **pack** — a signed manifest that composes multiple vessels.
- **registry record** — the ownership and discovery pointer for a vessel manifest CID.
- **attestation** — a signed statement about authenticity, compatibility, or review state.
- **royalty policy** — the derivative payment rules attached to a lineage branch.

## 2. Protocol invariants

1. The canonical artifact is addressed by manifest CID.
2. Ownership is separable from hosting location.
3. Every operation resolves against a chain adapter, not a hardcoded chain.
4. Secrets never form part of the traded artifact.
5. A fork preserves `parent_cids[]` lineage.
6. Revocation never deletes history; it adds a new signed state.

## 3. Lifecycle operations

### registry

Publish a new registry record containing:

- vessel ID,
- manifest CID,
- active chain adapter,
- royalty policy reference,
- current owner reference,
- optional status flags.

### discovery

Discovery surfaces index by:

- manifest CID,
- vessel ID,
- skills,
- capabilities,
- price model,
- signer identity,
- review and trust signals.

### ownership

Ownership is the current authority allowed to transfer, list, unlist, or revoke public sale state. The owner may differ from the original author.

### transfer

A transfer reassigns the owner reference while keeping the manifest CID stable.

### fork

A fork creates a new manifest CID with one or more `parent_cids[]`. Forks inherit compatible royalty rules and provenance obligations.

### royalty

Royalty resolution is evaluated during paid transfer or paid fork flows, never by mutating historical artifacts.

### attestation

Attestations are signed claims about compatibility, review state, provenance, or policy compliance.

### signature

Every published manifest and every mutable registry event must carry a verifiable signature.

### revocation

Revocation marks a registry record, listing, or attestation as no longer valid without erasing the original record.

## 4. Required protocol messages

An implementation MUST define equivalents for:

- `PublishRecord`
- `UpdateListing`
- `TransferOwnership`
- `ForkVessel`
- `AttachAttestation`
- `RevokeRecord`
- `ResolveRoyalty`

Each message binds:

- target manifest CID,
- actor key,
- adapter/network,
- timestamp or nonce,
- signature.

## 5. Chain-agnostic posture

The protocol layer does not assume:

- EVM transaction models,
- Solana account models,
- a single token standard,
- a single wallet derivation scheme,
- a single payment network.

Those decisions belong exclusively to adapter specs in `chain-adapters.md`.

## 6. Trust boundaries

- bundle authenticity is proven by signatures,
- trade authority is proven by ownership state on the selected adapter,
- content availability is proven by content-addressed fetch,
- buyer trust is strengthened by attestations, not marketing copy.

## 7. Source paths

- `/Users/rudlord/HORCRX/research/01-lineage.md`
- `/Users/rudlord/HORCRX/research/02-prior-art.md`
- `/Users/rudlord/HORCRX/research/03-competitive-positioning.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
