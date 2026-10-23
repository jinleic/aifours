#!/usr/bin/env python3
"""Final positive/negative checks, with explicit expected failure reasons.

Heavy arithmetic replays are recorded separately in their audit JSON files.
No compiled local binary is executed by this or any claims.json command.
"""
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    cases = [
        (['code/check.py', 'schema'], True, ''),
        (['code/verify_result.py'], True, ''),
        (['code/check_controls.py'], True, ''),
        (['code/check_family.py'], True, ''),
        (['code/check_survivors.py'], True, ''),
        (['code/check.py', 'metadata', 'logs/control-even', '--start', '2', '--stop', '5000000000', '--step', '2', '--published-controls'], True, ''),
        (['code/check.py', 'single', 'evidence/negative-residue.json', '--bound', '1000000'], False, 'full residue mismatch'),
        (['code/check.py', 'single', 'evidence/negative-self-factor.json', '--bound', '1000000'], False, 'actual smallest sieve factor mismatch'),
        (['code/check.py', 'metadata', 'evidence/negative-coverage'], False, 'block arithmetic-class count'),
        (['code/check_windows.py', 'evidence/negative-window.jsonl', '--indices', '0', '--backend', 'pow'], False, 'full-residue hash mismatch'),
        (['code/check_family.py', 'evidence/power-two-family-broken.json'], False, 'small modular witness mismatch'),
        (['code/check_controls.py', 'evidence/controls-broken.json'], False, 'collision element not in D'),
        (['code/verify_result.py', '--result', 'evidence/result-broken.json'], False, 'claimed endpoint mismatch'),
    ]
    results = []
    for argv, positive, reason in cases:
        t0 = time.monotonic()
        run = subprocess.run([sys.executable]+argv, capture_output=True, text=True)
        ok = (run.returncode == 0) if positive else (run.returncode != 0 and reason in run.stderr)
        row = dict(command='python3 '+' '.join(argv), expected='success' if positive else 'nonzero',
                   returncode=run.returncode, expected_failure_reason=reason, passed=ok,
                   seconds=time.monotonic()-t0, stdout=run.stdout, stderr=run.stderr)
        results.append(row)
        print(('PASS ' if ok else 'FAIL ')+row['command'], flush=True)
        if not ok:
            Path('evidence/fast-checks.json').write_text(json.dumps(results, indent=2)+'\n')
            raise SystemExit(1)
    claims = json.loads(Path('claims.json').read_text())
    for claim in claims['claims']:
        for item in claim['evidence']:
            assert Path(item).is_file(), 'missing evidence '+item
        for field in ('verify_command', 'check_command', 'control_command'):
            assert not claim[field] or claim[field].startswith('python3 '), 'non-Python replay command'
    Path('evidence/fast-checks.json').write_text(json.dumps(results, indent=2)+'\n')
    status_path = Path('evidence/STATUS.json')
    status = json.loads(status_path.read_text())
    final_result = json.loads(Path('evidence/result.json').read_text())
    status.update(phase='complete; computations and final checks finished',
                  main_finished=True, python_finished=True,
                  final_general_end=final_result['end'], outcome='partial',
                  finalized_utc=final_result['finalized_utc'],
                  finalization_data_needed=[])
    status_path.write_text(json.dumps(status, indent=2)+'\n')
    print('PASS: all final positive checks and every deliberate negative-control failure; all claim evidence files exist.')


if __name__ == '__main__':
    main()
