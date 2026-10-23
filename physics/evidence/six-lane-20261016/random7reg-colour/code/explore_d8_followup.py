"""EXPLORATORY follow-up (floats, evidence only): d = 8 exact-exponent landscape and certification-cost inputs.

F1. Global minimum of the normalised margin r(M) = (Psi_8(J) - Psi_8(M)) / |M - J|_F^2 over the Birkhoff polytope
    (multistart SLSQP on r; near J, r -> (10-d)/20 = 0.1).
F2. Restricted-dual closed-form bounds (weak duality with lam_v = alpha + beta ln m_v, alpha optimised):
      B_beta(M) = (1-d/2) ln4 - (d/2) ln2 + ((d-1-d beta)/4) sum m ln m + (d/2) ln T_beta(M),
      T_beta(M) = (1/2) sum_{p!=r, q!=s} (m_pq m_rs)^beta,
    with Psi_d <= B_beta for all beta, B_1 = ln4 + phi_d (KPW's relaxation), B_beta(J) = Psi_d(J).
    Is there a single beta with B_beta <= B_beta(J) on B_4 at d = 8?  (multistart per beta)
F3. Relative volume of B_4 inside the 9-parameter cube [0,1]^9 (upper-left 3x3 block), Monte Carlo.
Writes ../evidence/explore_d8_followup.json.  Single-threaded, finite loops.
"""
import json
import math
import os
import time

import numpy as np
from scipy.optimize import minimize

import explore_exact_exponent as E

K = 4
J = E.J


def B_beta(M, d, beta):
    mv = M.reshape(-1)
    ent = sum(v * math.log(v) for v in mv if v > 0)
    T = 0.0
    for u in range(16):
        for v in range(16):
            if E.ADJ[u, v] > 0 and mv[u] > 0 and mv[v] > 0:
                T += (mv[u] * mv[v]) ** beta
    T *= 0.5
    return (1 - d / 2) * math.log(4) - (d / 2) * math.log(2) + (d - 1 - d * beta) / 4 * ent + (d / 2) * math.log(T)


def cons16():
    cons = []
    for p in range(K):
        cons.append({"type": "eq", "fun": (lambda z, p=p: z.reshape(K, K)[p, :].sum() - 1.0)})
    for q in range(K - 1):
        cons.append({"type": "eq", "fun": (lambda z, q=q: z.reshape(K, K)[:, q].sum() - 1.0)})
    return cons


def starts(rng, n):
    out = []
    for s in range(n):
        kind = s % 4
        if kind == 0:
            M0 = E.sinkhorn(np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=(K, K))))
        elif kind == 1:
            M0 = E.family(np.eye(K)[rng.permutation(K)], rng.uniform(0.1, 0.97))
        elif kind == 2:
            w = rng.dirichlet(np.ones(3))
            M0 = 0.9 * sum(wi * np.eye(K)[rng.permutation(K)] for wi in w) + 0.1 * J
        else:
            M0 = E.sinkhorn(np.exp(rng.normal(scale=6.0, size=(K, K))))
        out.append(M0)
    return out


def main():
    t0 = time.time()
    rng = np.random.default_rng(88)
    out = {"note": "EXPLORATORY numerics (floats); evidence only; no claim."}
    d = 8
    c0 = E.centre_value(d)
    # F1: minimise r(M) over B_4 \ {J}
    def r_of(z):
        M = np.clip(z.reshape(K, K), 1e-14, None)
        n2 = float(np.sum((M - J) ** 2))
        if n2 < 1e-10:
            return (10 - d) / 20
        return (c0 - E.psi_exact(M, d)[0]) / n2
    best = []
    for M0 in starts(rng, 120):
        if np.sum((M0 - J) ** 2) < 1e-4:
            continue
        res = minimize(r_of, M0.reshape(-1), method="SLSQP", bounds=[(1e-12, 1.0)] * 16, constraints=cons16(),
                       options={"maxiter": 300, "ftol": 1e-13})
        M = E.sinkhorn(np.clip(res.x.reshape(K, K), 1e-14, None), 50)
        best.append((r_of(M.reshape(-1)), float(np.sum((M - J) ** 2)), M.round(4).tolist()))
    best.sort(key=lambda x: x[0])
    out["F1 min normalised margin r(M) at d=8 (value, |M-J|^2, M)"] = best[0]
    out["F1 five smallest r"] = [(b[0], b[1]) for b in best[:5]]
    # F2: restricted-dual bounds
    f2 = {}
    pts = starts(rng, 60)
    for beta in (0.0, 0.25, 0.4, 0.5, 0.6, 0.75, 1.0):
        bJ = B_beta(J, d, beta)
        worst = (-1e9, None)
        for M0 in pts:
            res = minimize(lambda z: -(B_beta(np.clip(z.reshape(K, K), 1e-14, None), d, beta) - bJ), M0.reshape(-1),
                           method="SLSQP", bounds=[(1e-12, 1.0)] * 16, constraints=cons16(),
                           options={"maxiter": 300, "ftol": 1e-13})
            M = E.sinkhorn(np.clip(res.x.reshape(K, K), 1e-14, None), 50)
            val = B_beta(M, d, beta) - bJ
            if val > worst[0]:
                worst = (val, float(np.sum((M - J) ** 2)))
        # also at M=(J+I)/2
        Mh = E.family(np.eye(K), 0.5)
        f2[str(beta)] = {"B_beta(J) - Psi(J)": bJ - c0, "max over multistart of B_beta(M)-B_beta(J) [value, |M-J|^2]": worst,
                         "at (J+I)/2: B_beta - B_beta(J)": B_beta(Mh, d, beta) - bJ}
    out["F2 restricted-dual bounds at d=8"] = f2
    # F3: volume fraction of B_4 in the 9-parameter cube
    N = 400000
    Z = rng.uniform(size=(N, 3, 3))
    r4 = 1 - Z.sum(axis=2)            # 4th column entries for rows 1..3
    c4 = 1 - Z.sum(axis=1)            # 4th row entries for cols 1..3
    corner = 1 - c4.sum(axis=1)       # m44
    ok = (r4 >= 0).all(axis=1) & (c4 >= 0).all(axis=1) & (corner >= 0)
    out["F3 Monte Carlo fraction of [0,1]^9 lying in B_4 (upper-left 3x3 parametrisation)"] = float(ok.mean())
    out["F3 samples"] = N
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_d8_followup.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
