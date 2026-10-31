#!/usr/bin/env python3
"""Prospective f627 exact checker. STDOUT only; no file, network, or subprocess I/O.

NOT RUN by the author. All arithmetic is rational/Gaussian rational or exact
formal cyclic-character algebra. This program is finite corroboration only;
it does not establish a quantified theorem or an unrestricted PPT/SN3 result.
"""
from fractions import Fraction as F
from itertools import combinations


class CheckFailure(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def rejected(reason, operation):
    try:
        operation()
    except CheckFailure as exc:
        need(str(exc) == reason, "CONTROL_WRONG_REASON:" + reason + ":" + str(exc))
        print("CONTROL", reason, "REJECTED_AS_INTENDED")
        return
    raise CheckFailure("CONTROL_WAS_ACCEPTED:" + reason)


class G:
    """An exact Gaussian rational, including rational 0 and 1."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    @staticmethod
    def of(value):
        return value if isinstance(value, G) else G(value)

    def __add__(self, other):
        other = G.of(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G.of(other))

    def __rsub__(self, other):
        return G.of(other) - self

    def __mul__(self, other):
        other = G.of(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = G.of(other)
        den = other.re * other.re + other.im * other.im
        need(den != 0, "ZERO_GAUSSIAN_DIVISOR")
        return G((self.re * other.re + self.im * other.im) / den,
                 (self.im * other.re - self.re * other.im) / den)

    def __eq__(self, other):
        if not isinstance(other, (G, int, F)):
            return False
        other = G.of(other)
        return self.re == other.re and self.im == other.im

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def __str__(self):
        return "(" + str(self.re) + "," + str(self.im) + ")"


ZERO, ONE = G(0), G(1)


class Character:
    """Element of Q(i)[C_n], not a floating approximation to a root.

    Coefficient zero equals the average of evaluations over all n roots.
    Vanishing as a group-ring element implies vanishing at every root.
    """
    __slots__ = ("n", "terms")

    def __init__(self, n, terms=None):
        self.n = n
        out = {}
        for exponent, coefficient in (terms or {}).items():
            e = exponent % n
            out[e] = out.get(e, ZERO) + G.of(coefficient)
        self.terms = {e: c for e, c in out.items() if c != ZERO}

    @classmethod
    def constant(cls, n, value):
        return cls(n, {0: G.of(value)})

    @classmethod
    def monomial(cls, n, exponent):
        return cls(n, {exponent: ONE})

    def coerce(self, other):
        if isinstance(other, Character):
            need(other.n == self.n, "CHARACTER_MODULUS_MISMATCH")
            return other
        return Character.constant(self.n, other)

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for e, c in other.terms.items():
            out[e] = out.get(e, ZERO) + c
        return Character(self.n, out)

    __radd__ = __add__

    def __neg__(self):
        return Character(self.n, {e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for e, a in self.terms.items():
            for f, b in other.terms.items():
                k = (e + f) % self.n
                out[k] = out.get(k, ZERO) + a * b
        return Character(self.n, out)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def conj(self):
        return Character(self.n, {-e: c.conj() for e, c in self.terms.items()})

    def average(self):
        return self.terms.get(0, ZERO)


def zmat(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def ident(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def vzero(n):
    return [ZERO for _ in range(n)]


def vunit(n, index):
    out = vzero(n)
    out[index] = ONE
    return out


def vadd(*vectors):
    return [sum((v[i] for v in vectors), ZERO) for i in range(len(vectors[0]))]


def vscale(coefficient, vector):
    coefficient = G.of(coefficient)
    return [coefficient * x for x in vector]


def add_outer(matrix, coefficient, vector):
    coefficient = G.of(coefficient)
    for i, a in enumerate(vector):
        if a == ZERO:
            continue
        for j, b in enumerate(vector):
            if b != ZERO:
                matrix[i][j] = matrix[i][j] + coefficient * a * b.conj()


def add_matrix(left, right):
    return [[a + b for a, b in zip(row_l, row_r)]
            for row_l, row_r in zip(left, right)]


def subtract_matrix(left, right):
    return [[a - b for a, b in zip(row_l, row_r)]
            for row_l, row_r in zip(left, right)]


def need_matrix(left, right, reason):
    need(len(left) == len(right), reason)
    need(all(len(a) == len(b) and all(x == y for x, y in zip(a, b))
             for a, b in zip(left, right)), reason)


def mm(left, right):
    need(len(left[0]) == len(right), "MATRIX_DIMENSION")
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), ZERO)
             for j in range(len(right[0]))] for i in range(len(left))]


def dagger(matrix):
    return [[matrix[j][i].conj() for j in range(len(matrix))]
            for i in range(len(matrix[0]))]


def transpose_b(matrix, alice, bob):
    out = zmat(alice * bob, alice * bob)
    for a in range(alice):
        for b in range(bob):
            for c in range(alice):
                for d in range(bob):
                    out[a * bob + d][c * bob + b] = matrix[a * bob + b][c * bob + d]
    return out


def partials(matrix):
    a = [[sum((matrix[4*i+b][4*j+b] for b in range(4)), ZERO)
          for j in range(4)] for i in range(4)]
    b = [[sum((matrix[4*i+j][4*i+k] for i in range(4)), ZERO)
          for k in range(4)] for j in range(4)]
    return a, b


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), ZERO)


def ldl(matrix):
    """Exact no-pivot Hermitian LDL; zero PSD pivot requires a zero row.

    Returns (positive semidefinite, positive definite, reason).  No numerical
    tolerance, eigenvalue approximation, or floating-point operation occurs.
    """
    n = len(matrix)
    need_matrix(matrix, dagger(matrix), "LDL_NON_HERMITIAN")
    work = [row[:] for row in matrix]
    definite = True
    for k in range(n):
        d = work[k][k]
        need(d.im == 0, "LDL_NONREAL_PIVOT")
        if d.re < 0:
            return False, False, "NEGATIVE_PIVOT_" + str(k)
        if d.re == 0:
            definite = False
            if any(work[k][j] != ZERO for j in range(k + 1, n)):
                return False, False, "ZERO_PIVOT_NONZERO_ROW_" + str(k)
            continue
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                work[i][j] = work[i][j] - work[i][k] * work[k][j] / d
    return True, definite, "PSD"


def source(s, r):
    """The actual 20 by 20 Q, ordered Alice-major/Bob-minor."""
    q = zmat(20, 20)
    e = lambda a, b: vunit(20, 5*a+b)
    terms = [
        (1, vadd(e(0, 0), e(1, 1), e(2, 2))),
        (1, vadd(e(0, 1), e(1, 2))),
        (1, vadd(e(1, 0), vscale(-1, e(2, 1)))),
        (s, vadd(e(0, 2), e(3, 4))), (s, e(3, 2)), (s, e(0, 4)),
        (r, vadd(e(2, 0), e(3, 3))), (r, e(2, 3)), (r, e(3, 0)),
    ]
    for coefficient, vector in terms:
        add_outer(q, coefficient, vector)
    return q


def canonical_k(w):
    k = zmat(4, 5)
    for i in range(4):
        k[i][i] = ONE
    for i in range(3):
        k[i][4] = w[i]
    return k


def filtered(q, k):
    """Actual (I_4 tensor K) Q (I_4 tensor K)^dagger, all 256 entries."""
    out = zmat(16, 16)
    for a in range(4):
        for b in range(5):
            for c in range(4):
                for d in range(5):
                    value = q[5*a+b][5*c+d]
                    if value == ZERO:
                        continue
                    for x in range(4):
                        if k[x][b] == ZERO:
                            continue
                        for y in range(4):
                            if k[y][d] != ZERO:
                                out[4*a+x][4*c+y] = (out[4*a+x][4*c+y]
                                                          + k[x][b] * value * k[y][d].conj())
    return out


def physical_vectors(w):
    alpha, beta, gamma = w
    e = lambda a, b: vunit(16, 4*a+b)
    a = vadd(e(0, 0), e(1, 1), e(2, 2))
    b = vadd(e(0, 1), e(1, 2))
    d = vadd(e(1, 0), vscale(-1, e(2, 1)))
    u = vadd(e(0, 2), vscale(alpha, e(3, 0)), vscale(beta, e(3, 1)))
    fw = vadd(u, vscale(gamma, e(3, 2)))
    ev = vadd(e(2, 0), e(3, 3))
    zero_w = vadd(vscale(alpha, e(0, 0)), vscale(beta, e(0, 1)),
                  vscale(gamma, e(0, 2)))
    return a, b, d, u, fw, ev, zero_w


def direct_output(s, r, w):
    a, b, d, u, fw, ev, zero_w = physical_vectors(w)
    out = zmat(16, 16)
    for coefficient, vector in [(1, a), (1, b), (1, d), (s, fw), (r, ev),
                                (s, vunit(16, 14)), (s, zero_w),
                                (r, vunit(16, 11)), (r, vunit(16, 12))]:
        add_outer(out, coefficient, vector)
    return out


def central_ppt_certificate(s, r, w):
    """Independent physical 16 by 16 sum for the sufficient source region."""
    e = lambda a, b: vunit(16, 4*a+b)
    barw0 = vadd(*(vscale(w[j].conj(), e(0, j)) for j in range(3)))
    barw3 = vadd(*(vscale(w[j].conj(), e(3, j)) for j in range(3)))
    weights_and_vectors = [
        (F(1), vadd(e(0, 1), e(1, 0))),
        (F(1), vadd(e(1, 2), e(2, 1))), (F(1), e(0, 0)), (F(1), e(2, 2)),
        (F(1), vadd(e(0, 2), e(1, 1), vscale(-1, e(2, 0)))),
        (s-1, vadd(e(0, 2), vscale(F(2, 1)/(s-1), e(2, 0)))),
        (r-1-F(4, 1)/(s-1), e(2, 0)),
        (r, vadd(e(2, 3), e(3, 0))),
        (s, vadd(barw0, e(3, 2))), (r, e(3, 3)), (s, barw3),
    ]
    out = zmat(16, 16)
    for weight, vector in weights_and_vectors:
        need(weight >= 0, "PPT_CERTIFICATE_NEGATIVE_WEIGHT")
        add_outer(out, weight, vector)
    return out


def det3(m):
    return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
            - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
            + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))


def all_rank_two_minors(vector, zero, reason):
    for rows in combinations(range(4), 3):
        for cols in combinations(range(4), 3):
            matrix = [[vector[4*i+j] for j in cols] for i in rows]
            need(det3(matrix) == zero, reason + ":" + str(rows) + ":" + str(cols))


def character_five(w, modulus=5):
    """Actual coefficient matrix of V_z in Q(i)[C_modulus]."""
    a, b, d, u, _, _, _ = physical_vectors(w)
    z = Character.monomial(modulus, 1)
    z2 = Character.monomial(modulus, 2)
    zi = Character.monomial(modulus, -1)
    zi2 = Character.monomial(modulus, -2)
    p = lambda x: Character.constant(modulus, x)
    return [z*p(a[i]) + p(b[i]) - z2*p(d[i]) + zi*p(u[i])
            + zi2*p(w[1] if i == 14 else ZERO) for i in range(16)]


def character_three():
    w = (ZERO, ZERO, ZERO)
    a, _, d, _, _, _, _ = physical_vectors(w)
    n = 3
    z, zi = Character.monomial(n, 1), Character.monomial(n, -1)
    p = lambda x: Character.constant(n, x)
    return [p(a[i]) + z*p(d[i]) + zi*p(ONE if i == 1 else ZERO)
            for i in range(16)]


def mean_outer(vector):
    return [[(vector[i] * vector[j].conj()).average() for j in range(16)]
            for i in range(16)]


def check_five(w):
    v = character_five(w)
    zi = Character.monomial(5, -1)
    zero = Character.constant(5, ZERO)
    for row in range(4):
        need(v[4*row+2] == zi*v[4*row+1], "FIVE_DEPENDENT_COLUMNS")
        need(v[4*row+3] == zero, "FIVE_FOURTH_COLUMN")
    all_rank_two_minors(v, zero, "FIVE_3X3_MINOR")
    a, b, d, u, _, _, _ = physical_vectors(w)
    expected = zmat(16, 16)
    for weight, vector in [(1, a), (1, b), (1, d), (1, u),
                           (w[1].norm2(), vunit(16, 14))]:
        add_outer(expected, weight, vector)
    got = mean_outer(v)
    need_matrix(got, expected, "FIVE_CHARACTER_AVERAGE")
    return got


def check_three():
    v = character_three()
    z, zi = Character.monomial(3, 1), Character.monomial(3, -1)
    zero = Character.constant(3, ZERO)
    for row in range(4):
        need(v[4*row+1] == zi*v[4*row] - z*v[4*row+2],
             "THREE_DEPENDENT_COLUMNS")
        need(v[4*row+3] == zero, "THREE_FOURTH_COLUMN")
    all_rank_two_minors(v, zero, "THREE_3X3_MINOR")
    a, _, d, _, _, _, _ = physical_vectors((ZERO, ZERO, ZERO))
    expected = zmat(16, 16)
    for vector in (a, d, vunit(16, 1)):
        add_outer(expected, 1, vector)
    got = mean_outer(v)
    need_matrix(got, expected, "THREE_CHARACTER_AVERAGE")
    return got


def add_rank_two(matrix, weight, vector, reason):
    need(weight >= 0, reason + ":NEGATIVE_WEIGHT")
    all_rank_two_minors(vector, ZERO, reason + ":MINOR")
    add_outer(matrix, weight, vector)


def ellipsoid_rhs(s, r, w, mean5, delta_override=None, conjugate_gamma=False):
    _, _, _, u, _, ev, zero_w = physical_vectors(w)
    beta2, gamma2 = w[1].norm2(), w[2].norm2()
    delta = s-beta2-s*gamma2/(s-1)
    if delta_override is not None:
        delta = delta_override
    gamma = w[2].conj() if conjugate_gamma else w[2]
    out = [row[:] for row in mean5]
    for weight, vector in [
        (s-1, vadd(u, vscale(G(s/(s-1))*gamma, vunit(16, 14)))),
        (delta, vunit(16, 14)), (r, ev), (s, zero_w),
        (r, vunit(16, 11)), (r, vunit(16, 12)),
    ]:
        add_rank_two(out, weight, vector, "ELLIPSOID_TERM")
    return out


def beta_line_rhs(s, r, beta, mean3):
    w = (ZERO, beta, ZERO)
    _, b, _, _, fw, ev, _ = physical_vectors(w)
    out = [row[:] for row in mean3]
    for weight, vector in [(F(1), b), (s, fw), (r, ev),
                           (s*beta.norm2()-1, vunit(16, 1)),
                           (s, vunit(16, 14)), (r, vunit(16, 11)),
                           (r, vunit(16, 12))]:
        add_rank_two(out, weight, vector, "BETA_LINE_TERM")
    return out


def gamma_line_rhs(s, r, gamma, mean5zero, wrong_conjugate=False):
    x = gamma.norm2()
    _, _, _, _, _, ev, _ = physical_vectors((ZERO, ZERO, gamma))
    c = gamma if wrong_conjugate else gamma.conj()
    vector = vadd(vunit(16, 14), vscale(c / G(1+x), vunit(16, 2)))
    out = [row[:] for row in mean5zero]
    for weight, term in [(s*(1+x), vector),
                         (s-1+s*x*x/(1+x), vunit(16, 2)),
                         (r, ev), (r, vunit(16, 11)), (r, vunit(16, 12))]:
        add_rank_two(out, weight, term, "GAMMA_LINE_TERM")
    return out


class Poly:
    """Sparse integer polynomial in all formal range/filter variables."""
    size = 12

    def __init__(self, terms=None):
        self.terms = {m: int(c) for m, c in (terms or {}).items() if c != 0}

    @classmethod
    def constant(cls, value):
        return cls({(0,)*cls.size: int(value)})

    @classmethod
    def var(cls, index):
        monomial = [0]*cls.size
        monomial[index] = 1
        return cls({tuple(monomial): 1})

    @staticmethod
    def of(value):
        return value if isinstance(value, Poly) else Poly.constant(value)

    def __add__(self, other):
        out = dict(self.terms)
        for m, c in Poly.of(other).terms.items():
            out[m] = out.get(m, 0) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly.of(other))

    def __rsub__(self, other):
        return Poly.of(other) - self

    def __mul__(self, other):
        out = {}
        for m, a in self.terms.items():
            for n, b in Poly.of(other).terms.items():
                product = tuple(x+y for x, y in zip(m, n))
                out[product] = out.get(product, 0) + a*b
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        result = Poly.constant(1)
        for _ in range(power):
            result = result*self
        return result

    def __eq__(self, other):
        return self.terms == Poly.of(other).terms


def formal_range_identities():
    a, b, c, d, e, f, g, h, k, alpha, beta, gamma = [Poly.var(i) for i in range(12)]
    zero = Poly.constant(0)
    x = [[a+alpha*h, b+beta*h, c+gamma*h, zero],
         [d, a, b, zero], [e, -d, a, k],
         [f+alpha*c, beta*c, g+gamma*c, e]]
    minor2 = lambda i, j, p, q: x[i][p]*x[j][q]-x[i][q]*x[j][p]
    m1, m2, m3 = minor2(1, 2, 1, 2), minor2(1, 2, 0, 2), minor2(1, 3, 1, 3)
    need(m1 == a*a+b*d, "FORMAL_OUTPUT_MINOR_1")
    need(m2 == a*d-b*e, "FORMAL_OUTPUT_MINOR_2")
    need(m3 == a*e, "FORMAL_OUTPUT_MINOR_3")
    need(a*a*m1-a*b*m2-b*b*m3 == a**4, "FORMAL_OUTPUT_A4_IDENTITY")
    need(x[1][1] == a, "FORMAL_OUTPUT_11_INDEX")
    y = [[a, b, c, zero, h], [d, a, b, zero, zero],
         [e, -d, a, k, zero], [f, zero, g, e, c]]
    minor3 = lambda rows, cols: det3([[y[i][j] for j in cols] for i in rows])
    g1 = minor3((0, 1, 3), (0, 1, 3))
    g2 = minor3((1, 2, 3), (1, 2, 4))
    g3 = minor3((0, 1, 3), (1, 2, 3))
    g4 = minor3((1, 2, 3), (0, 1, 4))
    g5 = minor3((0, 1, 2), (0, 1, 2))
    for actual, expected, name in [
        (g1, e*(a*a-b*d), "FORMAL_SOURCE_G1"),
        (g2, c*(a*a+b*d), "FORMAL_SOURCE_G2"),
        (g3, e*(b*b-a*c), "FORMAL_SOURCE_G3"),
        (g4, -c*(d*d+a*e), "FORMAL_SOURCE_G4"),
        (g5, a**3+b*b*e-d*d*c-a*c*e, "FORMAL_SOURCE_G5"),
    ]:
        need(actual == expected, name)
    need(2*a*(g5-g3-g4)-(c*g1+e*g2) == 2*(a**4),
         "FORMAL_SOURCE_CORRECTED_A4_IDENTITY")
    print("FORMAL_RANGE", "3_OUTPUT_MINORS", "5_SOURCE_MINORS", "BOTH_A4_IDENTITIES")


def kernel_and_local_interface(q, k, output, w):
    kernel = [-w[0], -w[1], -w[2], ZERO, ONE]
    need(all(sum((k[i][j]*kernel[j] for j in range(5)), ZERO) == ZERO
             for i in range(4)), "KERNEL_VECTOR")
    need_matrix([row[:4] for row in k], ident(4), "K_RANK_FOUR_IDENTITY_MINOR")
    ii = G(0, 1)
    local = [[ONE, ii, ZERO, ZERO], [ZERO, ONE, ZERO, ZERO],
             [ZERO, ZERO, ONE, ZERO], [ZERO, ZERO, ZERO, G(2)]]
    inverse = [[ONE, -ii, ZERO, ZERO], [ZERO, ONE, ZERO, ZERO],
               [ZERO, ZERO, ONE, ZERO], [ZERO, ZERO, ZERO, G(F(1, 2))]]
    need_matrix(mm(local, inverse), ident(4), "L_RIGHT_INVERSE")
    need_matrix(mm(inverse, local), ident(4), "L_LEFT_INVERSE")
    kp = mm(local, k)
    need(all(sum((kp[i][j]*kernel[j] for j in range(5)), ZERO) == ZERO
             for i in range(4)), "LK_KERNEL_VECTOR")
    changed = filtered(q, kp)
    local16 = zmat(16, 16)
    for a in range(4):
        for i in range(4):
            for j in range(4):
                local16[4*a+i][4*a+j] = local[i][j]
    need_matrix(changed, mm(mm(local16, output), dagger(local16)), "LK_PHYSICAL_OUTPUT")


def region(s, r):
    return s > 1 and r > 1 and (s-1)*(r-1) >= 4


def check_scope(evidence, claim):
    if evidence == "PARENT_SUFFICIENT" and claim == "FILTERED_PPT_IFF_PARENT_REGION":
        raise CheckFailure("FILTERED_IFF_SCOPE_OVERCLAIM")
    if evidence == "FINITE_CASE" and claim == "UNIVERSAL_FILTERED_PPT_CLASSIFICATION":
        raise CheckFailure("FINITE_TO_UNIVERSAL_SCOPE_OVERCLAIM")


def print_matrix(label, matrix):
    print(label, str(len(matrix)) + "x" + str(len(matrix[0])))
    for row in matrix:
        print(" ".join(str(value) for value in row))


def test_case(name, s, r, w, mean3, mean5zero):
    s, r = F(s), F(r)
    need(s > 1 and r > 0, "CASE_DOMAIN")
    q, k = source(s, r), canonical_k(w)
    actual = filtered(q, k)
    need_matrix(actual, direct_output(s, r, w), "ACTUAL_20_TO_16_OUTPUT")
    qt = transpose_b(q, 4, 5)
    rt = transpose_b(actual, 4, 4)
    kbar = [[entry.conj() for entry in row] for row in k]
    need_matrix(rt, filtered(qt, kbar), "ACTUAL_COMPLEX_PARTIAL_TRANSPOSE")
    need(ldl(q)[0] and ldl(actual)[0], "SOURCE_OR_OUTPUT_NOT_PSD")
    norm = sum((x.norm2() for x in w), F(0))
    z, t = F(7)+2*s*(1+norm)+4*r, F(7)+4*(s+r)
    need(trace(q) == G(t) and trace(actual) == G(z), "TRACE")
    kk = mm(k, dagger(k))
    defect = [[G(1+norm if i == j else 0)-kk[i][j] for j in range(4)]
              for i in range(4)]
    need(ldl(defect)[0], "PHYSICAL_FILTER_CONTRACTION")
    prob = z/((1+norm)*t)
    need(F(0) < prob <= F(1), "PHYSICAL_SUCCESS_PROBABILITY")
    ma, mb = partials(actual)
    need(trace(ma) == G(z) and trace(mb) == G(z), "MARGINAL_TRACES")
    need(ldl(ma)[1] and ldl(mb)[1], "LOCAL_SUPPORT_NOT_FULL")
    kernel_and_local_interface(q, k, actual, w)
    ppt, _, why = ldl(rt)
    if region(s, r):
        need(ppt, "SOURCE_REGION_OUTPUT_NOT_PPT")
        need_matrix(rt, central_ppt_certificate(s, r, w), "PPT_POSITIVE_SUM")
    if name == "outside-source":
        need(not ppt, "OUTSIDE_CASE_EXPECTED_NPT")
    mean5 = check_five(w)
    delta = s-w[1].norm2()-s*w[2].norm2()/(s-1)
    certificates = []
    if delta >= 0:
        need_matrix(actual, ellipsoid_rhs(s, r, w, mean5), "ELLIPSOID_IDENTITY")
        certificates.append("ELLIPSOID")
    if w[0] == ZERO and w[2] == ZERO and s*w[1].norm2() >= 1:
        need_matrix(actual, beta_line_rhs(s, r, w[1], mean3), "BETA_LINE_IDENTITY")
        certificates.append("BETA_LINE")
    if w[0] == ZERO and w[1] == ZERO:
        need_matrix(actual, gamma_line_rhs(s, r, w[2], mean5zero), "GAMMA_LINE_IDENTITY")
        certificates.append("GAMMA_LINE")
    need(certificates, "NO_CERTIFICATE_FOR_SELECTED_CASE")
    if name == "assigned":
        expected_a = [[G(14), ZERO, ZERO, G(3)], [ZERO, G(3), ZERO, ZERO],
                      [ZERO, ZERO, G(8), ZERO], [G(3), ZERO, ZERO, G(18)]]
        expected_b = [[G(14), G(6), G(6), ZERO], [G(6), G(9), G(6), ZERO],
                      [G(6), G(6), G(14), ZERO], [ZERO, ZERO, ZERO, G(6)]]
        need(z == 43 and t == 31 and prob == F(43, 124), "ASSIGNED_TRACE_PROBABILITY")
        need_matrix(ma, expected_a, "ASSIGNED_ALICE_MARGINAL")
        need_matrix(mb, expected_b, "ASSIGNED_BOB_MARGINAL")
        print_matrix("ASSIGNED_Q", q)
        print_matrix("ASSIGNED_K", k)
    print("CASE", name, "s", s, "r", r, "w", *(str(x) for x in w),
          "trace", z, "success", prob, "PPT", ppt, why,
          "SN2_CERTIFICATES", ",".join(certificates))
    print_matrix("ACTUAL_R_" + name, actual)
    print_matrix("ACTUAL_PARTIAL_TRANSPOSE_" + name, rt)
    print_matrix("ALICE_MARGINAL_UNNORMALIZED_" + name, ma)
    print_matrix("BOB_MARGINAL_UNNORMALIZED_" + name, mb)
    return q, k, actual, rt


def controls(mean3, mean5zero):
    s, r = F(5), F(2)
    w = (G(2, 1), G(1), G(F(8, 5), F(4, 5)))
    q, k = source(s, r), canonical_k(w)
    actual = filtered(q, k)
    pt = transpose_b(actual, 4, 4)
    wrong_pt = filtered(transpose_b(q, 4, 5), k)
    need(pt[0][14]-wrong_pt[0][14] == G(0, -2*s), "WRONG_KBAR_CONTROL_SIGNATURE")
    rejected("WRONG_KBAR", lambda: need_matrix(pt, wrong_pt, "WRONG_KBAR"))

    w4 = (G(2, 1), G(1, 1), ZERO)
    five, four = check_five(w4), mean_outer(character_five(w4, 4))
    need(four[4][14]-five[4][14] == -w4[1].conj(), "FOUR_ROOT_CONTROL_D32_SIGNATURE")
    rejected("FOUR_ROOT_CROSS_TERM", lambda: need_matrix(four, five, "FOUR_ROOT_CROSS_TERM"))

    mean5 = check_five(w)
    delta_wrong = s-w[1].norm2()-w[2].norm2()
    wrong_delta = ellipsoid_rhs(s, r, w, mean5, delta_override=delta_wrong)
    need(wrong_delta[14][14]-actual[14][14] == G(w[2].norm2()/(s-1)),
         "DELTA_DENOMINATOR_CONTROL_SIGNATURE")
    rejected("DELTA_DENOMINATOR", lambda: need_matrix(wrong_delta, actual, "DELTA_DENOMINATOR"))
    wrong_cross = ellipsoid_rhs(s, r, w, mean5, conjugate_gamma=True)
    need(wrong_cross[2][14]-actual[2][14] == G(s)*(w[2]-w[2].conj()),
         "ELLIPSOID_CONJUGATE_CONTROL_SIGNATURE")
    rejected("ELLIPSOID_GAMMA_CONJUGATE",
             lambda: need_matrix(wrong_cross, actual, "ELLIPSOID_GAMMA_CONJUGATE"))

    # The deliberately reversed gap is not an actual exclusion from the line.
    beta2 = G(1).norm2()
    need(beta2 <= 3 and 3*beta2 >= 1, "BETA_OVERLAP_SETUP")
    rejected("BETA_COVERAGE_GAP", lambda: need(beta2 < F(1, 3) or beta2 > 3,
                                               "BETA_COVERAGE_GAP"))
    need(F(1, 5) <= 5 and 5*F(1, 5) == 1, "BETA_LOWER_ENDPOINT")
    need(F(5) <= 5 and 5*F(5) >= 1, "BETA_UPPER_ENDPOINT")

    gamma = G(40, 30)
    true_gamma = direct_output(F(3), F(3), (ZERO, ZERO, gamma))
    wrong_gamma = gamma_line_rhs(F(3), F(3), gamma, mean5zero, wrong_conjugate=True)
    need(wrong_gamma[2][14]-true_gamma[2][14] == G(3)*(gamma-gamma.conj()),
         "GAMMA_LINE_CONJUGATE_CONTROL_SIGNATURE")
    rejected("GAMMA_LINE_CONJUGATE",
             lambda: need_matrix(wrong_gamma, true_gamma, "GAMMA_LINE_CONJUGATE"))

    # [0w] is an actual nonzero rank-one range vector: its 00 entry need not vanish.
    product = physical_vectors(w)[6]
    for rows in combinations(range(4), 2):
        for cols in combinations(range(4), 2):
            need(product[4*rows[0]+cols[0]]*product[4*rows[1]+cols[1]]
                 - product[4*rows[0]+cols[1]]*product[4*rows[1]+cols[0]] == ZERO,
                 "PRODUCT_VECTOR_RANK_ONE")
    need(product[5] == ZERO and product[0] == w[0] and product[0] != ZERO,
         "PRODUCT_VECTOR_WRONG_INDEX_SETUP")
    need(actual[5][5] == ONE, "ACTUAL_11_DIAGONAL")
    rejected("WRONG_PRODUCT_VECTOR_00_INDEX",
             lambda: need(product[0] == ZERO, "WRONG_PRODUCT_VECTOR_00_INDEX"))
    rejected("FILTERED_IFF_SCOPE_OVERCLAIM",
             lambda: check_scope("PARENT_SUFFICIENT", "FILTERED_PPT_IFF_PARENT_REGION"))
    rejected("FINITE_TO_UNIVERSAL_SCOPE_OVERCLAIM",
             lambda: check_scope("FINITE_CASE", "UNIVERSAL_FILTERED_PPT_CLASSIFICATION"))


def main():
    formal_range_identities()
    mean3 = check_three()
    mean5zero = check_five((ZERO, ZERO, ZERO))
    cases = [
        ("assigned", 3, 3, (G(1), G(1), G(1))),
        ("zero", 3, 3, (ZERO, ZERO, ZERO)),
        ("both-boundaries-complex", 5, 2, (G(2, 1), G(1), G(F(8, 5), F(4, 5)))),
        ("huge-alpha-complex", 5, 2, (G(100000, 70001), G(1, 1), G(1, -1))),
        ("beta-outside-ellipse", 3, 3, (ZERO, G(2, 1), ZERO)),
        ("beta-lower-endpoint", 5, 2, (ZERO, G(F(1, 5), F(2, 5)), ZERO)),
        ("beta-upper-endpoint", 5, 2, (ZERO, G(1, 2), ZERO)),
        ("gamma-large-outside", 3, 3, (ZERO, ZERO, G(40, 30))),
        ("outside-source", 2, 2, (ZERO, ZERO, ZERO)),
    ]
    for name, s, r, w in cases:
        test_case(name, s, r, w, mean3, mean5zero)
    controls(mean3, mean5zero)
    print("FINISHED_FINITE_EXACT_CHECKS_ONLY_NO_UNIVERSAL_SN3_CLAIM")


if __name__ == "__main__":
    main()
