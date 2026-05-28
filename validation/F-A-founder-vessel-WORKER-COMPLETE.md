# F-A · founder-vessel · worker-complete

Mission: HORCRX #003 · founder vessel
Mission ID: 3b33da05-36b3-40ba-a061-ccf4f3fde037
Branch: foundation/founder-vessel
PR: pending F-A-07 (`gh pr list --state open --head foundation/founder-vessel` returned `[]` during F-A-06)

## Validation contract status

| Assertion | Status | Evidence |
|---|---|---|
| `A1.1` | `passed` | `specs/vessel-format/SPEC.md` §3 required-files list includes `voice.md`. |
| `A1.2` | `passed` | `specs/vessel-format/SPEC.md` §3 reserves `mission.md`, `ledger.md`, `autonomy.md`, `constraints.md`. |
| `A1.3` | `passed` | `specs/vessel-format/voice-md.schema.md` exists. |
| `A1.4` | `passed` | `specs/vessel-format/mission-md.schema.md` exists with required mission fields. |
| `A1.5` | `passed` | `specs/vessel-format/ledger-md.schema.md` exists with spend/earn knobs and ratios. |
| `A1.6` | `passed` | `specs/vessel-format/autonomy-md.schema.md` exists with HITL and no-trading fields. |
| `A1.7` | `passed` | `specs/vessel-format/manifest.schema.json`; `examples/horcrx-001-candysoul/manifest.json`; `examples/horcrx-002-orbel-pack/manifest.json`; `examples/horcrx-003-founder/manifest.json`. |
| `A1.8` | `passed` | `examples/horcrx-001-candysoul/manifest.json` references the required voice slot. |
| `A1.9` | `passed` | `examples/horcrx-002-orbel-pack/VOICE-DEFERRAL.md` explains the deferred pack-level voice handling under the updated slot requirement. |
| `A2.1` | `passed` | `examples/horcrx-003-founder/soul.md` plus voice-lint coverage. |
| `A2.2` | `passed` | `examples/horcrx-003-founder/agents.md` includes treasury + dispatch-audit guardrails. |
| `A2.3` | `passed` | `examples/horcrx-003-founder/principles.md` carries maker-not-trader doctrine. |
| `A2.4` | `passed` | `examples/horcrx-003-founder/intuition.md` includes signal, shipping, scope, bounty, and marketplace heuristics. |
| `A2.5` | `passed` | `examples/horcrx-003-founder/dreams.md` contains the mission-authored cycle. |
| `A2.6` | `passed` | `examples/horcrx-003-founder/voice.md` has the unique three-verb line. |
| `A2.7` | `passed` | `examples/horcrx-003-founder/mission.md` sets `$66.60`, success ladder, abort criteria, and termination state. |
| `A2.8` | `passed` | `examples/horcrx-003-founder/ledger.md` declares knobs, ratios, and host-signs custody. |
| `A2.9` | `passed` | `examples/horcrx-003-founder/autonomy.md` enumerates HITL ladder, kill switch, ASI rung, no-trading invariant. |
| `A2.10` | `passed` | `examples/horcrx-003-founder/manifest.json` validates against `specs/vessel-format/manifest.schema.json`. |
| `A2.11` | `passed` | `examples/horcrx-003-founder/mark.svg` exists. |
| `A2.12` | `passed` | Founder skeleton folders and `.gitkeep`/policy files exist under `examples/horcrx-003-founder/`. |
| `A2.13` | `passed` | `examples/horcrx-003-founder/plugins/marketplaces.json` declares the allowed earning surfaces and fields. |
| `A2.14` | `passed` | `examples/horcrx-003-founder/wallets/addresses.json` is public-only / empty. |
| `A2.15` | `passed` | `examples/horcrx-003-founder/crons/jobs.json` keeps `enabled: false`. |
| `A2.16` | `passed` | Secret-scan scope includes `examples/horcrx-003-founder/` and found no blocked patterns. |
| `A3.1` | `passed` | `specs/hermes-binding/BINDING.md` contains the founder-vessel binding section. |
| `A3.2` | `passed` | `specs/hermes-binding/BINDING.md` §9 cross-check rows cover `voice`, `mission`, `ledger`, `autonomy`. |
| `A3.3` | `passed` | `specs/hermes-binding/BINDING.md` §10.3 enumerates the declarative earning surfaces. |
| `A4.1` | `passed` | `specs/hermes-binding/open-questions-resolved.md` ADR 12 is `accepted`. |
| `A4.2` | `passed` | ADR 13 is `accepted` and carries a Signed-off-by HITL placeholder. |
| `A4.3` | `passed` | ADR 14 is `accepted`. |
| `A4.4` | `passed` | ADR 15 is `accepted` and carries a Signed-off-by HITL placeholder. |
| `A4.5` | `passed` | ADR 16 is `accepted`. |
| `A4.6` | `passed` | ADR 17 is `accepted` and carries a Signed-off-by HITL placeholder. |
| `A4.7` | `passed` | ADR 18 is `accepted` and carries a Signed-off-by HITL placeholder. |
| `A4.8` | `passed` | ADR 19 is `accepted`. |
| `A4.9` | `passed` | No ADR in the 12..19 range is marked `accepted-pending-HITL`. |
| `A5.1` | `passed` | `validation/F-A-founder-vessel-WORKER-COMPLETE.md` enumerates files, F-A-09 fix-forward commits, HITL decisions, deferrals, and assumptions. |
| `A5.2` | `passed` | `docs/roadmap/ROADMAP.md` marks Phase 0 complete and adds the Mission A line. |
| `A5.3` | `deferred` | `gh pr list --state open --head foundation/founder-vessel --json url,number,title` returned `[]`; F-A-07 opens the PR. |
| `A5.4` | `deferred` | PR checks cannot exist until F-A-07 opens the PR and waits for CI. |
| `A5.5` | `passed` | Branch commit subjects are Conventional Commits; verified by `git log --pretty=%s origin/main..HEAD`. |
| `A5.6` | `deferred` | Remote push/force-push audit is completed with F-A-07 after the branch is updated on origin. |
| `A6.1` | `passed` | Branch is `foundation/founder-vessel`; mission commits are ahead of `origin/main` only. |
| `A6.2` | `passed` | `git config core.hooksPath` returns `.githooks`. |
| `A6.3` | `passed` | All edited paths are under `/Users/rudlord/HORCRX/`; no writes were made to off-repo surfaces. |
| `A6.4` | `passed` | `git diff --name-only origin/main..HEAD -- packages/design-system` is empty. |
| `A6.5` | `passed` | `git diff --name-only origin/main..HEAD -- specs/hermes-webapi-backup` is empty. |
| `A6.6` | `passed` | Secret scan over founder/spec/binding paths returned clean. |
| `A6.7` | `passed` | Voice-lint passed on `SOUL.md`, candysoul/orbel founder identity files, and founder `voice.md`. |
| `A6.8` | `passed` | `CHANGELOG.md`, `docs/roadmap/ROADMAP.md`, `specs/hermes-binding/BINDING.md`, `WORKER-COMPLETE.md`, and `validation/F-A-founder-vessel-WORKER-COMPLETE.md` passed the UTF-8 + LF check. |
| `A6.9` | `passed` | Repo-root `WORKER-COMPLETE.md` is overwritten for this mission in the close-artifact phase. |
| `A6.10` | `passed` | `CHANGELOG.md` now has populated `## [Unreleased]` notes for the founder mission. |
| `A6.11` | `deferred` | No direct-push-to-main audit closes with F-A-07 remote actions. |
| `A6.12` | `deferred` | PR body references are validated once F-A-07 opens the PR. |
| `A6.13` | `passed` | Unrelated untracked operator-state files remain unadded in `git status --short`. |

## Files changed in this mission branch

- `/Users/rudlord/HORCRX/CHANGELOG.md`
- `/Users/rudlord/HORCRX/docs/roadmap/ROADMAP.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/manifest.json`
- `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/VOICE-DEFERRAL.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/agents.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/autonomy.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/briefs/daily/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/briefs/retros/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/briefs/weekly/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/crons/jobs.json`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/dreams.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/governance/policies.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/intuition.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/ledger.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/ledger/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/manifest.json`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/mark.svg`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/memory/canon.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/memory/grafts/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/mission.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/mission/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/notify/policy.json`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/observability/metrics-names.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/plugins/marketplaces.json`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/principles.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/skills/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/soul.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/traces/.gitkeep`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/voice.md`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/wallets/addresses.json`
- `/Users/rudlord/HORCRX/examples/horcrx-003-founder/workflows/.gitkeep`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/open-questions-resolved.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/autonomy-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/ledger-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/manifest.schema.json`
- `/Users/rudlord/HORCRX/specs/vessel-format/mission-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/voice-md.schema.md`
- `/Users/rudlord/HORCRX/WORKER-COMPLETE.md`
- `/Users/rudlord/HORCRX/validation/F-A-founder-vessel-WORKER-COMPLETE.md`

## F-A-09 fix-forward commits

- `445ea28 feat(spec): rename founder ledger knobs to short form`
- `4e5e472 docs(spec): clarify forbidden_actions as the no-trading invariant`
- `789ca68 docs(examples): add pack-level voice deferral note`

## Operator HITL decisions

| Decision | Surface | Current state | Stamp / note |
|---|---|---|---|
| Three-verb mission line | `examples/horcrx-003-founder/voice.md` | PENDING-HITL | `earn through making · move through earliness · compound through audit` (proposed; surfaced for PR review) |
| OQ-13 cap scale | `specs/hermes-binding/open-questions-resolved.md` ADR 13 | `accepted` | "pending operator hitl on treasury-relative cap scale (`1% / 5% / 15%`); surfaced in commit and PR checklist" |
| OQ-15 termination state | `specs/hermes-binding/open-questions-resolved.md` ADR 15 | `accepted` | "pending operator hitl on final conjunction shape for termination criteria; surfaced in commit and PR checklist" |
| OQ-17 spend-mix ratios | `specs/hermes-binding/open-questions-resolved.md` ADR 17 | `accepted` | "pending operator hitl on spend-mix ratios (`≤30 / ≥50 / ≤20`); surfaced in commit and PR checklist" |
| OQ-18 marketplace allowlist | `specs/hermes-binding/open-questions-resolved.md` ADR 18 | `accepted` | "pending operator hitl on marketplace allowlist additions; surfaced in commit and PR checklist" |

## Assumptions

- The existing top-level `## [Unreleased]` block in `CHANGELOG.md` should be populated rather than duplicated.
- PR creation, PR body references, and CI-on-PR checks are owned by F-A-07, so assertions A5.3, A5.4, A6.11, and A6.12 stay deferred in this report.
- Untracked packet and recon files (`docs/roadmap/mission-A-horcrx-003-founder-vessel.md`, `research/10-rags-to-riches-recon.md`, `research/11-harness-landscape.md`) are operator state and remain unstaged per HERMES-01.
- Mission B artifacts (`docs/roadmap/mission-B-hardening-pass.md`, `research/12-hardening-recon.md`, `specs/hermes-webapi-backup/`) remain untouched and out of scope for F-A-06.
- The operator still decides whether post-merge versioning becomes `v0.2.0-foundation` or `v0.1.2`; this worker did not cut or move any tag.

## Off-limits cross-check

- No writes to `packages/design-system/`; `git diff --name-only origin/main..HEAD -- packages/design-system` returned empty output.
- No writes or deletions in `specs/hermes-webapi-backup/`; `git diff --name-only origin/main..HEAD -- specs/hermes-webapi-backup` returned empty output.
- No writes to `~/.hermes/`, `~/wiki/`, `~/.claude-worktrees/ATLAS/`, or `~/.factory/skills/`; every touched path listed above stays under `/Users/rudlord/HORCRX/`.
- HERMES-01 honored: `docs/roadmap/mission-B-hardening-pass.md`, `research/12-hardening-recon.md`, and `specs/hermes-webapi-backup/` remain unstaged operator state.

## Open follow-ups

- F-A-07 must push `foundation/founder-vessel`, open the PR, verify the PR body references, and wait for green CI checks.
- F-A-08 must synthesize the per-surface validator results into `library/validator-synthesis.md` and update `validation-state.json`.
- Final operator review still owns the three-verb mission line plus OQ-13, OQ-15, OQ-17, and OQ-18 confirmation at PR review.
