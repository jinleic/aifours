"""Claim C5: single-function (F = G) reading of the conjecture fails for Sawada-Kotera-type P.

P = D_t + c1 D_x + c3 D_x^3 + c5 D_x^5 (odd), Q = D_x, R = D_y.  With F = G = f the first equation
P(D) f.f = 0 holds identically (P odd), so (1) reduces to D_x P f.f = 0 and (2) to D_y P f.f = 0.

Computes, in the rational-function field Q(k_i, l_i, c1, c3, c5):
  (a) Hirota's three-soliton residuals of D_x P f.f = 0  -> expected: all zero (identity);
  (b) the same for D_y P f.f = 0                      -> expected: nonzero, proportional to c5;
  (c) the factorisation of the obstruction and a comparison with constraint (16) of
      Wang-Yang-Tang-Chen (Nonlinear Dyn. 2024) for c1 = c3 = 0;
  (d) an exact rational witness for P = D_t + D_x^5 (pure Sawada-Kotera).
Run:  python single_function_3ss.py   (deterministic; about 9 minutes, dominated by one sympy factorisation)
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.fields import field

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hirota_ns as H  # noqa: E402

Dx, Dy, Dt = H.DX, H.DY, H.DT
OUT = Path(__file__).resolve().parent.parent / "results"


def symbolic_residuals(with_y: bool):
    names = ["k1", "k2", "k3", "l1", "l2", "l3", "c1", "c3", "c5"]
    K, *gens = field(",".join(names), QQ)
    g = dict(zip(names, gens))
    c1, c3, c5 = g["c1"], g["c3"], g["c5"]
    # bilinear symbol with symbolic coefficients, built directly as {(a, b, c): coeff}
    P = {(0, 0, 1): K.one, (1, 0, 0): c1, (3, 0, 0): c3, (5, 0, 0): c5}
    M = {(0, 1, 0): K.one} if with_y else {(1, 0, 0): K.one}
    B = H.bmul(M, P)
    waves = []
    for i in (1, 2, 3):
        k = g[f"k{i}"]
        l = g[f"l{i}"] if with_y else K.zero
        w = -(c1 * k + c3 * k**3 + c5 * k**5)
        waves.append((k, l, w))
    f, A = H.hirota_product_solution(B, waves)
    res = H.residuals([B], waves, f, f)
    return K, g, res, A


def main():
    OUT.mkdir(exist_ok=True)
    report = {}
    t0 = time.time()
    _, _, res_x, _ = symbolic_residuals(with_y=False)
    report["DxP_nonzero_coefficients"] = len(res_x)
    print(f"(a) D_x(D_t+c1D_x+c3D_x^3+c5D_x^5) f.f: nonzero three-soliton coefficients = {len(res_x)}"
          f"  [{time.time() - t0:.1f}s]")

    t0 = time.time()
    K, g, res_y, A = symbolic_residuals(with_y=True)
    print(f"(b) D_y(D_t+c1D_x+c3D_x^3+c5D_x^5) f.f: nonzero coefficients at n = {sorted(res_y)}"
          f"  [{time.time() - t0:.1f}s]")
    report["DyP_nonzero_n"] = [list(n) for n in sorted(res_y)]
    # all nonzero coefficients sit at n = (1,1,1) (Hirota's three-soliton condition)
    val = res_y[(1, 1, 1)][0]
    num = sp.factor(sp.sympify(str(val.numer.as_expr())))
    den = sp.factor(sp.sympify(str(val.denom.as_expr())))
    print("    numerator of the (1,1,1) coefficient, factored:")
    print("     ", num)
    report["DyP_residual_111_numerator_factored"] = str(num)
    report["DyP_residual_111_denominator_factored"] = str(den)

    k1, k2, k3, l1, l2, l3, c1, c3, c5 = sp.symbols("k1 k2 k3 l1 l2 l3 c1 c3 c5")
    # Wang-Yang-Tang-Chen 2024, eq. (16) (wave-number constraint for the 2DSK three-soliton solution)
    wang16 = l2 * l3 * (l2**2 - l3**2) * k1**3 - l1 * l3 * (l1**2 - l3**2) * k2**3 + l1 * l2 * (l1**2 - l2**2) * k3**3
    numer_poly = sp.Poly(sp.expand(num), k1, k2, k3, l1, l2, l3, c1, c3, c5)
    pure = sp.factor(sp.expand(num).subs({c1: 0, c3: 0}))
    ratio = sp.cancel(sp.expand(num).subs({c1: 0, c3: 0}) / wang16)
    print("    c1 = c3 = 0 numerator / Wang et al. (16) constraint =", sp.factor(ratio))
    report["ratio_to_wang2024_eq16_for_c1_c3_zero"] = str(sp.factor(ratio))
    # c5-dependence: the numerator vanishes identically when c5 = 0
    at_c5_zero = sp.expand(num).subs(c5, 0)
    print("    numerator at c5 = 0:", at_c5_zero)
    report["numerator_at_c5_zero"] = str(at_c5_zero)
    report["numerator_total_degree"] = numer_poly.total_degree()

    # (d) exact rational witness for pure Sawada-Kotera P = D_t + D_x^5
    wit = {"k": [Fr(1), Fr(2), Fr(3)], "l": [Fr(1), Fr(3), Fr(7)]}
    B = H.bpoly(Dy * (Dt + Dx**5))
    waves = [(k, l, -k**5) for k, l in zip(wit["k"], wit["l"])]
    f, _ = H.hirota_product_solution(B, waves)
    r = H.residuals([B], waves, f, f)
    print("(d) witness k=(1,2,3), l=(1,3,7): nonzero coefficients:",
          {str(n): str(v[0]) for n, v in r.items()})
    report["witness"] = {"k": [str(x) for x in wit["k"]], "l": [str(x) for x in wit["l"]],
                         "nonzero_coefficients": {str(n): str(v[0]) for n, v in r.items()}}
    wang_val = (wang16.subs({k1: 1, k2: 2, k3: 3, l1: 1, l2: 3, l3: 7}))
    print("    Wang et al. (16) at the witness:", wang_val)
    report["wang16_at_witness"] = str(wang_val)
    # control: the same witness for D_x(D_t + D_x^5) (Sawada-Kotera, l irrelevant) gives zero residual
    Bx = H.bpoly(Dx * (Dt + Dx**5))
    wx = [(k, Fr(0), -k**5) for k in wit["k"]]
    fx, _ = H.hirota_product_solution(Bx, wx)
    rx = H.residuals([Bx], wx, fx, fx)
    print("    control D_x(D_t+D_x^5) at k=(1,2,3): nonzero coefficients =", len(rx))
    report["control_SK_nonzero"] = len(rx)
    (OUT / "single_function_3ss.json").write_text(json.dumps(report, indent=2))
    print("wrote", OUT / "single_function_3ss.json")


if __name__ == "__main__":
    main()
