---
title: Troubleshoot CI failures
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Troubleshoot CI failures

This page covers the failure modes that have already shown up during the hardening pass.

## 1. `ajv` prints `strictTypes` warnings

Symptom:

```text
strict mode: missing type "array" for keyword "items" ...
strict mode: use allowUnionTypes to allow union type keyword ...
```

What it means:

- `ajv` still validated the manifest examples, so the job can pass even while schema hygiene warnings remain.
- The warning usually means a schema branch declares `items`, `properties`, or `required` without an explicit `type`, or uses a union form that `ajv` wants rewritten.

What to do:

1. reproduce locally with the `ci/schema-validate` command from `docs/onboarding/02-run-validators.md`,
2. add the missing explicit `type` in the flagged schema branch,
3. prefer `oneOf` or explicit `type` branches over ambiguous union shorthand,
4. re-run `ajv` and confirm the example manifests still validate.

Do not suppress the warning unless the schema design is intentionally relying on an `ajv` behavior you can justify in the PR.

## 2. `commitlint` rejects the subject or scope

The repo accepts only these commit types:

- `feat`
- `fix`
- `docs`
- `chore`
- `build`
- `ci`
- `refactor`
- `test`
- `polish`

Common failures:

- missing scope or colon separator,
- free-form prefixes such as `update:` or `misc:`,
- deny-listed scope tokens such as `wip`, `tmp`, `temp`, or `fixup`.

Examples:

```text
docs(ops): add marketplace operator runbook
ci(validation): add docs allowlist gate
```

```text
docs(wip): draft notes        # rejected
fixup: quick change           # rejected
```

Fix the subject and recommit; do not bypass `.githooks/commit-msg`.

## 3. `voice-lint` flags operational syntax in identity-only files

Current rule shape:

- a line that starts with `$`, `sudo`, `git `, `npm `, `pnpm `, `brew `, or `/Users/` fails,
- a blockquote line that starts with those patterns also fails.

Usual causes:

- command examples written as blockquotes instead of fenced code blocks,
- absolute paths pasted into `SOUL.md`, `voice.md`, or `soul.md`,
- identity prose that accidentally starts a line with shell syntax.

Safe fixes:

- move command examples into fenced code blocks in operational docs,
- rewrite quoted prose so the command is inline rather than line-leading,
- keep identity files about voice, doctrine, and behavior only.

## 4. `secret-scan` finds a false positive

Start by assuming the finding is real. Only whitelist after you confirm the string is test data, a hash, or a published public identifier.

Recommended order:

1. remove the value if it does not belong in the repo,
2. redact or shorten the sample if the docs only need illustrative syntax,
3. move examples into fenced markdown blocks instead of executable-looking added lines when possible,
4. if the value is intentionally harmless and still blocks `gitleaks`, add the narrowest possible entry to `.gitleaksignore` and explain why in the PR.

Avoid broad allowlist patterns. The goal is to clear one justified false positive without teaching the scanner to miss nearby real leaks.

## 5. Baseline triage order

If several gates fail at once, use this order:

1. `pnpm test`
2. `ci/schema-validate`
3. `ci/markdown-link-check`
4. `ci/secret-scan`
5. the narrower H2 gate scripts touched by your change

Fix the first hard failure before trusting later output.
