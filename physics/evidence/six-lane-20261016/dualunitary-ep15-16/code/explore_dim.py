"""Float exploration: Jacobian ranks of the dual system at random dual points, P9, U_s(2pi/3)."""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402
import numcore as nc  # noqa: E402


def svals(A):
    return np.linalg.svd(A, compute_uv=False)


def rank(A, tol=1e-8):
    s = svals(A)
    return int((s > tol * max(1, s[0])).sum()), s


def report(name, U):
    J = nc.jac_dual(U)
    rJ, sJ = rank(J)
    T = nc.lu_tangent(U)
    rT, _ = rank(T)
    JG = nc.jac_G(U)
    rJG, _ = rank(np.vstack([J, JG]))
    # kernel of J, and gradient of e_p restricted
    s_small = sJ[rJ - 3:rJ + 3] if rJ >= 3 else sJ[:6]
    rec = dict(name=name, dual_res=float(nc.dual_residual(U)), ep=float(nc.ep(U)), rank_Jdual=rJ,
               kernel_dim=162 - rJ, rank_LU_tangent=rT, rank_J_dual_plus_G=rJG,
               svals_around_gap=[float(x) for x in s_small])
    print(json.dumps(rec))
    return rec


def main():
    rng = np.random.default_rng(20261017)
    out = []
    S = np.array(g.swap(), dtype=complex)
    U0 = np.array(g.U36(-0.5, np.sqrt(3) / 2), dtype=complex)
    out.append(report("P9", np.array(g.P9(), dtype=complex)))
    out.append(report("U_s(2pi/3)=S*U36", S @ U0))
    out.append(report("SWAP", S))
    for t in range(6):
        U, k = nc.mr_map(nc.haar(9, rng), iters=20000, tol=1e-13)
        out.append(report(f"MR-random-{t} (iters {k})", U))
    with open(os.path.join(os.path.dirname(__file__), "..", "evidence", "explore_dim.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
