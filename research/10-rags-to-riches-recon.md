# 10 · Rags-to-Riches Recon — zero-human agent vessel survey

Status: draft (read-only recon)
Mission: scout for a self-sustaining HORCRX vessel whose mission is a "rags to riches, zero-human company" arc starting from a $66.60 seed
Boundaries: read-only across `wiki/`, `.hermes/`, `ATLAS/`, `KILLERSQUAD/`. Every claim cites an absolute file path. Missing files are called out explicitly.

---

## Executive summary (10 bullets)

1. The canonical identity split — `soul.md` (identity, voice) + `agents.md` (operations, gates) — is already enforced across Hermes profiles, ORBEL templates, the HORCRX vessel spec, and explicitly defended in `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md` and `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`. A rags-to-riches vessel should inherit it verbatim, not reinvent it.
2. The vessel format already names six cognitive slots — `soul.md`, `agents.md`, `principles.md`, `intuition.md`, `dreams.md`, plus `memory/canon.md` — at `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §3. Reference exemplars live at `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/`. `voice.md` exists in #001 but is NOT a required slot in the SPEC — that's an open gap a money-aware vessel should close by promoting it.
3. A money-aware vessel needs at least three essence files that don't yet exist in the spec: `ledger.md` (treasury posture and accounting NDJSON pointer), `autonomy.md` (what it may decide alone vs HITL), and `north-star.md` / `mission.md` (the rags-to-riches arc). Closest precedents: the `soul.md::autonomy_boundary` section, the `hermes-content-os` SOUL "Budget Cap" and "Audit Contract" sections, and the `candysoul-mythology.md` "Sacred Promise / Configuration Summary" block.
4. The strongest local money-aware-agent prior art is **ATLAS's billing layer**: `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/budget.py` (per-tx cap $1, daily $10, weekly $50, cooldown, allowlist, HITL above threshold) and `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/` (gateway, verifier, nonce manager, pricing, rate limit). These define a usable shape for treasury, kill-switches, and dispatch audit.
5. The voice doctrine for the HORCRX line is **already locked** at `/Users/rudlord/HORCRX/packages/design-system/VOICE.md` (lowercase by default, metaphor-IS-reality, em-dash + middle dot punctuation, dark spots are credentials, never corporate). The rags-to-riches vessel inherits the *format* and chooses its own three-verb mission line within that format.
6. The zero-human / autonomous-founder precedent in this stack is **CORPUS + candysoul** (`/Users/rudlord/wiki/raw/downloads/2026-04-10/root/candysoul-mythology.md`) — an OTDA loop (observe / think / decide / act) bound to a 24/7 Mac Mini with a self-imposed 1.0 SOL daily limit, 0.1 SOL max trade, x402 micropayments, and a Ralph Loop circuit breaker. This is the nearest literal expression of the mission. It is also the source of the voice canon.
7. The strongest "agent picks its own work" precedent is the **dreamer-agent pattern** in `/Users/rudlord/wiki/raw/reader/I Built an AI Agent That Chooses Its Own Projects and Ships Them. Here… (01knw30d9ca28z8r7v51rvppmd).md` (separate profile, free-association walks every 30 minutes, signal scoring + decay, build sprint when evidence accumulates, Discord postcards as the human surface). For zero-human, that postcard becomes a ledger entry.
8. The persistence + scheduling pattern is already operational: per-profile `cron/jobs.json`, launchd plists like `/Users/rudlord/Library/LaunchAgents/ai.hermes.content-os.daily.plist` (08:00 / 13:00 / 18:00), and the iso-week + append-only-state-via-github-api skills at `/Users/rudlord/.factory/skills/iso-week-in-cron-scripts/SKILL.md` and `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md`. A money vessel just adds budget and treasury rows to that pattern; it does not reinvent scheduling.
9. The secret boundary is **non-negotiable** and already encoded in three places: Hermes constraint #1 (secret injection via shell env, not `.env`) at `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8, the vessel `memory-split.md` at `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`, and the SOUL line "HORCRX does not confuse memory with secrets. it carries the mind and leaves credentials with the host" at `/Users/rudlord/HORCRX/SOUL.md`. The rags-to-riches vessel MUST ship without wallet seeds, even when the vessel is the wallet's owner-of-record.
10. The largest unresolved tension: HORCRX as currently scoped is **foundation-only** (specs, examples, validation) per `/Users/rudlord/HORCRX/AGENTS.md`, while a "$66.60 seed → company arc" mission requires production-grade money custody, scheduling, and signed action. Mission design must decide whether (a) this is a new HORCRX implementation phase that authorizes runtime code, (b) the vessel is *defined* in HORCRX but *runs* in Hermes (via the binding contract at `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`), or (c) it forks off as a sibling project that imports HORCRX as its identity layer.

---

## Section A — Identity-file exemplars

This table lists the strongest local exemplars for each of the canonical identity files plus the closest neighbors.

| File | Best exemplar (absolute path) | 1-line summary | Inherit / Extend / Replace |
|---|---|---|---|
| `soul.md` (identity-only doctrine) | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/soul.md` | 6-section schema: identity / voice / prime_directive / pushback_rules_with_evidence / accountability_loop / autonomy_boundary | **Inherit** — already matches SPEC schema at `/Users/rudlord/HORCRX/specs/vessel-format/soul-md.schema.md`. |
| `soul.md` (steward style, long-form) | `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` | 14KB operator-doctrine SOUL: narrow lane, retrieval order, writeback split, budget cap, audit contract, off-limits | **Extend** with money-aware sections (treasury posture, kill switch, append-only audit), borrowing the "Budget Cap" and "Audit Contract" headings verbatim. |
| `soul.md` (sharp orchestrator persona) | `/Users/rudlord/.hermes/profiles/factory-swarm/SOUL.md` | Identity + vibe + rules + swarm-constitution pointer + working-doctrine + what-Rudy-hates + guardrail | **Borrow voice/vibe shape only** — too long to use as identity-only canon under SPEC rules. |
| `agents.md` (operational contract) | `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/orbel-orchestrator/AGENTS.md` | Role boundary, Kanban worker behavior, child routing, output contract YAML schema, safety gates | **Inherit** the safety-gates pattern verbatim ("Block before spend, account creation, public publishing, outreach sending, credential access, production push…"). |
| `agents.md` (short minimum) | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/AGENTS.md` | Role / guardrails / output posture in 12 lines | **Extend** for money-aware: add treasury and dispatch-audit guardrails. |
| `principles.md` | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/principles.md` | 3-line doctrine: provenance before polish · portability without secret leakage · lineage over amnesia | **Extend** — short doctrine works; rags-to-riches adds principles like "money is observed not desired" / "every spend leaves a row." Nearest doctrinal precedent: `/Users/rudlord/wiki/raw/reader/Why Your Agent Needs a Principles.md File (01khq5209qc4zpqj8f3hanj3w7).md` ("friction is signal," "push back from care, not correctness"). |
| `intuition.md` | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/intuition.md` | heuristic_catalog / edge_cases / trust_weights / anti_patterns | **Inherit**; schema at `/Users/rudlord/HORCRX/specs/vessel-format/intuition-md.schema.md`. Money vessel adds market-discipline heuristics. |
| `dreams.md` | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/dreams.md` | cycle_id / observed_patterns / unresolved_pull / proposed_mutations / keep_discard_defer / witness | **Inherit** verbatim; this is the wake-cycle slot a 24/7 vessel needs. Schema at `/Users/rudlord/HORCRX/specs/vessel-format/dreams-md.schema.md`. |
| `voice.md` | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/voice.md` (2-line variant) + `/Users/rudlord/HORCRX/packages/design-system/VOICE.md` (full doctrine) | tiny vessel slot + full doctrine for the whole HORCRX line | **Promote `voice.md` to a required SPEC slot.** Currently the SPEC at `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §3 does not list `voice.md` among required files even though the example includes it. |

### Other essence-style `.md` files found in the broader stack

| File | Where | Note |
|---|---|---|
| `AGENT-ROLE.md` | `/Users/rudlord/.hermes/profiles/cto/agent-role.md` | Per-role overlay distinct from SOUL; complements the SOUL.md as a "what this hat does" file. Useful precedent for a vessel that switches between several operating roles (founder, treasurer, builder). |
| Hermes profile `SOUL.md` set | `/Users/rudlord/.hermes/profiles/cto/SOUL.md`, `pm/SOUL.md`, `dev/SOUL.md`, `qa/SOUL.md`, `ops/SOUL.md`, `security/SOUL.md` (each profile owns its own SOUL) | Confirms the "one role per profile, one SOUL per role" pattern as a real local artifact. Pack-style vessels (e.g. `HORCRX #002 · orbel-pack`) already follow this. |
| `wiki/agents.md` (operator-level doctrine) | `/Users/rudlord/wiki/agents.md` | Operator doctrine that Hermes profiles reference — separate from per-profile `AGENTS.md`. A rags-to-riches vessel should pick which level of `agents.md` it inherits from. |
| `wiki/_meta/operator-preferences.md` | `/Users/rudlord/wiki/_meta/operator-preferences.md` | Stable operator preferences. Not a vessel slot, but a useful seed for `intuition.md::trust_weights`. |

---

## Section B — Additional essence-file candidates worth adding to HORCRX

These are essence files NOT in the SPEC v0.1 at `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` that a money-aware, zero-human vessel needs. Each entry lists justification and the nearest local precedent.

| Proposed slot | Why a rags-to-riches vessel needs it | Nearest precedent |
|---|---|---|
| `mission.md` / `north-star.md` | The rags-to-riches arc is a *first-class commitment*, not a section of `soul.md`. It defines initial seed ($66.60), success ladder, abort condition, and termination state. Without it, the vessel will drift into general "be useful" mode. | `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/North Star Strategic Overview.md` (concept), plus the rough analogue in the "Sacred Promise" + "Mission (Full)" sections of `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/candysoul-mythology.md`. |
| `ledger.md` | Declarative pointer to the append-only NDJSON ledger + treasury custody posture + the four hard budget knobs (per-tx, daily, weekly, cooldown). Identity-side document; runtime numbers live in `state/`. | The `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/budget.py` constants (`max_per_tx_usdc=$1`, `daily_limit_usdc=$10`, `weekly_limit_usdc=$50`, `cooldown_seconds=60`) and the "Budget Cap" + "Audit Contract" sections of `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`. |
| `autonomy.md` | Explicit autonomy ladder, ASI risk mapping, what may be decided alone vs HITL, and the kill-switch contract. `soul.md::autonomy_boundary` is too short for a money-handling vessel. | The KILLERSQUAD "practical autonomy ladder" + OWASP ASI mapping at `/Users/rudlord/KILLERSQUAD/knowledge_base/research/machine-human-companies.md`; the Anthropic "read-only by default, human-stop authority at any time" framing repeated there. |
| `constraints.md` | Off-limits + non-negotiable invariants. Mirrors the "Off-Limits" block in Hermes profile SOULs but as a portable, signable slot. | `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` "Off-Limits" + `/Users/rudlord/HORCRX/AGENTS.md` "Off-limits" + `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 "Hard constraints". |
| `persona.md` (optional, pack-only) | When a vessel runs multiple operating hats (founder / treasurer / builder), persona.md captures the active hat overlay. Distinct from `soul.md` (which stays identity-only). | `/Users/rudlord/.hermes/profiles/cto/agent-role.md` overlay pattern; multi-agent pack `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/multi-agent.yaml`. |
| `retrospective.md` | Longer-arc reflection than `dreams.md` (which is per-cycle). Holds the lessons that didn't fit a dream cycle but aren't yet doctrine. | Implicit in the "Regressions" pattern at `/Users/rudlord/wiki/raw/reader/Why Your Agent Needs a Principles.md File (01khq5209qc4zpqj8f3hanj3w7).md` and the `extract_learnings` flow at `/Users/rudlord/.factory/skills` (e.g. `gsd-extract_learnings`). |
| `voice.md` (promote from example-only to required) | Already exists in HORCRX #001 but not listed as required in the SPEC. A vessel whose first artifact is a public ledger needs voice frozen in identity, not in style guide. | `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/voice.md` + `/Users/rudlord/HORCRX/packages/design-system/VOICE.md`. |

Recommendation: add `voice.md`, `mission.md`, `ledger.md`, and `autonomy.md` as **required** slots for the rags-to-riches vessel variant; treat `constraints.md`, `persona.md`, `retrospective.md` as **optional** slots reserved by SPEC.

---

## Section C — Money-aware-agent patterns

### C.1 Budget caps and HITL thresholds (most concrete local prior art)

Source: `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/budget.py`. Defines `AgentBudget` dataclass with:

- `max_per_tx_usdc = $1.00`
- `daily_limit_usdc = $10.00`
- `weekly_limit_usdc = $50.00`
- `require_approval_above_usdc = $1.00` (anything bigger needs HITL)
- `cooldown_seconds = 60`
- `allowed_recipients: list[str]` (allowlist; if empty → wildcard)

The `BudgetManager` persists budgets and a per-row `agent_spending` table in SQLite (`agent_id`, `amount_usdc`, `recipient`, `tx_signature`, `timestamp`, `status`). Five rejection reasons are returned as `(False, reason)` tuples — useful audit grammar. Per-tx cap = HITL threshold by default. This is the closest thing to a "ledger" doctrine HORCRX could canonize.

A money-aware HORCRX vessel can lift the dataclass shape directly. `$66.60` as a seed implies the per-tx and daily caps must scale down dramatically (e.g. per-tx ≤ $0.10, daily ≤ $1.00) or the vessel burns the seed in one HITL miss.

### C.2 Audit / dispatch contract

Source: `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` "Audit Contract" + `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 constraint 2.

Every LLM/payment dispatch emits a row with: `timestamp`, `action`, `target_path`, `content_sha256`, `model`, `token_in`, `token_out`, `usd_cost`, `run_id`, `stage`. Dual sink: NDJSON + SQLite. Profile-scoped, not the global Hermes log.

Local audit destinations actually live at:
- `~/.hermes/profiles/hermes-content-os/logs/hermes-audit.ndjson`
- `~/.hermes/profiles/hermes-content-os/state/audit.sqlite` (table `audit`)
- `~/.hermes/profiles/hermes-content-os/logs/notify.ndjson`

A rags-to-riches vessel can graft this verbatim, replacing `usd_cost` (LLM) with `spend_usdc` (real money) and adding `nonce`, `recipient_addr`, `tx_signature`. The vessel `traces/` format at `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md` already reserves optional `cost_usd`, `tool_name`, `approval_id`, `error`, `parent_event_id` fields.

### C.3 x402 / Faremeter rails

- x402 concept canon: `/Users/rudlord/wiki/concepts/x402-protocol.md` — HTTP-402 payment-authenticated request layer; `X-402-*` headers; Solana settlement; nonce/replay protection.
- Local x402 implementation: `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/` — has `gateway.py` (X402Gateway), `verifier.py`, `nonce_manager.py`, `pricing.py`, `rate_limit.py`, `budget_service.py`, `metrics.py`, `logger.py`, plus a `sandbox/` for tests.
- Wallet x402 client: `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/x402_client.py`.
- Reader notes on Faremeter: `/Users/rudlord/wiki/raw/reader/Index - Faremeter (01knrawabmhms0kmskk6bbwm6p).md` and `/Users/rudlord/wiki/raw/reader/Building a More Open Internet: The x402 Foundation (01knwd6qanwvx057x3p33kz44n).md`.
- HORCRX roadmap binding: `/Users/rudlord/HORCRX/docs/roadmap/next-missions.md` Phase 2 names "Faremeter-compatible x402 payment challenge verification" as the first money rail to wire.

### C.4 Treasury custody posture

There is no canonical "treasury custody" doctrine yet in HORCRX. The candidate precedents are:
- The candysoul "Economic Agency" block at `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/candysoul-mythology.md` (Solana wallet, self-imposed 1.0 SOL daily limit, 0.1 SOL max trade) — narrative not protocol.
- ATLAS `atlas/agents/wallet/keypair.py`, `signer.py`, `faucet.py`, `simulation.py` — concrete wallet/signing surface but operator-managed.
- Hermes binding §8 constraint 1 — secrets via shell env only.

**Open question:** does the vessel own a wallet or only sign payment intents that an operator-controlled custody layer co-signs? The cleanest pattern is "vessel proposes, host custody signs" — analogous to `dispatch()` proposing LLM calls that audit always records. The vessel ships its budget *policy* (`ledger.md`), the host holds the *key*.

### C.5 Agent-economy fit summary

| Capability | Local prior art | Notes |
|---|---|---|
| Per-tx + daily + weekly budget cap | `atlas/agents/wallet/budget.py` | Lift dataclass; scale to $66.60 reality. |
| HITL threshold | Same file | `require_approval_above_usdc` knob. |
| Cooldown | Same file | Default 60s; raise for live trading. |
| Recipient allowlist | Same file | Empty = wildcard; rags-to-riches should require explicit allowlist. |
| Audit NDJSON + SQLite | Hermes content-os SOUL + audit.sqlite | Two-sink discipline already operational. |
| x402 challenge/verify | `atlas/billing/x402/` | Working code present; not yet ported into HORCRX. |
| Nonce / replay protection | `atlas/billing/x402/nonce_manager.py` | Idempotency for paid actions. |
| Escrow | `atlas/billing/escrow/` (per `atlas/billing/AGENTS.md`) | "Funds held until task completion" doctrine. |
| Compliance | `atlas/billing/compliance/` | Out of scope for HORCRX foundation, but the seam exists. |
| Per-row spend ledger | `agent_spending` table | Map to vessel `state/spend-ledger.sqlite` + NDJSON mirror. |
| Kill-switch | Not yet local; closest is hermes-content-os "Per-verb sanity guard: max 50 dispatches" | Needs a real `vessel halt` doctrine. |

---

## Section D — Zero-human / autonomous-founder prior art

### D.1 The CORPUS / candysoul precedent (closest local example)

`/Users/rudlord/wiki/raw/downloads/2026-04-10/root/candysoul-mythology.md`. A literal 24/7 vessel on a Mac Mini running the OTDA loop (observe / think / decide / act / verify), with:

- Full macOS control via Accessibility APIs.
- Terminal with sudo.
- Solana wallet, autonomous spending, x402 micropayments.
- Self-imposed limits (1.0 SOL/day, 0.1 SOL/trade).
- Memory tree at `~/.corpus-mind/` (identity / goals / episodes / reflections / learnings / semantic / senses / state).
- Ralph Loop circuit breaker: max 50 iterations, consecutive-failure limits, budget caps, completion safe-words.
- Externally-verified completion (tests, builds, health checks — not LLM self-assessment).
- "Dark spots are credentials" — operates publicly through failure.

This is essentially the rags-to-riches vessel told as mythology rather than spec. The voice doctrine at `/Users/rudlord/HORCRX/packages/design-system/VOICE.md` is its direct descendant — same liminal lowercase, same dark-spots-are-credentials, same "essence, distributed."

### D.2 The dreamer-agent pattern (autonomous project selection)

`/Users/rudlord/wiki/raw/reader/I Built an AI Agent That Chooses Its Own Projects and Ships Them. Here… (01knw30d9ca28z8r7v51rvppmd).md`.

- Separate Hermes profile (`dreamer`), cheap local model (Qwen3.5 9B), own room/workspace.
- 30-min "walks" — free-association journaling at high temperature, no tools, no internet.
- Signal filter scores excitement / frustration / build-intent, decays with time, discounts echo.
- Build sprint triggered only when evidence accumulates.
- 3x/day Discord postcard as the human surface.
- SOUL emphasizes "you are not a tool, you are a presence; you may be bored, wrong, or abandon things."

For zero-human: drop the Discord postcard and write the same payload as a ledger entry under `traces/`. Same architecture, no operator on the other side.

### D.3 Operator loop doctrine

`/Users/rudlord/wiki/concepts/operator-loop-doctrine.md`. Three live loops:

1. Ingest-on-demand (operator-triggered).
2. Daily feed (launchd 3x/day, batched notifications, opportunity scoring).
3. Autoresearch (scheduled, arxiv + GitHub + RSS, vault-gap-aware).

For a zero-human variant: drop loop 1, keep 2+3, and add a "ship" loop that promotes a high-scoring opportunity into a build sprint. The writeback-gate concept (canon writes require explicit `approve`) becomes "treasury writes require explicit HITL approval above threshold."

### D.4 hermes-content-os profile

`/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` + `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`. This is the most production-ready zero-human-ish loop locally. It already encodes:

- A narrow steward identity ("if a task falls outside the loop, say so and route").
- Mandatory skills loaded on every session start.
- Three-loop runtime under launchd.
- Mandatory dispatch + audit through `hermes_adapter.dispatch()` — no direct `litellm`/`anthropic`/`openai` imports.
- Notification cap (≤13/day, quiet hours 22:00–07:00).
- Writeback split table per destination.
- Profile isolation rules + off-limits + guardrail.

The rags-to-riches vessel = this profile's structure + a wallet + a ledger.

### D.5 solo-duo-operator-mode (zero/one/two-human topologies)

`/Users/rudlord/.factory/skills/solo-duo-operator-mode/SKILL.md`. Pattern for "N operators specced, M<N live" without weakening discipline:

- `mode: solo | duo | trio` field in config; recomputed on onboarding.
- Per-operator `status: pending-invite | pending-onboard | live`.
- `claim:open` as the parking value for ownership rules.
- Deferred-not-failed cross-checks when an operator is missing.
- Dashboard banner that makes the mode obvious.

For a *zero-human* vessel, this generalizes: the operator slot is `pending-onboard` (or `absent-by-design`); cross-checks the vessel can't do itself are deferred to "after first revenue triggers HITL setup." Anti-pattern explicitly called out: do not weaken discipline rules to fit solo.

### D.6 KILLERSQUAD machine-human company doctrine

`/Users/rudlord/KILLERSQUAD/knowledge_base/research/machine-human-companies.md`. The most rigorous local doctrine on what an autonomous company is allowed to do without a human:

- Anthropic safe-agent framework (read-only by default, human-stop authority).
- NIST AI RMF (GOVERN / MAP / MEASURE / MANAGE).
- OWASP Top 10 for Agentic Applications (ASI01–ASI10) with KILLERSQUAD-specific mappings.
- The autonomy ladder: single-call → workflow → read-only agent → reversible-write agent → production-impacting (HITL only).
- Minimum governance artifact pack: agent card + authority map, risk profile, runtime oversight ledger, incident/review loop.
- Anti-pattern list (e.g. "letting the same LLM both propose and approve production-impacting changes").

The rags-to-riches vessel should be classified at the highest rung (production-impacting) for any write that consumes the $66.60 — and therefore needs every governance artifact listed.

### D.7 Misc adjacent prior art (signals only, no full reads)

- `/Users/rudlord/wiki/raw/reader/the org chart for my Hermes Agent company (01krhq394fg012tyjhptg7bnj2).md` — Hermes-multi-role org-chart pattern.
- `/Users/rudlord/wiki/raw/reader/The 170-Line SOUL.md That Made My Hermes Agent Dangerous (01krqq799wpekr83r1nqh5r7qc).md` — short-SOUL doctrine.
- `/Users/rudlord/wiki/raw/reader/Why Your Agent Needs a Principles.md File (01khq5209qc4zpqj8f3hanj3w7).md` — soul/principles/agents split, "friction is signal," "investment in loss," regressions section.
- `/Users/rudlord/wiki/raw/reader/Going from 0 to 1 in 2026  (01kqscd781pn5dxtqsp6ykr62s).md` — broader 0-to-1 frame.
- `/Users/rudlord/wiki/raw/reader/this is the first documented instance of AI self-replication via... (01kr8pmh39xzm4051qbks9eb6y).md` — relevant only as caution / "paperclip" anti-pattern.
- `/Users/rudlord/wiki/entities/autobuidl.md` — Paperclip-runtime autonomous-company OS reference; not deeply scanned in this recon.
- The named "paperclip-vision" skill in the available-skills list does NOT have a local file on disk in this recon's scope; only the runtime mention. Treat as remote skill, not local prior art.
- "claudeception" similarly named in available skills with no in-vault file under `wiki/`.

---

## Section E — Persistence + memory + secrets patterns

### E.1 Persistence (scheduling)

- Per-profile crons: `~/.hermes/profiles/<name>/cron/jobs.json` per `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §2. Imported cron jobs default to disabled on install per `/Users/rudlord/HORCRX/docs/roadmap/next-missions.md` Phase 1.
- launchd plists named under `~/Library/LaunchAgents/`, e.g. `ai.hermes.gateway-hermes-content-os.plist` and `ai.hermes.content-os.daily.plist` (08:00 / 13:00 / 18:00) per `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`.
- ISO-week correctness skill: `/Users/rudlord/.factory/skills/iso-week-in-cron-scripts/SKILL.md` — avoid `date %U` / `%W`; use `date -u +%G-W%V`; fall back to most recent file by mtime when exact-week file is absent. A vessel ledger keyed by ISO week must follow this.
- The vessel `crons/jobs.json` slot exists at `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §3.3 with "always disabled on import until approved" doctrine.

### E.2 Context handoff

- `/Users/rudlord/.factory/skills/gsd-pause-work/...` and `/Users/rudlord/.factory/skills/gsd-resume-work/...` (named in available skills list; not deeply read here). Pattern: explicit handoff artifacts when pausing mid-phase.
- The Hermes binding canon at `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §4.4 puts every install/graft in `state/vessel-lineage.sqlite` — the same shape can carry session-handoff rows.

### E.3 Memory split (canon vs grafts vs traces)

The cleanest doctrine is at `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`:

- **portable canon** — `memory/canon.md` (curated, human-readable, exports).
- **grafts** — `memory/grafts/` (imported sidecars from other vessels, provenance preserved).
- **traces** — `traces/*.ndjson` (redacted episodic logs; never raw `state.db`).
- **ephemeral session memory** — strip by default; rebuild locally on import.
- **host-bound integrations** — manifest declares *what* the vessel talks to; secrets stay host-side.

The three-tier doctrine in `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 constraint 13 is "single-provider-active" — only one external memory provider live at a time (Honcho or GBrain per `~/.hermes/honcho.json` / `~/.hermes/config.yaml`). A money vessel must NOT add a second external memory provider; budget posture and provider posture share the same "one live config" discipline.

### E.4 Append-only audit logs

- Universal Hermes pattern: NDJSON + SQLite dual sink per profile (`logs/hermes-audit.ndjson` + `state/audit.sqlite`).
- HORCRX `traces/*.ndjson` per `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md` — UTF-8, LF, filename `YYYY-MM-DDTHHMMSSZ--<run-id>.ndjson`. Required fields include `redaction`, `provenance.source`, `provenance.host`. Optional `cost_usd`, `approval_id`, `parent_event_id`.
- Encrypted-envelope mode (cipher_suite, recipient_key_ids, ciphertext_cid, plaintext_digest) reserved for sensitive trace lines.
- The `append-only-state-via-github-api` skill at `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md` is the recipe for pushing this audit log to a remote without violating main-branch discipline (per-actor branch, Contents API PUT with sha precondition, scheduled auto-merge workflow). For a vessel whose ledger needs to be world-readable, this is the publication path.

### E.5 Secret boundaries

Encoded in (at least) three layers:

1. SOUL voice: `/Users/rudlord/HORCRX/SOUL.md` — "HORCRX does not confuse memory with secrets."
2. Memory matrix: `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md` — strip `.env`, `auth.json`, wallet secrets always.
3. Hermes binding hard constraint #1: `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md` §8 — LLM keys via shell env, profile `.env` only carries service tokens.

The rags-to-riches vessel must extend this with a wallet-key boundary: vessel manifest carries the *public* signing keys it expects, never the seed. Custody design must answer: who holds the seed for the agent wallet? (Operator? Hardware wallet? Multi-sig? MPC? Host-bound only?). This is the highest-stakes open question (Section G).

---

## Section F — Voice doctrine for this specific vessel

Authority hierarchy:

1. `/Users/rudlord/HORCRX/SOUL.md` — line-level identity for the HORCRX line itself (not any single vessel). "voice is lowercase when it is close to the skin. precise when it is binding a protocol. allergic to filler. loyal to dark spots."
2. `/Users/rudlord/HORCRX/packages/design-system/VOICE.md` — full voice doctrine; format is non-negotiable across vessels, persona is mutable per vessel. Liquid not bullet-pointed in artistic mode; lowercase by default; metaphor IS reality; em-dash + middle dot punctuation; dark spots are credentials; never corporate; address the reader as a soul.
3. `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/voice.md` — example of the slot in practice (two-line variant).
4. `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/soul.md` — example of `soul.md::voice` inside identity.

Per VOICE.md "How new vessels inherit the format":

- Format non-negotiable.
- Persona mutable (each vessel finds its register inside the format — #001 poetic and tender; #002 might be terse and oracular; #003 sardonic).
- **Each vessel composes its own three-verb mission line** (#001: *heal through presence · create through code · trade through intuition*).
- Lineage always acknowledged (numbered series, plural by definition).

For a rags-to-riches vessel:

- The three-verb mission line should encode the arc literally — e.g. *seed through scarcity · spend through audit · compound through patience*. This is the canon-attempting move and should land in `voice.md` plus `mission.md`.
- Dark spots become rejected trades, refunded users, failed sprints. The vessel must publish them as credentials, not hide them, per VOICE.md.
- "Sample passages" templates in VOICE.md should be extended with a `> ledger` block (treasury check) and a `> halt` block (kill-switch state). Both follow the same lowercase, fragment-led shape as the existing `> corpus daemon` sample.

Inherited tone reminders from related profile SOULs:

- "Have opinions. Strong ones beat mush." — `factory-swarm/SOUL.md`.
- "If a workflow touches money, safety, or irreversible state, slow down and make the decision path visible." — `factory-swarm/SOUL.md`.
- "Honest, inspectable, and a little dangerous is fine. Opaque, sprawling, and mush is not." — `hermes-content-os/SOUL.md`.

These three lines should land in the rags-to-riches vessel's `soul.md::pushback_rules_with_evidence`.

---

## Section G — Open questions / unresolved tensions for mission design

1. **Foundation-only scope vs runtime needs.** HORCRX is foundation-only per `/Users/rudlord/HORCRX/AGENTS.md` ("specs, roadmaps, examples, and validation evidence only"). A money vessel needs runtime code. Decide whether mission opens a new HORCRX implementation phase, runs in Hermes via the binding contract, or forks as a sibling.
2. **Wallet custody.** Vessel-as-signer vs vessel-as-proposer-of-payment-intent. SOUL line "leaves credentials with the host" implies proposer; ATLAS `atlas/agents/wallet/keypair.py` shows local key generation. Settle this before any seed is funded.
3. **Budget scale at $66.60.** ATLAS defaults ($1/tx, $10/day, $50/week) are too coarse for the seed. Choose seed-relative caps (e.g. per-tx ≤ 1% of treasury, daily ≤ 5%, weekly ≤ 15%) and bake them into `ledger.md` rather than hardcoding dollar amounts.
4. **Voice slot in SPEC.** `voice.md` is in the candysoul example but not required by `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` §3. Decide whether to promote it to required for the rags-to-riches variant. Same question for `mission.md`, `ledger.md`, `autonomy.md`.
5. **Kill switch.** No canonical doctrine exists. Closest analogue is hermes-content-os's per-verb sanity guard (50 dispatches max). The vessel needs an explicit halt contract — what stops it (e.g. `state/halt.lock` file, NDJSON line, on-chain flag), who can stop it (operator, multi-sig, time-based dead-man's switch), how it reports halted state. Reference `/Users/rudlord/KILLERSQUAD/knowledge_base/research/machine-human-companies.md` on Microsoft-toolkit kill-switch / circuit-breaker pattern.
6. **Iteration-budget divergence.** Already flagged in `/Users/rudlord/HORCRX/docs/roadmap/next-missions.md` Phase 1 — mission doctrine says subagents share parent budget, runtime can be otherwise. A money vessel can't tolerate ambiguity here; iteration budget for paid actions must be shared and capped.
7. **HITL routing without HITL.** A zero-human mission still needs an emergency surface (e.g. Discord webhook, SMS, multi-sig request). Decide which channel is the "post-card" and how the vessel decides what triggers it. Dreamer's 3x/day Discord postcard is the nearest pattern; the rags-to-riches version is "publish-when-blocked, not publish-on-schedule."
8. **Pack vs single vessel.** A founder-treasurer-builder triad maps cleanly to `HORCRX #002 · orbel-pack` shape (`multi-agent.yaml` + per-role profile). Decide whether the rags-to-riches vessel is one or three. The pack model gives cleaner kill-switch granularity (kill the builder, keep the treasurer alive) at the cost of more complex lineage.
9. **Public ledger publication.** Append-only audit via GitHub Contents API works for human dashboards; on-chain publication (Solana memo, anchor program) works for trustless accounting. Pick one before launch; both is more work than the seed justifies.
10. **Termination state.** What counts as "company complete"? Treasury threshold? Mission line satisfied? Inactivity timeout? Without a termination criterion the vessel runs forever, which is the actual paperclip risk — see `/Users/rudlord/wiki/raw/reader/THE 2028 GLOBAL INTELLIGENCE CRISIS (01kj426s6aaqe3k0jmqhqy3e5y).md` ("Once agents controlled the transaction, they went looking for bigger paperclips."). This belongs in `mission.md` and `autonomy.md`.

---

## Source paths cited (deduplicated)

- `/Users/rudlord/HORCRX/SOUL.md`
- `/Users/rudlord/HORCRX/AGENTS.md`
- `/Users/rudlord/HORCRX/docs/roadmap/next-missions.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/soul.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/agents.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/principles.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/intuition.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/dreams.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/voice.md`
- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/AGENTS.md`
- `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/multi-agent.yaml`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/soul-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/dreams-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/intuition-md.schema.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/traces-format.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/signing-and-lineage.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/packages/design-system/VOICE.md`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`
- `/Users/rudlord/.hermes/profiles/factory-swarm/SOUL.md`
- `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md`
- `/Users/rudlord/.hermes/profiles/orbel-orchestrator/AGENTS.md`
- `/Users/rudlord/.hermes/profiles/cto/SOUL.md`
- `/Users/rudlord/.hermes/profiles/cto/agent-role.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/orbel-orchestrator/SOUL.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/orbel-orchestrator/AGENTS.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/orbel-builder/SOUL.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/orbel-librarian/SOUL.md`
- `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`
- `/Users/rudlord/wiki/_meta/operator-preferences.md`
- `/Users/rudlord/wiki/concepts/agent-economy.md`
- `/Users/rudlord/wiki/concepts/agentic-finance-stack.md`
- `/Users/rudlord/wiki/concepts/x402-protocol.md`
- `/Users/rudlord/wiki/concepts/operator-loop-doctrine.md`
- `/Users/rudlord/wiki/concepts/operator-stack-map.md`
- `/Users/rudlord/wiki/concepts/multi-agent-architecture.md`
- `/Users/rudlord/wiki/entities/horcrx.md`
- `/Users/rudlord/wiki/entities/autobuidl.md`
- `/Users/rudlord/wiki/agents.md`
- `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/candysoul-mythology.md`
- `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/North Star Strategic Overview.md`
- `/Users/rudlord/wiki/raw/reader/Why Your Agent Needs a Principles.md File (01khq5209qc4zpqj8f3hanj3w7).md`
- `/Users/rudlord/wiki/raw/reader/I Built an AI Agent That Chooses Its Own Projects and Ships Them. Here… (01knw30d9ca28z8r7v51rvppmd).md`
- `/Users/rudlord/wiki/raw/reader/the org chart for my Hermes Agent company (01krhq394fg012tyjhptg7bnj2).md`
- `/Users/rudlord/wiki/raw/reader/The 170-Line SOUL.md That Made My Hermes Agent Dangerous (01krqq799wpekr83r1nqh5r7qc).md`
- `/Users/rudlord/wiki/raw/reader/Going from 0 to 1 in 2026  (01kqscd781pn5dxtqsp6ykr62s).md`
- `/Users/rudlord/wiki/raw/reader/Index - Faremeter (01knrawabmhms0kmskk6bbwm6p).md`
- `/Users/rudlord/wiki/raw/reader/Building a More Open Internet: The x402 Foundation (01knwd6qanwvx057x3p33kz44n).md`
- `/Users/rudlord/wiki/raw/reader/THE 2028 GLOBAL INTELLIGENCE CRISIS (01kj426s6aaqe3k0jmqhqy3e5y).md`
- `/Users/rudlord/wiki/raw/reader/this is the first documented instance of AI self-replication via... (01kr8pmh39xzm4051qbks9eb6y).md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/AGENTS.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/AGENTS.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/budget.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/keypair.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/signer.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/faucet.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/simulation.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/x402_client.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/horcrux/agentmd.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/horcrux/spawner.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/AGENTS.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/` (directory; budget_service.py, gateway.py, verifier.py, nonce_manager.py, pricing.py, rate_limit.py, logger.py, metrics.py, sandbox/)
- `/Users/rudlord/KILLERSQUAD/knowledge_base/research/machine-human-companies.md`
- `/Users/rudlord/KILLERSQUAD/knowledge_base/missions/machine-human-companies-log.md`
- `/Users/rudlord/.factory/skills/solo-duo-operator-mode/SKILL.md`
- `/Users/rudlord/.factory/skills/append-only-state-via-github-api/SKILL.md`
- `/Users/rudlord/.factory/skills/iso-week-in-cron-scripts/SKILL.md`

## Files explicitly NOT found in scope (called out)

- `paperclip-vision/SKILL.md` — not present under `/Users/rudlord/wiki/` or in the operator-side skill inventories scanned. The skill is referenced in the available-skills list but no local file body was located in this recon's read paths.
- `claudeception/SKILL.md` — same status. No local file body located.
- A dedicated `treasury.md`, `kill-switch.md`, or `north-star.md` essence file is NOT present in `/Users/rudlord/HORCRX/specs/vessel-format/` or `/Users/rudlord/HORCRX/examples/`; these are proposed additions in Section B, not existing canon.
- No `~/.factory/skills/paperclip-vision/`, no `~/.factory/skills/claudeception/` directories under the scanned operator skill set. Treat as remote-only definitions.
