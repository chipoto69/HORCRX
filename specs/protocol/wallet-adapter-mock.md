# Wallet adapter mock

Version: `v0.1-draft`

This contract defines the **mock wallet adapter** that Phase 3 of
`docs/roadmap/next-missions.md` can consume before any live wallet keys,
embedded-wallet credentials, or payment rails exist.

The mock stays intentionally close to the adapter shapes exposed by Crossmint
and Privy: a connectable client with explicit session state, message signing,
transaction signing, and disconnect semantics. It exists to unblock browse,
preview, and purchase-intent UI flows without granting the frontend any live
custody surface.

## Goals

- keep the Phase 3 marketplace UI unblocked while wallets remain off-limits,
- provide a deterministic adapter contract for fixtures and browser tests,
- preserve forward-compatibility with Crossmint/Privy-style provider wrappers,
- guarantee that no secret, seed phrase, API key, or live signer material is
  required in foundation phase.

## Normalized shape

The mock exposes one adapter object with a small Crossmint/Privy-compatible
surface:

```ts
type MockWalletAdapter = {
  status: "idle" | "connected";
  provider: "mock-crossmint" | "mock-privy";
  chain: "base" | "solana";
  address: string | null;
  connect(input?: ConnectInput): Promise<ConnectResult>;
  signMessage(message: string): Promise<MockSignature>;
  signTransaction(transaction: string): Promise<MockTransactionRef>;
  disconnect(): Promise<void>;
};
```

## Connect contract

`connect(input?)` returns a deterministic mock session record:

```ts
type ConnectInput = {
  provider?: "mock-crossmint" | "mock-privy";
  chain?: "base" | "solana";
};

type ConnectResult = {
  provider: "mock-crossmint" | "mock-privy";
  chain: "base" | "solana";
  address: string;
  connected_at: string; // ISO 8601 UTC
};
```

Rules:

- default provider: `mock-privy`
- default chain: `base`
- Base address shape: `0x` + 40 lowercase hex characters
- Solana address shape: base58, 32–44 characters
- returned addresses come from fixed fixture constants, never from generated keys

Suggested fixture addresses:

- Base: `0x7c3a6f0db5a4df0b8ab62e5e53417b6a33b4f0a1`
- Solana: `So11111111111111111111111111111111111111112`

## Message signing contract

`signMessage(message)` returns a deterministic mock signature envelope:

```ts
type MockSignature = {
  chain: "base" | "solana";
  address: string;
  algorithm: "mock-ecdsa" | "mock-ed25519";
  signature: string;
};
```

Rules:

- Base sessions use `mock-ecdsa`
- Solana sessions use `mock-ed25519`
- `signature` MUST be deterministic for the same `(chain, address, message)`
- recommended encoding:
  `mocksig:<sha256(chain + ":" + address + ":" + message)>`

This mirrors the "sign arbitrary payload" affordance that both Crossmint and
Privy expose while staying obviously non-production.

## Transaction signing contract

`signTransaction(transaction)` returns a deterministic transaction reference:

```ts
type MockTransactionRef = {
  chain: "base" | "solana";
  address: string;
  tx_hash: string;
  signed_payload: string;
};
```

Rules:

- `signed_payload` echoes the canonical serialized transaction string that the
  UI passes in
- `tx_hash` MUST be deterministic for the same `(chain, address, transaction)`
- recommended encoding:
  `mocktx:<sha256(chain + ":" + address + ":" + transaction)>`

The mock is allowed to emulate "sign and return" only. It MUST NOT emulate
broadcast, nonce management, gas estimation, or chain finality.

## Disconnect contract

`disconnect()` clears the in-memory session state and returns the adapter to:

- `status = "idle"`
- `address = null`
- last-signed payload references discarded from active memory

No persistent storage is written. Refreshing the UI should rebuild state from
fixtures alone.

## Compatibility notes

- **Crossmint shape**: keep explicit `connect()` and signer-return semantics so a
  later Crossmint adapter can satisfy this interface by wrapping its SDK object.
- **Privy shape**: keep provider identity and connected wallet metadata separate
  from the message/transaction verbs so a later Privy client can swap in under
  the same contract.
- **HITL**: purchase dispatch remains outside this adapter. Wallet connection is
  not approval to spend.

## Out of scope

- live wallet keys,
- live RPC calls,
- embedded-wallet API credentials,
- fiat checkout,
- custody recovery,
- transaction broadcast.
