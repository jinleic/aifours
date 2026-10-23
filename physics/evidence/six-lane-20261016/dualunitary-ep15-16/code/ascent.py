"""Float candidate search: Riemannian gradient ascent of e_p on D (dual unitaries) with Gauss-Newton retraction.

Floats only generate candidates (README 0.4).  Usage:
  python -B ascent.py SEED NRUNS OUTJSONL [--start mr|us|perm|p9far] [--steps K]
"""
import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402
import numcore as nc  # noqa: E402


def F_dual(U):
    return np.concatenate([nc.herm_vec(nc.herm_res(U)), nc.herm_vec(nc.herm_res(nc.R(U)))])


def gn_project(U, tol=1e-13, maxit=50, rank=None):
    """Minimal-norm Gauss-Newton steps onto D = {F_dual = 0}."""
    for it in range(maxit):
        r = F_dual(U)
        nr = np.linalg.norm(r)
        if nr < tol:
            return U, nr, it
        J = nc.jac_dual(U)
        W, s, Vh = np.linalg.svd(J, full_matrices=False)
        k = rank if rank is not None else int((s > 1e-9 * s[0]).sum())
        delta = -(Vh[:k].T @ ((W[:, :k].T @ r) / s[:k]))
        U = U + nc.from_vec(delta)
    return U, np.linalg.norm(F_dual(U)), maxit


def grad_f(U):
    """ambient gradient of f = Tr (A A^dag)^2, A = U^G, as complex 9x9 (real inner product Re tr X^dag Y)."""
    A = nc.G(U)
    H = A @ A.conj().T
    return nc.G(4 * H @ A)


def f_val(U):
    A = nc.G(U)
    H = A @ A.conj().T
    return float(np.real(np.trace(H @ H)))


def tangent_proj(U, v):
    J = nc.jac_dual(U)
    W, s, Vh = np.linalg.svd(J)
    k = int((s > 1e-9 * s[0]).sum())
    Vn = Vh[:k]          # row space (normal directions)
    return v - Vn.T @ (Vn @ v), k


def descend(U, steps=3000, eta0=0.02, log_every=0, gtol=1e-10):
    """minimise f on D (maximise e_p)."""
    U, res, _ = gn_project(U)
    f = f_val(U)
    eta = eta0
    hist = []
    for t in range(steps):
        gvec = nc.to_vec(grad_f(U))
        gt, k = tangent_proj(U, gvec)
        gn = np.linalg.norm(gt)
        if gn < gtol:
            break
        while True:
            Un, res, _ = gn_project(U - eta * nc.from_vec(gt))
            fn = f_val(Un)
            if res < 1e-11 and fn < f - 1e-4 * eta * gn ** 2:
                U, f = Un, fn
                eta = min(eta * 1.5, 1.0)
                break
            eta *= 0.5
            if eta < 1e-12:
                return U, f, gn, t, hist, "linesearch-fail"
        if log_every and t % log_every == 0:
            hist.append((t, 1 - (f - 9) / 72, gn))
    return U, f, gn, t, hist, "ok"


def start_point(kind, rng):
    S = np.array(g.swap(), dtype=complex)
    if kind == "mr":
        U, _ = nc.mr_map(nc.haar(9, rng), iters=20000, tol=1e-12)
        return U
    if kind == "us":
        U0 = S @ np.array(g.U36(-0.5, np.sqrt(3) / 2), dtype=complex)
        Z = rng.standard_normal((9, 9)) + 1j * rng.standard_normal((9, 9))
        return U0 + 0.05 * Z / np.linalg.norm(Z)
    if kind == "p9far":
        P = np.array(g.P9(), dtype=complex)
        Z = rng.standard_normal((9, 9)) + 1j * rng.standard_normal((9, 9))
        return nc.polar(P + rng.uniform(0.6, 1.5) * Z / np.linalg.norm(Z) * 3)
    raise ValueError(kind)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed", type=int)
    ap.add_argument("nruns", type=int)
    ap.add_argument("out")
    ap.add_argument("--start", default="mr")
    ap.add_argument("--steps", type=int, default=3000)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    with open(a.out, "a") as fo:
        for r in range(a.nruns):
            t0 = time.time()
            U0 = start_point(a.start, rng)
            U, f, gn, t, hist, status = descend(U0, steps=a.steps)
            ep = 1 - (f - 9) / 72
            sv = np.linalg.svd(nc.G(U), compute_uv=False)
            rec = dict(seed=a.seed, run=r, start=a.start, ep=ep, ep_direct=float(nc.ep(U)), f=f, gradnorm=float(gn),
                       steps=t, status=status, dual_res=float(nc.dual_residual(U)),
                       svals_UG=[float(x) for x in sv], secs=round(time.time() - t0, 2))
            if ep > 0.9375 + 1e-6:
                rec["U_re"] = U.real.tolist()
                rec["U_im"] = U.imag.tolist()
            fo.write(json.dumps(rec) + "\n")
            fo.flush()
            print(r, status, round(ep, 10), "grad", f"{gn:.1e}", "steps", t, "res", f"{rec['dual_res']:.1e}",
                  "sv", np.round(sv, 4), rec["secs"], flush=True)


if __name__ == "__main__":
    main()
