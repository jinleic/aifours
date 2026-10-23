"""Exact (sympy) check of the marginal identity used in review/LEMMA_R_PROOF.r2.md §0.

For a generic 9x9 matrix U (entries and formal conjugates independent symbols), with the source conventions
U^Gamma[(i,beta),(j,alpha)] = U[(i,alpha),(j,beta)] and the 14|23 flattening M[(a,d),(b,c)] = U[(c,d),(a,b)]
(= 3 psi(a,b,c,d)), verify the polynomial identities
  (I1) M M^dag == (U^Gamma^dag U^Gamma)^T            (so 9 rho_14 = (U^Gamma^dag U^Gamma)^T),
  (I2) U^Gamma U^Gamma^dag == Pi (M^dag M)^T Pi^T     with Pi the fixed permutation (b,c) -> (c,b) of rows,
  (I3) tr (U^Gamma U^Gamma^dag)^2 == tr (M M^dag)^2  (equal purities; spectra agree as M M^dag, M^dag M do).
Control: (I1) with U^Gamma U^Gamma^dag in place of U^Gamma^dag U^Gamma is NOT an identity.
Writes ../evidence/marginal_identity_exact.json.  Run: python -B marginal_identity_exact.py
"""
import itertools
import json
import os

import sympy as sp

R = range(3)
idx = lambda i, j: 3 * i + j


def main():
    U = sp.Matrix(9, 9, lambda r, c: sp.Symbol("u%d_%d" % (r, c)))
    Uc = sp.Matrix(9, 9, lambda r, c: sp.Symbol("w%d_%d" % (r, c)))          # formal conjugate
    G = sp.zeros(9, 9); Gc = sp.zeros(9, 9)
    M = sp.zeros(9, 9); Mc = sp.zeros(9, 9)
    for i, al, j, be in itertools.product(R, repeat=4):
        G[idx(i, be), idx(j, al)] = U[idx(i, al), idx(j, be)]
        Gc[idx(i, be), idx(j, al)] = Uc[idx(i, al), idx(j, be)]
    for a, b, c, d in itertools.product(R, repeat=4):
        M[idx(a, d), idx(b, c)] = U[idx(c, d), idx(a, b)]
        Mc[idx(a, d), idx(b, c)] = Uc[idx(c, d), idx(a, b)]
    Pi = sp.zeros(9, 9)
    for b, c in itertools.product(R, repeat=2):
        Pi[idx(c, b), idx(b, c)] = 1
    MMd = (M * Mc.T).expand()
    GdG = (Gc.T * G).expand()
    GGd = (G * Gc.T).expand()
    MdM = (Mc.T * M).expand()
    out = {
        "I1 M M^dag == (U^G^dag U^G)^T": (MMd - GdG.T).expand() == sp.zeros(9, 9),
        "I2 U^G U^G^dag == Pi (M^dag M)^T Pi^T": (GGd - Pi * MdM.T * Pi.T).expand() == sp.zeros(9, 9),
        "I3 tr (U^G U^G^dag)^2 == tr (M M^dag)^2": sp.expand((GGd * GGd).trace() - (MMd * MMd).trace()) == 0,
        "control: M M^dag == (U^G U^G^dag)^T (must be false)": (MMd - GGd.T).expand() == sp.zeros(9, 9),
    }
    out["all_ok"] = out["I1 M M^dag == (U^G^dag U^G)^T"] and out["I2 U^G U^G^dag == Pi (M^dag M)^T Pi^T"] \
        and out["I3 tr (U^G U^G^dag)^2 == tr (M M^dag)^2"] and not out["control: M M^dag == (U^G U^G^dag)^T (must be false)"]
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "marginal_identity_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
