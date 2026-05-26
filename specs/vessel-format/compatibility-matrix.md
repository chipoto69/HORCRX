# Compatibility matrix

Version: `v0.1-draft`

The vessel format is broader than any single runtime. This matrix shows how the same slots map into the active local tool surfaces.

| Runtime / surface | `soul.md` | `agents.md` | `skills/` | `memory/` | `traces/` | `crons/jobs.json` | Notes |
|---|---|---|---|---|---|---|---|
| Hermes profile | native file in profile root | native companion contract | native `SKILL.md` discovery | maps to `memories/` + curated canon | maps to audit-friendly export layer | maps to `cron/jobs.json` | primary round-trip target |
| Anthropic Skill | n/a | n/a | native packet format | optional references only | not first-class | n/a | vessel embeds skill packets unchanged |
| MCP server | optional persona overlay | operator policy sidecar | tool discovery only | host-bound by default | trace export can reference tool calls | scheduler external | credentials never ship |
| Claude Code agent | persona/system context source | project contract source | skill folder or prompt includes | importable as context docs | optional audit export | host scheduler | useful as a non-Hermes consumer |
| OpenAI Assistant | assistant instructions analogue | project-side orchestration doc | tool descriptions or file attachments | vector/file import target | exported audit only | external scheduler | no direct 1:1 profile layout |
| Factory droid | role/persona prompt seed | operator/run contract | droid skill packs | contextual memory attachments | mission evidence | external scheduler | runtime wrapper, not vessel replacement |

## Slot-level guidance

- **Hermes profile** is the most exact filesystem mapping.
- **Anthropic Skill** is the canonical inner skill syntax.
- **MCP server** surfaces expectations and tool affordances, not secrets.
- **Claude Code agent** and **Factory droid** consume the vessel as structured context, not as a filesystem profile.
- **OpenAI Assistant** maps imperfectly, so only higher-level slots port cleanly.

## Local source paths

- `/Users/rudlord/HORCRX/research/07-skill-ecosystem-inventory.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/.factory/droids/`
- `/Users/rudlord/.hermes/skills/`
- `/Users/rudlord/.agents/skills/`
