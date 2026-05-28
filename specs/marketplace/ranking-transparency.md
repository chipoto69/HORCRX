# Ranking transparency

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

HORCRX discovery must be legible enough that a seller can explain why a listing ranked where it did, and a buyer can see which trust signals mattered. This document freezes the named ranking signals, their weights, and the dispute path operators use when a ranking is challenged.

## 1. Named signals and weights

| Signal | Weight | What it measures | Evidence surface |
|---|---:|---|---|
| `recency` | `0.20` | whether the listing is fresh enough to surface without burying stable high-trust inventory | `created_at`, `updated_at` |
| `reviewer_reputation` | `0.25` | weighted review quality after anti-Sybil gating and badge-tier normalization | reviews, reviewer eligibility policy |
| `sales_velocity` | `0.20` | sustained purchase or install evidence over a recent rolling window | purchase receipts, install attestations |
| `dispute_history` | `0.20` | inverse trust signal; unresolved disputes lower score even when other metrics are strong | dispute ledger, takedown history |
| `parent_lineage_depth` | `0.15` | whether the listing exposes a legible ancestry trail instead of an opaque clone surface | `parent_cids[]`, lineage snapshot |

The weights sum to `1.00`. Each signal is normalized onto `[0, 1]` before weighting. `dispute_history` is a penalty-aware signal: a clean listing scores near `1.0`, while unresolved fraud, provenance, or deepfake complaints push it toward `0.0`.

## 2. Guardrails and hard caps

1. An open deepfake, fraud, or provenance dispute clamps the listing below fully clean results until the case is resolved.
2. A frozen listing stays queryable for audit, but is removed from default commercial ranking surfaces.
3. Operators MAY add temporary manual review labels, but they must not change the published signal weights without updating this document.

## 3. Challenge path

A vessel owner, rights holder, or reviewer may challenge a ranking by opening an operator dispute with:

- the listing ID,
- the manifest CID,
- the ranking evidence they believe is wrong,
- the signal category being challenged,
- and any supporting receipts, provenance, or badge evidence.

The challenge path is:

1. open a dispute through `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md` §3,
2. operators acknowledge within the published first-response SLA,
3. the assigned reviewer recomputes the weighted signals from canonical evidence,
4. the operator records either `ranking-confirmed`, `ranking-corrected`, or `ranking-frozen-pending-more-evidence`.

Ranking challenges never delete prior state. They append a review outcome so later buyers can see both the original ranking posture and the operator correction trail.
