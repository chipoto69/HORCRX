# Memory split

Version: `v0.1-draft`

HORCRX memory is intentionally split so portable identity and learning can travel without dragging along every host-local, private, or runtime-only substrate.

## Three classes of memory

1. **portable canon** — human-curated memory safe to export.
2. **ephemeral session memory** — runtime history useful locally but too bulky or private by default.
3. **host-bound secrets and integrations** — credentials and live bindings that must never ship.

## Include / strip / re-inject matrix

| Surface | Class | Export rule | Import rule | Notes |
|---|---|---|---|---|
| `memory/canon.md` | portable canon | include | merge or replace per host policy | primary portable memory surface |
| `memory/grafts/*.md` | portable canon | include with provenance | materialize as sidecars | preserves foreign graft boundaries |
| `memories/MEMORY.md` summary | portable canon | include | merge into canon view | Hermes-compatible summary form |
| `memories/USER.md` | portable canon, consent-sensitive | include only with explicit consent | import behind operator review | may expose human preference modeling |
| `traces/*.ndjson` | semi-portable evidence | include if redacted | append to trace store | never a substitute for canon |
| `sessions/` | ephemeral | strip by default | optional later hydration path | too heavy and privacy-sensitive |
| `state.db` / FTS indexes | ephemeral | strip by default | rebuild locally from imported canon/traces | deterministic portability is not assumed |
| `logs/` | ephemeral | strip | do not restore | audit mirrors belong to host policy |
| Honcho peer state | ephemeral external | strip | reconnect to host peer if configured | single-provider rule remains host-owned |
| GBrain / shared memory bindings | host-bound | strip credentials, keep manifest only | rebind via host config | preserve boundary between local and shared memory |
| MCP credentials | host-bound | strip | re-inject from host secret store | MCP endpoints may be declared without secrets |
| `.env`, `auth.json`, wallet secrets | host-bound | strip always | rehydrate from host only | mind != secrets |

## MCP note

MCP server declarations may travel as metadata, but MCP tokens, headers, and API secrets do not. The vessel carries **what** it expects to talk to, not **how** to authenticate.

## Local source paths

- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/08-knowledge-graph-context.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/wiki/concepts/agent-memory-infrastructure.md`
- `/Users/rudlord/wiki/raw/downloads/2026-04-10/root/system-map.md`
