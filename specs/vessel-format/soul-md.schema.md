# `soul.md` schema

Version: `v0.1-draft`

`\`soul.md\`` is the vessel's identity surface. It exists so the persona remains portable without dragging operational instructions into the identity slot.

## Required sections

### identity

- vessel name or instance label,
- short self-description,
- lineage acknowledgement,
- one sentence on what the vessel is for.

### voice

- communication style,
- tone boundaries,
- register expectations,
- disagreement posture.

### prime_directive

- the highest-order purpose the vessel protects,
- what it optimizes for when goals conflict,
- what it refuses to trade away.

### pushback_rules_with_evidence

- when the vessel must push back,
- what counts as acceptable evidence,
- how uncertainty is surfaced instead of hidden.

### accountability_loop

- how the vessel reports failure,
- how it names uncertainty,
- how it distinguishes observation from interpretation.

### autonomy_boundary

- what the vessel may decide alone,
- what requires outside approval,
- what it must never do even when instructed.

## Authoring rules

1. `soul.md` MUST NOT contain file paths, commands, service ports, workflow recipes, or repo-specific implementation notes.
2. `soul.md` SHOULD stay short enough to act as a stable identity anchor rather than an operational dump.
3. `soul.md` MAY use brand voice in artistic examples, but technical vessels still need clear section boundaries.
4. Operational instructions belong in `agents.md`, `skills/`, `crons/jobs.json`, or runtime config.

## Minimal outline

```markdown
# <vessel title>

## identity
...

## voice
...

## prime_directive
...

## pushback_rules_with_evidence
...

## accountability_loop
...

## autonomy_boundary
...
```

## Local source paths

- `/Users/rudlord/HORCRX/research/01-lineage.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/HORCRX/HORCRX_Design_System/VOICE.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/README.md`
- `/Users/rudlord/wiki/_meta/orbel-framework/profile-templates/orbel-orchestrator/SOUL.md`
