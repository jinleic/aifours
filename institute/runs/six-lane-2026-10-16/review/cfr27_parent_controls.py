#!/usr/bin/env python3
"""Retained mathematical/format controls for the parent CFR and cyclic-DM verifier.
Includes a wraparound-only negative and noncanonical positive gauges. No claimant imports.
Usage: python3 -B cfr27_parent_controls.py NEW_OUTPUT_DIRECTORY
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo
import check_cfr_dm_parent as checker

HERE = Path(__file__).resolve().parent
PIN = HERE / 'cfr27-parent-inputs-v1'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def render(matrix):
    return ('\n'.join(' '.join(map(str, row)) for row in matrix) + '\n').encode('ascii')


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=False)
    manifest = json.loads((PIN / 'manifest.json').read_bytes())['files']
    fixtures = []

    def add(name, kind, matrix, r, n, category=None, raw=None, expected_sha=None):
        data = render(matrix) if raw is None else raw
        path = out / (name + '.raw')
        with path.open('xb') as f:
            f.write(data)
        fixtures.append((name, kind, path, r, n, expected_sha or sha(data), category))

    for tag in ['A', 'B']:
        cr = (PIN / (tag + '-CFR.raw')).read_bytes()
        dr = (PIN / (tag + '-DM.raw')).read_bytes()
        if sha(cr) != manifest[tag + '-CFR.raw']['sha256'] or sha(dr) != manifest[tag + '-DM.raw']['sha256']:
            raise ValueError('pin mismatch')
        C = checker.parse(cr, 5, 27)
        D = checker.parse(dr, 6, 27)
        # Genuine CFR gauges; they need not retain identity row0 or a common first symbol.
        L = [row[:] for row in C]; L[1] = L[1][1:] + L[1][:1]
        add(tag + '-positive-one-row-rotated', 'cfr', L, 5, 27)
        L = [[1 if x == 0 else 0 if x == 1 else x for x in row] for row in C]
        add(tag + '-positive-common-symbol-swap', 'cfr', L, 5, 27)
        L = [[row[(2 * i) % 27] for i in range(27)] for row in C]
        add(tag + '-positive-unit-position-multiplier', 'cfr', L, 5, 27)
        # Genuine DM gauges: arbitrary column constants cancel from every row difference.
        L = [[(D[i][c] + c * c + c) % 27 for c in range(27)] for i in range(6)]
        add(tag + '-positive-DM-column-constants', 'dm', L, 6, 27)
        add(tag + '-positive-DM-column-reversal', 'dm', [row[::-1] for row in D], 6, 27)
        L = [row[:] for row in C]; L[1] = L[0][:]
        add(tag + '-copy-CFR-row', 'cfr', L, 5, 27, 'EVENT_COLLISION')
        L = [row[:] for row in C]; L[1][-1] = L[1][0]
        add(tag + '-repeat-CFR-symbol', 'cfr', L, 5, 27, 'ROW_PERMUTATION')
        L = [row[:] for row in C]; L[1][0] = 27
        add(tag + '-CFR-point-27', 'cfr', L, 5, 27, 'POINT_RANGE')
        L = [row[:] for row in C]; L[1].pop()
        add(tag + '-drop-CFR-entry', 'cfr', L, 5, 27, 'ROW_WIDTH')
        # Find a transposition preserving each row's permutation but breaking the CFR property.
        selected = None
        for p in range(26):
            L = [row[:] for row in C]
            L[1][p], L[1][p + 1] = L[1][p + 1], L[1][p]
            try:
                checker.cfr(L, 27)
            except checker.Invalid as exc:
                if str(exc).split(':', 1)[0] == 'EVENT_COLLISION':
                    selected = L
                    break
        if selected is None:
            raise ValueError('no collision-making transposition control')
        add(tag + '-transpose-CFR-entries', 'cfr', selected, 5, 27, 'EVENT_COLLISION')
        add(tag + '-wrong-row-count', 'cfr', C, 4, 27, 'ROW_COUNT')
        add(tag + '-wrong-order-width', 'cfr', C, 5, 26, 'ROW_WIDTH')
        add(tag + '-wrong-digest', 'cfr', C, 5, 27, 'INPUT_SHA256', raw=cr, expected_sha='0' * 64)
        add(tag + '-missing-final-LF', 'cfr', C, 5, 27, 'FORMAT', raw=cr[:-1])
        add(tag + '-CRLF', 'cfr', C, 5, 27, 'FORMAT', raw=cr.replace(b'\n', b'\r\n', 1))
        add(tag + '-extra-line', 'cfr', C, 5, 27, 'ROW_COUNT', raw=cr + b'EXTRA\n')
        add(tag + '-leading-zero', 'cfr', C, 5, 27, 'FORMAT', raw=b'0' + cr)
        L = [row[:] for row in D]; L[0][0] = (L[0][0] + 1) % 27
        add(tag + '-modify-DM-entry', 'dm', L, 6, 27, 'DM_PAIR')
        L = [row[:] for row in D]; L[2] = L[1][:]
        add(tag + '-duplicate-DM-row', 'dm', L, 6, 27, 'DM_PAIR')
        L = [row[:] for row in D]
        for row in L:
            row[1] = row[0]
        add(tag + '-duplicate-DM-column', 'dm', L, 6, 27, 'DM_PAIR')
    add('positive-CFR2-3', 'cfr', [[0, 1, 2], [0, 2, 1]], 2, 3)
    add('positive-DM3-3', 'dm', [[0, 0, 0], [0, 1, 2], [0, 2, 1]], 3, 3)
    add('negative-circular-wrap-not-linear', 'cfr', [[0, 1, 2, 3], [1, 3, 0, 2]], 2, 4, 'EVENT_COLLISION')
    results = []
    for name, kind, path, r, n, digest, expected in fixtures:
        try:
            report = checker.check(kind, path, r, n, digest)
            actual = None
            rc = 0
        except checker.Invalid as exc:
            actual = str(exc).split(':', 1)[0]
            report = {'status': 'FAIL', 'error_type': 'Invalid', 'reason': str(exc)}
            rc = 1
        intended = actual == expected and rc == (0 if expected is None else 1)
        report.update(case=name, expected_category=expected, actual_category=actual, intended=intended,
                      fixture_sha256=sha(path.read_bytes()), expected_sha256=digest, expected_rows=r, expected_n=n, kind=kind)
        with (out / (name + '.json')).open('x') as f:
            json.dump(report, f, indent=1)
            f.write('\n')
        results.append({k: report[k] for k in ['case', 'expected_category', 'actual_category', 'intended', 'fixture_sha256', 'expected_sha256', 'expected_rows', 'expected_n', 'kind']})
    summary = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'status': 'PASS' if all(r['intended'] for r in results) else 'CONTROL-MISMATCH',
               'checker_sha256': sha(Path(checker.__file__).read_bytes()), 'controls_sha256': sha(Path(__file__).read_bytes()),
               'counts': {'total': len(results), 'positive': sum(r['expected_category'] is None for r in results),
                          'negative': sum(r['expected_category'] is not None for r in results)}, 'results': results}
    with (out / 'parent-result.json').open('x') as f:
        json.dump(summary, f, indent=1)
        f.write('\n')
    print(json.dumps({'status': summary['status'], 'counts': summary['counts'],
                      'mismatches': [r for r in results if not r['intended']]}, indent=1))
    return 0 if summary['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
