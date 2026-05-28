# 11 — Harness + Agentic-Framework Landscape

ATLAS → CORPUS → HORCRX.

**Scope:** map the integration surface a new HORCRX vessel (autonomous, money-aware founder agent) could ride on. The vessel must run continuously, pay its own bills, plan, execute, schedule, observe itself, and report.

**Posture:** read-only inventory. Every claim cites an absolute path. Local-in-repo, external-prior-art, and aspirational-only are distinguished explicitly.

## Provenance legend

- **[REPO]** — file or module already lives in `/Users/rudlord/HORCRX/`
- **[LOCAL]** — file lives on this machine but outside the HORCRX repo (Hermes profile, skill, droid, ATLAS worktree)
- **[ASPIRATIONAL]** — documented in HORCRX but no implementation exists yet
- **[EXTERNAL]** — third-party tool/spec referenced from documentation

---

## Section A — Harness candidates

The vessel needs a host loop. Four real options exist on this machine.

| Harness | Maturity | State location | Audit | Money awareness | Scheduling | Subagents | Fit for money-aware founder agent |
|---|---|---|---|---|---|---|---|
| **Hermes Agent** (NousResearch) [LOCAL] | Production. Single `AIAgent` loop at `/Users/rudlord/.hermes/hermes-agent/run_agent.py`, ~28 profiles live under `/Users/rudlord/.hermes/profiles/`. | Per-profile dir under `~/.hermes/profiles/<name>/` with `SOUL.md`, `AGENTS.md`, `config.yaml`, `memories/`, `skills/`, `sessions/`, `state.db`, `cron/jobs.json`, `state/audit.sqlite`, `logs/hermes-audit.ndjson` (see `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §2). | `dispatch()` mandates NDJSON+SQLite row per LLM call; direct `litellm`/`anthropic` imports forbidden (BINDING.md §8). | None native. Would need a payment skill + MCP server bolted on via x402 (`/Users/rudlord/HORCRX/specs/protocol/payment-layer.md`). | First-class. `<profile>/cron/jobs.json` already runs jobs every 4h in `hermes-content-os` (`/Users/rudlord/.hermes/profiles/hermes-content-os/cron/jobs.json`). | Yes; iteration-budget shared across subagents (`/Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py`). | **Strongest.** Continuous runtime, persistent memory, mandatory audit, mature cron substrate, MCP servers, dispatch budget. Operator already trusts it. |
| **Factory droids** [LOCAL] | Production for IDE/worker tasks. `~/.factory/droids/worker.md` is current; project droid dir `/Users/rudlord/HORCRX/.factory/` does not exist (verified). | Per-droid `.md` with YAML frontmatter at `/Users/rudlord/.factory/droids/` (worker, coder, factory-codex, deepseek-researcher, kimi-research, scrutiny-feature-reviewer, user-testing-flow-validator, preflight-checker, memory-bank-indexer). | None at droid level; relies on host session log. | None. | None native; needs an outer scheduler (launchd, GH Actions). | First-class via `Task`/Worker delegation. `dispatching-parallel-agents` skill at `/Users/rudlord/.agents/skills/dispatching-parallel-agents/SKILL.md` codifies the pattern. | Good for **bursts of bounded work** (research, code edits, reviews). Not a 24/7 vessel: each droid invocation is a session, not a loop. |
| **Plain Python loop / Ralph-style** [LOCAL] | Pattern only. `loop-maestro` skill at `/Users/rudlord/.claude/skills/loop-maestro/SKILL.md` defines Ralph tenets (fresh context, disk state, signals over scripts, "let Ralph Ralph"). | Disk + git, no enforced shape. | Whatever the loop authors write. | Hand-rolled. | launchd/cron supervisor or `while true` daemon. | Hat-based hand-off (architect/implementer/tester/etc.) via Ralph hats. | Useful **inside** a Hermes profile or droid invocation; weaker as a standalone harness because it lacks the audit, memory, and approval surfaces Hermes already gives for free. |
| **GitHub Actions** [EXTERNAL, used locally] | Mature for CI; the `append-only-state-via-github-api` skill at `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md` shows how to run a 10-minute auto-merge loop and stream NDJSON state to a branch. | Repo files on a per-actor branch (`audit/<actor>`) + auto-merged main. | Whatever workflow logs. | None native; would need self-funded compute credits. | Cron in YAML; up to every 5 min (often 10–15 in practice). | Matrix jobs only; no agent-to-agent messaging. | Best as the **off-host backup loop and audit-mirror**, not as the primary harness. Public, free-ish, durable. Bad fit for any flow that needs an open wallet (key custody on GH is dangerous). |

### Verdict

The founder vessel should ride **Hermes as primary harness**, dispatch **Factory droids as worker burst-capacity**, optionally embed **Ralph loops inside a Hermes session** for self-improving sub-phases, and mirror **append-only state to a GitHub Actions backup** for off-host durability. This matches the constraints in `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §1–§8 and the audit posture in `/Users/rudlord/HORCRX/docs/infrastructure/observability.md`.

---

## Section B — Recommended integration topology

```text
                                  +-------------------------------------------+
                                  |              OPERATOR / HUMAN             |
                                  |  approvals, key custody, spend caps,      |
                                  |  GATE-01..08 wiki writes                  |
                                  +---------------------+---------------------+
                                                        |
                                                        | HITL: approve_purchase,
                                                        |       approve_signing,
                                                        |       approve_canon_write
                                                        v
+--------------------------------+        +---------------------------------------+
|     SCHEDULER LAYER            |        |       HERMES PROFILE (PRIMARY)        |
| - launchd plists (macOS host)  |  tick  |  ~/.hermes/profiles/horcrx-founder/   |
| - <profile>/cron/jobs.json     +------->|                                       |
| - GH Actions (off-host backup) |        |  SOUL.md       (identity, voice)      |
+--------------------------------+        |  AGENTS.md     (operational contract) |
                                          |  config.yaml   (model + MCP wiring)   |
                                          |                                       |
                                          |   +-------------------------------+   |
                                          |   |   AIAgent loop (run_agent.py) |   |
                                          |   |   iteration_budget enforced   |   |
                                          |   +-----+-------------------+-----+   |
                                          |         |                   |         |
                                 dispatch()|         | tool call         | subagent|
                                 audit     v         v                   v         |
                                 +---------+----+ +--+---------+ +-------+------+  |
                                 | NDJSON+SQL   | | MCP fan-out| | Factory     |  |
                                 | audit sinks  | | sanity     | | droid Task  |  |
                                 | logs/...     | | supabase   | | worker.md   |  |
                                 | state/...    | | hf, ctx7   | | + parallel  |  |
                                 +--------------+ | x402 facil.| +-------------+  |
                                                  | postiz     |                  |
                                                  +-----+------+                  |
                                                        |                          |
                                                        v                          |
+----------------------------+        +--------------------------+        +-------+------+
| WALLET / VAULT (isolated)  |<------>| x402 facilitator         |        | LEDGER / FS  |
| - shell-env LLM keys       | verify | (Faremeter-style)        |        | ledger/      |
| - signer key (Base/Sol)    | proof  | nonce + expiry + chain   |        | briefs/      |
| - rotates via approval     |        +-----+--------------+-----+        | mission/     |
+----------------------------+              |              |              | traces/      |
                                             v              v              | memory/canon |
                                +-------------+   +---------+--------+     +------+-------+
                                | Base RPC    |   | Solana RPC       |            |
                                | Alchemy/QN  |   | Helius           |            v
                                +-------------+   +------------------+   +--------+--------+
                                                                          | GH Actions      |
                                                                          | off-host mirror |
                                                                          | audit/<actor>   |
                                                                          | branch          |
                                                                          +-----------------+
```

### Walkthrough

1. **Tick.** Scheduler fires (launchd plist or `cron/jobs.json` row). Hermes wakes the `horcrx-founder` profile and runs the `AIAgent` loop with a bounded iteration budget (`/Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py`).
2. **Plan.** SOUL+AGENTS+skills produce a plan; loop policy is the optional Ralph harness embedded as a skill (see `/Users/rudlord/.claude/skills/loop-maestro/SKILL.md`).
3. **Dispatch.** Every LLM call goes through `dispatch()`, which writes one row to `logs/hermes-audit.ndjson` and `state/audit.sqlite` (BINDING.md §8). Direct provider imports are forbidden.
4. **Tools.** Tool calls fan out to MCP servers (sanity, supabase, hugging-face, context7, postiz, x402 facilitator) configured under `<profile>/config.yaml` with `mcp_servers:` (see `/Users/rudlord/.claude/skills/hermes-agent-mcp-server-registration/SKILL.md`).
5. **Subagents.** For bounded burst-work (research, edits, reviews) the vessel dispatches a Factory droid worker (`/Users/rudlord/.factory/droids/worker.md`) following the `dispatching-parallel-agents` pattern. Shared iteration budget applies (BINDING.md §8 hard constraint).
6. **Money.** When a paid action is required, the loop calls the x402 facilitator MCP. The facilitator verifies nonce+expiry against the chosen chain adapter (`/Users/rudlord/HORCRX/specs/protocol/chain-adapters.md`) using Base (Alchemy/QuickNode) or Solana (Helius) RPCs. **Signing keys live in a separate vault host**, never inside the vessel bundle, per `/Users/rudlord/HORCRX/docs/infrastructure/security.md` §1.
7. **HITL.** Irreversible flows (purchase ≥ cap, signing, canon writes) raise an approval card via the existing operator surface (Telegram + Kanban in `hermes-content-os`).
8. **State.** Outputs land in vessel folders (`ledger/`, `briefs/`, `mission/`, `memory/canon.md`, `traces/*.ndjson`). Append-only state is mirrored to a GitHub branch via `append-only-state-via-github-api` for off-host durability.
9. **Report.** A cron job emits a Telegram rundown (pattern already live in `/Users/rudlord/.hermes/profiles/hermes-content-os/cron/jobs.json` job `6d46873090da`).

---

## Section C — MCP + Skill inventory mapped to founder-agent capabilities

### C.1 MCP servers available in this environment

| MCP server | Where surfaced | Founder-agent capability |
|---|---|---|
| **sanity** | Loaded via ToolSearch (deferred tool list in environment header) | Headless CMS for "ship and sell" surface: deploy_studio, create_documents_from_markdown, publish_documents, semantic_search. Lets the agent maintain a customer-facing site. |
| **supabase** | Skill `/Users/rudlord/.agents/skills/supabase/SKILL.md` | Postgres + auth + edge functions. Backing store for leads, transactions, idempotent upserts (pattern in `/Users/rudlord/.claude/skills/postgres-idempotent-import-backfill/SKILL.md`). |
| **hugging-face** | Referenced in task brief as available [EXTERNAL, expected via MCP] | Model search, dataset retrieval, inference endpoints for cheap utility work. |
| **context7** | Referenced in task brief [EXTERNAL, expected via MCP] | Up-to-date library docs on demand. Reduces hallucinated APIs for code that ships. |
| **playwright** | Loaded in environment (deferred tools `playwright___*`) | Headless browser automation: forms, scraping, e2e checks. Pair with `agent-browser` skill. |

> Sanity, hugging-face, context7 are documented as available via ToolSearch in the environment header; the vessel config must declare them in `<profile>/config.yaml:mcp_servers` for Hermes to expose them (registration pattern: `/Users/rudlord/.claude/skills/hermes-agent-mcp-server-registration/SKILL.md`).

### C.2 Skills directly relevant to a self-running founder agent

| Skill | Absolute path | Founder-agent use |
|---|---|---|
| **content-os** | `/Users/rudlord/.factory/skills/content-os/SKILL.md` | Reference implementation of a real, running vault-native operator loop with inbox.sqlite, 13 verbs, GATE-01..08, daily Telegram digests, autoresearch. **Closest local prior art to what the founder vessel should feel like.** |
| **autoresearch** | Skill listed in environment header [LOCAL, install not verified on disk] | Autonomous experiment loop with MAD-based confidence scoring + git-branch isolation. Direct pattern for "try → measure → keep or revert". |
| **ralph-loop / loop-maestro** | `/Users/rudlord/.claude/skills/loop-maestro/SKILL.md` | Multi-phase orchestration with hats (architect, implementer, tester, debugger, optimizer). Embedded as inner loop, not outer harness. |
| **claudeception** | `/Users/rudlord/.claude/skills/claudeception/SKILL.md` | Continuous learning: extracts reusable knowledge from sessions into new skills. Founder vessel uses this to *grow* its own skill library. |
| **append-only-state-via-github-api** | `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md` | Pattern for high-frequency NDJSON state writes to a shared repo branch with auto-merge workflow. Directly enables the ledger/audit mirror. |
| **gsd-* family** (~80 skills) | `/Users/rudlord/.agents/skills/gsd-*` | Phase-based project management substrate: `gsd-new-milestone`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-audit-fix`, `gsd-ship`, `gsd-autonomous`. The vessel can drive itself through `gsd-autonomous` once a milestone is set. |
| **solo-duo-operator-mode** | `/Users/rudlord/.factory/skills/solo-duo-operator-mode/SKILL.md` | Pattern for N-operator topologies where seats may be empty (live\|pending-onboard). Useful when "the founder agent" is one of two seats, the other being the human. |
| **dispatching-parallel-agents** | `/Users/rudlord/.agents/skills/dispatching-parallel-agents/SKILL.md` | Codifies parallel subagent dispatch with isolated context. Used by the vessel to fan out research/code-edit work to droids. |
| **capture / verify / droid-cli** | Background skills in environment header (not standalone files in `~/.claude/skills/`). [ASPIRATIONAL on disk; behavioral knowledge inside `droid-control`] | Recording lifecycle + deliverable verification. Important once the vessel records its own demos or QA evidence for sale. |
| **paperclip-vision** | `/Users/rudlord/ORGANIZED/agents/factory-swarm/vendor/paperclip/skills/paperclip-vision` (symlinked into `~/.claude/skills/`) | Founder-interview skill that produces `VISION.md` + `CEO_BOOTSTRAP.md`. Direct match: the founder vessel needs a VISION + bootstrap, and this skill builds them. |
| **agent-browser** | `/Users/rudlord/.claude/skills/agent-browser/SKILL.md` | Browser/Electron automation. For real revenue work: filling forms, posting on social, navigating Stripe/payment dashboards. |
| **browser-navigation** | Environment-header skill, `agent-browser`-based | Same family, narrower scope (test, screenshot, debug). |
| **cua-driver** | `/Applications/CuaDriver.app/Contents/Resources/Skills/cua-driver` | Native macOS AX-tree driving. Needed if the vessel must operate a native macOS app it cannot reach via browser. |
| **droid-control** | Environment-header skill | Outer-shell for terminal TUI + browser automation. Recording-grade evidence capture for "the agent did X". |
| **postiz** | `/Users/rudlord/.agents/skills/postiz/SKILL.md` | Scheduling to 28+ social channels. Founder needs distribution. |
| **render-workflows** | `/Users/rudlord/.claude/skills/render-workflows/SKILL.md` | Managed task runner for fan-out and long-running jobs (up to 24h). Alternative to launchd for off-host scheduled work. |
| **iso-week-in-cron-scripts** | `/Users/rudlord/.factory/skills/iso-week-in-cron-scripts/SKILL.md` | Fix for the silent-cron-failure trap. Mandatory reading for anything that picks files by week number. |

---

## Section D — Scheduler + persistence options ranked

| Rank | Option | Source | Best for | Caveats |
|---|---|---|---|---|
| 1 | **Hermes `<profile>/cron/jobs.json`** | `/Users/rudlord/.hermes/profiles/hermes-content-os/cron/jobs.json` (live, 19+ completed runs) | Primary loop; per-profile schedule with first-class agent reasoning, Telegram/Kanban delivery, audit. | Bound to a long-running Hermes gateway; if `state.db-wal` corrupts, jobs stall (observed Codex auth failures in current jobs). |
| 2 | **launchd plists (macOS)** | `~/Library/LaunchAgents/ai.hermes.content-os.daily.plist` referenced from `/Users/rudlord/.factory/skills/content-os/SKILL.md` | Outer supervisor that boots Hermes gateway and runs critical jobs even if Hermes itself is down. | macOS-only; not portable to a VPS. |
| 3 | **GitHub Actions cron + Contents-API push** | `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md` | Off-host backup loop, every 10 min auto-merge of per-actor branch into main. Free-tier durable. | Min granularity ~5 min; cannot hold secrets safely; not appropriate for signing keys. |
| 4 | **Render Workflows** | `/Users/rudlord/.claude/skills/render-workflows/SKILL.md` | Managed task fan-out, up to 24h jobs, paid plan. Good for heavy data-processing jobs the vessel commissions. | Beta SDK; managed cost; introduces a third-party trust domain. |
| 5 | **Plain `while true` loop + flock** | Pattern only (Ralph loop family) | Throwaway dev experiments. | No audit, no budget, no replay; do not run as production. |

Persistence layers used in combination:

- **Markdown canon:** `vessel/memory/canon.md` (portable, signed-on-export).
- **SQLite (host-local):** `<profile>/state.db` (sessions, FTS5), `<profile>/state/audit.sqlite`, optionally `<profile>/ledger.sqlite` for the founder vessel.
- **NDJSON (append-only):** `<profile>/logs/hermes-audit.ndjson` + `vessel/traces/*.ndjson` per `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md`.
- **Off-host mirror:** GitHub per-actor branch `audit/horcrx-founder` (pattern).
- **External provider (single active):** Honcho **or** GBrain, per BINDING.md §8 hard constraint "Tier 3 single-provider-active".

---

## Section E — Payment-rail integration plan

### E.1 What's specced [REPO]

- **x402-first posture** with HTTP-native challenge/response, nonce + expiry, chain-adapter verification, manifest-CID-bound evidence (`/Users/rudlord/HORCRX/specs/protocol/payment-layer.md`).
- **Chain adapters** for Base (ERC-721 + ERC-2981 baseline, ERC-6551 optional) and Solana (Metaplex Core baseline, cNFT optional) with symmetric `IChainAdapter` (`/Users/rudlord/HORCRX/specs/protocol/chain-adapters.md`).
- **Identity layers** split into author key, owner key, runtime delegated key, attester key (`/Users/rudlord/HORCRX/specs/protocol/identity-and-keys.md`).
- **Faremeter** evaluated as the most concrete TS x402 client; not required at protocol layer (`/Users/rudlord/HORCRX/specs/protocol/payment-layer.md` §4).
- **Audit integration**: every Hermes-mediated purchase must add `action`, `manifest_cid`, `listing_id`, `vessel_cid`, `royalty_target`, `run_id` to the audit row (`/Users/rudlord/HORCRX/docs/infrastructure/observability.md` §4.1).
- **Trust-domain split**: mind and secrets never live in the same artifact. Signing host is isolated from preview host (`/Users/rudlord/HORCRX/docs/infrastructure/security.md` §1, §3).

### E.2 What exists as prior art [LOCAL]

- x402 gateway, nonce manager, pricing, verifier registry at `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/` (working prototype, per `/Users/rudlord/HORCRX/research/06-local-modules-inventory.md`).
- Solana verifier working; Base verifier scaffolded (`/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/solana_verifier.py`, `base_verifier.py`).
- Agent wallet stack at `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/` (prototype).
- AgentCard with `AgentCredentials`, `allowed_executors` at `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`.

### E.3 What's missing for a money-aware founder vessel [ASPIRATIONAL]

1. **x402 facilitator exposed as an MCP server** the Hermes profile can `dispatch()` against. Today the facilitator is Python in the ATLAS worktree, not wrapped in MCP.
2. **Spend caps + budget approval flow** integrated with Hermes `iteration_budget` and operator HITL. Today spend isn't budgeted at the dispatch layer.
3. **Vault host process** that holds signing keys. The repo specifies the split but no implementation exists in `/Users/rudlord/HORCRX/apps/` (verified: `apps/` has a single child dir).
4. **Receipt store** keyed by manifest CID + listing ID + nonce, with replay protection durable across restarts.
5. **Royalty resolver** that produces deterministic payout plans from signed parent lineage (specced in `/Users/rudlord/HORCRX/specs/marketplace/royalties.md`, not implemented in repo).
6. **Wallet rotation runbook** + revocation propagation (specced in `identity-and-keys.md` §4, not implemented).

### E.4 Phasing for the founder vessel

- **Phase 0:** Vessel earns nothing real. All "payments" are recorded as ledger rows with dry-run flag; no on-chain calls.
- **Phase 1:** Read-only chain calls (resolve owner, check balances) via Helius + Alchemy free tiers.
- **Phase 2:** x402 facilitator behind MCP, settled against a sandbox key with hard daily cap and required HITL approval per purchase ≥ cap.
- **Phase 3:** Production signing in isolated vault process, rotation tested, revocation propagation drilled.

---

## Section F — Observability + audit plan

The vessel **must** keep the following files/tables alive at all times. These are the load-bearing audit surfaces.

### F.1 Files

| Surface | Path | Schema source | Why |
|---|---|---|---|
| Hermes audit NDJSON | `~/.hermes/profiles/horcrx-founder/logs/hermes-audit.ndjson` | BINDING.md §8 hard constraint | Every LLM call must leave a row. |
| Hermes audit SQLite mirror | `~/.hermes/profiles/horcrx-founder/state/audit.sqlite` | BINDING.md §8 | Indexed query surface for the same events. |
| Vessel traces | `vessel/traces/YYYY-MM-DDTHHMMSSZ--<run-id>.ndjson` | `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md` | Portable, redacted episodic log suitable for export, replay, royalty proof. |
| Vessel lineage | `~/.hermes/profiles/horcrx-founder/state/vessel-lineage.sqlite` | BINDING.md §4.4 | Tracks installs, grafts, royalty_target, signed_manifest_cid. |
| Ledger | `vessel/ledger/<YYYY-MM>.ndjson` | NEW (this report) | Append-only money-flow record: action, manifest_cid, listing_id, chain, nonce, expiry, amount, status, evidence_cid. |
| Mission log | `vessel/mission/log.md` + `vessel/mission/MISSION.md` | NEW (this report) | Operator-readable narrative + structured mission/objective state. |
| Briefs | `vessel/briefs/<YYYY-MM-DD>--<topic>.md` | NEW (this report) | Daily/weekly reasoning briefs the vessel writes to itself. |
| Kanban substrate | `~/.hermes/kanban.db` | BINDING.md §8 hard constraint | Every meaningful action gets a card + 5-min heartbeat. |
| Notify log | `vessel/notify/notify.ndjson` | content-os pattern (`/Users/rudlord/.factory/skills/content-os/SKILL.md`) | Quiet-hours, throttle, deliver-once semantics for outbound messages. |

### F.2 NDJSON envelope (vessel-local additions)

Every row in `vessel/traces/*.ndjson` follows `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md` (`ts`, `run_id`, `event_id`, `stage`, `actor`, `summary`, `artifacts[]`, `redaction`, `provenance`). For money-relevant events, add (per `/Users/rudlord/HORCRX/docs/infrastructure/observability.md` §4.1):

- `action` ∈ {`vessel_purchase`, `vessel_install`, `x402_verify`, `signing`, `payout`}
- `manifest_cid`, `listing_id`, `vessel_cid`, `royalty_target`
- `chain`, `payment_reference`, `nonce`, `expiry`

### F.3 Metrics baseline

Adopt the names in `/Users/rudlord/HORCRX/docs/infrastructure/observability.md` §2: `horcrx_x402_verify_latency_ms`, `horcrx_replay_rejections_total`, `horcrx_signature_failures_total`, `horcrx_royalty_resolution_latency_ms`. Add three vessel-side:

- `horcrx_vessel_spend_usd_total{period}`
- `horcrx_vessel_iterations_total{run_id}`
- `horcrx_vessel_approval_pending_seconds{kind}`

### F.4 Alerting

Page on signature failures, replay rejections, missing audit rows for successful purchases (mirrors observability.md §6). Add vessel-specific: page on `horcrx_vessel_spend_usd_total` crossing the daily cap.

---

## Section G — Risk surface + mitigations

The vessel is a small money-aware autonomous agent. The risks are concrete.

| Risk | Concrete failure mode | Mitigation | Source |
|---|---|---|---|
| **Soul theft** | Unsigned export staging on a compromised host leaks identity + tone + behavioral patterns. | Sign only after allowlisted export; short-lived unsigned staging; manifest diff preview before sign. | `/Users/rudlord/HORCRX/docs/infrastructure/security.md` §2.1 |
| **Secret extraction at export** | Export accidentally includes `.env`, `auth.json`, `state.db`, wallet seed. | Strict export allowlist; strip-and-rehydrate posture in `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md`; secret scan before sign. | `/Users/rudlord/HORCRX/docs/infrastructure/security.md` §2 |
| **Key leak via subagent** | A dispatched droid or MCP server exfiltrates a private key from env. | Keys never enter the vessel runtime context. Signing happens in an isolated vault host that the Hermes profile reaches via a *bounded* MCP server with single-purpose `sign_*` verbs and required HITL ≥ cap. | `security.md` §3, `identity-and-keys.md` §3 |
| **Replay attack on x402 proofs** | Old payment proof reused to claim a new purchase. | Nonce + expiry + durable replay store; receipt binding to `manifest_cid` + `listing_id`; idempotent verifier. | `/Users/rudlord/HORCRX/specs/protocol/payment-layer.md` §2, `security.md` §2.1 |
| **Runaway spend** | The vessel loops, each iteration purchasing data, draining the wallet. | (1) Hermes iteration budget shared with subagents (BINDING.md §8); (2) per-day hard USD cap enforced *before* signing; (3) HITL approval required ≥ N USD; (4) cap-breach drops vessel into read-only mode and pages operator. | `iteration_budget.py`, this report §F.4 |
| **Infinite loop / context drift** | Ralph hat keeps re-architecting without shipping. | (1) Iteration budget cap; (2) Ralph "completion promise" (`/Users/rudlord/.claude/skills/loop-maestro/SKILL.md`); (3) cron tick replaces the live agent every N hours with a fresh-context successor. | loop-maestro SKILL.md |
| **Cron silently skipped** | `date +%U` returns wrong week and the job no-ops without erroring. | Use `date -u +%G-W%V` and fall back to most-recent-file-by-mtime per `/Users/rudlord/.factory/skills/iso-week-in-cron-scripts/SKILL.md`. | iso-week skill |
| **Audit row missing for paid action** | Purchase succeeds but no NDJSON row → no royalty attribution, no dispute trail. | Page alert on missing audit row (observability.md §6); refuse to sign without an audit handle. | observability.md §6 |
| **Branch-protection lockout for high-freq writes** | Vessel can't push 10-minute ledger updates to main. | `append-only-state-via-github-api`: per-actor branch via Contents API PUT, auto-merge workflow. | `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md` |
| **Canon write without GATE chain** | Vessel writes directly to `~/wiki/` and bypasses GATE-01..08. | Refuse direct writes; route through wiki-ingest. AGENTS.md off-limits enforced. | BINDING.md §8 hard constraint, `/Users/rudlord/HORCRX/AGENTS.md` |
| **Deepfake of operator** | Vessel impersonates Rudy in public messaging. | Separate creator/signer/installer identity surfaces; signer fingerprint shown on outbound posts. | `security.md` §2.1, `identity-and-keys.md` §1 |
| **Iteration-budget bypass** | Subagent silently exceeds parent budget. | Honor BINDING.md §8 "Iteration budget shared with subagents"; ADR 11 in `open-questions-resolved.md`. | `iteration_budget.py`, BINDING.md §9 |
| **Gateway/cache poisoning** | A scraped page or bundle is tampered en route. | Verify returned bytes against CID every fetch; dual-pin IPFS+Arweave for critical artifacts. | `security.md` §2.1 |

---

## Section H — Concrete file-tree proposal for vessel folder additions

Beyond the v0.1 vessel-format spec (`/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §2.1), the founder vessel adds the following folders. All are append-mostly and portable; secrets remain out per `security.md` §1.

```text
horcrx-003-founder/
├── soul.md                     # identity, voice (from SPEC.md §3.1)
├── agents.md                   # operational contract (from SPEC.md §3.1)
├── principles.md               # stable doctrine
├── intuition.md                # heuristics
├── dreams.md                   # reflection summaries
├── voice.md                    # tone rules
├── manifest.json               # bundle index
├── mark.svg                    # identity mark
│
├── skills/                     # SKILL.md packets (from SPEC.md §3.3)
├── plugins/
├── workflows/                  # declarative workflows
├── crons/
│   └── jobs.json               # disabled on import (BINDING.md §4.2)
├── traces/                     # NDJSON per traces-format.md
├── memory/
│   ├── canon.md
│   └── grafts/
│
├── mission/                    # NEW — operator-readable mission state
│   ├── MISSION.md              # current mission, objectives, success criteria
│   ├── VISION.md               # produced by paperclip-vision skill
│   ├── CEO_BOOTSTRAP.md        # produced by paperclip-vision skill
│   ├── log.md                  # running narrative, one row per tick
│   └── kanban-export.ndjson    # mirror of ~/.hermes/kanban.db rows for this vessel
│
├── ledger/                     # NEW — money flow, append-only
│   ├── 2026-05.ndjson          # one file per month, NDJSON rows
│   ├── 2026-06.ndjson
│   ├── caps.json               # daily/weekly USD caps, who-approved-what
│   └── receipts/               # raw x402 receipts keyed by CID
│       └── <manifest-cid>--<nonce>.json
│
├── briefs/                     # NEW — daily/weekly reasoning briefs
│   ├── daily/
│   │   └── 2026-05-27.md
│   ├── weekly/
│   │   └── 2026-W21.md         # per iso-week skill: use %G-W%V
│   └── retros/
│       └── 2026-05-26--retro.md
│
├── notify/                     # NEW — outbound message log
│   ├── notify.ndjson           # quiet-hours, throttle, dedup (content-os pattern)
│   └── policy.json             # quiet-hours, channel routing
│
├── wallets/                    # NEW — *public* wallet metadata only
│   ├── addresses.json          # public addresses by chain (NO private keys here)
│   ├── caps.json               # per-wallet daily cap
│   └── rotation-log.ndjson     # signed rotation events (BINDING.md §4.4 schema)
│
├── observability/              # NEW — vessel-side metrics + alerts config
│   ├── metrics-names.md        # canonical metric names (observability.md §2)
│   ├── dashboards.json         # 5-panel dashboard spec (observability.md §5)
│   └── alerts.json             # alert routing
│
├── governance/                 # NEW — approval state
│   ├── pending-approvals.ndjson    # HITL queue
│   ├── decisions.ndjson            # resolved approvals, append-only
│   └── policies.md                 # what requires HITL, what doesn't
│
└── multi-agent.yaml            # pack-only role graph (SPEC.md §6) — only if shipping as a pack
```

### Notes on the additions

- `mission/`, `ledger/`, `briefs/`, `notify/`, `wallets/` (public-only), `observability/`, `governance/` are **not** in `SPEC.md` §2.1; they are proposed here as portable-by-default vessel-level conventions. They mirror well-trodden patterns already live in `hermes-content-os` (audit, notify, kanban) and `content-flywheel` (append-only NDJSON).
- All seven folders are append-mostly and strip-safe by default. None contains secrets. Rotation events in `wallets/rotation-log.ndjson` are signed but reference only public material.
- The `wallets/` folder explicitly excludes private keys. Private keys live in a separate host (`security.md` §1 "Vault domain"). The vessel only carries public wallet metadata.

---

## Source paths (consolidated)

### [REPO]
- `/Users/rudlord/HORCRX/AGENTS.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/open-questions-resolved.md`
- `/Users/rudlord/HORCRX/specs/protocol/PROTOCOL.md`
- `/Users/rudlord/HORCRX/specs/protocol/payment-layer.md`
- `/Users/rudlord/HORCRX/specs/protocol/chain-adapters.md`
- `/Users/rudlord/HORCRX/specs/protocol/identity-and-keys.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
- `/Users/rudlord/HORCRX/specs/marketplace/ARCHITECTURE.md`
- `/Users/rudlord/HORCRX/specs/marketplace/royalties.md`
- `/Users/rudlord/HORCRX/specs/marketplace/discovery-and-trust.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/hosting.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/security.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/observability.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/local-dev.md`
- `/Users/rudlord/HORCRX/docs/infrastructure/services.md`
- `/Users/rudlord/HORCRX/research/04-economic-thesis.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/06-local-modules-inventory.md`
- `/Users/rudlord/HORCRX/research/07-skill-ecosystem-inventory.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`

### [LOCAL] — Hermes
- `/Users/rudlord/.hermes/hermes-agent/run_agent.py`
- `/Users/rudlord/.hermes/hermes-agent/AGENTS.md`
- `/Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py`
- `/Users/rudlord/.hermes/config.yaml`
- `/Users/rudlord/.hermes/honcho.json`
- `/Users/rudlord/.hermes/kanban.db`
- `/Users/rudlord/.hermes/profiles/factory-swarm/`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/cron/jobs.json`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`
- `/Users/rudlord/.hermes/profiles/orbel-orchestrator/`
- `/Users/rudlord/.hermes/profiles/github-steward/`
- `/Users/rudlord/.hermes/skills/kanban-task.md`

### [LOCAL] — Droids and skills
- `/Users/rudlord/.factory/droids/worker.md`
- `/Users/rudlord/.factory/droids/coder/`
- `/Users/rudlord/.factory/droids/factory-codex/`
- `/Users/rudlord/.factory/droids/deepseek-researcher/`
- `/Users/rudlord/.factory/droids/kimi-research/`
- `/Users/rudlord/.factory/skills/content-os/SKILL.md`
- `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md`
- `/Users/rudlord/.factory/skills/solo-duo-operator-mode/SKILL.md`
- `/Users/rudlord/.factory/skills/iso-week-in-cron-scripts/SKILL.md`
- `/Users/rudlord/.claude/skills/loop-maestro/SKILL.md`
- `/Users/rudlord/.claude/skills/claudeception/SKILL.md`
- `/Users/rudlord/.claude/skills/render-workflows/SKILL.md`
- `/Users/rudlord/.claude/skills/agent-browser/SKILL.md`
- `/Users/rudlord/.claude/skills/hermes-agent-mcp-server-registration/SKILL.md`
- `/Users/rudlord/.agents/skills/dispatching-parallel-agents/SKILL.md`
- `/Users/rudlord/.agents/skills/orchestration/SKILL.md`
- `/Users/rudlord/.agents/skills/postiz/SKILL.md`
- `/Users/rudlord/.agents/skills/supabase/SKILL.md`
- `/Users/rudlord/ORGANIZED/agents/factory-swarm/vendor/paperclip/skills/paperclip-vision/`

### [LOCAL] — ATLAS prior art
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`

### [LOCAL] — Wiki
- `/Users/rudlord/wiki/hermes.md`
- `/Users/rudlord/wiki/AGENTS.md` *(not directly read here; referenced by BINDING.md)*
- `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
- `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/system-map.md`
