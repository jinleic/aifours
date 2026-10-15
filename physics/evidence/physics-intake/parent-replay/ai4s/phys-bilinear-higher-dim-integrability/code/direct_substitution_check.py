"""Independent check of claim C5 by direct differentiation (does not use hirota_ns.py).

The three-soliton candidate f = sum_S prod_{i in S} c_i e^{eta_i} prod_{i<j in S} A_ij is built with the
phase factors printed in the literature:
  2DSK  D_y(D_t + D_x^5) f.f = 0  : A_ij = (ki-kj)(li-lj)(ki^2-ki kj+kj^2) / ((ki+kj)(li+lj)(ki^2+ki kj+kj^2))
        [Wang-Yang-Tang-Chen, Nonlinear Dyn. 2024, eq. (15)]
  SK    D_x(D_t + D_x^5) f.f = 0  : A_ij = (ki-kj)^2(ki^2-ki kj+kj^2) / ((ki+kj)^2(ki^2+ki kj+kj^2))
The Hirota derivative is evaluated from its definition B(d_x - d_x', d_y - d_y', d_t - d_t') f(x,y,t) f(x',y',t')
by sympy differentiation, then restricted to x = x', ... and to the origin, with the phase constants c_i kept
symbolic.  The result is the polynomial sum_n C(n) c^n whose coefficients are the exponential coefficients
C(n) of the residual; all arithmetic is exact.
Run: python direct_substitution_check.py
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

x, y, t, xp, yp, tp = sp.symbols("x y t xp yp tp")
c = sp.symbols("c1:4")
OUT = Path(__file__).resolve().parent.parent / "results"


def three_soliton(ks, ls, ws, Aij, X, Y, T):
    f = 0
    for S in itertools.product((0, 1), repeat=3):
        term = 1
        for i in range(3):
            if S[i]:
                term *= c[i] * sp.exp(ks[i] * X + ls[i] * Y + ws[i] * T)
        for i in range(3):
            for j in range(i + 1, 3):
                if S[i] and S[j]:
                    term *= Aij[(i, j)]
        f += term
    return f


def hirota(op_terms, f1, f2):
    """op_terms: list of (coeff, (a, b, cc)) meaning coeff * Dx^a Dy^b Dt^cc."""
    total = 0
    for co, (a, b, cc) in op_terms:
        # (d_x - d_x')^a (d_y - d_y')^b (d_t - d_t')^cc applied to f1(x,y,t) f2(x',y',t')
        for i in range(a + 1):
            for j in range(b + 1):
                for m in range(cc + 1):
                    sgn = (-1) ** ((a - i) + (b - j) + (cc - m))
                    coef = sp.binomial(a, i) * sp.binomial(b, j) * sp.binomial(cc, m) * sgn
                    d1 = f1
                    if i:
                        d1 = sp.diff(d1, x, i)
                    if j:
                        d1 = sp.diff(d1, y, j)
                    if m:
                        d1 = sp.diff(d1, t, m)
                    d2 = f2
                    if a - i:
                        d2 = sp.diff(d2, xp, a - i)
                    if b - j:
                        d2 = sp.diff(d2, yp, b - j)
                    if cc - m:
                        d2 = sp.diff(d2, tp, cc - m)
                    total += co * coef * d1 * d2
    return total


def residual_polynomial(op_terms, ks, ls, ws, Aij):
    f1 = three_soliton(ks, ls, ws, Aij, x, y, t)
    f2 = three_soliton(ks, ls, ws, Aij, xp, yp, tp)
    expr = hirota(op_terms, f1, f2)
    expr = expr.subs({xp: 0, yp: 0, tp: 0, x: 0, y: 0, t: 0})
    return sp.Poly(sp.expand(expr), *c)


def main():
    OUT.mkdir(exist_ok=True)
    ks = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
    ls = [sp.Integer(1), sp.Integer(3), sp.Integer(7)]
    ws = [-k**5 for k in ks]
    A2 = {}
    A1 = {}
    for i in range(3):
        for j in range(i + 1, 3):
            ki, kj, li, lj = ks[i], ks[j], ls[i], ls[j]
            A2[(i, j)] = ((ki - kj) * (li - lj) * (ki**2 - ki * kj + kj**2)
                          / ((ki + kj) * (li + lj) * (ki**2 + ki * kj + kj**2)))
            A1[(i, j)] = ((ki - kj) ** 2 * (ki**2 - ki * kj + kj**2)
                          / ((ki + kj) ** 2 * (ki**2 + ki * kj + kj**2)))
    # D_y (D_t + D_x^5) = Dy Dt + Dx^5 Dy ;  D_x (D_t + D_x^5) = Dx Dt + Dx^6
    op_2dsk = [(1, (0, 1, 1)), (1, (5, 1, 0))]
    op_sk = [(1, (1, 0, 1)), (1, (6, 0, 0))]
    p2 = residual_polynomial(op_2dsk, ks, ls, ws, A2)
    p1 = residual_polynomial(op_sk, ks, [0, 0, 0], ws, A1)
    nz2 = {str(m): str(v) for m, v in zip(p2.monoms(), p2.coeffs()) if v != 0}
    nz1 = {str(m): str(v) for m, v in zip(p1.monoms(), p1.coeffs()) if v != 0}
    print("2DSK D_y(D_t+D_x^5) f.f, k=(1,2,3), l=(1,3,7): nonzero exponential coefficients:", nz2)
    print("SK   D_x(D_t+D_x^5) f.f, k=(1,2,3)          : nonzero exponential coefficients:", nz1)
    (OUT / "direct_substitution_check.json").write_text(json.dumps(
        {"2DSK_nonzero_coefficients": nz2, "SK_nonzero_coefficients": nz1}, indent=2))


if __name__ == "__main__":
    main()
