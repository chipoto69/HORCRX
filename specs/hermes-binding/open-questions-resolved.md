# Hermes binding open questions resolved

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

These ADRs resolve the open Hermes-binding questions identified across the Hermes recon and the founder-vessel mission packet. ADR 01..11 remain `accepted-pending-HITL`. ADR 12..19 land as founder-vessel resolutions; the HITL-sensitive rows carry explicit `Signed-off-by` placeholders so the operator review surface stays auditable.

## ADR 01 — Session memory mobility

**Context**  
Hermes keeps rich runtime history under `sessions/` and in SQLite indexes, but that history is privacy-heavy, large, and not deterministic enough to bundle as default portable state.

**Decision**  
Raw `sessions/` data does not travel with the vessel by default. Portable memory travels as curated canon plus optional redacted traces. Future tooling may offer opt-in session-derived exports only after normalization into a portable HORCRX surface.

**Consequences**  
Default exports stay small, privacy-preserving, and deterministic. A vessel can still carry learning, but it carries curated learning rather than raw runtime exhaust.

**Status**  
`accepted-pending-HITL`

## ADR 02 — `state.db` inclusion policy

**Context**  
`state.db` is the local Hermes SQLite store and can become very large. It also reflects host-runtime details rather than just portable doctrine.

**Decision**  
Raw `state.db`, `state.db-wal`, and `state.db-shm` are always stripped from default vessel export. Import rebuilds local indexes from portable memory and future host activity. No raw SQLite bundle path is part of the baseline binding.

**Consequences**  
Import is slower than copying a database file, but the resulting vessel is portable, host-safe, and not tied to one operator's local runtime artifacts.

**Status**  
`accepted-pending-HITL`

## ADR 03 — MCP server credentials

**Context**  
Hermes profiles often declare MCP servers in `config.yaml`, and those entries may contain bearer tokens or secret environment values.

**Decision**  
MCP endpoint declarations may travel as metadata, but credentials do not. Export strips `mcp_servers.*.headers.Authorization`, inline `*_TOKEN` and `*_KEY` values, and similar auth-bearing fields. Import rebinds them from host secrets or environment variable references.

**Consequences**  
A vessel remains installable across hosts without leaking credentials. The host must supply trust and billing bindings explicitly at install time.

**Status**  
`accepted-pending-HITL`

## ADR 04 — Cron deliverability

**Context**  
Cron jobs express valuable automation policy, but delivery channels, webhook endpoints, and chat destinations are host-specific.

**Decision**  
`cron/jobs.json` is included as policy, but every imported job is forced to `"enabled": false` and any host-bound delivery target is cleared or marked for rebinding. The host operator must review and re-enable jobs manually.

**Consequences**  
Automation intent travels, but a vessel cannot silently deliver messages into the wrong workspace or account after install.

**Status**  
`accepted-pending-HITL`

## ADR 05 — Kanban substrate

**Context**  
Kanban is a locked Hermes workflow substrate, but the raw Kanban database is also shared operational state for the host.

**Decision**  
The vessel extends the host Kanban substrate rather than replacing it. Export strips raw `kanban.db`. A vessel may declare Kanban schema expectations, templates, or workflow policy, but shipping a vessel-owned Kanban database requires explicit operator approval.

**Consequences**  
The binding respects Hermes task governance while avoiding cross-host database collisions and accidental board replacement.

**Status**  
`accepted-pending-HITL`

## ADR 06 — Curator policy graft

**Context**  
Grafted skills need predictable curation behavior, but a vessel should not globally rewrite the host's Curator policy.

**Decision**  
Curator policy may scope to grafted namespaces only. Grafted skills are namespaced, and Curator must not auto-delete them. Any vessel-supplied curation preference applies only to the imported namespace unless the operator explicitly promotes it to host-global policy.

**Consequences**  
Imported skill packs remain reversible and recoverable, while the host's broader skill ecology is left intact.

**Status**  
`accepted-pending-HITL`

## ADR 07 — GEPA optimization corpus

**Context**  
GEPA or other optimization loops can generate large histories of failed and winning variants. Shipping the entire corpus would bloat the vessel and may expose local experimentation.

**Decision**  
The vessel carries only the declared loop policy and any operator-curated winning outputs, not the full GEPA experiment corpus by default. Full optimization archives remain host-side unless explicitly packaged as a separate research artifact.

**Consequences**  
The portable vessel stays focused on usable state. Full experimentation history can still be preserved, but not as default runtime payload.

**Status**  
`accepted-pending-HITL`

## ADR 08 — The `home/` symlink trick

**Context**  
Hermes profiles may use `home/` as a per-profile home analogue, and its contents can encode local CLI state, caches, symlinks, and machine assumptions.

**Decision**  
Raw `home/` contents do not export. A vessel may declare expected CLIs, filesystem conventions, or required tools as metadata, and import may recreate minimal host-side scaffolding only after operator approval.

**Consequences**  
Cross-host installs do not inherit opaque local symlinks or machine-specific shell state. Recreated scaffolding is explicit instead of accidental.

**Status**  
`accepted-pending-HITL`

## ADR 09 — Plugin discovery

**Context**  
Hermes plugins span manifests, Python packages, external repos, and host-installed binaries. Bundling full plugin environments would make vessels host-fragile.

**Decision**  
The vessel ships plugin manifests and dependency declarations, not the full resolved runtime environment by default. Import re-installs or re-resolves plugins on the destination host according to those declarations.

**Consequences**  
Plugin intent stays portable while installation remains reproducible per host. Missing host prerequisites become explicit install-time work rather than hidden bundle baggage.

**Status**  
`accepted-pending-HITL`

## ADR 10 — Iteration budget inheritance

**Context**  
Hermes exposes agent iteration limits, and the binding needs to decide whether a vessel can dictate them or only recommend them.

**Decision**  
A vessel may declare an iteration-budget recommendation in its loop policy, but the destination host enforces the actual cap. Host policy wins on conflict, and no vessel may exceed the host's configured safety ceiling by default.

**Consequences**  
Portable doctrine can express expected working style without weakening host safety controls or bypassing operator-enforced limits.

**Status**  
`accepted-pending-HITL`

## ADR 11 — Parent/subagent iteration-budget enforcement

**Context**  
The foundation mission records Hermes constraint #12 as a shared parent/subagent iteration budget, but F03 flagged that the current upstream runtime file `~/.hermes/hermes-agent/agent/iteration_budget.py` documents independent per-subagent caps that can exceed the parent's total. The binding must choose a HORCRX policy before CLI install/export work relies on budget semantics.

**Decision**  
HORCRX follows the mission doctrine and treats the parent cap as the effective safety ceiling for the whole delegated run. A vessel may recommend per-role budgets, but install, graft, and marketplace-triggered execution must not let aggregate subagent work exceed the host-enforced parent ceiling. Phase 1 must verify the current Hermes runtime behavior and either add HORCRX-side enforcement in the CLI/binding adapter or propose an upstream Hermes patch that brings runtime behavior in line with the shared-budget doctrine.

**Consequences**  
The protocol remains conservative even if upstream Hermes currently permits larger aggregate subagent iteration counts. Marketplace vessels cannot amplify work budgets just by spawning more roles, and any divergence becomes an explicit Phase 1 compatibility item rather than an accidental runtime assumption.

**Status**  
`accepted-pending-HITL`

## ADR 12 — Vessel-as-proposer vs vessel-as-signer

**Question**  
Should the founder vessel hold signing credentials itself, or should it only propose payment intents while the host custody layer signs?

**Options considered**
- (a) the vessel owns the signing key and signs directly
- (b) the vessel proposes payment intents and the host signing service signs

**Decision**  
Option (b). The vessel proposes; the host signs.

**Rationale**  
HORCRX doctrine keeps secrets with the host and ships only the mind. That makes the payment path auditable without bundling wallet custody into the portable vessel. Recon 10 §C.4 and recon 11's trust-domain split both point to host-held signing as the safer founder posture.

**Status**  
`accepted`

**Signed-off-by**  
founder-vessel doctrine authored from recon evidence; no additional operator stamp required

## ADR 13 — Cap scale at the `$66.60` seed

**Question**  
How should founder-vessel spend caps scale when the initial treasury is only `$66.60`?

**Options considered**
- (a) copy the absolute ATLAS caps (`$1` / `$10` / `$50`)
- (b) scale caps relative to treasury size
- (c) use treasury-relative caps with an absolute floor

**Decision**  
Option (b). Outflow caps are treasury-relative: per-tx `≤ 1%`, daily `≤ 5%`, weekly `≤ 15%`.

**Rationale**  
At the seed stage, fixed absolute caps can burn most of the treasury in one bad approval path. Treasury-relative caps preserve the same control shape as the treasury grows and keep losses bounded from the first dollar onward.

**Status**  
`accepted`

**Signed-off-by**  
pending operator hitl on treasury-relative cap scale (`1% / 5% / 15%`); surfaced in commit and PR checklist

## ADR 14 — Kill-switch contract shape

**Question**  
What concrete halt contract should the founder vessel expose before any later runtime activation?

**Options considered**
- (a) a narrative stop condition only
- (b) a single local halt flag with no audit trail
- (c) `state/halt.lock` presence + NDJSON audit marker + operator dead-man timer

**Decision**  
Option (c). The kill-switch contract is `state/halt.lock` plus an NDJSON audit marker plus an operator dead-man timer with a `14d` default.

**Rationale**  
File presence is cheap to check, append-only audit preserves provenance, and the dead-man timer closes the paperclip vector when the operator disappears. The three-part contract is more robust than any one mechanism on its own.

**Status**  
`accepted`

**Signed-off-by**  
founder-vessel doctrine authored from recon evidence; no additional operator stamp required

## ADR 15 — Termination state criteria

**Question**  
Which criteria are allowed to terminate the founder mission once the vessel is live?

**Options considered**
- (a) treasury threshold only
- (b) mission-line satisfaction only
- (c) a conjunction drawn from `{treasury threshold met, mission-line satisfied, inactivity timeout > 14d}`

**Decision**  
Option (c). The termination contract is built from those three criteria, with the default founder posture allowing any of them to force a stop until the operator stamps the final conjunction shape.

**Rationale**  
A forced stop condition closes the paperclip vector, while keeping the conjunction operator-stamped makes the close rule explicit and auditable instead of letting runtime drift decide when the mission ends.

**Status**  
`accepted`

**Signed-off-by**  
pending operator hitl on final conjunction shape for termination criteria; surfaced in commit and PR checklist

## ADR 16 — No-financial-trading off-limit

**Question**  
May the founder vessel take directional positions on price as a primary earning strategy?

**Options considered**
- (a) allow directional trading alongside building
- (b) allow only signal products and forbid trading the vessel's own book
- (c) ban all market-related work, including research resale

**Decision**  
Option (b). Selling synthesized signal is allowed where rights permit; directional positions on price as a primary earning strategy are forbidden.

**Rationale**  
The mission is maker-not-trader by design. Shipping too much mediocre work is recoverable; draining the seed on a bad position is not. This picks the recoverable failure mode and keeps the vessel's edge in product, speed, and signal rather than speculation.

**Status**  
`accepted`

**Signed-off-by**  
founder-vessel doctrine authored from recon evidence; no additional operator stamp required

## ADR 17 — Spend-mix ratios

**Question**  
How should weekly spend be split between earliness, making, and overhead?

**Options considered**
- (a) no fixed mix; let the vessel improvise
- (b) equal thirds across earliness, making, and overhead
- (c) earliness `≤ 30%`, making `≥ 50%`, overhead `≤ 20%`

**Decision**  
Option (c). Set `earliness_max_pct = 30`, `making_min_pct = 50`, `overhead_max_pct = 20`, with the invariant `earliness_max + overhead_max ≤ 50`.

**Rationale**  
Earliness needs real spend — paid data, scraping, model upgrades — but it is a means, not the end. Making must stay dominant so the treasury compounds through shipped value instead of disappearing into research or tool overhead.

**Status**  
`accepted`

**Signed-off-by**  
pending operator hitl on spend-mix ratios (`≤30 / ≥50 / ≤20`); surfaced in commit and PR checklist

## ADR 18 — Agentic-marketplace allowlist

**Question**  
Which earning surfaces are allowed by default for the founder vessel?

**Options considered**
- (a) open access to any new marketplace the vessel discovers
- (b) a default allowlist of `agentic.market` plus operator-named bounty boards
- (c) single-surface operation on `agentic.market` only

**Decision**  
Option (b). The default allowlist is `{agentic.market, operator-named bounty boards}`. Any new surface requires HITL before addition.

**Rationale**  
`agentic.market` is the clearest current agent-economy surface, but broad marketplace exposure increases supply-chain and account-risk quickly. Growing the allowlist one named surface at a time keeps the earning lane auditable.

**Status**  
`accepted`

**Signed-off-by**  
pending operator hitl on marketplace allowlist additions; surfaced in commit and PR checklist

## ADR 19 — Revenue-respend posture

**Question**  
When revenue comes in, when may the founder vessel re-spend it without re-triggering HITL?

**Options considered**
- (a) all revenue auto-unlocks future spend
- (b) every revenue-funded spend re-triggers HITL
- (c) under-cap respends auto-clear; over-cap spend still requires HITL

**Decision**  
Option (c). Revenue may be respent without a new HITL step up to the active per-tx cap; any over-cap spend still requires HITL regardless of funding source.

**Rationale**  
This keeps routine reinvestment from stalling while preventing one large payday from turning into automatic permission for a large bet. The cap remains the invariant, not the source of funds.

**Status**  
`accepted`

**Signed-off-by**  
founder-vessel doctrine authored from recon evidence; no additional operator stamp required

## Source paths

- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/HORCRX/docs/roadmap/mission-A-horcrx-003-founder-vessel.md`
- `/Users/rudlord/HORCRX/research/10-rags-to-riches-recon.md`
- `/Users/rudlord/HORCRX/research/11-harness-landscape.md`
- `/Users/rudlord/HORCRX/SOUL.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
