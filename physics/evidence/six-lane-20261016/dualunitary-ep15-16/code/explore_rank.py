"""Float exploration of the rank of U^Gamma on D (candidate structure only).

(1) MR-map outputs polished by Gauss-Newton to residual <1e-13: singular values of U^G.
(2) Local test: from a polished point move along random tangent directions of D, retract by Gauss-Newton,
    and record sigma_7(U^G) -> is rank<=6 an open condition on D near the point?
(3) Kernel structure: for rank-6 points, is det identically zero on ker U^G (3x3 reshapes)?
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numcore as nc  # noqa: E402
from ascent import gn_project  # noqa: E402


def tangent_basis(U):
    J = nc.jac_dual(U)
    _, s, Vh = np.linalg.svd(J)
    k = int((s > 1e-9 * s[0]).sum())
    return Vh[k:].T, k  # columns span ker J


def main():
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
    nruns = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    out = []
    for r in range(nruns):
        U, k = nc.mr_map(nc.haar(9, rng), iters=3000, tol=1e-10)
        U, res, it = gn_project(U, tol=1e-13)
        sv = np.linalg.svd(nc.G(U), compute_uv=False)
        rec = dict(run=r, res=float(res), ep=float(nc.ep(U)), sv=[float(x) for x in sv])
        if res < 1e-12:
            Tb, kJ = tangent_basis(U)
            rec["rankJ"] = kJ
            s7 = []
            for eps in (1e-3, 1e-2, 1e-1):
                vals = []
                for _ in range(3):
                    v = Tb @ rng.standard_normal(Tb.shape[1])
                    v /= np.linalg.norm(v)
                    U2, res2, _ = gn_project(U + eps * nc.from_vec(v), tol=1e-13)
                    sv2 = np.linalg.svd(nc.G(U2), compute_uv=False)
                    vals.append((float(sv2[6]), float(res2)))
                s7.append((eps, vals))
            rec["sigma7_after_tangent_moves"] = s7
            # kernel determinant test (columns of U^G indexed by (a,d) = parties 1,4)
            A = nc.G(U)
            _, sA, VhA = np.linalg.svd(A)
            rk = int((sA > 1e-8).sum())
            rec["rank"] = rk
            if rk < 9:
                K = VhA[rk:].conj().T  # columns: kernel vectors
                dets = []
                for _ in range(5):
                    w = K @ (rng.standard_normal(K.shape[1]) + 1j * rng.standard_normal(K.shape[1]))
                    w /= np.linalg.norm(w)
                    dets.append(abs(np.linalg.det(w.reshape(3, 3))))
                rec["max|det| on ker (random unit vectors)"] = max(dets)
                # left kernel (rows indexed by (c,b) = parties 3,2)
                WA = np.linalg.svd(A)[0]
                L = WA[:, rk:]
                detsL = []
                for _ in range(5):
                    w = L @ (rng.standard_normal(L.shape[1]) + 1j * rng.standard_normal(L.shape[1]))
                    w /= np.linalg.norm(w)
                    detsL.append(abs(np.linalg.det(w.reshape(3, 3))))
                rec["max|det| on left ker"] = max(detsL)
        out.append(rec)
        print(json.dumps({k: (v if k != 'sv' else [round(x, 5) for x in v]) for k, v in rec.items()}), flush=True)
    with open(os.path.join(os.path.dirname(__file__), "..", "evidence", "explore_rank.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
