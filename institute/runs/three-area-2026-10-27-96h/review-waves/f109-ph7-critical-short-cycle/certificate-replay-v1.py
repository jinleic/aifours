#!/usr/bin/env python3
"""Independent exact replay of the pinned PH7 coefficient/cover claim.

Only the manifest and its pinned inputs are read.  No author program is imported
or executed.  The receipt is exclusively created next to this program.
"""
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'manifest-v1.json'
MANIFEST_SHA = '8f1fa208bdb84a0fbbb44c12c9a1ce22af20a9076ec5ec650babb09db0cb4f75'
RECEIPT = HERE / 'certificate-receipt-v1.json'
Z5 = (0,) * 5
Z7 = (0,) * 7


class Reject(Exception):
    pass


def require(test, reason):
    if not test:
        raise Reject(reason)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def const(c, n):
    c = F(c)
    return {(0,) * n: c} if c else {}


def add(*polys):
    result = {}
    for poly in polys:
        for key, value in poly.items():
            result[key] = result.get(key, F(0)) + value
    return {k: v for k, v in result.items() if v}


def scale(poly, factor):
    factor = F(factor)
    return {k: v * factor for k, v in poly.items() if v * factor}


def minus(a, b):
    return add(a, scale(b, -1))


def multiply(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(i + j for i, j in zip(ka, kb))
            out[key] = out.get(key, F(0)) + va * vb
    return {k: v for k, v in out.items() if v}


def variable(i, n):
    e = [0] * n
    e[i] = 1
    return {tuple(e): F(1)}


def ymul(left, right):
    out = [{} for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], multiply(a, b))
    return out


def extract_affine(poly):
    parts = [{}, {}, {}]  # constant, t, r
    for exponent, value in poly.items():
        tail = exponent[5:]
        require(tail in ((0, 0), (1, 0), (0, 1)), 'NONAFFINE_EQUATION')
        slot = {(0, 0): 0, (1, 0): 1, (0, 1): 2}[tail]
        parts[slot][exponent[:5]] = value
    return parts


def digest_poly(poly):
    require(all(v.denominator == 1 for v in poly.values()), 'NONINTEGER_COEFFICIENT')
    rows = [[list(k), str(v.numerator)] for k, v in sorted(poly.items())]
    return sha(json.dumps(rows, separators=(',', ':')).encode())


def reconstruct():
    # Work in Q[u0,...,u4,t,r][y].  Derive both equations from the
    # two characteristic polynomials, rather than entering their coefficients.
    us = [variable(i, 7) for i in range(5)]
    t, r = variable(5, 7), variable(6, 7)
    one = const(1, 7)
    diagonal = [one]
    for u in us:
        diagonal = ymul(diagonal, [u, one])
    diagonal = ymul(diagonal, [r, t, one])
    complex_pair = [const(F(17, 9), 7), const(2, 7), one]
    target = ymul([{}, one], ymul(complex_pair, complex_pair))
    require([x.get(Z7, F(0)) for x in target] ==
            [0, F(289, 81), F(68, 9), F(70, 9), 4, 1], 'TARGET_EXPANSION')
    p = minus(diagonal[6], target[4])
    q = minus(minus(diagonal[5], target[3]), multiply(target[4], p))
    factored = ymul(target, [q, p, one])
    b0, a00, a01 = extract_affine(minus(diagonal[4], factored[4]))
    b1, a10, a11 = extract_affine(minus(diagonal[3], factored[3]))

    # Cross-check the six extracted coefficients in elementary-symmetric form.
    # This also guards the y-coefficient indexing and the eliminated p,q.
    u5 = [variable(i, 5) for i in range(5)]
    elementary = [const(1, 5)] + [{} for _ in range(4)]
    for u in u5:
        for k in range(4, 0, -1):
            elementary[k] = add(elementary[k], multiply(elementary[k - 1], u))
    _, s1, s2, s3, s4 = elementary
    C = lambda x: const(x, 5)
    expected = [
        add(s3, scale(s2, -4), scale(s1, F(74, 9)), C(F(-28, 3))),
        add(s2, scale(s1, -4), C(F(74, 9))),
        add(s1, C(-4)),
        add(s4, scale(s2, F(-70, 9)), scale(s1, F(212, 9)), C(F(-1007, 27))),
        add(s3, scale(s1, F(-70, 9)), C(F(212, 9))),
        add(s2, C(F(-70, 9))),
    ]
    actual = [b0, a00, a01, b1, a10, a11]
    require(actual == expected, 'E_COEFFICIENT_MISMATCH')
    det = minus(multiply(a00, a11), multiply(a01, a10))
    tn = minus(multiply(a01, b1), multiply(b0, a11))
    rn = minus(multiply(b0, a10), multiply(a00, b1))
    D = scale(det, 81)
    N = scale(minus(multiply(tn, tn), scale(multiply(rn, det), 4)), -19683)
    return D, N, dict(zip(('b0', 'a00', 'a01', 'b1', 'a10', 'a11'),
                          (len(x) for x in actual)))


def make_trie(paths):
    require(type(paths) is list and paths, 'EMPTY_PATH_LIST')
    trie = {}
    for path in paths:
        require(type(path) is str and path and set(path) <= {'0', '1'}, 'BAD_PATH')
        node = trie
        for bit in path:
            require('$' not in node, 'PREFIX_COLLISION')
            node = node.setdefault(bit, {})
        require('$' not in node, 'DUPLICATE_PATH')
        require(not node, 'PREFIX_COLLISION')
        node['$'] = True
    def validate(node):
        if '$' in node:
            require(len(node) == 1, 'PREFIX_COLLISION')
            return (1, 0)
        require(set(node) == {'0', '1'}, 'MISSING_CHILD')
        l0, n0 = validate(node['0'])
        l1, n1 = validate(node['1'])
        return (l0 + l1, n0 + n1 + 1)
    leaves, internal = validate(trie)
    require(leaves == len(paths) and internal == leaves - 1, 'TREE_COUNTS')
    return trie, internal


def initial_grid(poly, d):
    # For P(u), P(x/(1-x))*prod(1-x)^d has basis coefficient
    # [u^k]P / prod binom(d,k_i).  The common multiple is positive.
    m = d + 1
    common = math.lcm(*(math.comb(d, k) for k in range(m))) ** 5
    stride = [m ** (4 - j) for j in range(5)]
    arr = [0] * (m ** 5)
    for exponent, value in poly.items():
        require(len(exponent) == 5 and all(0 <= e <= d for e in exponent), 'DEGREE')
        require(value.denominator == 1, 'NONINTEGER_COEFFICIENT')
        div = math.prod(math.comb(d, e) for e in exponent)
        require(common % div == 0, 'SCALE')
        arr[sum(exponent[i] * stride[i] for i in range(5))] = value.numerator * (common // div)
    return arr, common, stride


def split_grid(arr, d, stride, axis):
    # Closed-form integer midpoint de Casteljau.  Both children have scale
    # multiplied by 2^d; positive scale changes cannot change signs.
    m = d + 1
    left, right = [0] * len(arr), [0] * len(arr)
    other = [j for j in range(5) if j != axis]
    lw = [[(k, (1 << (d - j)) * math.comb(j, k)) for k in range(j + 1)]
          for j in range(m)]
    rw = [[(j + k, (1 << j) * math.comb(d - j, k)) for k in range(d - j + 1)]
          for j in range(m)]
    for coord in itertools.product(range(m), repeat=4):
        base = sum(coord[h] * stride[other[h]] for h in range(4))
        line = [arr[base + k * stride[axis]] for k in range(m)]
        for j in range(m):
            idx = base + j * stride[axis]
            left[idx] = sum(line[k] * c for k, c in lw[j])
            right[idx] = sum(line[k] * c for k, c in rw[j])
    return left, right


def direct_compact(poly, d, point):
    rate = [x / (1 - x) for x in point]
    result = sum((v * math.prod(rate[i] ** e for i, e in enumerate(k))
                  for k, v in poly.items()), F(0))
    return result * math.prod((1 - x) ** d for x in point)


def evaluate_grid(arr, d, scale_factor, bounds, point):
    # Independently contract Bernstein bases from the last coordinate.
    local = [(x - lo) / (hi - lo) for x, (lo, hi) in zip(point, bounds)]
    result = list(arr)
    m = d + 1
    for axis in range(4, -1, -1):
        z = local[axis]
        w = [math.comb(d, j) * z ** j * (1 - z) ** (d - j) for j in range(m)]
        result = [sum((result[i + j] * w[j] for j in range(m)), F(0))
                  for i in range(0, len(result), m)]
    require(len(result) == 1, 'EVAL_SHAPE')
    return result[0] / scale_factor


def cover(poly, degree, paths):
    trie, internal = make_trie(paths)
    root, common, stride = initial_grid(poly, degree)
    require(min(map(len, paths)) >= 5, 'UNSPLIT_COORDINATE')
    m = degree + 1
    point = tuple(map(F, ('1/3', '2/5', '3/5', '4/7', '5/8')))
    midpoint = (F(1, 2),) * 5
    expected_point = direct_compact(poly, degree, point)
    expected_midpoint = direct_compact(poly, degree, midpoint)
    stats = {'leaves': 0, 'internal_nodes': internal, 'entries': 0,
             'zero_entries': 0, 'interior_corners': 0, 'midpoint_incident_leaves': 0,
             'sample_incident_leaves': 0, 'min_path_depth': min(map(len, paths)),
             'max_path_depth': max(map(len, paths)), 'base_scale': common}
    all_leaf_coefficients = hashlib.sha256()
    def visit(node, path, arr, bounds):
        if '$' in node:
            require(min(arr) >= 0, 'NEGATIVE_BERNSTEIN_COEFFICIENT')
            stats['leaves'] += 1
            stats['entries'] += len(arr)
            stats['zero_entries'] += arr.count(0)
            count = 0
            for bits in itertools.product((0, 1), repeat=5):
                xyz = [bounds[i][bits[i]] for i in range(5)]
                if all(0 < x < 1 for x in xyz):
                    index = sum((degree if bit else 0) * stride[i] for i, bit in enumerate(bits))
                    require(arr[index] > 0, 'NONPOSITIVE_INTERIOR_CORNER')
                    count += 1
            require(count > 0, 'NO_INTERIOR_CORNER')
            stats['interior_corners'] += count
            scale_factor = common * (1 << (degree * len(path)))
            if all(lo <= x <= hi for x, (lo, hi) in zip(midpoint, bounds)):
                stats['midpoint_incident_leaves'] += 1
                require(evaluate_grid(arr, degree, scale_factor, bounds, midpoint) == expected_midpoint,
                        'MIDPOINT_LEAF_EVALUATION')
            if all(lo <= x <= hi for x, (lo, hi) in zip(point, bounds)):
                stats['sample_incident_leaves'] += 1
                require(evaluate_grid(arr, degree, scale_factor, bounds, point) == expected_point,
                        'SAMPLE_LEAF_EVALUATION')
            all_leaf_coefficients.update(json.dumps([path, arr], separators=(',', ':')).encode() + b'\n')
            return
        axis = len(path) % 5
        left, right = split_grid(arr, degree, stride, axis)
        lo, hi = bounds[axis]
        middle = (lo + hi) / 2
        lb, rb = list(bounds), list(bounds)
        lb[axis], rb[axis] = (lo, middle), (middle, hi)
        visit(node['0'], path + '0', left, tuple(lb))
        visit(node['1'], path + '1', right, tuple(rb))
    visit(trie, '', root, ((F(0), F(1)),) * 5)
    require(expected_point > 0 and expected_midpoint > 0, 'POSITIVE_POINT_CONTROL')
    require(stats['leaves'] == len(paths), 'NOT_ALL_LEAVES')
    require(stats['midpoint_incident_leaves'] > 0 and stats['sample_incident_leaves'] > 0, 'POINT_NOT_COVERED')
    stats['leaf_arrays_sha256'] = all_leaf_coefficients.hexdigest()
    stats['interior_midpoint_value'] = str(expected_midpoint)
    stats['interior_sample_value'] = str(expected_point)
    stats['global_one_corner_coefficient'] = root[-1]  # x=(1,1,1,1,1)
    stats['global_zero_corner_coefficient'] = root[0]
    return stats


def expect_reject(label, fn, expected):
    try:
        fn()
    except Reject as exc:
        require(str(exc) == expected, label + ': WRONG_REJECTION:' + str(exc))
        return {'status': 'EXPECTED_REJECTION', 'reason': str(exc)}
    raise Reject(label + ': NOT_REJECTED')


def one_dim_controls():
    # Exact, independent midpoint evaluations for degrees 2 and 4, including
    # both child orientations and a mixed-sign Bernstein array.
    for d, line in ((2, [-5, 2, 7]), (4, [-3, 2, 8, -9, 5])):
        shape = d + 1
        stride = [shape ** (4 - j) for j in range(5)]
        arr = [line[(idx // stride[0]) % shape] for idx in range(shape ** 5)]
        L, R = split_grid(arr, d, stride, 0)
        x = F(2, 7)
        def value(seq, z):
            return sum((F(seq[k]) * math.comb(d, k) * z ** k * (1 - z) ** (d-k)
                        for k in range(shape)), F(0))
        l = [L[k * stride[0]] for k in range(shape)]
        r = [R[k * stride[0]] for k in range(shape)]
        require(value(l, x) / (1 << d) == value(line, x / 2), 'LEFT_SPLIT_CONTROL')
        require(value(r, x) / (1 << d) == value(line, (1 + x) / 2), 'RIGHT_SPLIT_CONTROL')
    return 'PASS: exact degree-2 and degree-4 evaluations on both children'


def main():
    require(not RECEIPT.exists(), 'RECEIPT_EXISTS')
    started = clock()
    manifest_bytes = MANIFEST.read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'MANIFEST_HASH')
    manifest = json.loads(manifest_bytes)
    inputs = []
    cert = None
    for item in manifest['inputs_in_read_order']:
        data = Path(item['path']).read_bytes()
        require(sha(data) == item['sha256'], 'INPUT_HASH:' + item['path'])
        require(len(data) == item['bytes'] and data.count(b'\n') == item['LF'], 'INPUT_SIZE:' + item['path'])
        inputs.append({'path': item['path'], 'sha256': sha(data), 'bytes': len(data), 'LF': data.count(b'\n')})
        if item['role'] == 'Author dyadic-cover certificate':
            cert = json.loads(data)
    require(cert is not None, 'MISSING_CERTIFICATE')
    require(cert['z'] == '8/9' and cert['split_axis'] == 'path depth modulo 5', 'CERTIFICATE_CONVENTIONS')
    D, N, equations = reconstruct()
    polys = {'D': (D, 2), 'N': (N, 4)}
    controls = {'de_casteljau': one_dim_controls()}
    results = {}
    for name, (poly, degree) in polys.items():
        paths = cert[name + '_positive_compactified_binary_leaf_paths']
        digest = digest_poly(poly)
        require(digest == cert[name + '_coefficients_sha256'], 'COEFFICIENT_DIGEST:' + name)
        require(len(poly) == cert[name + '_terms'], 'TERM_COUNT:' + name)
        require(cert[name + '_variable_degrees'] == [degree] * 5, 'DEGREE_METADATA:' + name)
        require([max(k[i] for k in poly) for i in range(5)] == [degree] * 5, 'ACTUAL_DEGREE:' + name)
        controls[name + '_missing_leaf'] = expect_reject('missing', lambda: make_trie(paths[:-1]), 'MISSING_CHILD')
        controls[name + '_duplicate_leaf'] = expect_reject('duplicate', lambda: make_trie(paths + [paths[0]]), 'DUPLICATE_PATH')
        controls[name + '_prefix_leaf'] = expect_reject('prefix', lambda: make_trie(paths + [paths[0] + '0']), 'PREFIX_COLLISION')
        changed = dict(poly)
        first = min(changed)
        changed[first] += 1
        controls[name + '_altered_coefficient'] = expect_reject(
            'coefficient', lambda: require(digest_poly(changed) == cert[name + '_coefficients_sha256'], 'COEFFICIENT_DIGEST'),
            'COEFFICIENT_DIGEST')
        controls[name + '_sign_flip'] = expect_reject('sign', lambda: cover(scale(poly, -1), degree, paths),
                                                      'NEGATIVE_BERNSTEIN_COEFFICIENT')
        result = cover(poly, degree, paths)
        require(result['global_one_corner_coefficient'] == 0, 'EXPECTED_ZERO_BOUNDARY_CORNER')
        controls[name + '_closed_boundary'] = expect_reject(
            'boundary', lambda: require(result['global_one_corner_coefficient'] > 0, 'ZERO_BOUNDARY_NOT_STRICT'),
            'ZERO_BOUNDARY_NOT_STRICT')
        result.update({'coefficient_sha256': digest, 'terms': len(poly), 'degrees': [degree] * 5})
        results[name] = result
    receipt = {'kind': 'independent_same_harness_exact_certificate_replay',
               'clock_started': started, 'clock_finished': clock(),
               'manifest_sha256': sha(manifest_bytes), 'inputs_in_order': inputs,
               'code_sha256': sha(Path(__file__).read_bytes()), 'equation_term_counts': equations,
               'results': results, 'controls': controls,
               'limits': 'Trusted Python standard library arbitrary-precision integers/Fractions, this implementation and SHA-256. No author code executed or imported; not formal/kernel, human, cross-family, PH existence or novelty verification.'}
    encoded = (json.dumps(receipt, indent=2) + '\n').encode()
    with RECEIPT.open('xb') as out:
        out.write(encoded)
    print(json.dumps({'status': 'PASS', 'receipt': str(RECEIPT), 'receipt_sha256': sha(encoded),
                      'code_sha256': receipt['code_sha256'], 'clock_started': started,
                      'clock_finished': receipt['clock_finished'], 'results': results,
                      'controls': controls}, indent=2))


if __name__ == '__main__':
    main()
