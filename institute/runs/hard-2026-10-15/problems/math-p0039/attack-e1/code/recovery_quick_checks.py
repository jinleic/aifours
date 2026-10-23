#!/usr/bin/env python3
"""Positive/negative recovery checks with explicit failure reasons.

This is a bounded validation suite, not an exhaustive replay of the production
interval. All subprocesses use Python; no producing binary or module is run.
Each child has a timeout below 900 seconds. Exact chunk/window computations
are logged separately by their own bounded commands.
"""
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    cases = [
        (['code/make_recovery_controls.py'], True, ''),
        (['code/recover_logs.py', '--check-only'], True, ''),
        (['code/check.py', 'schema'], True, ''),
        (['code/recheck.py', 'main-metadata'], True, ''),
        (['code/recheck.py', 'python-records'], True, ''),
        (['code/check_controls.py'], True, ''),
        (['code/check_family.py'], True, ''),
        (['code/check_survivors.py'], True, ''),
        (['code/check.py', 'metadata', 'logs/control-even', '--start', '2', '--stop',
          '5000000000', '--step', '2', '--published-controls'], True, ''),
        (['code/check.py', 'records', 'logs/small-sieve'], True, ''),
        (['code/check.py', 'records', 'logs/arith-main'], True, ''),
        (['code/check.py', 'single', 'evidence/negative-residue.json', '--bound', '1000000'],
         False, 'full residue mismatch'),
        (['code/check.py', 'single', 'evidence/negative-self-factor.json', '--bound', '1000000'],
         False, 'actual smallest sieve factor mismatch'),
        (['code/check.py', 'metadata', 'evidence/negative-coverage'],
         False, 'block arithmetic-class count'),
        (['code/recheck.py', 'main-negative'], False, 'claimed endpoint mismatch'),
        (['code/recheck.py', 'comparison-negative'], False, 'shared full residue mismatch'),
        (['code/check_controls.py', 'evidence/controls-broken.json'], False, 'collision element not in D'),
        (['code/check_family.py', 'evidence/power-two-family-broken.json'], False, 'small modular witness mismatch'),
        (['code/check_windows.py', 'evidence/negative-window.jsonl', '--indices', '0', '--backend', 'pow'],
         False, 'full-residue hash mismatch'),
        (['code/check_interval.py', '0', '--evidence', 'evidence/prefix-chunk-broken.json', '--backend', 'pow'],
         False, 'full-interval hash mismatch'),
        (['code/recover_logs.py', '--manifest', 'selection-inputs/first-attempt-logs/BROKEN-MANIFEST.json'],
         False, 'compressed hash mismatch'),
    ]
    rows = []
    for argv, positive, expected in cases:
        begin = time.monotonic()
        run = subprocess.run([sys.executable]+argv, capture_output=True, text=True, timeout=830)
        passed = run.returncode == 0 if positive else (run.returncode != 0 and expected in run.stderr)
        row = dict(command=['python3']+argv, expected='success' if positive else 'nonzero',
                   returncode=run.returncode, expected_reason=expected, passed=passed,
                   seconds=time.monotonic()-begin, stdout=run.stdout, stderr=run.stderr)
        rows.append(row)
        Path('evidence/recovery-quick-checks.json').write_text(json.dumps(rows, indent=2)+'\n')
        print(json.dumps({k: row[k] for k in ('command', 'returncode', 'passed', 'seconds')}), flush=True)
        if not passed:
            raise SystemExit(1)
    claims = json.loads(Path('claims.json').read_text())
    for c in claims['claims']:
        for f in c['evidence']:
            assert Path(f).is_file(), 'missing evidence '+f
        for k in ('verify_command', 'check_command', 'control_command'):
            assert not c[k] or c[k].startswith('python3 '), 'non-Python replay command'
    print('PASS: all stated recovery checks and expected negative-control failures; subset scope only.')


if __name__ == '__main__':
    main()
