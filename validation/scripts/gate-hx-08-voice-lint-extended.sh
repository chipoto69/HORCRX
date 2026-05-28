#!/usr/bin/env bash
# GATE-HX-08 — packages/design-system/VOICE.md plus root/examples *soul*.md and voice.md surfaces
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/../.." && pwd)
tmp_list=$(mktemp)
trap 'rm -f "$tmp_list"' EXIT

{
  find "$repo_root" -maxdepth 1 -type f \( -iname '*soul*.md' -o -iname 'voice.md' \)
  find "$repo_root/examples" -type f \( -iname '*soul*.md' -o -iname 'voice.md' \)
  find "$repo_root/packages/design-system" -maxdepth 1 -type f -iname 'voice.md'
} | sort -u > "$tmp_list"

while IFS= read -r file; do
  [ -z "$file" ] && continue
  if grep -E '^\s*(\$|sudo |git |npm |pnpm |brew |/Users/)|^>\s*(\$|sudo |git |npm |pnpm |brew |/Users/)' "$file" >/dev/null; then
    echo "GATE-HX-08 FAIL: operational syntax found in ${file#$repo_root/}" >&2
    exit 1
  fi
done < "$tmp_list"

count=$(wc -l < "$tmp_list" | tr -d ' ')
echo "GATE-HX-08 PASS: linted $count voice/identity markdown files."
