"""Independent first-quantized check of the CFP engine (conventions, sqrt(N), CG order).

For small N, every state produced by the polynomial engine is expanded into an explicit
symmetric tensor in (C^(2f+1))^(tensor N) with orthonormal one-particle basis e_m, and the CFP
is recomputed from its definition
    cfp = < Psi_N(L, M=L) | sum_{m,M'} <f m; L' M' | L L> Psi_(N-1)(L', M') (x) e_m(particle N) >
using sympy's exact Clebsch-Gordan coefficients.  The result (with sign) must equal the
engine's fpc_core.SpinBosons.cfp_sq_sign.
Run: $PY code/verify_first_quantized.py
"""
import itertools
from math import factorial

import sympy as sp
from sympy.physics.wigner import clebsch_gordan

from check_seniority_factorization import harmonic_states
from fpc_core import SpinBosons


def to_tensor(B, poly, N):
    """Polynomial in z_m (unnormalised orbitals eps_m) -> normalised symmetric tensor dict."""
    f = B.f
    out = {}
    for a, c in poly.items():
        # z^a |0> = prod_m (sqrt(w_m) a+_m)^(a_m) |0> = prod_m w_m^(a_m/2) sqrt(a_m!) |a>
        amp = sp.Rational(int(c.p), int(c.q))
        for am, wm in zip(a, B.w):
            amp *= sp.sqrt(sp.Rational(int(wm.p), int(wm.q))) ** am * sp.sqrt(factorial(am))
        # |a> = sqrt(prod a_m! / N!) * sum over distinct arrangements
        pref = sp.sqrt(sp.Rational(sp.prod([factorial(x) for x in a]), factorial(N)))
        seq = [m - f for m, am in enumerate(a) for _ in range(am)]
        for arr in set(itertools.permutations(seq)):
            out[arr] = out.get(arr, 0) + amp * pref
    nrm = sp.sqrt(sum(sp.nsimplify(x) ** 2 for x in out.values()))
    return {k: sp.nsimplify(x / nrm) for k, x in out.items()}


def lowered(B, poly, L):
    """[(M, polynomial)] for M = L, L-1, ..., -L via S-."""
    out = [(L, poly)]
    p = poly
    for M in range(L - 1, -L - 1, -1):
        p = B.sminus(p)
        out.append((M, p))
    return out


def cfp_first_quantized(B, parent, N, L, daughter, Lp):
    f = B.f
    Psi = to_tensor(B, parent, N)
    acc = 0
    for Mp, dpoly in lowered(B, daughter, Lp):
        m = L - Mp
        if abs(m) > f:
            continue
        cg = clebsch_gordan(f, Lp, L, m, Mp, L)
        if cg == 0:
            continue
        Dt = to_tensor(B, dpoly, N - 1)
        for key, x in Dt.items():
            y = Psi.get(key + (m,))
            if y is not None:
                acc += cg * x * y
    return sp.nsimplify(sp.radsimp(acc))


def main():
    checks = 0
    for f, Nmax in ((1, 5), (2, 4), (3, 3)):
        B = SpinBosons(f)
        H = harmonic_states(B, Nmax)
        states = {}
        for (v, L), hs in H.items():
            for al, h in enumerate(hs):
                p, N = h, v
                while N <= Nmax:
                    states[(N, v, L, al)] = p
                    p = B.pair_cre(p)
                    N += 2
        for (N, v, L, al), p in states.items():
            if N < 2:
                continue
            for (N2, v2, L2, al2), q in states.items():
                if N2 != N - 1 or not (abs(L - L2) <= f <= L + L2):
                    continue
                sq, sg = B.cfp_sq_sign(p, N, L, q, L2)
                c = cfp_first_quantized(B, p, N, L, q, L2)
                ref = sg * sp.sqrt(sp.Rational(int(sq.p), int(sq.q)))
                assert sp.simplify(c - ref) == 0, (f, N, v, L, al, v2, L2, al2, c, ref)
                checks += 1
    print(f"first-quantized check OK: {checks} CFPs (f=1 N<=5, f=2 N<=4, f=3 N<=3) agree with the engine,"
          f" including signs")


if __name__ == "__main__":
    main()
