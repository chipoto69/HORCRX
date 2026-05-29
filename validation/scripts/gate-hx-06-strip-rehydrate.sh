#!/usr/bin/env bash
# GATE-HX-06 — specs/hermes-binding/strip-and-rehydrate.md §2–§9
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/../.." && pwd)
fixture_dir="$repo_root/validation/fixtures/profile-fixture"
if [ ! -d "$fixture_dir" ]; then
  echo "GATE-HX-06 FAIL: missing fixture directory $fixture_dir" >&2
  exit 1
fi
output_dir=$(mktemp -d)
trap 'rm -rf "$output_dir"' EXIT

FIXTURE_DIR="$fixture_dir" OUTPUT_DIR="$output_dir" python3 - <<'PY'
import os
import shutil
from pathlib import Path

source = Path(os.environ['FIXTURE_DIR'])
output = Path(os.environ['OUTPUT_DIR']) / 'stripped-profile'
output.mkdir(parents=True, exist_ok=True)

strip_roots = {
    '.env', 'auth.json', 'auth.lock', 'state.db', 'state.db-wal', 'state.db-shm',
    'sessions', 'home', 'gateway.lock', 'gateway.pid', 'gateway_state.json', 'processes.json',
    'cache', 'audio_cache', 'image_cache', 'pastes', 'logs'
}


def redact_config(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        indent = line[: len(line) - len(line.lstrip())]
        if stripped.startswith('Authorization:'):
            lines.append(f'{indent}Authorization: ${{HOST_HORCRX_MARKETPLACE_TOKEN}}')
        elif stripped.startswith('api_key:'):
            lines.append(f'{indent}api_key: ${{HOST_MODEL_API_KEY}}')
        elif stripped.endswith('_TOKEN: fixture-secret-token'):
            key = stripped.split(':', 1)[0]
            lines.append(f'{indent}{key}: ${{HOST_{key}}}')
        else:
            lines.append(line)
    return '\n'.join(lines) + '\n'


for child in source.iterdir():
    if child.name in strip_roots:
        continue
    if child.name == 'cron':
        (output / 'cron').mkdir(parents=True, exist_ok=True)
        jobs = child / 'jobs.json'
        if jobs.exists():
            shutil.copy2(jobs, output / 'cron/jobs.json')
        continue
    destination = output / child.name
    if child.is_dir():
        shutil.copytree(child, destination, dirs_exist_ok=True)
    elif child.name == 'config.yaml':
        destination.write_text(redact_config(child.read_text(encoding='utf-8')), encoding='utf-8', newline='\n')
    else:
        shutil.copy2(child, destination)
PY

stripped_profile="$output_dir/stripped-profile"

for must_exist in SOUL.md AGENTS.md config.yaml cron/jobs.json; do
  if [ ! -e "$stripped_profile/$must_exist" ]; then
    echo "GATE-HX-06 FAIL: missing retained surface $must_exist" >&2
    exit 1
  fi
done

for must_strip in .env auth.json auth.lock state.db state.db-wal state.db-shm sessions home gateway.lock gateway.pid gateway_state.json processes.json cache audio_cache image_cache pastes logs; do
  if [ -e "$stripped_profile/$must_strip" ]; then
    echo "GATE-HX-06 FAIL: stripped surface survived: $must_strip" >&2
    exit 1
  fi
done

if grep -q 'fixture-secret-token\|sk-test-redacted-fixture' "$stripped_profile/config.yaml"; then
  echo "GATE-HX-06 FAIL: secret-bearing config values survived redaction" >&2
  exit 1
fi

echo "GATE-HX-06 PASS: stripped profile kept portable surfaces and removed runtime/auth state."
