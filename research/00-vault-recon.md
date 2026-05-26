# 00 — Vault Recon

This dossier was built from the mission library first, then spot-checked against the live local source surfaces those dossiers cite. The goal was promotion, not re-mining. Every major claim below points back to a local source path.

## What was mined

| Surface | What it contributed | Source paths |
|---|---|---|
| Local codebases | Existing HORCRX prototype, x402 implementation, AgentCard schema, marketplace modules, and SDK paths | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-A-local-codebases.md` |
| Skill ecosystem | Real manifest formats, symlink patterns, and the six mandatory skill surfaces | `/Users/rudlord/.agents/skills/`, `/Users/rudlord/.claude/skills/`, `/Users/rudlord/.factory/skills/`, `/Users/rudlord/.codex/skills/`, `/Users/rudlord/.openclaw/skills/`, `/Users/rudlord/.hermes/skills/`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-B-skill-ecosystem.md` |
| Wiki canon | The economic, doctrinal, and payment-layer context already present in the operator vault | `/Users/rudlord/wiki/concepts/x402-protocol.md`, `/Users/rudlord/wiki/concepts/agent-memory-infrastructure.md`, `/Users/rudlord/wiki/raw/reader/Building a More Open Internet: The x402 Foundation (01knwd6qanwvx057x3p33kz44n).md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md` |
| External prior art | The standards landscape, starred repositories, and the existing drafted prior-art survey | `/tmp/horcrx-research/02-prior-art.md`, `/tmp/horcrx-research/starred.json`, `/tmp/horcrx-research/own-repos.json`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md` |
| Knowledge graph context | The 89K-line wiki graph, ORBEL schemas, topic_key gaps, and Honcho synthesis conventions | `/Users/rudlord/wiki/.understand-anything/knowledge-graph.json`, `/Users/rudlord/wiki/_meta/orbel-framework/schemas/orbel-artifact-contracts.yaml`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-E-knowledge-graph.md` |
| Hermes runtime | The concrete export/import boundary HORCRX must respect to remain useful on day one | `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`, `/Users/rudlord/.hermes/skills/kanban-task.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md` |
| Brand layer | The already-finished HORCRX identity surface and the first vessel naming convention | `/Users/rudlord/HORCRX/HORCRX_Design_System/README.md`, `/Users/rudlord/HORCRX/HORCRX_Design_System/VOICE.md` |

## What recon says, in plain terms

1. HORCRX is not starting from zero. A full prototype already exists at `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/` with x402, marketplace, identity, wallet, and SDK surfaces already shaped.
2. Hermes is the only runtime in the stack with enough operational mass to make the first vessel format worth shipping. The five-pillar profile structure described in `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md` is the load-bearing compatibility target.
3. The skill layer is already fragmented across multiple hosts, but the dominant procedural-memory format is still Anthropic-style `SKILL.md` with YAML frontmatter, as documented in `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-B-skill-ecosystem.md`.
4. The vault already contains the missing market and doctrine context: x402, agentic.market, Story Protocol, ORBEL, agent-memory discipline, and the mind-vs-secrets trust split are all already present in `/Users/rudlord/wiki/`.
5. The research gap is not conceptual ambition. The gap is canonical packaging: one signed, portable, content-addressed vessel artifact that can carry soul, skills, memory, traces, and market lineage together.

## What was intentionally not re-mined

- The full wiki corpus was not re-read end to end; promotion relied on `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md` and `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-E-knowledge-graph.md`.
- Hermes internals were not modified or exhaustively re-audited; this dossier promotes the runtime map already condensed in `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`.
- No new external web reconnaissance was needed because `/tmp/horcrx-research/02-prior-art.md` and the library dossiers already captured the relevant May 2026 standards surface.

## Evidence backbone

- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`
- `/Users/rudlord/wiki/concepts/x402-protocol.md`
- `/Users/rudlord/wiki/concepts/agent-memory-infrastructure.md`
- `/Users/rudlord/wiki/.understand-anything/knowledge-graph.json`
- `/Users/rudlord/wiki/_meta/orbel-framework/MANIFEST.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`
- `/Users/rudlord/HORCRX/HORCRX_Design_System/README.md`
