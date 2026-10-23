"""EXPLORATORY, floats only (not evidence; no proof uses this). (k, d) = (5, 12).

E1. Row function F_5(r) = (3/2) S^2 + Q/2 on the simplex Delta_5 (S = sum r^{11/12}, Q = sum r^{11/6}):
    minimum of (F(u*) - F(r)) / |r - u*|^2, to choose a safe constant c_row for the supplementary interval check,
    and the local coefficient at u*.
E2. KPW's relaxed exponent phi_12(M) = -(1/5) sum m ln m + 6 ln(1 - 2/5 + sum m^2/25) on 5x5 doubly stochastic M:
    multistart search for points with phi_12(M) > phi_12(J) (context only: is the relaxed route unavailable at
    (5, 12) for a structural reason, or only because AN's row-wise bound stops at d < 11.83?).
Writes ./explore_k5.json.
"""
import json
import math
import os

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
K, D = 5, 12
BETA = (D - 1) / D


def F(r):
    r = np.clip(r, 0.0, None)
    S = np.sum(r ** BETA)
    Q = np.sum(r ** (2 * BETA))
    return 1.5 * S * S + 0.5 * Q


def e1():
    u = np.full(K, 1.0 / K)
    FU = F(u)
    rng = np.random.default_rng(512)
    best = (1e9, None)
    fam = {}
    # two-value families
    for name, gen, lo, hi in (("x,y,y,y,y", lambda x: np.array([x] + [(1 - x) / 4] * 4), 0.0, 1.0),
                              ("x,x,y,y,y", lambda x: np.array([x, x] + [(1 - 2 * x) / 3] * 3), 0.0, 0.5)):
        xs = np.linspace(lo, hi, 20001)
        vals = []
        for x in xs:
            r = gen(x)
            d2 = np.sum((r - u) ** 2)
            if d2 < 1e-10:
                continue
            vals.append(((FU - F(r)) / d2, x))
        m = min(vals)
        fam[name] = {"min ratio": m[0], "at x": m[1]}
        if m[0] < best[0]:
            best = (m[0], name + f" x={m[1]:.5f}")
    # random points on the simplex (Dirichlet with various concentrations), plus vertices/edges
    for _ in range(200000):
        a = rng.choice([0.05, 0.2, 1.0, 5.0])
        r = rng.dirichlet(np.ones(K) * a)
        d2 = np.sum((r - u) ** 2)
        if d2 < 1e-10:
            continue
        val = (FU - F(r)) / d2
        if val < best[0]:
            best = (val, "random " + np.array2string(r, precision=4))
    # local coefficient by finite differences along a direction
    h = np.array([1, -1, 0, 0, 0]) / math.sqrt(2)
    t = 1e-4
    loc = (FU - F(u + t * h)) / (t * t)
    return {"F(u*)": FU, "8*5^(-5/6)": 8 * 5 ** (-5 / 6), "families": fam, "global min ratio found": best[0],
            "where": best[1], "local coefficient (finite difference)": loc,
            "local coefficient (analytic) 5^{-2b} b (425 b - 400)/2 with b = 11/12": -(5 ** (-2 * BETA)) * BETA * (425 * BETA - 400) / 2}


def phi(M):
    mv = M.reshape(-1)
    ent = np.sum(np.where(mv > 0, mv * np.log(np.where(mv > 0, mv, 1.0)), 0.0))
    return -ent / K + (D / 2) * math.log(1 - 2 / K + np.sum(mv * mv) / K ** 2)


def sinkhorn(M, it=2000):
    for _ in range(it):
        M = M / M.sum(axis=1, keepdims=True)
        M = M / M.sum(axis=0, keepdims=True)
    return M


def e2():
    J = np.full((K, K), 1.0 / K)
    pJ = phi(J)
    cons = []
    for p in range(K):
        cons.append({"type": "eq", "fun": (lambda z, p=p: z.reshape(K, K)[p, :].sum() - 1)})
    for q in range(K - 1):
        cons.append({"type": "eq", "fun": (lambda z, q=q: z.reshape(K, K)[:, q].sum() - 1)})
    rng = np.random.default_rng(1205)
    best = (-1e9, None)
    starts = []
    for _ in range(300):
        starts.append(sinkhorn(np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4, 8]), size=(K, K)))))
    for t in np.linspace(0.05, 1.0, 20):
        starts.append((1 - t) * J + t * np.eye(K))
    results = []
    for M0 in starts:
        res = minimize(lambda z: -phi(np.clip(z.reshape(K, K), 1e-15, None)), M0.reshape(-1), method="SLSQP",
                       bounds=[(0.0, 1.0)] * (K * K), constraints=cons, options={"maxiter": 500, "ftol": 1e-14})
        M = np.clip(res.x.reshape(K, K), 0, None)
        val = phi(np.clip(M, 1e-15, None)) - pJ
        dist = float(np.sum((M - J) ** 2))
        results.append((val, dist))
        if val > best[0]:
            best = (val, M)
    # one-parameter families
    fam = {}
    for name, P in (("M_t = (1-t)J + tI", np.eye(K)),
                    ("(1-t)J + t(1 + J_4/4)", np.block([[np.ones((1, 1)), np.zeros((1, 4))], [np.zeros((4, 1)), np.full((4, 4), 0.25)]])),
                    ("(1-t)J + t(J_2/2 + J_3/3)", np.block([[np.full((2, 2), 0.5), np.zeros((2, 3))], [np.zeros((3, 2)), np.full((3, 3), 1 / 3)]]))):
        vals = [(phi(np.clip((1 - t) * J + t * P, 1e-300, None)) - pJ, t) for t in np.linspace(0.01, 1.0, 400)]
        fam[name] = {"max phi - phi(J)": max(vals)[0], "at t": max(vals)[1]}
    nonJ = [r for r in results if r[1] > 1e-6]
    return {"phi_12(J)": pJ, "best phi_12(M) - phi_12(J) over 320 SLSQP starts": best[0],
            "best M distance^2 to J": float(np.sum((best[1] - J) ** 2)),
            "best M": np.round(best[1], 5).tolist(),
            "number of runs ending away from J (dist^2 > 1e-6)": len(nonJ),
            "max over those of phi - phi(J)": (max(nonJ)[0] if nonJ else None),
            "families": fam,
            "local coefficient of phi at J: 1/2 - d/(2(k-1)^2)": 0.5 - D / (2 * (K - 1) ** 2)}


def main():
    out = {"note": "floats; exploratory; not evidence; not used by any proof", "E1 row ratio": e1(), "E2 relaxed phi_12": e2()}
    with open(os.path.join(HERE, "explore_k5.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
