#!/usr/bin/env python3
"""onb_push.py: EXPLORATION ONLY. Lane moqls7-maximum.

K1 search on a 4-net with the frame fixed: the 7 points of line 0 (row 0) carry the standard basis (point with
column label j gets e_j). One chosen point p0 off that line is pushed to weight >= 3 by the penalty
sum_k relu(|z_p0,k|^2 - c)^2 with c < 1/2. (By the K1 weight-2 argument every non-classical assignment has a
weight >= 3 entry in this frame; for the Desarguesian nets Aut(N) restricted to row 0 is transitive on the 42 other
points, so p0 may be fixed.) Objective = sum_lines ||Z_l^H Z_l - I||^2 + w * penalty.
Usage: onb_push.py CLASSFILE IDX --starts N --seed S [--p0 Q] [--c 0.45] [--w 10]
"""
import argparse
import collections
import json
import time

import numpy as np
from scipy.optimize import minimize

import onb_numeric as o


def run(net, starts, seed, p0, c, w):
    L = o.make_problem(net)
    npts = len(net)
    row0 = L[0]                                # points of the first line of class 0
    # column label of each row-0 point: class 1 label
    basis_of = {q: net[q][1] for q in row0}
    free = [q for q in range(npts) if q not in basis_of]
    idx = {q: i for i, q in enumerate(free)}

    def full(x):
        Zf = (x[: len(free) * 7] + 1j * x[len(free) * 7:]).reshape(len(free), 7)
        Z = np.zeros((npts, 7), complex)
        for q, k in basis_of.items():
            Z[q, k] = 1.0
        Z[free] = Zf
        return Z

    def f(x):
        Z = full(x)
        Zl = Z[L]
        G = np.einsum("lpk,lqk->lpq", Zl.conj(), Zl) - np.eye(7)[None]
        val = float(np.sum(np.abs(G) ** 2))
        W = 2 * np.einsum("lqp,lqk->lpk", G, Zl)
        gc = np.zeros_like(Z)
        np.add.at(gc, L.reshape(-1), W.reshape(-1, 7))
        z = Z[p0]
        ex = np.maximum(np.abs(z) ** 2 - c * np.vdot(z, z).real, 0.0)
        val += w * float(np.sum(ex ** 2))
        # exact gradient: e_k = |z_k|^2 - c*sum_j |z_j|^2; d/dconj(z_m) sum_k relu(e_k)^2 = 2 z_m (relu(e_m) - c sum_k relu(e_k))
        gc[p0] += w * 2 * z * (ex - c * ex.sum())
        g = gc[free]
        return val, np.concatenate([2 * g.real.reshape(-1), 2 * g.imag.reshape(-1)])
    rng = np.random.default_rng(seed)
    res = []
    for s in range(starts):
        x0 = rng.normal(size=2 * len(free) * 7) / np.sqrt(14)
        r = minimize(f, x0, jac=True, method="L-BFGS-B",
                     options={"maxiter": 50000, "ftol": 1e-30, "gtol": 1e-14, "maxcor": 30})
        Z = full(r.x)
        base = o.fobj(np.concatenate([Z.real.reshape(-1), Z.imag.reshape(-1)]), L, npts)[0]
        rec = {"start": s, "obj": r.fun, "residual_without_push": base}
        if base < 1e-12:
            V = Z / np.linalg.norm(Z, axis=1, keepdims=True)
            rec.update({"rays": o.rays(Z), "weight_p0": int((np.abs(V[p0]) > 1e-6).sum()),
                        "maxweight": int((np.abs(V) > 1e-6).sum(axis=1).max())})
            if rec["rays"] > 7:
                np.save("k1_candidate_seed%d_start%d.npy" % (seed, s), Z)
        res.append(rec)
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("classfile")
    ap.add_argument("idx", type=int)
    ap.add_argument("--starts", type=int, default=50)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--p0", type=int, default=None)
    ap.add_argument("--c", type=float, default=0.45)
    ap.add_argument("--w", type=float, default=10.0)
    a = ap.parse_args()
    net = [tuple(q) for q in json.load(open(a.classfile))["classes"][a.idx]["net"]]
    L = o.make_problem(net)
    p0 = a.p0 if a.p0 is not None else next(q for q in range(49) if q not in set(L[0]))
    t0 = time.time()
    res = run(net, a.starts, a.seed, p0, a.c, a.w)
    zs = [r for r in res if r["residual_without_push"] < 1e-12]
    hist = collections.Counter(round(r["obj"], 3) for r in res)
    print(json.dumps({"class": a.idx, "p0": p0, "c": a.c, "starts": a.starts, "zeros": zs[:10], "n_zeros": len(zs),
                      "min_obj": min(r["obj"] for r in res), "top": hist.most_common(6),
                      "sec": round(time.time() - t0, 1)}))
