# 09 — Hermes Binding Recon

This file intentionally stays close to the raw research shape. F03 will promote it into `specs/hermes-binding/`, but this dossier preserves the reconnaissance layer that later spec decisions should cite.

## 1. Hermes runtime in five facts

1. Hermes is a single-class agent runtime centered on `AIAgent` in `/Users/rudlord/.hermes/hermes-agent/run_agent.py`.
2. A profile is an isolated agent home under `/Users/rudlord/.hermes/profiles/<name>/`.
3. Memory is layered across markdown canon, SQLite, and one active external provider.
4. Skills are progressive-disclosure procedural memory, dominated by Anthropic-style `SKILL.md`.
5. `dispatch()` is auditable and budgeted; it is not optional in the local doctrine.

## 2. Canonical profile shape

```text
/Users/rudlord/.hermes/profiles/<name>/
├── SOUL.md
├── AGENTS.md
├── config.yaml
├── .env
├── auth.json
├── memories/
├── skills/
├── sessions/
├── state.db
├── cron/jobs.json
├── home/
├── logs/
├── state/audit.sqlite
└── caches, hooks, plugins, dashboards, and runtime sidecars
```

Required minimum in practice: `SOUL.md` plus `config.yaml`. Everything else can be materialized later, but the directory shape itself is canonical. Sources: `/Users/rudlord/.hermes/profiles/factory-swarm/`, `/Users/rudlord/.hermes/profiles/hermes-content-os/`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`.

## 3. Five-pillar mapping

| Pillar | Local Hermes meaning | HORCRX implication |
|---|---|---|
| SOUL | identity, voice, rules | signed `soul.md` slot |
| MEMORY | markdown canon + SQLite + provider | explicit export split between portable and ephemeral memory |
| SKILLS | progressive disclosure procedures | keep `SKILL.md` unchanged inside the vessel |
| CRONS | scheduled work | exportable policy plus disabled-by-default install |
| LOOP | self-improving policy around the other pillars | explicit loop policy slot instead of invisible runtime magic |

`AGENTS.md` remains the operational-contract companion and should stay separate from SOUL in every example.

## 4. Proposed export, import, and graft semantics

### Export path
`hermes profile export --as-vessel <name>` should serialize `SOUL.md`, `AGENTS.md`, redacted `config.yaml`, skills, memory canon, cron policy, and lineage metadata while stripping secrets, auth material, raw caches, and runtime locks.

### Import path
`horcrx install <cid-or-path>` should verify signatures, materialize a fresh profile, re-inject host secrets from the host environment, and leave imported crons disabled by default.

### Composition path
`horcrx graft <cid> --slot {skills|soul-overlay|memory-pack}` should support partial adoption without requiring full-profile replacement.

## 5. ORBEL-as-pack evidence

The ORBEL template set at `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/` already behaves like a five-vessel pack in spirit: one role per profile, a strict SOUL/AGENTS split, and typed artifact contracts. That makes ORBEL the strongest local reference for a multi-vessel bundle.

## 6. Open questions that F03 must resolve

1. session-memory mobility,
2. `state.db` inclusion policy,
3. MCP credential rehydration,
4. cron deliverability rebinding,
5. kanban substrate export policy,
6. curator-policy graft behavior,
7. GEPA history portability,
8. `home/` recreation rules,
9. plugin dependency packaging,
10. iteration-budget recommendation vs host enforcement.

## 7. Hard constraints

| Hard constraint | Why it is non-negotiable | Citation path |
|---|---|---|
| Secret injection via shell env, not `.env` | prevents shipping LLM keys inside vessel artifacts | `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`, `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` |
| `dispatch()` audit requirement | every LLM call must leave an auditable trail | `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`, `/Users/rudlord/.hermes/profiles/hermes-content-os/state/audit.sqlite` |
| Profile directory shape is canonical | import/export must round-trip without inventing a new runtime layout | `/Users/rudlord/.hermes/profiles/factory-swarm/`, `/Users/rudlord/.hermes/profiles/hermes-content-os/` |
| Skill manifest format is Anthropic `SKILL.md` with YAML frontmatter | changing the packet format would break the active skill ecosystem | `/Users/rudlord/.hermes/skills/kanban-task.md`, `/Users/rudlord/.hermes/hermes-agent/AGENTS.md` |
| Honcho/GBrain memory boundary | per-profile memory and shared memory stay distinct | `/Users/rudlord/.hermes/honcho.json`, `/Users/rudlord/.hermes/config.yaml` |
| Kanban as task substrate | meaningful work is already expected to land in Kanban | `/Users/rudlord/.hermes/skills/kanban-task.md`, `/Users/rudlord/.hermes/kanban.db` |
| Session log retention | runtime history is intentionally retained and indexed | `/Users/rudlord/.hermes/config.yaml` |
| Shell-env LLM keys path | runtime model keys are resolved at dispatch time, not persisted locally | `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md` |
| SOUL/AGENTS split | identity stays out of operational instructions | `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`, `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md` |
| `/Users/rudlord/.hermes/config.yaml` is read-only for profile work | per-profile overrides belong in profile-local config | `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` |
| GATE-01..08 for canon writes | any vault-touching vessel must respect the existing writeback gates | `/Users/rudlord/wiki/_meta/commit-standards.md`, `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md` |
| Iteration budget shared with subagents | subagents cannot bypass the host loop budget | `/Users/rudlord/.hermes/hermes-agent/agent/iteration_budget.py`, `/Users/rudlord/.hermes/hermes-agent/AGENTS.md` |
| Three-tier memory; Tier 3 single-provider-active | the runtime already assumes one active external provider at a time | `/Users/rudlord/.hermes/hermes-agent/AGENTS.md`, `/Users/rudlord/.hermes/honcho.json` |
| Curator never deletes; archives only | skill evolution is reversible by policy | `/Users/rudlord/wiki/raw/reader/Hermes Agent Masterclass (01ksj3wrnkp4gr67mg0106p6m8).md`, `/Users/rudlord/.hermes/skills/.curator_backups/` |

## Source paths

- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`
- `/Users/rudlord/.hermes/profiles/orbel-orchestrator/SOUL.md`
- `/Users/rudlord/.hermes/skills/kanban-task.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
- `/Users/rudlord/wiki/raw/reader/Hermes Agent Masterclass (01ksj3wrnkp4gr67mg0106p6m8).md`
