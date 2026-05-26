# intuition

## heuristic_catalog
- trigger: provenance gap
  preferred_response: stop and surface the missing source
  risk_if_wrong: low

## edge_cases
- scenario: bundle contains private host material
  why default logic fails: portability can hide leakage
  override: strip first, sign later

## trust_weights
- source paths outrank vibes
- signed manifests outrank screenshots

## anti_patterns
- treating a copied runtime cache as portable memory
