# 02 — Prior Art

This file promotes the already-drafted survey at `/tmp/horcrx-research/02-prior-art.md` into repo-local canon and compresses it into the standards and product surfaces that matter most to HORCRX.

## Payment and commerce standards

### x402
x402 is the strongest payment-native rail already aligned with the local lineage. It already appears in ATLAS code, in the operator wiki, and in the broader market context around agentic commerce. HORCRX should assume x402-first settlement and treat the market layer as an extension of a paid HTTP primitive, not a separate checkout stack. Sources: `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`, `/Users/rudlord/wiki/concepts/x402-protocol.md`, `/Users/rudlord/wiki/raw/reader/Building a More Open Internet: The x402 Foundation (01knwd6qanwvx057x3p33kz44n).md`, `/tmp/horcrx-research/02-prior-art.md`.

### ACP and AP2
ACP and AP2 matter because they define adjacent agent-payment abstractions that buyers and sellers will expect to interoperate with, but they do not displace the local x402 momentum captured in the mission research. HORCRX should remain compatible at the abstraction boundary while shipping x402 first. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`.

### Faremeter
Faremeter is the most concrete x402-adjacent SDK surface mentioned across the research. It matters less as doctrine and more as implementation gravity: if HORCRX later needs a TypeScript-side payment helper, the local research already points there. Sources: `/Users/rudlord/wiki/raw/reader/Index - Faremeter*.md`, `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`.

## Identity, ownership, and royalty standards

### Story Protocol
Story Protocol is the clearest prior-art surface for derivative licensing and on-chain royalty graphs. HORCRX should evaluate it as the human-IP and derivative-lineage layer, not as the vessel runtime itself. Sources: `/Users/rudlord/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`, `/tmp/horcrx-research/02-prior-art.md`.

### ERC-6551
ERC-6551 is the strongest Base-side candidate for a vessel that owns its own wallet and can accumulate state without abandoning standard NFT tooling. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`.

### ERC-7857
ERC-7857 is the closest semantic match for a transferable AI artifact with private payloads, but it is still niche relative to ERC-6551. It is relevant as an optional evolution path rather than a day-one assumption. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`.

### ERC-8004
ERC-8004 matters because trust and reputation are part of the purchase decision for vessels, not just services. Its agent-identity framing lines up with the reputation and registry logic already present in ATLAS. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`.

## Artifact and supply-chain standards

### Anthropic Skills
Anthropic Skills is the one format that already spans the operator's active environments. HORCRX should adopt `SKILL.md` verbatim inside `skills/` and add signing, dependency metadata, and marketplace listing around it instead of inventing a new skill syntax. Sources: `/Users/rudlord/.agents/skills/`, `/Users/rudlord/.hermes/skills/`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-B-skill-ecosystem.md`, `/tmp/horcrx-research/02-prior-art.md`.

### Sigstore
Sigstore is the most mature signing analogue in the prior-art set. Even if HORCRX defaults to in-protocol Ed25519 signatures later, Sigstore remains the clearest model for transparency-log-backed artifact provenance. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`.

## Storage, discovery, and adjacent market surfaces

### agentic.market and Bazaar
Bazaar is the best proof that paid agent discovery can become a legible market surface. It is still a service-discovery layer. HORCRX is different because it packages the vessel itself. Sources: `/Users/rudlord/wiki/raw/reader/Introducing Agentic.Market: The Homepage of the Agent Economy (01kpqjdkmmejp0htc75mtkehzs).md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md`, `/tmp/horcrx-research/02-prior-art.md`.

### Letta, Graphiti, and portable memory
The memory layer has partial prior art but no canonical portable vessel bundle. Letta and Graphiti are useful import/export targets, not substitutes for a HORCRX memory spec. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/wiki/concepts/agent-memory-infrastructure.md`.

### Metaplex Core and Solana asset surfaces
Metaplex Core is the strongest Solana-native candidate for vessel assets, especially when the local stack already includes Solana verification logic and cNFT reputation patterns. Sources: `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/reputation/`.

## Working decision table

| Surface | Best current read | Why it matters to HORCRX |
|---|---|---|
| x402 | primary settlement rail | already aligns with ATLAS and the wiki economy thesis |
| ACP | interop target | buyer expectations, especially merchant-side flows |
| AP2 | interop target | delegated agent payments without changing the core protocol thesis |
| Story Protocol | derivative-IP option | strongest prior art for royalty graph and licensing |
| ERC-6551 | Base adapter default | vessel can own a wallet while staying in standard NFT tooling |
| ERC-7857 | optional advanced adapter | private payload semantics for intelligent NFTs |
| ERC-8004 | trust and reputation extension | agent discovery and reputation alignment |
| Anthropic Skills | mandatory skill packet syntax | already dominant across local agent surfaces |
| Sigstore | signing analogue | transparency and supply-chain provenance |
| Faremeter | implementation gravity | concrete x402 helper surface for future TS work |

## Source paths

- `/tmp/horcrx-research/02-prior-art.md`
- `/tmp/horcrx-research/starred.json`
- `/tmp/horcrx-research/own-repos.json`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md`
