# ledger

## custody_posture
host_signs_vessel_proposes

## spend_knobs
- per_tx: 1% of treasury
- daily: 5% of treasury
- weekly: 15% of treasury
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
- earliness: 30
- making: 50
- overhead: 20
- note: earliness + overhead must stay at or below 50 so making never drops beneath half the spend.

## revenue_respend_policy
revenue may be respent without re-triggering hitl up to the declared per_tx; any over-cap revenue-funded spend still requires hitl.

## treasury_notes
- the vessel proposes, the host signs, and every paid action leaves an audit row.
- live recipient allowlisting stays empty until a later phase binds public payout addresses and operator approvals.
- marketplace access is declared here and detailed per surface in plugins/marketplaces.json.

## review_triggers
- any request to widen spend caps or shorten cooldowns.
- any new marketplace added beyond the declared five surfaces.
- any request to bind a public payout address to a live custody flow.

## signed_off_by
pending operator hitl on OQ-13, OQ-17, and OQ-18
