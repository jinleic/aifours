#!/usr/bin/env python3
"""moqls_numeric.py: EXPLORATION ONLY (never evidence). Lane moqls7-maximum.

Numerical search for t mutually orthogonal QLS(7) in standard form (row 0 of every square fixed to |0>,...,|6>),
with an optional non-classicality push on square 0 at cell (1,0):
  - objective: sum over squares s of ||G^s_l - I||^2 over the 14 row/column lines l (G^s the Gram matrix of square s's
    vectors); plus, for pairs s < t, ||G^s o G^t - I||_F^2 over all 49x49 entries (o = Hadamard product; this is the
    tensor-ONB condition);
  - push: sum_k relu(|z_(1,0),k|^2 - c)^2 on square 0, forcing every coordinate of that entry below c (c < 1 means
    weight >= 2, so square 0 cannot be classical).
Some squares may be fixed classical (--classical FILE: a JSON list of Latin squares in standard form).
Variables: rows 1..6 of each free square (42 vectors in C^7).
Reports the residual, ray counts per square, and the maximum weight in the standard frame.
"""
import argparse
import json
import time

import numpy as np
from scipy.optimize import minimize

P = 7
NQ = P * P
LINES = [[P * r + c for c in range(P)] for r in range(P)] + [[P * r + c for r in range(P)] for c in range(P)]
LINES = np.array(LINES)


def unpack(x, nfree):
    n = nfree * 42 * P
    Zf = (x[:n] + 1j * x[n:]).reshape(nfree, 42, P)
    out = []
    for s in range(nfree):
        Z = np.zeros((NQ, P), complex)
        Z[:P] = np.eye(P)
        Z[P:] = Zf[s]
        out.append(Z)
    return out


def objective(x, nfree, fixed, cpush, wpush):
    Zs = unpack(x, nfree) + fixed
    t = len(Zs)
    f = 0.0
    grads = [np.zeros((NQ, P), complex) for _ in range(t)]
    Gs = [Z.conj() @ Z.T for Z in Zs]                 # G[q,q'] = <z_q, z_q'>
    for s in range(nfree):
        Z, G = Zs[s], Gs[s]
        for l in LINES:
            H = G[np.ix_(l, l)] - np.eye(P)
            f += float(np.sum(np.abs(H) ** 2))
            grads[s][l] += 2 * H.conj() @ Z[l]
    for s in range(t):
        for u in range(s + 1, t):
            if s >= nfree and u >= nfree:
                continue
            H = Gs[s] * Gs[u] - np.eye(NQ)
            f += float(np.sum(np.abs(H) ** 2))
            if s < nfree:
                grads[s] += 2 * (Gs[u] * H.conj()) @ Zs[s]
            if u < nfree:
                grads[u] += 2 * (Gs[s] * H.conj()) @ Zs[u]
    if nfree > 0 and wpush > 0:
        z = Zs[0][P]                                   # cell (1,0)
        ex = np.maximum(np.abs(z) ** 2 - cpush, 0.0)
        f += wpush * float(np.sum(ex ** 2))
        grads[0][P] += wpush * 2 * ex * z
    g = np.concatenate([np.concatenate([2 * grads[s][P:].real.reshape(-1) for s in range(nfree)]),
                        np.concatenate([2 * grads[s][P:].imag.reshape(-1) for s in range(nfree)])])
    return f, g


def rays(Z, tol=1e-5):
    V = Z / np.linalg.norm(Z, axis=1, keepdims=True)
    reps = []
    for v in V:
        if not any(abs(abs(np.vdot(r, v)) - 1) < tol for r in reps):
            reps.append(v)
    return len(reps)


def maxweight(Z, tol=1e-5):
    V = Z / np.linalg.norm(Z, axis=1, keepdims=True)
    return int((np.abs(V) > tol).sum(axis=1).max())


def run(t, classical, starts, seed, cpush, wpush, maxiter):
    fixed = []
    for L in classical:
        Z = np.zeros((NQ, P), complex)
        for r in range(P):
            for c in range(P):
                Z[P * r + c, L[r][c]] = 1
        fixed.append(Z)
    nfree = t - len(fixed)
    rng = np.random.default_rng(seed)
    out = []
    for s in range(starts):
        x0 = rng.normal(size=2 * nfree * 42 * P) / np.sqrt(14)
        t0 = time.time()
        r = minimize(objective, x0, args=(nfree, fixed, cpush, wpush), jac=True, method="L-BFGS-B",
                     options={"maxiter": maxiter, "ftol": 1e-30, "gtol": 1e-13, "maxcor": 30})
        Zs = unpack(r.x, nfree)
        rec = {"start": s, "f": r.fun, "rays": [rays(Z) for Z in Zs], "maxweight": [maxweight(Z) for Z in Zs],
               "iters": int(r.nit), "sec": round(time.time() - t0, 1)}
        out.append(rec)
        print(json.dumps(rec), flush=True)
        if r.fun < 1e-20 and max(rec["rays"]) > P:
            np.save("moqls_candidate_seed%d_start%d.npy" % (seed, s), np.array(Zs))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, default=3)
    ap.add_argument("--classical", default=None, help="JSON file with a list of Latin squares (standard form)")
    ap.add_argument("--starts", type=int, default=5)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--cpush", type=float, default=0.9)
    ap.add_argument("--wpush", type=float, default=10.0)
    ap.add_argument("--maxiter", type=int, default=20000)
    a = ap.parse_args()
    cl = json.load(open(a.classical)) if a.classical else []
    run(a.t, cl, a.starts, a.seed, a.cpush, a.wpush, a.maxiter)
