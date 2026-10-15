"""Finite-difference check of Lemma 1 (K2) and of the symmetry/boundary identities (M0) on a
stochastic example (B0 != 0, D1'D0 != 0), plus a Monte Carlo check of Lemma 2 at the saddle point
(J(u°, w°) from (x0, 0) equals x0'P(t0)x0).

Command (from this directory):
  PYTHONPATH=. .../venv/bin/python check_identities.py ../evidence/identities.json
"""
import json
import sys

import numpy as np
from scipy.linalg import expm

from shp import Plant, solve_grde, continuous_controller_gains, simulate

pl = Plant(A=[[0.0, 1.0], [-2.0, -0.4]], B=[[0.0], [1.0]], C=[[1.0], [0.5]],
           A0=[[0.2, 0.0], [0.3, 0.2]], B0=[[0.0], [0.3]], D0=[[1.0, 0.0], [0.0, 0.3]], D1=[[0.0], [1.0]])
gam, h, T, dt = 1.2, 0.5, 3.0, 0.0025
sol = solve_grde(pl, gam, h, T, dt, store=True)
assert sol["ok"]
P, G, N, Nw = sol["P"], sol["G"], sol["N"], sol["Nw"]
n = pl.n
I = np.eye(n)


def K(i, j):  # K(t_i, t_i + j dt)
    return np.hstack([P[i], -I]) @ G[i, j]


out = {"gamma": gam, "h": h, "T": T, "dt": dt, "K2": [], "M0": []}
rng = np.random.default_rng(1)
for _ in range(12):
    i = int(rng.integers(Nw + 2, N - 2 * Nw - 2))  # keep t + h <= T so that k != 0
    j = int(rng.integers(2, Nw - 2))
    s_idx = i + j
    # dK/dt at fixed absolute s: column j-1 at time i+1, column j+1 at time i-1
    dK = (K(i + 1, j - 1) - K(i - 1, j + 1)) / (2 * dt)
    Rh, S, L, Ri, H0 = pl.blocks(P[i])
    Ac = pl.A - pl.B @ Ri @ L
    k = K(i, Nw)
    m = k.T @ G[i, j][:n]  # m(t,s) = k' Phi11(t,s) C
    rhs = -Ac.T @ K(i, j) - k @ m / gam**2
    out["K2"].append(dict(t=i * dt, s=s_idx * dt, max_abs_err=float(np.abs(dK - rhs).max()),
                          scale=float(np.abs(rhs).max())))
# (M0): M(t,t+h,s) computed from the definition equals m(t,s) = k' Phi11(t,s) C
for _ in range(6):
    i = int(rng.integers(0, N - Nw - 1))
    j = int(rng.integers(1, Nw))
    # forward transition Phi(t+h, t) and Phi(t+h, s) from step propagators
    def fwd(i0, i1):
        Phi = np.eye(2 * n)
        for q in range(i0, i1):
            Hq = pl.blocks(0.5 * (P[q] + P[q + 1]))[4]
            Phi = expm(Hq * dt) @ Phi
        return Phi
    Ph_t = fwd(i, i + Nw)
    Ph_s = fwd(i + j, i + Nw)
    Kts = K(i, j)
    M_def = pl.C.T @ Ph_t[n:, n:] @ Kts + pl.C.T @ Ph_s[n:, :n] @ pl.C
    k = K(i, Nw)
    m = k.T @ G[i, j][:n]
    out["M0"].append(dict(t=i * dt, s=(i + j) * dt, M_def=M_def.tolist(), m=m.tolist(),
                          abs_diff=float(np.abs(M_def - m).max())))
# Lemma 2 at the saddle: from x0 at t0 = 0 with empty window, J(u*, w*) = x0'P(0)x0.
x0 = np.array([1.0, -0.5])

def saddle_mc(dts, n_paths, seed):
    """Lemma 2 at the saddle point from (x0, empty window): returns (x0'P(0)x0, mean J, se)."""
    s2 = solve_grde(pl, gam, h, T, dts, store=True)
    P2, G2, N2, Nw2 = s2["P"], s2["G"], s2["N"], s2["Nw"]
    U2 = continuous_controller_gains(pl, s2, dts)
    r2 = np.random.default_rng(seed)
    wts = np.full(Nw2 + 1, dts)
    wts[0] = wts[-1] = dts / 2
    X = np.zeros((n_paths, n))  # state
    X[:] = x0
    V = np.zeros((n_paths, Nw2))  # window v_k, ..., v_{k+Nw-1}
    Ez = np.zeros(n_paths)
    Ew = np.zeros(n_paths)
    for k_ in range(N2):
        if k_ <= N2 - Nw2 - 1:
            kk = np.hstack([P2[k_], -I]) @ G2[k_, Nw2]  # k(t)
            mrow = np.array([(kk.T @ G2[k_, j][:n]).item() for j in range(Nw2 + 1)])  # m(t, t+j dt)
            # implicit trapezoid: w = gam^-2 (k'x + sum_{j<Nw} wt_j m_j v_j + wt_Nw m_Nw w)
            lin = X @ kk[:, 0] + V @ (wts[:Nw2] * mrow[:Nw2])
            w = lin / (gam**2 - wts[Nw2] * mrow[Nw2])
        else:
            w = np.zeros(n_paths)
        Yw = np.hstack([X, V, w[:, None]])
        u = Yw @ U2[k_].T
        z = X @ pl.D0.T + u @ pl.D1.T
        Ez += dts * np.sum(z * z, axis=1)
        Ew += dts * w * w
        noise = (X @ pl.A0.T + u @ pl.B0.T) * (np.sqrt(dts) * r2.standard_normal((n_paths, 1)))
        vk = V[:, 0] if Nw2 > 0 else w
        Xn = X + dts * (X @ pl.A.T + u @ pl.B.T + vk[:, None] @ pl.C.T) + noise
        V = np.hstack([V[:, 1:], w[:, None]]) if Nw2 > 0 else V
        X = Xn
    J = Ez - gam**2 * Ew
    return float(x0 @ P2[0] @ x0), float(J.mean()), float(J.std() / np.sqrt(n_paths))


out["lemma2_saddle"] = []
for dts, seed in [(0.005, 11), (0.0025, 12), (0.00125, 13)]:
    xPx, Jm, se = saddle_mc(dts, 20000, seed)
    out["lemma2_saddle"].append(dict(dt=dts, x0=x0.tolist(), xPx=xPx, J_mc=Jm, J_mc_se=se, n_paths=20000))
print(json.dumps({k: (v if k != "M0" else [dict(t=e["t"], s=e["s"], abs_diff=e["abs_diff"]) for e in v])
                  for k, v in out.items()}, indent=1))
with open(sys.argv[1], "w") as f:
    json.dump(out, f, indent=1)
