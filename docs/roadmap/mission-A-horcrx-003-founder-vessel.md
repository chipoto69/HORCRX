# Mission A — HORCRX #003 · founder (rags-to-riches vessel)

ATLAS → CORPUS → HORCRX.

Status: kickoff-ready (foundation-spec mission; no runtime code yet)
Recon: `/Users/rudlord/HORCRX/research/10-rags-to-riches-recon.md`, `/Users/rudlord/HORCRX/research/11-harness-landscape.md`
Parallel mission: `/Users/rudlord/HORCRX/docs/roadmap/mission-B-hardening-pass.md`

## 1. mission line

Author the third numbered HORCRX vessel — `horcrx-003-founder` — whose mission is a **zero-human company built from a $66.60 seed, earned by being smarter and earlier than the other agents in the market**. The vessel is a *maker*, not a trader. Its edge is product, speed, and signal — not arbitrage of price.

Earning posture (broad, productively):

- **Selling services** through agent-economy surfaces (agentic.market — https://agentic.market/?chart=transactions — ClawHub-style bounty boards, plus any equivalent that emerges).
- **Picking up code bounties**, scraping/data jobs, and other "agents need tokens spent, here's the labor" markets.
- **Shipping its own micro-products** when the bet is small enough to fit the seed and the runtime allows.
- **Researching and re-selling** synthesized signal where rights permit — being *earlier* is the moat.
- Explicitly NOT financial-market trading. The vessel earns by producing value, not by predicting price.

Money custody, harness activation, and the wallet itself are NOT in this mission's scope (they live in a later HORCRX implementation phase). This mission produces the *seed of the soul* — identity, contracts, slots, gates — not the running agent.

Three-verb candidate (operator must approve final): **earn through making · move through earliness · compound through audit**. Final line lands in `vessel/voice.md` and `vessel/mission.md`. (Operator can override; the candidate is written to express maker-not-trader posture and the "smarter and earlier than others" edge.)

## 2. why now

- Foundation v0.1.1 is shipped; reference vessels #001 (single) and #002 (pack) are live.
- The recon dossiers prove the harness, money rails, audit posture, persistence, and voice doctrine all exist as prior art and need only to be composed into a third reference vessel.
- A money-aware vessel is the cleanest forcing function for: `voice.md` promotion, `mission.md` / `ledger.md` / `autonomy.md` slot definition, and the GATE chain referenced by the parallel hardening mission.

## 3. scope (in)

### 3.1 New spec extensions (additions to `specs/vessel-format/`)

- `specs/vessel-format/SPEC.md` — promote `voice.md` to a required slot; reserve four optional slots: `mission.md`, `ledger.md`, `autonomy.md`, `constraints.md`. (Section A row "voice.md" in recon 10.)
- `specs/vessel-format/voice-md.schema.md` — schema for the slot.
- `specs/vessel-format/mission-md.schema.md` — schema (north-star line, success ladder, abort criteria, termination state).
- `specs/vessel-format/ledger-md.schema.md` — declarative pointer to NDJSON ledger + the four hard knobs (per-tx, daily, weekly, cooldown, allowlist, HITL threshold).
- `specs/vessel-format/autonomy-md.schema.md` — HITL ladder + kill-switch contract + ASI rung classification.
- Update `specs/vessel-format/SPEC.md` §3 + `manifest.schema.json` to reflect the new slots.

### 3.2 New vessel reference (the body of this mission)

`examples/horcrx-003-founder/` populated with:

```
horcrx-003-founder/
├── soul.md              # identity-only (SOUL schema §3.1)
├── agents.md            # operational contract (treasury + dispatch-audit guardrails)
├── principles.md        # extended candysoul base + maker-not-trader doctrine
├── intuition.md         # heuristics for "smarter and earlier than others": signal scoring, time-to-ship, scope discipline, bounty triage, agentic-marketplace selection
├── dreams.md            # wake-cycle slot (first cycle authored in this mission)
├── voice.md             # three-verb mission line, inherits VOICE.md format
├── mission.md           # NEW slot — rags-to-riches arc, abort, termination
├── ledger.md            # NEW slot — treasury posture (declarative only)
├── autonomy.md          # NEW slot — HITL ladder + kill switch
├── constraints.md       # optional — non-negotiable invariants
├── manifest.json        # validates against extended manifest.schema.json
├── mark.svg
├── skills/              # mandatory skills the vessel loads on boot (paperclip-vision, content-os, autoresearch, claudeception, append-only-state, iso-week, dispatching-parallel-agents — all SKILL.md packets)
├── plugins/             # mcp_servers manifests (sanity, supabase, hugging-face, context7, x402-facilitator) — no secrets, no payload
├── workflows/           # declarative wake/walk/dispatch loops
├── crons/jobs.json      # tick schedule, disabled on import per BINDING.md §4.2
├── traces/              # placeholder dir (no real traces yet — runtime is out of scope)
├── memory/
│   ├── canon.md         # portable seed memory
│   └── grafts/          # empty dir
├── mission/             # NEW vessel folder — VISION.md, CEO_BOOTSTRAP.md, kanban export
├── ledger/              # NEW vessel folder — caps.json + empty NDJSON skeleton
├── briefs/              # NEW vessel folder — daily/weekly/retro skeleton dirs
├── notify/policy.json   # quiet hours, channel routing (no tokens)
├── wallets/addresses.json  # PUBLIC addresses only — declared but unbound
├── observability/       # metric names, alert routing (declarative)
└── governance/          # pending-approvals NDJSON skeleton + policies.md
```

(Folder additions taken from recon 11 §H. All append-mostly, strip-safe, no secrets.)

### 3.3 Hermes-binding addendum (no live profile writes)

`specs/hermes-binding/BINDING.md` gains a new section "Founder-vessel binding" describing how `horcrx-003-founder` would install as a `~/.hermes/profiles/horcrx-founder/` profile *when* a later implementation phase authorizes it. This is **spec only**.

The binding section must enumerate the **earning surfaces** the vessel is allowed to operate on (declarative — no live integrations in this mission):

- agentic.market (https://agentic.market/?chart=transactions) — service listing + transaction surface.
- ClawHub-class bounty boards (and any equivalent that surfaces by mission close — operator-curated allowlist in `vessel/plugins/marketplaces.json`).
- Generic code-bounty surfaces (Gitcoin-style, Replit bounties, etc., where rights permit).
- Self-hosted micro-product publishing (a Sanity site, a Supabase-backed API, a hugging-face Space) — the vessel ships and sells its own thing.
- Data/scrape services (the "agents pay other agents to scrape half the internet" lane).

Each surface in `marketplaces.json` declares: name, surface URL, account model (per-agent vs operator-shared), settlement currency, fee posture, evidence schema for completed jobs, anti-Sybil status. No tokens, no API keys — just the declarative shape so a later phase can wire it.

### 3.4 Open-question resolutions

Resolve the highest-stakes recon 10 §G questions plus the new earning-posture questions in `specs/hermes-binding/open-questions-resolved.md`:

- **OQ-12**: vessel-as-proposer vs vessel-as-signer (recommend proposer; host custody).
- **OQ-13**: scale of caps at $66.60 seed (recommend treasury-relative caps: per-tx ≤ 1% spend, daily ≤ 5% spend, weekly ≤ 15% spend — applied to **outflows**, not earned-then-respent revenue, which has its own row).
- **OQ-14**: kill-switch contract shape (`state/halt.lock` + NDJSON marker + operator dead-man timer).
- **OQ-15**: termination state criteria (treasury threshold AND/OR mission-line satisfaction AND/OR inactivity timeout — operator picks the conjunction in HITL).
- **OQ-16** (new — maker doctrine): explicit "no financial-market trading" off-limit. The vessel may NOT take directional positions on price as a primary earning strategy. Selling a *signal product* is allowed; using that signal to trade for its own book is forbidden. Anti-paperclip + anti-rug.
- **OQ-17** (new — earliness budget): how much of treasury the vessel may spend on *being earlier* (scraping, paid API calls, data buys, model upgrades) vs. how much on *making* (compute to actually ship). Recommend: ≤ 30% of weekly spend on earliness, ≥ 50% on making, ≤ 20% on overhead (LLM tokens, infra). Operator confirms ratios in `ledger.md`.
- **OQ-18** (new — agentic-marketplace allowlist): which surfaces are permitted in v0. Default allowlist: `agentic.market`, plus operator-named bounty boards. New surfaces require HITL.
- **OQ-19** (new — revenue-respend posture): revenue may be respent without re-triggering HITL up to the OQ-13 cap; above the cap, revenue-funded spend still requires HITL (so a single big payday doesn't auto-unlock big-bet spend).

## 4. scope (out)

- No runtime code. No `apps/` additions beyond the design-system wrapper. No FastAPI/Hermes profile spinup. The vessel is a **bundle on disk**, not a running agent.
- No wallet creation. No keypair generation. The vessel's `wallets/addresses.json` is empty until a later phase.
- No money on chain. No x402 facilitator. No live payment.
- No live Hermes profile writes anywhere on the host.
- No edits to inherited brand canon (`packages/design-system/`) or `VOICE.md`.
- No wiki writes outside the wiki-librarian gate (recon 12 §B.1 — one-way bridge).
- No remote push without operator approval; tags, releases, contracts not in scope.

## 5. acceptance criteria

A1. `examples/horcrx-003-founder/manifest.json` validates against the **extended** `specs/vessel-format/manifest.schema.json`.
A2. Every required slot from §3.2 exists, is non-empty, and is valid against its schema.
A3. The vessel's `voice.md` carries a unique three-verb mission line; `packages/design-system/VOICE.md` rules pass `voice-lint`.
A4. `mission.md` defines: seed amount ($66.60), earning posture (maker, not trader; "smarter and earlier than others"), success ladder (≥3 rungs — e.g. first dollar earned, first $10 earned, first $100 earned), abort criteria (≥3 named, including "drift into directional trading"), termination state (single sentence).
A5. `ledger.md` carries: the spend knobs (per-tx, daily, weekly, cooldown, HITL threshold, recipient allowlist), the **earn knobs** (allowed marketplaces, minimum job size, evidence requirements, payout addresses by chain), the OQ-17 spend-mix ratios (earliness / making / overhead), and treasury custody posture ("vessel proposes, host signs").
A6. `autonomy.md` enumerates: what the vessel may decide alone, what requires HITL, what is forbidden (including OQ-16 no-trading); kill-switch contract; ASI rung per `/Users/rudlord/KILLERSQUAD/knowledge_base/research/machine-human-companies.md` autonomy ladder.
A7. All resolved open questions (OQ-12..OQ-19) land in `specs/hermes-binding/open-questions-resolved.md` with `accepted` status (no `accepted-pending-HITL`).
A8. `specs/hermes-binding/BINDING.md` gains the founder-vessel binding section; §9 cross-check table extended with rows covering the new slots.
A9. `validation/F-A-founder-vessel-WORKER-COMPLETE.md` reports: every change made, every schema test run, every gap left for a later phase.
A10. `docs/roadmap/ROADMAP.md` Phase 0 marked complete; new line entry for "Mission A · horcrx-003-founder · spec-complete" pointing to this packet.

## 6. off-limits (mission-specific, in addition to repo AGENTS.md off-limits)

- Do NOT generate any wallet keys, real or test. Public addresses in `wallets/addresses.json` MUST be declared empty (the slot exists; the binding does not).
- Do NOT write to `~/.hermes/`, `~/wiki/`, `~/.claude-worktrees/ATLAS/`, `~/.factory/skills/`, or any of the operator's running runtime locations.
- Do NOT install or activate the founder profile in Hermes; this mission ends at "spec on disk."
- Do NOT modify the existing reference vessels (`examples/horcrx-001-candysoul/`, `examples/horcrx-002-orbel-pack/`) except to mirror the new required slot changes consistently (the `voice.md` promotion forces a `voice.md` check across all three references).
- Do NOT add LLM keys, wallet seeds, or any service token anywhere in the repo or in CI.
- Do NOT delete or modify `specs/hermes-webapi-backup/`; that disposition belongs to Mission B.
- Do NOT push to remote without explicit operator approval.
- Voice doctrine: identity-only files (`soul.md`, `voice.md`) MUST contain no shell commands, no `/Users/...` paths, no `git`/`npm`/etc. AGENTS.md and operational files carry those.

## 7. recommended worker topology

| Role | Responsibility | Output |
|---|---|---|
| **vessel-author** | Compose `examples/horcrx-003-founder/` and the new SPEC schema files. Inherit candysoul shape; extend with money-aware slots. | the vessel folder + schema files |
| **doctrine-reviewer** | Audit identity/voice files against `SOUL.md`, `VOICE.md`, and recon 10 §F voice-canon authority hierarchy. Catch corporate drift. | review comments on each `.md` |
| **hermes-binding-extender** | Author the founder-vessel BINDING.md section and the §9 cross-check rows. Resolve OQ-12..OQ-15. | BINDING.md diff + open-questions-resolved.md diff |
| **validator** | Extend `manifest.schema.json`, run `schema-validate` against #001, #002, #003. Confirm `voice-lint` extended scope passes. | green CI on PR |
| **operator (HITL)** | Approve final three-verb mission line; approve OQ resolutions (especially OQ-13 cap scale and OQ-15 termination state). | inline approval comments on PR |

Suggested execution shape: vessel-author and hermes-binding-extender work in parallel after the first ~30 min of joint scope-lock; doctrine-reviewer reviews continuously; validator gates the PR; operator HITL gates the merge.

Use `dispatching-parallel-agents` SKILL pattern (`/Users/rudlord/.agents/skills/dispatching-parallel-agents/SKILL.md`).

## 8. dependencies and blockers

- Mission B (hardening) is **parallel, not blocking**. The two missions share zero file collisions: A writes `examples/horcrx-003-founder/` + new schema files + targeted SPEC.md/BINDING.md/open-questions-resolved.md edits; B writes `docs/`, `validation/`, `.github/`, `.githooks/`, and most of `specs/marketplace/`. Light coordination on `manifest.schema.json` (A extends; B does not touch).
- `paperclip-vision` SKILL (recon 11 §C.2) is referenced for `VISION.md` + `CEO_BOOTSTRAP.md`. If not installed locally, vessel-author falls back to hand-authoring those files from `mission.md` + `autonomy.md`.
- Operator HITL needed for OQ-13 (cap scale) and OQ-15 (termination) before mission can ship.

## 9. forensic / "design before hope" notes

- The largest unresolved tension flagged in recon 10 §G.1 (foundation-only vs runtime-needed) is **deliberately deferred** by this mission. The vessel is fully expressible as a spec + folder bundle without any runtime activation. The runtime activation is a future implementation phase (post-Phase-1 in `next-missions.md`).
- The recon-flagged paperclip risk (`/Users/rudlord/wiki/raw/reader/THE 2028 GLOBAL INTELLIGENCE CRISIS ...`) is closed by mandating `autonomy.md::termination_state` and the kill-switch contract. The vessel cannot ship without an answer to "when does it stop."
- Voice canon authority: `packages/design-system/VOICE.md` > `SOUL.md` > vessel `voice.md`. Each vessel composes within the format; the format is non-negotiable.
- **Maker-not-trader doctrine** (OQ-16). The edge is "smarter + earlier than other agents," expressed through product, signal, and labor — not through directional bets on price. This closes a second paperclip vector: a trading agent with autonomous funds + iteration budget is a near-classical optimizer-going-wrong scenario. A maker agent's worst loss-of-control case is "shipped too much mediocre work" — recoverable. A trader agent's is "drained the seed on a bad position" — unrecoverable. We pick the recoverable failure mode by design.
- **Earliness is a budget line, not a vibe** (OQ-17). Being earlier requires real spend — paid data, scraping, paid model calls, monitoring. By forcing earliness into the ledger as a named ratio, we make it auditable. Without this knob, the vessel either underspends on signal (and loses the edge) or overspends (and burns the seed before shipping). Operator HITL on the ratio at mission close.

## 10. success-shaped close

Mission ends when:

- `examples/horcrx-003-founder/` is on disk and validates.
- `specs/vessel-format/SPEC.md` lists the new required + reserved slots.
- BINDING.md §9 has been re-cross-checked.
- `validation/F-A-founder-vessel-WORKER-COMPLETE.md` is written.
- A PR is opened (not merged) with all of the above; operator merges after reviewing.

This is the seed of the soul. Runtime activation belongs to a later phase that AGENTS.md must explicitly authorize.
