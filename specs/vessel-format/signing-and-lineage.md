# Signing and lineage

Version: `v0.1-draft`

HORCRX uses content addressing plus explicit signatures so a vessel can be bought, forked, and audited without trusting a single hosting surface.

## Default signing posture

- **Ed25519** is the default signature algorithm for manifests and slot bodies.
- **secp256k1** is supported for EVM-native operator flows and wallet-aligned attestations.
- A vessel MAY expose more than one public signing key, but every signature must declare its algorithm and scope.

## Signing scopes

1. **manifest signature** — covers the top-level manifest and slot map.
2. **per-slot signature** — covers a single slot or slot artifact.
3. **attestation signature** — covers marketplace events such as publication, purchase acknowledgement, or revocation.

## Per-slot signing

Every slot entry SHOULD declare:

- `cid`,
- `digest`,
- `signer_key_id`,
- `algorithm`,
- optional `transparency_log_uri`.

Per-slot signing matters because:

- a collaborator can sign only the slot they authored,
- encrypted slots can retain provenance without exposing plaintext,
- packs can keep child-vessel provenance intact.

## Parent CID lineage

Lineage is recorded through `parent_cids[]` in `manifest.json`.

Rules:

1. a genesis vessel has an empty `parent_cids[]` array;
2. a fork records the immediate parent manifest CID;
3. a merge or recomposition MAY record multiple parent CIDs;
4. royalties and provenance resolve against the parent CID chain, not just the current seller.

## Transparency-log option

HORCRX does not require Sigstore, but it reserves an optional transparency-log anchor inspired by the Sigstore model surfaced in `/Users/rudlord/HORCRX/research/02-prior-art.md`.

A manifest MAY include:

- `transparency_log.kind`,
- `transparency_log.entry_id`,
- `transparency_log.inclusion_proof`.

## Local source paths

- `/Users/rudlord/HORCRX/research/02-prior-art.md`
- `/Users/rudlord/HORCRX/research/05-risks-and-tensions.md`
- `/Users/rudlord/HORCRX/research/09-hermes-binding-recon.md`
- `/tmp/horcrx-research/02-prior-art.md`
