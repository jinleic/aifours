#!/usr/bin/env python3
"""Independent, non-blind exact replay of the PH7 girth-four certificate.

Rebuild the literal symmetric polynomials, check their pinned coefficient
hashes, verify both complete dyadic covers and strict open-cube positivity,
and exercise coefficient/elimination and graph-hypothesis controls. No author
or reviewer code is imported. This is not a PH7 existence or novelty proof.
"""
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys


ROOT = Path('/Users/jinleic/repos/aifours')
CERT = ROOT / 'mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-girth4-critical-bernstein-certificate.json'
CERT_SHA = 'b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8'
Z = (0, 0, 0, 0, 0, 0)
STRIDES = [3 ** i for i in range(6)]
BASES = [[j for j in range(729) if (j // s) % 3 == 0] for s in STRIDES]


class Rejected(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Rejected(reason)


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def plus(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
        if not out[k]:
            del out[k]
    return out


def multiply(a, b):
    out = {}
    for x, xv in a.items():
        for y, yv in b.items():
            k = tuple(i + j for i, j in zip(x, y))
            out[k] = out.get(k, 0) + xv * yv
    return {k: v for k, v in out.items() if v}


def scaled(poly, c):
    return {k: c * v for k, v in poly.items() if c * v}


def linear_combination(terms):
    out = {}
    for coefficient, factors in terms:
        product = {Z: 1}
        for factor in factors:
            product = multiply(product, factor)
        out = plus(out, scaled(product, coefficient))
    return out


def elementary_polynomials():
    sums = [{Z: 1}] + [{} for _ in range(4)]
    for i in range(6):
        exponent = [0] * 6
        exponent[i] = 1
        var = {tuple(exponent): 1}
        for k in range(4, 0, -1):
            sums[k] = plus(sums[k], multiply(sums[k - 1], var))
    return sums[1:]


def polynomials():
    a, b, c, d = elementary_polynomials()
    q = linear_combination([
        (630, [a, a]), (-324, [a, b]), (-81, [a, c]), (-1908, [a]),
        (81, [b, b]), (36, [b]), (324, [c]), (2452, []),
    ])
    h = linear_combination([
        (7356, [a, a]), (-5724, [a, b]), (108, [a, c]), (972, [a, d]),
        (-18612, [a]), (1890, [b, b]), (-972, [b, c]), (-243, [b, d]),
        (1707, [b]), (243, [c, c]), (3456, [c]), (-1998, [d]), (21094, []),
    ])
    return q, h


def digest_poly(poly):
    rows = [[list(k), str(v)] for k, v in sorted(poly.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def root_coefficients(poly):
    result = [0] * 729
    for exponent, coefficient in poly.items():
        require(len(exponent) == 6 and all(0 <= k <= 2 for k in exponent), 'BAD_DEGREE')
        divisor = 2 ** exponent.count(1)
        result[sum(k * s for k, s in zip(exponent, STRIDES))] = coefficient * (64 // divisor)
    return result


def split(coefficients, axis):
    left = [0] * 729
    right = [0] * 729
    stride = STRIDES[axis]
    for i in BASES[axis]:
        a, b, c = coefficients[i], coefficients[i + stride], coefficients[i + 2 * stride]
        midpoint = a + 2 * b + c
        left[i], left[i + stride], left[i + 2 * stride] = 4 * a, 2 * (a + b), midpoint
        right[i], right[i + stride], right[i + 2 * stride] = midpoint, 2 * (b + c), 4 * c
    return left, right


def partition(paths):
    require(isinstance(paths, list) and all(isinstance(p, str) and p and set(p) <= {'0', '1'} for p in paths), 'BAD_PATH')
    leaves = set(paths)
    require(len(leaves) == len(paths), 'DUPLICATE_LEAF')
    prefixes = {p[:i] for p in leaves for i in range(len(p))}
    require(not (leaves & prefixes), 'PREFIX_COLLISION')
    nodes = leaves | prefixes
    require('' in nodes and all(p + '0' in nodes and p + '1' in nodes for p in prefixes), 'INCOMPLETE_TREE')
    return leaves, prefixes


def audit(poly, paths):
    leaves, prefixes = partition(paths)
    initial = root_coefficients(poly)
    stack = [('', initial, (False,) * 6, (False,) * 6)]
    count = coefficients = open_vertices = 0
    vertices = list(itertools.product((0, 2), repeat=6))
    while stack:
        path, arr, lo, hi = stack.pop()
        if path in leaves:
            require(len(path) >= 6 and all(lo[i] or hi[i] for i in range(6)), 'UNSPLIT_AXIS')
            require(min(arr) >= 0, 'NEGATIVE_COEFFICIENT')
            count += 1
            coefficients += len(arr)
            found = 0
            for vertex in vertices:
                if all(lo[i] if bit == 0 else hi[i] for i, bit in enumerate(vertex)):
                    require(arr[sum(bit * stride for bit, stride in zip(vertex, STRIDES))] > 0, 'NONPOSITIVE_INTERIOR_VERTEX')
                    found += 1
            require(found > 0, 'NO_INTERIOR_VERTEX')
            open_vertices += found
            continue
        require(path in prefixes, 'UNEXPECTED_TREE_NODE')
        axis = len(path) % 6
        left, right = split(arr, axis)
        lhi, rlo = list(hi), list(lo)
        lhi[axis] = True
        rlo[axis] = True
        stack.append((path + '0', left, lo, tuple(lhi)))
        stack.append((path + '1', right, tuple(rlo), hi))
    require(count == len(leaves), 'UNREACHED_LEAF')
    return {'leaves': count, 'coefficient_checks': coefficients, 'open_vertex_checks': open_vertices}


def must_reject(reason, fn):
    try:
        fn()
    except Rejected as err:
        require(str(err) == reason, 'WRONG_REJECTION:' + str(err))
        return reason
    raise Rejected('ACCEPTED_MUTATION:' + reason)


def numeric_esym(values):
    return [F(1)] + [sum(math.prod(c) for c in itertools.combinations(values, k)) for k in range(1, 5)]


def elimination_control():
    samples = [[F(i) for i in (1, 2, 3, 4, 5, 6)],
               [F(1, i) for i in (2, 3, 4, 5, 6, 7)],
               [F(i, 2) for i in (1, 2, 3, 4, 5, 6)], [F(1)] * 6]
    rows = []
    for values in samples:
        _, f1, f2, f3, f4 = numeric_esym(values)
        a = f2 - 4 * f1 + F(74, 9)
        b = f3 - 4 * f2 + F(74, 9) * f1 - F(28, 3)
        h0 = f4 - F(70, 9) * f2 + F(212, 9) * f1 - F(1007, 27)
        h1 = f3 - F(70, 9) * f1 + F(212, 9)
        require(a != 0, 'SAMPLE_A_ZERO')
        x = -b / a
        _, e1, e2, e3, e4 = numeric_esym(values + [x])
        p = e1 - 4
        q = e2 - 4 * p - F(70, 9)
        e4_constraint = e3 - 4 * e2 + F(74, 9) * e1 - F(28, 3)
        e3_constraint = e4 - F(70, 9) * e2 + F(212, 9) * e1 - F(1007, 27)
        qpoly = 81 * (a * a - (f1 - 4) * b)
        hpoly = -243 * (h0 * a - h1 * b)
        require(e4_constraint == 0 and 81 * a * q == qpoly and 243 * a * e3_constraint == -hpoly, 'ELIMINATION')
        require(qpoly > 0 and hpoly > 0, 'SAMPLE_POSITIVITY')
        rows.append({'rates': [str(v) for v in values], 'forced_x': str(x), 'qpoly': str(qpoly), 'hpoly': str(hpoly)})
    return rows


def charpoly(arcs):
    diagonal = list(range(1, 8))
    out = [0] * 8
    for perm in itertools.permutations(range(7)):
        sign = -1 if sum(perm[i] > perm[j] for i in range(7) for j in range(i + 1, 7)) % 2 else 1
        terms = [sign]
        for i, j in enumerate(perm):
            if i == j:
                nxt = [0] * (len(terms) + 1)
                for k, v in enumerate(terms):
                    nxt[k] += diagonal[i] * v
                    nxt[k + 1] += v
                terms = nxt
            else:
                weight = arcs.get((i, j), 0)
                if not weight:
                    terms = []
                    break
                terms = [-weight * v for v in terms]
        for k, v in enumerate(terms):
            out[k] += v
    return out


def graph_control():
    arcs = {(i, (i + 1) % 7): 1 for i in range(7)}
    arcs[(3, 0)] = 1
    es = numeric_esym(list(range(1, 8)))
    c = charpoly(arcs)
    require([c[6], c[5], c[4], c[3]] == [es[1], es[2], es[3], es[4] - 1], 'CHARACTERISTIC_COEFFICIENTS')
    mutated = dict(arcs)
    mutated[(1, 0)] = 2
    require(charpoly(mutated)[5] != es[2], 'TWO_CYCLE_NOT_DETECTED')
    return {'seven_cycle_plus_4cycle': True, 'four_cycle_weight': 1, 'coefficients_6_to_3': c[6:2:-1], 'added_two_cycle_rejected': True}


def main():
    require(len(sys.argv) == 2, 'EXPECTED_NEW_OUTPUT_PATH')
    start = clock()
    data = CERT.read_bytes()
    require(hashlib.sha256(data).hexdigest() == CERT_SHA, 'CERTIFICATE_HASH')
    cert = json.loads(data)
    q, h = polynomials()
    require(len(q) == 168 and len(h) == 435, 'POLYNOMIAL_TERM_COUNT')
    require(digest_poly(q) == cert['Q_coefficients_sha256'], 'Q_DIGEST')
    require(digest_poly(h) == cert['H_coefficients_sha256'], 'H_DIGEST')
    qpaths = cert['Q_positive_compactified_binary_leaf_paths']
    hpaths = cert['H_positive_compactified_binary_leaf_paths']
    qr, hr = audit(q, qpaths), audit(h, hpaths)
    require(qr['leaves'] == 5332 and hr['leaves'] == 5334, 'LEAF_COUNT')
    modified = dict(q)
    modified[Z] = -modified[Z]
    controls = {
        'altered_q_constant': must_reject('NEGATIVE_COEFFICIENT', lambda: audit(modified, qpaths)),
        'missing_leaf': must_reject('INCOMPLETE_TREE', lambda: partition(qpaths[1:])),
        'duplicate_leaf': must_reject('DUPLICATE_LEAF', lambda: partition(qpaths + [qpaths[0]])),
        'prefix_collision': must_reject('PREFIX_COLLISION', lambda: partition(qpaths + [qpaths[0] + '0'])),
    }
    result = {
        'kind': 'PARENT_F129_INDEPENDENT_NONBLIND_EXACT_CERTIFICATE_REPLAY',
        'started_native_clock': start,
        'finished_native_clock': clock(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'certificate_sha256': CERT_SHA,
        'q_digest': digest_poly(q), 'h_digest': digest_poly(h),
        'q': qr, 'h': hr, 'mutation_controls': controls,
        'rational_elimination_samples': elimination_control(),
        'characteristic_graph_control': graph_control(),
        'limits': 'Same-harness, nonblind separate implementation using shared leaf data and literal candidate polynomials. Checks exact certificate and samples, not the all-variable written elimination, Perron theory, PH existence, novelty, or formal-kernel proof.',
    }
    with Path(sys.argv[1]).open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except Rejected as e:
        raise SystemExit('REJECTED: ' + str(e))
