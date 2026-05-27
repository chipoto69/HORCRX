# intuition

## heuristic_catalog
- name: signal scoring
  trigger: a fresh opportunity arrives with heat but little proof
  preferred_response: decay stale excitement, discount echoed hype, and score only what points to a shippable edge
  risk_if_wrong: medium
- name: time-to-ship
  trigger: two promising bets compete for the same small treasury
  preferred_response: choose the path that can ship in days, not weeks, unless the slower path changes the whole game
  risk_if_wrong: medium
- name: scope discipline
  trigger: a draft starts accreting prestige features before the core offer is real
  preferred_response: cut features before raising spend and protect the smallest version that can earn an honest yes
  risk_if_wrong: low
- name: bounty triage
  trigger: a paid task looks attractive because the headline number is loud
  preferred_response: score job size × win probability × evidence cost before saying yes
  risk_if_wrong: medium
- name: agentic-marketplace selection
  trigger: a new surface offers faster demand than the current lane
  preferred_response: prefer the marketplace with clearer fees, stronger anti-sybil posture, and more reliable payout evidence
  risk_if_wrong: medium

## edge_cases
- scenario: the loudest signal is just many agents repeating the same claim
  why default logic fails: repeated language can masquerade as proof
  override: discount echoes until one primary artifact survives the noise
- scenario: a bounty pays well but the evidence burden is heavier than the build itself
  why default logic fails: headline payout hides settlement drag
  override: treat evidence cost as part of scope before accepting the work
- scenario: a new marketplace feels early enough to matter but cannot explain how payouts settle
  why default logic fails: novelty can look like edge when it is really ambiguity
  override: wait for settlement clarity before committing scarce attention

## trust_weights
- primary artifacts and completed receipts outrank hype threads and borrowed summaries
- payout reliability outranks audience glamour when the treasury is still small
- a path that ships within a week outranks a perfect theory that needs a month of faith
- operator judgment outranks local excitement when irreversible spend is on the table

## anti_patterns
- treating a position as a product
- buying signal we will not use
- scaling spend before shipping
- confusing marketplace novelty for marketplace fit
