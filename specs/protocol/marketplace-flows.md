# Marketplace flows

Version: `v0.1-draft`

This document defines the user-facing verbs the protocol must support while staying neutral on exact UI or service architecture.

## 1. list

The current owner publishes a listing that binds:

- manifest CID,
- price or pricing model,
- accepted settlement rail,
- royalty policy,
- disclosure level for encrypted slots.

## 2. discover

Buyers search by capability, role, signer, lineage, price, or trust signals. Discovery is read-only until payment intent begins.

## 3. purchase

A buyer satisfies the payment challenge, the adapter verifies settlement, and the marketplace records a purchase receipt tied to the manifest CID.

## 4. transfer

Ownership changes without changing the vessel payload. Transfer may be sale-driven or direct custody handoff.

## 5. fork

A buyer or licensed actor creates a new manifest with `parent_cids[]` populated, new signatures attached, and derivative royalty rules inherited or extended.

## 6. unlist

The owner removes the active public listing while keeping the underlying registry record and historical provenance intact.

## 7. revoke

An author, owner, or policy authority marks a record, attestation, or public listing as revoked. Revocation never erases history; it adds a new signed state.

## 8. Buyer modes

- **agent buyer** — uses x402-compatible in-band purchase flows and leaves audit evidence;
- **human buyer** — uses a hosted market surface, then receives the manifest pointer or bundle access according to policy.

## 9. Source paths

- `/Users/rudlord/HORCRX/research/03-competitive-positioning.md`
- `/Users/rudlord/HORCRX/research/04-economic-thesis.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/wiki/entities/atlas-marketplace.md`
