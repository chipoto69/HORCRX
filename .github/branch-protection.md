# Branch protection specification

This file documents the intended protection rules for `main`. The F09 publisher run used the default operator decision: **spec-only** branch protection documentation, with no live `gh api` protection mutation.

## `main` rule

```yaml
branch: main
require_pull_request_reviews: true
dismiss_stale_reviews: true
require_code_owner_reviews: true
required_status_checks:
  strict: true
  contexts:
    - ci/commitlint
    - ci/schema-validate
    - ci/markdown-link-check
required_linear_history: true
restrict_pushes: admins_only
enforce_admins: true
allow_force_pushes: false
allow_deletions: false
```

## Operational notes

- All changes should arrive through pull requests.
- CODEOWNERS approval is required for changes under `/specs/`, `/contracts/`, and `/.github/`.
- Direct pushes to `main` are blocked locally by `.githooks/pre-push`; the remote rule above is the corresponding GitHub-side policy.
- Actual branch protection API application remains optional for a later operator-approved hardening pass.
