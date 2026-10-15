#!/usr/bin/env python3
"""Run Comparator for configs in the isolated Mathlib project and write receipts."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / 'lean-verify'
COMPARATOR = Path('/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/comparator')
LAKE = Path.home() / '.elan/bin/lake'
SECURITY_LIMIT = ('macOS run with Comparator fake-landrun: no OS sandbox. Statement and definition '
                  'comparison, transitive permitted-axiom checks and fresh Lean-kernel replay execute; '
                  'no external kernel was configured.')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module_file(module):
    return PROJECT / (module.replace('.', '/') + '.lean')


def run(config_name, expected):
    config_path = PROJECT / 'configs' / (config_name + '.json')
    config = json.loads(config_path.read_text())
    environment = os.environ.copy()
    environment['PATH'] = str(Path.home() / '.elan/bin') + ':' + environment['PATH']
    environment['COMPARATOR_LANDRUN'] = str(COMPARATOR / 'scripts/fake-landrun.sh')
    environment['COMPARATOR_LEAN4EXPORT'] = str(COMPARATOR / '.lake/packages/lean4export/.lake/build/bin/lean4export')
    solution_olean = PROJECT / '.lake/build/lib/lean' / (config['solution_module'].replace('.', '/') + '.olean')
    previously_built = solution_olean.exists()
    command = [str(LAKE), 'env', str(COMPARATOR / '.lake/build/bin/comparator'), str(config_path)]
    started = time.monotonic()
    process = subprocess.run(command, cwd=PROJECT, env=environment, stdin=subprocess.DEVNULL,
                             capture_output=True, text=True)
    log_text = process.stdout + '\n--- stderr ---\n' + process.stderr
    receipts = ROOT / 'receipts'
    receipts.mkdir(exist_ok=True)
    (receipts / (config_name + '.log')).write_text(log_text)
    accepted = (process.returncode == 0 and 'Lean default kernel accepts the solution' in process.stdout
                and 'Your solution is okay!' in process.stdout)
    receipt = {
        'config': config_name,
        'config_sha256': sha(config_path),
        'challenge_sha256': sha(module_file(config['challenge_module'])),
        'solution_sha256': sha(module_file(config['solution_module'])),
        'theorem_names': config['theorem_names'],
        'definition_names': config.get('definition_names', []),
        'permitted_axioms': config['permitted_axioms'],
        'expected_acceptance': expected,
        'accepted': accepted,
        'matches_expected': accepted == expected,
        'exit_code': process.returncode,
        'kernel_accepts_marker': 'Lean default kernel accepts the solution' in process.stdout,
        'comparator_ok_marker': 'Your solution is okay!' in process.stdout,
        'solution_olean_existed_before_run': previously_built,
        'elapsed_seconds': time.monotonic() - started,
        'log': str(receipts / (config_name + '.log')),
        'security_limit': SECURITY_LIMIT,
    }
    (receipts / (config_name + '.json')).write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({key: receipt[key] for key in ('config', 'accepted', 'expected_acceptance', 'matches_expected', 'exit_code', 'solution_olean_existed_before_run', 'elapsed_seconds')}), flush=True)
    if not receipt['matches_expected']:
        print('\n'.join(log_text.splitlines()[-30:]), flush=True)
    return receipt['matches_expected']


if __name__ == '__main__':
    results = []
    for item in sys.argv[1:]:
        name, _, expectation = item.partition('=')
        if expectation not in ('accept', 'reject'):
            raise SystemExit('Use CONFIG=accept or CONFIG=reject')
        results.append(run(name, expectation == 'accept'))
    raise SystemExit(0 if all(results) else 1)
