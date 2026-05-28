# Worker Complete — Mission B hardening pass

Date: 2026-05-28
Repo: `chipoto69/HORCRX`
Local path: repo checkout root
Branch: `foundation/hardening-pass`
PR: `https://github.com/chipoto69/HORCRX/pull/9`

## Mission

Mission B · hardening pass close fix-forward

## Diagnosis

- Mission B started from a foundation-only repo with the doctrinal packet already landed, but enforcement drift remained: live `main` branch protection still exposed only five required contexts while `.github/branch-protection.md` documented eighteen.
- The final validator synthesis at `mission:library/validator-synthesis-B-final.md` reported nine blockers at local head `d83fd91`, including an unpushed branch, a stale repo-root `WORKER-COMPLETE.md`, a stale `[Unreleased]` section, onboarding/runbook documentation gaps, a missing signing-key follow-up link, and the HX.5 false positive around the H6 pack-deferral note.
- Repo-root `WORKER-COMPLETE.md` still described the Mission A founder-vessel close on `foundation/founder-vessel`, so Mission B no longer had the required top-level close artifact.
- Operator-only follow-up remained intentionally open: GitHub `release` environment required reviewers (`H8.3`) still needs a Settings UI stamp during PR review.

## Strategy chosen — eight-phase hardening branch, then close fix-forward

- Keep all work on `foundation/hardening-pass`, publish the previously unpushed 27-commit Mission B stack to GitHub, and use GitHub Actions truth rather than PR aggregation rows.
- Re-apply `main` branch protection directly from `.github/branch-protection.md` so the documented context list and live GitHub policy converge again.
- Land the worker-addressable fix-forward items as small Conventional Commit docs/validation commits: changelog, onboarding validator guide, runbook service coverage, signing-key deferral link, and a CI false-positive fix required to restore green `ci/secret-scan`.
- Amend the mission-local validation contract so HX.5 explicitly accepts the H6-authorized `examples/horcrx-002-orbel-pack/MANIFEST-DEFERRAL.md` note, while deferring the operator-only `H8.3` setting and post-push bot-comment triage to PR review / F-B-Vf2.

## Changes applied

1. `0ea11d9 feat(ci): add secret-scan job and extend voice-lint`
2. `def2da5 feat(githooks): harden protected-ref push and scope checks`
3. `762e7c7 docs(security): require voice and secret scan contexts`
4. `ce4023c docs(roadmap): commit Mission B source-of-truth packet and recon for PR audit trail`
5. `bebf984 chore(actions): pin workflows to commit SHAs`
6. `43c7d77 docs(research): archive hermes webapi backup prototype`
7. `7fb598e fix(ci): allow quoted prose in voice lint`
8. `f13a532 feat(validation): add H2 validation gates and fixtures`
9. `d87b70d feat(ci): add H2 gate jobs and pack-child validation`
10. `e189c4e docs(onboarding): add clone and hooks bootstrap`
11. `7a2198e docs(onboarding): add local validator guide`
12. `bf959e6 docs(onboarding): add CI troubleshooting guide`
13. `0b505e7 docs(onboarding): add mission entry checklist`
14. `d8b234a docs(ops): add per-service operations runbook`
15. `ae8d2ee docs(release): add release procedure guide`
16. `c0cbad2 docs(ops): add marketplace operator runbook`
17. `42cd335 docs(security): add secret handling guide`
18. `ad1788a docs(canonical): expand docs allowlist`
19. `28630e3 docs(readme): add security operator contract links`
20. `772e307 docs(security): replace vulnerability intake placeholder`
21. `8907b9b feat(spec): harden memory graft and trace validation`
22. `7415676 feat(spec): add marketplace listing and trust policy surfaces`
23. `965bf87 docs(ops): publish marketplace dispute SLA defaults`
24. `ecd9726 feat(validation): add marketplace lockdown validators`
25. `7ac1324 feat(ci): add marketplace lockdown validation gates`
26. `b633ce0 feat(apps): stub marketplace-ui, marketplace-api, api READMEs`
27. `1093037 feat(examples): add Base + Solana listing fixtures`
28. `912cebe feat(spec): add wallet-adapter-mock contract`
29. `b5d44a0 feat(spec): add horcrx-marketplace MCP JSON-RPC schema`
30. `39e97fb docs(examples): add ORBEL pack manifest deferral note`
31. `0f7af75 feat(ci): enforce docs hygiene gates`
32. `a056b21 chore(release): harden release workflow`
33. `7c14bb1 feat(ci): add changelog regression gate`
34. `d83fd91 docs(security): defer vessel signing fingerprint`
35. `c5bc097 docs(release): append Mission B hardening-pass notes to Unreleased`
36. `5e6c035 docs(onboarding): document Mission B CI gates in run-validators`
37. `27dca4b docs(ops): add IPFS/Arweave/CESS sections to RUNBOOK`
38. `11f498e docs(security): link signing-key deferral to roadmap Phase 1`
39. `70206d2 fix(validation): avoid secret-scan false positive in AEAD fixture`
40. `b30dc54 docs(onboarding): fix changelog-regression example link parsing`
41. `18daa27 fix(ci): allowlist public AEAD fixture for gitleaks`

## Verification

- Validator synthesis pointer: `mission:library/validator-synthesis-B-final.md` recorded the pre-fix state and drove this fix-forward scope.
- Published the previously local Mission B stack with `git push` from `d83fd91`; that head initially failed `ci/secret-scan`, which was traced to a public libsodium AEAD fixture being scanned as a secret.
- Re-applied live branch protection via `gh api --method PUT repos/chipoto69/HORCRX/branches/main/protection` using the required context list parsed from `.github/branch-protection.md`; the API now returns all 18 documented required checks.
- Post-fix CI truth on head `18daa27` completed green in both workflows: push run `26573919722` and pull_request run `26573921348` each returned `status=completed` and `conclusion=success`.
- Final head verification after this repo-root report commit is re-checked in the feature handoff so the close report and the pushed head remain aligned without force-pushing shared history.

## Operator HITL decisions

| Decision | Status | Evidence |
|---|---|---|
| H1.1 branch protection live on `main` | APPLIED 2026-05-28 | `gh api repos/chipoto69/HORCRX/branches/main/protection` now reports the full 18-context rule from `.github/branch-protection.md`. |
| H1.7 `specs/hermes-webapi-backup/` disposition | APPLIED | Archived under `research/archive/hermes-webapi-backup/README.md` on this branch. |
| H3.11 security intake channel | APPLIED | `SECURITY.md` publishes `security@horcrux.dev`. |
| H5.5 marketplace dispute SLA defaults | APPLIED | `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md` keeps `<48h` first response and `<14d` resolution targets. |
| H8.3 GitHub `release` environment required reviewers | PENDING PR review / operator UI | Must be configured in GitHub Settings; not worker-addressable in-repo. |
| H8.5 vessel signing-key publication | DEFERRED with follow-up link | `SECURITY.md` now links to `docs/roadmap/next-missions.md#phase-1--vessel-cli-and-hermes-export`. |

## Known follow-ups

- `H8.3` remains the only operator-only blocker from the final validator pass; F-B-Vf2 should treat it as deferred-by-operator-choice if the Settings UI stamp has not landed yet.
- PR #9 still carries 19 bot review comments. They are intentionally left for separate triage after F-B-Vf2 confirms the branch is otherwise green.
- The mission-local validation contract edit for HX.5 lives at `mission:validation-contract.md` and should be consumed by F-B-Vf2; it is not a repo commit by design.

## Files written / modified

- `.githooks/commit-msg`
- `.githooks/pre-push`
- `.github/branch-protection.md`
- `.github/workflows/ci.yml`
- `.github/workflows/release.yml`
- `.gitleaks.toml`
- `CHANGELOG.md`
- `README.md`
- `SECURITY.md`
- `apps/api/README.md`
- `apps/marketplace-api/README.md`
- `apps/marketplace-ui/README.md`
- `docs/CANONICAL.md`
- `docs/infrastructure/hosting.md`
- `docs/infrastructure/local-dev.md`
- `docs/infrastructure/observability.md`
- `docs/infrastructure/security.md`
- `docs/infrastructure/services.md`
- `docs/onboarding/01-clone-and-hooks.md`
- `docs/onboarding/02-run-validators.md`
- `docs/onboarding/03-troubleshoot-ci.md`
- `docs/onboarding/04-mission-checklist.md`
- `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md`
- `docs/ops/RUNBOOK.md`
- `docs/release/RELEASING.md`
- `docs/roadmap/ROADMAP.md`
- `docs/roadmap/migration-from-knowledge-horcrux.md`
- `docs/roadmap/mission-A-horcrx-003-founder-vessel.md`
- `docs/roadmap/mission-B-hardening-pass.md`
- `docs/roadmap/next-missions.md`
- `docs/security/SECRETS.md`
- `examples/horcrx-002-orbel-pack/MANIFEST-DEFERRAL.md`
- `examples/listings/listing-001.json`
- `examples/listings/listing-002.json`
- `research/12-hardening-recon.md`
- `research/archive/hermes-webapi-backup/README.md`
- `research/archive/hermes-webapi-backup/__init__.py`
- `research/archive/hermes-webapi-backup/__main__.py`
- `research/archive/hermes-webapi-backup/app.py`
- `research/archive/hermes-webapi-backup/deps.py`
- `research/archive/hermes-webapi-backup/errors.py`
- `research/archive/hermes-webapi-backup/models/__init__.py`
- `research/archive/hermes-webapi-backup/models/chat.py`
- `research/archive/hermes-webapi-backup/models/common.py`
- `research/archive/hermes-webapi-backup/models/config.py`
- `research/archive/hermes-webapi-backup/models/memory.py`
- `research/archive/hermes-webapi-backup/models/sessions.py`
- `research/archive/hermes-webapi-backup/models/skills.py`
- `research/archive/hermes-webapi-backup/routes/chat.py`
- `research/archive/hermes-webapi-backup/routes/config.py`
- `research/archive/hermes-webapi-backup/routes/health.py`
- `research/archive/hermes-webapi-backup/routes/memory.py`
- `research/archive/hermes-webapi-backup/routes/models.py`
- `research/archive/hermes-webapi-backup/routes/sessions.py`
- `research/archive/hermes-webapi-backup/routes/skills.py`
- `research/archive/hermes-webapi-backup/sse.py`
- `research/archive/hermes-webapi-backup/zai_defaults.py`
- `specs/hermes-binding/BINDING.md`
- `specs/marketplace/anti-sybil-schema.json`
- `specs/marketplace/ip-preservation.md`
- `specs/marketplace/mcp.schema.json`
- `specs/marketplace/ranking-transparency.md`
- `specs/protocol/chain-adapters.md`
- `specs/protocol/wallet-adapter-mock.md`
- `specs/registry/listing.schema.json`
- `specs/vessel-format/compatibility-matrix.md`
- `specs/vessel-format/memory-graft-provenance.md`
- `specs/vessel-format/traces-format.md`
- `validation/VAL-INDEX.md`
- `validation/fixtures/aead/age-cctv-x25519.json`
- `validation/fixtures/aead/x25519-xsalsa20-poly1305-libsodium.json`
- `validation/fixtures/envelopes/operator-slot-body.age.json`
- `validation/fixtures/envelopes/per-buyer-envelope.x25519-xsalsa20-poly1305.json`
- `validation/fixtures/known-cids.json`
- `validation/fixtures/payout-target-format/invalid.json`
- `validation/fixtures/payout-target-format/valid.json`
- `validation/fixtures/previews/preview-integrity.json`
- `validation/fixtures/profile-fixture/AGENTS.md`
- `validation/fixtures/profile-fixture/SOUL.md`
- `validation/fixtures/profile-fixture/audio_cache/audio.tmp`
- `validation/fixtures/profile-fixture/auth.json`
- `validation/fixtures/profile-fixture/auth.lock`
- `validation/fixtures/profile-fixture/cache/cache.tmp`
- `validation/fixtures/profile-fixture/config.yaml`
- `validation/fixtures/profile-fixture/cron/jobs.json`
- `validation/fixtures/profile-fixture/cron/output/last-run.txt`
- `validation/fixtures/profile-fixture/gateway.lock`
- `validation/fixtures/profile-fixture/gateway.pid`
- `validation/fixtures/profile-fixture/gateway_state.json`
- `validation/fixtures/profile-fixture/home/.keep`
- `validation/fixtures/profile-fixture/image_cache/image.tmp`
- `validation/fixtures/profile-fixture/pastes/paste.txt`
- `validation/fixtures/profile-fixture/processes.json`
- `validation/fixtures/profile-fixture/sessions/session-001.md`
- `validation/fixtures/profile-fixture/state.db`
- `validation/fixtures/profile-fixture/state.db-shm`
- `validation/fixtures/profile-fixture/state.db-wal`
- `validation/fixtures/registry/revocation-lineage.json`
- `validation/fixtures/royalty/expected-payout-plan.json`
- `validation/fixtures/royalty/lineage-fixture.json`
- `validation/fixtures/traces/redaction-expected.ndjson`
- `validation/fixtures/traces/redaction-input.ndjson`
- `validation/scripts/aead-kats.py`
- `validation/scripts/chain-adapter-symmetry.py`
- `validation/scripts/gate-hx-04-signature-roundtrip.py`
- `validation/scripts/gate-hx-05-parent-cid-resolves.py`
- `validation/scripts/gate-hx-06-strip-rehydrate.sh`
- `validation/scripts/gate-hx-07-docs-allowlist.sh`
- `validation/scripts/gate-hx-08-voice-lint-extended.sh`
- `validation/scripts/marketplace-envelope-kats.py`
- `validation/scripts/payout-target-format.py`
- `validation/scripts/preview-integrity.py`
- `validation/scripts/redaction-validator.py`
- `validation/scripts/revocation-never-deletes.py`
- `validation/scripts/royalty-determinism.py`
- `validation/scripts/x402-nonce-replay.py`
- `mission:validation-contract.md` *(mission-local HX.5 allowance for the H6 pack-deferral note)*
