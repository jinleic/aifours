"""Float exploration of D's strata from diverse seeds (candidates only).

For each seed: project to D (MR map then Gauss-Newton), record tangent dimension (162 - rank J_dual), rank of U^G,
kernel type, e_p; then run Riemannian ascent of e_p and record the same data at the local maximum.
Usage: python -B explore_components.py SEED NPER OUTJSONL
"""
import itertools
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402
import numcore as nc  # noqa: E402
from ascent import descend, gn_project  # noqa: E402


def dual_perms():
    reps = {}
    for p in itertools.permutations(range(9)):
        P = np.zeros((9, 9))
        P[list(p), range(9)] = 1
        PR = nc.R(P)
        if not ((PR.sum(0) == 1).all() and (PR.sum(1) == 1).all()):
            continue
        key = (int(np.linalg.matrix_rank(nc.G(P))), round(float(nc.ep(P)), 6))
        reps.setdefault(key, P)
    return reps


def info(U):
    J = nc.jac_dual(U)
    s = np.linalg.svd(J, compute_uv=False)
    rJ = int((s > 1e-8 * s[0]).sum())
    A = nc.G(U)
    sA = np.linalg.svd(A, compute_uv=False)
    rk = int((sA > 1e-7).sum())
    kt = None
    if 0 < 9 - rk:
        _, _, Vh = np.linalg.svd(A)
        K = Vh[rk:].conj().T
        rng = np.random.default_rng(0)
        sch = []
        for _ in range(3):
            w = K @ (rng.standard_normal(K.shape[1]) + 1j * rng.standard_normal(K.shape[1]))
            w /= np.linalg.norm(w)
            sch.append(np.round(np.linalg.svd(w.reshape(3, 3), compute_uv=False), 4).tolist())
        kt = sch
    return dict(tangent_dim=162 - rJ, rank_UG=rk, ep=float(nc.ep(U)), res=float(nc.dual_residual(U)),
                sv_UG=[round(float(x), 6) for x in sA], kernel_schmidt=kt)


def seeds(rng, nper, perms):
    S = np.array(g.swap(), dtype=complex)
    P9 = np.array(g.P9(), dtype=complex)
    for _ in range(nper):
        yield "haar-mr", nc.mr_map(nc.haar(9, rng), iters=4000, tol=1e-10)[0]
    for key, P in perms.items():
        for eps in (0.05, 0.3, 0.8):
            Z = nc.haar(9, rng)
            D1 = np.diag(np.exp(2j * np.pi * rng.random(9)))
            U = nc.polar(D1 @ P + eps * (Z - np.eye(9)))
            yield f"perm{key}-eps{eps}", nc.mr_map(U, iters=4000, tol=1e-10)[0]
    for eps in (1.0, 1.5, 2.5):
        for _ in range(max(1, nper // 4)):
            Z = rng.standard_normal((9, 9)) + 1j * rng.standard_normal((9, 9))
            U = nc.polar(P9 + eps * Z / np.linalg.norm(Z) * 3)
            yield f"p9far-{eps}", nc.mr_map(U, iters=4000, tol=1e-10)[0]
    for _ in range(max(1, nper // 4)):
        th = rng.uniform(0, 2 * np.pi)
        yield f"Us(theta={th:.3f})", S @ np.array(g.U36(np.cos(th), np.sin(th)), dtype=complex)


def main():
    seed, nper, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = np.random.default_rng(seed)
    perms = dual_perms()
    with open(out, "a") as fo:
        for name, U in seeds(rng, nper, perms):
            t0 = time.time()
            U, res, _ = gn_project(U, tol=1e-13)
            if res > 1e-11:
                fo.write(json.dumps(dict(seed=seed, start=name, status="projection-failed", res=float(res))) + "\n")
                continue
            a = info(U)
            U2, f, gn, t, _, status = descend(U, steps=2000)
            b = info(U2)
            rec = dict(seed=seed, start=name, start_info=a, max_info=b, ascent_status=status, ascent_steps=t,
                       gradnorm=float(gn), secs=round(time.time() - t0, 1))
            if b["ep"] > 0.9375 + 1e-6 and b["ep"] < 1 - 1e-9:
                rec["U_re"] = U2.real.tolist()
                rec["U_im"] = U2.imag.tolist()
            fo.write(json.dumps(rec) + "\n")
            fo.flush()
            print(name, "start", a["tangent_dim"], a["rank_UG"], round(a["ep"], 5), "-> max", b["tangent_dim"],
                  b["rank_UG"], round(b["ep"], 8), status, t, flush=True)


if __name__ == "__main__":
    main()
