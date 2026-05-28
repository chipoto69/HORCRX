# Changelog

All notable changes to HORCRX are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- HORCRX vessel #003 · founder (`examples/horcrx-003-founder/`) — first money-aware reference vessel.
- New spec slots: `mission.md`, `ledger.md`, `autonomy.md`, `constraints.md` (optional) with schemas under `specs/vessel-format/`.
- Promoted `voice.md` to a required identity slot for all vessels.
- Founder-vessel binding section in `specs/hermes-binding/BINDING.md` (§10).
- Open-question resolutions OQ-12..OQ-19 in `specs/hermes-binding/open-questions-resolved.md`.

### Changed
- `specs/vessel-format/manifest.schema.json` extended with `kind: "founder"` and the new required slots for that kind.
- `examples/horcrx-001-candysoul/manifest.json` updated to reference the now-required voice slot.

### Operator HITL
- OQ-13 (cap scale), OQ-15 (termination state), OQ-17 (spend-mix ratios), OQ-18 (marketplace allowlist), and the vessel's three-verb mission line remain surfaced for PR review.

## [0.1.1] - 2026-05-27
### Changed
- Bumped `softprops/action-gh-release` from 2 to 3 (#2)
- Bumped `actions/checkout` from 4 to 6 (#3)
- Bumped `actions/setup-node` from 4 to 6 (#4)

## [0.1.0-foundation] - 2026-05-26
### Added
- Initial monorepo scaffold (pnpm + turbo)
- Research dossier in `research/` (10 files, full source-path citations)
- Vessel format specification (folder + signed bundle, manifest JSON Schema)
- Chain-agnostic protocol spec (Base + Solana adapters)
- Hermes binding contract (14 hard constraints locked, 10 ADRs resolved)
- Marketplace + IP preservation architecture
- Infrastructure plan + threat model
- Roadmap Phases 0–8 with spawnable next-mission specs
- Inherited design system as `packages/design-system/` (no redesign)
- GitHub repo with CI (commitlint + schema validation + link check), release workflow, CODEOWNERS, ISSUE/PR templates, dependabot, SECURITY.md
- Two reference vessels: `examples/horcrx-001-candysoul/`, `examples/horcrx-002-orbel-pack/`

### Inherited
- HORCRX_Design_System (brand identity, voice, Departure Mono font, 17 preview cards, landing.html)
- x402 + multi-chain verifier patterns from ATLAS knowledge-horcrux worktree (reference only; no code copied this phase)
- ORBEL artifact contracts and 5-role template (reference only; orbel-pack example vessel inspired by it)

### Known limitations
- Foundation only — no production code, no contracts deployed, no marketplace UI built
- Open binding questions resolved as ADRs but pending operator HITL confirmation on production-bound ones (see `specs/hermes-binding/open-questions-resolved.md`)

[Unreleased]: https://github.com/chipoto69/HORCRX/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/chipoto69/HORCRX/compare/v0.1.0-foundation...v0.1.1
[0.1.0-foundation]: https://github.com/chipoto69/HORCRX/releases/tag/v0.1.0-foundation
