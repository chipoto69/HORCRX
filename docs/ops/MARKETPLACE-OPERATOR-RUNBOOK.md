---
title: Marketplace operator runbook
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Marketplace operator runbook

This runbook describes the human review posture for listings, disputes, takedowns, payout disagreements, and deepfake-risk cases. It is a spec-first operator contract until the marketplace services ship.

## 1. Response targets

Proposed defaults for Mission B operator HITL confirmation:

- first response to a dispute or takedown report: **under 48 business hours**,
- listing freeze on dispute open: **immediate**,
- target resolution window: **under 14 calendar days**,
- reviewer rotation: **weekly**, with handoff notes preserved in the operator log.

## 2. Listing approval workflow

1. confirm the listing references a valid manifest or preservation artifact,
2. verify signer identity, published provenance, and payout target shape,
3. confirm preview metadata does not disclose restricted payloads,
4. review dispute history, trust badges, and any lineage warnings,
5. approve, request edits, or reject with a written reason.

Minimum evidence to capture:

- listing ID,
- manifest CID,
- signer fingerprint or provenance reference,
- payout target,
- reviewer identity and timestamp.

## 3. Dispute intake workflow

Accept reports covering at least these categories:

- plagiarism or attribution failure,
- unpaid derivative use,
- false provenance,
- unauthorized commercial extraction,
- deepfake or likeness misuse,
- payout misdirection.

Intake steps:

1. acknowledge receipt,
2. freeze the listing immediately if the claim is non-frivolous,
3. collect reporter contact, listing ID, manifest CID, and supporting evidence,
4. assign a reviewer and severity tier,
5. record the dispute state without deleting listing history.

## 4. Takedown procedure

Use takedown mode when the listing should stop transacting before final resolution.

1. freeze listing visibility or purchase flow,
2. preserve the full audit trail and current listing metadata,
3. notify the listed publisher with the claim summary,
4. request counter-evidence or corrective action by a dated deadline,
5. resolve to reinstatement, forced correction, continued freeze, or external escalation.

Takedown must not erase lineage history; it adds state and operator evidence on top of the existing record.

## 5. Royalty payout dispute path

Use this path when authors agree the listing may stay visible but contest who should be paid.

1. place affected payouts on hold,
2. snapshot the lineage graph, payout target, royalty policy, and receipt evidence,
3. recompute the payout plan from canonical lineage inputs,
4. compare the recomputed plan with the disputed settlement,
5. either release funds, reroute according to the verified plan, or escalate to neutral review.

Required evidence:

- child manifest CID,
- `parent_cids[]` chain,
- royalty policy identifiers,
- receipt or escrow reference,
- operator decision log.

## 6. Deepfake escalation tier

Treat deepfake-persona or likeness misuse reports as the highest trust-risk class.

Immediate actions:

1. freeze the listing,
2. preserve all visible provenance, signer, preview, and complaint artifacts,
3. route the case to the highest-privilege reviewer tier,
4. require signer-identity evidence before reinstatement,
5. publish the eventual resolution state so future buyers can see the trust trail.

Escalate externally if the report also includes fraud, impersonation, or legal-risk claims beyond normal marketplace moderation.
