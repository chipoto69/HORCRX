# Hosting and cost envelopes

Version: `v0.1-draft`

Pricing review date: **2026-05-26**.

The first HORCRX deployment should optimize for three things: cheap enough to iterate, simple enough to reason about, and cleanly separable by trust boundary. The cost numbers below are therefore **envelopes**, not procurement commitments. They are intended to help later workers choose defaults without pretending that traffic, storage, or RPC load is already known. Sources: `docs/infrastructure/services.md`, `specs/marketplace/ARCHITECTURE.md`, `specs/protocol/payment-layer.md`.

## 1. Recommended vendor split

| Surface | Recommended default | Rough monthly envelope | Why this split |
|---|---|---:|---|
| **registry indexer + private API** | Hetzner regular-performance cloud | **€20-€60/mo** for two small nodes; **€60-€180/mo** once a separate worker box or read replica is needed | Cheap EU-hosted compute with enough headroom for indexers, queue workers, and internal APIs before managed infra is necessary. Source reviewed 2026-05-26: `https://www.hetzner.com/cloud/regular-performance`, `https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/` |
| **brand site / early marketplace UI** | Vercel Hobby/Pro | **$0/mo** for brand-only staging; **$20+/seat/mo** once the team needs Pro collaboration and credit-based production usage | Fastest path for static or hybrid web surfaces while the product is mostly documentation and read-heavy discovery. Source reviewed 2026-05-26: `https://vercel.com/pricing`, `https://vercel.com/docs/plans/pro-plan`, `https://vercel.com/docs/pricing` |
| **edge alternative for static delivery** | Cloudflare Pages / Workers | **$0/mo** for low-volume static delivery; **low tens of $/mo** once paid Workers or Pages Functions usage appears | Good fit for cache-heavy previews and static brand assets if the team prefers Cloudflare edge primitives over Vercel. Source reviewed 2026-05-26: `https://www.cloudflare.com/plans/developer-platform/`, `https://developers.cloudflare.com/pages/functions/pricing/`, `https://developers.cloudflare.com/workers/platform/pricing/` |
| **hot object cache** | Cloudflare R2 | **$3.75/mo** at 250 GB, **$15/mo** at 1 TB, plus operation charges; zero egress remains the key advantage | Ideal as a derivative cache for public bundle downloads and preview assets; do not treat it as canonical storage. Source reviewed 2026-05-26: `https://developers.cloudflare.com/r2/pricing/` |
| **Solana RPC** | Helius | **$49-$499/mo** on shared plans before custom/dedicated contracts | Strongest fit with the Solana-first research trail and the future need for indexing, webhook, and landing-quality RPC features. Source reviewed 2026-05-26: `https://www.helius.dev/pricing`, `https://www.helius.dev/docs/billing/plans` |
| **Base / EVM RPC (cost-efficient)** | Alchemy | **$0/mo** while free-tier compute is enough; roughly **$4/mo per additional 10M CU** beyond the free 30M CU baseline at listed pay-as-you-go rates | Best early default if Base traffic is still small and usage-based billing is preferred. Source reviewed 2026-05-26: `https://www.alchemy.com/pricing`, `https://www.alchemy.com/docs/reference/pay-as-you-go-pricing-faq` |
| **Base / EVM RPC (fixed-plan alternative)** | QuickNode | **$49/mo** Accelerate, **$249/mo** Scale, **$499/mo** Business, **$999/mo** Enterprise | Better fit if the team wants fixed-plan budgeting or chain-specific add-ons from day one. Source reviewed 2026-05-26: `https://www.quicknode.com/pricing`, `https://www.quicknode.com/docs/platform/billing/flat-rate-rps` |

## 2. Suggested deployment phases

### Phase A — internal prototype

- Hetzner: 1 app node + 1 worker/indexer node
- Vercel Hobby or Cloudflare Pages free tier for the brand site
- Helius dev-tier or equivalent shared Solana RPC
- Alchemy free tier for Base RPC
- R2 only if public bundle previews need fast caching

**Envelope:** roughly **€20-€60/mo + $0-$60/mo**.

### Phase B — closed beta

- Hetzner: add separate gateway or replica node
- Vercel Pro or Cloudflare paid developer plan
- Helius paid shared tier
- Alchemy pay-as-you-go or QuickNode Accelerate/Scale
- R2 cache enabled for previews and larger bundles

**Envelope:** roughly **€60-€180/mo + $100-$650/mo** depending on RPC choice and team seats.

### Phase C — public marketplace

- Hetzner or equivalent private compute remains possible, but trust-sensitive services may need stronger isolation
- Helius or dedicated Solana infrastructure likely becomes non-optional
- QuickNode or Alchemy enterprise-style contract may replace pay-as-you-go convenience
- R2 and IPFS pinning bills become workload-driven instead of essentially fixed

**Envelope:** expect **high hundreds to low thousands of USD/mo** before staff time, legal review, or human support.

## 3. Procurement guidance by surface

### 3.1 Hetzner

Use Hetzner for the private service plane first:

- registry indexer
- x402 facilitator
- internal admin APIs
- search worker jobs

Avoid putting key custody or signing secrets on the same public node that serves previews.

### 3.2 Vercel or Cloudflare Pages

Use Vercel if the team wants the fastest frontend path and collaboration ergonomics. Use Cloudflare Pages if edge caching, Workers integration, and zero-egress R2 proximity matter more than frontend workflow polish.

### 3.3 RPC vendors

Use **Helius** for Solana by default unless later benchmarking disproves it. For Base, start with **Alchemy** if traffic is unknown and switch to **QuickNode** when fixed-plan predictability or add-on features become more valuable than granular usage billing.

## 4. Cost items intentionally excluded from this envelope

These documents do **not** model:

- legal/compliance spending,
- operator support workload,
- fiat on-ramp or wallet vendor charges,
- CDN overages outside R2/Pages/Workers pricing,
- enterprise contracts with custom SLAs,
- LLM inference spend for later search or ranking features.

Those belong in a future implementation-phase budget, not the foundation spec.

## Source paths

- `docs/infrastructure/services.md`
- `specs/marketplace/ARCHITECTURE.md`
- `specs/protocol/payment-layer.md`
- `https://www.hetzner.com/cloud/regular-performance`
- `https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/`
- `https://vercel.com/pricing`
- `https://vercel.com/docs/plans/pro-plan`
- `https://vercel.com/docs/pricing`
- `https://www.cloudflare.com/plans/developer-platform/`
- `https://developers.cloudflare.com/pages/functions/pricing/`
- `https://developers.cloudflare.com/workers/platform/pricing/`
- `https://developers.cloudflare.com/r2/pricing/`
- `https://www.helius.dev/pricing`
- `https://www.helius.dev/docs/billing/plans`
- `https://www.alchemy.com/pricing`
- `https://www.alchemy.com/docs/reference/pay-as-you-go-pricing-faq`
- `https://www.quicknode.com/pricing`
- `https://www.quicknode.com/docs/platform/billing/flat-rate-rps`
