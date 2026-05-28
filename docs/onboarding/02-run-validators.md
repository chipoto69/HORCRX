---
title: Run validators locally
version: v0.1-draft
updated: 2026-05-28
owner: hardening-mission
---

# Run validators locally

Run every command below from the repo root after `git fetch origin --prune`.

## 1. Baseline schema sanity

```bash
pnpm test
```

## 2. `ci/schema-validate`

```bash
manifest_args=(
  -d examples/horcrx-001-candysoul/manifest.json
  -d examples/horcrx-002-orbel-pack/manifest.json
  -d examples/horcrx-003-founder/manifest.json
)
while IFS= read -r child; do
  manifest_args+=( -d "$child" )
done < <(find examples \( -path 'examples/*/members/*/manifest.json' -o -path 'examples/*/orbel-*/manifest.json' \) -print | sort)
npx --yes ajv-cli@5 validate \
  --spec=draft2020 \
  -s specs/vessel-format/manifest.schema.json \
  "${manifest_args[@]}"
listing_args=()
while IFS= read -r listing; do
  listing_args+=( -d "$listing" )
done < <(find examples/listings -maxdepth 1 -name '*.json' -print | sort)
npx --yes ajv-cli@5 validate \
  --spec=draft2020 \
  -s specs/registry/listing.schema.json \
  "${listing_args[@]}"
npx --yes ajv-cli@5 compile --spec=draft2020 -s specs/marketplace/mcp.schema.json
npx --yes ajv-cli@5 compile --spec=draft2020 -s specs/marketplace/anti-sybil-schema.json
```

## 3. `ci/commitlint`

```bash
regex='^(feat|fix|docs|chore|build|ci|refactor|test|polish)(\(.+\))?: .+'
git log --pretty=format:'%s' origin/main..HEAD | while IFS= read -r subject; do
  [ -z "$subject" ] && continue
  if printf '%s\n' "$subject" | grep -Eq '^(Merge|Revert) '; then
    continue
  fi
  printf '%s\n' "$subject" | grep -Eq "$regex"
done
```

## 4. `ci/markdown-link-check`

```bash
python3 - <<'PY'
import re
import sys
from pathlib import Path
from urllib.parse import unquote

root = Path.cwd()
link_re = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
missing = []
for md in root.rglob('*.md'):
    if '.git' in md.parts or 'node_modules' in md.parts:
        continue
    text = md.read_text(encoding='utf-8')
    for raw in link_re.findall(text):
        target = raw.strip().split()[0].strip('<>')
        if not target or target.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        target = unquote(target.split('#', 1)[0])
        if not target:
            continue
        candidate = (md.parent / target).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError:
            continue
        if not candidate.exists():
            missing.append(f'{md.relative_to(root)} -> {raw}')
if missing:
    print('Broken internal markdown links:')
    print('\n'.join(missing))
    sys.exit(1)
print('markdown-link-check: PASS')
PY
```

## 5. `ci/secret-scan`

Fast local diff-hunk scan (matches the mission helper posture):

```bash
diff_added=$(git diff origin/main..HEAD -- ':!**/*.md' ':!validation/**' | grep -E '^\+[^+]' || true)
patterns='(-----BEGIN [A-Z ]*PRIVATE KEY-----|sk_live_[A-Za-z0-9]{20,}|sk_test_[A-Za-z0-9]{20,}|xox[bpars]-[A-Za-z0-9-]{20,}|ghp_[A-Za-z0-9]{30,}|AIza[0-9A-Za-z\-_]{30,})'
if [ -n "$diff_added" ] && echo "$diff_added" | grep -E -q "$patterns"; then
  echo 'SECRET-SCAN FAIL: high-entropy match in added lines'
  echo "$diff_added" | grep -E "$patterns" | head -5
  exit 1
fi
echo 'secret-scan OK'
```

If you have the `gitleaks` CLI installed locally, run the CI-equivalent full scanner as well:

```bash
gitleaks git .
```

## 6. `ci/voice-lint`

```bash
set -e
for f in SOUL.md packages/design-system/VOICE.md examples/*/voice.md examples/*/soul.md; do
  if [ -f "$f" ]; then
    if grep -E '^(\$|sudo|git |npm |pnpm |brew |/Users/)|^>\s*(\$|sudo|git |npm |pnpm |brew |/Users/)' "$f"; then
      echo "VOICE-LINT FAIL: '$f' contains operational syntax"
      exit 1
    fi
  fi
done
echo 'voice-lint OK'
```

## 7. `ci/gate-hx-04-signature-roundtrip`

```bash
./validation/scripts/gate-hx-04-signature-roundtrip.py
```

## 8. `ci/gate-hx-05-parent-cid-resolves`

```bash
./validation/scripts/gate-hx-05-parent-cid-resolves.py
```

## 9. `ci/gate-hx-06-strip-rehydrate`

```bash
./validation/scripts/gate-hx-06-strip-rehydrate.sh
```

## 10. `ci/gate-hx-07-docs-allowlist`

```bash
./validation/scripts/gate-hx-07-docs-allowlist.sh
```

## 11. `ci/gate-hx-08-voice-lint-extended`

```bash
./validation/scripts/gate-hx-08-voice-lint-extended.sh
```

## 12. `ci/x402-nonce-replay`

```bash
./validation/scripts/x402-nonce-replay.py
```

## 13. `ci/royalty-determinism`

```bash
./validation/scripts/royalty-determinism.py
```

## 14. `ci/docs-frontmatter`

```bash
python3 - <<'PY'
import sys
from pathlib import Path

docs_root = Path('docs')
required_fields = ('title', 'version', 'updated')

for path in sorted(docs_root.rglob('*.md')):
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0].strip() != '---':
        print(f'MISSING FRONTMATTER: {path}')
        sys.exit(1)
    try:
        closing_index = lines[1:].index('---') + 1
    except ValueError:
        print(f'UNTERMINATED FRONTMATTER: {path}')
        sys.exit(1)
    frontmatter = lines[1:closing_index]
    for field in required_fields:
        if not any(line.startswith(f'{field}:') for line in frontmatter):
            print(f'MISSING {field}: {path}')
            sys.exit(1)

print('docs-frontmatter: PASS')
PY
```

## 15. `ci/redaction-validator`

```bash
./validation/scripts/redaction-validator.py
```

## 16. `ci/aead-kats`

```bash
python3 -m pip install pynacl cryptography
./validation/scripts/aead-kats.py
```

## 17. `ci/payout-target-format`

```bash
./validation/scripts/payout-target-format.py
./validation/scripts/royalty-split-sum.py
```

## 18. `ci/revocation-never-deletes`

```bash
./validation/scripts/revocation-never-deletes.py
```

## 19. `ci/chain-adapter-symmetry`

```bash
./validation/scripts/chain-adapter-symmetry.py
```

## 20. `ci/preview-integrity`

```bash
./validation/scripts/preview-integrity.py
```

## 21. `ci/marketplace-envelope-kats`

```bash
python3 -m pip install cryptography pynacl
./validation/scripts/marketplace-envelope-kats.py
```

## 22. `ci/changelog-regression`

```bash
set -euo pipefail
mapfile -t annotated_tags < <(
  git tag --points-at HEAD --list 'v*' | while IFS= read -r tag; do
    [ -z "$tag" ] && continue
    if [ "$(git cat-file -t "$tag")" = "tag" ]; then
      printf '%s\n' "$tag"
    fi
  done
)

if [ "${#annotated_tags[@]}" -eq 0 ]; then
  echo "No annotated v* tag points at HEAD; changelog regression check skipped."
  exit 0
fi

for tag in "${annotated_tags[@]}"; do
  version="${tag#v}"
  section_prefix="^## \\[$version\\]"
  if ! grep -Eq "${section_prefix}( - .+)?$" CHANGELOG.md; then
    echo "CHANGELOG.md is missing a matching section for $tag" >&2
    exit 1
  fi
done

printf 'Validated CHANGELOG sections for: %s\n' "${annotated_tags[*]}"
```

## 23. Recommended pre-push sequence

For documentation-heavy changes, this order catches most mistakes quickly:

```bash
pnpm test
./validation/scripts/gate-hx-07-docs-allowlist.sh
python3 - <<'PY'
import re
import sys
from pathlib import Path
from urllib.parse import unquote

root = Path.cwd()
link_re = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
missing = []
for md in root.rglob('*.md'):
    if '.git' in md.parts or 'node_modules' in md.parts:
        continue
    text = md.read_text(encoding='utf-8')
    for raw in link_re.findall(text):
        target = raw.strip().split()[0].strip('<>')
        if not target or target.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        target = unquote(target.split('#', 1)[0])
        if not target:
            continue
        candidate = (md.parent / target).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError:
            continue
        if not candidate.exists():
            missing.append(f'{md.relative_to(root)} -> {raw}')
if missing:
    print('Broken internal markdown links:')
    print('\n'.join(missing))
    sys.exit(1)
print('markdown-link-check: PASS')
PY
```
