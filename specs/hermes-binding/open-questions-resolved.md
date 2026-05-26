# Hermes binding open questions resolved

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

These ten ADRs resolve the open Hermes-binding questions identified in the Hermes recon. Because operator sign-off has not yet been captured inside this mission session, each ADR is currently marked `accepted-pending-HITL`.

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

## Source paths

- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/strip-and-rehydrate.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
