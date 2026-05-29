# Branch protection specification

This file documents the intended protection rules for `main`. Mission B H1 applies this rule via `gh api` as an operator-gated hardening step.

## `main` rule

```yaml
branch: main
require_pull_request_reviews: true
dismiss_stale_reviews: true
require_code_owner_reviews: true
required_approving_review_count: 1
required_status_checks:
  strict: true
  contexts:
    - ci/commitlint
    - ci/schema-validate
    - ci/markdown-link-check
    - ci/docs-frontmatter
    - ci/voice-lint
    - ci/secret-scan
    - ci/gate-hx-04-signature-roundtrip
    - ci/gate-hx-05-parent-cid-resolves
    - ci/gate-hx-06-strip-rehydrate
    - ci/gate-hx-07-docs-allowlist
    - ci/gate-hx-08-voice-lint-extended
    - ci/x402-nonce-replay
    - ci/royalty-determinism
    - ci/payout-target-format
    - ci/revocation-never-deletes
    - ci/chain-adapter-symmetry
    - ci/preview-integrity
    - ci/marketplace-envelope-kats
    - ci/changelog-regression
required_linear_history: true
restrict_pushes: admins_only
enforce_admins: false
allow_force_pushes: false
allow_deletions: false
```

## Operational notes

- All changes should arrive through pull requests.
- CODEOWNERS approval is required for changes under `/specs/`, `/contracts/`, and `/.github/`.
- Admin enforcement is disabled to permit operator UI admin-override merge on single-owner PRs. See §Single-CODEOWNER merge path (personal repo) for the canonical override pattern. All admin actions are auditable in PR history.
- Direct pushes to `main` are blocked locally by `.githooks/pre-push`; the remote rule above is the corresponding GitHub-side policy.
- Mission B H1 applies the corresponding GitHub-side rule through `gh api repos/chipoto69/HORCRX/branches/main/protection --method PUT`.

## Single-CODEOWNER merge path (personal repo)

This repo is owned by a single user (`chipoto69`), not a GitHub organization.
On personal repositories, GitHub does NOT support `bypass_pull_request_allowances`
in branch protection — the API returns HTTP 422 with "Only organization
repositories can have users and team restrictions".

Required-reviews + required-checks therefore deadlock single-owner PRs:
the operator cannot approve their own PR, and no second reviewer exists.

### Canonical merge path: GitHub UI admin-override

The operator (repo admin) can merge any PR via the **"Merge without waiting for
requirements"** checkbox visible only to admins because `enforce_admins: false`
keeps the admin bypass path available for this personal repo.

This requires `enforce_admins: false` in this file's spec — see line ~37.

Steps:
1. Open the PR in the GitHub web UI
2. Scroll to the merge button
3. Check the admin-override box ("Merge without waiting for requirements")
4. Click "Confirm squash and merge"

This bypasses both required-review and required-status-check rules for that
single merge action. It is auditable in the PR history.

### Off-limits

- Do NOT use admin-override to skip checks that actually failed (only use it
  to bypass review when no reviewer exists, or to merge a release-prep PR
  whose required contexts are blocked by main-state drift after a workflow
  rollout).
- Do NOT use admin-override to push a force-push or destructive change.
- Do NOT use admin-override on cross-mission handoff PRs that should genuinely
  wait for a reviewer.

### Future: migrate to organization

If/when CODEOWNERS expands to a team, migrate the repo to a GitHub organization
(e.g., create a HORCRX org, transfer the repo to it). At that point,
`bypass_pull_request_allowances` becomes available and review-bypass can be
narrowly granted to the operator instead of using full admin-override.
