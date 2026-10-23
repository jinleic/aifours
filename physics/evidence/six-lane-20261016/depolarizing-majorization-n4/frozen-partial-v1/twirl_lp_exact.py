"""Exact rational version of twirl_ppt_lp.py (closed-form LP data, sympy exact simplex).

Per site the twirled variable lives in span{Phi+, 1-Phi+} (commutant of conj(U) (x) U). Closed forms:
  depolarizing N = D_p:  Tr(J_N Phi+) = 2 - 3p/2,  Tr(J_N (1-Phi+)) = 3p/2      (J_N = 2(1-p) Phi+ + (p/2) 1)
  identity:              Tr(J Phi+) = 2,           Tr(J (1-Phi+)) = 0            (J = 2 Phi+)
  X -> Tr(X) 1:          Tr(J Phi+) = 1,           Tr(J (1-Phi+)) = 3            (J = 1 (x) 1)
  Tr(Phi+) = 1, Tr(1-Phi+) = 3; Tr_sigma Phi+ = 1/2, Tr_sigma(1-Phi+) = 3/2;
  partial transpose: Phi+ -> F/2 (eigs +1/2 sym, -1/2 anti), 1-Phi+ -> 1-F/2 (eigs 1/2 sym, 3/2 anti).
LP: max sum_S obj_S c_S  s.t. 0 <= c_S <= 1/16, sum_S c_S 3^{4-|S|} = k, sum_S c_S (1/2)^{|S|} (3/2)^{4-|S|} <= 1,
    0 <= sum_S c_S prod_l g(l in S, tau_l) <= 1/16 for all tau in {sym, anti}^4.
Usage: python twirl_lp_exact.py dep <p as fraction> | U <s>
Prints exact LP optimum and exact target K_k for every k = 1..15.
"""
import itertools
import sys
from math import comb

import sympy as sp
from sympy.solvers.simplex import lpmax

n = 4
subsets = [S for r in range(n + 1) for S in itertools.combinations(range(n), r)]
half, three_half = sp.Rational(1, 2), sp.Rational(3, 2)


def g(inS, tau):
    return (half if tau == 0 else -half) if inS else (half if tau == 0 else three_half)


def lp_value(obj, k):
    c = sp.symbols("c0:16")
    cons = []
    for i in range(16):
        cons += [c[i] >= 0, c[i] <= sp.Rational(1, 16)]
    cons.append(sp.Eq(sum(c[i] * 3 ** (n - len(S)) for i, S in enumerate(subsets)), k))
    cons.append(sum(c[i] * half ** len(S) * three_half ** (n - len(S)) for i, S in enumerate(subsets)) <= 1)
    for tau in itertools.product((0, 1), repeat=n):
        e = sum(c[i] * sp.prod([g(l in S, tau[l]) for l in range(n)]) for i, S in enumerate(subsets))
        cons += [e >= 0, e <= sp.Rational(1, 16)]
    val, sol = lpmax(sum(obj[i] * c[i] for i in range(16)), cons)
    return val, sol


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "dep":
        p = sp.Rational(sys.argv[2])
        a_in, a_out = 2 - 3 * p / 2, 3 * p / 2
        obj = [a_in ** len(S) * a_out ** (n - len(S)) for S in subsets]
        eig = sorted([(1 - p / 2) ** (n - w) * (p / 2) ** w for w in range(n + 1) for _ in range(comb(n, w))],
                     reverse=True)
    else:
        s = int(sys.argv[2])
        obj = [comb(len(S), s) * 2 ** s * 3 ** (n - len(S)) for S in subsets]
        eig = sorted([comb(z, s) for z in range(n + 1) for _ in range(comb(n, z))], reverse=True)
    ky = [sum(eig[:k]) for k in range(1, 17)]
    for k in range(1, 16):
        val, _ = lp_value(obj, k)
        print(f"k={k:2d} LP_exact={val} target={ky[k-1]} LP-target={sp.nsimplify(val - ky[k-1])} "
              f"{'TIGHT' if val == ky[k-1] else ('LOOSE' if val > ky[k-1] else 'BELOW?')}", flush=True)
