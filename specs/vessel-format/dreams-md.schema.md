# `dreams.md` schema

Version: `v0.1-draft`

`dreams.md` is a portable reflection slot for wake-cycle synthesis. It is not a raw session dump. It is the compressed record of what the vessel thinks mattered after work.

## Purpose

- preserve recurring themes without exporting every transcript,
- capture pattern recognition that should survive host migration,
- keep dream-cycle material separate from operational memory canon.

## Required fields

```markdown
# dreams

## cycle_id
- unique label for the reflection window

## observed_patterns
- repeated motifs, tensions, or opportunities

## unresolved_pull
- what still feels open after the cycle ends

## proposed_mutations
- candidate skill, memory, or doctrine changes

## keep_discard_defer
- what should persist, what should be dropped, what should wait

## witness
- who or what validated the reflection
```

## Constraints

1. Do not embed secrets.
2. Do not embed full raw chat logs.
3. Reference traces by CID or relative path instead of copying them inline.
4. Prefer one reflection per cycle or per day.

## Recommended metadata

- `created_at`
- `source_traces[]`
- `confidence`
- `consent_scope`

## Local source paths

- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
