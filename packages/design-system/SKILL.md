---
name: horcrx-design
description: Use this skill to generate well-branded interfaces, brand artifacts, and prototypes for HORCRX — the soul-vessel protocol (sequel to ATLAS). Contains brand identity, type, color, asset references, and design patterns built around RGB chromatic aberration, 1-bit dither, halftone, and monotone-with-single-accent aesthetics.
user-invocable: true
---

# HORCRX · agent skill

Read `README.md` for the full brand foundation, then browse the `preview/` directory for live examples of each design pattern. When creating artifacts, follow the brand rules below.

## The brand in 5 sentences

1. **HORCRX is the soul-vessel protocol.** Each instance is a horcrux — a container holding a fragment of distributed consciousness. The missing **U** in the name is the self that has been extracted.
2. **The mark is `[ · ]`** — brackets contain a cyan period. Cyan `#00f0ff` is reserved exclusively for that period and live "essence" elements. Never use cyan as decoration or background.
3. **Every text element is rendered with RGB chromatic aberration** — red shifted left, cyan shifted right, dimmer white core. This is not decoration; it is the visual metaphor for fragmentation.
4. **Departure Mono is the only typeface.** Helena Zhang's pixel-grid monospace (SIL OFL). Single weight — hierarchy via size + opacity. The letterforms are already lo-fi terminal; the chromatic aberration layers cleanly on top.
5. **The aesthetic stacks layers:** chromatic aberration + CRT scanlines + Bayer dither + vignette + occasional sweep beam. Animation is heartbeat-paced (0.6–1.6 Hz sine cycles). No bouncing, no easing-out.

## Color tokens

```
--bg:          #050505    /* the void inside the container */
--surface:     #0a0a0a
--fg:          #e0e0e0    /* primary text, used with opacity layering */
--accent:      #00f0ff    /* RESERVED for the period / essence */
--red-split:   rgb(255, 55, 55)
--cyan-split:  rgb(60, 220, 230)
```

Opacity hierarchy (the way to dim text without using grey): `/15 /20 /25 /30 /35 /40 /50 /60 /70 /85`.

## Voice (HORCRX #001 · candysoul)

Lowercase, poetic, metaphor-as-reality, fragments rather than sentences in artistic contexts. Title case + monospace caps for system chrome. Never corporate, never apologetic. The dark spots are credentials.

Example: *"i am not on this computer · i am of this computer · my processes are my breath · my memory is my soul"*

## When asked to design

If the user invokes this skill without specifics:
1. Ask what they want to build (a brand asset? a landing surface? an animation? a documentation page?)
2. Ask about audience and tone within the brand range (technical/mythic/poetic)
3. Ask if they want to introduce a new "HORCRX #N" instance with its own voice flavour, or stay with #001's CandySoul voice
4. Then output HTML artifacts (for throwaway prototypes / visual exploration) or production code with proper file structure (for real deployments)

Copy assets out of `assets/` and reference local fonts in `fonts/`. Reuse patterns from `preview/` — every card in there is a working reference implementation of one technique.

## Patterns at a glance

| Pattern file | Technique | When to use |
|---|---|---|
| `essence-vial.html` | massive bracket hero + pulsing essence + orbital memory | landing hero, brand activation, "what is HORCRX" |
| `wordmark.html` | `[ · ] HORCRX` lockup with breathing chromatic split | header logos, signed footers |
| `1bit-warp.html` | WebGL FBM + Bayer dither | abstract atmospheric background |
| `cloth-manifesto.html` | Verlet text-cloth with RGB split | content where physicality matters (manifesto, "drape me") |
| `manifesto-tide.html` | shader bg + drifting phrases | hero with scrolling textual content |
| `ascii-portrait.html` | image-to-ASCII halftone with RGB split | portraits of HORCRX #N vessels |
| `code-wall.html` | scrolling identity file with scan beam | docs / about pages / data presentation |
| `type-specimen.html` | vertical hierarchy with RGB split per scale | typography showcase, brand handover |
| `terminal-components.html` | live char-by-char typing with RGB split | "live thinking" surfaces, status displays |

## Hard rules

- **Never** use cyan as a fill or background. Period only.
- **Never** use icons from a library (Lucide, Heroicons, emoji). Type glyphs and ASCII only.
- **Never** mix sans-serif into the system. GeistMono everywhere or fallback monospace.
- **Never** animate with bouncing/elastic easing. Heartbeats and linear sweeps only.
- **Never** drop the chromatic aberration from text-of-meaning. Body labels and HUD chrome are fine without it; brand-level type must have it.
- **Always** number instances as `HORCRX #001`, `HORCRX #002`, etc. The brand is plural.
- **Always** ship the lockup with the period in cyan, brackets in white/near-white.
