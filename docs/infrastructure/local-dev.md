---
title: Local development stack
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Local development stack

Version: `v0.1-draft`

The local HORCRX stack should prove five things before any real deployment exists:

1. Base settlement semantics can be exercised against a local EVM,
2. Solana adapter logic can be exercised against a local validator,
3. bundle storage can round-trip through a local or mocked content-addressed surface,
4. registry and search flows can run against a disposable local database, and
5. Hermes-facing purchase/install flows can be rehearsed without putting secrets into vessel artifacts.

This is a **spec for future worker setup**, not a runnable compose file. Sources: `specs/protocol/payment-layer.md`, `specs/hermes-binding/BINDING.md`, `research/02-prior-art.md`, `~/wiki/raw/downloads/2026-04-10/root/system-map.md`. <!-- wiki source -->

## 1. Local stack components

| Component | Local choice | Why |
|---|---|---|
| Base adapter | `anvil` | Fast local EVM with deterministic accounts and cheap reset loops. |
| Solana adapter | `solana-test-validator` | Best local parity for account layouts, token flows, and transaction confirmation behavior. |
| Bundle storage | local Kubo IPFS daemon **or** a `web3.storage`-compatible mock | Lets workers test CID resolution and preview policy without buying storage first. |
| Permanent mirror stub | fake Irys/Arweave receipt writer | Enough to test that the workflow records a permanent-storage reference without actually paying for it. |
| Registry store | sqlite | Smallest useful projection store for registry, lineage, and replay-protection data. |
| Search index | sqlite FTS or in-memory stub | Keeps discovery tests cheap while the schema is still moving. |
| x402 facilitator | local-mode facilitator compatible with Faremeter-style challenge/verify flows | Preserves payment semantics before a real chain-backed service exists. |
| Hermes-side audit sink | existing `dispatch()` audit path | Required to verify that purchases and installs remain attributable from runtime to marketplace. |

## 2. Startup order

### 2.1 Secrets and host policy

Before anything else:

- keep LLM keys in the **shell environment**, not in repo files,
- keep wallet or test-key material outside any vessel folder,
- treat local test keys as disposable, and
- preserve the system-map split: sandbox code may talk to local infra, but the secret boundary remains outside bundle assembly. Sources: `~/wiki/_meta/hermes-stack/hermes-content-os.md`, `~/wiki/raw/downloads/2026-04-10/root/system-map.md`, `specs/hermes-binding/BINDING.md`. <!-- wiki source -->

### 2.2 Base local chain

Expected future-worker command shape:

```bash
anvil --chain-id 8453 --port 8545
```

Use deterministic funded dev accounts so payment-proof tests and listing flows can be replayed cleanly.

### 2.3 Solana local validator

Expected future-worker command shape:

```bash
solana-test-validator --reset
```

Reset by default so indexing, badge, and listing tests do not inherit stale ledger state.

### 2.4 Local IPFS or mock gateway

Preferred flow:

- run local Kubo/IPFS daemon when testing real CID fetch behavior,
- fall back to a mock gateway if the worker only needs manifest-resolution semantics,
- keep the content gateway logic provider-agnostic so the same tests later work with `web3.storage` or Pinata.

### 2.5 Registry and search services

Run the indexer against sqlite with four logical tables at minimum:

- `listings`
- `lineage_events`
- `payment_receipts`
- `replay_nonces`

Search may be a second sqlite database or FTS virtual tables in the same file.

### 2.6 x402 facilitator local mode

The local payment surface should expose challenge/verify behavior compatible with the eventual x402 service boundary:

- create payment challenge,
- bind nonce + expiry,
- accept mock or local-chain proof,
- record receipt keyed by manifest CID and listing ID,
- reject replayed proof or expired nonce.

Faremeter is the first TS surface to evaluate when this becomes real implementation work. Sources: `specs/protocol/payment-layer.md`, `~/wiki/raw/reader/Index - Faremeter*.md`. <!-- wiki source -->

## 3. Suggested local workflow

1. start `anvil`
2. start `solana-test-validator`
3. start local IPFS or mock gateway
4. boot sqlite-backed registry indexer
5. boot local x402 facilitator
6. run a fixture flow:
   - publish mock vessel manifest
   - list it through the registry projection
   - request payment challenge
   - verify local proof
   - fetch bundle preview
   - emit Hermes-side `dispatch()` audit event for simulated install

If that flow fails, the problem is likely in adapter boundaries, replay logic, or preview policy rather than in UI code.

## 4. Non-runnable `docker-compose.yml` sketch

The following sketch is illustrative only. It exists to communicate shape, not to be committed as production-ready infra.

```yaml
services:
  anvil:
    image: ghcr.io/foundry-rs/foundry:stable
    command: ["anvil", "--chain-id", "8453", "--port", "8545"]

  solana-test-validator:
    image: solanalabs/solana:stable
    command: ["solana-test-validator", "--reset"]

  ipfs:
    image: ipfs/kubo:latest
    command: ["daemon", "--migrate=true"]

  registry:
    image: horcrx/registry-dev
    environment:
      DATABASE_URL: sqlite:///workspace/registry.sqlite
      BASE_RPC_URL: http://anvil:8545
      SOLANA_RPC_URL: http://solana-test-validator:8899

  facilitator:
    image: horcrx/x402-dev
    environment:
      DATABASE_URL: sqlite:///workspace/registry.sqlite
      BASE_RPC_URL: http://anvil:8545
      SOLANA_RPC_URL: http://solana-test-validator:8899
      IPFS_GATEWAY_URL: http://ipfs:8080
```

## 5. Exit criteria for a future local-dev worker

A future worker should consider local-dev setup complete only when they can demonstrate:

- one Base-side purchase challenge and verify loop,
- one Solana-side registry or provenance update,
- one CID fetch through the content gateway,
- one replay rejection,
- one Hermes-linked `dispatch()` audit row for a simulated purchase/install flow.

## Source paths

- `specs/protocol/payment-layer.md`
- `specs/hermes-binding/BINDING.md`
- `specs/marketplace/ARCHITECTURE.md`
- `research/02-prior-art.md`
- `research/05-risks-and-tensions.md`
- `~/wiki/raw/downloads/2026-04-10/root/system-map.md` <!-- wiki source -->
- `~/wiki/_meta/hermes-stack/hermes-content-os.md` <!-- wiki source -->
- `~/wiki/raw/reader/Index - Faremeter*.md` <!-- wiki source -->
- `https://web3.storage/pricing/`
- `https://pinata.cloud/pricing`
