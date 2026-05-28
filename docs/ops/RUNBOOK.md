---
title: Operations runbook
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Operations runbook

HORCRX is still foundation-first. No live service in this document is deployed from this repo today. Treat every section below as a future-worker spec for how the operator surface should behave once implementation begins.

## Shared operating posture

- production rollout is operator-gated,
- every service change rides through PR review and green validators,
- public-plane services stay separate from trust-sensitive services,
- rollback always favors freezing writes over serving ambiguous state.

## Registry indexer

### Deploy

- roll forward only from a reviewed commit that preserves chain-adapter read parity,
- deploy schema changes and indexer code together so event projections stay version-aligned,
- keep a backfill plan ready before enabling new event types or new chain adapters.

### Health-check

- latest indexed Base and Solana block heights are within the accepted lag budget,
- listing row counts match expected chain events for the rollout window,
- lineage and revocation lookups return deterministic results for known fixture manifests.

### Rollback

- freeze new indexing writes,
- revert to the last known-good indexer build,
- rebuild affected projections from canonical chain data if the bad rollout wrote corrupt rows,
- do not mutate canonical manifest history to paper over index drift.

### Incident posture

- declare the indexer degraded if ownership, revocation, or listing state looks inconsistent,
- prefer read-only mode over serving uncertain write paths,
- record the affected chain range, listing IDs, and revocation rows before recovery starts.

## Content gateway

### Deploy

- ship gateway changes only with explicit CID-verification coverage,
- keep cache policy changes separate from access-policy changes when possible,
- stage preview/redaction changes in a limited environment before widening traffic.

### Health-check

- known manifest CIDs resolve to the expected manifest bytes,
- preview endpoints never expose restricted slot material,
- cache hit paths and origin fetch paths both re-hash returned content against CID.

### Rollback

- disable the bad release at the edge,
- purge poisoned cache entries,
- revert to the last build that re-verified CIDs correctly,
- temporarily reduce gateway features rather than weakening integrity checks.

### Incident posture

- treat any CID mismatch as a security event,
- freeze bundle release for affected artifacts until integrity is re-confirmed,
- preserve logs for cache key, manifest CID, slot CID, and upstream mirror used.

## IPFS pinning surface

### Deploy

- keep provider-specific rollout changes separate from content-policy changes,
- verify the retention policy and billing metadata mapping before enabling new pin classes,
- stage provider migrations behind the content gateway so retrieval semantics stay CID-first.

### Health-check

- known bundle and slot CIDs remain pinned at the active provider,
- provider object IDs map cleanly back to the intended manifest or slot CID,
- retrieval hints returned to the content gateway still resolve the expected bytes.

### Rollback

- stop issuing new pins through the bad provider integration,
- re-point the gateway to the last known-good provider routing,
- preserve existing pin metadata so bundles can be re-hydrated or re-pinned without inventing new identifiers,
- prefer temporary hot-cache service over weakening CID verification.

### Incident posture

- treat unexpected unpinning, retention drift, or provider byte mismatch as durability incidents,
- capture the affected CID set, provider object IDs, and policy class before remediation starts,
- escalate billing or quota exhaustion quickly because pin loss can cascade into preview and install failures.

## Arweave bundler

### Deploy

- roll uploader and funding-state changes together so permanent-write receipts stay auditably linked,
- isolate retry-policy edits from signing or manifest-generation changes,
- validate Irys funding posture before widening any new preservation class.

### Health-check

- known signed bundles return permanent transaction references,
- receipt metadata still binds the expected manifest CID and retention class,
- failed uploads surface retryable versus terminal errors distinctly.

### Rollback

- freeze new permanent-storage writes first,
- revert to the last uploader build that produced valid transaction receipts,
- preserve the funding ledger and failed payload references for replay after recovery,
- do not re-sign bundles just to work around a bad bundler rollout.

### Incident posture

- treat lost receipts, duplicate uploads, or funding-state drift as preservation-control incidents,
- capture manifest CID, bundle hash, funder identity, and retry history for every affected upload,
- prefer queueing signed bundles for later replay over improvising manual permanent writes.

## Signing service

### Deploy

- keep verification-only changes separate from custody-boundary changes,
- require operator review for any signer metadata, fingerprint display, or detached-signing flow changes,
- rotate dependencies cautiously because this surface sits close to provenance trust.

### Health-check

- known-good signatures verify for manifests and signed slots,
- signer fingerprint lookup remains stable for published artifacts,
- the service can reject malformed signatures without timing out or silently downgrading checks.

### Rollback

- disable new signing operations first,
- fall back to the last build that produced correct verification verdicts,
- preserve audit evidence for every request made during the bad window,
- never reuse or export secret key material as part of a rollback shortcut.

### Incident posture

- treat signer mismatch, unexpected key rotation, or verification bypass as high severity,
- freeze publication and badge issuance until provenance is re-established,
- notify operators responsible for key custody immediately.

## x402 facilitator

### Deploy

- roll challenge/verify changes with replay-protection migrations in the same window,
- require test coverage for nonce expiry, manifest-CID binding, and purchase-receipt formation,
- deploy admin-only controls separately from public challenge endpoints.

### Health-check

- challenge creation works for known listings,
- replayed proofs are rejected,
- receipts bind the expected listing ID, manifest CID, payer reference, and nonce state.

### Rollback

- freeze purchase issuance if nonce durability or receipt binding is in doubt,
- restore the previous verifier build,
- keep the durable nonce store intact so rollback does not reopen spent proofs.

### Incident posture

- treat replay acceptance, receipt mismatch, or payout-target drift as a financial-control incident,
- place affected listings into a safe mode until settlement evidence is trustworthy again,
- preserve the failing receipt, nonce, listing ID, and adapter verdicts for audit.

## Search and discovery

### Deploy

- separate ranking-model changes from ingestion/storage changes when possible,
- snapshot ranking inputs before enabling new signals or weights,
- document any new trust or dispute signal before exposing it publicly.

### Health-check

- known listings remain searchable by exact identifier and expected tags,
- trust badges, dispute state, and lineage filters render consistently,
- ranking output is stable for a fixed fixture corpus.

### Rollback

- revert to the previous ranking config or search index snapshot,
- keep the raw indexed corpus if only ranking is wrong,
- disable any new signal that cannot be explained or audited quickly.

### Incident posture

- treat silent ranking drift, missing dispute flags, or badge mislabeling as trust incidents,
- degrade gracefully to simpler ranking rather than showing misleading confidence,
- capture the exact query, filters, ranking version, and listing IDs involved.

## CESS evaluation lane

### Deploy

- keep CESS work behind an explicit experiment flag because it is not part of the first shipping path,
- ship mirror-policy changes separately from any content-gateway routing changes,
- document the retrieval SLO and legal-region assumptions before enabling a pilot.

### Health-check

- evaluation fixtures still produce a clear go / no-go recommendation,
- cost and retrieval measurements remain comparable with the IPFS + Arweave baseline,
- mirror-policy output stays traceable to the tested bundle size profile and durability target.

### Rollback

- disable any active CESS mirroring experiment before touching the primary gateway path,
- fall back to the baseline IPFS hot path plus Arweave/Irys permanent anchor posture,
- preserve experiment logs and recommendation artifacts for later review instead of deleting them,
- do not let a failed CESS trial mutate canonical manifest or registry semantics.

### Incident posture

- treat retrieval instability, unverifiable mirror receipts, or policy ambiguity as evaluation failures, not production incidents,
- capture bundle class, retrieval timings, region constraints, and operator decision context for the failed run,
- keep CESS out of the default storage policy until a future worker can demonstrate stable, auditable behavior.
