#!/usr/bin/env bash
# GATE-HX-07 — docs/CANONICAL.md allowlist from docs/roadmap/mission-B-hardening-pass.md H7.1
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/../.." && pwd)
canonical_file="$repo_root/docs/CANONICAL.md"

if [ ! -f "$canonical_file" ]; then
  echo "GATE-HX-07 FAIL: docs/CANONICAL.md is missing" >&2
  exit 1
fi

actual=$(mktemp)
allowed=$(mktemp)
trap 'rm -f "$actual" "$allowed"' EXIT

find "$repo_root/docs" -type f -name '*.md' | sed "s#^$repo_root/##" | sort > "$actual"
grep -E '^- `docs/.+`$' "$canonical_file" | perl -pe 's/^- `([^`]+)`$/\1/' | sort -u > "$allowed"

missing=$(comm -23 "$actual" "$allowed" || true)
stale=$(comm -13 "$actual" "$allowed" || true)

if [ -n "$missing" ] || [ -n "$stale" ]; then
  echo 'GATE-HX-07 FAIL: docs allowlist mismatch' >&2
  if [ -n "$missing" ]; then
    echo 'Unlisted docs:' >&2
    printf '%s\n' "$missing" >&2
  fi
  if [ -n "$stale" ]; then
    echo 'Stale allowlist entries:' >&2
    printf '%s\n' "$stale" >&2
  fi
  exit 1
fi

count=$(wc -l < "$actual" | tr -d ' ')
echo "GATE-HX-07 PASS: $count docs files are explicitly allowlisted."
