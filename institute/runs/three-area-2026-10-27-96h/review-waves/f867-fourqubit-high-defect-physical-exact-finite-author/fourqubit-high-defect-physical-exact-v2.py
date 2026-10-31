#!/usr/bin/env python3
"""UNRUN author source: finite exact checks, not a global spectral theorem.

Python >=3.10, standard library only.  Parent must read the COMPLETE source,
freeze its hash and issue a separate one-shot GO before executing.  All physics
arithmetic is in Q(i,sqrt(6)); there are no floating-point tolerances.  The
monotonic clock is used only for a cooperative resource deadline.  A parent
launcher must separately impose an outer wall limit <=55 seconds.  The program
writes no files and launches no processes.  It reports INCOMPLETE, not PASS,
if its internal 36-second deadline is encountered at a cooperative guard.
"""
import itertools
import json
import math
import signal
import sys
import time


class Exact:
    """(a+b*sqrt(6)+i*(c+d*sqrt(6)))/n; canonical integer coefficients."""
    __slots__ = ("a", "b", "c", "d", "n")

    def __init__(self, a=0, b=0, c=0, d=0, n=1):
        if n == 0:
            raise ZeroDivisionError("zero denominator")
        if n < 0:
            a, b, c, d, n = -a, -b, -c, -d, -n
        g = math.gcd(a, b, c, d, n)
        self.a, self.b, self.c, self.d, self.n = (
            a // g, b // g, c // g, d // g, n // g
        )

    def __bool__(self):
        return bool(self.a or self.b or self.c or self.d)

    def __eq__(self, other):
        if isinstance(other, int):
            return not (self.b or self.c or self.d) and self.a == other * self.n
        if not isinstance(other, Exact):
            return NotImplemented
        return (self.a, self.b, self.c, self.d, self.n) == (
            other.a, other.b, other.c, other.d, other.n
        )

    def __neg__(self):
        return Exact(-self.a, -self.b, -self.c, -self.d, self.n)

    def __add__(self, other):
        other = exact(other)
        if not self:
            return other
        if not other:
            return self
        return Exact(
            self.a * other.n + other.a * self.n,
            self.b * other.n + other.b * self.n,
            self.c * other.n + other.c * self.n,
            self.d * other.n + other.d * self.n,
            self.n * other.n,
        )

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-exact(other))

    def __rsub__(self, other):
        return exact(other) - self

    def __mul__(self, other):
        other = exact(other)
        if not self or not other:
            return ZERO
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = other.a, other.b, other.c, other.d
        return Exact(
            a * e + 6 * b * f - c * g - 6 * d * h,
            a * f + b * e - c * h - d * g,
            a * g + 6 * b * h + c * e + 6 * d * f,
            a * h + b * g + c * f + d * e,
            self.n * other.n,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError("inverse of zero")
        a, b, c, d, n = self.a, self.b, self.c, self.d, self.n
        e = a * a + 6 * b * b + c * c + 6 * d * d
        f = 2 * (a * b + c * d)
        den = e * e - 6 * f * f
        return Exact(
            n * (a * e - 6 * b * f),
            n * (b * e - a * f),
            n * (6 * d * f - c * e),
            n * (c * f - d * e),
            den,
        )

    def __truediv__(self, other):
        return self * exact(other).inverse()

    def __rtruediv__(self, other):
        return exact(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("only nonnegative integral powers")
        result = ONE
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def conjugate(self):
        return Exact(self.a, self.b, -self.c, -self.d, self.n)

    def real_sign(self):
        if self.c or self.d:
            raise ValueError("ordered comparison of non-real field element")
        a, b = self.a, self.b
        if not a:
            return (b > 0) - (b < 0)
        if not b or (a > 0) == (b > 0):
            return (a > 0) - (a < 0)
        comparison = a * a - 6 * b * b
        if comparison == 0:
            raise ArithmeticError("nonzero rational equals rational sqrt(6)")
        chosen = a if comparison > 0 else b
        return (chosen > 0) - (chosen < 0)

    def __str__(self):
        return f"({self.a},{self.b},{self.c},{self.d})/{self.n}"


def exact(value):
    if isinstance(value, Exact):
        return value
    if isinstance(value, int):
        return Exact(value)
    raise TypeError("physics values must be integral or Exact")


def rat(a, b=1):
    return Exact(a, 0, 0, 0, b)


ZERO = Exact()
ONE = Exact(1)
I = Exact(0, 0, 1)
ROOT6 = Exact(0, 1)
DEADLINE = None
STOP = None
STAGE = "not_started"
CHECKS = 0


class Incomplete(Exception):
    pass


class Failed(Exception):
    pass


def on_signal(signum, _frame):
    global STOP
    STOP = signum


def guard():
    if STOP is not None:
        raise Incomplete("signal-" + str(STOP))
    if DEADLINE is not None and time.monotonic() >= DEADLINE:
        raise Incomplete("cooperative internal deadline")


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise Failed(label)


def le(a, b):
    return (exact(b) - exact(a)).real_sign() >= 0


def zeros(rows, cols=None):
    if cols is None:
        cols = rows
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(a, b)]


def scale(a, scalar):
    return [[scalar * x for x in row] for row in a]


def outer(a, b=None):
    if b is None:
        b = a
    return [[x * y.conjugate() for y in b] for x in a]


def inner(a, b):
    return sum((x.conjugate() * y for x, y in zip(a, b)), ZERO)


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def product(a, b):
    result = zeros(len(a), len(b[0]))
    for i in range(len(a)):
        guard()
        for k, aik in enumerate(a[i]):
            if aik:
                for j, bkj in enumerate(b[k]):
                    if bkj:
                        result[i][j] = result[i][j] + aik * bkj
    return result


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def trace_product(a, b):
    total = ZERO
    for i in range(len(a)):
        guard()
        for j in range(len(a)):
            if a[i][j] and b[j][i]:
                total += a[i][j] * b[j][i]
    return total


def rank(a):
    work = [row[:] for row in a]
    rows, cols = len(work), len(work[0])
    r = 0
    for c in range(cols):
        guard()
        pivot = next((i for i in range(r, rows) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        p = work[r][c]
        for i in range(r + 1, rows):
            if not work[i][c]:
                continue
            factor = work[i][c] / p
            work[i][c] = ZERO
            for j in range(c + 1, cols):
                work[i][j] -= factor * work[r][j]
        r += 1
        if r == rows:
            break
    return r


def psd(a):
    """Exact Hermitian Schur-complement test, including zero-pivot kernels."""
    if a != dagger(a):
        return False
    work = [row[:] for row in a]
    n = len(work)
    for k in range(n):
        guard()
        pivot = None
        for i in range(k, n):
            sign = work[i][i].real_sign()
            if sign < 0:
                return False
            if sign > 0 and pivot is None:
                pivot = i
        if pivot is None:
            return all(not work[i][j] for i in range(k, n)
                       for j in range(k, n))
        work[k], work[pivot] = work[pivot], work[k]
        for row in work:
            row[k], row[pivot] = row[pivot], row[k]
        p = work[k][k]
        for i in range(k + 1, n):
            if not work[i][k]:
                continue
            factor = work[i][k] / p
            for j in range(k + 1, n):
                if work[k][j]:
                    work[i][j] -= factor * work[k][j]
    return True


def cut_index(x, keep):
    result = 0
    for q in keep:
        result = (result << 1) | ((x >> (3 - q)) & 1)
    return result


def reduced(a, keep):
    keep = tuple(keep)
    discarded = sum(1 << (3 - q) for q in range(4) if q not in keep)
    idx = [cut_index(i, keep) for i in range(16)]
    out = zeros(1 << len(keep))
    for i in range(16):
        guard()
        for j in range(16):
            if not ((i ^ j) & discarded):
                out[idx[i]][idx[j]] += a[i][j]
    return out


def physical_layers(a):
    layers = {0: eye(16), 4: a}
    marginals = {}
    for size in (1, 2, 3):
        layer = zeros(16)
        for keep in itertools.combinations(range(4), size):
            m = reduced(a, keep)
            marginals[keep] = m
            discarded = sum(1 << (3 - q) for q in range(4) if q not in keep)
            idx = [cut_index(i, keep) for i in range(16)]
            for i in range(16):
                guard()
                for j in range(16):
                    if not ((i ^ j) & discarded):
                        layer[i][j] += m[idx[i]][idx[j]]
        layers[size] = layer
    return layers, marginals


def apply_local_vector(v, unitaries):
    out = v[:]
    for q, u in enumerate(unitaries):
        bit = 1 << (3 - q)
        old = out
        out = []
        for i in range(16):
            row = 1 if i & bit else 0
            out.append(u[row][0] * old[i & ~bit] + u[row][1] * old[i | bit])
    return out


def conjugate_local(a, unitaries):
    out = a
    for q, u in enumerate(unitaries):
        guard()
        if u == eye(2):
            continue
        bit = 1 << (3 - q)
        old = out
        out = zeros(16)
        for r in range(16):
            guard()
            rr = 1 if r & bit else 0
            for c in range(16):
                cc = 1 if c & bit else 0
                value = ZERO
                for x in (0, 1):
                    ri = (r & ~bit) | (x * bit)
                    for y in (0, 1):
                        ci = (c & ~bit) | (y * bit)
                        value += u[rr][x] * old[ri][ci] * u[cc][y].conjugate()
                out[r][c] = value
    return out


def spinflip(a, transpose=True):
    out = zeros(16)
    for i in range(16):
        for j in range(16):
            sign = -1 if ((i.bit_count() + j.bit_count()) & 1) else 1
            out[i][j] = sign * (a[15 - j][15 - i] if transpose
                                else a[15 - i][15 - j])
    return out


def theta(v):
    return [(-1 if i.bit_count() & 1 else 1) * v[15 - i].conjugate()
            for i in range(16)]


def bilinear(v, w):
    return sum((v[i] * (-1 if i.bit_count() & 1 else 1) * w[15 - i]
                for i in range(16)), ZERO)


def pauli_vector(v, q, which):
    bit = 1 << (3 - q)
    out = []
    for i in range(16):
        if which == "X":
            out.append(v[i ^ bit])
        elif which == "Y":
            out.append((I if i & bit else -I) * v[i ^ bit])
        else:
            out.append((-1 if i & bit else 1) * v[i])
    return out


def channel(a, retention):
    """Apply the physical local map independently on all four qubits."""
    b = (ONE - retention) / 2
    out = a
    for q in range(4):
        bit = 1 << (3 - q)
        old = out
        out = zeros(16)
        for r in range(16):
            guard()
            for c in range(16):
                value = retention * old[r][c]
                if not ((r ^ c) & bit):
                    value += b * (old[r & ~bit][c & ~bit] + old[r | bit][c | bit])
                out[r][c] = value
    return out


def reconstruct_index(left, x, y):
    right = tuple(q for q in range(4) if q not in left)
    answer = 0
    for sequence, value in ((left, x), (right, y)):
        for pos, qubit in enumerate(sequence):
            if (value >> (len(sequence) - 1 - pos)) & 1:
                answer |= 1 << (3 - qubit)
    return answer


def minor_polynomial(psi, vac, left, rows, cols):
    def entries(vector):
        return [[vector[reconstruct_index(left, r, c)] for c in cols] for r in rows]
    a, b = entries(psi), entries(vac)
    a2 = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    ab = (a[0][0] * b[1][1] + b[0][0] * a[1][1]
          - a[0][1] * b[1][0] - b[0][1] * a[1][0])
    b2 = b[0][0] * b[1][1] - b[0][1] * b[1][0]
    return a2, ab, b2


def reference_prefixes():
    result = {}
    for j in range(5):
        values = []
        for h in range(5):
            values.extend([math.comb(4 - h, j) if j <= 4 - h else 0]
                          * math.comb(4, h))
        running, pref = ZERO, []
        for value in values:
            running += value
            pref.append(running)
        result[j] = pref
    return result


def output_reference(t):
    hi, lo = (ONE + t) / 2, (ONE - t) / 2
    values = []
    for h in range(5):
        values.extend([hi ** (4 - h) * lo ** h] * math.comb(4, h))
    total, result = ZERO, []
    for value in values:
        total += value
        result.append(total)
    return result


def householder_projectors():
    """One nested family of literal, complex, physical rank-k projectors."""
    v = [ONE + I * (j % 3) for j in range(16)]
    n = inner(v, v)
    require(n == 41, "projector Householder vector norm")
    w = sub(eye(16), scale(outer(v), rat(2, 41)))
    require(w == dagger(w), "Householder Hermitian")
    require(product(w, w) == eye(16), "Householder unitary")
    qs = []
    q = zeros(16)
    for j in range(16):
        col = [w[i][j] for i in range(16)]
        q = add(q, outer(col))
        qs.append(q)
        require(trace(q) == j + 1 and q == dagger(q), "literal projector trace/Hermitian")
    return v, qs


def expectation_prefixes(a, v):
    """Tr[(W P_k W) a], all k, with W=I-2vv*/41 and the SAME W."""
    av = []
    for i in range(16):
        guard()
        av.append(sum((a[i][j] * v[j] for j in range(16)), ZERO))
    total = inner(v, av)
    require(total == total.conjugate(), "Hermitian Householder expectation")
    diagonal = cross = norm = ZERO
    result = []
    for j in range(16):
        diagonal += a[j][j]
        cross += v[j].conjugate() * av[j]
        norm += v[j].conjugate() * v[j]
        value = diagonal - rat(2, 41) * (cross + cross.conjugate())
        value += rat(4, 41 * 41) * norm * total
        require(value == value.conjugate(), "real projector expectation")
        result.append(value)
    return result


def main():
    global STAGE
    STAGE = "field and local unitaries"
    require(ROOT6 * ROOT6 == 6 and I * I == -1, "field generators")
    require((ONE + I * ROOT6) * (ONE + I * ROOT6).inverse() == 1,
            "field inverse control")
    u1 = [[rat(3, 5), I * rat(4, 5)], [I * rat(4, 5), rat(3, 5)]]
    u2 = [[rat(3, 5), rat(4, 5)], [-rat(4, 5), rat(3, 5)]]
    u3 = [[ONE, ZERO], [ZERO, I]]
    unit = [u1, u2, u3, eye(2)]
    for u in unit:
        require(product(u, dagger(u)) == eye(2), "actual local unitary")

    STAGE = "actual states and marginals"
    vac = [ZERO for _ in range(16)]
    vac[0] = ONE
    psi = [rat(1, 3) if i.bit_count() == 2 else
           I * ROOT6 / 6 if i in (0, 15) else ZERO for i in range(16)]
    require(inner(psi, psi) == 1 and inner(vac, vac) == 1, "state normalization")
    require(inner(psi, vac) == -I * ROOT6 / 6, "physical overlap")
    rvac, rpsi = apply_local_vector(vac, unit), apply_local_vector(psi, unit)
    require(inner(rpsi, rpsi) == 1 and inner(rvac, rvac) == 1, "rotated norms")
    base_p, base_p_m = physical_layers(outer(vac))
    base_s, base_s_m = physical_layers(outer(psi))
    rot_p, _ = physical_layers(outer(rvac))
    rot_s, _ = physical_layers(outer(rpsi))
    for j in (1, 2, 3):
        require(conjugate_local(base_p[j], unit) == rot_p[j], "vacuum layer covariance")
        require(conjugate_local(base_s[j], unit) == rot_s[j], "pure layer covariance")
    pair = [[rat(5, 18), ZERO, ZERO, ZERO],
            [ZERO, rat(2, 9), rat(2, 9), ZERO],
            [ZERO, rat(2, 9), rat(2, 9), ZERO],
            [ZERO, ZERO, ZERO, rat(5, 18)]]
    for keep, m in base_s_m.items():
        require(trace(m) == 1 and m == dagger(m), "actual pure marginal")
        if len(keep) == 1:
            require(m == scale(eye(2), rat(1, 2)), "singleton formula")
        if len(keep) == 2:
            require(m == pair and trace_product(m, m) == rat(19, 54),
                    "pair matrix and purity")
    for j in range(5):
        for x in range(16):
            expected = math.comb(4 - x.bit_count(), j) if j <= 4 - x.bit_count() else 0
            for y in range(16):
                require(base_p[j][x][y] == (expected if x == y else 0),
                        "product layer eigenbasis")
    require(base_s[1] == scale(eye(16), 2), "pure H1")
    require(trace(base_s[2]) == 24 and psd(sub(base_s[2], eye(16)))
            and psd(sub(scale(eye(16), 3), base_s[2])), "pure H2 I<=H2<=3I")
    require(trace(base_s[3]) == 8 and trace_product(base_s[3], base_s[3]) == rat(74, 9),
            "pure H3 trace and exact second moment")
    require(trace_product(base_s[3], base_p[3]) == rat(14, 3)
            and trace_product(base_p[3], base_p[3]) == 20, "H3 cross and vacuum moments")
    require(psd(base_s[3]) and psd(sub(scale(eye(16), 4), base_s[3])),
            "pure H3 positivity and upper bound")

    STAGE = "finite H3 rank and cut witnesses"
    twirl = scale(outer(psi), 2)
    for q in range(4):
        for which in ("X", "Y", "Z"):
            twirl = add(twirl, scale(outer(pauli_vector(psi, q, which)), rat(1, 2)))
    require(twirl == base_s[3], "actual thirteen-vector H3 rank witness")
    require(rank(base_s[3]) <= 13, "actual pure H3 rank at most thirteen")
    for k in (2, 3, 4):
        require(le(k * rat(74, 9), (k + 3) * (k + 3)), "H3 finite Cauchy rank bound")
    for left in ((0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3)):
        columns = (1, 3) if len(left) == 1 else (2, 3)
        require(minor_polynomial(psi, vac, left, (0, 1), columns)
                == (-rat(1, 9), ZERO, ZERO), "cut minor -a^2/9")
    require(bilinear(psi, psi) == rat(1, 3)
            and bilinear(psi, vac) == I * ROOT6 / 6
            and bilinear(vac, vac) == 0, "range spin-flip bilinear coefficients")
    xi = [psi[j] - I * ROOT6 / 3 * vac[j] for j in range(16)]
    xn = [psi[j] + I * ROOT6 / 6 * vac[j] for j in range(16)]
    require(theta(xi) == xi and bilinear(xn, xn) == 0,
            "actual eta-one and eta-zero range rays")

    STAGE = "physical projectors"
    vec, projectors = householder_projectors()
    test_prefix = expectation_prefixes(rot_s[2], vec)
    for k, qproj in enumerate(projectors, 1):
        require(trace_product(qproj, rot_s[2]) == test_prefix[k - 1],
                "literal projector vs fast same-Q formula")
    refs = reference_prefixes()
    cases = {}
    for frame, v, pure, p_layers, s_layers in (
        ("identity", vac, psi, base_p, base_s),
        ("complex_local", rvac, rpsi, rot_p, rot_s),
    ):
        for q in (ZERO, rat(1, 8)):
            guard()
            STAGE = "density " + frame + " q=" + str(q)
            rho = add(scale(outer(pure), ONE - q), scale(outer(v), q))
            layers, marg = physical_layers(rho)
            require(rho == dagger(rho) and trace(rho) == 1, "actual density Hermitian trace one")
            require(rank(rho) == (1 if not q else 2), "actual density rank")
            for keep, m in marg.items():
                require(m == dagger(m) and trace(m) == 1, "actual mixed marginal")
            for j in range(5):
                require(layers[j] == add(scale(s_layers[j], ONE - q), scale(p_layers[j], q)),
                        "same-density physical layer linearity")
            require(trace(layers[2]) == 24 and trace(layers[3]) == 8, "mixed H2/H3 traces")
            expected_moment = (rat(74) - 64 * q + 170 * q * q) / 9
            require(trace_product(layers[3], layers[3]) == expected_moment,
                    "mixed H3 actual exact second moment")
            require(expected_moment == (rat(74, 9) if not q else rat(2197, 288)),
                    "selected H3 moment")
            if frame == "identity":
                require(psd(sub(layers[2], scale(eye(16), ONE - q)))
                        and psd(sub(scale(eye(16), 3 + 3 * q), layers[2])),
                        "mixed H2 PSD bounds")
                require(psd(layers[3]) and psd(sub(scale(eye(16), 4), layers[3])),
                        "mixed H3 positivity and upper bound")
            delta = scale(sub(rho, spinflip(rho)), rat(1, 2))
            d2 = q * q + (ONE - q) ** 2 * rat(8, 9)
            require(delta == dagger(delta) and trace(delta) == 0 and rank(delta) == 2,
                    "actual spin-flip defect rank and Hermiticity")
            require(trace_product(delta, delta) == d2 / 2,
                    "actual defect spectrum squared identity")
            require(d2 == (rat(8, 9) if not q else rat(401, 576)), "selected defect")
            require(le(rat(3, 13), d2) and d2 != rat(3, 13), "outside mixed defect region")
            require(le(q, (ONE - q) / 3) and q != (ONE - q) / 3,
                    "range hull obstruction strict")
            positive_j = {j: expectation_prefixes(layers[j], vec) for j in range(5)}
            negative_j = {j: expectation_prefixes(spinflip(layers[j]), vec) for j in range(5)}
            for p in (ZERO, rat(1, 2), rat(2, 3), ONE, rat(4, 3)):
                guard()
                STAGE = "channel " + frame + " q=" + str(q) + " p=" + str(p)
                lam = ONE - p
                negative = lam.real_sign() < 0
                t = -lam if negative else lam
                b = (ONE - t) / 2
                coeff = [t ** j * b ** (4 - j) for j in range(5)]
                out = channel(rho, lam)
                pure_output = channel(rho, t)
                if negative:
                    require(out == spinflip(pure_output), "FULL-transpose negative channel")
                basis = negative_j if negative else positive_j
                output_exp = expectation_prefixes(out, vec)
                ref = output_reference(t)
                for k in range(1, 17):
                    actual = output_exp[k - 1]
                    layer_sum = sum((coeff[j] * basis[j][k - 1] for j in range(5)), ZERO)
                    reference_sum = sum((coeff[j] * refs[j][k - 1] for j in range(5)), ZERO)
                    require(actual == layer_sum, "same physical Q and actual layers")
                    require(ref[k - 1] == reference_sum, "coordered product reference")
                    for j in range(5):
                        require(le(basis[j][k - 1], refs[j][k - 1]), "finite physical layer inequality")
                    g = 3 if k <= 5 else 5 if k <= 11 else 0
                    require(le(basis[2][k - 1], refs[2][k - 1] - (ONE - q) * g),
                            "finite H2 projector gap")
                    require(le(actual, ref[k - 1] - (ONE - q) * g * t * t * b * b),
                            "finite output projector gap")
                require(output_exp[-1] == 1 and ref[-1] == 1, "rank sixteen boundary")
            cases[(frame, str(q))] = (rho, layers, pure, v)

    STAGE = "reason-specific exact mutants"
    rho, layers, _, v = cases[("complex_local", str(rat(1, 8)))]
    e15 = [ZERO for _ in range(16)]
    e15[15] = ONE
    opposite = apply_local_vector(e15, unit)
    qvac, qopposite = outer(v), outer(opposite)
    require(inner(v, opposite) == 0, "same-Q mutant orthogonal projectors")
    t, b = rat(1, 2), rat(1, 4)
    good = trace_product(qvac, channel(rho, t))
    mixed_projectors = sum(((t ** j) * (b ** (4 - j)) *
                            trace_product(qopposite if j == 1 else qvac, layers[j])
                            for j in range(5)), ZERO)
    require(good - mixed_projectors == rat(1, 256), "same-Q mutant rejected exactly")
    require(spinflip(rho, False) != spinflip(rho, True), "spinflip omission mutant rejected")
    require(rat(74, 9) - (8 + rat(1, 9)) == rat(1, 9),
            "H3 missing-factor-two moment mutant rejected")
    pos = channel(rho, rat(1, 3))
    neg = channel(rho, -rat(1, 3))
    y1 = zeros(16)
    for i in range(16):
        y1[i][i ^ 8] = I if i & 8 else -I
    require(trace_product(y1, pos) == rat(1, 25), "non-real output witness")
    pair_index = next(((i, j) for i in range(16) for j in range(i + 1, 16)
                       if pos[i][j] != pos[j][i]), None)
    require(pair_index is not None, "complex off-diagonal witness exists")
    i, j = pair_index
    w = [ZERO for _ in range(16)]
    w[i], w[j] = ONE, I
    rproj = scale(outer(w), rat(1, 2))
    qphysical = spinflip(rproj)
    require(spinflip(qphysical) == rproj, "full projector transpose involution")
    true_value = trace_product(qphysical, neg)
    require(true_value == trace_product(rproj, pos), "negative physical projector transport")
    require(true_value != trace_product(spinflip(qphysical, False), pos),
            "wrong-projector-transpose mutant rejected")
    for k in (1, 5, 11, 16):
        qphysical = projectors[k - 1]
        rproj = spinflip(qphysical)
        for j in range(5):
            require(trace_product(rproj, layers[j])
                    == negative_j_for(layers[j], vec, k),
                    "same transported projector across all negative layers")
    return {"states": 4, "p_values_per_state": 5, "ranks_per_value": 16,
            "pure_h3_moment": str(rat(74, 9)),
            "mixed_h3_moment": str(rat(2197, 288)),
            "defect_squared": [str(rat(8, 9)), str(rat(401, 576))],
            "same_q_mutant_discrepancy": str(rat(1, 256))}


def negative_j_for(layer, vec, k):
    return expectation_prefixes(spinflip(layer), vec)[k - 1]


def run():
    global DEADLINE
    DEADLINE = time.monotonic() + 36
    status = 1
    try:
        signal.signal(signal.SIGALRM, on_signal)
        signal.signal(signal.SIGTERM, on_signal)
        signal.signal(signal.SIGINT, on_signal)
        signal.setitimer(signal.ITIMER_REAL, 36)
        result = main()
        guard()
        print(json.dumps({"status": "PASS", "checks": CHECKS, "results": result}, sort_keys=True), flush=True)
        status = 0
    except Incomplete as exc:
        print(json.dumps({"status": "INCOMPLETE", "stage": STAGE,
                          "checks": CHECKS, "reason": str(exc)}, sort_keys=True), flush=True)
        status = 2
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "stage": STAGE, "checks": CHECKS,
                          "reason": type(exc).__name__ + ": " + str(exc)}, sort_keys=True), flush=True)
        status = 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    return status


if __name__ == "__main__":
    sys.exit(run())
