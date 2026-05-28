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
    - ci/voice-lint
    - ci/secret-scan
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
- Mission B H1 applies the corresponding GitHub-side rule through `gh api repos/chipoto69/HORCRX/branches/main/protection --method PUT`.
