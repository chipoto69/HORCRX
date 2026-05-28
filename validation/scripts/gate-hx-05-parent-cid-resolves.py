#!/usr/bin/env python3
# GATE-HX-05 — specs/vessel-format/signing-and-lineage.md §Parent CID lineage; specs/marketplace/royalties.md §2.1

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXAMPLES = REPO / 'examples'
KNOWN_CIDS = REPO / 'validation/fixtures/known-cids.json'


def fail(message: str) -> None:
    print(f'GATE-HX-05 FAIL: {message}', file=sys.stderr)
    raise SystemExit(1)


def manifest_cid(path: Path) -> str:
    return f"cid:sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def main() -> None:
    whitelist = set(json.loads(KNOWN_CIDS.read_text(encoding='utf-8')).get('whitelist', []))
    manifest_paths = sorted(EXAMPLES.rglob('manifest.json'))
    cid_to_path = {manifest_cid(path): path for path in manifest_paths}
    path_to_parents: dict[Path, list[Path]] = {}
    parent_edges = 0
    pack_refs = 0

    for path in manifest_paths:
        manifest = load_manifest(path)
        parent_paths: list[Path] = []
        for parent_cid in manifest.get('parent_cids', []):
            if parent_cid in cid_to_path:
                parent_paths.append(cid_to_path[parent_cid])
            elif parent_cid not in whitelist:
                fail(f"{path.relative_to(REPO)} references unresolved parent_cid {parent_cid}")
            parent_edges += 1
        path_to_parents[path] = parent_paths

        pack = manifest.get('pack')
        if isinstance(pack, dict):
            for member in pack.get('members', []):
                member_cid = member.get('manifest_cid')
                if not member_cid:
                    fail(f"{path.relative_to(REPO)} pack.members entry is missing manifest_cid")
                if member_cid not in cid_to_path:
                    fail(f"{path.relative_to(REPO)} references unresolved pack member manifest_cid {member_cid}")
                pack_refs += 1

    visiting: set[Path] = set()
    visited: set[Path] = set()

    def dfs(node: Path) -> None:
        if node in visiting:
            fail(f'cycle detected at {node.relative_to(REPO)}')
        if node in visited:
            return
        visiting.add(node)
        for parent in path_to_parents[node]:
            dfs(parent)
        visiting.remove(node)
        visited.add(node)

    for path in manifest_paths:
        dfs(path)

    print(f'GATE-HX-05 PASS: resolved {parent_edges} parent_cids across {len(manifest_paths)} manifests and {pack_refs} pack-member manifest references with no cycles.')


if __name__ == '__main__':
    main()
