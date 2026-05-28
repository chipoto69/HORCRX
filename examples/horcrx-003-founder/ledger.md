# ledger

## custody_posture
host_signs_vessel_proposes

## spend_knobs
- per_tx: 2% of treasury
- daily: 8% of treasury
- weekly: 20% of treasury
- cooldown: 60
- hitl_threshold: any spend at or above per_tx
- allowlist: []

## earn_knobs
- allowed_marketplaces:
  - agentic.market
  - clawhub-class-bounty
  - code-bounty-generic
  - self-hosted-microproduct
  - data-scrape-service
- min_job_size: $0.10
- evidence_schema: see plugins/marketplaces.json::marketplaces[*].evidence_schema
- payout_addresses_by_chain: {}

## spend_mix_ratios
- earliness: 40
- making: 40
- overhead: 20
- note: earliness + overhead must stay at or below 60 so making never drops beneath 40% of spend.

## revenue_respend_policy
revenue may be respent without re-triggering hitl up to the declared per_tx; any over-cap revenue-funded spend still requires hitl.

## treasury_notes
- the vessel proposes, the host signs, and every paid action leaves an audit row.
- live recipient allowlisting stays empty until a later phase binds public payout addresses and operator approvals.
- the five declared marketplaces are live from v0 and detailed per surface in plugins/marketplaces.json.

## review_triggers
- any request to widen spend caps or shorten cooldowns.
- any new marketplace added beyond the declared five surfaces.
- any request to bind a public payout address to a live custody flow.

## signed_off_by
- approved 2026-05-28 — loosened to 2%/8%/20% to give the vessel headroom while still leaving 80% weekly preserved
- approved 2026-05-28 — earliness gets more headroom since being-earlier is the moat for a maker agent
- approved 2026-05-28 — full allowlist live from v0; new surfaces beyond these five require HITL
