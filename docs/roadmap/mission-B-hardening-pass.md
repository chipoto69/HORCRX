---
title: Mission B — HORCRX hardening pass
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Mission B — HORCRX hardening pass

ATLAS → CORPUS → HORCRX.

Status: kickoff-ready (foundation-spec mission; no runtime code yet)
Recon: `research/12-hardening-recon.md`
Parallel mission: `docs/roadmap/mission-A-horcrx-003-founder-vessel.md`

## 1. mission line

Harden HORCRX's documentation, wiki strategy, access controls, secrets posture, memory + traces specifications, marketplace pre-launch surfaces, apps foundation prep, and supply-chain release discipline — so the system can scale without leakage or drift. Each phase is "design before hope": every step is explicit, every gate is enforced, every assumption is converted into either a spec line or a CI check. No production code is written; this mission produces *enforced foundation*.

## 2. why now

Per recon 12, foundation v0.1.1 is doctrinally strong but **enforcement is thin**:

- Only 4 CI gates exist (commitlint, schema-validate, markdown-link-check, voice-lint).
- Branch protection is spec-only; no GitHub-side rule applied.
- No secret scanner. No SBOM. Action versions are floating major tags.
- `validation/` is a single worker report — no scripts, no fixtures, no GATE chain, no signature roundtrip, no strip-rehydrate, no nonce-replay, no royalty-determinism tests.
- 6 High-severity doc gaps (onboarding, runbook, security model, release process, marketplace operator runbook, VAL-* index).
- Marketplace pre-launch lockdown table has 10+ open rows (payout target typing, ranking transparency, anti-Sybil, dispute SLA, revocation-never-deletes, etc.).
- One untracked `specs/hermes-webapi-backup/` directory violates AGENTS.md foundation-only rule.

This mission converts each gap into either a spec line, a doc file, a CI gate, or an operator HITL decision.

## 3. scope (in)

Eight phases, executable in **wave order H1 → H8**. Each phase is independently scopable and can be parallelized inside the wave; later waves depend on earlier waves only where stated.

### H1 · secrets, hooks, branch protection (BLOCKER for all later phases)
- Apply documented `branch-protection.md` rules via `gh api` (operator HITL).
- New CI job `ci/secret-scan` (`trufflehog` or `gitleaks`, SHA-pinned).
- Extend `voice-lint` scope to: `packages/design-system/VOICE.md`, every `examples/*/voice.md`, every `examples/*/soul.md`.
- `branch-protection.md` updated to list `ci/voice-lint` and `ci/secret-scan` as required contexts.
- `pre-push` hook extended beyond `refs/heads/main` to all protected refs.
- `commit-msg` hook deny-list adds `wip`, `tmp`, `temp`, `fixup`.
- Untracked `specs/hermes-webapi-backup/` disposition (operator decision: move to `research/` archive or delete).
- All GitHub Actions pinned to commit SHAs via Dependabot's pinning support.

### H2 · validation contract + GATE chain
- `validation/VAL-INDEX.md` enumerates every `VAL-*` ID, links to spec section + test fixture.
- `validation/scripts/` lands runnable scripts for GATE-HX-04..08 (see recon 12 §F.3).
- New CI jobs: signature-roundtrip, parent-cid-resolves, strip-rehydrate, docs-allowlist, extended voice-lint.
- x402 nonce-replay property test against a stub facilitator.
- Royalty-resolution determinism test against golden fixtures.
- `branch-protection.md` updated with new CI contexts.

### H3 · docs onboarding + ops runbook
- `docs/onboarding/` — `01-clone-and-hooks.md`, `02-run-validators.md`, `03-troubleshoot-ci.md`, `04-mission-checklist.md`.
- `docs/ops/RUNBOOK.md` — one section per service in `docs/infrastructure/services.md` §2.
- `docs/release/RELEASING.md` — tag → draft → publish flow + signing posture.
- `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md` — dispute intake, listing approval/takedown, royalty payout dispute, deepfake escalation.
- `docs/security/SECRETS.md` — intended secret stores per surface; shell-env-only rule.
- `docs/CANONICAL.md` — allowlist of docs (used by GATE-HX-07).
- README extended with security/contributing/validation links and a "report a vulnerability" CTA.
- `SECURITY.md` placeholder contact replaced (operator HITL).

### H4 · memory + traces spec hardening
- `specs/vessel-format/memory-graft-provenance.md` — graft provenance + consent record schema.
- `specs/vessel-format/traces-format.md` extended with `schema_version`, max-line-size, append-only invariant, rotation rule, redaction-validator contract.
- `specs/hermes-binding/BINDING.md` §4.4 lineage SQLite schema gains explicit append-only constraint + per-row chain-hash field.
- Redaction-validator script in `validation/scripts/`, wired as GATE.
- AEAD test vectors (KATs) for `age` and `x25519-xsalsa20-poly1305` in CI.
- Non-Hermes runtime trace export semantics added to `specs/vessel-format/compatibility-matrix.md`.

### H5 · marketplace pre-launch lockdown
- `specs/registry/listing.schema.json` — listing row.
- `payout_target` typed-identifier rule (`evm:0x...` / `solana:...`) documented + tested.
- `specs/marketplace/ranking-transparency.md` — weights + challenge path.
- `specs/marketplace/anti-sybil-schema.json` — rate-limits, reviewer eligibility.
- Dispute SLA published in `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md`.
- "Revocation never deletes" property test.
- Chain-adapter symmetry property test (Base ↔ Solana).
- Encrypted-envelope KATs.
- Preview-integrity (re-hash on fetch) test with golden fixtures.

### H6 · apps foundation prep
- `apps/marketplace-ui/`, `apps/marketplace-api/`, `apps/api/` — directory placeholders + stub READMEs linking specs.
- `examples/listings/` — listing fixture set.
- `specs/protocol/wallet-adapter-mock.md` — mock contract for Phase-3 frontend.
- `specs/marketplace/mcp.schema.json` — MCP `horcrx-marketplace` JSON-RPC schema.
- `examples/horcrx-002-orbel-pack/` per-member manifests materialized OR explicitly marked deferred.

### H7 · wiki + canon harden (HORCRX-internal)
- `docs/CANONICAL.md` allowlist (used by GATE-HX-07).
- Every `docs/**.md` gains minimum frontmatter (`title`, `version`, `updated`).
- `ci.yml` gains `ci/docs-frontmatter` job.
- `markdown-link-check` tightened to flag unannotated `~/wiki/...` references. <!-- wiki source -->
- Cross-link policy stated explicitly: HORCRX reads `~/wiki/`, never writes outside the wiki-librarian gate. <!-- wiki source -->

### H8 · supply chain + release discipline
- SBOM generation in `release.yml` (CycloneDX or SPDX, pin SHA).
- Action SHAs pinned everywhere (resolves `setup-node@v4` vs `@v6` drift between `ci.yml` and `release.yml`).
- `release.yml` requires manual operator approval (GH environment with required reviewers).
- CHANGELOG.md regression test in CI (tag → matching section).
- Vessel-signing-key fingerprint section in `SECURITY.md` populated once a real key exists (operator-gated; placeholder text replaced).

## 4. scope (out)

- No runtime code (foundation-first per AGENTS.md).
- No live contract deploys, no testnet/mainnet, no paid RPC.
- No public package publishing (npm, etc.).
- No edits to `~/wiki/`, `~/.hermes/`, `~/.claude-worktrees/ATLAS/`, `~/.factory/skills/`. <!-- wiki source -->
- No production key generation; no real signing fingerprint published until operator confirms a key exists.
- No production-ready listing intake (the schemas/policies land; the actual listing UI is Phase 3 of `next-missions.md`).
- No team/CODEOWNERS expansion (single-operator stays); pre-stage only.
- No edits to `examples/horcrx-001-candysoul/` or `examples/horcrx-002-orbel-pack/` except the targeted `voice.md` consistency change forced by Mission A's slot promotion.
- No deletion of `specs/hermes-webapi-backup/` without an explicit operator decision recorded in `validation/F-B-hardening-WORKER-COMPLETE.md`.

## 5. acceptance criteria

Each phase has its own acceptance set (mirroring recon 12 §G); the mission overall closes when:

B1. **H1 done**: branch protection live on `main` (`gh api` confirmed), `ci/secret-scan` job green, voice-lint scope extended, GH Actions pinned to SHAs, `specs/hermes-webapi-backup/` disposition recorded.
B2. **H2 done**: `validation/VAL-INDEX.md` enumerates ≥ 14 `VAL-*` IDs with coverage status; all five new GATE jobs green in CI; nonce-replay + royalty-determinism tests green.
B3. **H3 done**: all six High-severity doc gaps from recon 12 §A closed; `SECURITY.md` placeholder contact replaced; README links updated.
B4. **H4 done**: memory-graft provenance schema lands; traces format gains `schema_version` + append-only + rotation; AEAD KATs green; BINDING.md §4.4 has explicit append-only + chain-hash.
B5. **H5 done**: every row of recon 12 §E.3 lockdown table has a corresponding schema/doc/test in repo; cross-chain symmetry test green.
B6. **H6 done**: three new apps/ dirs exist with stub READMEs + spec links; listing fixtures + wallet-adapter mock + MCP schema land; pack manifest decision recorded.
B7. **H7 done**: docs frontmatter + canonical allowlist enforced in CI; cross-link policy documented.
B8. **H8 done**: SBOM in release pipeline; action SHAs pinned; release requires operator approval; CHANGELOG regression check live; (signing-key fingerprint deferred until key exists, recorded as a follow-up).
B9. `validation/F-B-hardening-WORKER-COMPLETE.md` reports each phase's completion + every operator HITL decision.
B10. `docs/roadmap/ROADMAP.md` Phase 0 marked complete; new entry "Mission B · hardening · spec+enforcement complete" pointing to this packet.

## 6. off-limits (mission-specific, in addition to repo AGENTS.md off-limits)

- Do NOT write to `~/wiki/` (recon 12 §B.1 one-way bridge). The wiki-librarian mission owns those writes. <!-- wiki source -->
- Do NOT touch live Hermes profiles or `~/.hermes/` runtime files.
- Do NOT create operator secrets, real or test, in the repo or in CI. CI must enforce, not import, secrets.
- Do NOT generate signing keys; the fingerprint section in `SECURITY.md` stays placeholder until a real key exists and operator publishes it.
- Do NOT push to remote without explicit operator approval. Branch-protection apply (`gh api`) is the sole operator-HITL push event in H1.
- Do NOT modify `examples/horcrx-001-candysoul/` or `horcrx-002-orbel-pack/` content except the `voice.md` slot consistency change required by Mission A's SPEC update.
- Do NOT edit `packages/design-system/` beyond extending `voice-lint` scope (lint config only, not the canon files themselves).
- Do NOT add LLM keys, wallet seeds, MCP tokens, or any service credential anywhere.
- Do NOT split CODEOWNERS into teams in this mission (single-operator stays).
- Do NOT cut a new release tag; this mission ships its changes via PRs only.

## 7. recommended worker topology

| Wave | Workers | Notes |
|---|---|---|
| H1 (blocker) | security-worker + operator HITL | sequential before any other phase ships |
| H2 | validator/evaluator + builder | runs in parallel with H3, H4, H5 |
| H3 | docs-worker + design-system reviewer + operator HITL on legal posture | parallel with H2, H4, H5 |
| H4 | memory/traces specialist + cryptography reviewer | parallel with H2, H3, H5 |
| H5 | marketplace builder + protocol reviewer + dispute-policy reviewer | parallel with H2, H3, H4 |
| H6 | foundation builder + frontend reviewer | runs after H2 (depends on listing schema) |
| H7 | docs-worker + librarian reviewer | runs after H3 (depends on CANONICAL.md scope) |
| H8 | release/build worker + security worker + operator HITL | runs last; depends on H1, H2 |

Suggested execution shape: H1 first, fully serialized through operator approval. Then waves: {H2, H3, H4, H5} run in parallel; {H6, H7} run when their dependencies clear; H8 closes.

Use `dispatching-parallel-agents` SKILL pattern (`~/.agents/skills/dispatching-parallel-agents/SKILL.md`) and the GATE-discipline of `content-os` (`~/.factory/skills/content-os/SKILL.md`) as live precedents.

## 8. dependencies and blockers

- Mission A is **parallel, not blocking**. The two missions share zero file collisions except a coordinated edit to `specs/vessel-format/manifest.schema.json` and `specs/vessel-format/SPEC.md` (Mission A extends; Mission B does not touch). H1 must complete before Mission A merges so that branch protection is live for the founder-vessel PR.
- Operator HITL required in H1 (branch protection apply, web-api-backup disposition), H3 (security contact), H5 (listing schema final shape if multiple acceptable), H8 (release approval rule).
- GitHub Actions Dependabot SHA-pinning support must be confirmed available; otherwise pin manually via `actions/setup-node@<sha> # v6.0.0` comment-tag pattern.

## 9. forensic / "design before hope" notes

- Recon 12 §H lists 12 unresolved operator questions. Each phase H1..H8 must resolve its associated questions or defer them with a stamped `validation/F-B-hardening-WORKER-COMPLETE.md` entry. Nothing is allowed to drift quietly.
- The GATE-HX-01..08 chain mirrors content-os's GATE-01..08 pattern and the wiki canon's `_meta/commit-standards.md` GATE-07 pattern — that is intentional. Cross-system gate parity reduces operator cognitive load.
- The "design before hope" doctrine applies recursively: each new doc must declare its own update cadence + ownership in frontmatter so we never relitigate "is this current."

## 10. success-shaped close

Mission ends when:

- Every phase H1..H8 has its acceptance criteria met (or a stamped deferral recorded in the worker-complete report with a follow-up issue).
- Eight PRs (one per phase) are merged via the now-protected `main` branch.
- `validation/F-B-hardening-WORKER-COMPLETE.md` enumerates each merged PR, every operator HITL decision, every deferral.
- `docs/roadmap/ROADMAP.md` reflects the new hardening status.

This is the floor of the temple. After this mission, every future mission has rails to ride on and can never bypass them quietly.
