# 06 — Local Modules Inventory

The local stack already contains most of the modules HORCRX needs. The key design task is selection and recomposition, not greenfield reinvention.

## Inheritable modules from `knowledge-horcrux`

| Module | Absolute path | Maturity | Why it is worth inheriting |
|---|---|---|---|
| x402 gateway stack | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/` | working prototype | already has nonce, replay protection, payment proof parsing, pricing, budgets, and transaction recording |
| Multi-chain verifier registry | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/` | mixed: Solana working, Base scaffolded | establishes the adapter seam HORCRX needs for chain symmetry |
| AgentCard and agent registry | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/` | working | preserves the local identity and capability schema that the vessel manifest should extend |
| SAID identity federation | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/` | prototype | relevant for signer identity, federation, and marketplace trust |
| Agent wallet stack | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/wallet/` | prototype | useful for vessel-held payment flows and budget control |
| cNFT reputation | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/reputation/` | prototype | maps directly onto discovery-and-trust requirements |
| Marketplace v2 | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/` | working backend | provides existing market shape and domain vocabulary |
| Marketplace router | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/api/routers/marketplace_v2.py` | working | concrete API behaviors worth preserving conceptually |
| Horcrux entity prototype | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/horcrux/` | minimal but real | proof that the concept already has a code foothold |
| Knowledge-side horcrux dataclass | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/knowledge/` | working prototype | shows how ATLAS currently thinks about a knowledge horcrux |
| Bridge surfaces | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/bridges/` | prototype | important for marketplace and runtime interop |
| Canonical SQL schema | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/core/db/migrations/005_agent_economy.sql` | locked | preserves entity relationships the economic layer already assumes |
| Python SDK | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/sdk/python/atlas_sdk` | working | future import/export and registry helpers can borrow shape |
| TypeScript SDK | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/sdk/typescript/src/` | working | future marketplace and x402 tooling can borrow shape |

## Local supporting modules outside `knowledge-horcrux`

| Surface | Path | Why it matters |
|---|---|---|
| HORCRX design system | `/Users/rudlord/HORCRX/HORCRX_Design_System/` | already defines the mark, typography, and `HORCRX #001 · candysoul` language |
| Hermes profile doctrine | `/Users/rudlord/.hermes/profiles/` | provides the canonical on-disk runtime shape the vessel must round-trip to |
| ORBEL templates | `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/` | direct template for multi-vessel packs and role bundles |
| Spine-worker template | `/Users/rudlord/railway-hermes-worker/hermes-agent-template/` | useful for profile packaging patterns |
| oh-my-hermes | `/Users/rudlord/oh-my-hermes/` | demonstrates persona and skill packaging patterns |
| content-flywheel append-only decisions | `/Users/rudlord/ydefix-content-flywheel/` | useful for provenance and atomic decision logs |

## Reuse posture

- **Reuse directly**: x402 header semantics, agent registry vocabulary, skill packet format, Hermes profile layout.
- **Port carefully**: wallet, reputation, and marketplace logic where chain assumptions are explicit.
- **Do not inherit blindly**: large monolithic files such as marketplace service surfaces should inform domain structure, not dictate repo layout.
- **Treat as greenfield**: `dreams.md`, `intuition.md`, signed `.horcrx` bundle rules, derivative royalty graph, and cross-runtime export contract.

## Source paths

- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/`
- `/Users/rudlord/HORCRX/HORCRX_Design_System/`
- `/Users/rudlord/.hermes/profiles/`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-A-local-codebases.md`
