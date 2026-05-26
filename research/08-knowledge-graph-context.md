# 08 — Knowledge Graph Context

The wiki graph already contains a pre-HORCRX cluster. F01 does not need to invent the conceptual neighborhood; it needs to expose it clearly for the later spec workers.

## Graph facts

- `knowledge-graph.json` lives at `/Users/rudlord/wiki/.understand-anything/knowledge-graph.json`.
- The current graph snapshot is 8.5 MB, 89,230 lines, with 4,194 nodes and 2,253 edges according to `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-E-knowledge-graph.md`.
- The highest-signal HORCRX-adjacent nodes are already clustered around `atlas`, `atlas-corpus`, `atlas-marketplace`, `agent-memory-infrastructure`, and `hermes-agent`.

## ORBEL artifact contracts

The file `/Users/rudlord/wiki/_meta/orbel-framework/schemas/orbel-artifact-contracts.yaml` is the cleanest existing local schema surface for multi-agent handoff discipline. The key artifacts are `SourceRef`, `EvidenceItem`, `ResearchPacket`, `BuildBrief`, `EvaluationReport`, `LearningRecord`, and `HITLPackage`. Those contracts matter because a vessel pack is not just a pile of files; it is a set of roles exchanging typed artifacts.

## topic_key and registry implications

The mission library reports that `topic_key` coverage is still incomplete for this cluster. That means HORCRX should not treat itself as an isolated page or entity. It should enter the same canonical grouping discipline already used elsewhere in the wiki, with `/Users/rudlord/wiki/_meta/topic-key-registry.json` as the eventual registry touchpoint. This matters for later wiki promotion and for consistent retrieval.

## Honcho synthesis convention

The local synthesis pattern counts observations explicitly. That convention is visible in the pages cited by `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-E-knowledge-graph.md`, and it is worth inheriting because it turns high-level claims into auditable summaries rather than vibes.

## What later workers should take from this

1. Reuse the existing ATLAS cluster instead of inventing parallel terminology.
2. Keep provenance first-class; the ORBEL artifact contracts already encode this.
3. Treat `topic_key` and canonical-page registration as part of the protocol's discoverability surface, not as afterthought documentation chores.
4. Use the graph as evidence that HORCRX belongs inside an existing doctrine spine rather than beside it.

## Source paths

- `/Users/rudlord/wiki/.understand-anything/knowledge-graph.json`
- `/Users/rudlord/wiki/_meta/orbel-framework/schemas/orbel-artifact-contracts.yaml`
- `/Users/rudlord/wiki/_meta/topic-key-registry.json`
- `/Users/rudlord/wiki/queries/orbel-framework-operating-system-v2.md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-E-knowledge-graph.md`
