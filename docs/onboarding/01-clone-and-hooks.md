---
title: Clone and hooks bootstrap
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Clone and hooks bootstrap

Use this checklist when you are setting up a fresh HORCRX worktree.

## 1. Clone the repository

Run from the parent directory where you keep local source checkouts:

```bash
git clone https://github.com/chipoto69/HORCRX.git
cd HORCRX
```

If you are joining an active mission branch instead of `main`, fetch first and then check out the branch your mission packet names.

## 2. Bootstrap the local git hooks

HORCRX expects repo-local hooks from `.githooks/` to be active before your first commit:

```bash
git config --local core.hooksPath .githooks
git config core.hooksPath
```

Expected output:

```text
.githooks
```

Why this matters:

- `commit-msg` rejects non-Conventional-Commit subjects and deny-listed scopes such as `wip`, `tmp`, `temp`, and `fixup`.
- `pre-push` blocks direct pushes to protected refs such as `main`, release branches, and tags.

## 3. Install workspace dependencies

```bash
pnpm install
```

HORCRX is foundation-first, so the dependency surface is intentionally small. A clean install should complete without generating app build artifacts.

## 4. Run the first validator pass

Start with the same baseline the mission workers use:

```bash
pnpm test
npx --yes ajv-cli@5 validate --spec=draft2020 \
  -s specs/vessel-format/manifest.schema.json \
  -d examples/horcrx-001-candysoul/manifest.json \
  -d examples/horcrx-002-orbel-pack/manifest.json \
  -d examples/horcrx-003-founder/manifest.json
```

What good looks like:

- `pnpm test` prints `schema json OK`.
- `ajv` reports each reference manifest as `valid`.
- `strictTypes` warnings may still appear today; treat them as schema hygiene follow-up, not as a passing/failing mismatch by themselves.

## 5. Before you start editing

Confirm these basics:

- you are on the branch your mission or PR expects,
- `git status --porcelain` does not show unrelated files you plan to stage,
- you have read `AGENTS.md` for repo rules and off-limits paths,
- you know which validators your change can affect.
