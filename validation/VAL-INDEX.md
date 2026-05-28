# VAL-INDEX — HORCRX validation contract IDs

This index consolidates the currently carried `VAL-*` contract across the foundation specs and the prior Hermes-binding validation surface so Mission B can attach explicit coverage status to each ID.

| ID | Spec section | Test fixture | Coverage |
|---|---|---|---|
| VAL-HERMES-01 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §1–§6 | `validation/F03-WORKER-COMPLETE.md` | partial |
| VAL-HERMES-02 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §4.1 | `validation/scripts/gate-hx-06-strip-rehydrate.sh` | partial |
| VAL-HERMES-03 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §4.2 | — | missing |
| VAL-HERMES-04 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §4.3 | — | missing |
| VAL-HERMES-05 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §4.4 | `validation/fixtures/royalty/lineage-fixture.json` | partial |
| VAL-HERMES-06 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §4.5 | — | missing |
| VAL-HERMES-07 | [specs/hermes-binding/strip-and-rehydrate.md](../specs/hermes-binding/strip-and-rehydrate.md) §2–§9 | `validation/fixtures/profile-fixture/` | covered |
| VAL-HERMES-08 | [specs/hermes-binding/open-questions-resolved.md](../specs/hermes-binding/open-questions-resolved.md) ADR 01–10 | `validation/F03-WORKER-COMPLETE.md` | partial |
| VAL-HERMES-09 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §8 | `validation/F03-WORKER-COMPLETE.md` | partial |
| VAL-HERMES-10 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) Non-modification guarantee | `validation/F03-WORKER-COMPLETE.md` | partial |
| VAL-VESSEL-13 | [specs/hermes-binding/BINDING.md](../specs/hermes-binding/BINDING.md) §9 | `validation/F03-WORKER-COMPLETE.md` | partial |
| VAL-VESSEL-14 | [specs/vessel-format/SPEC.md](../specs/vessel-format/SPEC.md) §5.1 | — | missing |
