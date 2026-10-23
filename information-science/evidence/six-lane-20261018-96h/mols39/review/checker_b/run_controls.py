#!/usr/bin/env python3
"""Run checker_b.py on every case of controls/expected.json and compare the observed
exit status, verdict and failing sets with the hand-derived expectations.

Usage: python3 -I -B run_controls.py OUTDIR
OUTDIR (relative to this directory, or absolute) must not exist; it is created and
receives control_results.json (exclusive create) plus the squares file of the --emit
cases.  Each checker run is `<this python> -I -B checker_b.py ARGS` with cwd = this
directory and no timeout.  Exit 0 iff every case behaves exactly as expected.

Beyond the expected sets, every witness the checker reports is re-validated directly
from the control matrix with the bridge formula, the emitted squares are compared
byte for byte with the closed form of the linear control, and controls/ is
snapshotted (names + SHA-256) before and after to show the checker never wrote there.
"""

import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(HERE, 'checker_b.py')
CONTROLS = os.path.join(HERE, 'controls')
EXPECTED = os.path.join(CONTROLS, 'expected.json')
CAP = 8  # checker_b's WITNESS_CAP, restated


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, 'rb') as fh:
        return sha256_bytes(fh.read())


def snapshot(directory):
    return {name: sha256_file(os.path.join(directory, name)) for name in sorted(os.listdir(directory))}


def read_matrix(path):
    """Plain re-read of a well-formed control matrix (whitespace-separated ints)."""
    with open(path, 'rb') as fh:
        return [[int(t) for t in line.split()] for line in fh.read().split(b'\n') if line.split()]


def square_entry(D, n, t, c, g):
    """Bridge formula restated: L_t[c][g] = (D_t(c) - D_0(c) + g) mod n."""
    return (D[t][c] - D[0][c] + g) % n


def linear_squares_text(n, mults):
    """Closed form of the squares of a linear DM: L_t[c][g] = ((a_t - a_0)c + g) mod n."""
    blocks = []
    for t in range(1, len(mults)):
        m = (mults[t] - mults[0]) % n
        blocks.append('\n'.join(' '.join(str((m * c + g) % n) for g in range(n)) for c in range(n)))
    return '\n\n'.join(blocks) + '\n'


def witness_problems(D, n, props):
    probs = []
    dm_fail = [tuple(p) for p in props['dm']['failing_pairs']]
    orth_fail = [tuple(p) for p in props['orthogonal']['failing_pairs']]
    if len(props['dm']['witnesses']) != min(len(dm_fail), CAP):
        probs.append('dm witness count %d for %d failing pairs' % (len(props['dm']['witnesses']), len(dm_fail)))
    if len(props['orthogonal']['witnesses']) != min(len(orth_fail), CAP):
        probs.append('orthogonality witness count %d for %d failing pairs'
                     % (len(props['orthogonal']['witnesses']), len(orth_fail)))
    for w in props['dm']['witnesses']:
        i, j = w['rows']
        c1, c2 = w['columns']
        d1 = (D[i][c1] - D[j][c1]) % n
        d2 = (D[i][c2] - D[j][c2]) % n
        if (i, j) not in dm_fail or c1 == c2 or not d1 == d2 == w['difference']:
            probs.append('dm witness %s invalid' % json.dumps(w))
    for d in props['latin']['details']:
        t = d['square']
        if (d['bad_columns'] > 0) != ('column_witness' in d) or (d['bad_rows'] > 0) != ('row_witness' in d):
            probs.append('latin detail %s lacks or has a spurious witness' % json.dumps(d))
        cw = d.get('column_witness')
        if cw is not None:
            g = cw['column']
            r1, r2 = cw['rows']
            if r1 == r2 or not square_entry(D, n, t, r1, g) == square_entry(D, n, t, r2, g) == cw['symbol']:
                probs.append('latin column witness %s invalid' % json.dumps(d))
        rw = d.get('row_witness')
        if rw is not None:
            c = rw['row']
            g1, g2 = rw['columns']
            if g1 == g2 or not square_entry(D, n, t, c, g1) == square_entry(D, n, t, c, g2) == rw['symbol']:
                probs.append('latin row witness %s invalid' % json.dumps(d))
    for w in props['orthogonal']['witnesses']:
        s, t = w['squares']
        (c1, g1), (c2, g2) = w['cells']
        a, b = w['pair']
        same_a = square_entry(D, n, s, c1, g1) == square_entry(D, n, s, c2, g2) == a
        same_b = square_entry(D, n, t, c1, g1) == square_entry(D, n, t, c2, g2) == b
        if (s, t) not in orth_fail or (c1, g1) == (c2, g2) or not (same_a and same_b):
            probs.append('orthogonality witness %s invalid' % json.dumps(w))
    return probs


def compare(case, out, code, checker_sha):
    exp = case['expect']
    probs = []
    if out.get('checker') != 'checker_b':
        probs.append('JSON checker field %r' % out.get('checker'))
    if out.get('verdict') != exp['verdict']:
        probs.append('verdict %s, expected %s' % (out.get('verdict'), exp['verdict']))
    if out.get('exit_code') != code:
        probs.append('JSON exit_code %r differs from process status %d' % (out.get('exit_code'), code))
    if 'checker_sha256' in out and out['checker_sha256'] != checker_sha:
        probs.append('JSON checker_sha256 differs from the checker file')
    if case['file'] is not None and out.get('input_sha256') != sha256_file(os.path.join(HERE, case['file'])):
        probs.append('JSON input_sha256 differs from the control file')
    for part in exp.get('reason_contains', []):
        if part not in str(out.get('reason', '')):
            probs.append('reason lacks %r' % part)
    if exp['verdict'] not in ('PASS', 'FAIL'):
        if 'properties' in out or 'verdicts' in out:
            probs.append('property verdicts reported despite verdict %s' % out.get('verdict'))
        return probs
    n, k = exp['n'], exp['k']
    if (out.get('well_formed'), out.get('n'), out.get('k'), out.get('num_squares')) != (True, n, k, k - 1):
        probs.append('well_formed/n/k/num_squares = %r' % ((out.get('well_formed'), out.get('n'), out.get('k'),
                                                             out.get('num_squares')),))
        return probs
    props = out['properties']
    dm, latin, orth = props['dm'], props['latin'], props['orthogonal']
    counts = (dm['pairs_checked'], latin['squares_checked'], orth['pairs_checked'])
    if counts != (k * (k - 1) // 2, k - 1, (k - 1) * (k - 2) // 2):
        probs.append('checked counts %r' % (counts,))
    if sorted(dm['failing_pairs']) != sorted(exp['dm_fail_pairs']):
        probs.append('dm failing pairs %s, expected %s' % (dm['failing_pairs'], exp['dm_fail_pairs']))
    got_latin = {str(d['square']): [d['bad_rows'], d['bad_columns']] for d in latin['details']}
    if got_latin != exp['latin_fail']:
        probs.append('latin failures %s, expected %s' % (got_latin, exp['latin_fail']))
    if sorted(latin['failing_squares']) != sorted(int(t) for t in exp['latin_fail']):
        probs.append('latin failing_squares %s' % latin['failing_squares'])
    if sorted(orth['failing_pairs']) != sorted(exp['orth_fail_pairs']):
        probs.append('orthogonal failing pairs %s, expected %s' % (orth['failing_pairs'], exp['orth_fail_pairs']))
    want = {'dm': 'FAIL' if exp['dm_fail_pairs'] else 'PASS',
            'latin': 'FAIL' if exp['latin_fail'] else 'PASS',
            'orthogonal': 'FAIL' if exp['orth_fail_pairs'] else 'PASS'}
    if out.get('verdicts') != want or any(props[name]['verdict'] != v for name, v in want.items()):
        probs.append('per-property verdicts %s, expected %s' % (out.get('verdicts'), want))
    if out['diagnostics']['bridge_agreement']['verdict'] != 'PASS':
        probs.append('bridge_agreement %s' % json.dumps(out['diagnostics']['bridge_agreement']))
    if case['file'] is not None:
        probs += witness_problems(read_matrix(os.path.join(HERE, case['file'])), n, props)
    return probs


def brief(out):
    if out is None:
        return 'no JSON line'
    verdict = out.get('verdict')
    if verdict in ('PASS', 'FAIL') and 'properties' in out:
        p = out['properties']
        lat = {str(d['square']): [d['bad_rows'], d['bad_columns']] for d in p['latin']['details']}
        return 'verdict=%s n=%s k=%s dm_fail=%s latin_fail=%s orth_fail=%s' % (
            verdict, out.get('n'), out.get('k'), json.dumps(p['dm']['failing_pairs'], separators=(',', ':')),
            json.dumps(lat, separators=(',', ':')), json.dumps(p['orthogonal']['failing_pairs'], separators=(',', ':')))
    return 'verdict=%s reason=%s' % (verdict, out.get('reason'))


def main(argv):
    if len(argv) != 2:
        sys.stderr.write('usage: run_controls.py OUTDIR\n')
        return 2
    outdir = argv[1] if os.path.isabs(argv[1]) else os.path.join(HERE, argv[1])
    outrel = os.path.relpath(outdir, HERE)
    os.makedirs(outdir)  # refuses an existing OUTDIR
    with open(EXPECTED, 'rb') as fh:
        expected_bytes = fh.read()
    cases = json.loads(expected_bytes)['cases']
    checker_sha = sha256_file(CHECKER)
    controls_before = snapshot(CONTROLS)
    emitted = {}
    records = []
    for case in cases:
        args = [a.replace('{OUT}', outrel) for a in case['args']]
        proc = subprocess.run([sys.executable, '-I', '-B', CHECKER] + args, cwd=HERE,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = proc.stdout.decode('utf-8', 'replace')
        stderr = proc.stderr.decode('utf-8', 'replace')
        probs = []
        out = None
        lines = stdout.splitlines()
        if len(lines) != 1:
            probs.append('expected exactly one stdout line, got %d' % len(lines))
        else:
            try:
                out = json.loads(lines[0])
            except ValueError as exc:
                probs.append('stdout is not JSON: %s' % exc)
        if proc.returncode != case['expect']['exit']:
            probs.append('exit %d, expected %d' % (proc.returncode, case['expect']['exit']))
        if out is not None:
            probs += compare(case, out, proc.returncode, checker_sha)
        post = case.get('post', {})
        post_info = {}
        if 'emit_linear' in post:
            spec = post['emit_linear']
            path = os.path.join(HERE, spec['path'].replace('{OUT}', outrel))
            if not os.path.isfile(path):
                probs.append('emitted file missing')
            else:
                with open(path, 'rb') as fh:
                    data = fh.read()
                emitted[path] = sha256_bytes(data)
                post_info.update(emit_sha256=emitted[path], emit_bytes=len(data))
                if data != linear_squares_text(spec['n'], spec['mults']).encode('ascii'):
                    probs.append('emitted squares differ from the closed form')
                info = (out or {}).get('emit') or {}
                if info.get('sha256') != emitted[path] or info.get('bytes') != len(data):
                    probs.append('JSON emit record does not match the emitted file')
        if 'unchanged' in post:
            path = os.path.join(HERE, post['unchanged'].replace('{OUT}', outrel))
            after = sha256_file(path) if os.path.isfile(path) else None
            post_info.update(unchanged_before=emitted.get(path), unchanged_after=after)
            if emitted.get(path) is None or after != emitted[path]:
                probs.append('emit target unknown or changed')
        records.append({'name': case['name'], 'kind': case['kind'], 'intended': case['intended'],
                        'argv': ['python3', '-I', '-B', 'checker_b.py'] + args,
                        'exit': proc.returncode, 'stdout': stdout, 'stderr': stderr,
                        'expect': case['expect'], 'post': post_info,
                        'problems': probs, 'as_expected': not probs})
        print('%-26s exit=%d %s -> %s' % (case['name'], proc.returncode, brief(out),
                                          'as expected' if not probs else 'MISMATCH: ' + '; '.join(probs)))
    controls_after = snapshot(CONTROLS)
    outdir_listing = sorted(os.listdir(outdir))
    global_probs = []
    if controls_after != controls_before:
        global_probs.append('controls/ changed during the run')
    if outdir_listing != ['squares.txt']:
        global_probs.append('unexpected OUTDIR content %s' % outdir_listing)
    if sha256_file(CHECKER) != checker_sha:
        global_probs.append('checker_b.py changed during the run')
    n_ok = sum(r['as_expected'] for r in records)
    all_ok = n_ok == len(records) and not global_probs
    results = {'harness': 'run_controls.py', 'python_executable': sys.executable, 'python_version': sys.version,
               'checker': 'checker_b.py', 'checker_sha256': checker_sha,
               'expected_json_sha256': sha256_bytes(expected_bytes), 'outdir': outrel,
               'controls_snapshot': controls_before, 'controls_unchanged': controls_after == controls_before,
               'outdir_listing_before_results': outdir_listing, 'global_problems': global_probs,
               'cases_total': len(records), 'cases_as_expected': n_ok, 'all_as_expected': all_ok,
               'cases': records}
    with open(os.path.join(outdir, 'control_results.json'), 'x', encoding='ascii') as fh:
        json.dump(results, fh, indent=1)
        fh.write('\n')
    for prob in global_probs:
        print('GLOBAL MISMATCH: ' + prob)
    print('%d/%d cases as expected%s; checker_b.py sha256 %s; record %s'
          % (n_ok, len(records), '' if not global_probs else ' (global problems)', checker_sha,
             os.path.join(outrel, 'control_results.json')))
    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
