"""EXPLORATORY, floats only (not evidence; not used by any proof). At (k, d) = (4, 8): does the UNCONSTRAINED supremum of
GSVY's Phi_1^{B(x)B}(R) = (d/2) ln(R^T A R) - (d-1) ln sum R^{d/(d-1)} over R >= 0 (A = allowed-pair adjacency of K_4 x K_4)
exceed its value at R = 1 (which is U(J))? GSV/GSVY drop the overlap-marginal constraints and maximise Phi_1 freely;
PROOF_CHI8 bounds Phi_1(M^{7/8}) only on row-stochastic M. Writes ./unconstrained_phi1.json.
"""
import json
import math
import os

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
K, D = 4, 8
P = D / (D - 1)
CELLS = [(p, q) for p in range(K) for q in range(K)]
A = np.array([[1.0 if (u[0] != v[0] and u[1] != v[1]) else 0.0 for v in CELLS] for u in CELLS])


def phi(z):
    z = z - z.max()                     # scale invariance: normalise so that max R = 1 (no overflow)
    R = np.exp(np.clip(z, -60, 0))
    return (D / 2) * math.log(R @ A @ R) - (D - 1) * math.log(np.sum(R ** P))


def main():
    UJ = phi(np.zeros(16))
    rng = np.random.default_rng(20261017)
    best, bestz, vals = -1e9, None, []
    for _ in range(400):
        z0 = rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=16)
        res = minimize(lambda z: -phi(z), z0, method="BFGS", options={"maxiter": 3000, "gtol": 1e-11})
        v = -res.fun
        vals.append(v)
        if v > best:
            best, bestz = v, res.x
    R = np.exp(np.clip(bestz - bestz.max(), -60, 0))
    alpha = R ** P / np.sum(R ** P)          # GSVY map (20)
    # sanity: value of Phi_1 at R = I^{7/8} (permutation-type overlap) and at a 3x3 sub-block
    Rid = np.array([1.0 if p == q else 1e-30 for (p, q) in CELLS])
    out = {"note": "floats; exploratory; not evidence; not used by PROOF_CHI8",
           "U(J) = Phi_1(1)": UJ, "8 ln3 - 12 ln2": 8 * math.log(3) - 12 * math.log(2),
           "best over 400 BFGS starts": best, "best - U(J)": best - UJ,
           "number of starts within 1e-9 of U(J)": int(sum(abs(v - UJ) < 1e-9 for v in vals)),
           "map (20) image of the best R, times 4 (as a 4x4 matrix)": (4 * alpha.reshape(4, 4)).round(6).tolist(),
           "Phi_1 at R = indicator of the diagonal (U(I))": phi(np.log(Rid)),
           "U(I) = 4 ln3 - 6 ln2": 4 * math.log(3) - 6 * math.log(2)}
    with open(os.path.join(HERE, "unconstrained_phi1.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
