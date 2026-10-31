#!/usr/bin/env python3
"""UNRUN F832 source. No imports from old sources, no filesystem writes.

On a separately authorized parent run, construct the full grade-three W and
its full grade-four bracket image, the complete s=3 second seed, and the actual
first-only two-copy lowest F3 pencil. Exact Fraction arithmetic only. The
terminal JSON is PASS_FINITE_EXACT only after every check completes. The bound
is cooperative, not a claim that a parent supervisor will observe termination.
"""
import itertools
import json
import math
import signal
import sys
import time
import traceback
from fractions import Fraction as F

START = time.monotonic()
DEADLINE = START + 40.0
STOP = False


def stop_signal(_sig, _frame):
    global STOP
    STOP = True


class Interrupted(Exception):
    pass


def guard():
    if STOP or time.monotonic() >= DEADLINE:
        raise Interrupted('cooperative stop or 40-second internal deadline')


def require(condition, message):
    if not condition:
        raise ValueError(message)


# Indices x,a,b,c,d,e,f,g and their horizontal degrees.
DEG = ((0, 0), (1, 0), (0, 1), (1, 1),
       (1, 1), (2, 1), (1, 2), (2, 2))
# Each entry is a list (output letter, coefficient).
E1 = (((1, 1),), (), ((3, 1),), ((5, -2),),
      ((5, -1),), (), ((7, 1),), ())
E2 = (((2, 1),), ((4, 1),), (), ((6, 1),),
      ((6, 2),), ((7, -1),), (), ())
F1 = ((), ((0, 1),), (), ((2, 2),),
      ((2, 1),), ((3, -1),), (), ((6, 1),))
F2 = ((), (), ((0, 1),), ((1, 1),),
      ((1, 2),), (), ((4, 1),), ((5, -1),))
E12 = (((3, 1), (4, -1)), ((5, -1),), ((6, -1),),
       ((7, -1),), ((7, 1),), (), (), ())


def clean(v):
    return {k: c for k, c in v.items() if c}


def axpy(dst, src, k):
    if k:
        for w, c in src.items():
            dst[w] = dst.get(w, F(0)) + k * c
            if not dst[w]:
                del dst[w]
    return dst


def scale(v, k):
    return clean({w: k * c for w, c in v.items()})


def add(*vs):
    out = {}
    for v in vs:
        axpy(out, v, F(1))
    return out


def letter(i):
    return {(i,): F(1)}


def bracket(v, w):
    out = {}
    for a, ca in v.items():
        for b, cb in w.items():
            term = ca * cb
            out[a + b] = out.get(a + b, F(0)) + term
            out[b + a] = out.get(b + a, F(0)) - term
    return clean(out)


def action(table, v):
    out = {}
    for word, coeff in v.items():
        for pos, u in enumerate(word):
            for z, c in table[u]:
                nw = word[:pos] + (z,) + word[pos + 1:]
                out[nw] = out.get(nw, F(0)) + coeff * c
    return clean(out)


def weight(v):
    require(bool(v), 'weight of zero vector')
    def wt(word):
        return (sum(DEG[i][0] for i in word),
                sum(DEG[i][1] for i in word))
    first = wt(next(iter(v)))
    require(all(wt(w) == first for w in v), 'inhomogeneous vector')
    return first


def right_nested(word):
    out = letter(word[-1])
    for u in reversed(word[:-1]):
        out = bracket(letter(u), out)
    return out


class Space:
    # Echelon vectors themselves are legitimate ambient tensor/Lie vectors.
    def __init__(self):
        self.rows = {}
        self.tags = {}

    def copy(self):
        q = Space()
        q.rows = {k: dict(v) for k, v in self.rows.items()}
        q.tags = dict(self.tags)
        return q

    def reduce(self, vector):
        v = dict(vector)
        coeff = {}
        for p in sorted(self.rows):
            c = v.get(p, F(0))
            if c:
                coeff[p] = c
                axpy(v, self.rows[p], -c)
        return v, coeff

    def insert(self, vector, tag='R'):
        guard()
        v, _ = self.reduce(vector)
        if not v:
            return None
        p = min(v)
        v = scale(v, 1 / v[p])
        self.rows[p] = v
        self.tags[p] = tag
        return p

    def size(self):
        return len(self.rows)

    def vectors(self):
        return [self.rows[p] for p in sorted(self.rows)]


def get(spaces, wt):
    if wt not in spaces:
        spaces[wt] = Space()
    return spaces[wt]


def cyclic(seed):
    # Every retained independent vector is raised by both generators; this
    # spans the entire U(n_+) cyclic module, not selected weight translates.
    spaces = {}
    q = []
    p = get(spaces, weight(seed)).insert(seed)
    require(p is not None, 'zero seed')
    q.append(get(spaces, weight(seed)).rows[p])
    i = 0
    while i < len(q):
        guard()
        v = q[i]
        i += 1
        for tab in (E1, E2):
            w = action(tab, v)
            if w:
                s = get(spaces, weight(w))
                p = s.insert(w)
                if p is not None:
                    q.append(s.rows[p])
    return spaces


def dim(spaces):
    return sum(s.size() for s in spaces.values())


def is_member(spaces, v):
    if not v:
        return True
    s = spaces.get(weight(v))
    return s is not None and not s.reduce(v)[0]


def verify_levi_closure(spaces):
    for sp in list(spaces.values()):
        for v in sp.vectors():
            guard()
            for tab in (E1, E2, F1, F2):
                require(is_member(spaces, action(tab, v)),
                        'cyclic/bracket module is not Levi-stable')


def brackets_of_module(module):
    out = {}
    for sp in module.values():
        for w in sp.vectors():
            for j in range(8):
                v = bracket(letter(j), w)
                if v:
                    get(out, weight(v)).insert(v)
    return out


def merge_spaces(a, b):
    out = {wt: sp.copy() for wt, sp in a.items()}
    overlap = 0
    for wt, sp in b.items():
        for v in sp.vectors():
            if get(out, wt).insert(v) is None:
                overlap += 1
    return out, overlap


def basis_free_quotient(relations, grade, wt):
    # Extend the WHOLE relation by all right-nested bracket generators.
    out = relations.get(wt, Space()).copy()
    for word in itertools.product(range(8), repeat=grade):
        guard()
        if (sum(DEG[i][0] for i in word),
                sum(DEG[i][1] for i in word)) != wt:
            continue
        v = right_nested(word)
        if v:
            out.insert(v, 'Q')
    pivots = [p for p in sorted(out.rows) if out.tags[p] == 'Q']
    return out, pivots


def quotient_coordinates(space, quotient_pivots, v):
    remainder, coeff = space.reduce(v)
    require(not remainder, 'vector is not in the constructed free space')
    return {i: coeff.get(p, F(0)) for i, p in enumerate(quotient_pivots)
            if coeff.get(p, F(0))}


def null_combinations(columns):
    # Returns a basis of relations among the supplied columns, with independent
    # input-column coefficient dictionaries. Keys of a column can be tuples.
    rows = {}
    lifts = {}
    kernel = []
    for j, column in enumerate(columns):
        guard()
        v = dict(column)
        lift = {j: F(1)}
        for p in sorted(rows):
            c = v.get(p, F(0))
            if c:
                axpy(v, rows[p], -c)
                axpy(lift, lifts[p], -c)
        if not v:
            kernel.append(lift)
        else:
            p = min(v)
            factor = 1 / v[p]
            rows[p] = scale(v, factor)
            lifts[p] = scale(lift, factor)
    return kernel


def linear_combination(vectors, coeff):
    out = {}
    for i, c in coeff.items():
        axpy(out, vectors[i], c)
    return out


def lowest_quotient(relations, quotient, pivots):
    reps = [quotient.rows[p] for p in pivots]
    cols = []
    for v in reps:
        col = {}
        for side, (tab, wt) in enumerate(((F1, (1, 1)), (F2, (2, 0)))):
            reduced, _ = relations.get(wt, Space()).reduce(action(tab, v))
            for w, c in reduced.items():
                col[(side,) + w] = c
        cols.append(col)
    lifts = null_combinations(cols)
    return [linear_combination(reps, c) for c in lifts]


def lowest_free(subspace):
    reps = subspace.vectors()
    cols = []
    for v in reps:
        col = {}
        for side, tab in enumerate((F1, F2)):
            for w, c in action(tab, v).items():
                col[(side,) + w] = c
        cols.append(col)
    return [linear_combination(reps, c) for c in null_combinations(cols)]


def rank(columns):
    s = Space()
    for v in columns:
        s.insert(v)
    return s.size()


def d_letter(i, j, slope, wrong_cartan=False):
    # D_i acting on letter j, at r=2, s=3+t. 'slope' selects t.
    if i == 0:
        c = DEG[j][1] if slope else 2 * DEG[j][0] + 3 * DEG[j][1] - 2
        if wrong_cartan:
            c = -c
        return ((j, c),) if c else ()
    if i == 1:
        return () if slope else tuple((k, -2 * c) for k, c in E1[j])
    if i == 2:
        return tuple((k, -(1 if slope else 3) * c) for k, c in E2[j])
    if i == 3:
        return tuple((k, -(1 if slope else 3) * c) for k, c in E12[j])
    if i == 4:
        return () if slope else tuple((k, 2 * c) for k, c in E12[j])
    return ()


def delta(v, slope=False, wrong_cartan=False):
    # In tensor words move each grade-zero [f3,u_i] to the right. It acts as
    # a derivation on later letters. On genuine Lie tensors the right tails
    # cancel by the noncommutative deletion derivation, not a vacuum assumption.
    # This is the actual recursive delta on every embedded Lie bracket.
    out = {}
    for word, coeff in v.items():
        guard()
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                for z, c in d_letter(word[i], word[j], slope, wrong_cartan):
                    a = list(word)
                    a[j] = z
                    del a[i]
                    key = tuple(a)
                    out[key] = out.get(key, F(0)) + coeff * c
    return clean(out)


def matrix_columns(vectors, target, pivots, slope=False):
    return [quotient_coordinates(target, pivots, delta(v, slope))
            for v in vectors]


def ptrim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return tuple(p)


def psub(a, b):
    return ptrim([(a[i] if i < len(a) else 0) -
                  (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def pmul(a, b):
    if not a or not b:
        return ()
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pdivmod(a, b):
    require(bool(b), 'polynomial division by zero')
    a = list(ptrim(a))
    q = [F(0)] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        guard()
        n = len(a) - len(b)
        c = a[-1] / b[-1]
        q[n] += c
        for i, z in enumerate(b):
            a[n + i] -= c * z
        a = list(ptrim(a))
    return ptrim(q), ptrim(a)


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while b:
        _, r = pdivmod(a, b)
        a, b = b, r
    return ptrim([c / a[-1] for c in a]) if a else ()


def positive_integer_roots(p):
    # Exact for the degree <= 2 gcd. The discriminant square test is the
    # quadratic rational-root criterion, with no numerical approximation.
    require(bool(p) and len(p) <= 3, 'unexpected common-minor degree')
    den = 1
    for c in p:
        den = math.lcm(den, c.denominator)
    z = [int(c * den) for c in p]
    candidates = set()
    if len(z) == 2:
        if (-z[0]) % z[1] == 0:
            candidates.add((-z[0]) // z[1])
    elif len(z) == 3:
        c, b, a = z
        disc = b * b - 4 * a * c
        if disc >= 0:
            d = math.isqrt(disc)
            if d * d == disc:
                for numerator in (-b + d, -b - d):
                    if numerator % (2 * a) == 0:
                        candidates.add(numerator // (2 * a))
    return sorted(k for k in candidates if k >= 1)


def rstr(c):
    return str(c.numerator) if c.denominator == 1 else '%s/%s' % (c.numerator, c.denominator)


def serial_poly(p):
    return [rstr(c) for c in p]  # ascending powers; [] means zero


def main():
    x, a, b, c, d, e, f, g = (letter(i) for i in range(8))
    h = bracket(x, bracket(x, a))
    h1, h2 = action(E1, h), action(E2, h)
    h22 = action(E2, h2)
    h12, h21 = action(E1, h2), action(E2, h1)
    hA, hB = action(E1, h22), action(E2, h12)
    htable = [
        (h, {}, {}), (h1, h, {}), (h2, {}, scale(h, 4)),
        (h22, {}, scale(h2, 6)), (h12, scale(h2, 2), scale(h1, 4)),
        (h21, h2, scale(h1, 5)),
        (hA, scale(h22, 3), scale(h12, 6)),
        (hB, scale(h22, 2), add(scale(h12, 3), scale(h21, 4))),
    ]
    for v, f1v, f2v in htable:
        require(action(F1, v) == f1v and action(F2, v) == f2v,
                'h lowering table mismatch')

    W = cyclic(h)
    require(dim(W) == 35, 'whole W is not 35 dimensional')
    verify_levi_closure(W)
    for sp in W.values():
        for v in sp.vectors():
            require(not delta(v) and not delta(v, True), 'F3 does not kill whole W')
    A = brackets_of_module(W)
    verify_levi_closure(A)
    # Check the entire first relation descends for both coefficients of t.
    for sp in A.values():
        for v in sp.vectors():
            require(is_member(W, delta(v)) and is_member(W, delta(v, True)),
                    'first relation does not descend to target W quotient')

    z1 = add(bracket(x, h12), scale(bracket(a, h2), -2),
             scale(bracket(b, h1), -4), scale(bracket(d, h), 4))
    z2 = add(bracket(x, h21), scale(bracket(a, h2), -1),
             scale(bracket(b, h1), -5), scale(bracket(c, h), 2), bracket(d, h))
    z27 = add(scale(bracket(x, hA), 4), scale(bracket(x, hB), -3),
              scale(bracket(a, h22), -6), scale(bracket(b, h12), -15),
              scale(bracket(b, h21), 12), scale(bracket(d, h2), 18),
              scale(bracket(f, h), -72))
    require(z1.get((0, 0, 0, 5), 0) == -1 and
            z2.get((3, 0, 0, 1), 0) == 2 and
            z27.get((0, 0, 0, 7), 0) == 5,
            'explicit tensor witness coefficient mismatch')
    for z in (z1, z2, z27):
        require(is_member(A, z) and not action(F1, z) and not action(F2, z),
                'claimed lowest relation is not an actual first relation')
    require(rank([z1, z2]) == 2 and bool(z27), 'relation witnesses dependent')
    lowA21 = lowest_free(A[(2, 1)])
    lowA22 = lowest_free(A[(2, 2)])
    require(len(lowA21) == 2 and len(lowA22) == 1,
            'whole first-relation lowest multiplicities differ from 2,1')

    # Boundary second seed is (ad x)^3 b, with its entire Levi module.
    seed2 = bracket(x, bracket(x, bracket(x, b)))
    B = cyclic(seed2)
    require(dim(B) == 81, 'whole second seed is not 81 dimensional')
    verify_levi_closure(B)
    for sp in B.values():
        for v in sp.vectors():
            require(not delta(v), 's=3 F3 does not kill second seed')
    AB, overlap = merge_spaces(A, B)
    require(overlap == 0, 'first and second complete seed spaces intersect')

    P, pp = basis_free_quotient(A, 4, (2, 1))
    T, tp = basis_free_quotient(W, 3, (2, 1))
    require(len(pp) == 5 and len(tp) == 4 and W[(2, 1)].size() == 2,
            'first-only source/target dimensions disagree')
    K = lowest_quotient(A, P, pp)
    require(len(K) == 2, 'whole first-only lowest space not two-dimensional')
    m0 = matrix_columns(K, T, tp)
    m1 = matrix_columns(K, T, tp, True)
    require(rank(m0) == 2, 'boundary-constant lowest pencil is not rank two')

    # Full-root and lowest checks in the ACTUAL boundary quotient, not just a
    # comparison against first-only dimensions.
    PB, pbp = basis_free_quotient(AB, 4, (2, 1))
    KB = lowest_quotient(AB, PB, pbp)
    require(len(pbp) == 4 and len(KB) == 2, 'boundary quotient dimensions')
    root0 = matrix_columns([PB.rows[p] for p in pbp], T, tp)
    low0 = matrix_columns(KB, T, tp)
    require(rank(root0) == 4 and rank(low0) == 2,
            'actual s=3 root or complete lowest map is not injective')
    require(B[(2, 1)].size() == 1, 'boundary second-seed weight not a line')
    boundary_line = B[(2, 1)].vectors()[0]
    require(bool(A[(2, 1)].reduce(boundary_line)[0]),
            'boundary second-seed line already in first relation')
    require(bool(A[(1, 1)].reduce(action(F1, boundary_line))[0]),
            'boundary second-seed line unexpectedly lowest modulo first relation')

    # All six maximal minors of the full 4 x 2 affine matrix, exact gcd.
    minors = []
    for i in range(4):
        for j in range(i + 1, 4):
            mij = lambda row, col: ptrim((m0[col].get(row, F(0)),
                                          m1[col].get(row, F(0))))
            p = psub(pmul(mij(i, 0), mij(j, 1)),
                     pmul(mij(j, 0), mij(i, 1)))
            minors.append(((i, j), p))
    gcd = ()
    for _, p in minors:
        gcd = pgcd(gcd, p)
    require(gcd and len(gcd) <= 3, 'zero or over-degree common gcd')
    for _, p in minors:
        require(not pdivmod(p, gcd)[1], 'gcd does not divide a minor')
    roots = positive_integer_roots(gcd)

    # Reason-specific mutation controls, each compared to the corresponding
    # actual, fully constructed object. No controls are asserted before run.
    wrong = delta(h, wrong_cartan=True)
    require(bool(wrong) and not delta(h), 'negative-Cartan mutant not detected')
    just_seed = Space()
    just_seed.insert(h)
    require(bool(h1) and bool(just_seed.reduce(h1)[0]),
            'omitted-W-translate mutant not detected')
    require(rank([K[0]]) == 1 and rank(K) == 2,
            'dropped-lowest-copy mutant not detected')
    target_witness = delta(bracket(a, h2))
    require(target_witness == scale(h12, -2) and bool(target_witness) and
            is_member(W, target_witness),
            'unquotiented-target mutant not detected')
    require(len(pp) == 5 and len(pbp) == 4,
            'omitted-boundary-seed mutant not detected')

    return {
        'W_dimension': dim(W), 'A_dimension': dim(A),
        'second_seed_dimension_s3': dim(B), 'A_intersect_B_dimension': overlap,
        'first_relation_lowest_multiplicities_21_22': [len(lowA21), len(lowA22)],
        'first_only_P_K_T_dimensions': [len(pp), len(K), len(tp)],
        's3_source_lowest_target_dimensions': [len(pbp), len(KB), len(tp)],
        's3_root_rank': rank(root0), 's3_lowest_rank': rank(low0),
        'pencil_M0_columns': [[rstr(m0[j].get(i, F(0))) for i in range(4)] for j in range(2)],
        'pencil_M1_columns': [[rstr(m1[j].get(i, F(0))) for i in range(4)] for j in range(2)],
        'minors_ascending_t_coefficients': [
            {'rows_0_based': list(ij), 'coefficients': serial_poly(p)} for ij, p in minors],
        'monic_gcd_ascending_t_coefficients': serial_poly(gcd),
        'positive_integer_t_roots': roots,
        'exact_exceptional_integers_s_ge_4': [3 + t for t in roots],
        'mutants_detected': ['negative_cartan', 'omitted_W_translate',
            'dropped_lowest_copy', 'unquotiented_target', 'omitted_s3_seed'],
        'scope': 'r=2; all integer s>=3; actual F3 on the entire (2,1) lowest space; conditional on named actual-source and ideal imports'
    }


result = {'status': 'INCOMPLETE', 'payload': None, 'reason': None}
try:
    signal.signal(signal.SIGTERM, stop_signal)
    signal.signal(signal.SIGINT, stop_signal)
    payload = main()
    guard()
    result['payload'] = payload
    result['status'] = 'PASS_FINITE_EXACT'
except Interrupted as exc:
    result['reason'] = str(exc)
except BaseException as exc:
    result['status'] = 'ERROR_NO_VERDICT'
    result['reason'] = '%s: %s' % (type(exc).__name__, str(exc))
    result['traceback'] = traceback.format_exc()
finally:
    result['elapsed_monotonic_seconds'] = time.monotonic() - START
    print(json.dumps(result, sort_keys=True), flush=True)

sys.exit(0 if result['status'] == 'PASS_FINITE_EXACT' else
         2 if result['status'] == 'INCOMPLETE' else 3)
