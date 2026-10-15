#!/usr/bin/env python3
"""Replay the delivered checks in a new directory, preserving all original receipts."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
FILES = [
    'TASK.md', 'verify.py', 'Formal.lean', 'NegativeControl.lean', 'claims.json',
    'REPORT.md', 'REFERENCES.md', 'STRUCTURAL.md', 'source-evidence.json',
    'levi_character_check.py', 'level4_invariant_check.py',
    'check_level4_invariant.py', 'level4-invariant-vectors.json',
    'level4_cells_producer.py', 'level4_cells_check.py',
    'level4-cells-certificate.json', 'check_levi.py', 'level3-certificate.json',
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=False)
    hashes = {}
    for name in FILES:
        source = HERE / name
        hashes[name] = hashlib.sha256(source.read_bytes()).hexdigest()
        shutil.copyfile(source, destination / name)
    baseline = HERE.parent / 'evidence/round2-uniform/parent-independent-check.json'
    commands = [
        [sys.executable, 'verify.py'],
        [sys.executable, 'levi_character_check.py'],
        [sys.executable, 'check_level4_invariant.py'],
        [sys.executable, 'level4_cells_check.py'],
        [sys.executable, 'check_levi.py', 'level3-certificate.json',
         '--baseline', str(baseline), '--output', str(destination / 'levi-independent-check.json')],
    ]
    environment = dict(os.environ, LEAN_IMPORT_WORKERS='1', OMP_NUM_THREADS='1',
                       OPENBLAS_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    runs = []
    for number, command in enumerate(commands, 1):
        log_path = destination / f'replay-{number}.log'
        started = time.monotonic()
        with log_path.open('w') as log:
            result = subprocess.run(command, cwd=destination, env=environment,
                                    stdout=log, stderr=subprocess.STDOUT, timeout=1200)
        runs.append({'command': command, 'cwd': str(destination),
                     'returncode': result.returncode, 'seconds': time.monotonic() - started,
                     'log': str(log_path)})
        if result.returncode:
            break
    receipt = {'scope': 'Partial Lean and exact finite Lie-module evidence only',
               'full_original_goal_solved': False,
               'all_requested_checks_pass': len(runs) == len(commands) and
                                            all(run['returncode'] == 0 for run in runs),
               'source_sha256': hashes, 'runs': runs,
               'comparator_run': False, 'nanoda_run': False}
    (destination / 'replay.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))
    raise SystemExit(0 if receipt['all_requested_checks_pass'] else 1)


if __name__ == '__main__':
    main()
