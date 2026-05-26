# IP preservation

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

HORCRX uses the same signed, content-addressed vessel primitive for two related jobs:

1. preserving **agent vessels** as portable operating state with lineage and royalty metadata;
2. preserving **human creative work** as timestamped, attributable, and dispute-ready IP artifacts.

The marketplace therefore cannot treat "agent" and "human" as separate products with separate rails. They share notarization, storage, proof, and dispute infrastructure; they differ mainly in slot shape and disclosure policy. Sources: `research/04-economic-thesis.md`, `research/03-competitive-positioning.md`, `specs/vessel-format/SPEC.md`, `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`.

## 1. Preservation surfaces

| Surface | What is preserved | Typical buyer or verifier | Why HORCRX fits |
|---|---|---|---|
| **agent vessel** | soul, skills, memory canon, traces, lineage, royalty target | agent operator, runtime, collector, downstream fork author | the artifact is already a signed manifest plus slot bodies |
| **writer packet** | essays, books, research notebooks, prose voice, draft lineage | publisher, collaborator, arbitration surface | authorship and revision order matter more than hosting |
| **designer packet** | visual systems, tokens, illustration style, prompts, source assets | studio, client, remix partner | attribution and derivative boundaries matter more than a single file export |
| **voice/likeness packet** | speech corpus, consent terms, model checkpoints, signature anchors | voice licensor, synth platform, provenance checker | deepfake risk makes signer identity and disclosure policy first-class |
| **code author packet** | repository snapshots, policy terms, access receipts, monetized inference rights | AI agent, training pipeline, human integrator | CodeVault-style paid access maps cleanly onto content-addressed proof |

This table keeps both the **human** and **agent** use cases explicit and makes the preservation surface a superset of marketplace listing rather than a side product. Sources: `research/04-economic-thesis.md`, `research/02-prior-art.md`, `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`.

## 2. Core preservation workflow

### 2.1 Prepare artifact

The creator selects what will be preserved:

- full vessel,
- partial vessel slot set,
- human creative packet,
- or hybrid packet linking human-authored work to a vessel lineage.

The preparation step must preserve the mind-versus-secrets boundary already established in the Hermes binding and mission doctrine. Secrets, auth files, and host-local credentials are never part of a preservation artifact. Sources: `specs/hermes-binding/BINDING.md`, `research/05-risks-and-tensions.md`.

### 2.2 Timestamped notarization

Every preservation artifact gets **timestamped notarization** before listing or archival release. The lowest-cost default is a Solana-side anchor such as Metaplex inscription-style recording, while Base can anchor the same manifest CID through the chain adapter surface when EVM-side continuity matters more. The important property is not chain preference; it is that a durable timestamp ties a signer to a manifest CID or commitment hash. Sources: `research/02-prior-art.md`, `specs/protocol/chain-adapters.md`, `specs/protocol/PROTOCOL.md`.

### 2.3 Content-addressed storage

The preserved payload is stored using **content-addressed storage**:

- IPFS for broad retrieval and marketplace fetch,
- Arweave for permanent backup,
- optional future CESS replication for additional redundancy.

The registry stores pointers and policy; the preservation payload itself remains content-addressed and portable. Sources: `specs/protocol/registry-design.md`, `specs/marketplace/ARCHITECTURE.md`.

### 2.4 Optional ZK ownership proofs

When a creator wants to prove authorship or possession without revealing the full work, HORCRX can attach **optional ZK ownership proofs** over a commitment chain:

1. hash the raw work or sensitive slot,
2. anchor the commitment in the manifest or preservation record,
3. generate a zk-SNARK or equivalent proof that the preserved artifact matches the committed source without exposing the source.

This should stay optional because many creators only need timestamped notarization plus signatures, not a heavier proving system. Sources: `research/05-risks-and-tensions.md`, `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`.

## 3. Human use cases

### Writers

Writers preserve essays, books, outlines, notebooks, and prose voice as signed packets with explicit licensing terms. The main value is proving sequence, authorship, and derivative boundaries before the work is remixed into training corpora or publishing workflows. Sources: `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`.

### Designers

Designers preserve brand systems, illustration sets, motion language, prompts, and token libraries as linked slots. The preservation artifact can separate public preview assets from paid or private source material while keeping one signed lineage chain. Sources: `research/05-risks-and-tensions.md`, `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`.

### Voice and likeness owners

Voice owners preserve recordings, model checkpoints, allowed-use terms, and revocation policy with stronger provenance requirements because impersonation costs are higher. Marketplace discovery can show a public signer, a trust badge, and a consent policy without exposing the full corpus. Sources: `research/05-risks-and-tensions.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`.

### Code authors

Code authors preserve repository states, access terms, and usage receipts so AI systems can pay for inference, training access, or premium retrieval rather than scrape silently. This is the clearest bridge from the CodeVault prior-art surface into HORCRX. Sources: `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`, `research/03-competitive-positioning.md`.

## 4. Agent vessel use cases

Agent creators preserve vessels for:

- sale,
- cold storage,
- controlled collaboration,
- fork licensing,
- or runtime portability.

The preservation layer matters even when no immediate sale is planned because timestamped, signed, lineage-aware exports make it easier to prove that a later fork or hosted service actually descends from a specific vessel state. Sources: `specs/vessel-format/SPEC.md`, `specs/hermes-binding/BINDING.md`, `research/04-economic-thesis.md`.

## 5. Disclosure and access policy

Preservation artifacts should support three disclosure levels:

| Level | What the market can see | Typical use |
|---|---|---|
| **public** | full payload or fully open slots | open distribution, public showcase |
| **preview** | manifest, metadata, thumbnails, short excerpts, policy text | discovery before purchase |
| **restricted** | commitment hash plus purchase or dispute-gated payload release | sensitive voice corpora, premium code, private research packets |

This lets HORCRX preserve monetizable work without forcing every artifact into full public release. Sources: `specs/vessel-format/SPEC.md`, `specs/marketplace/ARCHITECTURE.md`.

## 6. Dispute workflow

HORCRX must provide a **dispute workflow** because preservation without enforcement becomes theater.

### 6.1 Intake

- rate-limit filings,
- require signer identity or delegated claimant identity,
- require manifest CID or commitment hash,
- require evidence bundle and claimed harm type.

### 6.2 Preliminary review

The marketplace checks whether the complaint is about:

- plagiarism,
- unpaid derivative use,
- deepfake or likeness misuse,
- false provenance,
- or unauthorized commercial extraction.

Low-evidence complaints are rejected quickly so the system cannot be used as a griefing vector. Sources: `research/05-risks-and-tensions.md`, `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`.

### 6.3 Evidence review

Evidence review can use:

- signatures,
- timestamped notarization records,
- royalty and lineage graphs,
- trust badges,
- optional ZK ownership proofs,
- and content similarity checks where legally safe.

### 6.4 Resolution

Resolution options:

- warning label,
- listing freeze,
- payout escrow hold,
- forced attribution fix,
- or handoff to a neutral arbiter / DAO / legal escalation surface.

The registry should never erase history; it should add dispute and resolution state so future buyers can see the trail. Sources: `specs/protocol/PROTOCOL.md`, `research/05-risks-and-tensions.md`.

## 7. Story Protocol posture

Story Protocol is an **integration option**, not a dependency. HORCRX should be able to preserve, list, and sell artifacts without Story, while offering Story-backed licensing or dispute evidence when creators want stronger legal and ecosystem weight for derivative flows. Sources: `research/02-prior-art.md`, `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`.

## Source paths

- `research/02-prior-art.md`
- `research/03-competitive-positioning.md`
- `research/04-economic-thesis.md`
- `research/05-risks-and-tensions.md`
- `specs/vessel-format/SPEC.md`
- `specs/protocol/PROTOCOL.md`
- `specs/protocol/chain-adapters.md`
- `specs/protocol/registry-design.md`
- `specs/hermes-binding/BINDING.md`
- `specs/marketplace/ARCHITECTURE.md`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`
- `~/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md`
- `~/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`
