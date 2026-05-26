# `intuition.md` schema

Version: `v0.1-draft`

`intuition.md` captures portable heuristics: the short-form edge the vessel has earned but cannot cleanly express as a formal rule engine.

## Purpose

- preserve decision heuristics across runtime migration,
- distinguish durable instincts from situational notes,
- make hidden operating assumptions inspectable.

## Required fields

```markdown
# intuition

## heuristic_catalog
- name
- trigger
- preferred_response
- risk_if_wrong

## edge_cases
- scenario
- why default logic fails
- override

## trust_weights
- which evidence sources are favored and why

## anti_patterns
- situations where the intuition should be ignored
```

## Rules

1. Every heuristic must be explainable to another operator.
2. Intuition may be compact, but it cannot be mystical handwaving.
3. If a heuristic depends on hidden credentials or a private host setup, it belongs in host config, not in `intuition.md`.
4. Tie unusual heuristics back to evidence or lived failure when possible.

## Local source paths

- `/Users/rudlord/HORCRX/research/04-economic-thesis.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/HORCRX_Design_System/VOICE.md`
