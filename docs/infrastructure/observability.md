---
title: Observability baseline
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Observability baseline

Version: `v0.1-draft`

HORCRX observability should answer one question end to end: **who published, who paid, what bundle was served, what runtime installed it, and can we prove that chain of events after the fact?**

That means metrics alone are not enough. The stack needs structured logs for evidence, traces for flow reconstruction, and runtime-linked audit rows for Hermes-mediated purchases and installs. Sources: `specs/hermes-binding/BINDING.md`, `specs/protocol/payment-layer.md`, `specs/marketplace/ARCHITECTURE.md`, `~/wiki/_meta/hermes-stack/hermes-content-os.md`. <!-- wiki source -->

## 1. Logging contract

All services should emit **NDJSON** logs with a shared envelope.

### 1.1 Required common fields

| Field | Meaning |
|---|---|
| `timestamp` | ISO8601 UTC event time |
| `service` | emitting service name |
| `event` | semantic event name such as `listing_indexed`, `payment_verified`, `bundle_served` |
| `trace_id` | cross-service trace correlation key |
| `request_id` | request-level correlation key |
| `manifest_cid` | top-level vessel identifier when present |
| `listing_id` | marketplace listing reference when present |
| `actor_type` | `author`, `buyer`, `runtime`, `reviewer`, `system` |
| `status` | `ok`, `rejected`, `error` |
| `duration_ms` | elapsed time for timed operations |

### 1.2 Service-specific payloads

- **registry indexer**: chain, block/slot, ownership pointer, parent lineage hash
- **content gateway**: slot CID, cache hit/miss, redaction policy, bytes served
- **signing service**: signer fingerprint, signature algorithm, verification verdict
- **x402 facilitator**: nonce, expiry, chain, proof reference, replay-reject reason
- **search index**: query class, result count, ranking path, embedding model version

## 2. Metrics baseline

Use **Prometheus exposition** or **OpenTelemetry metrics** from day one. The exact collector can change later; the metric names should not.

### 2.1 Minimum counters and histograms

| Metric | Why it matters |
|---|---|
| `horcrx_registry_events_total` | detects ingestion drift or chain adapter starvation |
| `horcrx_gateway_requests_total` | top-line preview and download demand |
| `horcrx_gateway_cache_hit_ratio` | shows whether R2/cache strategy is paying off |
| `horcrx_signature_failures_total` | early warning for forgery attempts or bad client packaging |
| `horcrx_x402_verify_latency_ms` | payment user experience and replay-store health |
| `horcrx_replay_rejections_total` | direct signal that nonce protection is working |
| `horcrx_royalty_resolution_latency_ms` | lineage computation health |
| `horcrx_search_queries_total` | discovery demand and ranking load |
| `horcrx_bundle_bytes_served_total` | storage and cache cost driver |

## 3. Trace model

The first implementation should trace one canonical user journey:

```text
search -> preview -> challenge -> payment verify -> bundle fetch -> install handoff
```

Each span should carry at least:

- `manifest_cid`
- `listing_id`
- `runtime_profile` when a Hermes install is involved
- `chain`
- `payment_reference`

This keeps marketplace, gateway, and runtime evidence joinable later.

## 4. Hermes `dispatch()` audit integration

This is the load-bearing piece.

When a Hermes profile buys or installs a vessel, the marketplace flow must still produce the existing Hermes audit artifacts described in `~/wiki/_meta/hermes-stack/hermes-content-os.md`: <!-- wiki source -->

- profile-scoped NDJSON audit log,
- profile-scoped SQLite audit mirror,
- `dispatch()`-mediated logging even when budget caps are disabled.

### 4.1 Required runtime correlation fields

A Hermes-mediated marketplace action should add, at minimum:

- `action`: `vessel_purchase` or `vessel_install`
- `manifest_cid`
- `listing_id`
- `vessel_cid`
- `royalty_target`
- `run_id` or equivalent dispatch correlation field

This aligns directly with the provenance requirement in `specs/hermes-binding/BINDING.md` and ensures that later royalty or dispute analysis can join runtime activity back to the signed bundle lineage. Sources: `specs/hermes-binding/BINDING.md`, `~/wiki/_meta/hermes-stack/hermes-content-os.md`. <!-- wiki source -->

## 5. Dashboard sketch

A future Grafana or equivalent dashboard should expose at least five panels:

1. **Marketplace throughput** — listings indexed, purchases verified, bundles served
2. **Integrity panel** — signature failures, replay rejections, CID mismatches
3. **Storage panel** — cache hit rate, bytes served, IPFS pin health, Arweave mirror lag
4. **RPC dependency panel** — Base and Solana provider latency/error rates
5. **Hermes runtime audit panel** — vessel purchases and installs grouped by profile and manifest CID

## 6. Alerting priorities

Page or high-priority alert on:

- signature verification failure spikes,
- replay rejection spikes above expected background,
- R2/cache or IPFS gateway serving CID-mismatched payloads,
- royalty resolver output divergence for the same lineage input,
- missing Hermes audit rows for successful purchases.

Warn-only on:

- search latency drift,
- temporary cache hit degradation,
- mirror backlog growth.

## Source paths

- `specs/hermes-binding/BINDING.md`
- `specs/protocol/payment-layer.md`
- `specs/marketplace/ARCHITECTURE.md`
- `research/05-risks-and-tensions.md`
- `~/wiki/_meta/hermes-stack/hermes-content-os.md` <!-- wiki source -->
- `~/wiki/raw/downloads/2026-04-10/root/system-map.md` <!-- wiki source -->
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
