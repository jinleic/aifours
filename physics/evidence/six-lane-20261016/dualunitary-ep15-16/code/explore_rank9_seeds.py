"""Float probe for exotic strata of D with rank U^G >= 7 outside O9 (candidates only).

Seeds biased toward full-rank U^G: random T-dual unitaries (alternating polar on U and U^G), partially
2-unitarised matrices (alternating polar on U, U^R, U^G for k steps), and P9 at Frobenius distance >= 1.
Each seed is projected onto D (MR map + Gauss-Newton); we record rank U^G, tangent dimension, e_p, and the
twist-system null dimension (w Z_bc symmetric).  Usage: python -B explore_rank9_seeds.py SEED N OUTJSONL
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402
import numcore as nc  # noqa: E402
from ascent import gn_project  # noqa: E402


def tdual_seed(rng, iters=400):
    U = nc.haar(9, rng)
    for _ in range(iters):
        U = nc.G(nc.polar(nc.G(U)))
        U = nc.polar(U)
    return U


def partial_2u(rng, k):
    U = nc.haar(9, rng)
    for _ in range(k):
        U = nc.R(nc.polar(nc.R(U)))
        U = nc.G(nc.polar(nc.G(U)))
        U = nc.polar(U)
    return U


def twist_null(U):
    T = U.reshape(3, 3, 3, 3)
    rows = []
    for b in range(3):
        for c in range(3):
            M = T[c, :, :, b].T
            for (i, j) in [(0, 1), (0, 2), (1, 2)]:
                r = np.zeros(9, complex)
                for k in range(3):
                    r[3 * i + k] += M[k, j]
                    r[3 * j + k] -= M[k, i]
                rows.append(r)
    s = np.linalg.svd(np.array(rows), compute_uv=False)
    return float(s[-1])


def main():
    seed, n, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = np.random.default_rng(seed)
    P9 = np.array(g.P9(), dtype=complex)
    with open(out, "a") as fo:
        for t in range(n):
            kind = ["tdual", "partial2u-3", "partial2u-10", "partial2u-30", "p9far"][t % 5]
            if kind == "tdual":
                U0 = tdual_seed(rng)
            elif kind.startswith("partial2u"):
                U0 = partial_2u(rng, int(kind.split("-")[1]))
            else:
                Z = rng.standard_normal((9, 9)) + 1j * rng.standard_normal((9, 9))
                U0 = nc.polar(P9 + rng.uniform(1.0, 2.0) * 3 * Z / np.linalg.norm(Z))
            U, _ = nc.mr_map(U0, iters=4000, tol=1e-10)
            U, res, _ = gn_project(U, tol=1e-13)
            rec = dict(seed=seed, t=t, kind=kind, res=float(res))
            if res < 1e-11:
                J = nc.jac_dual(U)
                s = np.linalg.svd(J, compute_uv=False)
                sv = np.linalg.svd(nc.G(U), compute_uv=False)
                rec.update(tangent_dim=int(162 - (s > 1e-8 * s[0]).sum()), rank_UG=int((sv > 1e-7).sum()),
                           sv_UG=[round(float(x), 7) for x in sv], ep=float(nc.ep(U)), twist_smin=twist_null(U))
                if rec["rank_UG"] > 6 and rec["ep"] < 1 - 1e-9:
                    rec["U_re"] = U.real.tolist()
                    rec["U_im"] = U.imag.tolist()
            fo.write(json.dumps(rec) + "\n")
            fo.flush()
            print(t, kind, rec.get("tangent_dim"), rec.get("rank_UG"), round(rec.get("ep", -1), 6),
                  round(rec.get("twist_smin", -1), 8), flush=True)


if __name__ == "__main__":
    main()
