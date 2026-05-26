# Payment layer

Version: `v0.1-draft`

HORCRX is **x402-first**. Payment is treated as a protocol surface, not as an afterthought checkout modal.

## 1. Why x402 is the first rail

The strongest local implementation gravity already lives in `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`, where the existing gateway, nonce manager, pricing helpers, and verifier registry define the current payment semantics. The research canon in `/Users/rudlord/HORCRX/research/02-prior-art.md` and `/Users/rudlord/HORCRX/research/04-economic-thesis.md` points to the same direction.

## 2. Required semantics

A HORCRX payment layer implementation MUST preserve the following ideas:

- HTTP-native payment challenge/response,
- replay resistance through nonce plus expiry,
- a chain adapter that validates settlement,
- typed evidence linking a purchase to a manifest CID,
- auditability for both operator and runtime.

## 3. Settlement posture

- **EVM settlement** is handled through the Base adapter.
- **Solana settlement** is handled through the Solana adapter.
- The abstract payment layer treats both as peers.
- Any future adapter must satisfy the same x402-style proof contract.

## 4. Faremeter role

`Faremeter` is the most concrete TypeScript-side payment helper surfaced in the local research. HORCRX does not depend on it at the protocol layer, but future implementations SHOULD evaluate it first for x402-compatible client and facilitator flows.

## 5. Purchase evidence model

A successful purchase should bind:

- manifest CID,
- listing ID,
- payer identity,
- payee or settlement destination,
- chain/network,
- proof nonce,
- proof expiry,
- verified transaction reference.

## 6. Audit expectations

The payment layer must be compatible with Hermes-style auditable dispatch. Agent-side purchase flows should leave enough evidence to attribute later installs or royalty payouts.

## 7. Source paths

- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/`
- `/Users/rudlord/HORCRX/research/02-prior-art.md`
- `/Users/rudlord/HORCRX/research/04-economic-thesis.md`
- `/Users/rudlord/wiki/concepts/x402-protocol.md`
- `/Users/rudlord/wiki/raw/reader/Index - Faremeter*.md`
