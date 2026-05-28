# `voice.md` schema

Version: `v0.1-draft`

`voice.md` is the vessel's identity cadence. It exists so the vessel can declare a local mission line and persona overlay without duplicating the full HORCRX voice canon.

## Purpose

- pin the vessel's three-verb directive,
- state the local persona overlay inside the inherited `VOICE.md` format,
- optionally carry short sample passages for catalog or audit surfaces.

## Required fields

| field | requirement |
|---|---|
| `mission_line` | first non-heading line near the top; lowercase; format `<verb> through <noun> · <verb> through <noun> · <verb> through <noun>` |
| `tone_notes` | 1–6 short lines describing register, pressure, and persona overlay within the inherited voice format |

## Optional fields

| field | use |
|---|---|
| `sample_passages` | short examples that prove the local voice without repeating the global canon |

## Validation rules

1. `voice.md` MUST stay identity only — no shell commands, no host paths, no executable strings.
2. The mission line MUST appear once, as a single line, near the top of the file.
3. The mission line MUST stay lowercase aside from preserved brand names or catalog refs.
4. `tone_notes` SHOULD stay compact; this slot is a local overlay, not a duplicate of `packages/design-system/VOICE.md`.
5. Sample passages MAY be prose or quoted blocks, but they MUST preserve the inherited lowercase-first posture.

## Minimal outline

```markdown
# voice

earn through making · move through earliness · compound through audit

## tone_notes
...
...
```

## Local source paths

- `/Users/rudlord/HORCRX/packages/design-system/VOICE.md`
- `/Users/rudlord/HORCRX/SOUL.md`
- `/Users/rudlord/HORCRX/research/10-rags-to-riches-recon.md`
