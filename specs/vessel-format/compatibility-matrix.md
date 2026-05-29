# Compatibility matrix

Version: `v0.1-draft`

The vessel format is broader than any single runtime. This matrix shows how the same slots map into the active local tool surfaces.

| Runtime / surface | `soul.md` | `agents.md` | `skills/` | `memory/` | `traces/` | `crons/jobs.json` | Notes |
|---|---|---|---|---|---|---|---|
| Hermes profile | native file in profile root | native companion contract | native `SKILL.md` discovery | maps to `memories/` + curated canon | maps to audit-friendly export layer | maps to `cron/jobs.json` | primary round-trip target |
| Anthropic Skill | n/a | n/a | native packet format | optional references only | not first-class; export as adjacent NDJSON evidence artifact when needed | n/a | vessel embeds skill packets unchanged |
| MCP server | optional persona overlay | operator policy sidecar | tool discovery only | host-bound by default | trace export can reference tool calls | scheduler external | credentials never ship |
| Claude Code agent | persona/system context source | project contract source | skill folder or prompt includes | importable as context docs | maps to external session/worker evidence export, not a native trace store | host scheduler | useful as a non-Hermes consumer |
| OpenAI Assistant | assistant instructions analogue | project-side orchestration doc | tool descriptions or file attachments | vector/file import target | exported audit only | external scheduler | no direct 1:1 profile layout |
| Factory droid | role/persona prompt seed | operator/run contract | droid skill packs | contextual memory attachments | mission evidence NDJSON or handoff artifact, not a first-class runtime trace store | external scheduler | runtime wrapper, not vessel replacement |

## Slot-level guidance

- **Hermes profile** is the most exact filesystem mapping.
- **Anthropic Skill** is the canonical inner skill syntax.
- **MCP server** surfaces expectations and tool affordances, not secrets.
- **Claude Code agent** and **Factory droid** consume the vessel as structured context, not as a filesystem profile.
- **OpenAI Assistant** maps imperfectly, so only higher-level slots port cleanly.

## Non-Hermes trace export semantics

- **Anthropic Skill** — traces are not first-class inside the skill packet. Export them as a sibling NDJSON evidence artifact or marketplace attachment, with the skill itself carrying only references.
- **Claude Code agent** — traces map to external session evidence, worker reports, or mission artifacts. The runtime can consume exported NDJSON, but it does not persist vessel traces as a native profile surface.
- **Factory droid** — traces map to mission evidence and end-of-run handoff artifacts. They remain portable as NDJSON exports, but the droid runtime is a wrapper rather than a canonical trace store.

## Local source paths

- `/Users/rudlord/HORCRX/research/07-skill-ecosystem-inventory.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/.factory/droids/`
- `/Users/rudlord/.hermes/skills/`
- `/Users/rudlord/.agents/skills/`
