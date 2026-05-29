# manifest deferral

The pack already points at five role-level manifests through
`manifest.json::pack.members[*].manifest_cid`, but foundation phase does **not**
promote a second canonical `members/<role>/manifest.json` tree yet.

That normalization is deferred until a later implementation mission decides how
ORBEL child vessels should be materialized by the packing toolchain and whether
the existing role directories remain the canonical child-manifest paths for
marketplace and CI surfaces.

Until then, the root pack manifest stays authoritative for membership, and the
role manifests under `orbel-orchestrator/`, `orbel-researcher/`,
`orbel-builder/`, `orbel-evaluator-evolver/`, and `orbel-librarian/` remain the
reference child vessels for audit only.
