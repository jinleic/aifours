
import argparse
import time
from fractions import Fraction as F
from math import factorial

END = float("inf")


class AuditError(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise AuditError(reason)


def tick():
    need(time.monotonic() <= END, "BUDGET_EXCEEDED_NO_PASS")


class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)

    def __add__(self, other):
        other = g(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-g(other))

    def __rsub__(self, other):
        return g(other) - self

    def __mul__(self, other):
        other = g(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = g(other)
        denominator = other.r * other.r + other.i * other.i
        need(denominator != 0, "ZERO_DIVISOR")
        return G((self.r * other.r + self.i * other.i) / denominator,
                 (self.i * other.r - self.r * other.i) / denominator)

    def __rtruediv__(self, other):
        return g(other) / self

    def conjugate(self):
        return G(self.r, -self.i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        other = g(other)
        return self.r == other.r and self.i == other.i

    def __str__(self):
        if not self.i:
            return str(self.r)
        if not self.r:
            return str(self.i) + "i"
        return "(" + str(self.r) + "+" + str(self.i) + "i)"

    __repr__ = __str__


def g(value):
    return value if isinstance(value, G) else G(value)


Z, ONE, II = G(), G(1), G(0, 1)


def zeros(n, m=None):
    return [[Z for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    result = zeros(n)
    for j in range(n):
        result[j][j] = ONE
    return result


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    c = g(c)
    return [[c * x for x in row] for row in a]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def mm(a, b):
    tick()
    result = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        tick()
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        result[i][j] = result[i][j] + x * y
    return result


def inner(v, w):
    return sum((x.conjugate() * y for x, y in zip(v, w)), Z)


def outer(v, w):
    return [[x * y.conjugate() for y in w] for x in v]


def quadratic(a, v):
    return sum((x.conjugate() * a[i][j] * y
                for i, x in enumerate(v) if x
                for j, y in enumerate(v) if y and a[i][j]), Z)


def rank(a):
    b = [row[:] for row in a]
    r = 0
    for j in range(len(b[0])):
        tick()
        p = next((i for i in range(r, len(b)) if b[i][j]), None)
        if p is None:
            continue
        b[r], b[p] = b[p], b[r]
        pivot = b[r][j]
        b[r] = [x / pivot for x in b[r]]
        for i in range(len(b)):
            if i != r and b[i][j]:
                q = b[i][j]
                b[i] = [x - q * y for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def determinant(a):
    b = [row[:] for row in a]
    result = ONE
    for j in range(len(b)):
        tick()
        p = next((i for i in range(j, len(b)) if b[i][j]), None)
        if p is None:
            return Z
        if p != j:
            b[j], b[p] = b[p], b[j]
            result = -result
        pivot = b[j][j]
        result = result * pivot
        for i in range(j + 1, len(b)):
            q = b[i][j] / pivot
            for k in range(j + 1, len(b)):
                b[i][k] = b[i][k] - q * b[j][k]
            b[i][j] = Z
    return result


def is_psd(a):
    if a != dagger(a):
        return False
    b = [row[:] for row in a]
    for k in range(len(b)):
        tick()
        pivot = b[k][k]
        if pivot.i or pivot.r < 0:
            return False
        if not pivot:
            if any(b[k][j] for j in range(k + 1, len(b))):
                return False
            continue
        for i in range(k + 1, len(b)):
            for j in range(i, len(b)):
                value = b[i][j] - b[i][k] * b[k][j] / pivot
                b[i][j] = value
                b[j][i] = value.conjugate()
    return True


def unit(i, j):
    result = zeros(4)
    result[i][j] = ONE
    return result


def vector(items):
    result = [Z for _ in range(16)]
    for i, j, c in items:
        result[4 * i + j] = g(c)
    return result


def coefficient_matrix(v):
    return [v[4 * i:4 * i + 4] for i in range(4)]


def phi(x, mutation="literal"):
    y = [
        [x[0][0] + x[1][1] + x[2][2], x[0][1], x[0][2], x[0][3]],
        [x[1][0], x[1][1] + x[2][2] + x[3][3], x[1][2], x[1][3]],
        [x[2][0], x[2][1], x[2][2] + x[3][3] + x[0][0], x[3][2]],
        [x[3][0], x[3][1], x[2][3], x[3][3] + x[0][0] + x[1][1]],
    ]
    if mutation == "missing_transpose":
        y[2][3], y[3][2] = x[2][3], x[3][2]
    if mutation == "reverse_cycle":
        total = sum((x[i][i] for i in range(4)), Z)
        for i in range(4):
            y[i][i] = total - x[(i + 1) % 4][(i + 1) % 4]
    return scale(1 if mutation == "wrong_scale" else F(1, 3), y)


def repaired(x, lam, delta, schur):
    y = scale(lam, phi(x))
    tr = sum((x[i][i] for i in range(4)), Z)
    for i in range(4):
        for j in range(4):
            y[i][j] = y[i][j] + schur[i][j] * x[i][j]
        y[i][i] = y[i][i] + delta * tr
    return y


def superoperator(function):
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            tick()
            y = function(unit(i, j))
            for a in range(4):
                for b in range(4):
                    result[4 * a + b][4 * i + j] = y[a][b]
    return result


def choi(function):
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            tick()
            block = function(unit(i, j))
            for a in range(4):
                for b in range(4):
                    result[4 * i + a][4 * j + b] = block[a][b]
    return result


def reshuffle(t):
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            for a in range(4):
                for b in range(4):
                    result[4 * i + a][4 * j + b] = t[4 * a + b][4 * i + j]
    return result


def reference_choi(lam, delta, schur):
    result = scale(delta, eye(16))
    for i in range(4):
        for j in range(4):
            m = 0 if (i, j) in ((2, 3), (3, 2)) else 1
            result[5 * i][5 * j] = (
                result[5 * i][5 * j] + lam * F(m, 3) + schur[i][j]
            )
            if i != j and j != (i + 1) % 4:
                q = 4 * i + j
                result[q][q] = result[q][q] + lam * F(1, 3)
    result[11][14] = result[11][14] + lam * F(1, 3)
    result[14][11] = result[14][11] + lam * F(1, 3)
    return result


def drift(x, k):
    return add(mm(k, x), mm(x, dagger(k)))


def scalar_coefficients(n):
    fac = factorial(n)
    e = F(1, 3 ** n * fac)
    common = (F(1) - (-F(1, 3)) ** n) / (4 * fac)
    h = e if n % 2 == 0 else F(0)
    s = e if n % 2 else F(0)
    co = e * (-1) ** (n // 2) if n % 2 == 0 else F(0)
    si = e * (-1) ** ((n - 1) // 2) if n % 2 else F(0)
    populations = [
        common + (h + co) / 2,
        common - (s + si) / 2,
        common + (h - co) / 2,
        common + (-s + si) / 2,
    ]
    return populations, e, h, s


def closed_superoperator_coefficient(n):
    populations, e, h, s = scalar_coefficients(n)
    result = zeros(16)
    for i in range(4):
        for shift in range(4):
            a = (i + shift) % 4
            result[5 * a][5 * i] = g(populations[shift])
        for j in range(4):
            if i != j and (i, j) not in ((2, 3), (3, 2)):
                q = 4 * i + j
                result[q][q] = g(e)
    result[11][11] = result[14][14] = g(h)
    result[14][11] = result[11][14] = g(s)
    return result


def closed_choi_coefficient(n):
    populations, e, h, s = scalar_coefficients(n)
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            if i == j:
                result[5 * i][5 * j] = g(populations[0])
            else:
                result[5 * i][5 * j] = g(
                    h if (i, j) in ((2, 3), (3, 2)) else e
                )
                q = 4 * i + j
                result[q][q] = g(populations[(j - i) % 4])
    result[11][14] = result[14][11] = g(s)
    return result


def must_reject(tag, observed, correct):
    try:
        need(observed == correct, tag)
    except AuditError as error:
        need(str(error) == tag, "WRONG_MUTATION_REJECTION_REASON")
        print("MUTANT_REJECTED", tag, "observed", observed, "correct", correct)
    else:
        raise AuditError(tag + "_ESCAPED")


def main():
    global END
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=50)
    args = parser.parse_args()
    need(1 <= args.seconds <= 55, "INVALID_DEADLINE")
    started = time.monotonic()
    END = started + args.seconds

    need(II * II == -1, "GAUSSIAN_UNIT")
    a = [ONE, II, G(1, 1), Z]
    b = [Z, ONE, II, G(1, -1)]
    ss = add(outer(a, a), scale(F(1, 2), outer(b, b)))
    ss_literal = [
        [G(1), G(0, -1), G(1, -1), Z],
        [II, G(F(3, 2)), G(1, F(1, 2)), G(F(1, 2), F(1, 2))],
        [G(1, 1), G(1, -F(1, 2)), G(F(5, 2)), G(-F(1, 2), F(1, 2))],
        [Z, G(F(1, 2), -F(1, 2)), G(-F(1, 2), -F(1, 2)), ONE],
    ]
    need(ss == ss_literal, "COMPLEX_GRAM_ENTRIES")
    need(is_psd(ss) and rank(ss) == 2, "SINGULAR_COMPLEX_GRAM")
    sf = add(ss, scale(F(1, 7), eye(4)))
    need(is_psd(sf) and rank(sf) == 4, "FULL_RANK_COMPLEX_GRAM")
    s0 = zeros(4)

    p = vector([(2, 3, 1), (3, 2, -1)])
    w = vector([(2, 3, 1), (3, 2, -F(3, 5))])
    v = vector([(2, 3, 1), (3, 2, G(-F(3, 5), F(1, 10)))])
    chi = vector([(0, 1, 1), (1, 0, II)])
    omega = vector([(i, i, 1) for i in range(4)])
    for name, z in (("p", p), ("w", w), ("v", v), ("chi", chi)):
        need(rank(coefficient_matrix(z)) == 2, "RANK_TWO_" + name)
        need(inner(omega, z) == 0, "OMEGA_ORTHOGONAL_" + name)
    need(inner(v, v) == F(137, 100), "COMPLEX_VECTOR_NORM")

    cphi = choi(phi)
    tphi = superoperator(phi)
    need(cphi == reshuffle(tphi), "BASE_RESHUFFLE")
    need(cphi == reference_choi(F(1), F(0), s0), "BASE_FULL_BLOCKS")
    need(quadratic(cphi, p) == -F(1, 3), "SEED_NEGATIVE_QUADRATIC")
    need(quadratic(cphi, v) == -F(83, 300), "COMPLEX_SEED_QUADRATIC")

    cases = [("seed", F(1), F(0), s0, False, None)]
    for name, schur in (("zero", s0), ("singular_complex", ss),
                        ("full_complex", sf)):
        cases.append(("negative_1_5_" + name, F(1), F(1, 5),
                      schur, False, None))
        cases.append(("positive_5_24_" + name, F(1), F(5, 24),
                      schur, True, 16))
        cases.append(("lambda0_delta0_" + name, F(0), F(0),
                      schur, True, rank(schur)))
    cases.extend([
        ("lambda0_positive_complex", F(0), F(1, 7), ss, True, 16),
        ("lambda0_negative_complex", F(0), -F(1, 7), ss, False, None),
        ("lambda2_positive_complex", F(2), F(5, 12), ss, True, 16),
        ("lambda_half_positive_complex", F(1, 2), F(5, 48), ss, True, 16),
    ])
    need(len(cases) == 14, "SELECTED_CASE_COUNT")
    for name, lam, delta, schur, expected_psd, expected_rank in cases:
        function = lambda x, l=lam, d=delta, s=schur: repaired(x, l, d, s)
        c = choi(function)
        need(c == reference_choi(lam, delta, schur), "CASE_BLOCKS_" + name)
        need(c == reshuffle(superoperator(function)), "CASE_RESHUFFLE_" + name)
        need(is_psd(c) == expected_psd, "CASE_PSD_" + name)
        if expected_rank is not None:
            need(rank(c) == expected_rank, "CASE_RANK_" + name)
        qp, qw, qv = (quadratic(c, z) for z in (p, w, v))
        need(qp == 2 * delta - lam / 3, "CASE_P_QUADRATIC_" + name)
        need(qw == F(34, 25) * delta - F(7, 25) * lam,
             "CASE_W_QUADRATIC_" + name)
        need(qv == F(137, 100) * delta - F(83, 300) * lam,
             "CASE_V_QUADRATIC_" + name)
        print("CASE", name, "PSD", expected_psd,
              "q_p", qp, "q_w", qw, "q_complex", qv)

    positive = choi(lambda x: repaired(x, F(1), F(5, 24), s0))
    h0 = [[positive[5 * i][5 * j] for j in range(4)] for i in range(4)]
    for n, numerator in enumerate((13, 105, 725, 1105), start=1):
        minor = [row[:n] for row in h0[:n]]
        need(determinant(minor) == F(numerator, 24 ** n),
             "POSITIVE_D_LEADING_MINOR_" + str(n))
    pair = [[positive[i][j] for j in (11, 14)] for i in (11, 14)]
    need(determinant(pair) == F(1, 576), "POSITIVE_PAIR_DETERMINANT")

    k = [
        [G(1, 1), G(2, -1), Z, Z],
        [Z, G(-F(1, 2), F(1, 3)), Z, Z],
        [Z, Z, Z, G(1, 2)],
        [Z, Z, G(-2, 1), G(F(3, 4), -1)],
    ]
    dk = lambda x: drift(x, k)
    cd = choi(dk)
    vk = [k[a][i] for i in range(4) for a in range(4)]
    drift_formula = add(outer(vk, omega), outer(omega, vk))
    need(cd == drift_formula, "COMPLEX_K_DRIFT_OUTER_IDENTITY")
    need(cd == reshuffle(superoperator(dk)), "COMPLEX_K_DRIFT_RESHUFFLE")
    need(quadratic(cd, omega) == 10, "PLUS_K_DRIFT_SIGN")
    for name, z in (("p", p), ("w", w), ("v", v), ("chi", chi)):
        need(quadratic(cd, z) == 0, "ORTHOGONAL_DRIFT_ZERO_" + name)
    cl = choi(lambda x: add(dk(x), repaired(x, F(1), F(1, 5), ss)))
    need(cl == add(cd, choi(lambda x: repaired(x, F(1), F(1, 5), ss))),
         "COMPLEX_GENERATOR_LINEARITY")
    need(quadratic(cl, v) == -F(1, 375), "COMPLEX_GENERATOR_NEGATIVE")
    print("COMPLEX_K_IDENTITY_AND_SIGN_CHECKED")

    power = eye(16)
    for n in range(13):
        direct = scale(F(1, factorial(n)), power)
        closed = closed_superoperator_coefficient(n)
        need(direct == closed, "TAYLOR_FULL_SUPEROPERATOR_" + str(n))
        need(reshuffle(direct) == closed_choi_coefficient(n),
             "TAYLOR_FULL_CHOI_" + str(n))
        denominator = 3 ** n * factorial(n)
        first_column = [direct[5 * i][0] * denominator for i in range(4)]
        print("TAYLOR", n, "FULL_MATRICES_EQUAL",
              "scaled_population_column", first_column)
        if n < 12:
            power = mm(tphi, power)

    must_reject(
        "MISSING_34_43_TRANSPOSE",
        quadratic(choi(lambda x: phi(x, "missing_transpose")), p),
        -F(1, 3),
    )
    must_reject(
        "WRONG_ONE_THIRD_SCALE",
        choi(lambda x: phi(x, "wrong_scale"))[0][0],
        F(1, 3),
    )
    must_reject(
        "WRONG_CYCLIC_ORIENTATION",
        choi(lambda x: phi(x, "reverse_cycle"))[1][1],
        0,
    )
    must_reject(
        "INCORRECT_CHOI_RESHAPE",
        tphi[1][1],
        cphi[1][1],
    )
    must_reject(
        "NEGATIVE_K_DRIFT_CONVENTION",
        quadratic(choi(lambda x: scale(-1, dk(x))), omega),
        10,
    )

    tick()
    print("ALL_SPECIFIED_FINITE_CHECKS_PASSED",
          "elapsed_seconds", time.monotonic() - started)


if __name__ == "__main__":
    try:
        main()
    except AuditError as error:
        print("FAIL", error)
        raise SystemExit(1)

