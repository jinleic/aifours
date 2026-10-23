#!/usr/bin/env python3
"""onb_many.py: EXPLORATION ONLY. Many-start scan for ONB-assignments on the 7 net classes of order 7.

For each start: random unit vectors, then averaged alternating projections (each line's 7 vectors replaced by the
nearest ONB via polar decomposition; every point's new vector is the normalised average of its 4 line projections),
then L-BFGS polishing of the residual F = sum_lines ||Z_l^H Z_l - I||^2 (onb_numeric.fobj). Records the residual
distribution, and for zero-residual runs the number of rays (7 = classical) and the maximum weight in the row-0 frame.
Usage: onb_many.py CLASSFILE IDX --starts N --seed S [--ap-iters K]
"""
import argparse
import collections
import json
import time

import numpy as np
from scipy.optimize import minimize

import onb_numeric as o


def polar(M):
    U, _, Vh = np.linalg.svd(M)
    return U @ Vh


def alt_proj(Z, L, iters):
    npts = Z.shape[0]
    for _ in range(iters):
        acc = np.zeros_like(Z)
        for l in L:
            B = Z[l].T                    # columns = vectors
            Q = polar(B)                  # nearest unitary
            acc[l] += Q.T
        Z = acc / np.linalg.norm(acc, axis=1, keepdims=True)
    return Z


def run(net, starts, seed, ap_iters):
    L = o.make_problem(net)
    npts = len(net)
    rng = np.random.default_rng(seed)
    fs, zeros = [], []
    for s in range(starts):
        Z = rng.normal(size=(npts, 7)) + 1j * rng.normal(size=(npts, 7))
        Z /= np.linalg.norm(Z, axis=1, keepdims=True)
        if ap_iters:
            Z = alt_proj(Z, L, ap_iters)
        x0 = np.concatenate([Z.real.reshape(-1), Z.imag.reshape(-1)])
        r = minimize(o.fobj, x0, args=(L, npts), jac=True, method="L-BFGS-B",
                     options={"maxiter": 50000, "ftol": 1e-30, "gtol": 1e-14, "maxcor": 30})
        fs.append(r.fun)
        if r.fun < 1e-12:
            Zf = (r.x[: npts * 7] + 1j * r.x[npts * 7:]).reshape(npts, 7)
            zeros.append({"start": s, "f": r.fun, "rays": o.rays(Zf),
                          "maxweight_row0frame": int(o.weights_in_frame(Zf, L[0]).max())})
            if zeros[-1]["rays"] > 7:
                np.save("onb_candidate_seed%d_start%d.npy" % (seed, s), Zf)
    hist = collections.Counter(round(f, 3) for f in fs)
    return {"starts": starts, "min_f": min(fs), "zeros": zeros, "top_minima": hist.most_common(8)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("classfile")
    ap.add_argument("idx", type=int)
    ap.add_argument("--starts", type=int, default=100)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--ap-iters", type=int, default=0)
    a = ap.parse_args()
    net = [tuple(q) for q in json.load(open(a.classfile))["classes"][a.idx]["net"]]
    t0 = time.time()
    res = run(net, a.starts, a.seed, a.ap_iters)
    res.update({"class": a.idx, "seed": a.seed, "ap_iters": a.ap_iters, "sec": round(time.time() - t0, 1)})
    print(json.dumps(res))
