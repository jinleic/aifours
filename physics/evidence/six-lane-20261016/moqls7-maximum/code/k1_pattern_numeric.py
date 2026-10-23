#!/usr/bin/env python3
"""k1_pattern_numeric.py: EXPLORATION ONLY. Lane moqls7-maximum.

Numerical realization search for a fixed K1 support pattern on a net: row 0 carries e_j; every other point p has its
vector supported exactly on the pattern's support S(p); a penalty keeps every pattern coordinate above delta
(|c|^2 >= delta * |z|^2). Objective = sum_lines ||Z_l^H Z_l - I||^2 + w * penalty.
Usage: k1_pattern_numeric.py CLASSFILE IDX MODELS.json MODEL_INDEX --starts N --delta D
"""
import argparse
import collections
import json

import numpy as np
from scipy.optimize import minimize

import onb_numeric as o


def run(net, supp, starts, seed, delta, w):
    L = o.make_problem(net)
    npts = len(net)
    row0 = set(L[0].tolist())
    basis_of = {q: net[q][1] for q in row0}
    slots = [(p, k) for p in range(npts) if p not in row0 for k in supp[p]]
    pidx = np.array([s[0] for s in slots])
    kidx = np.array([s[1] for s in slots])

    def full(x):
        Z = np.zeros((npts, 7), complex)
        for q, k in basis_of.items():
            Z[q, k] = 1.0
        Z[pidx, kidx] = x[: len(slots)] + 1j * x[len(slots):]
        return Z

    def f(x):
        Z = full(x)
        Zl = Z[L]
        G = np.einsum("lpk,lqk->lpq", Zl.conj(), Zl) - np.eye(7)[None]
        val = float(np.sum(np.abs(G) ** 2))
        W = 2 * np.einsum("lqp,lqk->lpk", G, Zl)
        gc = np.zeros_like(Z)
        np.add.at(gc, L.reshape(-1), W.reshape(-1, 7))
        nrm = np.sum(np.abs(Z) ** 2, axis=1)            # |z_p|^2
        a2 = np.abs(Z[pidx, kidx]) ** 2
        ex = np.maximum(delta * nrm[pidx] - a2, 0.0)       # want a2 >= delta*|z|^2
        val += w * float(np.sum(ex ** 2))
        # d/dconj(z) of ex^2 terms: 2 ex * (delta * z_p(all coords) - z_pk e_k)
        for j, (p, k) in enumerate(slots):
            if ex[j] > 0:
                gc[p] += w * 2 * ex[j] * delta * Z[p]
                gc[p, k] -= w * 2 * ex[j] * Z[p, k]
        g = gc[pidx, kidx]
        return val, np.concatenate([2 * g.real, 2 * g.imag])
    rng = np.random.default_rng(seed)
    out = []
    for s in range(starts):
        x0 = rng.normal(size=2 * len(slots)) / np.sqrt(8)
        r = minimize(f, x0, jac=True, method="L-BFGS-B",
                     options={"maxiter": 50000, "ftol": 1e-30, "gtol": 1e-14, "maxcor": 30})
        Z = full(r.x)
        base = o.fobj(np.concatenate([Z.real.reshape(-1), Z.imag.reshape(-1)]), L, npts)[0]
        out.append({"obj": r.fun, "residual": base})
        if base < 1e-12 and r.fun < 1e-12:
            np.save("k1pattern_candidate_seed%d_start%d.npy" % (seed, s), Z)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("classfile")
    ap.add_argument("idx", type=int)
    ap.add_argument("models")
    ap.add_argument("model_index", type=int)
    ap.add_argument("--starts", type=int, default=50)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--delta", type=float, default=0.01)
    ap.add_argument("--w", type=float, default=100.0)
    a = ap.parse_args()
    net = [tuple(q) for q in json.load(open(a.classfile))["classes"][a.idx]["net"]]
    model = json.load(open(a.models))["models"][a.model_index]
    supp = collections.defaultdict(list)
    for s in model:
        p, k = map(int, s.split(":"))
        supp[p].append(k)
    res = run(net, supp, a.starts, a.seed, a.delta, a.w)
    zs = [r for r in res if r["obj"] < 1e-12]
    hist = collections.Counter(round(r["obj"], 4) for r in res)
    print(json.dumps({"starts": a.starts, "delta": a.delta, "n_zero": len(zs), "min_obj": min(r["obj"] for r in res),
                      "min_residual": min(r["residual"] for r in res), "top": hist.most_common(6)}))
