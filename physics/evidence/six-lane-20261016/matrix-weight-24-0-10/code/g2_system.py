"""Linear genus-2 system for a hypothetical even (Type II) additive self-dual (24, 2^24, 10) code over F4,
i.e. a [[24,0,10]] stabilizer state.

Unknowns: S3-symmetric pair counts f(tau) on ALLOWED types (wt u, wt v, wt(u+v) in {0,10,12,...,24}).
Equations (all necessary for an actual code):
  (G2) genus-2 MacWilliams self-duality  sum_tau f(tau) K(tau->tau') = 2^48 f(tau') for every type tau'
  (N)  f(00 type) = 1;   (M) genus-1 marginals f(u,0)-types = A_i of AMH Eq. (38)
Solved modulo primes (int64 Gaussian elimination) to get the rank / solution-space dimension; a unique
solution is then reconstructed by CRT and checked EXACTLY elsewhere.
"""
import itertools
import json
import sys
import time

import numpy as np

from genus2 import brute_T, tau_to_orbit, transform_row, types

N = 24
ALLOWED_W = set([0] + list(range(10, 25, 2)))
A38 = {0: 1, 10: 18216, 12: 156492, 14: 1147608, 16: 3736557, 18: 6248088, 20: 4399164, 22: 1038312, 24: 32778}


def allowed_types(n=N, allowed=ALLOWED_W):
    out = []
    for tau in types(n):
        i, j, t, p = tau_to_orbit(tau, n)
        k = i + j - t - p
        if i in allowed and j in allowed and k in allowed and tau[3] % 2 == 0:
            out.append(tau)
    return out


def s3key(tau):
    a, b, c, d = tau
    return (tuple(sorted((a, b, c))), d)


def build_mod(p, n=N, allowed=ALLOWED_W, A=A38, log=print):
    T = brute_T()
    al = allowed_types(n, allowed)
    orbits = {}
    for tau in al:
        orbits.setdefault(s3key(tau), []).append(tau)
    okeys = sorted(orbits)
    col = {k: c for c, k in enumerate(okeys)}
    # rows: S3-orbit representatives of all types (f_hat is S3-symmetric when f is)
    allT = types(n)
    rowkeys = sorted({s3key(t) for t in allT})
    rep = {}
    for t in allT:
        rep.setdefault(s3key(t), t)
    rowidx = {k: r for r, k in enumerate(rowkeys)}
    M = np.zeros((len(rowkeys), len(okeys)), dtype=np.int64)
    t0 = time.time()
    rep_arrays_idx = np.array([rep[k] for k in rowkeys])
    for ci, k in enumerate(okeys):
        acc = np.zeros((n + 1,) * 4, dtype=np.int64)
        for tau in orbits[k]:
            acc = (acc + transform_row(tau, n, T, mod=p)) % p
        vals = acc[rep_arrays_idx[:, 0], rep_arrays_idx[:, 1], rep_arrays_idx[:, 2], rep_arrays_idx[:, 3]]
        M[:, ci] = vals % p
        if ci % 50 == 0:
            log(f"  col {ci}/{len(okeys)}  {time.time() - t0:.1f}s")
    big = pow(2, 2 * n, p)
    for k in okeys:
        if k in rowidx:
            M[rowidx[k], col[k]] = (M[rowidx[k], col[k]] - big) % p
    # extra rows: normalization and marginals (rhs vector)
    extra = []
    rhs = []
    zero = s3key((0, 0, 0, 0))
    r = np.zeros(len(okeys), dtype=np.int64); r[col[zero]] = 1; extra.append(r); rhs.append(1)
    for i, Ai in A.items():
        if i == 0:
            continue
        key = s3key((0, i, 0, 0))
        r = np.zeros(len(okeys), dtype=np.int64); r[col[key]] = 1; extra.append(r); rhs.append(Ai % p)
    Mfull = np.vstack([M, np.array(extra)])
    b = np.concatenate([np.zeros(len(rowkeys), dtype=np.int64), np.array(rhs, dtype=np.int64)])
    return Mfull, b, okeys, orbits


def solve_mod(Mfull, b, p):
    """Gaussian elimination mod p on [M | b]. Returns (rank, consistent, particular solution, free columns)."""
    A = np.concatenate([Mfull % p, (b % p)[:, None]], axis=1).astype(np.int64)
    m, ncol = A.shape
    nv = ncol - 1
    piv_cols = []
    r = 0
    for c in range(nv):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr):
            A[nzr] = (A[nzr] - (col[nzr, None] * A[r][None, :]) % p) % p
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    rank = r
    consistent = not np.any(A[rank:, nv] % p)
    x = np.zeros(nv, dtype=np.int64)
    for i, c in enumerate(piv_cols):
        x[c] = A[i, nv]
    free = [c for c in range(nv) if c not in set(piv_cols)]
    return rank, consistent, x, free


if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 2147483647
    Mfull, b, okeys, orbits = build_mod(p)
    rank, cons, x, free = solve_mod(Mfull, b, p)
    out = {"prime": p, "n_unknown_orbits": len(okeys), "n_rows": int(Mfull.shape[0]), "rank": rank,
           "consistent": bool(cons), "solution_space_dim": len(okeys) - rank,
           "free_orbit_keys": [list(map(lambda z: list(z) if isinstance(z, tuple) else z, okeys[c])) for c in free]}
    print(json.dumps({k: v for k, v in out.items() if k != "free_orbit_keys"}))
    out["x_mod_p"] = {json.dumps(okeys[c]): int(x[c]) for c in range(len(okeys))}
    json.dump(out, open(f"../evidence/g2_system_mod_{p}.json", "w"))
