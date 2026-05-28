# 12 — Hardening Recon (parallel-mission scoping)

Mission scope: scoping recon for a hardening pass over HORCRX's documentation, wiki strategy, access controls, memory + traces, apps surface, marketplace surfaces, and validation rigor — so the system can scale without leakage or drift.

Read-only. Every finding cites absolute repo paths plus, where useful, the spec section/line behind the claim. No production code is proposed; this is mission scoping for a later worker swarm.

Repo head at recon: `99be6a7` (post-`v0.1.1`). Worktree shows `M WORKER-COMPLETE.md` and an untracked `specs/hermes-webapi-backup/` directory (FastAPI scaffold) that does not belong under `specs/` and is contradictory with the foundation-only operator contract in `/Users/rudlord/HORCRX/AGENTS.md`. Flagged in Section C.

---

## Section A — Documentation gap map

Each row = area → current state in repo → severity → suggested remedy.

| Area | Current state (absolute paths + section/lines) | Severity | Suggested remedy |
|---|---|---|---|
| Developer onboarding | `/Users/rudlord/HORCRX/README.md` (lines 1–32) is a 32-line landing; `/Users/rudlord/HORCRX/CONTRIBUTING.md` (lines 1–40) covers branch + commit but not local dev install, hook bootstrap drift, or CI failure triage. `/Users/rudlord/HORCRX/docs/infrastructure/local-dev.md` (lines 1–134) is explicitly "a spec for future worker setup, not a runnable compose file". | High | Add `docs/onboarding/` with: `01-clone-and-hooks.md`, `02-run-validators.md`, `03-troubleshoot-ci.md`, `04-mission-checklist.md`. Pull hook bootstrap (`git config core.hooksPath .githooks`) out of `AGENTS.md` (line 31) into a top-level developer checklist. |
| Runtime ops manual | Not present. `/Users/rudlord/HORCRX/docs/infrastructure/services.md` (lines 1–120) defines the service catalog but no SOPs (deploy/rollback/incident). | High | Add `docs/ops/RUNBOOK.md` with sections per service (registry indexer, content gateway, signing service, x402 facilitator, search/discovery) — even as "future-worker spec", explicitly distinguishing "spec" vs "live runbook." |
| Security model | Solid table in `/Users/rudlord/HORCRX/docs/infrastructure/security.md` §2 (lines 31–43) and `/Users/rudlord/HORCRX/SECURITY.md` (lines 1–32). Threat model is good; reporting contact is a placeholder (`SECURITY.md` line 9 "security@horcrux.dev (placeholder; replace with real contact)"). Signing key fingerprint section is also a stub (line 14). | High | Replace placeholders with a real intake channel (operator decision); publish first vessel-signing-key fingerprint when a key exists; add a "supply chain" section covering dependency surface (Dependabot in `/Users/rudlord/HORCRX/.github/dependabot.yml`) and lockfile reproducibility expectations. |
| Threat model | `/Users/rudlord/HORCRX/docs/infrastructure/security.md` §2 covers 8 threat classes. Missing: insider/operator compromise; CI runner compromise; package-registry MITM; manifest-CID collision corner cases; off-chain royalty resolver bias attacks. | Medium | Extend the security threat matrix to STRIDE coverage; add an explicit row per CI surface and per third-party adapter (Faremeter, IPFS, Arweave, Helius, Alchemy, R2). |
| Release process | `/Users/rudlord/HORCRX/.github/workflows/release.yml` (28 lines) drafts on tag push but does not publish. `/Users/rudlord/HORCRX/CHANGELOG.md` is maintained by hand; `WORKER-COMPLETE.md` lines 32–35 flags drafts are still in Draft state. No documented "how to cut a release" doc. | High | Add `docs/release/RELEASING.md` covering: pre-tag checklist (validators green, schemas validate, changelog updated, no secret leak), tag format, draft → publish promotion, signing posture for future signed releases, post-release cleanup of helper branches. |
| Marketplace operator runbook | Not present. `/Users/rudlord/HORCRX/specs/marketplace/ARCHITECTURE.md` §2 names eight services but no operator-side procedures (listing approval, takedown, dispute intake, refund/escrow hold). | High | Add `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md`. Spec the operator workflows that match `/Users/rudlord/HORCRX/specs/marketplace/ip-preservation.md` §6.1–§6.4 dispute pipeline. |
| IP-preservation policy | Good spec coverage in `/Users/rudlord/HORCRX/specs/marketplace/ip-preservation.md` (lines 1–124) and `/Users/rudlord/HORCRX/specs/marketplace/royalties.md` (lines 1–116). Missing: machine-readable policy schema, jurisdiction posture, takedown SLA, evidence-retention period. | Medium | Add `specs/marketplace/policy-schema.md` + JSON Schema sibling to `royalties.md` table §5, and `docs/policy/legal-posture.md` explicitly bracketing the "not legal claims" boundary already stated in `next-missions.md` Phase 7 off-limits. |
| Hermes binding hard-constraint audit | `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §9 (the 14-row cross-check) is the strongest single piece in the corpus. ADR-11 (iteration budget) flagged in `/Users/rudlord/HORCRX/specs/hermes-binding/open-questions-resolved.md` lines 168–192 still depends on Phase 1 to verify runtime parity. | Low | Keep as-is until Phase 1 verifies runtime; ensure hardening mission tracks ADRs 01–11 status transition from `accepted-pending-HITL` to `accepted`. |
| Memory split spec coverage | `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md` (lines 1–48) covers include/strip/re-inject but only at table level. No PII redaction tier definitions, no graft provenance schema, no operator-consent record format. | Medium | Add `specs/vessel-format/memory-graft-provenance.md` defining how `memory/grafts/*.md` carry parent_cid lineage and consent metadata (referenced but unspecified in `memory-split.md`). |
| Traces format coverage | `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md` (lines 1–88) specifies NDJSON event shape + redaction. Missing: retention policy, append-only enforcement, line-canonicalization rule (LF, ordering), max line size, schema-version field. | Medium | Add retention/append-only section; add `schema_version` to the required event schema; mirror NDJSON canonicalization rules from `SPEC.md` §5.1 to traces files. |
| Validation contract index | Refs to `VAL-VESSEL-14` (in `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §5.1 line 89), `VAL-HERMES-01..10`, `VAL-VESSEL-13` (in `/Users/rudlord/HORCRX/validation/F03-WORKER-COMPLETE.md`) exist but no single index file enumerates the full VAL-* contract. `CONTRIBUTING.md` line 24 references "the validation contract lives at the mission artifact path" — i.e. external, not in repo. | High | Add `validation/VAL-INDEX.md` enumerating every `VAL-*` ID, the spec section it tests, current coverage status, and the test/fixture that exercises it. Without this, the PR template (`/Users/rudlord/HORCRX/.github/PULL_REQUEST_TEMPLATE.md` lines 15, 22) cannot be honestly completed. |
| Reference vessel coverage | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/manifest.json` is full; `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/manifest.json` is sparse (only `multi_agent` + `mark` slots — the five member vessels are referenced by CID but their manifests are not actually rendered as JSON in the pack subdirs; see `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/` LS). | Medium | Either materialize per-member manifests or document that the pack-member manifests live elsewhere; ensure the CID values in `manifest.json` lines 80–95 are provable from local sources. |
| Brand & voice canon | `/Users/rudlord/HORCRX/packages/design-system/VOICE.md` is canonical; CI guards root `SOUL.md` only (`/Users/rudlord/HORCRX/.github/workflows/ci.yml` lines 75–79: `voice-lint` step). No lint over `packages/design-system/VOICE.md` itself or per-vessel `voice.md` files. | Low | Extend `voice-lint` to assert: no `/Users/`, `git `, `npm ` in any `*soul*.md` and any `voice.md` under `examples/`. |
| docs/roadmap currency | `/Users/rudlord/HORCRX/docs/roadmap/ROADMAP.md` Phase 0 still says "complete when this worker's validation table is accepted for `v0.1.0-foundation`." Now post-`v0.1.1`, the doc still reads as foundation-pre-close. | Low | Update Phase 0 to "Complete — `v0.1.0-foundation` released 2026-05-26, `v0.1.1` deps roll 2026-05-27". Add a "next mission" pointer block at the top of ROADMAP for parallel hardening. |
| README discoverability | `/Users/rudlord/HORCRX/README.md` does not link to `SECURITY.md`, `CONTRIBUTING.md`, `validation/`, `research/INDEX.md`, or `docs/infrastructure/security.md`. | Low | Add a "Security & Operator Contract" subsection in README with the four links and a "report a vulnerability" CTA. |

---

## Section B — Wiki + canon hardening recommendations

### B.1 HORCRX-specific wiki vs `~/wiki` (the operator vault)

`/Users/rudlord/wiki/AGENTS.md` and `/Users/rudlord/wiki/_meta/commit-standards.md` clearly establish `~/wiki` as the **operator's personal multi-system canon** (Hermes/Claude/Codex doctrine). HORCRX wiki notes already exist (`/Users/rudlord/wiki/concepts/horcrx-protocol.md`, `/Users/rudlord/wiki/entities/horcrx.md`, `/Users/rudlord/wiki/_HORCRX/`).

Recommendation: **keep them separate, with a one-way bridge**.

- `~/wiki` stays the operator vault. Wiki writes from HORCRX missions remain reserved for the dedicated wiki-librarian mission (per AGENTS.md off-limits line: "Wiki writes are reserved for the dedicated librarian mission and must follow the wiki gate process").
- HORCRX maintains its own `docs/` tree (already does — `/Users/rudlord/HORCRX/docs/infrastructure/`, `/Users/rudlord/HORCRX/docs/roadmap/`) as the **product wiki**. Cross-link, do not cross-write.
- Promote stable HORCRX doctrine to `~/wiki/entities/horcrx.md` and `~/wiki/concepts/horcrx-protocol.md` only through the wiki-librarian gate process documented in `/Users/rudlord/wiki/_meta/commit-standards.md` §1 (`doctrine`, `entity`, `concept`, `intake`, `index`) and the GATE-01..08 sequence referenced from `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 row 11.

### B.2 Harden `_meta` surface (the operator vault, read-only from HORCRX side)

`/Users/rudlord/wiki/_meta/canonical-pages.txt` and `/Users/rudlord/wiki/_meta/commit-standards.md` are the load-bearing files. They are not under HORCRX control but HORCRX missions must:

1. **Never write to `_meta/canonical-pages.txt`** outside GATE-07 (already documented).
2. **Read `_meta/commit-standards.md` §3 branch discipline before push** — HORCRX repo already mirrors it (`/Users/rudlord/HORCRX/.githooks/pre-push`).
3. **Honor frontmatter key order** (referenced from `_meta/commit-standards.md` §5) when (and only when) the wiki-librarian mission edits a HORCRX-related canon page.

### B.3 HORCRX-internal wiki hygiene rules (proposed)

To prevent HORCRX's own `docs/` from drifting into an undisciplined dump:

1. **Canonical-pages allowlist**: add `/Users/rudlord/HORCRX/docs/CANONICAL.md` enumerating which docs are operator-canon (so future PRs cannot silently add docs/ files without listing them). Mirror `~/wiki/_meta/canonical-pages.txt` pattern.
2. **Frontmatter rule**: require minimum frontmatter on every `docs/**.md`: `title`, `version`, `updated`. Today none of the docs have frontmatter (`/Users/rudlord/HORCRX/docs/infrastructure/security.md` starts directly with `# Security and threat model` / `Version: v0.1-draft`).
3. **Link-resolution gate**: `/Users/rudlord/HORCRX/.github/workflows/ci.yml` already has `markdown-link-check` (lines 47–82). Extend it to fail on absolute paths that do not resolve under repo root (currently it skips externals; tighten to also flag `~/wiki/...` references that are not annotated as "wiki" sources).
4. **Voice doctrine surface**: extend `voice-lint` (ci.yml lines 75–79) to also lint `packages/design-system/VOICE.md` and any `examples/*/voice.md` — same operator/no-shell-commands rule.

---

## Section C — Access/secrets/CI threat model

### C.1 Concrete findings

| Finding | Evidence (absolute paths + lines) | Risk | Recommended action |
|---|---|---|---|
| Branch protection is spec-only, not enforced | `/Users/rudlord/HORCRX/.github/branch-protection.md` (whole file, 33 lines); `/Users/rudlord/HORCRX/WORKER-COMPLETE.md` line 56–60: "no active branch-protection rule on `main` at the GitHub API level". | High — direct-push to `main` is currently blockable only by the local `pre-push` hook (`/Users/rudlord/HORCRX/.githooks/pre-push`), which only fires for clients that ran `git config core.hooksPath .githooks`. | Apply the documented protection via `gh api` (or web UI). Required contexts: `ci/commitlint`, `ci/schema-validate`, `ci/markdown-link-check`. Add `ci/voice-lint` (currently missing from `branch-protection.md` lines 11–13 even though it is in `ci.yml`). |
| CODEOWNERS is single-operator | `/Users/rudlord/HORCRX/.github/CODEOWNERS`: `* @chipoto69`. | Medium — single-point of code-review (acceptable for foundation, fragile at scale). | Plan a transition to per-area teams (`/specs/` to a specs team, `/contracts/` to a contracts team) once the team exists; document in `docs/release/RELEASING.md`. |
| CI runners have no pinned action SHAs | `/Users/rudlord/HORCRX/.github/workflows/ci.yml` uses floating major tags (`actions/checkout@v6`, `actions/setup-node@v4` line 53 — note: `ci.yml` mixes `@v6` on lines 17, 48, 54, 80 with `@v4` for `setup-node` on line 53). | Medium — supply-chain bias if an action's `vN` tag is force-moved by attacker. | Pin to commit SHAs via Dependabot's pinning support; resolve the `setup-node` version inconsistency (release.yml line 17 uses `@v6` while ci.yml line 53 uses `@v4`). |
| `pre-push` hook checks only `main`, not other protected refs | `/Users/rudlord/HORCRX/.githooks/pre-push` lines 2–7 hard-codes `refs/heads/main`. No protection for future release branches or tags. | Low | Either keep as-is + rely on remote protection, or extend pattern to cover `refs/tags/v*` and any future `release/*` branches. |
| Commit-msg hook does not block fixup/WIP subjects | `/Users/rudlord/HORCRX/.githooks/commit-msg` line 3 regex accepts any `feat|fix|docs|chore|build|ci|refactor|test|polish` prefix; mirrors `ci.yml` line 21 but does not block `chore(wip):` or `fix(tmp):`. | Low | Add a deny-list for `scope` containing `wip`, `tmp`, `temp`, `fixup`. |
| Untracked `specs/hermes-webapi-backup/` violates AGENTS.md | `/Users/rudlord/HORCRX/specs/hermes-webapi-backup/` (FastAPI app code with routers, models, sessions, CORS middleware reading `HERMES_CORS_ORIGINS`). `/Users/rudlord/HORCRX/AGENTS.md` line 8: "HORCRX is foundation-first ... specs, roadmaps, examples, and validation evidence only until a later implementation phase explicitly authorizes production code." | Medium | Move this directory out of `specs/` into either `research/` (if recon) or delete it entirely (it's untracked and looks like an accidental drop). The path inside `specs/` will mislead future workers into thinking it's authored HORCRX canon. |
| Secret-flow paths not enumerated anywhere | `/Users/rudlord/HORCRX/SECURITY.md` line 9 "security@horcrux.dev (placeholder)". No file enumerates: which CI secrets exist (none currently — GH UI not inspected), which runtime secrets later services will need, where keys live during signing flow (`/Users/rudlord/HORCRX/docs/infrastructure/security.md` §3.3 says "Signing stays isolated" but does not say where keys are custodied). | High | Add `docs/security/SECRETS.md` listing intended secret stores (per surface), explicit "shell env, not `.env`" rule (already in `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 row 1), and forbid checking any `.env` into the repo (already enforced by `.gitignore` line 2 — but `!.env.example` exception on line 4 needs an explicit "must not contain real values" doc). |
| No secret-scanner gate in CI | `ci.yml` has no `trufflehog`, `gitleaks`, or `git-secrets` job. `.gitignore` line 2 ignores `.env` only; nothing prevents a worker from committing a `secrets.json`, `wallet.json`, or pasted token inside a markdown file. | High — directly contradicts the "no secrets" off-limit in `/Users/rudlord/HORCRX/AGENTS.md`. | Add a `ci/secret-scan` job. Suggested: `trufflesecurity/trufflehog-actions-scan`. Pin by SHA. |
| No SBOM / dependency provenance | `/Users/rudlord/HORCRX/package.json` is minimal (one devDep: `turbo`). Dependabot covers npm + github-actions (`/Users/rudlord/HORCRX/.github/dependabot.yml`). No SBOM generation for the eventual implementation packages. | Low (now), High (after Phase 1) | Add SBOM generation as a Phase 1 hardening gate, not now. |
| Token paths in future Hermes binding | `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md` §2 (mcp auth headers row, lines 30–34) handles the most dangerous credentials (`Authorization`, `*_TOKEN`, `model.api_key`). Coverage looks correct; **no** gap there. | None | Keep as-is. Implementation worker must enforce. |
| Hermes audit NDJSON not yet portable | `/Users/rudlord/HORCRX/docs/infrastructure/observability.md` §4 specifies the runtime correlation fields, but does not state retention, max line size, or rotation policy for the future `<profile>/logs/hermes-audit.ndjson` export. | Medium | Specify rotation + max-line-size + redaction-validation in `docs/infrastructure/observability.md` §1.2; add `--include-audit` redaction contract reference to `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md` §5. |

### C.2 Where tokens/keys flow (intended, today, all spec-only)

1. **Vessel signing keys**: isolated signing service (per `/Users/rudlord/HORCRX/docs/infrastructure/services.md` §3.3) — NEVER on public preview node. Today: undefined. No fingerprint published (`SECURITY.md` line 12 stub).
2. **x402 facilitator nonce/replay store**: "durable replay store" per `docs/infrastructure/security.md` §2.1. Today: undefined.
3. **Operator wallet seeds / LLM keys**: shell env only per `BINDING.md` §8 row 1. **MUST never** appear in repo files.
4. **MCP bearer tokens**: stripped on export, re-injected from host (`strip-and-rehydrate.md` §2). Today: implementation pending.

No tokens or keys are present in the repo today. The risk is **forward** (when implementation lands) and **process** (no scanner enforces the absence).

---

## Section D — Memory + traces hardening (spec vs impl gaps)

### D.1 Memory spec gaps

| Topic | Spec coverage | Gap |
|---|---|---|
| Portable canon (`memory/canon.md`) | `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md` lines 9, 13–16 | No size cap, no canonicalization rule, no schema (free-form markdown). |
| Grafts (`memory/grafts/`) | `memory-split.md` line 14 "include with provenance" | Provenance schema not defined: which parent_cid? signed by whom? consent envelope? |
| `memories/USER.md` consent gate | `memory-split.md` line 16 "include only with explicit consent" | No consent-record format. Where is the consent stored? How is it later auditable? |
| Cross-vessel memory grafts | `BINDING.md` §4.3 "graft `memory-pack` --into <profile>" | Provenance write to `<profile>/state/vessel-lineage.sqlite` is specified (BINDING.md §4.4) but graft-level consent record is NOT specified. |
| Ephemeral session strip | `memory-split.md` lines 18–22, `strip-and-rehydrate.md` §4 | Coverage is complete. |
| Honcho/GBrain boundary | `memory-split.md` lines 24–25 | Re-bind path is named but not formalized. No "host-supplied bindings" schema. |

### D.2 Traces spec gaps

| Topic | Spec coverage | Gap |
|---|---|---|
| NDJSON event schema | `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md` lines 16–38 | No `schema_version` field, no max event size, no max file size before rotation, no append-only enforcement, no canonical line ordering. |
| Redaction enforcement | `traces-format.md` §"Redaction rules" lines 40–52 | "Allowed redaction styles" listed but **no automated linter / verifier** in `validation/`. Cannot prove a trace is redacted before export. |
| Encrypted envelope | `traces-format.md` lines 56–69 | `cipher_suite` enum is `age | x25519-xsalsa20-poly1305` — no AEAD test vector or key-id rotation rule. |
| Provenance source enum | `traces-format.md` `provenance.source: "dispatch|cron|workflow|manual"` (line 29) | OK. |
| Cross-runtime traces (non-Hermes) | `/Users/rudlord/HORCRX/specs/vessel-format/compatibility-matrix.md` row "Anthropic Skill" notes "not first-class" | Anthropic/Claude Code/Factory droid export semantics for traces not specified at all. |
| Audit join key | `docs/infrastructure/observability.md` §4.1 fields | `vessel_cid` is mandatory but `trace_file_path` / `event_id` correlation back to `hermes-audit.ndjson` rows is unspecified. |

### D.3 Provenance writes (BINDING.md §4.4)

Schema for `<profile>/state/vessel-lineage.sqlite` is in `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` lines 145–157. Append-only invariant is implicit ("Provenance is append-only history") but **not stated**. Hardening mission must:

1. Add explicit append-only constraint (no UPDATE/DELETE on lineage rows).
2. Add a row hash / chain hash so that later edits are detectable.
3. Specify how revocation (per `/Users/rudlord/HORCRX/specs/protocol/PROTOCOL.md` §3 "revocation") is recorded — likely a new lineage row marking the prior row revoked, never a delete.

---

## Section E — Apps + marketplace readiness audit

### E.1 Apps surface inventory

```
/Users/rudlord/HORCRX/apps/
└── brand/                  (only entry)
    ├── README.md           # symlink wrapper
    ├── index.html          → ../../packages/design-system/applications/landing.html
    ├── preview/            → ../../packages/design-system/preview
    ├── assets/             → ../../packages/design-system/assets
    ├── fonts/              → ../../packages/design-system/fonts
    └── colors_and_type.css → ../../packages/design-system/colors_and_type.css
```

Status:

- `apps/brand/` is a thin static wrapper. No product app exists.
- `docs/roadmap/ROADMAP.md` Phase 3 (web marketplace UI) and `next-missions.md` Phase 3 are the first real app surfaces.
- No `apps/api/`, `apps/marketplace-api/`, or `apps/marketplace-ui/` directory yet — the migration table at `/Users/rudlord/HORCRX/docs/roadmap/migration-from-knowledge-horcrux.md` lines 16, 21 only **destines** them there.

### E.2 First user-facing app — what foundation must give it

For Phase 3 (web marketplace UI per `next-missions.md` lines 79–98) to be unblocked, foundation must already provide:

| Foundation piece | Where today | Ready? |
|---|---|---|
| Manifest JSON Schema | `/Users/rudlord/HORCRX/specs/vessel-format/manifest.schema.json` | ✅ |
| Listing data shape (registry projection) | `/Users/rudlord/HORCRX/specs/protocol/registry-design.md` only describes split, not row schema | ❌ — needs `specs/registry/listing.schema.json` |
| Preview policy enumeration | `/Users/rudlord/HORCRX/specs/marketplace/ip-preservation.md` §5 table (lines 96–101) lists `public | preview | restricted` | ✅ at concept level; ❌ at schema level |
| Trust badge taxonomy | `/Users/rudlord/HORCRX/specs/marketplace/discovery-and-trust.md` §3 lines 49–58 names six badge classes | ✅ |
| Royalty policy shape | `/Users/rudlord/HORCRX/specs/marketplace/royalties.md` §5 table (lines 73–82) | ✅ |
| Reference fixtures | `examples/horcrx-001-candysoul/` + `examples/horcrx-002-orbel-pack/` | ⚠️ Pack reference is sparse (see Section A row "Reference vessel coverage"). |
| MCP server shape | `/Users/rudlord/HORCRX/specs/marketplace/ARCHITECTURE.md` §3.8 lines 79–82 names tools but no JSON-RPC schema | ❌ — Phase 4 dependency. |
| Wallet adapter mock | Not present | ❌ — Phase 3 risk if Crossmint/Privy spec is not pre-shaped. |

### E.3 Marketplace hardening — must lock before any listing goes live

| Concern | Today | Lock-down recommendation |
|---|---|---|
| IP — signing keys published | Stub in `SECURITY.md` line 12 ("Once first production vessel signing key is established...") | Publish key fingerprint + signing service URL + revocation procedure before listing #1 |
| Royalties — payout target validation | `/Users/rudlord/HORCRX/specs/marketplace/royalties.md` §5 allows arbitrary `payout_target` strings | Require `payout_target` to be a chain-typed identifier (e.g. `evm:0x...` or `solana:...`) with chain adapter verification before listing publishes |
| Discovery — search ranking auditability | `/Users/rudlord/HORCRX/specs/marketplace/discovery-and-trust.md` §6 blended score | Need a "ranking transparency" doc: which signals weight how much, and how to challenge a ranking |
| Trust — anti-Sybil ruleset | `discovery-and-trust.md` §4 lines 76–82 names controls | Need a concrete rate-limit + reviewer-eligibility schema before reviews go live |
| Dispute — intake SLA | `ip-preservation.md` §6.1–6.4 | Needs a published response-time SLA + freeze rule + reviewer rotation |
| Takedown — irreversibility | `ip-preservation.md` §6.4 "registry should never erase history; should add dispute and resolution state" | Need an explicit "revocation never deletes" enforcement test (cross-ref with PROTOCOL.md §2.6, §3 revocation) |
| Deepfake — voice/likeness gating | `discovery-and-trust.md` §5 KYC-light tier | Need a "high-risk slot type" enum and forced badges before voice/likeness listings can publish |
| Cross-chain symmetry | `chain-adapters.md` §4 symmetry rules | Need a property-test suite proving Base and Solana adapters expose equivalent operations |
| Encrypted envelopes | `SPEC.md` §5.2; `traces-format.md` §"Encrypted envelope" | Need a test vector + KAT (known-answer test) for `age` and `x25519-xsalsa20-poly1305` |
| Preview integrity | `docs/infrastructure/security.md` §2.1 row "Gateway/cache poisoning" | Need "re-hash on fetch" verifier as a property test, with golden fixtures |

---

## Section F — Validation + verification gaps with proposed gates

### F.1 What `validation/` actually contains today

`/Users/rudlord/HORCRX/validation/F03-WORKER-COMPLETE.md` — single worker report. **No scripts, no fixtures, no property tests, no JSON Schema test runner, no signature-roundtrip checker.** The validation directory is documentation, not enforcement.

`/Users/rudlord/HORCRX/.github/workflows/ci.yml` currently enforces:

1. `commitlint` (lines 13–34) — subject regex.
2. `schema-validate` (lines 36–46) — `ajv` against the two example manifests.
3. `markdown-link-check` (lines 47–82) — internal links only.
4. `voice-lint` (lines 75–79) — root SOUL.md identity-only check.

That is the entire enforced contract. Everything else is spec text.

### F.2 Missing validators

| Missing validator | What it should assert | Reference |
|---|---|---|
| Manifest deterministic round-trip | Pack→Bundle→Unpack→repack reproduces same CID | `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §5.1 (VAL-VESSEL-14) |
| Signature roundtrip | Ed25519 sign/verify across manifest + per-slot signatures | `signing-and-lineage.md` §"Per-slot signing" |
| Parent CID lineage chain | `parent_cids[]` resolve to existing manifests, no cycles, no missing parents | `signing-and-lineage.md` §"Parent CID lineage" |
| Strip-and-rehydrate property test | Apply strip rules to a known Hermes profile fixture; assert no `.env`, `auth.json`, `state.db`, `sessions/`, `logs/` survive | `strip-and-rehydrate.md` §2 |
| Trace redaction property test | Given a trace with embedded secrets, redact + assert no leakage | `traces-format.md` §"Redaction rules" |
| x402 nonce replay test | Replayed proof is rejected | `payment-layer.md` §2 |
| Royalty resolution determinism | Same lineage input → identical payout plan | `royalties.md` §2.2 |
| Chain adapter symmetry | Base and Solana both expose `publishRecord`, `transferRecord`, ... | `chain-adapters.md` §1, §4 |
| Frontmatter / canonical-pages lint | (See Section B.3) | proposed |
| Secret scan | Whole-repo gitleaks/trufflehog | proposed (Section C.1) |

### F.3 Proposed gates (analogous to content-os GATE-01..08)

Patterned on `/Users/rudlord/wiki/_meta/commit-standards.md` GATE-07 + `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 row 11.

| Gate | Name | Enforces |
|---|---|---|
| **GATE-HX-01** | conventional-commits | already enforced (`ci.yml` commitlint + `.githooks/commit-msg`) |
| **GATE-HX-02** | secret-scan | new — block any commit containing high-entropy strings, `BEGIN PRIVATE KEY`, BIP-39 seeds, `sk_live_`, etc. |
| **GATE-HX-03** | manifest-schema | already enforced (`ci.yml` schema-validate) |
| **GATE-HX-04** | signature-roundtrip | new — every manifest in `examples/` round-trips sign→verify |
| **GATE-HX-05** | parent-cid-resolves | new — every `parent_cids[]` entry resolves to an in-repo or whitelisted external manifest |
| **GATE-HX-06** | strip-rehydrate | new — fixture Hermes profile passes strip rules; no host-bound paths survive |
| **GATE-HX-07** | wiki-allowlist | new — any file added under `docs/` is on `docs/CANONICAL.md` allowlist (see B.3 §1) |
| **GATE-HX-08** | voice-lint extended | new — `voice-lint` extended to `packages/design-system/VOICE.md`, all `examples/*/voice.md` and `examples/*/soul.md` |

Recommend pinning each gate to a Conventional-Commits scope (e.g., `feat(gate): add HX-05 parent-cid-resolves`) so the trail of how gates landed is auditable.

---

## Section G — Proposed mission phases

Same style as `/Users/rudlord/HORCRX/docs/roadmap/next-missions.md`. Five-to-eight phases for a parallel **hardening mission** that runs alongside (not in place of) Phases 1–8 already in `next-missions.md`.

Universal off-limits: read-only against `~/wiki/`, no live Hermes profile writes, no remote pushes without explicit operator approval, no contract deploy, no secrets in repo.

---

### Phase H1 — secrets, hooks, branch protection

**Mission**: lift the local-hook security posture to enforced remote posture.

**Acceptance criteria**:

- `gh api` applies `/Users/rudlord/HORCRX/.github/branch-protection.md` rules to `main` (operator-approved).
- New CI job `ci/secret-scan` (`trufflehog` or `gitleaks`, SHA-pinned) blocks high-entropy strings, private-key blobs, BIP-39 seeds.
- `voice-lint` extended to lint `packages/design-system/VOICE.md`, every `examples/*/voice.md` and `examples/*/soul.md`.
- `branch-protection.md` lists `ci/voice-lint` and `ci/secret-scan` in required contexts.
- `pre-push` hook extended to block force-push on any branch (not just `main`).
- `commit-msg` hook deny-list adds `wip`, `tmp`, `temp`, `fixup`.
- Untracked `specs/hermes-webapi-backup/` is moved out of `specs/` or deleted (operator decision).
- All GitHub Actions pinned to commit SHAs via Dependabot.

**Off-limits**: no operator-secret intake channels published until the security@horcrux.dev contact is real; no signing-key fingerprint published until a real key exists; no public org-wide rule changes outside this repo.

**Recommended worker topology**: solo security worker + operator HITL for branch-protection apply.

---

### Phase H2 — validation contract + GATE chain

**Mission**: stand up the GATE-HX-01..08 chain (Section F.3) and the VAL-INDEX (Section A row "Validation contract index").

**Acceptance criteria**:

- `/Users/rudlord/HORCRX/validation/VAL-INDEX.md` enumerates every `VAL-*` ID, links to spec section + test fixture.
- `validation/scripts/` has runnable scripts for: GATE-HX-04 signature-roundtrip, GATE-HX-05 parent-cid-resolves, GATE-HX-06 strip-rehydrate (fixture Hermes profile), GATE-HX-07 docs-allowlist, GATE-HX-08 extended voice-lint.
- Each gate is wired into `.github/workflows/ci.yml` as a separate job.
- `branch-protection.md` updated to include all new CI contexts.
- Property test for x402 nonce replay (using a stub facilitator) is in place.
- Royalty-resolution determinism test runs against golden fixtures.

**Off-limits**: do not generate any production keys, do not pay any third-party services, do not deploy any contracts.

**Recommended worker topology**: validator/evaluator + builder + operator HITL on gate names + final CI matrix.

---

### Phase H3 — docs onboarding + ops runbook

**Mission**: close every High-severity row in Section A documentation gap map.

**Acceptance criteria**:

- `docs/onboarding/01-clone-and-hooks.md`, `02-run-validators.md`, `03-troubleshoot-ci.md`, `04-mission-checklist.md` exist.
- `docs/ops/RUNBOOK.md` exists with one section per service from `docs/infrastructure/services.md` §2 catalog.
- `docs/release/RELEASING.md` exists describing tag → draft → publish flow.
- `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md` exists describing dispute intake, listing approval/takedown, royalty payout dispute, deepfake escalation.
- `docs/security/SECRETS.md` enumerates intended secret stores per surface.
- `docs/CANONICAL.md` lists every doc explicitly (allowlist for GATE-HX-07).
- README extended with the new doc links and a security contact CTA.

**Off-limits**: do not edit the inherited brand canon (`packages/design-system/`); do not modify `SOUL.md` or `VOICE.md`; do not invent legal claims (Phase 7 already off-limits that).

**Recommended worker topology**: docs worker + design-system reviewer + operator HITL on legal posture text.

---

### Phase H4 — memory + traces spec hardening

**Mission**: close the Section D gaps.

**Acceptance criteria**:

- `specs/vessel-format/memory-graft-provenance.md` defines graft provenance + consent record schema.
- `specs/vessel-format/traces-format.md` adds `schema_version`, max-line-size, append-only invariant, rotation rule, redaction-validator contract.
- `specs/hermes-binding/BINDING.md` §4.4 (lineage SQLite schema) gains an explicit append-only constraint + per-row chain-hash field.
- A redaction-validator script lands in `validation/scripts/` and is wired as a GATE.
- AEAD test vectors / KATs for `age` and `x25519-xsalsa20-poly1305` are present and run in CI.
- Non-Hermes-runtime trace export semantics (Claude Code / Factory droid / Anthropic Skill) added to `compatibility-matrix.md`.

**Off-limits**: do not touch live audit files under `~/.hermes/`; no operator session imports.

**Recommended worker topology**: memory/traces specialist + cryptography reviewer.

---

### Phase H5 — marketplace pre-launch lockdown

**Mission**: close Section E.3 lockdown table before any listing can publish.

**Acceptance criteria**:

- `specs/registry/listing.schema.json` defines the listing row.
- `payout_target` typed-identifier rule documented + tested.
- "Ranking transparency" doc exists describing weights and a challenge path.
- Anti-Sybil schema (rate-limits, reviewer eligibility) lands as a `marketplace-policy.json` schema.
- Dispute SLA published in `docs/ops/MARKETPLACE-OPERATOR-RUNBOOK.md`.
- Revocation-never-deletes test exists.
- Chain-adapter symmetry property test (Base ↔ Solana) lands.
- Encrypted-envelope KATs land.
- Preview-integrity (re-hash on fetch) test with golden fixtures lands.

**Off-limits**: no contract deploys; no production listing intake; no payment processing.

**Recommended worker topology**: marketplace builder + protocol reviewer + dispute-policy reviewer.

---

### Phase H6 — apps foundation prep

**Mission**: make Phase 3 (web UI) unblocked.

**Acceptance criteria**:

- `apps/` gets directory placeholders: `apps/marketplace-ui/`, `apps/marketplace-api/`, `apps/api/`, each with a stub `README.md` linking to the spec it consumes.
- Listing fixture set lands under `examples/listings/`.
- Wallet-adapter mock contract lands under `specs/protocol/wallet-adapter-mock.md`.
- MCP `horcrx-marketplace` JSON-RPC schema lands under `specs/marketplace/mcp.schema.json`.
- The `examples/horcrx-002-orbel-pack/` per-member manifests are materialized (or the docs explicitly mark them as deferred).

**Off-limits**: no real frontend implementation (that is Phase 3 of `next-missions.md`); no live wallet integration.

**Recommended worker topology**: foundation builder + frontend reviewer.

---

### Phase H7 — wiki + canon harden (HORCRX-internal)

**Mission**: apply B.2/B.3 to HORCRX's own `docs/`.

**Acceptance criteria**:

- `docs/CANONICAL.md` allowlist exists.
- Every `docs/**.md` has minimum frontmatter (`title`, `version`, `updated`).
- `ci.yml` gains a `ci/docs-frontmatter` job.
- `markdown-link-check` tightened to flag unannotated `~/wiki/...` references.
- Cross-link policy stated in `docs/CANONICAL.md`: HORCRX may **read** `~/wiki/`, never **write** outside the wiki-librarian mission.

**Off-limits**: no writes to `~/wiki/` from this mission; no edits to `~/wiki/_meta/canonical-pages.txt`; no edits to `~/wiki/agents.md`, `~/wiki/claude.md`, `~/wiki/hermes.md`.

**Recommended worker topology**: docs worker + librarian reviewer.

---

### Phase H8 — supply chain + release discipline

**Mission**: tighten the dependency + release surface ahead of any first published package.

**Acceptance criteria**:

- SBOM generation wired into `release.yml` (CycloneDX or SPDX, pin SHA).
- Action SHAs pinned in both `ci.yml` and `release.yml` (no floating `vN` tags).
- `release.yml` publishes only after a manual operator approval step (GitHub environment with required reviewers).
- `CHANGELOG.md` regression test in CI: tag → matching changelog section must exist (today the release workflow already errors if missing, but lacks a pre-tag CI check).
- Vessel-signing-key fingerprint section in `SECURITY.md` is populated when a real key exists (operator-gated).

**Off-limits**: no production key generation in this phase; no published packages on npm; no contracts deployed.

**Recommended worker topology**: release/build worker + security worker + operator HITL on environment approvals.

---

## Section H — Open questions for operator

1. **Wiki bridge direction**: do we want a one-way HORCRX → `~/wiki` promotion via the wiki-librarian mission, or also a `~/wiki` → HORCRX/docs/ snapshot? My recommendation is one-way only, but the existing `~/wiki/_HORCRX/` directory suggests an experimental bidirectional pattern may already be in motion.

2. **Branch protection apply**: `/Users/rudlord/HORCRX/WORKER-COMPLETE.md` line 56 explicitly defers the `gh api` apply. Phase H1 requires going live with it — do you want that in this hardening mission or kept deferred?

3. **Untracked `specs/hermes-webapi-backup/`**: delete, move, or keep? It looks like an accidental drop given AGENTS.md's foundation-only contract. The `app.py` line 30 reads `HERMES_CORS_ORIGINS` from env which is fine, but the directory being inside `specs/` is misleading.

4. **Real security contact**: `SECURITY.md` line 9 placeholder. Do we publish a real email or a Signal/Keybase intake before Phase H1 closes, or hold until first real key/listing exists?

5. **Single-CODEOWNER**: `/Users/rudlord/HORCRX/.github/CODEOWNERS` is `* @chipoto69`. At what scale do we split per-area teams? Hardening mission can pre-stage the structure but cannot create teams.

6. **ADR-11 (iteration budget)**: the upstream Hermes runtime divergence is still flagged for Phase 1 verification. Should Phase H4 (memory + traces) also verify ADR-11 from the HORCRX side, or remain Phase-1-scoped?

7. **Per-slot signing keys**: `SPEC.md` §5.2 + `signing-and-lineage.md` allow per-slot signers, but reference vessels use one author key (`examples/horcrx-001-candysoul/manifest.json` line 174 single Ed25519 key). Do we mandate at least one per-slot signature example before Phase H5 closes?

8. **Voice doctrine scope**: should `voice-lint` (CI) lint **every** markdown file matching `*soul*.md` or `voice.md`, or only the canonical roots? My recommendation in Phase H1 is "all matching files in `examples/` plus root + design-system" — confirm scope.

9. **Validation script language**: Python (consistent with `ci.yml` line 56 markdown-link-check), Node (consistent with `ajv` in `ci.yml` line 42 schema-validate), or both? Operator preference matters because GATE-HX-04..06 will compound.

10. **Marketplace pre-launch lockdown ordering**: Phase H5 closes the listing-blockers, but the *operator* still needs to approve the first listing. Should H5 also produce a "listing-go" checklist that the operator signs off on, or is that out of scope?

11. **Hermes-binding revisit cadence**: the 14 hard constraints in `BINDING.md` §8 are locked. Do we ever expect Hermes upstream to change those, and if so, what's the trigger for re-running the §9 cross-check?

12. **Encryption suite finality**: `traces-format.md` lists `age | x25519-xsalsa20-poly1305`. Is one the canonical default, or are both acceptable and chosen per-vessel? Phase H4 needs the answer to produce KATs.

---

## Source paths cited in this recon

Foundation docs (HORCRX repo):
- `/Users/rudlord/HORCRX/README.md`
- `/Users/rudlord/HORCRX/AGENTS.md`
- `/Users/rudlord/HORCRX/SOUL.md`
- `/Users/rudlord/HORCRX/SECURITY.md`
- `/Users/rudlord/HORCRX/CONTRIBUTING.md`
- `/Users/rudlord/HORCRX/CHANGELOG.md`
- `/Users/rudlord/HORCRX/WORKER-COMPLETE.md`
- `/Users/rudlord/HORCRX/package.json`

CI + repo policy:
- `/Users/rudlord/HORCRX/.github/workflows/ci.yml`
- `/Users/rudlord/HORCRX/.github/workflows/release.yml`
- `/Users/rudlord/HORCRX/.github/branch-protection.md`
- `/Users/rudlord/HORCRX/.github/CODEOWNERS`
- `/Users/rudlord/HORCRX/.github/dependabot.yml`
- `/Users/rudlord/HORCRX/.github/PULL_REQUEST_TEMPLATE.md`
- `/Users/rudlord/HORCRX/.githooks/commit-msg`
- `/Users/rudlord/HORCRX/.githooks/pre-push`
- `/Users/rudlord/HORCRX/.gitignore`
- `/Users/rudlord/HORCRX/.gitattributes`

Infrastructure docs:
- `/Users/rudlord/HORCRX/docs/infrastructure/security.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/services.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/observability.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/hosting.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/local-dev.md`

Roadmap:
- `/Users/rudlord/HORCRX/docs/roadmap/ROADMAP.md`
- `/Users/rudlord/HORCRX/docs/roadmap/next-missions.md`
- `/Users/rudlord/HORCRX/docs/roadmap/migration-from-knowledge-horcrux.md`

Specs:
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/manifest.schema.json`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/signing-and-lineage.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/compatibility-matrix.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/soul-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/dreams-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/intuition-md.schema.md`
- `/Users/rudlord/HORCRX/specs/protocol/PROTOCOL.md`
- `/Users/rudlord/HORCRX/specs/protocol/chain-adapters.md`
- `/Users/rudlord/HORCRX/specs/protocol/identity-and-keys.md`
- `/Users/rudlord/HORCRX/specs/protocol/interop.md`
- `/Users/rudlord/HORCRX/specs/protocol/marketplace-flows.md`
- `/Users/rudlord/HORCRX/specs/protocol/payment-layer.md`
- `/Users/rudlord/HORCRX/specs/protocol/registry-design.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/open-questions-resolved.md`
- `/Users/rudlord/HORCRX/specs/marketplace/ARCHITECTURE.md`
- `/Users/rudlord/HORCRX/specs/marketplace/ip-preservation.md`
- `/Users/rudlord/HORCRX/specs/marketplace/royalties.md`
- `/Users/rudlord/HORCRX/specs/marketplace/discovery-and-trust.md`
- `/Users/rudlord/HORCRX/specs/marketplace/agent-economy-fit.md`
- `/Users/rudlord/HORCRX/specs/hermes-webapi-backup/app.py` (untracked, flagged)

Research:
- `/Users/rudlord/HORCRX/research/INDEX.md`
- `/Users/rudlord/HORCRX/research/04-economic-thesis.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`

Validation + examples:
- `/Users/rudlord/HORCRX/validation/F03-WORKER-COMPLETE.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/manifest.json`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/AGENTS.md`
- `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/manifest.json`

Apps + design-system:
- `/Users/rudlord/HORCRX/apps/brand/README.md`
- `/Users/rudlord/HORCRX/packages/design-system/README.md`
- `/Users/rudlord/HORCRX/packages/design-system/VOICE.md`

Wiki (read-only):
- `/Users/rudlord/wiki/AGENTS.md`
- `/Users/rudlord/wiki/CLAUDE.md` (file is `claude.md` lowercase in repo)
- `/Users/rudlord/wiki/hermes.md`
- `/Users/rudlord/wiki/_meta/canonical-pages.txt`
- `/Users/rudlord/wiki/_meta/commit-standards.md`
