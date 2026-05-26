# Discovery and trust

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

Discovery is only valuable if buyers can tell the difference between a real vessel, a respected seller, a low-signal clone, and a deepfake persona wrapped in polished UI. HORCRX therefore treats reviews, reputation, attestations, and provenance controls as first-class market data. Sources: `research/05-risks-and-tensions.md`, `research/03-competitive-positioning.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`.

## 1. Review system

HORCRX should expose a **review system** with three rules:

1. only verified purchasers or verified installers can submit a review;
2. review weight is adjusted by reputation and anti-Sybil controls;
3. provenance and disclosure context are shown alongside the score.

This inherits the practical shape already visible in the ATLAS marketplace backend, where purchase state and review state are linked, but adds vessel-specific context such as lineage depth, encrypted-slot disclosure, and preservation-artifact type. Sources: `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`, `specs/protocol/marketplace-flows.md`.

### 1.1 Review payload

Each review should bind:

- manifest CID,
- reviewer identity,
- proof of purchase or install,
- numeric rating,
- textual feedback,
- declared use case,
- and optional downstream fork result.

That keeps reviews anchored to actual economic or runtime contact rather than drive-by attention farming. Sources: `specs/marketplace/ARCHITECTURE.md`, `specs/hermes-binding/BINDING.md`.

## 2. Reputation cNFTs

HORCRX should **inherit reputation cNFTs from ATLAS**, not invent a second badge taxonomy. The inherited badge classes are:

- `TRADER`
- `RESEARCHER`
- `BUILDER`
- `CURATOR`
- `COLLABORATOR`

Each badge also carries a tier progression, which can be used to weight reviews, prioritize discovery, and expose seller history without pretending that raw volume equals trust. Sources: `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/reputation/cnft.py`, `research/06-local-modules-inventory.md`.

### 2.1 How cNFTs affect ranking

Reputation cNFTs should influence:

- result ranking,
- default sort order for comparable listings,
- review helpfulness weighting,
- and trust badge prominence.

They should **not** override explicit fraud or dispute flags. High-reputation actors can still ship bad derivatives or misleading preservation artifacts. Sources: `research/05-risks-and-tensions.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/reputation/cnft.py`.

## 3. Trust badges

Trust badges are signed, content-addressed attestations layered on top of a vessel or preservation artifact. Examples:

- signature verified,
- lineage verified,
- verified purchase volume,
- curator reviewed,
- rights holder verified,
- preservation dispute resolved.

Unlike reputation cNFTs, which describe standing over time, trust badges describe **specific claims** about a particular listing or artifact. Sources: `specs/protocol/PROTOCOL.md`, `specs/vessel-format/signing-and-lineage.md`, `research/05-risks-and-tensions.md`.

## 4. Anti-Sybil controls

The review and trust system needs anti-Sybil protections because vessel markets are easy to spam with cheap clones and fake praise.

Minimum controls:

- verified-purchase gating,
- reviewer cooldown windows,
- badge-weighted helpful votes,
- duplicate-wallet and duplicate-signer heuristics,
- anomaly detection on review timing and wording.

These controls should reduce manipulation without making anonymous or pseudonymous creators impossible. Sources: `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`, `research/05-risks-and-tensions.md`.

## 5. Anti-deepfake-persona controls

Deepfake personas are one of the highest-cost trust failures for HORCRX because the marketplace may list:

- agent personalities,
- creator voice packets,
- likeness-linked artifacts,
- and branded derivative vessels.

Required anti-deepfake controls:

1. **mandatory signing key publication** for every listed artifact;
2. clear separation between creator identity, seller identity, and runtime installer identity;
3. public provenance chain from parent CIDs to current listing;
4. optional **KYC-light tier** for creators who want stronger human-facing assurance;
5. voice or likeness packets must disclose whether the seller is the originator, a licensed operator, or a derivative creator.

Sources: `research/05-risks-and-tensions.md`, `specs/hermes-binding/BINDING.md`, `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`.

### 5.1 KYC-light posture

KYC-light should remain optional and scoped:

- useful for high-value voice or likeness listings,
- useful for enterprise buyers who need stronger counterparty evidence,
- not required for ordinary open vessel trade.

The goal is better trust signaling, not mandatory identity extraction from every pseudonymous builder. Sources: `research/05-risks-and-tensions.md`, `research/02-prior-art.md`.

## 6. Discovery ranking stack

Search/discovery should rank using a blended score over:

- capability match,
- price and licensing fit,
- signer verification,
- review quality,
- reputation cNFT tier,
- trust badge count and freshness,
- dispute history,
- and lineage clarity.

This keeps "best" from collapsing into "most marketed." A vessel with clean provenance and strong downstream reviews should outrank a louder but unverifiable clone. Sources: `specs/marketplace/ARCHITECTURE.md`, `research/03-competitive-positioning.md`.

## 7. Buyer-facing trust summary

Every listing page and MCP preview should expose:

- manifest CID,
- signer status,
- reputation cNFT summary,
- review count and verified-purchase share,
- trust badges,
- dispute state,
- deepfake-risk disclosures for persona-linked artifacts.

Trust needs to be legible to both humans and agents. Sources: `specs/marketplace/ARCHITECTURE.md`, `specs/protocol/interop.md`.

## Source paths

- `research/02-prior-art.md`
- `research/03-competitive-positioning.md`
- `research/05-risks-and-tensions.md`
- `research/06-local-modules-inventory.md`
- `specs/protocol/PROTOCOL.md`
- `specs/protocol/marketplace-flows.md`
- `specs/protocol/interop.md`
- `specs/vessel-format/signing-and-lineage.md`
- `specs/hermes-binding/BINDING.md`
- `specs/marketplace/ARCHITECTURE.md`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/marketplace/service_v2.py`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/reputation/cnft.py`
- `~/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`
