"""Float probe (candidates only): actively seek dual unitaries with sigma_7(U^G) > 0 outside O9.

Minimise  Phi(U) = ||F_dual(U)||^2 - lam * sum_{i>=7} sigma_i(U^G)^2 + mu * relu(0.72 - ||G-I||^2)^2
over all 9x9 complex U (ambient), annealing lam -> 0, then Gauss-Newton polish onto D.  The relu term keeps
e_p <= 0.99 (away from O9, where sigma_7..9 = 1).  Usage: python -B seek_rank7.py SEED N OUTJSONL
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numcore as nc  # noqa: E402
from ascent import gn_project  # noqa: E402

I9 = np.eye(9)


def phi_and_grad(U, lam, mu):
    E1 = U @ U.conj().T - I9
    UR = nc.R(U)
    E2 = UR @ UR.conj().T - I9
    A = nc.G(U)
    Gm = A @ A.conj().T
    w, V = np.linalg.eigh(Gm)          # ascending
    small = V[:, :3]
    s_small = float(w[:3].sum())
    f = float(np.real(np.trace((Gm - I9) @ (Gm - I9))))
    pen = max(0.0, 0.72 - f)
    val = np.linalg.norm(E1) ** 2 + np.linalg.norm(E2) ** 2 - lam * s_small + mu * pen ** 2
    g = 4 * E1 @ U + nc.R(4 * E2 @ UR)
    gA = -lam * 2 * (small @ small.conj().T) @ A
    if pen > 0:
        gA = gA + mu * 2 * pen * (-4 * (Gm - I9) @ A)
    g = g + nc.G(gA)
    return val, g, s_small, f


def run(U, rng):
    for lam in (0.3, 0.1, 0.03, 0.01, 0.003, 0.0):
        eta = 0.05
        val, g, s, f = phi_and_grad(U, lam, 10.0)
        for it in range(1500):
            while True:
                Un = U - eta * g
                vn, gn, sn, fn = phi_and_grad(Un, lam, 10.0)
                if vn <= val - 1e-4 * eta * np.linalg.norm(g) ** 2:
                    U, val, g, s, f = Un, vn, gn, sn, fn
                    eta = min(eta * 1.3, 1.0)
                    break
                eta *= 0.5
                if eta < 1e-14:
                    break
            if eta < 1e-14 or np.linalg.norm(g) < 1e-10:
                break
    return U


def main():
    seed, n, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = np.random.default_rng(seed)
    with open(out, "a") as fo:
        for t in range(n):
            U0 = nc.haar(9, rng)
            U = run(U0, rng)
            U, res, _ = gn_project(U, tol=1e-13)
            sv = np.linalg.svd(nc.G(U), compute_uv=False)
            rec = dict(seed=seed, t=t, res=float(res), ep=float(nc.ep(U)), sv_UG=[round(float(x), 8) for x in sv],
                       rank_UG=int((sv > 1e-6).sum()))
            if rec["rank_UG"] > 6 and rec["ep"] < 1 - 1e-9 and res < 1e-11:
                rec["U_re"] = U.real.tolist()
                rec["U_im"] = U.imag.tolist()
            fo.write(json.dumps(rec) + "\n")
            fo.flush()
            print(t, f"res {res:.1e}", "ep", round(rec["ep"], 6), "rank", rec["rank_UG"], np.round(sv, 4), flush=True)


if __name__ == "__main__":
    main()
