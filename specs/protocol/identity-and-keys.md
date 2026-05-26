# Identity and keys

Version: `v0.1-draft`

HORCRX separates author identity, owner authority, and runtime delegation.

## 1. Identity layers

- **author key** — signs the vessel manifest and authored slots;
- **owner key** — controls listing, transfer, and revocation state;
- **runtime delegated key** — lets an agent act within bounded permissions;
- **attester key** — signs trust or compatibility attestations.

A single human or organization may hold more than one of these roles, but the protocol does not collapse them into one assumption.

## 2. DID strategy

Every vessel SHOULD expose a DID-compatible identifier for human-readable identity projection. The protocol does not require one DID method, but it does require:

- stable identifier syntax,
- a way to rotate keys,
- a way to associate the DID document with the current author or owner key set.

## 3. Agent-as-signer

The AgentCard model already includes `AgentCredentials`, `allowed_executors`, and bounded autonomy surfaces at `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`. HORCRX uses that shape to allow **delegated agent signing** when:

- the owner explicitly grants a delegated key,
- the delegation scope is recorded,
- the runtime action is auditable,
- the delegated key cannot silently replace the owner key.

## 4. Key rotation

Rotation must support:

1. author-key rollover without losing lineage,
2. owner-key rollover after custody changes,
3. delegated-key expiry and revocation,
4. historical verification of old signatures after new keys are introduced.

Rotation is modeled as a signed registry or DID update, not as destructive mutation of the historical vessel manifest.

## 5. SAID federation

The local stack already includes SAID identity work under `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`. HORCRX should remain compatible with that federation model so a vessel can expose:

- a protocol-native manifest signer,
- an optional SAID-linked external identity,
- marketplace trust signals anchored to the federated identity.

## 6. Source paths

- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/identity/`
- `/Users/rudlord/HORCRX/research/01-lineage.md`
- `/Users/rudlord/HORCRX/research/02-prior-art.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
