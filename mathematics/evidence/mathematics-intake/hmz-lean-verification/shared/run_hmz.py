#!/usr/bin/env python3
"""Run the sanctioned wrapper once and retain provenance, output and journals."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

WORKSPACE = Path('/Users/jinleic/jinleic-workspace')
ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--repo', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--timeout', type=int, required=True)
args = parser.parse_args()
repo = args.repo.resolve()
output = args.output.resolve()
if not repo.is_relative_to(ROOT) or not output.is_relative_to(ROOT):
    raise SystemExit('Both repository and evidence must stay within this scratch root')
if args.timeout <= 0:
    raise SystemExit('A positive finite HMZ duration is required')
task = repo / 'TASK.md'
if not task.is_file():
    raise SystemExit('Missing frozen TASK.md')
output.mkdir(parents=True, exist_ok=True)
receipt_path = output / 'process.json'
if receipt_path.exists():
    raise SystemExit('Refusing to overwrite an existing run')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(path, *arguments):
    return subprocess.check_output(['git', '-C', str(path), *arguments], text=True).strip()

def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()

baseline = git(repo, 'rev-parse', 'HEAD')
frozen_paths = [task] + [repo / name for name in ('verify.py', 'ACCEPTANCE.md') if (repo / name).is_file()]
frozen = {str(path.relative_to(repo)): sha(path) for path in frozen_paths}
install_path = Path.home() / '.local/share/uv/tools/hmz/lib/python3.12/site-packages/hmz-0.1.0.dist-info/direct_url.json'
command = [str(WORKSPACE / 'scripts/hmz-run.sh'), '--dir', str(repo), '--timeout', str(args.timeout), '--task-file', str(task)]
record = {
    'schema': 'ai4s-hmz-run/1',
    'repo': str(repo),
    'baseline_commit': baseline,
    'command': command,
    'timeout_seconds': args.timeout,
    'started_at_utc': stamp(),
    'frozen_sha256': frozen,
    'wrapper_sha256': sha(WORKSPACE / 'scripts/hmz-run.sh'),
    'flow_sha256': sha(WORKSPACE / 'scripts/hmz-flows/rlar-bypass/__init__.py'),
    'pairing_sha256': sha(WORKSPACE / 'scripts/hmz-tiers.json'),
    'pairing': json.loads((WORKSPACE / 'scripts/hmz-tiers.json').read_text()),
    'hmz_install': json.loads(install_path.read_text()),
    'official_flowverse_commit': git(Path.home() / '.humanize/flowverses/official', 'rev-parse', 'HEAD'),
    'os_sandbox': False,
    'acceptance': 'Exit status alone is not acceptance. Require the actual reviewer done:true and terminal ended how:done; separately check mathematical scope and Lean evidence.',
}
receipt_path.write_text(json.dumps(record, indent=2) + '\n')
start = time.monotonic()
with (output / 'wrapper.log').open('w') as log:
    process = subprocess.run(command, cwd=WORKSPACE, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT)
record.update({
    'ended_at_utc': stamp(),
    'elapsed_seconds': time.monotonic() - start,
    'returncode': process.returncode,
    'frozen_unchanged': {name: (repo / name).is_file() and sha(repo / name) == digest for name, digest in frozen.items()},
})
epic_root = Path.home() / '.humanize/epics' / str(repo).replace('/', '-')
journals = []
if epic_root.is_dir():
    for run in sorted(epic_root.iterdir()):
        if not run.is_dir():
            continue
        entry = {'directory': str(run)}
        for name in ('epic.jsonl', 'resume.jsonl'):
            source = run / name
            if source.is_file():
                destination = output / (run.name + '-' + name)
                destination.write_bytes(source.read_bytes())
                entry[name] = {'path': str(source), 'copy': str(destination), 'sha256': sha(source)}
        journals.append(entry)
record['journals'] = journals
receipt_path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({key: record[key] for key in ('repo', 'returncode', 'elapsed_seconds', 'frozen_unchanged', 'journals')}, indent=2), flush=True)
raise SystemExit(process.returncode)
