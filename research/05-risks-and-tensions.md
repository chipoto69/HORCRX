# 05 — Risks and Tensions

HORCRX is valuable precisely because it makes agent state portable. That same portability creates the main failure modes.

| Risk | Why it matters | Mitigation sketch | Sources |
|---|---|---|---|
| Soul theft | a vessel bundle can leak identity, tone, and hard-won behavioral patterns | require signed manifests, per-slot signatures, and host-controlled secret rehydration | `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`, `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/system-map.md` |
| Replay | paid purchase or install proofs can be replayed across hosts or requests | keep nonce and expiry semantics aligned with x402 and registry-side provenance records | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/x402/`, `/Users/rudlord/wiki/concepts/x402-protocol.md` |
| Signature forgery | unsigned or weakly signed bundles destroy trust in lineage | default to strong bundle signing and optional transparency-log anchoring | `/tmp/horcrx-research/02-prior-art.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md` |
| Deepfake personas | a fake vessel can claim to be a known operator, profile, or creator | separate creator identity, vessel signer, and runtime installer identities; display provenance chains prominently | `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md` |
| Regulatory exposure | a revenue-sharing artifact can drift toward KYC, securities, or consumer-protection obligations | keep launch scope narrow, prefer notarization and paid access over speculative token layers, and avoid token-first framing | `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-C-wiki-deep-dive.md`, `/tmp/horcrx-research/02-prior-art.md` |
| Trust-domain separation failure | mind and secrets living in the same artifact is catastrophic | enforce the mind-vs-secrets split from `system-map.md`; secrets never ship inside the vessel | `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/system-map.md`, `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md` |
| IP enforcement weakness | derivative use without royalties or attribution undermines the economic thesis | attach lineage metadata to every fork and keep explicit royalty targets in the manifest | `/Users/rudlord/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`, `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/codevault-landing-copy.md` |
| Memory drift | instruction memory and learning memory can collapse into one junk drawer | preserve separate canon, episodic, and host-local layers; require operator-visible promotion gates | `/Users/rudlord/wiki/concepts/agent-memory-infrastructure.md` |
| Privacy leakage from sessions | raw sessions and `state.db` can expose operator behavior beyond what should be tradable | default to exporting memory canon only; require opt-in session inclusion and aggressive redaction | `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md` |
| Cross-chain asymmetry | Base and Solana differ enough to fragment the protocol if one side dominates | keep chain adapters symmetric at the spec layer and push chain-specific logic to adapters | `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-D-prior-art.md`, `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/` |

## Highest-tension design choices

1. **Portability vs privacy** — every extra exported slot increases usefulness and risk at the same time.
2. **Forkability vs authorship control** — vessels are more valuable when they can be remixed, but that only works if derivative attribution is durable.
3. **Human-friendly onboarding vs strong provenance** — simplified buyer flows cannot erase signer identity, runtime installer identity, or source lineage.
4. **Cross-runtime ambition vs Hermes-first practicality** — the protocol should stay runtime-agnostic, but the first compatibility target is Hermes.

## Source paths

- `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/system-map.md`
- `/Users/rudlord/wiki/concepts/agent-memory-infrastructure.md`
- `/Users/rudlord/wiki/raw/reader/Keeping What's Yours in the Age of Autonomous Corporations (01jwfbnr0p3qzcd2xsdp8xsmxb).md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/billing/chains/`
