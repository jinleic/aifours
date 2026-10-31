#!/usr/bin/env python3
"""Exact rational algebra for the zero-lag literal-gain candidate.

Checks a fixed degree-six, tangent-linear upper profile for C=131/100,
and brackets the positive root of the displayed entire even function.
It does NOT check the Ito, optional-stopping or physical-input limit proofs.
Standard library only. No floating-point arithmetic occurs.
"""
from fractions import Fraction as F
from math import comb


def trim(a):
    a = [F(x) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(*polys):
    out = [F(0)] * max(map(len, polys))
    for a in polys:
        for i, v in enumerate(a):
            out[i] += v
    return trim(out)


def scale(a, c):
    return trim([v * c for v in a])


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return trim(out)


def power(a, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, a)
    return out


def at(a, x):
    out = F(0)
    for v in reversed(a):
        out = out * x + v
    return out


def derivative(a):
    return trim([i * v for i, v in enumerate(a)][1:] or [0])


def bernstein(a, left, right):
    """Exact degree-n Bernstein coefficients of a(left+(right-left)u)."""
    n = len(a) - 1
    ordinary = [
        sum((a[i] * comb(i, j) * left ** (i - j)
             * (right - left) ** j for i in range(j, n + 1)), F(0))
        for j in range(n + 1)
    ]
    return [
        sum((ordinary[j] * F(comb(k, j), comb(n, j))
             for j in range(k + 1)), F(0))
        for k in range(n + 1)
    ]


def check_profile():
    c, C, b = F(107, 200), F(131, 100), F(3, 2)
    # Polynomials in y^2=t, with phi'(y)=y*d(t).
    p = [C - c, c / 2, c / 24, c / 240]
    d = [c, c / 6, c / 40]
    h = [C, F(0), F(0), -c / 48]
    q2 = mul([0, 1], power(d, 2))
    # Direct coefficient check: H=phi''-y phi'+phi.
    phi_y = [p[0], 0, p[1], 0, p[2], 0, p[3]]
    phi_dy = derivative(phi_y)
    phi_ddy = derivative(phi_dy)
    direct_h = add(phi_ddy, scale(mul([0, 1], phi_dy), -1), phi_y)
    if direct_h != [h[0], 0, 0, 0, 0, 0, h[3]]:
        raise AssertionError("H coefficient identity failed")
    # Global phi(y)-|y| positivity on the polynomial piece, by phi''>=c.
    a = F(27, 20)
    gap_a = at(p, a * a) - a
    slope_a = a * at(d, a * a) - 1
    margin = gap_a - slope_a ** 2 / (2 * c)
    if margin <= F(1, 20000):
        raise AssertionError("strong-convexity profile margin failed")
    # Tangent-linear continuation for |y|>=b.
    value_b = at(p, b * b)
    slope_b = b * at(d, b * b)
    intercept_b = value_b - b * slope_b
    if not (slope_b > 1 and value_b > b and intercept_b < 0
            and slope_b ** 2 < C * value_b):
        raise AssertionError("tangent-linear tail inequalities failed")
    # Case 1, t in [0,36/25]: H>=2G, so sup_s sqrt(s)(H+(1-s)G)=H<=C.
    cut = F(36, 25)
    r = add(mul(h, p), scale(q2, -2))
    br = bernstein(r, F(0), cut)
    if min(br) <= 0 or at(h, b * b) <= 0:
        raise AssertionError("first profile interval failed")
    # Case 2: sufficient unconditional cubic inequality
    # 4(H+G)^3 <= 27 C^2 G on [36/25,9/4].
    j = add(scale(mul(power(p, 2), q2), 27 * C ** 2),
            scale(power(add(mul(h, p), q2), 3), -4))
    bj = bernstein(j, cut, b * b)
    if min(bj) <= 2:
        raise AssertionError("second profile interval failed")
    # With Q_epsilon=I+R k^2+epsilon the initial potential is nonpositive.
    if 1 + p[0] ** 2 >= C ** 2:
        raise AssertionError("initial regularized potential failed")
    print("PROFILE PASS: C=131/100; phi''>=107/200 on the polynomial piece")
    print("phi(y)-abs(y) > 1/20000 on that piece; exact margin:", margin)
    print("tangent slope:", slope_b, "intercept:", intercept_b)
    print("R Bernstein coefficients:", len(br), "all strictly positive")
    print("min R Bernstein coefficient:", min(br))
    print("J Bernstein coefficients:", len(bj), "all > 2")
    print("tail G<C and regularized initial value <0: PASS")


def harmonic_bounds(x, n=24):
    """Bracket h(x)=1-sum_{k>=1} x^(2k)/(2^k k!(2k-1))."""
    term = x * x / 2
    total = F(0)
    for k in range(1, n + 1):
        total += term
        term *= x * x * (2 * k - 1) / (2 * (k + 1) * (2 * k + 1))
    # term is now the first omitted term. Every subsequent ratio is <=r.
    r = x * x / (2 * (n + 2))
    if not 0 < r < 1:
        raise AssertionError("geometric remainder ratio failed")
    return 1 - total - term / (1 - r), 1 - total


def check_root():
    lo, hi = F(32673, 25000), F(130693, 100000)
    hlo, _ = harmonic_bounds(lo)
    _, hhi = harmonic_bounds(hi)
    if not (hlo > F(17, 1000000) and hhi < -F(4, 10000000)):
        raise AssertionError("entire-function root bracket failed")
    print("ROOT PASS: 32673/25000 < r < 130693/100000")
    print("h(32673/25000)>17/1000000; h(130693/100000)<-4/10000000")
    print("LIMIT: exact finite algebra only, not a stochastic proof or independent review")


def main():
    check_profile()
    check_root()


if __name__ == "__main__":
    main()
