---
title: Security and threat model
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Security and threat model

Version: `v0.1-draft`

The security rule that matters most for HORCRX is simple: **the mind and the secrets do not live in the same trust domain**. A vessel may carry portable cognition, memory canon, skills, and lineage. It must not become a bag of credentials. Every infrastructure choice below follows from that split. Sources: `~/wiki/raw/downloads/2026-04-10/root/system-map.md`, `specs/hermes-binding/BINDING.md`, `research/05-risks-and-tensions.md`. <!-- wiki source -->

## 1. Trust domains

| Domain | What it may hold | What it must not hold |
|---|---|---|
| **Archive** | signed markdown truth, manifests, lineage metadata, public slot payloads | reusable secrets, wallet seeds, raw auth tokens |
| **Vault** | credentials, wallet keys, API tokens, rehydration material | general bundle assembly, public preview logic |
| **Nucleus / runtime host** | approvals, orchestration state, scoped session handles, audit sinks | raw Vault contents passed directly into sandbox reasoning |
| **Sandbox / LLM execution** | minimally scoped task context, approved bundle payloads, temporary working state | direct Vault access, unredacted secret stores, permanent credential copies |
| **Public marketplace plane** | listings, previews, signed public metadata, cached public blobs | export-time secrets, signing keys, privileged admin tooling |

This reproduces the system-map doctrine in marketplace form: Archive is read-mostly truth, Vault is secret isolation, Nucleus mediates access, and Sandbox never talks to Vault directly. Sources: `~/wiki/raw/downloads/2026-04-10/root/system-map.md`. <!-- wiki source -->

## 2. Threat model

### 2.1 Threat matrix

| Threat | Attacker model and capabilities | Impact | Mitigations | Residual risk |
|---|---|---|---|---|
| **Soul theft** | Attacker gains access to unsigned export staging, CI artifacts, or a compromised operator workstation before the bundle is finalized. | Identity, tone, and hard-won behavioral patterns are copied and resold or impersonated. | Sign only after allowlisted export; keep unsigned staging short-lived; require manifest diff preview before signing; never stage decrypted secret-bearing files with bundle assets. Sources: `research/05-risks-and-tensions.md`, `specs/hermes-binding/strip-and-rehydrate.md` | Public-facing vessels are still inherently copyable after release; provenance reduces harm but cannot make public cognition non-copyable. |
| **Signature forgery** | Attacker fabricates a signer identity or abuses weak/private-key handling to publish fake vessels. | Buyers install impersonated or tampered vessels. | Ed25519 default, optional transparency-log anchoring, isolated signing service, signer/install identity separation, visible fingerprint display in UI and runtime. Sources: `specs/vessel-format/signing-and-lineage.md`, `research/05-risks-and-tensions.md` | Key compromise remains catastrophic until revocation propagates everywhere. |
| **Replay attacks** | Attacker reuses an old x402 proof, nonce, or purchase receipt against another request or host. | Double-download, unauthorized access, or incorrect royalty attribution. | One-time nonce + expiry, receipt binding to manifest CID and listing ID, durable replay store, idempotent verifier behavior, audit correlation on every verify call. Sources: `specs/protocol/payment-layer.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/` | Distributed race conditions can still create narrow replay windows if clocks or stores drift. |
| **Plagiarism via fork-without-royalty** | Attacker republishes a vessel with stripped parent lineage or altered royalty target. | Authors lose attribution and derivative revenue; trust in the protocol erodes. | Require signed `parent_cids[]`, lineage-aware discovery ranking, similarity review for popular vessels, dispute/takedown process, and refusal to grant marketplace trust badges to orphaned derivatives. Sources: `specs/marketplace/royalties.md`, `research/05-risks-and-tensions.md` | Off-platform redistribution still exists and may require social or legal enforcement. |
| **Royalty oracle manipulation** | Attacker compromises the off-chain resolver or injects false lineage inputs to change payout plans. | Revenue goes to the wrong party or derivative flows stall. | Deterministic lineage calculation from signed manifests, dual verification path, payout-plan hash logging, and optional on-chain anchoring of final payout receipts. Sources: `specs/marketplace/ARCHITECTURE.md`, `specs/protocol/PROTOCOL.md` | Any off-chain resolver remains a trust concentration until more logic moves to verifiable or on-chain checks. |
| **Secret extraction at export** | Malicious or buggy export flow includes `.env`, `auth.json`, `state.db`, or session data that should have been stripped. | Wallets, tokens, operator history, or provider credentials leak inside vessels. | Strict export allowlist, strip-and-rehydrate policy, operator preview before sign, secret scanning, and host-side key reinjection only after install. Sources: `specs/hermes-binding/BINDING.md`, `specs/hermes-binding/strip-and-rehydrate.md`, `~/wiki/_meta/hermes-stack/hermes-content-os.md` | Human error is still possible if later tooling weakens the allowlist discipline. | <!-- wiki source -->
| **Deepfake persona spoofing** | Attacker publishes a vessel that claims a known operator, creator, or brand identity without control of the real signer. | Buyers trust the wrong source; disputes and reputational damage follow. | Separate creator profile, signer fingerprint, buyer, and installer identity surfaces; expose trust badges and review history; show signer mismatch warnings prominently. Sources: `research/05-risks-and-tensions.md`, `specs/marketplace/discovery-and-trust.md` | New users may still trust branding before provenance unless UI design stays disciplined. |
| **Gateway or cache poisoning** | Attacker controls a mirror, CDN edge, or cache entry and serves stale or incorrect bundle bytes. | Buyers fetch wrong content, previews lie, or malware is delivered under a trusted listing page. | Verify returned bytes against CID every time, keep R2 as cache not source of truth, dual-pin to IPFS + Arweave for important artifacts, and run integrity probes against hot content. Sources: `docs/infrastructure/services.md`, `specs/vessel-format/SPEC.md` | Availability attacks remain possible even if integrity attacks are blocked by CID verification. |

## 3. Required architectural controls

1. **No raw secret reuse across domains.** Export and install tooling may reference host-provided secret handles, never bundle secret material itself.
2. **Public preview is always redacted.** The content gateway may expose public slots and previews, but encrypted or sensitive slots remain gated.
3. **Signing stays isolated.** The signing surface is not the same host or process as the public preview surface.
4. **Runtime approval remains manual for irreversible flows.** Hermes install and purchase flows preserve operator approval and audit evidence. Sources: `specs/hermes-binding/BINDING.md`, `~/wiki/_meta/hermes-stack/hermes-content-os.md`. <!-- wiki source -->

## 4. Security review checklist for future implementation workers

Before any real service ships, a future worker should verify:

- export allowlist excludes `.env`, `auth.json`, `state.db`, and `sessions/` by default,
- x402 verification rejects nonce replay,
- the gateway re-hashes fetched payloads against CID,
- royalty resolution is deterministic for identical lineage input,
- signing keys live outside the public service plane,
- Hermes purchases emit `dispatch()` audit rows with vessel linkage fields.

## Source paths

- `research/05-risks-and-tensions.md`
- `specs/vessel-format/SPEC.md`
- `specs/vessel-format/signing-and-lineage.md`
- `specs/protocol/PROTOCOL.md`
- `specs/protocol/payment-layer.md`
- `specs/marketplace/ARCHITECTURE.md`
- `specs/marketplace/royalties.md`
- `specs/marketplace/discovery-and-trust.md`
- `specs/hermes-binding/BINDING.md`
- `specs/hermes-binding/strip-and-rehydrate.md`
- `~/wiki/raw/downloads/2026-04-10/root/system-map.md` <!-- wiki source -->
- `~/wiki/_meta/hermes-stack/hermes-content-os.md` <!-- wiki source -->
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
