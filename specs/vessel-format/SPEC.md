# HORCRX Vessel Format Specification

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

This specification defines the two canonical representations of a HORCRX vessel:

1. **working format** — a folder a runtime or operator edits directly;
2. **bundle format** — a signed, content-addressed `.horcrx` artifact for exchange, sale, fork, and archival.

The vessel format is intentionally shaped as a strict superset of the Hermes profile layout documented in `/Users/rudlord/.hermes/profiles/` and summarized in `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`.

## 1. Design goals

- Preserve the **SOUL.md / AGENTS.md** split already enforced by Hermes and ORBEL.
- Extend, not replace, the AgentCard model at `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`.
- Keep the abstract vessel format chain-agnostic.
- Make folder ↔ bundle round-trips deterministic.
- Separate **mind** from **secrets** so the bundle never ships host credentials.

## 2. Canonical representations

### 2.1 Working format: vessel folder

A single vessel is a directory named `horcrx-<catalog-id>/`.
A pack is a directory named `horcrx-<catalog-id>-pack/` with one or more child vessels.

```text
horcrx-001-candysoul/
├── soul.md
├── agents.md
├── principles.md
├── intuition.md
├── dreams.md
├── voice.md
├── manifest.json
├── mark.svg
├── skills/
│   └── <skill>/SKILL.md
├── plugins/
├── workflows/
├── crons/
│   └── jobs.json
├── traces/
│   └── *.ndjson
├── memory/
│   ├── canon.md
│   └── grafts/
└── multi-agent.yaml        # pack only
```

### 2.2 Bundle format: `.horcrx`

A `.horcrx` bundle is a deterministic tar archive compressed with zstd. It contains:

- the normalized working tree,
- `manifest.json` as the bundle index,
- detached per-slot signatures,
- optional encrypted envelopes for redacted slot bodies,
- no runtime-only caches, no raw credentials, and no host-local locks.

A bundle filename SHOULD follow:

```text
horcrx-<catalog-id>--<manifest-cid>.horcrx
```

## 3. Required files and slots

### 3.1 Identity and control plane

- `soul.md` — identity only; no commands, paths, or workflow instructions.
- `voice.md` — required identity cadence: mission line, tone notes, and optional sample passages.
- `agents.md` — operational contract, task routing, and safety gates.
- `manifest.json` — canonical bundle index and capability declaration.
- `mark.svg` — optional identity mark for catalog surfaces.

### 3.2 Cognitive slots

- `principles.md` — stable doctrine or values that are not pure persona.
- `intuition.md` — decision heuristics and edge-case instincts.
- `dreams.md` — dream-cycle or wake-cycle reflection summaries.
- `memory/canon.md` — portable, curated memory that may safely travel.
- `memory/grafts/` — imported memory sidecars from other vessels.
- `traces/*.ndjson` — redacted episodic traces suitable for audit or replay.

### 3.3 Procedural slots

- `skills/<name>/SKILL.md` — Anthropic-compatible skill packets.
- `plugins/` — manifests only by default; dependency payloads are optional.
- `workflows/` — declarative workflow definitions.
- `crons/jobs.json` — schedule policy, always disabled on import until approved.
- `multi-agent.yaml` — pack-only role graph for multi-vessel systems.

### 3.4 Founder-class slots (required for vessels with kind="founder", reserved otherwise)

- `mission.md` — the vessel's mission arc, seed amount, success ladder, abort criteria, termination state.
- `ledger.md` — declarative treasury posture: spend knobs, earn knobs, spend-mix ratios, custody posture.
- `autonomy.md` — HITL ladder, kill-switch contract, ASI rung, no-trading invariant.
- `constraints.md` — (optional) non-negotiable invariants beyond `autonomy.md`.

## 4. Folder invariants

1. Paths are UTF-8, slash-separated, and case-sensitive.
2. Identity-only files (`soul.md`, `voice.md`) MUST remain identity only and MUST NOT contain shell commands, host paths, or executable strings.
3. `agents.md` MAY contain commands, paths, and execution policy.
4. `skills/` preserves Anthropic `SKILL.md` syntax exactly.
5. `memory/canon.md` is portable; raw session stores are not.
6. `manifest.json` is the only authoritative index for bundle assembly.

## 5. Bundle assembly rules

The folder is canonical for editing. The bundle is canonical for trade.

### 5.1 Canonical serialization

To guarantee the same input yields the same CID:

1. Normalize all text files to UTF-8 with LF line endings.
2. Sort archive entries by bytewise ascending relative path.
3. Omit filesystem metadata that varies across hosts.
4. Set tar header `uid=0`, `gid=0`, `uname=''`, `gname=''`, `mtime=0`.
5. Use octal file modes `0644` for files, `0755` for directories, `0644` for SVG assets, and preserve executable bits only for declared scripts.
6. Serialize JSON with sorted keys and two-space indentation.
7. Compress the tar stream with zstd at a fixed level.
8. Compute the manifest CID from the uncompressed canonical tar byte stream.

These rules define the deterministic round-trip required by `VAL-VESSEL-14`.

### 5.2 Encrypted envelopes

A slot MAY be replaced in the bundle payload by an encrypted envelope when:

- the slot is licensed but not publicly readable,
- the slot is privately shared with a buyer,
- the slot contains operator-sensitive memory that is portable only under explicit consent.

An encrypted envelope contains:

- `cipher_suite`,
- `recipient_key_ids`,
- `ciphertext_cid`,
- `plaintext_digest`,
- optional `policy_uri`.

The manifest still exposes that the slot exists, but not its plaintext body.

## 6. Packs vs single vessels

A **single vessel** carries one persona/runtime package.
A **pack** carries multiple child vessels plus a task graph.

A pack MUST add:

- `kind: "pack"` in `manifest.json`,
- `multi-agent.yaml`,
- `pack.entrypoint`,
- `pack.members[]`,
- `pack.task_graph[]` edges between member IDs.

The ORBEL templates at `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/` are the reference local shape for packs.

## 7. Export and import posture

This spec does not redefine Hermes export/import commands; that binding belongs to F03. It does, however, reserve the following expectations:

- export strips `.env`, auth tokens, raw `state.db`, session logs, and host-local caches;
- import rehydrates secrets from the host, not from the vessel;
- pack members remain independently signable.

## 8. Example vessels

Reference examples live at:

- `/Users/rudlord/HORCRX/examples/horcrx-001-candysoul/`
- `/Users/rudlord/HORCRX/examples/horcrx-002-orbel-pack/`

`HORCRX #001 · candysoul` is the single-vessel reference.
`HORCRX #002 · orbel-pack` is the multi-vessel reference.

## 9. Source paths

- `/Users/rudlord/HORCRX/research/01-lineage.md`
- `/Users/rudlord/HORCRX/research/06-local-modules-inventory.md`
- `/Users/rudlord/HORCRX/research/07-skill-ecosystem-inventory.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/.claude-worktrees/ATLAS/knowledge-horcrux/atlas/agents/framework/agent_card.py`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
