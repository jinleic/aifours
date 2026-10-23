#!/usr/bin/env python3
"""Retained intended-invariant controls and unchanged Claude-authored generic checker runs for128.
Parent positive128 is already recorded; do not rerun it here. All outputs exclusive, no claimant imports.
Usage: python3 -B mcdsqs128_parent_controls.py NEW_OUTPUT_DIRECTORY
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
CERT = HERE / 'mcdsqs128-parent-inputs-v1/mcdsqs128_c21.txt'
SHA = 'a97b1ae50fa8f0dc7f3bb6908e6c714fdd233eeede2607c2d16c2101380fd326'
PARENT = HERE / 'check_mcdsqs_independent.py'
THIRD = HERE / 'mcdsqs-claude-verifier-v1/checker.py'
THIRD_SHA = 'bda2c7a116d55d021429a9f1c9be7e73619327dbc205fc088457cbaa143e5c37'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=False)
    if digest(CERT) != SHA or digest(THIRD) != THIRD_SHA:
        raise ValueError('candidate/third checker pin mismatch')
    lines = CERT.read_text().split('\n')[:-1]
    block = lines.index('BLOCKS') + 1
    point0 = lines.index('POINT 0')
    fixtures = []

    def add(name, new, parent_reason, third_invariant):
        path = out / (name + '.txt')
        with path.open('x') as f:
            f.write('\n'.join(new) + '\n')
        fixtures.append((name, path, parent_reason, third_invariant))

    L = list(lines); L[block + 1] = L[block]
    add('duplicate-block', L, 'duplicate block', 'blocks.distinct')
    L = list(lines); t = L[block].split(); t[-1] = '128'; L[block] = ' '.join(t)
    add('block-outside-range', L, 'block point outside range', 'range.point')
    L = list(lines); t = L[block].split(); t[-1] = t[0]; L[block] = ' '.join(t)
    add('repeated-block-point', L, 'repeated point in block', 'format.distinct_points')
    L = list(lines); del L[point0 + 2]
    add('drop-derived-triple', L, 'colouring does not use every derived triple', 'colour.exactly_once')
    L = list(lines); class1 = lines.index('CLASS 1', point0); moved = L.pop(point0 + 2); L.insert(class1, moved)
    add('move-triple-into-overlapping-class', L, 'colour class is not a partial parallel class', 'colour.disjoint')
    L = lines[:lines.index('POINT 127')]
    add('drop-last-point-section', L, 'missing or out-of-order POINT 127', 'colour.all_points')
    L = list(lines); L[L.index('COLOURS 64')] = 'COLOURS 63'
    add('colours-below-minimum', L, 'COLOURS is not the counting lower bound ceil(D/M)', 'colours.r_equals_L')
    parent_rows = []
    third_rows = []

    def parent_run(name, path, size, sha, expected_reason):
        receipt = out / (name + '-parent.json')
        p = subprocess.run(['/usr/bin/python3', '-B', str(PARENT), str(path), str(size), sha, str(receipt)],
                           capture_output=True, text=True)
        data = json.loads(receipt.read_bytes())
        intended = p.returncode == 1 and data.get('status') == 'INVALID' and data.get('error_type') == 'CertificateError' and data.get('reason') == expected_reason
        parent_rows.append({'case': name, 'fixture_sha256': digest(path), 'returncode': p.returncode,
                            'reason': data.get('reason'), 'expected_reason': expected_reason, 'intended': intended})

    def third_run(name, path, size, sha, invariant, opt):
        cmd = ['/usr/bin/python3'] + (['-O'] if opt else []) + ['-B', str(THIRD), str(size), str(path), sha]
        p = subprocess.run(cmd, capture_output=True, text=True)
        data = json.loads(p.stdout)
        positive = invariant is None
        intended = p.returncode == (0 if positive else 1) and data.get('valid') is positive
        if not positive:
            intended = intended and data.get('invariant') == invariant
        third_rows.append({'case': name, 'optimized': opt, 'fixture_sha256': digest(path),
                           'returncode': p.returncode, 'valid': data.get('valid'), 'invariant': data.get('invariant'),
                           'expected_invariant': invariant, 'reason': data.get('reason'), 'intended': intended,
                           'stderr': p.stderr})

    for name, path, parent_reason, inv in fixtures:
        sh = digest(path)
        parent_run(name, path, 128, sh, parent_reason)
        for opt in (False, True):
            third_run(name, path, 128, sh, inv, opt)
    parent_run('wrong-sha', CERT, 128, '0' * 64, 'SHA256 mismatch')
    parent_run('wrong-order', CERT, 32, SHA, 'header mismatch')
    small = HERE / 'mcdsqs128-parent-fill-v2/mcdsqs32-parent.txt'
    for opt in (False, True):
        third_run('candidate128', CERT, 128, SHA, None, opt)
        third_run('published-filler32', small, 32, digest(small), None, opt)
        third_run('wrong-sha', CERT, 128, '0' * 64, 'sha256.mismatch', opt)
        third_run('wrong-order', CERT, 32, SHA, 'header.v', opt)
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'status': 'PASS' if all(r['intended'] for r in parent_rows + third_rows) else 'CONTROL-MISMATCH',
              'script_sha256': digest(Path(__file__)), 'candidate_sha256': SHA,
              'parent_checker_sha256': digest(PARENT), 'third_checker_sha256': THIRD_SHA,
              'third_authorship': 'Claude CLI claude-opus-5-5 prompt-only generic checker, unchanged since the mcDSQS38 round; parent executes it',
              'parent_runs': parent_rows, 'third_runs': third_rows,
              'counts': {'parent': len(parent_rows), 'third': len(third_rows)},
              'scope': '7 retained mutations, expected-argument controls, optimized/nonoptimized third-route positives128/published32; no gate/priority/infinite-family proof.'}
    with (out / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=1)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'counts': result['counts'],
                      'mismatches': [r for r in parent_rows + third_rows if not r['intended']]}, indent=1))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
