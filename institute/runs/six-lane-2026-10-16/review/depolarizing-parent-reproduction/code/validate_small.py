#!/usr/bin/env python3
"""Small-M validation of sym_depol.py against brute force on R (x) (C^2)^{(x)M}.

Checks (all written to ../evidence/validation_small.json):
  A. S_N(Z) = Pi D^{(x)N}(Z) Pi  entrywise, random complex Z, N <= 8.
  B. Schur-Weyl block identity  E_r^dag D^{(x)M}(X) E_r = c_r S_N(tr_{2r} X)  entrywise
     (E_r = singlet embedding), random complex X on Sym^M, M <= 8, all r.
  C. Block weights sum_r m_r c_r lambda0(M-2r) = 1 and p_r = m_r tr(block_r) vs brute force.
  D. I_c(rho, D^{(x)M}) vs brute-force S(B)-S(RB) for random symmetric rank-two inputs:
     full / mod-3 (residues 0,1) / mod-3 complex / mod-2 supports, non-orthogonal pairs,
     random weights q, several eta, M = 2..10.
"""
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sym_depol import (LogFact, BWindows, apply_SN, assemble, coherent_information,  # noqa: E402
                       log_block_weights, partial_trace_factor)
from bruteforce import (SN_bf, block_bf, coherent_information_bf, dicke_matrix,  # noqa: E402
                        apply_depol, singlet_embedding)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../evidence/validation_small.json")


def SN_mine(Z, N, eta, lf):
    f = (1 - eta) / 2
    Bw = BWindows(f, N, N)
    O1 = apply_SN(Z[None], N, eta, Bw.get, N, lf)
    O2 = apply_SN(np.conj(Z.T)[None], N, eta, Bw.get, N, lf)
    return assemble(O1[0], O2[0], N)


def trace_2r(X, M, r, lf):
    """tr_{2r} X for a general operator X on Sym^M via rank-one factors of its columns."""
    N = M - 2 * r
    out = np.zeros((N + 1, N + 1), dtype=complex)
    I = np.eye(M + 1)
    for y in range(M + 1):
        A = partial_trace_factor(X[:, y], M, r, lf)        # |X e_y>
        Bv = partial_trace_factor(I[y], M, r, lf)          # |e_y>
        out += A.T @ np.conj(Bv)
    return out


def main():
    rng = np.random.default_rng(20261016)
    rep = dict(A=[], B=[], C=[], D=[])
    t0 = time.time()
    lf = LogFact(64)
    # A
    for N in range(1, 9):
        for eta in [0.1, 0.5, 11 / 15, 0.732, 2 / 3, 0.95]:
            Z = rng.normal(size=(N + 1, N + 1)) + 1j * rng.normal(size=(N + 1, N + 1))
            dev = float(np.abs(SN_mine(Z, N, eta, lf) - SN_bf(Z, N, eta)).max())
            rep["A"].append(dict(N=N, eta=eta, maxdev=dev))
    # B, C
    for M in range(2, 9):
        for eta in [0.2, 11 / 15, 0.9]:
            X = rng.normal(size=(M + 1, M + 1)) + 1j * rng.normal(size=(M + 1, M + 1))
            X = X @ np.conj(X.T)
            X /= np.trace(X).real
            f = (1 - eta) / 2
            lp = log_block_weights(M, eta, lf)
            V = dicke_matrix(M)
            Yfull = apply_depol((V.T @ X @ V).astype(complex), M, eta, 1)
            for r in range(M // 2 + 1):
                N = M - 2 * r
                Ym = (f * (1 - f)) ** r * SN_mine(trace_2r(X, M, r, lf), N, eta, lf)
                E = singlet_embedding(M, r)
                Yb = E.T @ Yfull @ E
                mr = math.comb(M, r) - (math.comb(M, r - 1) if r > 0 else 0)
                rep["B"].append(dict(M=M, r=r, eta=eta, maxdev=float(np.abs(Ym - Yb).max()),
                                     scale=float(np.abs(Yb).max())))
                rep["C"].append(dict(M=M, r=r, eta=eta, p_formula=math.exp(lp[r]),
                                     p_bruteforce=float(mr * np.trace(Yb).real)))
            rep["C"].append(dict(M=M, eta=eta, sum_p_minus_1=float(math.fsum(np.exp(lp)) - 1)))
    # D
    worst = 0.0
    for M in range(2, 11):
        for eta in [0.15, 0.5, 2 / 3, 0.732, 11 / 15, 0.9]:
            for pattern in ["full", "mod3", "mod3cplx", "mod2cplx"]:
                v = []
                for res in [0, 1]:
                    c = rng.normal(size=M + 1)
                    if "cplx" in pattern:
                        c = c + 1j * rng.normal(size=M + 1)
                    if pattern.startswith("mod3"):
                        c = c * ((np.arange(M + 1) % 3) == res)
                    if pattern.startswith("mod2"):
                        c = c * ((np.arange(M + 1) % 2) == res)
                    if np.linalg.norm(c) == 0:
                        c[res] = 1.0
                    v.append(c / np.linalg.norm(c))
                q = list(rng.dirichlet([1, 1]))
                a = coherent_information(v, q, M, eta, lf=lf, tail_logp=-1e9)
                b = coherent_information_bf(v, q, M, eta)
                dev = abs(a["Ic_nats"] - b["Ic_nats"])
                worst = max(worst, dev)
                rep["D"].append(dict(M=M, eta=eta, pattern=pattern, q=q,
                                     overlap=float(abs(np.vdot(v[0], v[1]))),
                                     Ic_mine=a["Ic_nats"], Ic_bf=b["Ic_nats"], dev=dev,
                                     SB_bf=b["SB"], SRB_bf=b["SRB"]))
        print("M=%d done, worst |dI_c| so far %.2e (%.0fs)" % (M, worst, time.time() - t0), flush=True)
    summ = dict(
        A_max=max(d["maxdev"] for d in rep["A"]),
        B_max=max(d["maxdev"] for d in rep["B"]),
        C_max_rel=max(abs(d["p_formula"] - d["p_bruteforce"]) / max(d["p_bruteforce"], 1e-300)
                      for d in rep["C"] if "p_formula" in d),
        C_max_sum=max(abs(d["sum_p_minus_1"]) for d in rep["C"] if "sum_p_minus_1" in d),
        D_max=max(d["dev"] for d in rep["D"]), D_count=len(rep["D"]),
        D_max_absIc=max(abs(d["Ic_bf"]) for d in rep["D"]),
        seconds=time.time() - t0)
    rep["summary"] = summ
    with open(OUT, "w") as fh:
        json.dump(rep, fh, indent=1)
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    main()
