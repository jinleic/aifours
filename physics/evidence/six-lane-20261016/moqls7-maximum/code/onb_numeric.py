#!/usr/bin/env python3
# (class mode reads evidence/nets7_classes.json: {"classes": [{"net": [[l0,l1,l2,l3], ...49], ...}, ...]})
"""onb_numeric.py: EXPLORATION ONLY (never evidence). Lane moqls7-maximum.

Numerically search for ONB-assignments on a net of order 7: unit vectors psi_q in C^7 for the 49 points such that the
7 vectors on every line form an orthonormal basis. Objective F(Z) = sum over lines l of ||Z_l^H Z_l - I||_F^2 (Z_l the
7x7 matrix of the line's unnormalised vectors), minimised by L-BFGS with the analytic gradient. A zero of F is an
ONB-assignment. Rays are counted with tolerance; a classical assignment has exactly 7 rays.

Usage:
  onb_numeric.py desarg "inf,0,1,2" --starts 20
  onb_numeric.py class evidence/mols7_classes.jsonl 3 --starts 20
"""
import argparse
import json
import sys
import time

import numpy as np
from scipy.optimize import minimize

import nets


def make_problem(net):
    L = np.array(nets.lines(net))      # (nlines, 7) point indices
    return L


def fobj(x, L, npts):
    Z = (x[: npts * 7] + 1j * x[npts * 7:]).reshape(npts, 7)        # rows = vectors
    Zl = Z[L]                                                          # (nl, 7 points, 7 coords)
    G = np.einsum("lpk,lqk->lpq", Zl.conj(), Zl) - np.eye(7)[None]   # Gram per line (p,q) = <z_p, z_q>
    f = float(np.sum(np.abs(G) ** 2))
    # G[l,p,q] = <z_p, z_q> = sum_k conj(z_pk) z_qk; f = sum |G|^2.
    # Wirtinger: df/dconj(z_pk) = 2 sum_q G[q,p] z_qk; real gradient = 2 * (Re, Im) of it.
    W = 2 * np.einsum("lqp,lqk->lpk", G, Zl)
    grad_c = np.zeros_like(Z)
    np.add.at(grad_c, L.reshape(-1), W.reshape(-1, 7))
    g = np.concatenate([2 * grad_c.real.reshape(-1), 2 * grad_c.imag.reshape(-1)])
    return f, g


def rays(Z, tol=1e-6):
    V = Z / np.linalg.norm(Z, axis=1, keepdims=True)
    reps = []
    for v in V:
        if not any(abs(abs(np.vdot(r, v)) - 1) < tol for r in reps):
            reps.append(v)
    return len(reps)


def weights_in_frame(Z, line, tol=1e-6):
    """Weights of all vectors in the frame where the given line is the standard basis."""
    V = Z / np.linalg.norm(Z, axis=1, keepdims=True)
    B = V[line]                     # rows: the ONB
    C = V @ B.conj().T              # coefficients <b_k, v> (conj), magnitudes matter
    return (np.abs(C) > tol).sum(axis=1)


def search(net, starts, seed, maxiter=20000):
    L = make_problem(net)
    npts = len(net)
    rng = np.random.default_rng(seed)
    out = []
    for s in range(starts):
        x0 = rng.normal(size=2 * npts * 7) / np.sqrt(14)
        t0 = time.time()
        res = minimize(fobj, x0, args=(L, npts), jac=True, method="L-BFGS-B",
                       options={"maxiter": maxiter, "ftol": 1e-30, "gtol": 1e-14, "maxcor": 30})
        Z = (res.x[: npts * 7] + 1j * res.x[npts * 7:]).reshape(npts, 7)
        nr = rays(Z) if res.fun < 1e-12 else None
        w = weights_in_frame(Z, L[0]) if res.fun < 1e-12 else None
        out.append({"start": s, "f": res.fun, "rays": nr, "maxweight_row0frame": None if w is None else int(w.max()),
                    "sec": round(time.time() - t0, 1)})
        print(json.dumps(out[-1]), flush=True)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["desarg", "class"])
    ap.add_argument("arg")
    ap.add_argument("idx", nargs="?", type=int, default=0)
    ap.add_argument("--starts", type=int, default=10)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.kind == "desarg":
        dirs = [d if d == "inf" else int(d) for d in a.arg.split(",")]
        net = nets.desarguesian_net(dirs)
    else:
        net = [tuple(q) for q in json.load(open(a.arg))["classes"][a.idx]["net"]]
    assert nets.is_net(net)
    search(net, a.starts, a.seed)
