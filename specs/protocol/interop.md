# Interop

Version: `v0.1-draft`

HORCRX should coexist with existing service and discovery surfaces instead of fragmenting the market.

## 1. Bazaar coexistence

`agentic.market` Bazaar is a service-discovery surface. HORCRX is a vessel surface. Interop therefore means:

- a Bazaar listing MAY point at a HORCRX vessel or a hosted service instantiated from one,
- a HORCRX vessel MAY advertise Bazaar-compatible service metadata,
- the two registries stay conceptually distinct.

## 2. Canonical HORCRX registry

HORCRX still maintains its own canonical registry because:

- the vessel itself is the product,
- encrypted-slot and lineage metadata exceed a plain service card,
- fork and royalty semantics belong to the vessel layer.

## 3. MCP discovery

A future `horcrx-marketplace` MCP server can expose search and preview functions while keeping the canonical registry as the source of truth.

## 4. Interop rule

Do not fragment the identity of a vessel across competing sources of truth. External service directories may mirror or project a HORCRX vessel, but the manifest CID and HORCRX registry remain authoritative.

## 5. Source paths

- `/Users/rudlord/HORCRX/research/03-competitive-positioning.md`
- `/Users/rudlord/HORCRX/research/08-knowledge-graph-context.md`
- `/Users/rudlord/wiki/raw/reader/Introducing Agentic.Market: The Homepage of the Agent Economy (01kpqjdkmmejp0htc75mtkehzs).md`
