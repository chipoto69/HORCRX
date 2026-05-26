# Registry design

Version: `v0.1-draft`

HORCRX splits registry responsibilities between a minimal on-chain pointer layer and a richer off-chain content/index layer.

## 1. On-chain responsibilities

The on-chain registry stores only what benefits from chain-level consensus:

- the vessel or pack identifier,
- the active manifest content hash or CID pointer,
- current owner reference,
- royalty configuration pointer,
- revocation or status flags,
- optional collection or adapter metadata.

This keeps the chain layer small and auditable.

## 2. Off-chain responsibilities

The off-chain registry stores the heavier discovery and retrieval surface:

- content fetch locations,
- manifest bodies,
- slot metadata,
- skill and capability indexes,
- review signals,
- search documents,
- provenance mirrors.

The default storage posture is:

- hot-path content via **IPFS**-style content addressing,
- archival or permanence via **Arweave/Irys**,
- query and ranking via a local or hosted index such as SQLite or Postgres.

## 3. Why the split exists

- ownership changes need consensus;
- content retrieval needs low-cost indexing and caching;
- market search needs richer metadata than most chains should hold;
- revocation should be visible on-chain without duplicating every slot body.

## 4. Source paths

- `/Users/rudlord/HORCRX/research/02-prior-art.md`
- `/Users/rudlord/HORCRX/research/03-competitive-positioning.md`
- `/Users/rudlord/HORCRX/research/06-local-modules-inventory.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/`
