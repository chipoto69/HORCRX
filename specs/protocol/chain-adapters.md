# Chain adapters

Version: `v0.1-draft`

The HORCRX protocol layer is chain-agnostic. Concrete settlement, ownership, and registry rules live behind an adapter contract.

## 1. Abstract `IChainAdapter`

```ts
interface IChainAdapter {
  readonly adapterId: string;
  readonly family: 'evm' | 'solana' | 'other';
  readonly network: string;
  resolveOwner(registryPointer: string): Promise<OwnerRecord>;
  publishRecord(input: PublishRecord): Promise<ChainReceipt>;
  transferRecord(input: TransferOwnership): Promise<ChainReceipt>;
  publishListing(input: UpdateListing): Promise<ChainReceipt>;
  revokeRecord(input: RevokeRecord): Promise<ChainReceipt>;
  verifyPaymentProof(input: PaymentProof): Promise<PaymentVerification>;
  resolveRoyalty(input: RoyaltyResolution): Promise<RoyaltyQuote>;
}
```

The shape mirrors the multi-chain seam already present in `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/protocol.py` and `registry.py`.

## 2. Base adapter

### 2.1 Ownership primitive

Use **ERC-721** as the default vessel ownership record because it is the safest and most legible default in existing Base tooling.

### 2.2 Royalty primitive

Use **ERC-2981** for default royalty declaration so derivative-aware marketplaces can query a standard royalty surface.

### 2.3 Optional wallet-holding primitive

Evaluate **ERC-6551** when a vessel should own a wallet or autonomous escrow account without abandoning the ERC-721 registry base.

### 2.4 Payment model

Use x402-compatible payment proof verification against Base transaction receipts and ERC-20 transfer logs when settlement is denominated in USDC or equivalent ERC-20 assets.

### 2.5 Pros

- strong marketplace and wallet tooling,
- clear owner-of-record semantics,
- natural fit for x402's growing EVM-side gravity,
- ERC-2981 gives immediate royalty interoperability.

### 2.6 Cons

- ERC-721 alone does not give the vessel its own wallet,
- ERC-6551 adds complexity and operational overhead,
- registry cost and contract upgrade posture must be managed carefully.

### 2.7 v0.1 posture

For the Base adapter, HORCRX specifies **ERC-721 + ERC-2981** as the baseline and keeps **ERC-6551** as an evaluated extension, not a day-one requirement.

## 3. Solana adapter

### 3.1 Ownership primitive

Use **Metaplex Core** as the default vessel ownership record because it is the strongest standard Solana asset surface for a portable, discoverable artifact.

### 3.2 Compressed or lightweight distribution path

Evaluate **cNFT** paths when lower-cost, high-volume asset issuance is more important than richer per-asset flexibility.

### 3.3 Payment model

Use x402-compatible payment proof verification against Solana transaction data, SPL token transfers, and memo-bound nonce semantics when settlement is denominated in USDC or SOL.

### 3.4 Pros

- low-cost, high-throughput settlement,
- strong local precedent via existing Solana verifier and cNFT reputation work,
- natural fit for memo-carried nonces and transaction-level provenance.

### 3.5 Cons

- asset-standard fragmentation between Core, legacy NFTs, and cNFT paths,
- account-model complexity for teams coming from EVM,
- some marketplace surfaces still assume collection-centric semantics.

### 3.6 v0.1 posture

For the Solana adapter, HORCRX specifies **Metaplex Core** as the baseline and keeps **cNFT** as an evaluated extension for lower-cost issuance and discovery surfaces.

## 4. Symmetry rules

To keep Base and Solana first-class:

1. both adapters must expose the same abstract operations;
2. both adapters must resolve royalties, revocations, and ownership changes;
3. neither adapter may alter the abstract vessel manifest shape;
4. chain-specific optimizations remain adapter-local.

## 5. Source paths

- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/protocol.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/registry.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/base_verifier.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/solana_verifier.py`
- `/Users/rudlord/HORCRX/research/02-prior-art.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
