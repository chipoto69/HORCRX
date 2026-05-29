---
title: Secret handling surfaces
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Secret handling surfaces

HORCRX follows the Hermes binding rule: inject secrets from shell environment or an operator-approved secret manager, not from vessel payloads and not from committed `.env` files.

## 1. Shell-env-only rule

Required posture:

- real credentials live in shell environment, platform secret stores, or dedicated key custody systems,
- committed `.env` files are forbidden,
- `.env.example` may exist only with fake or blank example values,
- vessel export and install flows may carry references to host bindings, never the secret material itself.

## 2. Intended secret stores by surface

| Surface | Secret examples | Intended store | Must not happen |
|---|---|---|---|
| CI / GitHub Actions | `GITHUB_TOKEN`, future package or release tokens | GitHub Actions encrypted secrets and environment-scoped secrets | committing tokens to workflow YAML, docs, fixtures, or example env files |
| Vessel signing | detached signing keys, future signing service credentials | operator-controlled key custody boundary such as HSM, hardware token, or Vault-style secret manager | private keys in repo, build artifacts, or public release assets |
| MCP / gateway integrations | bearer tokens, API keys, service auth headers | host shell environment or service secret manager injected at runtime | hard-coding tokens in manifests, specs, example configs, or markdown |
| x402 facilitator | replay-protection credentials, adapter secrets, nonce-store auth | private service configuration plus durable operator-managed secret storage | stateless nonce handling or secret reuse across public and private planes |
| Wallet custody | wallet seeds, signing mnemonics, hot-wallet credentials | dedicated wallet custody system or operator hardware signer | seeds in `.env`, repo fixtures, screenshots, or copied into tickets |

## 3. Operator checklist

Before a new secret-bearing surface is introduced:

1. name the surface and threat boundary,
2. decide the runtime store,
3. document how the secret is injected,
4. document how rotation and revocation work,
5. add or tighten scanning rules before the first credential is issued.

## 4. Repo hygiene rules

- do not commit `.env`, `auth.json`, `state.db`, wallet exports, or session dumps,
- do not use docs as a place to park real tokens for "just a minute",
- do not downgrade secret scanning because one example string looked inconvenient,
- do not treat public keys, fingerprints, or published CIDs as secrets unless the spec says otherwise.
