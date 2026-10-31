#!/usr/bin/env python3
"""Five intended-reason corruption controls for the standard-library pair replay.

Fixtures are retained in the exclusive owner root; original certificates and
all existing files remain unchanged. Positive replay is not rerun: its two
already recorded receipts are the positive controls.
"""
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    original = json.loads((ROOT / 'frontier-20261028-level6-336-fast-pair-algebra-v1.json').read_text())
    tests = []
    C = copy.deepcopy(original)
    C['residual_A'][0]['coefficient'] = str(int(C['residual_A'][0]['coefficient']) + 1)
    tests.append(('coefficient', C, 'minor reconstruction fails'))
    C = copy.deepcopy(original)
    C['residual_A'].append(C['residual_A'][0].copy())
    tests.append(('duplicate', C, 'duplicate exponent'))
    C = copy.deepcopy(original)
    C['positive_common_factor'] = [{'x_power': 0, 'y_power': 0, 'coefficient': '1'},
                                    {'x_power': 1, 'y_power': 0, 'coefficient': '-1'}]
    tests.append(('sign', C, 'common factor is not strictly one-sign'))
    C = copy.deepcopy(original)
    p = C['axis_coprimality']['prime']
    C['axis_coprimality']['bezout_u'][0] = (C['axis_coprimality']['bezout_u'][0] + 1) % p
    tests.append(('bezout', C, 'full Bezout identity fails'))
    C = copy.deepcopy(original)
    C['bezout_bound_on_exceptional_complex_pairs'] -= 1
    tests.append(('bound', C, 'Bezout bound mismatch'))
    results = []
    for name, C, reason in tests:
        path = ROOT / ('frontier-20261028-level6-corrupt-' + name + '-algebra-v1.json')
        with path.open('x') as stream:
            json.dump(C, stream)
            stream.write('\n')
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        command = [sys.executable, str(ROOT / 'frontier-20261028-level6-coprime-pair-replay.py'),
                   '--certificate', path.name, '--sha256', sha]
        proc = subprocess.run(command, text=True, capture_output=True, timeout=30)
        expected = 'CertificateError: ' + reason
        passed = proc.returncode != 0 and expected in proc.stderr
        if not passed:
            raise RuntimeError((name, proc.returncode, proc.stderr))
        results.append({'mutation': name, 'fixture': path.name, 'sha256': sha, 'returncode': proc.returncode,
                        'intended_exception': expected, 'intended_reason_observed': True})
    out = ROOT / 'frontier-20261028-level6-coprime-controls-v1.json'
    with out.open('x') as stream:
        json.dump({'status': 'PASS_FIVE_INTENDED_REASON_MUTATIONS', 'results': results,
                   'positive_receipts': ['frontier-20261028-level6-336-fast-pair-algebra-independent-replay-v1.json',
                                         'frontier-20261028-level6-436-fast-pair-algebra-independent-replay-v1.json']}, stream, indent=2)
        stream.write('\n')
    print('PASS five exact intended-reason certificate corruptions', out.name)


if __name__ == '__main__':
    main()
