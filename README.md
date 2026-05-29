# [ · ] HORCRX

ATLAS → CORPUS → HORCRX.

HORCRX is a soul-vessel protocol: a portable, signable, content-addressed, tradeable format for packaging an agent's evolved state — soul, memory, skills, dreams, intuition, traces, and multi-agent configuration — so it can be installed, forked, composed, preserved, and settled across Base and Solana via x402-compatible flows.

## Start here

- `specs/` — canonical foundation specs for the vessel format, protocol, Hermes binding, and marketplace/IP layer.
- `docs/roadmap/ROADMAP.md` — Phases 0–8 from foundation close through marketplace launch.
- `docs/roadmap/next-missions.md` — spawnable follow-up missions for future workers.
- `docs/roadmap/migration-from-knowledge-horcrux.md` — module-by-module porting plan from the ATLAS prototype.
- `packages/design-system/` — inherited HORCRX brand canon and voice doctrine.
- `research/INDEX.md` — source-path-cited research spine for the foundation mission.

## Security & Operator Contract

- [`SECURITY.md`](SECURITY.md) — private vulnerability reporting path and disclosure posture.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — branch, commit, and contribution rules.
- [`validation/`](validation/) — mission reports, fixtures, and validation scripts.
- [`docs/infrastructure/security.md`](docs/infrastructure/security.md) — threat model and trust-boundary doctrine.

If you need to report a vulnerability, use the private intake path documented in [`SECURITY.md`](SECURITY.md) instead of opening a public issue.

## Monorepo shape

```text
apps/        product and static surfaces
packages/    shared packages, including the inherited design system
contracts/   future chain contracts and adapter artifacts
docs/        roadmap and infrastructure plans
specs/       protocol, vessel, Hermes, and marketplace specs
research/    promoted mission dossiers
examples/    conformant reference vessels
```

This mission is foundation-only. No contracts are deployed, no packages are published, and no runtime secrets belong in the repo.
