#!/usr/bin/env python3
"""Independent exact checker for the pinned rational-inner P24 witness.

Prepared for a separately admitted run. Preparing this file is not permission to
execute it. It imports no producer/verifier code and uses no numerical samples.
The finite identities do not replace the separate real-Grassmann/open-set proof.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import signal
import sys
import time
from fractions import Fraction as F

PROOF_PIN = "267d717cd735537ff8c29a3c73a17ed7fb1f7939c85788a8cbd60374f74ab8a0"
RADIUS_PIN = "0708964e71ee8c3858b206bb6d192c73ef73df33b39084a1bf260ed46f6db043"
REPO = Path(__file__).resolve().parents[5]
PROOF = REPO / "information-science/evidence/three-area-20261023-96h/proof-SOF24-rational-inner-candidate-v1.md"
RADIUS_PROOF = REPO / "information-science/evidence/three-area-20261023-96h/parallel-18/sof24/proof-rational-inner-ADDENDUM-1-explicit-radius.md"
MAX_INPUT = 4 * 1024 * 1024
MAX_SOURCE = 1024 * 1024
MAX_BITS = 1000000
ZERO = (F(0),)
ONE = (F(1),)
RAT = re.compile(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z")
END = float("inf")
INTERRUPT = ""
MEMORY_BYTES = 1024 * 1024 * 1024
LAST_RSS_CHECK = 0.0


class CheckError(Exception):
    def __init__(self, code, detail):
        super().__init__(detail)
        self.code = code
        self.detail = detail


def require(condition, code, detail):
    if not condition:
        raise CheckError(code, detail)


def peak_rss():
    native = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        return native, native, "bytes"
    if sys.platform.startswith("linux"):
        return native, native * 1024, "KiB"
    return native, None, "platform-native-unresolved"


def tick():
    global LAST_RSS_CHECK
    now = time.monotonic()
    require(not INTERRUPT, "INCOMPLETE_INTERRUPTED", INTERRUPT)
    require(now < END, "INCOMPLETE_DEADLINE", "internal cooperative deadline reached")
    if now - LAST_RSS_CHECK >= 0.1:
        LAST_RSS_CHECK = now
        _, count, _ = peak_rss()
        require(count is None or count <= MEMORY_BYTES,
                "INCOMPLETE_MEMORY", "cooperative peak-RSS ceiling reached")


def interrupt_handler(number, _frame):
    global INTERRUPT
    if not INTERRUPT:
        INTERRUPT = signal.Signals(number).name


def norm(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    if not a:
        a = [F(0)]
    require(all(x.numerator.bit_length() <= MAX_BITS and
                x.denominator.bit_length() <= MAX_BITS for x in a),
            "INCOMPLETE_COEFFICIENT_SIZE", "exact coefficient bit ceiling reached")
    return tuple(a)


def add(a, b):
    tick()
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return norm(out)


def scale(a, c):
    return norm(x * c for x in a)


def sub(a, b):
    return add(a, scale(b, F(-1)))


def mul(a, b):
    tick()
    if a == ZERO or b == ZERO:
        return ZERO
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
            tick()
    return norm(out)


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def coefficient(a, i):
    return a[i] if i < len(a) else F(0)


def divrem(a, b):
    require(b != ZERO, "INTERNAL_DIVISION", "zero polynomial divisor")
    rem = a
    out = [F(0)] * max(1, len(a) - len(b) + 1)
    while rem != ZERO and len(rem) >= len(b):
        tick()
        shift = len(rem) - len(b)
        factor = rem[-1] / b[-1]
        out[shift] += factor
        rem = sub(rem, (F(0),) * shift + scale(b, factor))
    return norm(out), rem


def exact_div(a, b):
    q, r = divrem(a, b)
    require(r == ZERO, "INTERNAL_BAREISS_DIVISION", "nonexact polynomial Bareiss division")
    return q


def gcd(a, b):
    while b != ZERO:
        _, r = divrem(a, b)
        a, b = b, r
    return scale(a, 1 / a[-1]) if a != ZERO else ZERO


def polynomial_det(matrix):
    """Fraction-free polynomial Bareiss with exact row pivoting."""
    n = len(matrix)
    if n == 0:
        return ONE
    require(all(len(row) == n for row in matrix), "INTERNAL_SHAPE", "nonsquare determinant")
    a = [list(row) for row in matrix]
    previous = ONE
    sign = F(1)
    for k in range(n - 1):
        tick()
        pivot_row = next((r for r in range(k, n) if a[r][k] != ZERO), None)
        if pivot_row is None:
            return ZERO
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = sub(mul(pivot, a[i][j]), mul(a[i][k], a[k][j]))
                a[i][j] = exact_div(numerator, previous)
            a[i][k] = ZERO
        previous = pivot
    return scale(a[-1][-1], sign)


def rref(matrix, ncols=None):
    a = [list(row) for row in matrix]
    if ncols is None:
        ncols = len(a[0]) if a else 0
    require(all(len(row) == ncols for row in a), "INTERNAL_SHAPE", "ragged rational matrix")
    pivots = []
    row = 0
    for col in range(ncols):
        tick()
        p = next((i for i in range(row, len(a)) if a[i][col]), None)
        if p is None:
            continue
        a[row], a[p] = a[p], a[row]
        v = a[row][col]
        a[row] = [x / v for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                v = a[i][col]
                a[i] = [x - v * y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def nullspace(matrix, ncols):
    a, pivots = rref(matrix, ncols)
    result = []
    for col in range(ncols):
        if col not in pivots:
            x = [F(0)] * ncols
            x[col] = F(1)
            for i, p in enumerate(pivots):
                x[p] = -a[i][col]
            result.append(x)
    return result


def rational_det(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    out = F(1)
    for k in range(n):
        tick()
        p = next((i for i in range(k, n) if a[i][k]), None)
        if p is None:
            return F(0)
        if p != k:
            a[k], a[p] = a[p], a[k]
            out = -out
        pivot = a[k][k]
        out *= pivot
        for i in range(k + 1, n):
            factor = a[i][k] / pivot
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
            a[i][k] = F(0)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    require(bool(a) and bool(b) and len(a[0]) == len(b), "INTERNAL_SHAPE", "matrix product mismatch")
    out = [[F(0) for _ in b[0]] for _ in a]
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i][k]:
                for j in range(len(b[0])):
                    out[i][j] += a[i][k] * b[k][j]
        tick()
    return out


def pmatmul(a, b):
    require(bool(a) and bool(b) and len(a[0]) == len(b), "INTERNAL_SHAPE", "polynomial product mismatch")
    out = [[ZERO for _ in b[0]] for _ in a]
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i][k] != ZERO:
                for j in range(len(b[0])):
                    out[i][j] = add(out[i][j], mul(a[i][k], b[k][j]))
    return out


def constant_matrix(a):
    return [[(x,) for x in row] for row in a]


# Gaussian rationals are pairs; Gaussian polynomials are pairs of real polynomials.
def gadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def gmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(a, s):
    return a[0] * s, a[1] * s


def gconj(a):
    return a[0], -a[1]


def gdiv(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    require(d != 0, "INTERNAL_GAUSSIAN_DIVISION", "zero Gaussian divisor")
    return gscale(gmul(a, gconj(b)), 1 / d)


def cpadd(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def cpmul(a, b):
    return sub(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))


def cpscale(a, c):
    return sub(scale(a[0], c[0]), scale(a[1], c[1])), add(scale(a[0], c[1]), scale(a[1], c[0]))


def cppower(a, n):
    out = (ONE, ZERO)
    for _ in range(n):
        out = cpmul(out, a)
    return out


def cpconj(a):
    return a[0], scale(a[1], F(-1))


def gaussian_coefficients(a):
    return [(coefficient(a[0], i), coefficient(a[1], i)) for i in range(max(len(a[0]), len(a[1])))]


def laurent_product(a, b):
    out = {}
    for i, x in enumerate(gaussian_coefficients(a)):
        for j, y in enumerate(gaussian_coefficients(b)):
            out[i - j] = gadd(out.get(i - j, (F(0), F(0))), gmul(x, gconj(y)))
    return {k: v for k, v in out.items() if v != (0, 0)}


def circle_norm(p, q):
    out = laurent_product(p, p)
    for k, v in laurent_product(q, q).items():
        out[k] = gadd(out.get(k, (F(0), F(0))), v)
    out = {k: v for k, v in out.items() if v != (0, 0)}
    require(out == {0: (F(1), F(0))}, "CIRCLE_NORM_IDENTITY", "literal inner-pair norm polynomial differs from one")


def raw_curve():
    n = ((F(0), F(1)), ONE)
    d = ((F(0), F(1)), (F(-1),))
    n2d2 = cpmul(cppower(n, 2), cppower(d, 2))
    n3d = cpmul(cppower(n, 3), d)
    p = cpscale(cpadd(cpadd(cpscale(n2d2, (F(0), F(4))),
                            cpscale(n3d, (F(3), F(-4)))),
                      cpscale(cppower(n, 4), (F(3), F(0)))), (F(1, 10), F(0)))
    q = cpscale(cpadd(cpadd(cpscale(cpmul(n, cppower(d, 3)), (F(3), F(0))),
                            cpscale(n2d2, (F(-3), F(4)))),
                      cpscale(n3d, (F(0), F(4)))), (F(1, 10), F(0)))
    c = cppower(d, 4)
    circle_p = ((F(0), F(0), F(0), F(3, 10), F(3, 10)),
                (F(0), F(0), F(2, 5), F(-2, 5)))
    circle_q = ((F(0), F(3, 10), F(-3, 10)),
                (F(0), F(0), F(2, 5), F(2, 5)))
    circle_norm(circle_p, circle_q)
    expected_laurent = {
        -1: (F(4, 25), F(0)), 0: (F(0), F(-6, 25)),
        1: (F(-1, 4), F(0)), 2: (F(0), F(-6, 25)),
        3: (F(9, 100), F(0))}
    require(laurent_product(circle_p, circle_q) == expected_laurent,
            "LAURENT_SUPPORT", "full p-conjugate-q Laurent coefficient table differs")
    v = [p[0], p[1], q[0], q[1], c[0], c[1]]
    jv = [scale(p[1], F(-1)), p[0], scale(q[1], F(-1)), q[0], scale(c[1], F(-1)), c[0]]
    return p, q, c, [v, jv], circle_p, circle_q


def minors_of_curve(v):
    pairs = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    minors = [sub(mul(v[0][i], v[1][j]), mul(v[0][j], v[1][i])) for i, j in pairs]
    return pairs, minors


def coefficient_matrix(polynomials, degree):
    return [[coefficient(p, i) for p in polynomials] for i in range(degree + 1)]


def expected_kernel(pairs):
    def vector(terms):
        out = [F(0)] * 15
        for i, j, c in terms:
            if i > j:
                i, j, c = j, i, -c
            out[pairs.index((i, j))] += c
        return out
    out = []
    for j in range(3):
        for k in range(j + 1, 3):
            out.append(vector([(2*j, 2*k, F(1)), (2*j+1, 2*k+1, F(-1))]))
            out.append(vector([(2*j, 2*k+1, F(1)), (2*j+1, 2*k, F(1))]))
    out.append(vector([(0, 1, F(1)), (2, 3, F(1)), (4, 5, F(-1))]))
    return out


def hermitian_projection(vector, pairs):
    basis = []
    for i in range(6):
        x = [(F(0), F(0))] * 3
        x[i // 2] = (F(1), F(0)) if i % 2 == 0 else (F(0), F(1))
        basis.append(x)
    out = [[(F(0), F(0)) for _ in range(3)] for _ in range(3)]
    for weight, (i, j) in zip(vector, pairs):
        for a in range(3):
            for b in range(3):
                delta = gadd(gmul(basis[i][a], gconj(basis[j][b])),
                             gscale(gmul(basis[j][a], gconj(basis[i][b])), F(-1)))
                out[a][b] = gadd(out[a][b], gscale(gmul((F(0), F(1, 2)), delta), weight))
    return out


def fourier_functional(j):
    real = scale(mul(power((F(1), F(1)), j), power((F(-1), F(1)), 8-j)), F(1, 256))
    phase = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))][j % 4]
    coeffs = [gscale(phase, coefficient(real, k)) for k in range(9)]
    require(coeffs[4][1] == 0 and all(coeffs[4-k] == gconj(coeffs[4+k]) for k in range(1, 5)),
            "FOURIER_REALITY", "Cayley monomial is not coefficientwise real Laurent data")
    g1, g2, g3, g4 = coeffs[5], coeffs[6], coeffs[7], coeffs[8]
    b = gscale(g4, F(10, 3))
    c0 = gadd(gmul((F(1), F(3, 4)), b), gscale(gmul((F(0), F(1)), g3), F(-5, 2)))
    t = gadd(gadd(gscale(g2, F(-400, 3)), gscale(gmul((F(0), F(1)), b), F(160, 3))),
             gscale(gmul((F(-3), F(4)), c0), F(40, 3)))
    a0 = gdiv(t, (F(12), F(41)))
    z = gadd(gscale(g1, F(400)), gscale(c0, F(-120)))
    return F(13776)*z[0] + F(22300)*z[1] - F(106164)*a0[0] + F(4029152)*a0[1]


def cayley(poly, rho):
    out = ZERO
    for j, value in enumerate(poly):
        term = mul(power((F(1), F(1)), j), power((F(-1), F(1)), 4-j))
        out = add(out, scale(term, value * rho**j))
    return out


def reconstruct():
    p, q, c, raw, circle_p, circle_q = raw_curve()
    pairs, minors = minors_of_curve(raw)
    coeffs = coefficient_matrix(minors, 8)
    require(max(len(x)-1 for x in minors) == 8, "RAW_DEGREE", "raw curve minor degree is not eight")
    common = ZERO
    for x in minors:
        common = gcd(common, x)
    require(common == ONE, "RAW_MINOR_GCD", "raw minors have a nonconstant common factor")
    require(len(rref(coeffs)[1]) == 8 and len(rref(coeffs[:8])[1]) == 8,
            "RAW_COEFFICIENT_RANK", "full/first-eight raw coefficient rank differs from eight")
    k = expected_kernel(pairs)
    require(len(rref(k)[1]) == 7 and all(all(sum(a*b for a, b in zip(row, v)) == 0 for row in coeffs) for v in k),
            "RAW_KERNEL_IDENTITY", "anti-J plus full-rank Hermitian kernel does not annihilate raw coefficients")
    for i, row in enumerate(k):
        h = hermitian_projection(row, pairs)
        expected = [[(F(0), F(0)) for _ in range(3)] for _ in range(3)]
        if i == 6:
            for j, d in enumerate((1, 1, -1)):
                expected[j][j] = (F(d), F(0))
        require(h == expected, "HERMITIAN_KERNEL_PROJECTION", "raw kernel projection is not six zero directions plus diag(1,1,-1)")
    left = nullspace(transpose(coeffs), 9)
    require(len(left) == 1 and left[0][8] != 0, "RAW_SEPARATOR_EXISTENCE", "raw left kernel cannot separate z^8")
    separator = [x / left[0][8] for x in left[0]]
    products = [cpmul(c, cpconj(c))[0], cpmul(p, cpconj(p))[0]]
    for x, y in ((p, q), (p, c), (q, c)):
        product = cpmul(x, cpconj(y))
        products.extend(product)
    fm = coefficient_matrix(products, 8)
    det9 = rational_det([row + [F(i == 8)] for i, row in enumerate(fm)])
    require(det9 != 0, "HERMITIAN_DETERMINANT", "eight functions plus z^8 are not independent")
    alpha = fourier_functional(8)
    require(alpha > 1000000, "FOURIER_SEPARATOR_ALPHA", "explicit Fourier separator lower bound fails")
    fourier_separator = [fourier_functional(j) / alpha for j in range(9)]
    require(fourier_separator == separator, "SEPARATOR_REPRESENTATIONS", "raw coefficient and Fourier separators disagree")
    require(all(abs(x) < 122 for x in separator[:8]), "SEPARATOR_NORM_BOUND", "explicit separator bound fails")
    rho = F(1, 100000)
    radius_sum = sum(abs(separator[j])*math.comb(8, j) for j in range(8))
    require(rho * radius_sum < F(1, 2) and 122*255*rho < F(1, 2),
            "ROOT_DISK_BOUND", "explicit fixed radius is not strictly separated")
    transformed = [[cayley(x, rho) for x in row] for row in raw]
    transformed = [[row[i] for i in (4, 5, 0, 1, 2, 3)] for row in transformed]
    leading = [[coefficient(transformed[i][j], 4) for j in range(2)] for i in range(2)]
    lead_det = leading[0][0]*leading[1][1]-leading[0][1]*leading[1][0]
    require(lead_det == (1+rho*rho)**4 and lead_det > 0,
            "CAYLEY_LEADING_BLOCK", "real row-normalization determinant differs")
    inverse = [[leading[1][1]/lead_det, -leading[0][1]/lead_det],
               [-leading[1][0]/lead_det, leading[0][0]/lead_det]]
    transformed = pmatmul(constant_matrix(inverse), transformed)
    d = [row[:2] for row in transformed]
    nr = [row[2:] for row in transformed]
    top = [[coefficient(nr[i][j], 4) for j in range(4)] for i in range(2)]
    correction = pmatmul(d, constant_matrix(top))
    n = [[sub(nr[i][j], correction[i][j]) for j in range(4)] for i in range(2)]
    require(all(coefficient(d[i][j], 4) == F(i == j) for i in range(2) for j in range(2)) and
            all(len(x) <= 4 for row in n for x in row), "MONIC_CHART", "normalized D/N row degrees fail")
    common = ZERO
    for x in minors_of_curve([d[i]+n[i] for i in range(2)])[1]:
        common = gcd(common, x)
    require(common == ONE, "NORMALIZED_MINOR_GCD", "normalized row curve has a common minor factor")
    a = [[F(0) for _ in range(8)] for _ in range(8)]
    b = [[F(0) for _ in range(4)] for _ in range(8)]
    out = [[F(i == j) for j in range(8)] for i in range(2)]
    for block in range(4):
        for i in range(2):
            for j in range(2):
                a[2*block+i][j] = -coefficient(d[i][j], 3-block)
                if block < 3:
                    a[2*block+i][2*(block+1)+j] = F(i == j)
            for j in range(4):
                b[2*block+i][j] = coefficient(n[i][j], 3-block)
    return {"D": d, "N": n, "A": a, "B": b, "C": out, "rho": rho,
            "raw_left_separator": separator, "raw_kernel_basis": k,
            "determinant_9x9": det9, "raw_coefficients": coeffs,
            "circle_p": circle_p, "circle_q": circle_q,
            "radius_sum": radius_sum, "fourier_alpha": alpha}


def parse_fraction(value, where):
    require(isinstance(value, str) and len(value) <= 4096 and RAT.fullmatch(value) is not None,
            "INPUT_RATIONAL", where + " must be a canonical rational string")
    try:
        q = F(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CheckError("INPUT_RATIONAL", where + ": " + str(exc)) from exc
    require(str(q) == value, "INPUT_RATIONAL", where + " is not canonical")
    return q


def parse_matrix(value, rows, cols, where):
    require(isinstance(value, list) and len(value) == rows and
            all(isinstance(row, list) and len(row) == cols for row in value),
            "INPUT_SHAPE", where + " has wrong matrix shape")
    return [[parse_fraction(x, f"{where}[{i}][{j}]") for j, x in enumerate(row)] for i, row in enumerate(value)]


def parse_polynomials(value, rows, cols, degree, where):
    require(isinstance(value, list) and len(value) == rows and
            all(isinstance(row, list) and len(row) == cols for row in value),
            "INPUT_SHAPE", where + " has wrong polynomial-matrix shape")
    out = []
    for i, row in enumerate(value):
        line = []
        for j, poly in enumerate(row):
            require(isinstance(poly, list) and 1 <= len(poly) <= degree+1,
                    "INPUT_SHAPE", f"{where}[{i}][{j}] has wrong coefficient shape")
            line.append(norm(parse_fraction(x, f"{where}[{i}][{j}][{k}]") for k, x in enumerate(poly)))
        out.append(line)
    return out


def validate_payload(payload, expected):
    fields = {"D", "N", "A", "B", "C", "rho", "raw_left_separator", "raw_kernel_basis", "determinant_9x9"}
    require(isinstance(payload, dict) and set(payload) == fields,
            "INPUT_FIELDS", "input must contain exactly the nine declared witness fields")
    actual = {
        "D": parse_polynomials(payload["D"], 2, 2, 4, "D"),
        "N": parse_polynomials(payload["N"], 2, 4, 3, "N"),
        "A": parse_matrix(payload["A"], 8, 8, "A"),
        "B": parse_matrix(payload["B"], 8, 4, "B"),
        "C": parse_matrix(payload["C"], 2, 8, "C"),
        "rho": parse_fraction(payload["rho"], "rho"),
        "raw_kernel_basis": parse_matrix(payload["raw_kernel_basis"], 7, 15, "raw_kernel_basis"),
        "determinant_9x9": parse_fraction(payload["determinant_9x9"], "determinant_9x9")}
    require(isinstance(payload["raw_left_separator"], list) and len(payload["raw_left_separator"]) == 9,
            "INPUT_SHAPE", "raw_left_separator must have nine entries")
    actual["raw_left_separator"] = [parse_fraction(x, "raw_left_separator") for x in payload["raw_left_separator"]]
    for name in ("D", "N", "A", "B", "C", "rho", "determinant_9x9"):
        require(actual[name] == expected[name], "RECIPE_"+name.upper()+"_MISMATCH", name+" differs from independently reconstructed literal recipe")
    separator = actual["raw_left_separator"]
    require(separator[8] == 1 and all(sum(separator[i]*expected["raw_coefficients"][i][j] for i in range(9)) == 0 for j in range(15)),
            "RAW_SEPARATOR_ANNIHILATION", "supplied separator does not annihilate all literal raw minors with z^8 normalization")
    require(separator == expected["raw_left_separator"], "RAW_SEPARATOR_MISMATCH", "supplied raw separator differs from unique independently solved one")
    kernel = actual["raw_kernel_basis"]
    require(len(rref(kernel)[1]) == 7 and
            all(all(sum(a*b for a, b in zip(row, v)) == 0 for row in expected["raw_coefficients"]) for v in kernel),
            "RAW_KERNEL_SPAN", "supplied seven vectors are not a full raw coefficient kernel")
    require(len(rref(kernel+expected["raw_kernel_basis"])[1]) == 7,
            "RAW_KERNEL_SPAN", "supplied kernel is not anti-J plus diag(1,1,-1)")
    return actual


def verify_state_identities(actual):
    a, b, c, d, n = (actual[x] for x in ("A", "B", "C", "D", "N"))
    matrix = [[norm((-a[i][j], F(i == j))) for j in range(8)] for i in range(8)]
    characteristic = polynomial_det(matrix)
    determinant_d = polynomial_det(d)
    require(characteristic == determinant_d and len(characteristic) == 9 and characteristic[-1] == 1,
            "STATE_CHARACTERISTIC_IDENTITY", "actual det(sI-A) is not det D as an exact monic degree-eight polynomial")
    # Direct cofactors, independently of any Faddeev recursion.
    top_adjugate = []
    for i in range(2):
        row = []
        for j in range(8):
            minor = [[matrix[r][k] for k in range(8) if k != i] for r in range(8) if r != j]
            row.append(scale(polynomial_det(minor), F(-1 if (i+j) % 2 else 1)))
        top_adjugate.append(row)
    numerator = pmatmul(top_adjugate, constant_matrix(b))
    require(pmatmul(d, numerator) == [[mul(x, characteristic) for x in row] for row in n],
            "UNIVERSAL_TRANSFER_IDENTITY", "D*C*adj(sI-A)*B differs coefficientwise from N*det(sI-A)")
    # The actual C is [I2,0]; feedback changes only columns zero and one.
    require(c == [[F(i == j) for j in range(8)] for i in range(2)],
            "OUTPUT_CHART", "universal gain expansion requires the verified canonical output chart")
    def replaced(first=None, second=None):
        m = [list(row) for row in matrix]
        if first is not None:
            for i in range(8):
                m[i][0] = (b[i][first],)
        if second is not None:
            for i in range(8):
                m[i][1] = (b[i][second],)
        return polynomial_det(m)
    def det_columns(x, y):
        return sub(mul(x[0], y[1]), mul(x[1], y[0]))
    columns_n = [[n[i][j] for i in range(2)] for j in range(4)]
    columns_d = [[d[i][j] for i in range(2)] for j in range(2)]
    for r in range(4):
        require(replaced(first=r) == det_columns(columns_n[r], columns_d[1]),
                "UNIVERSAL_GAIN_LINEAR", "first gain-column coefficient differs")
        require(replaced(second=r) == det_columns(columns_d[0], columns_n[r]),
                "UNIVERSAL_GAIN_LINEAR", "second gain-column coefficient differs")
        for s in range(4):
            require(replaced(first=r, second=s) == det_columns(columns_n[r], columns_n[s]),
                    "UNIVERSAL_GAIN_QUADRATIC", "bilinear gain coefficient differs")
    # Multilinearity in the two modified columns proves the full eight-variable identity.
    identity = [[F(i == j) for j in range(8)] for i in range(8)]
    p = identity
    observations = []
    controls = []
    for _ in range(8):
        observations.extend(matmul(c, p))
        controls.append(matmul(p, b))
        p = matmul(p, a)
    controllability = [[x for block in controls for x in block[i]] for i in range(8)]
    require(len(rref(observations)[1]) == 8, "OBSERVABILITY_RANK", "actual plant is not observable")
    require(len(rref(controllability)[1]) == 8, "CONTROLLABILITY_RANK", "actual plant is not controllable")
    return characteristic


def read_pinned(path, expected, cap, code):
    with Path(path).open("rb") as stream:
        data = stream.read(cap+1)
    require(len(data) <= cap, "INPUT_SIZE", str(path)+" exceeds byte ceiling")
    digest = hashlib.sha256(data).hexdigest()
    require(digest == expected, code, str(path)+" bytes do not match the admitted pin")
    return data


def strict_object(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, "INPUT_DUPLICATE_KEY", "duplicate JSON key: "+key)
        out[key] = value
    return out


def reject_float(_value):
    raise CheckError("INPUT_NUMBER_TYPE", "JSON floats/nonfinite constants are forbidden")


def expected_rejection(code, operation):
    try:
        operation()
    except CheckError as exc:
        require(exc.code == code, "CONTROL_WRONG_REASON", "expected "+code+", received "+exc.code)
        return code
    raise CheckError("CONTROL_SURVIVED", "mutation was not rejected: "+code)


def main():
    global END, MEMORY_BYTES
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--input-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--deadline-seconds", type=int, default=900)
    parser.add_argument("--memory-bytes", type=int, default=1024*1024*1024)
    parser.add_argument("--max-output-bytes", type=int, default=2*1024*1024)
    args = parser.parse_args()
    started = time.monotonic()
    try:
        require(re.fullmatch(r"[0-9a-f]{64}", args.input_sha256) is not None,
                "INPUT_PIN_FORMAT", "input SHA256 must be sixty-four lowercase hexadecimal digits")
        require(1 <= args.deadline_seconds <= 3600 and 64*1024*1024 <= args.memory_bytes <= 8*1024*1024*1024 and
                1024 <= args.max_output_bytes <= 2*1024*1024,
                "RESOURCE_ARGUMENT", "resource settings outside frozen checker limits")
        END = started + args.deadline_seconds
        MEMORY_BYTES = args.memory_bytes
        signal.signal(signal.SIGTERM, interrupt_handler)
        signal.signal(signal.SIGINT, interrupt_handler)
        output = Path(args.output).resolve()
        require(output.is_relative_to(Path(__file__).resolve().parent), "OUTPUT_SCOPE", "output must remain inside the PH owner slot")
        require(not output.exists(), "OUTPUT_EXISTS", "refusing to overwrite any existing output")
        read_pinned(PROOF, PROOF_PIN, MAX_SOURCE, "PROOF_PIN_MISMATCH")
        read_pinned(RADIUS_PROOF, RADIUS_PIN, MAX_SOURCE, "RADIUS_PIN_MISMATCH")
        data = read_pinned(args.input, args.input_sha256, MAX_INPUT, "INPUT_SHA256_MISMATCH")
        payload = json.loads(data.decode("utf-8"), object_pairs_hook=strict_object,
                             parse_float=reject_float, parse_constant=reject_float)
        expected = reconstruct()
        actual = validate_payload(payload, expected)
        characteristic = verify_state_identities(actual)
        mutation_a = copy.deepcopy(payload)
        mutation_a["A"][0][0] = str(actual["A"][0][0]+1)
        mutation_ell = copy.deepcopy(payload)
        mutation_ell["raw_left_separator"][0] = str(actual["raw_left_separator"][0]+1)
        mutant_p = list(expected["circle_p"][0])
        mutant_p[4] += 1
        controls = [
            expected_rejection("RECIPE_A_MISMATCH", lambda: validate_payload(mutation_a, expected)),
            expected_rejection("RAW_SEPARATOR_ANNIHILATION", lambda: validate_payload(mutation_ell, expected)),
            expected_rejection("CIRCLE_NORM_IDENTITY", lambda: circle_norm((norm(mutant_p), expected["circle_p"][1]), expected["circle_q"])),
            expected_rejection("INPUT_SHA256_MISMATCH", lambda: read_pinned(args.input, "0"*64, MAX_INPUT, "INPUT_SHA256_MISMATCH"))]
        tick()
        native, rss_bytes, rss_units = peak_rss()
        receipt = {
            "status": "VALID_FIXED_EXACT_WITNESS",
            "scope": "finite exact algebra only; full real-Grassmann/open-ordinary-plant proof and priority are separate",
            "input_sha256": args.input_sha256,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "proof_sha256": PROOF_PIN, "radius_proof_sha256": RADIUS_PIN,
            "raw_minor_count": 15, "raw_coefficient_rank": 8, "raw_kernel_dimension": 7,
            "raw_real_simple_exclusion": "anti-J kernel projection zero plus full-rank diag(1,1,-1), at the separately reconstructed elementary Hermitian-rank lemma",
            "determinant_9x9": str(expected["determinant_9x9"]),
            "rho": str(expected["rho"]), "rho_separator_sum": str(expected["rho"]*expected["radius_sum"]),
            "fourier_alpha": str(expected["fourier_alpha"]),
            "characteristic_ascending": [str(x) for x in characteristic],
            "universal_transfer": "full polynomial adjugate identity; direct 7x7 cofactors",
            "universal_all_gain_identity": "all constant/linear/bilinear coefficients in the two modified columns, covering all eight gain variables",
            "controllability_rank": 8, "observability_rank": 8,
            "negative_controls_intended_reasons": controls,
            "elapsed_seconds": time.monotonic()-started,
            "peak_rss_native": native, "peak_rss_native_units": rss_units,
            "peak_rss_bytes": rss_bytes, "rss_enforcement": "cooperative peak check, not OS allocation prevention",
            "formal_kernel_verification": "NOT_PERFORMED", "novelty": "NOT_CERTIFIED"}
        encoded = (json.dumps(receipt, indent=2, sort_keys=True)+"\n").encode()
        require(len(encoded) <= args.max_output_bytes, "OUTPUT_SIZE", "receipt exceeds frozen output ceiling")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        print(json.dumps({"status": receipt["status"], "output": str(output), "input_sha256": args.input_sha256}))
        return 0
    except CheckError as exc:
        print(json.dumps({"status": "INCOMPLETE" if exc.code.startswith("INCOMPLETE") else "INVALID",
                          "code": exc.code, "detail": exc.detail,
                          "elapsed_seconds": time.monotonic()-started}), file=sys.stderr)
        return 2 if exc.code.startswith("INCOMPLETE") else 1
    except Exception as exc:
        print(json.dumps({"status": "INTERNAL_ERROR", "type": type(exc).__name__, "detail": str(exc),
                          "elapsed_seconds": time.monotonic()-started}), file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
