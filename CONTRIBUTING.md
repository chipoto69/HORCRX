# Contributing

HORCRX foundation work uses local mission branches and Conventional Commits.

## Branch strategy

- Default branch: `main`.
- Feature branches: `foundation/<area>` during the foundation mission, then focused feature branches in later phases.
- Do not push directly to `main`. Use a pull request once the validation contract is satisfied.

## Commit format

Commit subjects must match:

```text
<type>(<scope>): <subject>
```

Allowed types: `feat`, `fix`, `docs`, `chore`, `build`, `ci`, `refactor`, `test`, `polish`.

Install local hooks before committing:

```bash
git config core.hooksPath .githooks
```

The `commit-msg` hook enforces the subject format. The `pre-push` hook blocks direct pushes to `main`.

## Pull requests

PRs should include:

- summary of the feature or spec change,
- affected milestone or roadmap phase,
- validation-contract assertions covered,
- tests or validators run,
- confirmation that no secrets or off-limits paths were touched.

The validation contract lives at the mission artifact path for this foundation run and is summarized in `WORKER-COMPLETE.md` at close.
