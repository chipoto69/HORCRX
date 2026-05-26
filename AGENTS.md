<coding_guidelines>
# HORCRX Worker Notes

ATLAS → CORPUS → HORCRX.

## Operator contract

- HORCRX is foundation-first in this repo: specs, roadmaps, examples, and validation evidence only until a later implementation phase explicitly authorizes production code.
- Preserve the SOUL.md / AGENTS.md split. `SOUL.md` is identity and voice only; `AGENTS.md` is the operational contract for paths, commands, workflows, validation, safety gates, and repo rules.
- Voice doctrine lives at `packages/design-system/VOICE.md`. Technical specs stay precise; artistic prose follows the inherited HORCRX voice.
- Brand canon lives in `packages/design-system/`. Preserve inherited design-system files verbatim unless a task explicitly asks for a change.

## Commit format

Use Conventional Commits:

```text
<type>(<scope>): <subject>
```

Allowed types for this repo: `feat`, `fix`, `docs`, `chore`, `build`, `ci`, `refactor`, `test`, `polish`. Keep commits atomic and explain why in the body when needed.

## Branch and push rules

- Default branch: `main`.
- Mission branches use `foundation/<area>`.
- Never push directly to `main`; open a PR after validation.
- Never force-push a shared branch.
- Install hooks with `git config core.hooksPath .githooks` before committing.

## Off-limits

- Do not modify live Hermes profiles or runtime files.
- Do not modify the ATLAS `knowledge-horcrux` source worktree; it is read-only prior art.
- Do not write secrets, API keys, wallet seeds, private keys, or paid-service credentials into this repo.
- Do not deploy contracts, publish packages, or push to any remote unless a future mission explicitly assigns that work.
- Wiki writes are reserved for the dedicated librarian mission and must follow the wiki gate process.
</coding_guidelines>
