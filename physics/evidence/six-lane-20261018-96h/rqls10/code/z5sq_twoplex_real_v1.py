#!/usr/bin/env python3
"""z5sq_twoplex_real_v1: exact real (mod 2*pi) solvability of the phase system of z5sq_twoplex_probe_v1, per 2-plex.

Unknowns phi_r(k) (r in {00,01,10,11}, k in K; 40 reals mod 2*pi); 30 equations
phi_r2(k1) - phi_r1(k1) - phi_r2(k2) + phi_r1(k2) = pi (mod 2*pi), i.e. M phi' = 1 (mod 2) with phi' = phi/pi real.
Exact method: unimodular integer row reduction T M = E (row echelon over Z, Euclid on rows), T tracked. The zero
rows of E give a basis of the integer left kernel; the system is solvable iff (T.1)_i is even for every zero row i.
Then E_top phi' = (T.1)_top is solved over Q (free variables 0) and M phi' - 1 in 2 Z^30 is re-checked exactly.
Standard library; budget 270 s; input argv[1] (probe v1 JSON), output argv[2] (exclusive).
"""
import json, sys, time
from fractions import Fraction
T0 = time.monotonic()
P = 5
data = json.load(open(sys.argv[1]))
reps = [(0, 0), (0, 1), (1, 0), (1, 1)]
edges = {"nu": [((0, 0), (0, 1)), ((1, 0), (1, 1))], "mu": [((0, 0), (1, 0)), ((0, 1), (1, 1))],
         "w": [((0, 0), (1, 1)), ((0, 1), (1, 0))]}
key = {"mu": lambda p: p[0], "nu": lambda p: p[1], "w": lambda p: (p[0] - p[1]) % P}


def int_echelon(M):
    """Returns (E, T, pivots) with T unimodular, T M = E in row echelon form over Z."""
    m, n = len(M), len(M[0])
    E = [r[:] for r in M]
    T = [[int(i == j) for j in range(m)] for i in range(m)]
    row = 0
    pivots = []
    for col in range(n):
        if row == m:
            break
        while True:
            nz = [i for i in range(row, m) if E[i][col] != 0]
            if not nz:
                break
            i0 = min(nz, key=lambda i: abs(E[i][col]))
            E[row], E[i0] = E[i0], E[row]
            T[row], T[i0] = T[i0], T[row]
            clean = True
            for i in range(row + 1, m):
                if E[i][col] != 0:
                    q = E[i][col] // E[row][col]
                    E[i] = [a - q * b for a, b in zip(E[i], E[row])]
                    T[i] = [a - q * b for a, b in zip(T[i], T[row])]
                    if E[i][col] != 0:
                        clean = False
            if clean:
                break
        if E[row][col] != 0:
            pivots.append(col)
            row += 1
    return E, T, pivots, row


results = []
nsolv = 0
for ir, rec in enumerate(data["results"]):
    if time.monotonic() - T0 > 270:
        break
    K = [tuple(p) for p in rec["K"]]
    idx = {p: i for i, p in enumerate(K)}
    match = {}
    for dname in ("mu", "nu", "w"):
        groups = {}
        for p in K:
            groups.setdefault(key[dname](p), []).append(idx[p])
        match[dname] = [tuple(g) for g in groups.values()]
    var = lambda r, k: reps.index(r) * 10 + k
    M = []
    for dname, elist in edges.items():
        for (r1, r2) in elist:
            for (k1, k2) in match[dname]:
                row = [0] * 40
                row[var(r2, k1)] += 1
                row[var(r1, k1)] -= 1
                row[var(r2, k2)] -= 1
                row[var(r1, k2)] += 1
                M.append(row)
    E, T, piv, rank = int_echelon(M)
    c = [sum(T[i]) for i in range(30)]                       # T . 1
    bottom = c[rank:]
    solvable = all(x % 2 == 0 for x in bottom)
    out = {"index": ir, "rank": rank, "left_kernel_dim": 30 - rank, "bottom_parities": [x % 2 for x in bottom], "solvable": solvable,
           "component_sizes": rec["component_sizes"], "component_bipartite": rec["component_bipartite"]}
    if solvable:
        nsolv += 1
        # solve E_top phi' = c_top over Q by back substitution (free variables 0)
        phi = [Fraction(0)] * 40
        for i in range(rank - 1, -1, -1):
            pc = piv[i]
            s = Fraction(c[i]) - sum(Fraction(E[i][j]) * phi[j] for j in range(pc + 1, 40))
            phi[pc] = s / E[i][pc]
        resid = [sum(Fraction(M[i][j]) * phi[j] for j in range(40)) - 1 for i in range(30)]
        ok = all((x / 2).denominator == 1 for x in resid)
        out["phi_over_pi"] = [str(x) for x in phi]
        out["recheck_exact_mod2"] = ok
        out["denominators"] = sorted({x.denominator for x in phi})
    results.append(out)
res = {"probe": "z5sq_twoplex_real_v1", "n_examined": len(results), "n_solvable": nsolv, "results": results,
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(sys.argv[2], "x") as fh:
    json.dump(res, fh)
print(json.dumps({k: res[k] for k in ("n_examined", "n_solvable", "elapsed_s")}),
      json.dumps(sorted({(r["rank"], tuple(r["bottom_parities"])) for r in results})))
