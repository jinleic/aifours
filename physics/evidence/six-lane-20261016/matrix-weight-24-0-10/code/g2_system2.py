"""Genus-2 system with the PARTIAL MacWilliams transform (Fourier transform in the first component only):
for a self-dual additive code C, F(u,v) = 1_C(u) 1_C(v) satisfies  sum_u F(u,v) chi(<u,c>) = |C| F(c,v),
so the symmetrized pair counts obey  sum_tau f(tau) K1(tau->tau') = 2^n f(tau')  for EVERY type tau',
with K1 built from the brute-force-verified 5x5 matrix T1 (T1^2 = 4I, T1 T2 = T).  Rows for all tau' are used
(T1 does not commute with the full S3).  Also keeps the full-transform rows of g2_system.
"""
import json
import sys
import time

import numpy as np

from g2_system import A38, ALLOWED_W, allowed_types, s3key, solve_mod
from genus2 import brute_T, transform_row, types

T1 = np.array([[1, 0, 3, 0, 0], [0, 1, 0, 1, 2], [1, 0, -1, 0, 0], [0, 1, 0, 1, -2], [0, 1, 0, -1, 0]],
              dtype=np.int64)


def build_mod2(p, n=24, allowed=ALLOWED_W, A=A38, use_full=True, use_partial=True):
    T = brute_T()
    al = allowed_types(n, allowed)
    orbits = {}
    for tau in al:
        orbits.setdefault(s3key(tau), []).append(tau)
    okeys = sorted(orbits)
    col = {k: c for c, k in enumerate(okeys)}
    allT = types(n)
    tidx = np.array(allT)
    blocks = []
    if use_full:
        rowkeys = sorted({s3key(t) for t in allT})
        rep = {}
        for t in allT:
            rep.setdefault(s3key(t), t)
        ridx = np.array([rep[k] for k in rowkeys])
        Mf = np.zeros((len(rowkeys), len(okeys)), dtype=np.int64)
        for ci, k in enumerate(okeys):
            acc = np.zeros((n + 1,) * 4, dtype=np.int64)
            for tau in orbits[k]:
                acc = (acc + transform_row(tau, n, T, mod=p)) % p
            Mf[:, ci] = acc[ridx[:, 0], ridx[:, 1], ridx[:, 2], ridx[:, 3]] % p
        big = pow(2, 2 * n, p)
        for r, k in enumerate(rowkeys):
            if k in col:
                Mf[r, col[k]] = (Mf[r, col[k]] - big) % p
        blocks.append(Mf)
    if use_partial:
        Mp = np.zeros((len(allT), len(okeys)), dtype=np.int64)
        for ci, k in enumerate(okeys):
            acc = np.zeros((n + 1,) * 4, dtype=np.int64)
            for tau in orbits[k]:
                acc = (acc + transform_row(tau, n, T1, mod=p)) % p
            Mp[:, ci] = acc[tidx[:, 0], tidx[:, 1], tidx[:, 2], tidx[:, 3]] % p
        half = pow(2, n, p)
        for r, t in enumerate(allT):
            k = s3key(t)
            if k in col and t in set(orbits[k]):
                Mp[r, col[k]] = (Mp[r, col[k]] - half) % p
        blocks.append(Mp)
    extra, rhs = [], []
    zero = s3key((0, 0, 0, 0))
    r = np.zeros(len(okeys), dtype=np.int64); r[col[zero]] = 1; extra.append(r); rhs.append(1)
    for i, Ai in A.items():
        if i == 0:
            continue
        key = s3key((0, i, 0, 0))
        r = np.zeros(len(okeys), dtype=np.int64); r[col[key]] = 1; extra.append(r); rhs.append(Ai % p)
    M = np.vstack(blocks + [np.array(extra)])
    b = np.concatenate([np.zeros(sum(B_.shape[0] for B_ in blocks), dtype=np.int64), np.array(rhs, dtype=np.int64)])
    return M, b, okeys, orbits


if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 2147483647
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    t0 = time.time()
    if n == 24:
        M, b, okeys, orbits = build_mod2(p)
    else:
        data = json.load(open("../evidence/control_pair_counts.json"))
        name = {6: "hexacode", 12: "dodecacode_circulant_1_3_6"}[n]
        d = {6: 4, 12: 6}[n]
        wd = data[name]["weight_distribution"]
        allowed = set([0] + [w for w in range(d, n + 1) if w % 2 == 0])
        A = {w: wd[w] for w in range(n + 1) if wd[w]}
        M, b, okeys, orbits = build_mod2(p, n=n, allowed=allowed, A=A)
    rank, cons, x, free = solve_mod(M, b, p)
    out = {"prime": p, "n": n, "unknowns": len(okeys), "rows": int(M.shape[0]), "rank": rank,
           "consistent": bool(cons), "solution_dim": len(okeys) - rank, "seconds": round(time.time() - t0, 1)}
    if n != 24:
        lam = {tuple(map(int, k.split(","))): v for k, v in data[name]["lambda"].items()}
        from genus2 import orbit_to_tau
        actual = {}
        for o, v in lam.items():
            actual[s3key(orbit_to_tau(o))] = v
        xa = np.array([actual.get(k, 0) % p for k in okeys], dtype=object)
        resid = [(int(sum(int(M[r, c]) * int(xa[c]) for c in range(len(okeys)))) - int(b[r])) % p for r in range(M.shape[0])]
        out["actual_satisfies"] = not any(resid)
    print(json.dumps(out))
    json.dump({"out": out, "free": [okeys[f] for f in free]}, open(f"../evidence/g2_system2_n{n}_p{p}.json", "w"))
