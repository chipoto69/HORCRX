---
title: Mission entry checklist
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Mission entry checklist

Use this when you are entering a HORCRX mission branch or resuming an assigned feature.

## 1. Read the mission packet before editing

If a mission directory exists, read these files first:

- `mission.md`
- `AGENTS.md`
- `services.yaml`
- `validation-contract.md`
- `features.json`

Your feature's `fulfills` assertions define what "done" means. Treat them as binding acceptance criteria.

## 2. Bootstrap hooks before your first commit

```bash
git config --local core.hooksPath .githooks
git config core.hooksPath
```

Expected output:

```text
.githooks
```

## 3. Run the mission initializer if one exists

```bash
/path/to/mission/init.sh
```

Mission init scripts in HORCRX are expected to be idempotent. They may verify tool versions, fetch origin, re-check branch posture, and warm validator dependencies.

## 4. Confirm HERMES-01 before staging anything

HERMES-01 means: untracked or unrelated operator-state files must stay untouched unless the mission packet names a deliberate carve-out.

In practice:

- do not `git add .`,
- do not `git stash` unrelated work,
- do not `git clean` operator-state files,
- stage only the files your assigned feature actually changes.

## 5. Run the baseline validators

At minimum:

```bash
pnpm test
```

Then run the narrower validators your feature can affect. For docs work, that usually includes markdown link checks, docs allowlist checks, and any CI helper the feature touches.

## 6. Work inside mission boundaries

Keep these rules visible:

- never push directly to `main`,
- never force-push a shared mission branch,
- use Conventional Commits,
- respect off-limits paths from `AGENTS.md`,
- use `services.yaml` as the source of truth for reusable commands.

## 7. Close the loop before handoff

Before you report completion:

- re-run validators,
- check `git status --porcelain`,
- commit only the intended files,
- surface any pending operator HITL decisions in the handoff.
