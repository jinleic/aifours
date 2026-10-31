#!/usr/bin/env python3
"""Independent exact five-variable coefficient/cover audit; no author imports.

The coefficient construction starts from the two displayed actual coefficient
identities, not from either author checker. NumPy is used only as an object-array
container: every entry and every arithmetic operation is a Python arbitrary-
precision integer. Script and receipt are confined to this review directory.
"""
import datetime
import hashlib
import itertools
import json
import math
import os
import signal
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / 'manifest-v1.json'
RESULT = ROOT / 'certificate-results-v1.json'
MANIFEST_SHA = 'a30381bbdf9a0a8722122243450e9ee608f7f197948ecef30ee333fb38496f8f'
CERT_SHA = 'd1195a6f0099d105eb34e5a6acbeb1fec3d81c333658af7a3c8b2ea5ac79f2c9'
NAMES = ('b0', 'b1', 'b3', 'quadratic_discriminant')
LEAVES = (657, 567, 522, 565)
ZERO = (0, 0, 0, 0, 0)
MAX_DEPTH = 20
WALL_SECONDS = 600


class CheckFailure(Exception):
    def __init__(self, code, detail=''):
        self.code = code
        self.detail = detail
        super().__init__(code + (': ' + str(detail) if detail else ''))


def require(test, code, detail=''):
    if not test:
        raise CheckFailure(code, detail)


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pairs_without_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'DUPLICATE_JSON_KEY', key)
        result[key] = value
    return result


def json_from(data):
    return json.loads(data.decode('utf-8'), object_pairs_hook=pairs_without_duplicates)


def pin_inputs():
    raw_manifest = MANIFEST.read_bytes()
    require(sha(raw_manifest) == MANIFEST_SHA, 'MANIFEST_HASH')
    manifest = json_from(raw_manifest)
    rows = manifest['inputs_in_read_order']
    require(len(rows) == 5, 'INPUT_COUNT')
    pinned = []
    for row in rows:
        data = Path(row['path']).read_bytes()
        data.decode('utf-8')
        facts = (sha(data), len(data), data.count(b'\n'))
        require(facts == (row['sha256'], row['bytes'], row['LF']), 'INPUT_PIN', row['path'])
        require(data.endswith(b'\n'), 'INPUT_FINAL_LF', row['path'])
        pinned.append({'path': row['path'], 'sha256': facts[0], 'bytes': facts[1], 'LF': facts[2]})
        if row['sha256'] == CERT_SHA:
            cert = json_from(data)
    require(pinned[3]['sha256'] == CERT_SHA, 'CERTIFICATE_POSITION')
    return cert, pinned, {'sha256': sha(raw_manifest), 'bytes': len(raw_manifest), 'LF': raw_manifest.count(b'\n')}


def constant(c):
    return {ZERO: int(c)} if c else {}


def plus(*terms):
    out = {}
    for a in terms:
        for k, v in a.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def times_scalar(a, c):
    return {k: c*v for k, v in a.items() if c*v}


def difference(a, b):
    return plus(a, times_scalar(b, -1))


def times(a, b):
    out = {}
    for (a0, a1, a2, a3, a4), av in a.items():
        for (b0, b1, b2, b3, b4), bv in b.items():
            k = (a0+b0, a1+b1, a2+b2, a3+b3, a4+b4)
            out[k] = out.get(k, 0) + av*bv
    return {k: v for k, v in out.items() if v}


def square(a):
    items = list(a.items())
    out = {}
    for i, (k, av) in enumerate(items):
        for j in range(i, len(items)):
            h, bv = items[j]
            e = (k[0]+h[0], k[1]+h[1], k[2]+h[2], k[3]+h[3], k[4]+h[4])
            out[e] = out.get(e, 0) + av*bv*(1 if i == j else 2)
    return {k: v for k, v in out.items() if v}


def exact_div(a, d):
    require(all(v % d == 0 for v in a.values()), 'POLYNOMIAL_EXACT_DIVISION', d)
    return {k: v//d for k, v in a.items() if v}


def variables_and_elementaries():
    var = []
    for i in range(5):
        key = tuple(1 if j == i else 0 for j in range(5))
        var.append({key: 1})
    elem = []
    for order in range(1, 5):
        accum = []
        for indices in itertools.combinations(range(5), order):
            term = constant(1)
            for i in indices:
                term = times(term, var[i])
            accum.append(term)
        elem.append(plus(*accum))
    return var, elem


VAR, ELEMENTARIES = variables_and_elementaries()


def base_terms(z9=8, coefficient_delta=0):
    # z=z9/9, and D=y*((y+1)^2+z)^2 has coefficients
    # K=(54+2*z9)/9, L=(36+4*z9)/9, M=(9+z9)^2/81.
    # coefficient_delta changes K alone for the intended mutation control.
    e1, e2, e3, e4 = ELEMENTARIES
    k9 = 54 + 2*z9 + coefficient_delta
    l9 = 36 + 4*z9
    m81 = (9+z9)**2
    a = plus(times_scalar(e2, 9), times_scalar(e1, -36), constant(144-k9))
    b = plus(e1, constant(-4))
    d0 = plus(times_scalar(e3, 9), times_scalar(b, -k9), constant(-l9))
    c0 = difference(d0, times_scalar(a, 4))
    e = plus(times_scalar(e2, 9), constant(-k9))
    f0 = plus(times_scalar(e4, 81), times_scalar(a, -k9), times_scalar(b, -9*l9), constant(-m81))
    h = times(times(VAR[0], VAR[1]), VAR[2])
    o = plus(VAR[3], VAR[4])
    delta0 = difference(times(a, e), times_scalar(times(b, d0), 9))
    delta1 = times_scalar(times(b, h), 81)
    t0 = difference(times(b, f0), times(c0, e))
    t1 = times_scalar(times(h, difference(e, times_scalar(times(b, o), 9))), 9)
    r0 = difference(times_scalar(times(c0, d0), 9), times(a, f0))
    r1 = times_scalar(times(h, difference(times(a, o), plus(c0, d0))), 81)
    r2 = times_scalar(square(h), 729)
    return delta0, delta1, t0, t1, r0, r1, r2


def n0_only(z9=8, coefficient_delta=0):
    d0, _, t0, _, r0, _, _ = base_terms(z9, coefficient_delta)
    return exact_div(plus(times_scalar(square(t0), -9), times_scalar(times(r0, d0), 4)), 3)


def construct():
    d0, d1, t0, t1, r0, r1, r2 = base_terms()
    n0 = exact_div(plus(times_scalar(square(t0), -9), times_scalar(times(r0, d0), 4)), 3)
    n1 = exact_div(plus(times_scalar(times(t0, t1), -18), times_scalar(plus(times(r0, d1), times(r1, d0)), 4)), 3)
    n2 = exact_div(plus(times_scalar(square(t1), -9), times_scalar(plus(times(r1, d1), times(r2, d0)), 4)), 3)
    n3 = exact_div(times_scalar(times(r2, d1), 4), 3)
    b0 = n0
    b1 = plus(n0, exact_div(n1, 3))
    b2 = plus(n0, exact_div(times_scalar(n1, 2), 3), exact_div(n2, 3))
    b3 = plus(n0, n1, n2, n3)
    g = difference(times_scalar(times(b1, b3), 4), times_scalar(square(b2), 3))
    return (n0, n1, n2, n3), (b0, b1, b2, b3), {'b0': b0, 'b1': b1, 'b3': b3, 'quadratic_discriminant': g}


def evaluate(poly, point):
    return sum((Fraction(v) * math.prod(point[j]**k[j] for j in range(5)) for k, v in poly.items()), Fraction(0))


def direct_equation_controls(n, bs):
    rate_sets = [tuple(map(Fraction, ('1/2', '2/3', '3/2', '5/4', '7/5'))),
                 tuple(map(Fraction, ('3', '1/4', '7/3', '2', '5/3')))]
    cases = []
    for u in rate_sets:
        es = [sum((math.prod(c) for c in itertools.combinations(u, k)), Fraction(0)) for k in range(1, 5)]
        e1, e2, e3, e4 = es
        o = u[3]+u[4]
        for theta in (Fraction(0), Fraction(1, 3), Fraction(1)):
            w = theta*u[0]*u[1]*u[2]
            def eq(t, r):
                p = e1+t-4
                q = e2+t*e1+r-4*p-Fraction(70, 9)
                return (e3+t*e2+r*e1-w-(4*q+Fraction(70, 9)*p+Fraction(68, 9)),
                        e4+t*e3+r*e2-w*(o+t)-(Fraction(70, 9)*q+Fraction(68, 9)*p+Fraction(289, 81)))
            c = eq(0, 0)
            xt = eq(1, 0)
            xr = eq(0, 1)
            at = tuple(xt[i]-c[i] for i in range(2))
            ar = tuple(xr[i]-c[i] for i in range(2))
            require(eq(Fraction(2, 7), Fraction(3, 11)) == tuple(c[i]+at[i]*Fraction(2, 7)+ar[i]*Fraction(3, 11) for i in range(2)), 'EQUATION_NONLINEAR')
            den = at[0]*ar[1]-ar[0]*at[1]
            tn = -c[0]*ar[1]+ar[0]*c[1]
            rn = -at[0]*c[1]+c[0]*at[1]
            expected = -19683*(tn*tn-4*rn*den)
            actual = sum((evaluate(n[j], u)*theta**j for j in range(4)), Fraction(0))
            b = [evaluate(x, u) for x in bs]
            bern = b[0]*(1-theta)**3+3*b[1]*theta*(1-theta)**2+3*b[2]*theta**2*(1-theta)+b[3]*theta**3
            require(expected == actual == bern, 'DIRECT_EQUATION_CUBIC_MISMATCH')
            cases.append({'rates': [str(x) for x in u], 'theta': str(theta), 'exact_equations_vs_cubic_vs_bernstein': True})
    return cases


def coefficient_hash(poly):
    rows = [[list(k), str(v)] for k, v in sorted(poly.items())]
    return sha(json.dumps(rows, separators=(',', ':')).encode('ascii'))


def individual_degrees(poly):
    require(bool(poly), 'EMPTY_POLYNOMIAL')
    return [max(k[j] for k in poly) for j in range(5)]


def validate_headers(cert):
    require(set(cert) == {'z', 'theta_domain', 'rate_compactification', 'split_axis', 'records', 'identity', 'scope'}, 'CERTIFICATE_KEYS')
    require(cert['z'] == '8/9', 'DOMAIN_Z')
    require(cert['theta_domain'] == '[0,1]', 'DOMAIN_THETA')
    require(cert['rate_compactification'] == 'ui=xi/(1-xi)', 'DOMAIN_RATES')
    require(cert['split_axis'] == 'path depth modulo5', 'SPLIT_AXIS')
    require(cert['identity'] == 'N=b0(1-theta)^3+theta[3b1(1-theta)^2+3b2 theta(1-theta)+b3 theta^2]', 'IDENTITY')
    require([r['name'] for r in cert['records']] == list(NAMES), 'RECORD_ORDER')
    for rec, count in zip(cert['records'], LEAVES):
        require(set(rec) == {'name', 'individual_degrees', 'coefficient_terms', 'coefficient_sha256', 'positive_leaf_paths'}, 'RECORD_KEYS')
        require(len(rec['positive_leaf_paths']) == count, 'PINNED_LEAF_COUNT', rec['name'])


def coefficients_against_record(poly, rec):
    require(len(poly) == rec['coefficient_terms'], 'COEFFICIENT_TERMS', rec['name'])
    require(individual_degrees(poly) == rec['individual_degrees'], 'INDIVIDUAL_DEGREES', rec['name'])
    digest = coefficient_hash(poly)
    require(digest == rec['coefficient_sha256'], 'COEFFICIENT_HASH', rec['name'])
    return digest


def trie_for(paths):
    require(type(paths) is list and bool(paths), 'EMPTY_COVER')
    root = {}
    for path in paths:
        require(type(path) is str and 5 <= len(path) <= MAX_DEPTH and all(c in '01' for c in path), 'INVALID_PATH', path)
        node = root
        for ch in path:
            require('end' not in node, 'PREFIX_COLLISION', path)
            node = node.setdefault(ch, {})
        require(not node, 'DUPLICATE_OR_PREFIX_COLLISION', path)
        node['end'] = True
    def inspect(node):
        if 'end' in node:
            require(set(node) == {'end'}, 'PREFIX_COLLISION')
            return 1
        require(set(node) == {'0', '1'}, 'COVER_MISSING_BRANCH', str(sorted(node)))
        return inspect(node['0'])+inspect(node['1'])
    require(inspect(root) == len(paths), 'COVER_LEAF_COUNT')
    return root


def grid(poly, degrees):
    require(len(degrees) == 5 and all(type(d) is int and 1 <= d <= 8 for d in degrees), 'GRID_DEGREE')
    common = math.prod(math.lcm(*(math.comb(d, i) for i in range(d+1))) for d in degrees)
    data = np.zeros(tuple(d+1 for d in degrees), dtype=object)
    for k, v in poly.items():
        require(len(k) == 5 and all(0 <= k[j] <= degrees[j] for j in range(5)), 'GRID_EXPONENT')
        den = math.prod(math.comb(degrees[j], k[j]) for j in range(5))
        require(common % den == 0, 'GRID_SCALE')
        data[k] = v*(common//den)
    require(data.dtype == np.dtype(object), 'GRID_NONEXACT_DTYPE')
    return data, common


def bisect(data, axis):
    # Exact closed-form midpoint subdivision. All child coefficients are
    # scaled by 2**d, uniformly and positively, after each split.
    front = np.moveaxis(data, axis, 0)
    d = front.shape[0]-1
    left = np.empty(front.shape, dtype=object)
    right = np.empty(front.shape, dtype=object)
    for j in range(d+1):
        v = front[0].copy()
        for k in range(1, j+1):
            c = math.comb(j, k)
            v += front[k] if c == 1 else front[k]*c
        v *= 1 << (d-j)
        left[j] = v
        v = front[j].copy()
        for k in range(1, d-j+1):
            c = math.comb(d-j, k)
            v += front[j+k] if c == 1 else front[j+k]*c
        v *= 1 << j
        right[j] = v
    return np.moveaxis(left, 0, axis), np.moveaxis(right, 0, axis)


def check_cover(poly, degrees, paths):
    tree = trie_for(paths)
    initial, scale = grid(poly, degrees)
    counts = {'leaves': 0, 'bernstein_coefficients_checked': 0, 'open_corners_checked': 0,
              'min_depth': MAX_DEPTH+1, 'max_depth': 0, 'root_integer_scale': str(scale)}
    def walk(node, data, bounds, depth):
        if 'end' in node:
            require(type(data.flat[0]) is int, 'NON_PYTHON_INTEGER_COEFFICIENT')
            minimum = min(data.flat)
            require(minimum >= 0, 'NEGATIVE_BERNSTEIN_COEFFICIENT')
            checked = 0
            for corner in itertools.product((0, 1), repeat=5):
                if all(0 < bounds[j][0]+corner[j] < (1 << bounds[j][1]) for j in range(5)):
                    idx = tuple(degrees[j] if corner[j] else 0 for j in range(5))
                    require(data[idx] > 0, 'OPEN_CORNER_NOT_POSITIVE', idx)
                    checked += 1
            require(checked > 0, 'NO_OPEN_CORNER')
            counts['leaves'] += 1
            counts['bernstein_coefficients_checked'] += data.size
            counts['open_corners_checked'] += checked
            counts['min_depth'] = min(counts['min_depth'], depth)
            counts['max_depth'] = max(counts['max_depth'], depth)
            return
        axis = depth % 5
        left, right = bisect(data, axis)
        k, h = bounds[axis]
        for bit, child, arr in ((0, node['0'], left), (1, node['1'], right)):
            b = list(bounds)
            b[axis] = (2*k+bit, h+1)
            walk(child, arr, tuple(b), depth+1)
    walk(tree, initial, ((0, 0),)*5, 0)
    require(counts['leaves'] == len(paths), 'VISITED_LEAF_COUNT')
    return counts


def expect_failure(name, wanted, action):
    try:
        action()
    except CheckFailure as exc:
        require(exc.code == wanted, 'WRONG_CONTROL_FAILURE', name+' got '+exc.code+' wanted '+wanted)
        return {'name': name, 'expected': wanted, 'observed': exc.code, 'detail': exc.detail, 'pass': True}
    raise CheckFailure('CONTROL_ACCEPTED_INVALID_CASE', name)


def expect_hash_failure(poly, rec):
    require(coefficient_hash(poly) == rec['coefficient_sha256'], 'COEFFICIENT_HASH', rec['name'])


def timed_out(signum, frame):
    raise CheckFailure('WALL_CLOCK_LIMIT', WALL_SECONDS)


def main():
    started_at = now()
    started = time.monotonic()
    signal.signal(signal.SIGALRM, timed_out)
    signal.alarm(WALL_SECONDS)
    require(not RESULT.exists(), 'REFUSE_OUTPUT_OVERWRITE', str(RESULT))
    cert, inputs, manifest = pin_inputs()
    validate_headers(cert)
    n, bs, polynomials = construct()
    numeric = direct_equation_controls(n, bs)
    records = []
    for rec in cert['records']:
        poly = polynomials[rec['name']]
        digest = coefficients_against_record(poly, rec)
        tic = time.monotonic()
        stats = check_cover(poly, rec['individual_degrees'], rec['positive_leaf_paths'])
        stats.update({'name': rec['name'], 'individual_degrees': individual_degrees(poly),
                      'coefficient_terms': len(poly), 'coefficient_sha256': digest,
                      'elapsed_seconds': round(time.monotonic()-tic, 3)})
        records.append(stats)
        print('checked', rec['name'], json.dumps(stats, sort_keys=True), flush=True)
    require(sum(x['leaves'] for x in records) == 2311, 'TOTAL_LEAVES')
    controls = []
    controls.append(expect_failure('alter K=70/9 to 71/9 in the actual equations', 'COEFFICIENT_HASH',
                                   lambda: expect_hash_failure(n0_only(coefficient_delta=1), cert['records'][0])))
    bad = dict(polynomials['b0'])
    first = sorted(bad)[0]
    bad[first] += 1 if bad[first] >= 0 else -1
    controls.append(expect_failure('alter one exact b0 coefficient', 'COEFFICIENT_HASH',
                                   lambda: expect_hash_failure(bad, cert['records'][0])))
    controls.append(expect_failure('remove the first b0 leaf', 'COVER_MISSING_BRANCH',
                                   lambda: trie_for(cert['records'][0]['positive_leaf_paths'][1:])))
    bad_theta_cert = dict(cert)
    bad_theta_cert['theta_domain'] = '[0,2]'
    controls.append(expect_failure('wrong theta domain metadata [0,2]', 'DOMAIN_THETA', lambda: validate_headers(bad_theta_cert)))
    wrong_theta_b1 = plus(n[0], exact_div(times_scalar(n[1], 2), 3))
    controls.append(expect_failure('use theta=2*tau instead of theta=tau', 'COEFFICIENT_HASH',
                                   lambda: expect_hash_failure(wrong_theta_b1, cert['records'][1])))
    wrong_z_cert = dict(cert)
    wrong_z_cert['z'] = '1'
    controls.append(expect_failure('wrong z metadata 1', 'DOMAIN_Z', lambda: validate_headers(wrong_z_cert)))
    controls.append(expect_failure('rebuild equations at wrong z=1', 'COEFFICIENT_HASH',
                                   lambda: expect_hash_failure(n0_only(z9=9), cert['records'][0])))
    full32 = [''.join(bits) for bits in itertools.product('01', repeat=5)]
    positive = plus(constant(1), *(square(v) for v in VAR))
    positive_stats = check_cover(positive, [2]*5, full32)
    require(positive_stats['leaves'] == 32, 'POSITIVE_CONTROL_LEAVES')
    controls.append({'name': 'genuine P(u)=1+sum(u_i^2)>0 on all positive rates', 'pass': True, **positive_stats})
    controls.append(expect_failure('negative polynomial P(u)=-1', 'NEGATIVE_BERNSTEIN_COEFFICIENT',
                                   lambda: check_cover(constant(-1), [2]*5, full32)))
    controls.append(expect_failure('zero polynomial fails strict open-corner condition', 'OPEN_CORNER_NOT_POSITIVE',
                                   lambda: check_cover({}, [2]*5, full32)))
    require(len(controls) == 10 and all(c['pass'] for c in controls), 'CONTROLS_INCOMPLETE')
    signal.alarm(0)
    report = {'result': 'EXACT_COEFFICIENTS_AND_ALL_COVERS_PASS',
              'scope': 'coefficient equations and four positive polynomials only; no graph/PH caller or novelty adoption',
              'started_native_clock': started_at, 'finished_native_clock': now(),
              'elapsed_seconds': round(time.monotonic()-started, 3), 'wall_limit_seconds': WALL_SECONDS,
              'python': sys.version, 'numpy': np.__version__,
              'script_sha256': sha(Path(__file__).read_bytes()), 'manifest': manifest,
              'pinned_inputs': inputs, 'direct_equation_controls': numeric,
              'records': records, 'controls': controls,
              'totals': {'leaves': sum(x['leaves'] for x in records),
                         'bernstein_coefficients_checked': sum(x['bernstein_coefficients_checked'] for x in records),
                         'open_corners_checked': sum(x['open_corners_checked'] for x in records)}}
    with RESULT.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print('RESULT', report['result'], 'totals', json.dumps(report['totals']), 'elapsed_seconds', report['elapsed_seconds'], flush=True)
    print('receipt_sha256', sha(RESULT.read_bytes()), 'receipt', RESULT, flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('INCONCLUSIVE_OR_CONTROL_FAILURE', type(exc).__name__, str(exc), flush=True)
        raise
