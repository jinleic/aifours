"""Claim C7: a discrete extra dimension, R(S) = sinh(D_n), in the class P = D_t + p(D_x).

System (2d):  P(D_x, D_t) F.G = 0,   sinh(D_n) P(D_x, D_t) F.G = 0,   F, G functions of (x, n, t), n in Z.
On exp(eta) with eta = k x + nu n + w t the multiplier is sinh(nu_A - nu_C) = (Z_A/Z_C - Z_C/Z_A)/2,
Z_A = prod_{i in A} z_i, z_i = exp(nu_i).  Checked:
  symbolic N = 3 : p = c1 k + c3 k^3 (two amplitudes) and p = c1 k + c2 k^2 + c3 k^3 (all F/G patterns),
                   identity in Q(k_i, z_i, amplitudes, c_j);
  exact points   : p = k^4, k^5, k^5 + k^2 fail (fixed rational configurations).
Run: python discrete_variant.py
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from sympy import QQ
from sympy.polys.fields import field

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hirota_ns as H  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "results"


def system(waves, P, z, one):
    kap = H._kappa_table(waves)
    N = len(waves)
    Z = [one] * (1 << N)
    for S in range(1, 1 << N):
        v = one
        for i in range(N):
            if S >> i & 1:
                v = v * z[i]
        Z[S] = v

    def B1(A, C):
        return H.beval(P, H._vec_sub(kap[A], kap[C]))

    def B2(A, C):
        return B1(A, C) * (Z[A] / Z[C] - Z[C] / Z[A]) / 2

    return [B1, B2]


def symbolic():
    names = []
    for i in (1, 2, 3):
        names += [f"k{i}", f"z{i}", f"a{i}", f"b{i}"]
    names += ["c1", "c2", "c3"]
    K, *gens = field(",".join(names), QQ)
    g = dict(zip(names, gens))
    out = {}
    for label, pcoef, pats in (("c1k+c3k^3 two-amplitude", {1: g["c1"], 3: g["c3"]}, [("FG",) * 3]),
                               ("c1k+c2k^2+c3k^3", {1: g["c1"], 2: g["c2"], 3: g["c3"]},
                                list(itertools.product("FG", repeat=3)))):
        P = {(0, 0, 1): K.one}
        for j, cj in pcoef.items():
            P[(j, 0, 0)] = cj
        for pat in pats:
            waves, a, b = [], [], []
            for i, typ in zip((1, 2, 3), pat):
                k = g[f"k{i}"]
                pk = sum((cj * k**j for j, cj in pcoef.items()), K.zero)
                pmk = sum((cj * (-k) ** j for j, cj in pcoef.items()), K.zero)
                waves.append((k, K.zero, -pk if typ in ("FG", "F") else pmk))
                a.append(g[f"a{i}"] if typ in ("FG", "F") else K.zero)
                b.append(g[f"b{i}"] if typ in ("FG", "G") else K.zero)
            Bs = system(waves, P, [g["z1"], g["z2"], g["z3"]], K.one)
            F, G = H.two_function_solution(Bs, waves, a, b)
            out[f"{label} {''.join(t[0] for t in pat) if len(pats) > 1 else ''}".strip()] = \
                len(H.residuals(Bs, waves, F, G))
    return out


def failures():
    out = {}
    cfg = {"k": [Fr(1), Fr(2), Fr(-4)], "z": [Fr(2), Fr(3), Fr(5)]}
    for label, pc in (("k^4", {4: 1}), ("k^5", {5: 1}), ("k^5+k^2", {5: 1, 2: 1})):
        P = {(0, 0, 1): Fr(1)}
        for j, c in pc.items():
            P[(j, 0, 0)] = Fr(c)
        pats = {"FFG": "FFG", "two-amplitude": ("FG", "FG", "FG")} if all(j % 2 for j in pc) else {"FFG": "FFG"}
        for pname, pat in pats.items():
            waves, a, b = [], [], []
            for k, typ in zip(cfg["k"], pat):
                pk = sum(Fr(c) * k**j for j, c in pc.items())
                pmk = sum(Fr(c) * (-k) ** j for j, c in pc.items())
                waves.append((k, Fr(0), -pk if typ in ("FG", "F") else pmk))
                a.append(Fr(1) if typ in ("FG", "F") else Fr(0))
                b.append(Fr(3) if typ in ("FG", "G") else Fr(0))
            Bs = system(waves, P, cfg["z"], Fr(1))
            F, G = H.two_function_solution(Bs, waves, a, b)
            out[f"{label} {pname}"] = len(H.residuals(Bs, waves, F, G))
    return out


def main():
    OUT.mkdir(exist_ok=True)
    t0 = time.time()
    sym = symbolic()
    print(f"symbolic N=3, R(S) = sinh(D_n): nonzero residual counts {sym}  [{time.time() - t0:.1f}s]")
    fl = failures()
    print("exact configurations k=(1,2,-4), z=(2,3,5): nonzero residual counts", fl)
    (OUT / "discrete_variant.json").write_text(json.dumps({"symbolic_cubic": sym, "failures_deg_ge_4": fl},
                                                          indent=2))
    print("wrote", OUT / "discrete_variant.json")


if __name__ == "__main__":
    main()
