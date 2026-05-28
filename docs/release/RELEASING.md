---
title: Releasing HORCRX
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Releasing HORCRX

This repo is still in a foundation-first phase. Use this document as the operator checklist for the first tagged releases, not as permission to cut a tag from an unreviewed branch.

## 1. Pre-tag checklist

Before any release tag is created, confirm all of the following:

- validators are green locally and in CI,
- `specs/vessel-format/manifest.schema.json` parses cleanly and all reference manifests validate,
- `CHANGELOG.md` contains the matching version section,
- `SECURITY.md` still points to the active private intake path,
- no secret-scanner finding remains unresolved,
- operator-reviewed release notes are ready.

Recommended local pass:

```bash
pnpm test
./validation/scripts/gate-hx-04-signature-roundtrip.py
./validation/scripts/gate-hx-05-parent-cid-resolves.py
./validation/scripts/gate-hx-06-strip-rehydrate.sh
./validation/scripts/gate-hx-07-docs-allowlist.sh
./validation/scripts/gate-hx-08-voice-lint-extended.sh
./validation/scripts/x402-nonce-replay.py
./validation/scripts/royalty-determinism.py
```

## 2. Tag format

HORCRX release automation listens for tags that match:

```text
v*
```

Use semver-shaped tags such as:

```text
v0.1.2
v0.2.0
```

Match the tag exactly to the `CHANGELOG.md` section header the release workflow will extract.

## 3. Draft release flow

Current automation in `.github/workflows/release.yml` does this on tag push:

1. check out the tagged commit,
2. extract the matching `CHANGELOG.md` section,
3. create a **draft** GitHub release.

Operator flow after the draft exists:

1. inspect the generated release notes,
2. confirm the tag points at the intended reviewed commit,
3. attach any generated artifacts that belong to the release,
4. publish the draft only after the notes and artifacts are complete.

## 4. Signing posture

HORCRX does not yet publish a production vessel-signing key from this repo.

Until that changes:

- do not commit private signing material,
- do not fake a signing fingerprint in release notes,
- keep the public fingerprint location reserved in `SECURITY.md`,
- treat detached signing as operator-controlled infrastructure outside this repo.

## 5. Post-release cleanup

After publishing the draft release:

- confirm the release page references the same version as `CHANGELOG.md`,
- verify the release branch or helper branch has no unmerged follow-up fixes hiding on it,
- delete short-lived helper branches that were created only for the release once they are merged or no longer needed,
- leave the protected long-lived mission branches alone unless the operator explicitly closes them.

## 6. What not to do

- do not tag from `main` unless the reviewed PR is already merged,
- do not publish a release while CI is red,
- do not use release automation as a substitute for the private vulnerability intake process,
- do not cut a tag just to checkpoint work-in-progress.
