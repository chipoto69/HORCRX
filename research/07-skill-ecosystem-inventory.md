# 07 — Skill Ecosystem Inventory

HORCRX has to coexist with a real, already-messy skill ecosystem. The practical lesson from the local stack is that distribution is fragmented, but the core skill packet format is already converging.

## Mandatory six surfaces

| Surface | Path | Dominant format | Inventory signal |
|---|---|---|---|
| `.agents` | `/Users/rudlord/.agents/skills/` | `SKILL.md` with YAML frontmatter | largest canonical skill corpus |
| `.claude` | `/Users/rudlord/.claude/skills/` | `SKILL.md` and subagent markdown | mirror and host-specific overlays |
| `.factory` | `/Users/rudlord/.factory/skills/` and `/Users/rudlord/.factory/droids/` | `SKILL.md` plus droid manifests | worker-facing automation surface |
| `.codex` | `/Users/rudlord/.codex/skills/` and `/Users/rudlord/.codex/agents/` | `SKILL.md` plus `.toml` sidecars | strongest dual-manifest pattern |
| `.openclaw` | `/Users/rudlord/.openclaw/skills/` | `SKILL.md` | small but important registry-style surface |
| `.hermes` | `/Users/rudlord/.hermes/skills/` and `/Users/rudlord/.hermes/profiles/` | `SKILL.md`, profile-local skills, and runtime config | day-one runtime compatibility target |

## Packaging patterns that recur

1. **Canonical then mirror** — one skill directory is authoritative and other hosts symlink to it.
2. **Folder over single file** — references, scripts, templates, and assets often live beside `SKILL.md`.
3. **Profile-local overlays** — Hermes profiles keep their own skill cache in addition to shared global skills.
4. **Host-specific companion config** — Codex adds `.toml`; Hermes adds `config.yaml`; some hosts declare install recipes.
5. **Drift detection without signing** — `.skill-lock.json` already carries content hashes but not signed provenance.

## Manifest taxonomy

| Manifest type | Where it appears | What HORCRX should do |
|---|---|---|
| Anthropic-style `SKILL.md` | `.agents`, `.claude`, `.factory`, `.openclaw`, `.hermes` | adopt as the canonical inner skill format |
| Extended `SKILL.md` with install metadata | printing-press style surfaces | preserve extra metadata rather than flattening it away |
| Factory droid manifest | `.factory/droids/` | treat as a specialized runtime wrapper, not a replacement for `SKILL.md` |
| Codex dual file (`.md` + `.toml`) | `.codex/agents/` | support a transpiler or companion file slot in the vessel manifest |
| ORBEL `SOUL.md` + `AGENTS.md` pair | `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/` | use for full-vessel or multi-vessel bundles |

## What HORCRX must normalize

- globally unique skill identity rather than host-local naming collisions,
- consistent dependency declaration,
- signed provenance for installed skill packets,
- clear separation between reusable skill artifacts and runtime-local state,
- a policy for symlinks when exporting and importing vessels.

## Source paths

- `/Users/rudlord/.agents/skills/`
- `/Users/rudlord/.claude/skills/`
- `/Users/rudlord/.factory/skills/`
- `/Users/rudlord/.codex/skills/`
- `/Users/rudlord/.openclaw/skills/`
- `/Users/rudlord/.hermes/skills/`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-B-skill-ecosystem.md`
