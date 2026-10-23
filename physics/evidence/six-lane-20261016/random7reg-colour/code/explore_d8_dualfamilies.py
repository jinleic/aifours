"""EXPLORATORY (floats, evidence only): restricted-dual closed-form upper bounds for the exact exponent at d = 8.

Weak duality with lam_v = alpha + g(m_v), alpha optimised in closed form:
  B_g(M) = C - (d/2) ln(4d) + d/2 + sum_v [((d-1)/4) m_v ln m_v - (d/4) m_v g(m_v)] + (d/2) ln(Y^T A Y),
  Y_v = exp(g(m_v)), A = (J4-I4) (x) (J4-I4),  C = (1-d/2) ln 4 + (d/2) ln d - d/2.
  Psi_d(M) <= B_g(M) for every g, and B_g(J) = Psi_d(J).
Cauchy-Schwarz relaxation (row/column sums): Y^T A Y <= (sum Y)^2/2 + sum Y^2 gives F_g(M) >= B_g(M), a symmetric
function of the multiset of entries (equality at J and on M_t).
Family g(m) = beta ln m + gamma m + delta m^2. Grid search over (beta, gamma, delta); worst case over B_4 by
multistart SLSQP. Also checks F_g for the best g on B_4, and on the larger set of row-stochastic matrices.
Writes ../evidence/explore_d8_dualfamilies.json.  Single-threaded, finite loops.
"""
import itertools
import json
import math
import os
import time

import numpy as np
from scipy.optimize import minimize

import explore_exact_exponent as E

K, D = 4, 8
A = E.ADJ
C = (1 - D / 2) * math.log(4) + (D / 2) * math.log(D) - D / 2
PSIJ = E.centre_value(D)


def g_of(m, par):
    beta, gamma, delta = par
    with np.errstate(divide="ignore"):
        return beta * np.log(m) + gamma * m + delta * m * m


def B_g(M, par, cs=False):
    m = np.clip(M.reshape(-1), 1e-300, None)
    g = g_of(m, par)
    Y = np.exp(g)
    lin = np.sum((D - 1) / 4 * m * np.log(m) - D / 4 * m * g)
    if cs:
        Q = Y.sum() ** 2 / 2 + np.sum(Y * Y)
    else:
        Q = Y @ (A @ Y)
    return C - (D / 2) * math.log(4 * D) + D / 2 + lin + (D / 2) * math.log(Q)


def cons_ds():
    cons = []
    for p in range(K):
        cons.append({"type": "eq", "fun": (lambda z, p=p: z.reshape(K, K)[p, :].sum() - 1.0)})
    for q in range(K - 1):
        cons.append({"type": "eq", "fun": (lambda z, q=q: z.reshape(K, K)[:, q].sum() - 1.0)})
    return cons


def cons_rows():
    return [{"type": "eq", "fun": (lambda z, p=p: z.reshape(K, K)[p, :].sum() - 1.0)} for p in range(K)]


def worst_case(par, pts, cs=False, rows_only=False):
    best = (-1e9, None)
    cons = cons_rows() if rows_only else cons_ds()
    for M0 in pts:
        f = lambda z: -(B_g(np.clip(z.reshape(K, K), 1e-14, None), par, cs) - PSIJ)
        res = minimize(f, M0.reshape(-1), method="SLSQP", bounds=[(1e-12, 1.0)] * 16, constraints=cons,
                       options={"maxiter": 200, "ftol": 1e-12})
        M = np.clip(res.x.reshape(K, K), 1e-14, None)
        if not rows_only:
            M = E.sinkhorn(M, 30)
        else:
            M = M / M.sum(axis=1, keepdims=True)
        val = B_g(M, par, cs) - PSIJ
        if val > best[0]:
            best = (val, float(np.sum((M - E.J) ** 2)), M.round(4).tolist())
    return best


def main():
    t0 = time.time()
    rng = np.random.default_rng(808)
    pts = []
    for s in range(24):
        kind = s % 3
        if kind == 0:
            pts.append(E.sinkhorn(np.exp(rng.normal(scale=rng.choice([1, 2, 4]), size=(K, K)))))
        elif kind == 1:
            pts.append(E.family(np.eye(K)[rng.permutation(K)], rng.uniform(0.2, 0.95)))
        else:
            w = rng.dirichlet(np.ones(3))
            pts.append(0.9 * sum(wi * np.eye(K)[rng.permutation(K)] for wi in w) + 0.1 * E.J)
    # sanity: exactness at J
    out = {"note": "EXPLORATORY numerics (floats); evidence only; no claim.",
           "B_g(J) - Psi(J) for g=(1,0,0)": B_g(E.J, (1.0, 0.0, 0.0)) - PSIJ}
    # M_t profile of the true dual: lam_D, lam_O versus m_D, m_O
    prof = []
    for t in (0.2, 0.4, 0.5, 0.6, 2 / 3, 0.8, 0.9):
        M = E.family(np.eye(K), t)
        lam = E.solve_dual(M, D)[0].reshape(K, K)
        prof.append({"t": t, "m_D": M[0, 0], "lam_D": lam[0, 0], "m_O": M[0, 1], "lam_O": lam[0, 1]})
    out["true dual along M_t (lam vs m)"] = prof
    # grid search
    grid = []
    for beta, gamma, delta in itertools.product((0.75, 1.0, 1.25, 1.5), (-3.0, -1.5, 0.0, 1.5, 3.0), (-2.0, 0.0, 2.0)):
        par = (beta, gamma, delta)
        wc = worst_case(par, pts[:12])
        grid.append((wc[0], par, wc[1]))
    grid.sort(key=lambda r: r[0])
    out["grid best 8 (worst-case B_g - Psi(J), (beta,gamma,delta), |M-J|^2)"] = grid[:8]
    # refine the best few with more starts, and test the Cauchy-Schwarz relaxation F_g
    refined = []
    for wc0, par, _ in grid[:3]:
        wc_ds = worst_case(par, pts)
        wc_cs = worst_case(par, pts, cs=True)
        wc_rows = worst_case(par, pts, cs=True, rows_only=True)
        refined.append({"par": par, "B_g worst on B_4": wc_ds[:2], "F_g (Cauchy-Schwarz) worst on B_4": wc_cs[:2],
                        "F_g worst on row-stochastic matrices": wc_rows[:2], "F_g row-stoch argmax": wc_rows[2]})
    out["refined"] = refined
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_d8_dualfamilies.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
