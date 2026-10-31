#!/usr/bin/env python3
"""UNRUN author candidate: finite exact mixed-filter calculations only.

No data files, writes, network, child processes, third-party imports, floats,
randomness or tolerances.  A parent must read this complete source and issue
an independent one-shot GO before execution.  The internal cooperative guard
is 40 seconds; the parent external limit is at most 55 seconds.  Failure,
including timeout or an accepted intended-reason mutant, is a nonzero exit.
The finite fixtures do not classify any infinite family or prove SN3.
"""
from fractions import Fraction as F
from itertools import combinations
from time import monotonic_ns
import signal
import sys

START = monotonic_ns()
LIMIT_NS = 40_000_000_000
STOP_SIGNAL = None


class Failure(Exception):
    pass


def request_stop(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def guard():
    if STOP_SIGNAL is not None:
        raise Failure('signal-' + str(STOP_SIGNAL))
    if monotonic_ns() - START >= LIMIT_NS:
        raise Failure('internal-deadline')


def need(condition, reason):
    if not condition:
        raise Failure(reason)


def reject_for(reason, operation):
    try:
        operation()
    except Failure as exc:
        need(str(exc) == reason, 'mutant-wrong-reason:' + reason + ':' + str(exc))
        return
    raise Failure('mutant-accepted:' + reason)


class G:
    """Exact Gaussian rational, with no conversion through complex floats."""
    __slots__ = ('a', 'b')

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __bool__(self):
        return bool(self.a or self.b)

    def __eq__(self, other):
        other = gg(other)
        return self.a == other.a and self.b == other.b

    def __add__(self, other):
        other = gg(other)
        return G(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a, -self.b)

    def __sub__(self, other):
        return self + -gg(other)

    def __rsub__(self, other):
        return gg(other) - self

    def __mul__(self, other):
        other = gg(other)
        return G(self.a * other.a - self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = gg(other)
        d = other.a * other.a + other.b * other.b
        need(d != 0, 'gaussian-division-by-zero')
        return G((self.a * other.a + self.b * other.b) / d,
                 (self.b * other.a - self.a * other.b) / d)

    def conj(self):
        return G(self.a, -self.b)

    def norm2(self):
        return self.a * self.a + self.b * self.b

    def __repr__(self):
        return '(' + str(self.a) + ',' + str(self.b) + ')'


def gg(x):
    return x if isinstance(x, G) else G(x)


ZERO, ONE, I = G(), G(1), G(0, 1)


class E:
    """Q(i)[z]/(z^2-z+1); conjugation sends i to -i and z to 1-z."""
    __slots__ = ('a', 'b')

    def __init__(self, a=ZERO, b=ZERO):
        self.a, self.b = gg(a), gg(b)

    def __bool__(self):
        return bool(self.a or self.b)

    def __eq__(self, other):
        other = ee(other)
        return self.a == other.a and self.b == other.b

    def __add__(self, other):
        other = ee(other)
        return E(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return E(-self.a, -self.b)

    def __sub__(self, other):
        return self + -ee(other)

    def __mul__(self, other):
        other = ee(other)
        ac, bd = self.a * other.a, self.b * other.b
        return E(ac - bd, self.a * other.b + self.b * other.a + bd)

    __rmul__ = __mul__

    def div_g(self, scalar):
        return E(self.a / scalar, self.b / scalar)

    def conj(self):
        return E(self.a.conj() + self.b.conj(), -self.b.conj())


def ee(x):
    return x if isinstance(x, E) else E(x)


EZERO, EONE, ZETA = E(), E(ONE), E(ZERO, ONE)


def zero_matrix(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def vector(dim_a, dim_b, terms):
    out = [ZERO for _ in range(dim_a * dim_b)]
    for a, b, coefficient in terms:
        out[a * dim_b + b] = out[a * dim_b + b] + gg(coefficient)
    return out


def vector_sum(vectors, scalars):
    return [sum((gg(c) * v[j] for v, c in zip(vectors, scalars)), ZERO)
            for j in range(len(vectors[0]))]


def outer_add(matrix, v, weight=ONE):
    weight = gg(weight)
    nz = [(i, x) for i, x in enumerate(v) if x]
    for i, x in nz:
        for j, y in nz:
            matrix[i][j] = matrix[i][j] + weight * x * y.conj()


def sum_outers(vectors, weights):
    out = zero_matrix(len(vectors[0]), len(vectors[0]))
    for v, weight in zip(vectors, weights):
        outer_add(out, v, weight)
    return out


def equal_matrix(a, b, reason):
    need(len(a) == len(b) and all(len(x) == len(y) for x, y in zip(a, b)), reason)
    need(all(x == y for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b)), reason)


def transpose_b(matrix, dim_a, dim_b):
    return [[matrix[a * dim_b + d][c * dim_b + b]
             for c in range(dim_a) for d in range(dim_b)]
            for a in range(dim_a) for b in range(dim_b)]


def apply_filter(matrix, k):
    """(I4 tensor k) matrix (I4 tensor k)^dagger; k is 4 by 5."""
    maps = [[(4 * a + b, k[b][j]) for b in range(4) if k[b][j]]
            for a in range(4) for j in range(5)]
    out = zero_matrix(16, 16)
    for u in range(20):
        guard()
        for v in range(20):
            q = matrix[u][v]
            if q:
                for i, ki in maps[u]:
                    for j, kj in maps[v]:
                        out[i][j] = out[i][j] + ki * q * kj.conj()
    return out


def apply_filter_vector(v, k):
    out = [ZERO for _ in range(16)]
    for a in range(4):
        for j in range(5):
            if v[5 * a + j]:
                for b in range(4):
                    out[4 * a + b] = out[4 * a + b] + k[b][j] * v[5 * a + j]
    return out


def hermitian(matrix, reason):
    n = len(matrix)
    need(all(matrix[i][j] == matrix[j][i].conj()
             for i in range(n) for j in range(n)), reason)


def determinant(matrix):
    n = len(matrix)
    work = [row[:] for row in matrix]
    product = ONE
    for j in range(n):
        guard()
        pivot = next((i for i in range(j, n) if work[i][j]), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            work[j], work[pivot] = work[pivot], work[j]
            product = -product
        p = work[j][j]
        product = product * p
        for i in range(j + 1, n):
            if work[i][j]:
                q = work[i][j] / p
                for k in range(j + 1, n):
                    work[i][k] = work[i][k] - q * work[j][k]
                work[i][j] = ZERO
    return product


def principal_minors(matrix):
    hermitian(matrix, 'M-not-hermitian')
    values = []
    for size in range(1, len(matrix) + 1):
        for ids in combinations(range(len(matrix)), size):
            d = determinant([[matrix[i][j] for j in ids] for i in ids])
            need(d.b == 0, 'principal-minor-not-real')
            values.append((ids, d.a))
    return values


def psd_factors(matrix, reason):
    """Exact positive rank-one elimination, including zero-pivot boundaries."""
    hermitian(matrix, reason)
    n = len(matrix)
    work = [row[:] for row in matrix]
    factors = []
    for k in range(n):
        guard()
        d = work[k][k]
        need(d.b == 0 and d.a >= 0, reason)
        if d.a == 0:
            need(all(not work[i][k] for i in range(n)), reason)
            continue
        col = [work[i][k] for i in range(n)]
        weight = F(1, 1) / d.a
        factors.append((weight, col))
        for i in range(n):
            for j in range(n):
                work[i][j] = work[i][j] - gg(weight) * col[i] * col[j].conj()
    need(all(not x for row in work for x in row), reason)
    rebuilt = zero_matrix(n, n)
    for weight, col in factors:
        outer_add(rebuilt, col, weight)
    equal_matrix(rebuilt, matrix, reason)
    return factors


def rank(matrix):
    work = [row[:] for row in matrix]
    rows, cols, pivot_row = len(work), len(work[0]), 0
    for j in range(cols):
        guard()
        p = next((i for i in range(pivot_row, rows) if work[i][j]), None)
        if p is None:
            continue
        work[pivot_row], work[p] = work[p], work[pivot_row]
        for i in range(pivot_row + 1, rows):
            if work[i][j]:
                q = work[i][j] / work[pivot_row][j]
                for k in range(j, cols):
                    work[i][k] = work[i][k] - q * work[pivot_row][k]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def matmul(a, b):
    out = zero_matrix(len(a), len(b[0]))
    for i in range(len(a)):
        guard()
        for k in range(len(b)):
            if a[i][k]:
                for j in range(len(b[0])):
                    if b[k][j]:
                        out[i][j] = out[i][j] + a[i][k] * b[k][j]
    return out


def adjoint(a):
    return [[a[i][j].conj() for i in range(len(a))] for j in range(len(a[0]))]


def marginals(matrix):
    left = [[sum((matrix[4 * a + b][4 * c + b] for b in range(4)), ZERO)
             for c in range(4)] for a in range(4)]
    right = [[sum((matrix[4 * a + b][4 * a + d] for a in range(4)), ZERO)
              for d in range(4)] for b in range(4)]
    return left, right


# Sparse polynomials in formal z modulo z^6-1, with Gaussian coefficients.
def padd(a, b):
    out = dict(a)
    for exponent, value in b.items():
        out[exponent] = out.get(exponent, ZERO) + value
        if not out[exponent]:
            del out[exponent]
    return out


def pmul(a, b):
    out = {}
    for e, x in a.items():
        for f, y in b.items():
            k = (e + f) % 6
            out[k] = out.get(k, ZERO) + x * y
    return {k: v for k, v in out.items() if v}


def pneg(a):
    return {k: -v for k, v in a.items()}


def det3_ops(m, add, mul, neg, zero):
    result = zero
    for permutation, sign in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                              ((2, 1, 0), -1), ((1, 0, 2), -1), ((0, 2, 1), -1)):
        term = mul(mul(m[0][permutation[0]], m[1][permutation[1]]),
                   m[2][permutation[2]])
        result = add(result, term if sign == 1 else neg(term))
    return result


def polynomial_vectors(components, exponents):
    result = [{} for _ in range(16)]
    for v, e in zip(components, exponents):
        for j, value in enumerate(v):
            if value:
                result[j] = padd(result[j], {e % 6: value})
    return result


def check_poly_minors(v, reason):
    count = 0
    for rows in combinations(range(4), 3):
        for cols in combinations(range(4), 3):
            guard()
            m = [[v[4 * i + j] for j in cols] for i in rows]
            need(not det3_ops(m, padd, pmul, pneg, {}), reason)
            count += 1
    need(count == 16, 'poly-minor-count')


def check_field_minors(v):
    count = 0
    for rows in combinations(range(4), 3):
        for cols in combinations(range(4), 3):
            guard()
            m = [[v[4 * i + j] for j in cols] for i in rows]
            need(not det3_ops(m, lambda a, b: a + b, lambda a, b: a * b,
                              lambda a: -a, EZERO), 'root-rank3-minor')
            count += 1
    need(count == 16, 'field-minor-count')


def roots_and_powers():
    roots = [EONE]
    for _ in range(5):
        roots.append(roots[-1] * ZETA)
    need(roots[-1] * ZETA == EONE, 'zeta-order-divides-six')
    need(all(roots[i] != roots[j] for i in range(6) for j in range(i)), 'zeta-distinct')
    for exponent in range(1, 6):
        need(sum((roots[(k * exponent) % 6] for k in range(6)), EZERO) == EZERO,
             'character-orthogonality')
    return roots


def character_average(components, roots):
    exponents = (0, 1, -1, -2, -3, -4)
    symbolic = polynomial_vectors(components, exponents)
    check_poly_minors(symbolic, 'symbolic-rank3-minor')
    total = [[EZERO for _ in range(16)] for _ in range(16)]
    for k in range(6):
        guard()
        v = [sum((ee(comp[j]) * roots[(k * e) % 6]
                  for comp, e in zip(components, exponents)), EZERO)
             for j in range(16)]
        check_field_minors(v)
        nz = [(j, x) for j, x in enumerate(v) if x]
        for i, x in nz:
            for j, y in nz:
                total[i][j] = total[i][j] + x * y.conj()
    expected = sum_outers(components, [ONE] * 6)
    need(all(total[i][j].div_g(6) == ee(expected[i][j])
             for i in range(16) for j in range(16)), 'six-character-identity')
    return expected, symbolic


# Formal polynomials in commuting range parameters, over the integers.
def fadd(a, b):
    out = dict(a)
    for monomial, value in b.items():
        out[monomial] = out.get(monomial, 0) + value
        if not out[monomial]:
            del out[monomial]
    return out


def fneg(a):
    return {m: -c for m, c in a.items()}


def fmul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            key = tuple(sorted(m + n))
            out[key] = out.get(key, 0) + x * y
    return {m: c for m, c in out.items() if c}


def formal_range_identity():
    names = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'alpha', 'beta', 'gamma')
    p = {name: {(name,): 1} for name in names}
    a, b, c, d, e, f, g, h, k, al, be, ga = (p[name] for name in names)
    rows = [[fadd(a, fmul(al, h)), fadd(b, fmul(be, h)), fadd(c, fmul(ga, h)), {}],
            [d, a, b, {}], [e, fneg(d), a, k],
            [fadd(f, fmul(al, c)), fmul(be, c), fadd(g, fmul(ga, c)), e]]

    def minor(i, j, x, y):
        return fadd(fmul(rows[i][x], rows[j][y]),
                    fneg(fmul(rows[i][y], rows[j][x])))

    m1, m2, m3 = minor(1, 2, 1, 2), minor(1, 2, 0, 2), minor(1, 3, 1, 3)
    need(m1 == fadd(fmul(a, a), fmul(b, d)), 'range-m1')
    need(m2 == fadd(fmul(a, d), fneg(fmul(b, e))), 'range-m2')
    need(m3 == fmul(a, e), 'range-m3')

    def identity(first, reason):
        lhs = fadd(fadd(fmul(fmul(a, a), first),
                        fneg(fmul(fmul(a, b), m2))),
                   fneg(fmul(fmul(b, b), m3)))
        need(lhs == fmul(fmul(a, a), fmul(a, a)), reason)

    identity(m1, 'range-polynomial-identity')
    bad_m1 = fadd(fmul(a, a), fneg(fmul(b, d)))
    reject_for('range-identity-mutant', lambda: identity(bad_m1, 'range-identity-mutant'))


def case(label, s, r, alpha, beta, gamma, expected_q, expected_psd, singular, roots):
    guard()
    s, r = F(s), F(r)
    alpha, beta, gamma = gg(alpha), gg(beta), gg(gamma)
    need(s > 1 and r > 1 and (s - 1) * (r - 1) >= 4, 'source-admission')
    need(beta and gamma, 'mixed-filter-required')
    a, x, y = alpha.norm2(), gamma.norm2(), beta.norm2()
    need(y / s + x / (s - 1) > 1, 'exterior-required')

    q = x / s + a / (r + s) + ((1 + x + x * x + a * (1 + x)) / s
                                  + a * (x + a) / r) / y
    need(q == expected_q, 'fixture-q')
    kappa, eta = r / (r + s), s / (r + s)
    need(kappa + eta == 1 and kappa * kappa / r + eta * eta / s == 1 / (r + s),
         'weights')

    raw = [vector(4, 5, terms) for terms in (
        [(0, 0, 1), (1, 1, 1), (2, 2, 1)],
        [(0, 1, 1), (1, 2, 1)], [(1, 0, 1), (2, 1, -1)],
        [(0, 2, 1), (3, 4, 1)], [(0, 4, 1)], [(3, 2, 1)],
        [(3, 0, 1)], [(2, 0, 1), (3, 3, 1)], [(2, 3, 1)])]
    weights = [1, 1, 1, s, s, s, r, r, r]
    q20 = sum_outers(raw, weights)
    need(sum((q20[j][j] for j in range(20)), ZERO) == gg(7 + 4 * (s + r)), 'Q-trace')
    qpt = transpose_b(q20, 4, 5)
    psd_factors(qpt, 'Q-partial-transpose-PSD')

    w = [alpha, beta, gamma, ZERO]
    k = [[ONE if i == j else (w[i] if j == 4 else ZERO)
          for j in range(5)] for i in range(4)]
    kk = matmul(k, adjoint(k))
    expected_kk = [[(ONE if i == j else ZERO) + w[i] * w[j].conj()
                    for j in range(4)] for i in range(4)]
    equal_matrix(kk, expected_kk, 'physical-contraction')

    actual = apply_filter(q20, k)
    filtered = [apply_filter_vector(v, k) for v in raw]
    equal_matrix(actual, sum_outers(filtered, weights), 'actual-filtered-Q')
    A, B, D, fv, hv, gv, pv, jv, e23 = filtered
    expected_f = vector(4, 4, [(0, 2, 1), (3, 0, alpha), (3, 1, beta), (3, 2, gamma)])
    expected_h = vector(4, 4, [(0, 0, alpha), (0, 1, beta), (0, 2, gamma)])
    need(fv == expected_f and hv == expected_h, 'filter-ket-conjugation')

    actual_pt = transpose_b(actual, 4, 4)
    kbar = [[x.conj() for x in row] for row in k]
    expected_pt = apply_filter(qpt, kbar)
    equal_matrix(actual_pt, expected_pt, 'conjugated-filter-PT')
    psd_factors(actual_pt, 'R-partial-transpose-PSD')
    n = a + x + y
    trace = 7 + 2 * s * (1 + n) + 4 * r
    need(sum((actual[j][j] for j in range(16)), ZERO) == gg(trace), 'R-trace')
    probability = trace / ((1 + n) * (7 + 4 * (s + r)))
    need(0 < probability < 1, 'physical-success-probability')
    ma, mb = marginals(actual)
    need(rank(ma) == rank(mb) == 4, 'local-support-rank')

    # Actual output range equals the span of the nine filtered positive summands.
    columns = [[filtered[j][i] for j in range(9)] for i in range(16)]
    need(rank(actual) == rank(columns), 'actual-range-rank')
    need(actual[5][5] == ONE, 'physical-11-entry')
    need(rank([hv[i * 4:(i + 1) * 4] for i in range(4)]) == 1, 'H-is-product')
    if alpha:
        need(hv[0] != ZERO and hv[5] == ZERO, 'product-range-coordinate')
        reject_for('wrong-range-coordinate', lambda: need(hv[0] == ZERO, 'wrong-range-coordinate'))

    C = [[fv[i], hv[i], gv[i], pv[i]] for i in range(16)]
    ts = [[-gamma / beta, ONE / beta, gamma * gamma / beta, alpha * gamma / beta],
          [ZERO, ZERO, gamma, gg(kappa) * alpha],
          [alpha / beta, ZERO, -alpha * gamma / beta, -alpha * alpha / beta],
          [ZERO, ZERO, -gg(eta) * alpha, ZERO]]
    xs = [[sum((C[i][j] * t[j] for j in range(4)), ZERO) for i in range(16)] for t in ts]
    need(xs[0] == vector(4, 4, [(0, 0, alpha / beta), (0, 1, 1), (3, 1, -gamma)]),
         'X1-cancellation')
    need(xs[2] == vector(4, 4, [(0, 2, alpha / beta), (3, 1, alpha)]), 'X3-cancellation')
    components = [A, D] + xs
    char_sum, symbolic = character_average(components, roots)
    diagonal = [s, s, s, r]
    M = [[gg(diagonal[i] if i == j else 0)
          - sum((t[i] * t[j].conj() for t in ts), ZERO)
          for j in range(4)] for i in range(4)]
    norm_trace = sum((t[j].norm2() / diagonal[j] for t in ts for j in range(4)), F(0))
    need(norm_trace == q, 'q-is-weighted-column-trace')
    minors = principal_minors(M)
    need(len(minors) == 15, 'all-principal-minors-count')
    psd = all(value >= 0 for _, value in minors)
    need(psd == expected_psd, 'fixture-M-PSD-classification')
    need((minors[-1][1] == 0) == singular, 'fixture-M-singularity')
    if q <= 1:
        need(psd, 'q-sufficient-PSD')

    cmc = matmul(matmul(C, M), adjoint(C))
    residual = [row[:] for row in actual]
    for v, weight in ((B, -1), (jv, -r), (e23, -r)):
        outer_add(residual, v, weight)
    residual = [[residual[i][j] - char_sum[i][j] for j in range(16)] for i in range(16)]
    equal_matrix(residual, cmc, 'actual-residual-identity')
    if psd:
        factors = psd_factors(M, 'M-PSD-factorization')
        positive = zero_matrix(16, 16)
        for weight, column in factors:
            psi = [sum((C[i][j] * column[j] for j in range(4)), ZERO) for i in range(16)]
            need(all(not psi[4 * row + b] for row in (1, 2) for b in range(4)),
                 'residual-rank-support')
            need(weight > 0, 'residual-positive-weight')
            outer_add(positive, psi, weight)
        equal_matrix(positive, cmc, 'actual-positive-residual-identity')
        need(rank([B[4 * i:4 * (i + 1)] for i in range(4)]) == 2, 'B-rank')
        need(rank([jv[4 * i:4 * (i + 1)] for i in range(4)]) == 2, 'J-rank')
        need(rank([e23[4 * i:4 * (i + 1)] for i in range(4)]) == 1, '23-rank')

    # Each mutant is required to fail for the stated invariant, not any exception.
    if label == 'unequal-complex':
        wrong_pt = apply_filter(qpt, k)
        reject_for('wrong-filter-conjugation',
                   lambda: equal_matrix(actual_pt, wrong_pt, 'wrong-filter-conjugation'))
        wrong_M = [[gg(diagonal[i] if i == j else 0)
                    - sum((t[i] * t[j] for t in ts), ZERO)
                    for j in range(4)] for i in range(4)]
        reject_for('wrong-outer-conjugation',
                   lambda: hermitian(wrong_M, 'wrong-outer-conjugation'))
        wrong_symbolic = [dict(entry) for entry in symbolic]
        wrong_symbolic[0] = padd(wrong_symbolic[0], {0: ONE})
        reject_for('wrong-rank3-minor',
                   lambda: check_poly_minors(wrong_symbolic, 'wrong-rank3-minor'))
        wrong_exponents = (0, 1, -1, -2, -3, -3)
        bad = [[EZERO for _ in range(16)] for _ in range(16)]
        for root_index in range(6):
            v = [sum((ee(comp[j]) * roots[(root_index * exp) % 6]
                      for comp, exp in zip(components, wrong_exponents)), EZERO)
                 for j in range(16)]
            nz = [(j, entry) for j, entry in enumerate(v) if entry]
            for i, vi in nz:
                for j, vj in nz:
                    bad[i][j] = bad[i][j] + vi * vj.conj()
        reject_for('repeated-character-cross-term',
                   lambda: need(all(bad[i][j].div_g(6) == ee(char_sum[i][j])
                                    for i in range(16) for j in range(16)),
                                'repeated-character-cross-term'))
        wrong_q = x / s + a / (r + s) + ((1 + x + x * x + a * (1 + x)) / s
                                           + a * (x + a) / s) / y
        reject_for('wrong-q-denominator', lambda: need(wrong_q == norm_trace, 'wrong-q-denominator'))

    print('CASE', label, 's=', s, 'r=', r, 'q=', q, 'M_PSD=', psd,
          'M_det=', minors[-1][1], 'P=', probability,
          'rankR=', rank(actual), 'all_M_principal_minors=', len(minors),
          'root_rank3_minors=', 6 * 16, 'symbolic_rank3_minors=', 16, flush=True)


def main():
    formal_range_identity()
    roots = roots_and_powers()
    case('equal-complex', 3, 3, I, 3, I, F(41, 54), True, False, roots)
    case('unequal-complex', 2, 5, I, G(4, 1), I, F(484, 595), True, False, roots)
    case('q-boundary', F(5, 2), 4, 0, G(1, 1), I, F(1), True, False, roots)
    case('M-boundary-q-outside', 2, 5, 0, G(1, 1), I, F(5, 4), True, True, roots)
    case('M-nonPSD-q-outside', 2, 5, 0, I, I, F(2), False, False, roots)
    guard()
    print('STATUS: PASS — exact finite checks only; no global or SN3 conclusion', flush=True)


if __name__ == '__main__':
    try:
        signal.signal(signal.SIGTERM, request_stop)
        signal.signal(signal.SIGINT, request_stop)
        main()
    except Exception as exc:
        print('STATUS: FAIL', type(exc).__name__, str(exc), flush=True)
        sys.exit(1)
