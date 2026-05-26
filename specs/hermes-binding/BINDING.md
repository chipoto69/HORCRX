# HORCRX Hermes Binding Contract

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

This document defines the binding between a Hermes profile and a HORCRX vessel. It is the load-bearing compatibility surface for first-party HORCRX adoption because Hermes is the operator's production runtime and the first runtime HORCRX must round-trip without ambiguity.

> **Non-modification guarantee:** HORCRX does NOT modify any existing Hermes profile or fork. Export reads from an existing profile. Import materializes a new profile. Grafts append or namespace imported material without rewriting host doctrine in place. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`.

## 1. Hermes runtime in five facts

1. **Hermes is a single-class agent runtime.** The core execution loop is centered on `AIAgent` in `/Users/rudlord/.hermes/hermes-agent/run_agent.py`, which remains the compatibility anchor for CLI, gateway, batch, and IDE flows. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.hermes/hermes-agent/run_agent.py`.
2. **A profile is a complete isolated agent identity on disk.** The canonical home is `~/.hermes/profiles/<name>/`, with its own `SOUL.md`, optional `AGENTS.md`, `config.yaml`, `skills/`, `memories/`, `sessions/`, `cron/`, `state.db`, `home/`, and `logs/`. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.hermes/profiles/factory-swarm/`, `/Users/rudlord/.hermes/profiles/hermes-content-os/`, `/Users/rudlord/.hermes/profiles/github-steward/`.
3. **Memory is layered.** Hermes splits memory across markdown canon (`memories/MEMORY.md`, `memories/USER.md`), SQLite stores (`state.db` and related files), and one active external provider, with Honcho and GBrain called out as distinct boundaries in operator doctrine. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.hermes/config.yaml`, `/Users/rudlord/.hermes/honcho.json`, `/Users/rudlord/.hermes/hermes-agent/AGENTS.md`.
4. **Skills are progressive-disclosure procedural memory.** The packet format is Anthropic-style `SKILL.md` with YAML frontmatter, discovered from Hermes-global, profile-local, and external directories. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.hermes/hermes-agent/AGENTS.md`, `/Users/rudlord/.hermes/skills/kanban-task.md`.
5. **Dispatch is auditable and budgeted.** Operator doctrine requires `dispatch()`-mediated logging to profile-scoped NDJSON and SQLite audit sinks, and Hermes retains an explicit iteration-budget surface for the parent/subagent loop. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`, `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`, `/Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py`.

## 2. Canonical Hermes profile shape

The profile directory shape is canonical. HORCRX export and import preserve that shape rather than inventing a parallel runtime layout.

```text
~/.hermes/profiles/<name>/
├── SOUL.md
├── AGENTS.md
├── config.yaml
├── .env
├── auth.json
├── auth.lock
├── memories/
│   ├── MEMORY.md
│   ├── USER.md
│   └── *.lock
├── skills/
│   ├── .bundled_manifest
│   ├── .curator_state
│   ├── .curator_backups/
│   ├── .hub/
│   ├── .usage.json
│   └── <category>/<skill>/SKILL.md
├── sessions/
├── state.db
├── state.db-shm
├── state.db-wal
├── cron/
│   ├── jobs.json
│   ├── .tick.lock
│   └── output/<id>/
├── home/
├── logs/
│   ├── agent.log
│   ├── errors.log
│   ├── gateway.log
│   ├── gateway.error.log
│   ├── hermes-audit.ndjson
│   └── curator/
├── state/
│   └── audit.sqlite
├── lsp/
├── hooks/
├── image_cache/
├── audio_cache/
├── pairing/
├── sandboxes/
├── plugins/
├── bin/
├── scripts/
├── dashboards/
├── .skills_prompt_snapshot.json
├── .hermes_history
├── channel_directory.json
├── gateway.lock
├── gateway.pid
├── gateway_state.json
├── processes.json
├── context_length_cache.yaml
├── honcho.json
└── interrupt_debug.log
```

Required minimum in practice: `SOUL.md` plus `config.yaml`. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.hermes/profiles/factory-swarm/`, `/Users/rudlord/.hermes/profiles/hermes-content-os/`, `/Users/rudlord/.hermes/profiles/github-steward/`, `/Users/rudlord/.hermes/profiles/orbel-orchestrator/`.

## 3. Five-pillar pattern and HORCRX slot mapping

HORCRX preserves the existing Hermes five-pillar pattern and adds a first-class vessel mapping for each surface.

| Pillar | Hermes meaning | Local surface | HORCRX vessel slot |
|---|---|---|---|
| SOUL | identity, tone, voice, rules | `<profile>/SOUL.md` | `vessel.soul` |
| MEMORY | markdown canon, SQLite stores, one active external provider | `<profile>/memories/`, `state.db`, configured provider | `vessel.memory` with explicit portable/ephemeral split |
| SKILLS | procedural memory, progressive disclosure | `<profile>/skills/` plus external skill dirs | `vessel.skills` |
| CRONS | scheduled work policy and outputs | `<profile>/cron/jobs.json` | `vessel.crons` |
| LOOP | self-improving operating policy over the other pillars | config + audit + curator + optional GEPA surfaces | `vessel.loop_policy` |

`AGENTS.md` remains the operational companion, not a sixth pillar. HORCRX inherits the ORBEL doctrine that `SOUL.md` is identity only while `AGENTS.md` carries workflows, commands, paths, and project rules. Sources: `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`, `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`.

## 4. The Hermes ↔ HORCRX binding contract

### 4.1 Export path

```bash
hermes profile export --as-vessel <name>
```

Normative export behavior:

- read the existing profile at `~/.hermes/profiles/<name>/`;
- serialize `SOUL.md` verbatim into `vessel.soul`;
- serialize `AGENTS.md` into `vessel.agents` when present;
- serialize `config.yaml` into `vessel.config` after stripping secrets and host-bound credentials;
- serialize skills as content-addressed packets without changing the `SKILL.md` format;
- serialize portable memory canon and cron policy;
- compute lineage metadata and sign the vessel manifest;
- strip secrets, auth material, live caches, locks, and host-local runtime surfaces before bundle assembly.

Exact include/strip rules live in `strip-and-rehydrate.md`. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`, `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`.

### 4.2 Import path

```bash
horcrx install <cid-or-path> [--as-profile <name>] [--strategy keep-host|prefer-vessel|namespace]
```

Normative import behavior:

1. verify the manifest signature and parent lineage;
2. materialize a **new** profile directory under `~/.hermes/profiles/<name>/`;
3. write `SOUL.md`, `AGENTS.md`, redacted `config.yaml`, portable memory, skills, and cron policy into the new profile;
4. re-inject host-supplied credentials from shell environment, secret manager, or operator-approved host bindings;
5. leave imported cron jobs disabled until the operator re-enables them;
6. run a compatibility smoke check after materialization.

`namespace` is the default conflict strategy because it preserves host state, imported state, and provenance at the same time. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`.

### 4.3 Composition path

```bash
horcrx graft <cid> --slot skills --into <profile>
horcrx graft <cid> --slot soul-overlay --into <profile>
horcrx graft <cid> --slot memory-pack --into <profile>
```

Normative graft behavior:

- `skills` grafts land under a namespaced subtree such as `skills/vessel-<cid>/...`;
- `soul-overlay` appends an explicit overlay section rather than rewriting the host `SOUL.md`;
- `memory-pack` creates sidecars under a graft surface rather than mutating canonical host memory in place.

Grafts are additive. They do not rewrite or fork an existing host profile. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`, `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`.

### 4.4 Provenance and royalties

Every install or graft writes provenance rows to:

```text
<profile>/state/vessel-lineage.sqlite
```

Minimum schema:

| Column | Type | Meaning |
|---|---|---|
| `installed_at` | `TEXT` | ISO8601 UTC install or graft time |
| `profile_name` | `TEXT` | target Hermes profile |
| `vessel_cid` | `TEXT` | installed or grafted vessel manifest CID |
| `parent_cids_json` | `TEXT` | JSON array of parent lineage CIDs |
| `slot` | `TEXT` | `full-install`, `skills`, `soul-overlay`, or `memory-pack` |
| `author_keys_json` | `TEXT` | JSON array of author signing keys |
| `royalty_target` | `TEXT` | royalty recipient target from the manifest |
| `signed_manifest_cid` | `TEXT` | signed manifest CID actually installed |
| `strategy` | `TEXT` | conflict strategy used at install or graft |

Hermes audit rows emitted by vessel-installed or vessel-grafted material MUST also carry `vessel_cid` so downstream marketplace or royalty accounting can attribute execution to a lineage path without mutating Hermes' base audit requirement. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`, `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`.

### 4.5 Hermes as marketplace client

Hermes consumes the marketplace as a client, not as the canonical registry.

Required integration surfaces:

- a `vessel-marketplace` skill at `~/.hermes/skills/vessel-marketplace/SKILL.md`;
- an MCP server entry named `horcrx-marketplace`;
- read-only actions such as `search`, `browse`, `view`, and `preview`;
- purchase/install flows that route through Hermes approvals and `dispatch()` audit logging.

The marketplace client path must preserve operator approval for irreversible purchases and installs. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`.

## 5. ORBEL-as-vessel-bundle pattern

ORBEL already demonstrates the local shape of a multi-vessel pack:

- one role per profile;
- one `SOUL.md` plus one `AGENTS.md` per role;
- explicit task graph and artifact contracts;
- live materializations under `~/.hermes/profiles/orbel-*`.

That makes ORBEL the reference bundle pattern for `HORCRX #002 · orbel-pack`. The missing pieces are the signed HORCRX manifest, content-addressing, and marketplace listing. Sources: `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`.

## 6. Five named reference profiles

The local Hermes stack already contains the five profiles the binding should treat as reference vessels:

1. **factory-swarm** — orchestrator doctrine and layered identity surface. Sources: `/Users/rudlord/.hermes/profiles/factory-swarm/`, `/Users/rudlord/.hermes/profiles/factory-swarm/SOUL.md`.
2. **hermes-content-os** — narrow-lane steward profile with the clearest audit and auth doctrine. Sources: `/Users/rudlord/.hermes/profiles/hermes-content-os/`, `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`, `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`.
3. **github-steward** — autopilot and Git/GitHub operations reference. Sources: `/Users/rudlord/.hermes/profiles/github-steward/`, `/Users/rudlord/.hermes/profiles/github-steward/SOUL.md`.
4. **orbel-orchestrator** — the cleanest local SOUL/AGENTS split. Sources: `/Users/rudlord/.hermes/profiles/orbel-orchestrator/`, `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md`, `/Users/rudlord/.hermes/profiles/orbel-orchestrator/AGENTS.md`.
5. **factory-codex or coder** — implementation-lane reference for builder-style vessels. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.hermes/profiles/coder/`.

## 7. Open questions are resolved as ADRs

The ten open binding questions from the Hermes recon are resolved in:

- `/Users/rudlord/HORCRX/specs/hermes-binding/open-questions-resolved.md`

Until operator sign-off is captured, each ADR is marked `accepted-pending-HITL`. That keeps the contract concrete enough for downstream workers without pretending approval already happened. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/mission.md`.

## 8. Hard constraints (verbatim, locked)

These fourteen constraints are copied verbatim from the Hermes binding recon and are non-negotiable for HORCRX compatibility.

| Verbatim constraint | Citation paths |
|---|---|
| **Secret injection via shell env, not `.env`** — LLM provider keys (`OPENAI_API_KEY`, etc.) live in shell env; profile `.env` carries only service tokens. | `~/wiki/_meta/hermes-stack/hermes-content-os.md:Auth policy`; `~/.hermes/profiles/hermes-content-os/SOUL.md:Operator Setup — LLM Keys` |
| **`dispatch()` audit requirement** — every LLM call writes NDJSON+SQLite row. Direct `litellm`/`anthropic`/`openai` imports forbidden. | `~/.hermes/profiles/hermes-content-os/SOUL.md:Audit Contract`; `~/.hermes/profiles/hermes-content-os/state/audit.sqlite` |
| **Profile directory shape** is canonical (see §2). | `~/.hermes/profiles/factory-swarm/`, `hermes-content-os/`, `github-steward/` |
| **Skill manifest format** is Anthropic SKILL.md w/ YAML frontmatter. | `~/.hermes/skills/kanban-task.md:1-13`; `~/.hermes/hermes-agent/AGENTS.md:Skills` |
| **Honcho/GBrain memory boundary** — Honcho per-profile peer; GBrain shared durable memory via MCP; Tier 1 markdown + Tier 2 SQLite FTS5 in profile. | `~/.hermes/honcho.json`; `~/.hermes/config.yaml:gbrain`, `:honcho` |
| **Kanban as task substrate** — `~/.hermes/kanban.db` SQLite (3.1 MB multi-board). Every meaningful action gets a card + comments + 5m heartbeat. | `~/.hermes/skills/kanban-task.md`; `~/.hermes/kanban.db` |
| **Session log retention** — `sessions/` retained per profile; `state.db` is FTS5 index. `~/.hermes/config.yaml:sessions.retention_days: 90`. | `~/.hermes/config.yaml:sessions` |
| **Shell-env LLM keys path** — resolved at dispatch time from shell env; `~/.config/wiki-ingest/.env` does NOT exist. | `~/wiki/_meta/hermes-stack/hermes-content-os.md:Auth policy` |
| **SOUL/AGENTS split** — SOUL.md identity only; commands/paths/workflows go in AGENTS.md or skills/config/Kanban. | `~/wiki/_meta/orbel-framework/profile-templates/README.md`; `~/.hermes/profiles/orbel-orchestrator/SOUL.md` |
| **`~/.hermes/config.yaml` (root) is read-only** for per-profile work; overrides only via `<profile>/config.yaml`. | `~/.hermes/profiles/hermes-content-os/SOUL.md:Profile Isolation`; `:Off-Limits` |
| **GATE-01..08 for canon writes** — any vessel touching `~/wiki/` canon MUST go through wiki-ingest gates; never direct write. | `~/wiki/_meta/commit-standards.md`; `~/.hermes/profiles/hermes-content-os/SOUL.md:Writeback Split` |
| **Iteration budget shared with subagents** — `agent.max_turns` capped; subagents share budget. | `~/.hermes/hermes-agent/agent/iteration_budget.py`; `~/.hermes/hermes-agent/AGENTS.md:Agent Loop` |
| **Three-tier memory; Tier 3 single-provider-active** — only one external provider active at a time (Honcho is operator's choice). | `~/.hermes/hermes-agent/AGENTS.md:Memory-provider plugins` |
| **Curator never deletes; archives only** with pre-pass tarball snapshot. | `~/wiki/raw/reader/Hermes Agent Masterclass*.md`; `~/.hermes/skills/.curator_backups/` |

HORCRX export, import, graft, and marketplace behavior MUST preserve all fourteen constraints. Sources: `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`.

## 9. Cross-check against the vessel format spec

The current vessel format spec is compatible with this binding contract:

| Vessel spec surface | Hermes binding result |
|---|---|
| `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md` declares the vessel as a strict superset of Hermes profile shape. | Compatible with §2 because import/export keeps Hermes as the runtime directory model. |
| `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md` splits portable canon, ephemeral session memory, and host-bound secrets. | Compatible with §4 and the strip/rehydrate rules; no raw `state.db`, `sessions/`, or credentials are required to travel by default. |
| The vessel spec preserves `soul.md` and `agents.md` as separate surfaces. | Compatible with the SOUL/AGENTS split constraint. |
| The vessel spec keeps Anthropic-compatible `SKILL.md` packets unchanged. | Compatible with the skill manifest constraint. |
| The vessel spec requires host-side secret rehydration and deterministic bundle assembly. | Compatible with shell-env key injection and the non-modification guarantee. |

No current vessel-format decision in `/Users/rudlord/HORCRX/specs/vessel-format/` requires HORCRX to violate a Hermes hard constraint. Cross-check sources: `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`, `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`, `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`.

## Source paths

- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
- `/Users/rudlord/.hermes/config.yaml`
- `/Users/rudlord/.hermes/honcho.json`
- `/Users/rudlord/.hermes/hermes-agent/AGENTS.md`
- `/Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py`
- `/Users/rudlord/.hermes/profiles/factory-swarm/`
- `/Users/rudlord/.hermes/profiles/factory-swarm/SOUL.md`
- `/Users/rudlord/.hermes/profiles/github-steward/`
- `/Users/rudlord/.hermes/profiles/github-steward/SOUL.md`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`
- `/Users/rudlord/.hermes/profiles/orbel-orchestrator/`
- `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md`
- `/Users/rudlord/.hermes/skills/kanban-task.md`
- `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
