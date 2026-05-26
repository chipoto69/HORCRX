# Hermes export strip-and-rehydrate rules

Version: `v0.1-draft`

ATLAS → CORPUS → HORCRX.

This document defines the exact export and import treatment for Hermes profile surfaces when producing or installing a HORCRX vessel.

## 1. Rule classes

- **include** — serialize into the vessel by default.
- **strip** — never serialize the raw surface into the vessel.
- **re-inject from host** — export strips the surface; import restores it from host secrets, host configuration, or operator action.
- **require operator decision** — export or import pauses for explicit operator approval because the surface mixes portability with privacy, billing, or host-coupling risk.

## 2. Exact rules by surface

| Surface | Export rule | Import / install rule | Notes |
|---|---|---|---|
| `SOUL.md` | include verbatim | materialize verbatim in the new profile | identity surface only |
| `AGENTS.md` | include when present | materialize verbatim in the new profile | operational contract stays separate from `SOUL.md` |
| `config.yaml` | include after redaction | write redacted file, then rebind host-only fields | preserve model/provider/toolset policy without shipping secrets |
| `.env` | strip | re-inject from host only | never ship raw `.env` content in a vessel |
| `auth.json` | strip | re-inject from host only, usually by symlink or host-local copy | preserves shared operator identity without export |
| `auth.lock` | strip | regenerate on first auth touch if needed | runtime sidecar only |
| `memories/MEMORY.md` | include | merge into portable canon or write as Hermes summary | portable canon |
| `memories/USER.md` | include only with explicit consent | import behind operator review | consent-sensitive user modeling |
| `skills/**/SKILL.md` and referenced local skill assets | include | materialize into profile-local `skills/` | keep Anthropic packet format unchanged |
| `state.db` | strip | rebuild locally from imported canon, traces, and future host activity | raw SQLite store does not travel by default |
| `state.db-wal` | strip | do not restore | transient SQLite sidecar |
| `state.db-shm` | strip | do not restore | transient SQLite sidecar |
| `sessions/` | strip by default | optional later hydration only via normalized trace/session import, never by raw directory copy on default install | privacy-heavy and non-deterministic |
| `home/` | strip | recreate host-side scaffolding only after operator approval | vessel may declare expected CLIs, but not ship the host home contents |
| `gateway.lock` | strip | do not restore | runtime lock |
| `gateway.pid` | strip | do not restore | runtime PID file |
| `gateway_state.json` | strip | regenerate on first gateway start | runtime state |
| `processes.json` | strip | regenerate from the new host runtime | process inventory is host-local |
| `cache/` | strip | do not restore | host cache |
| `audio_cache/` | strip | do not restore | host cache |
| `image_cache/` | strip | do not restore | host cache |
| `pastes/` | strip | do not restore | host-local artifact cache |
| `logs/*` | strip by default | do not restore by default | `--include-audit` may export redacted audit evidence only |
| `cron/jobs.json` | include | install with every job forced to `"enabled": false`; host must rebind delivery targets before activation | policy travels, live delivery binding does not |
| `cron/output/**` | strip | do not restore | prior run outputs are runtime artifacts, not portable doctrine |
| `kanban.db` | require operator decision; default strip | default is host-extend, not vessel-owned replacement | task substrate is canonical but usually host-owned |
| `plugins/` manifest entries | include manifest metadata only | re-install or re-resolve plugins on host | do not ship opaque host environments by default |
| `mcp_servers.*.headers.Authorization` in `config.yaml` | strip | re-inject from host secret store or environment variable reference | never ship bearer tokens |
| `mcp_servers.*.env.*_TOKEN`, `mcp_servers.*.env.*_KEY`, `model.api_key`, `*.access_token_env` in `config.yaml` | strip or replace with host variable reference | host rebind required on import | preserve integration intent, not secrets |

## 3. Config redaction rules

Export retains these `config.yaml` categories:

- model/provider routing that does not embed secrets;
- toolsets, skills, plugins, and agent policy surfaces;
- cron policy fields;
- non-secret MCP endpoint metadata.

Export strips or rewrites these categories:

- secret-bearing headers such as `mcp_servers.*.headers.Authorization`;
- inline secret env values such as `*_TOKEN`, `*_KEY`, and `model.api_key`;
- host-specific process state;
- any field whose only meaning is local authentication rather than portable capability.

Recommended rewrite form on export:

```yaml
mcp_servers:
  horcrx-marketplace:
    headers:
      Authorization: ${HOST_HORCRX_MARKETPLACE_TOKEN}
```

The placeholder documents the required host binding without serializing the actual token.

## 4. Runtime and cache surfaces

The following surfaces are always treated as host-local runtime state and are never part of a default vessel:

- `state.db`, `state.db-wal`, `state.db-shm`
- `sessions/`
- `home/`
- `gateway.lock`, `gateway.pid`, `gateway_state.json`
- `processes.json`
- `cache/`, `audio_cache/`, `image_cache/`, `pastes/`
- `cron/output/`

If future tooling offers partial export for some of these classes, it must normalize them into a portable HORCRX surface first rather than packing the raw Hermes files.

## 5. Logs and audit treatment

`logs/*` is excluded by default. The one exception is an explicit audit-evidence opt-in:

```bash
hermes profile export --as-vessel <name> --include-audit
```

`--include-audit` does **not** copy raw log directories wholesale. It exports only a redacted audit evidence package derived from `logs/hermes-audit.ndjson` and `state/audit.sqlite`, with secret-bearing fields removed and provenance preserved.

## 6. Cron delivery rebinding

Imported cron policy is safe by default only when all jobs are disabled on install.

Import rules for each cron job:

1. force `"enabled": false`;
2. preserve schedule, prompt, skill, and script metadata;
3. clear or null out host-specific delivery channel IDs, webhook URLs, and bearer tokens;
4. require the operator to rebind delivery targets before enabling the job.

This keeps the portable automation intent while preventing a vessel from silently posting into the wrong host channels.

## 7. Kanban substrate rule

`kanban.db` is special because Kanban is a hard constraint for meaningful Hermes work, but the raw database is also host-local operational state.

Default rule:

- export strips the raw `kanban.db`;
- import extends the host Kanban substrate instead of replacing it;
- a vessel may ship Kanban schema expectations, board names, templates, or workflow policy as declarative metadata;
- any request to ship a vessel-owned Kanban substrate requires operator approval.

## 8. Conflict resolution strategies

The install and graft flows support three named strategies:

| Strategy | Behavior | Use when |
|---|---|---|
| `keep-host` | keep existing host content and ignore the incoming conflicting surface | the host profile is authoritative |
| `prefer-vessel` | replace the conflicting host surface with the vessel surface inside the target scope | the imported vessel should become the active truth |
| `namespace` | preserve both by materializing the imported surface under a vessel-specific namespace | default; safest for skills, overlays, and memory grafts |

Default strategy: `namespace`.

Recommended defaults by surface:

| Surface | Default strategy |
|---|---|
| skills | `namespace` |
| soul overlays | `namespace` via appended overlay section |
| memory grafts | `namespace` via sidecar files |
| config fragments | `keep-host` unless operator explicitly chooses otherwise |
| cron jobs | `namespace` plus disabled install |

## 9. Rehydration order

When installing a vessel into a fresh Hermes profile, rehydrate in this order:

1. create the new profile directory;
2. write `SOUL.md`, `AGENTS.md`, redacted `config.yaml`, skills, and portable memory;
3. attach host-supplied secret bindings and auth material;
4. install cron policy with jobs disabled;
5. materialize graft namespaces if partial slots were requested;
6. run post-install verification.

Suggested smoke check:

```bash
hermes -p <name> chat -Q -q 'Return exactly OK'
```

## Source paths

- `/Users/rudlord/.factory/missions/df2673b6-89f8-4626-b2b1-0857353d356c/library/W-F-hermes-binding.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/Users/rudlord/HORCRX/specs/hermes-binding/BINDING.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/SPEC.md`
- `/Users/rudlord/HORCRX/specs/vessel-format/memory-split.md`
- `/Users/rudlord/.hermes/config.yaml`
- `/Users/rudlord/.hermes/profiles/hermes-content-os/SOUL.md`
- `/Users/rudlord/wiki/_meta/hermes-stack/hermes-content-os.md`
