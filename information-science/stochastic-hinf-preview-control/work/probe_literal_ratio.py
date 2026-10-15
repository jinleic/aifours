"""Exploratory probe (not a theorem): the book's printed criterion E||z|| / E||w|| (pathwise L2 norm,
then expectation) versus the mean-square ratio sqrt(E||z||^2 / E||w||^2), for the mean-square-optimal
controller u* of example 1 (h = 0.5, T = 3, designed at 1.01 gamma*), under several disturbance
families including adaptive ones. Reports both ratios for every family.

Command (from this directory):
  OMP_NUM_THREADS=4 PYTHONPATH=. .../venv/bin/python probe_literal_ratio.py ../evidence/literal_probe.json
"""
import json
import sys

import numpy as np

from shp import (Plant, bisect_gamma, continuous_controller_gains, disc_closed_loop_gain, simulate,
                 solve_grde)

pl = Plant(A=[[1.0]], B=[[1.0]], C=[[1.0]], A0=[[0.5]], B0=[[0.4]], D0=[[1.0], [0.0]], D1=[[0.0], [1.0]])
h, T, dt = 0.5, 3.0, 0.01
gs = bisect_gamma(lambda g: solve_grde(pl, g, h, T, dt)["ok"], 0.05, 20.0, tol=1e-7)[1]
g_design = 1.01 * gs
sol = solve_grde(pl, g_design, h, T, dt, store=True)
U = continuous_controller_gains(pl, sol, dt)
gcl = bisect_gamma(lambda gg: disc_closed_loop_gain(pl, U, gg, h, T, dt)[0], 0.05, 20.0, tol=1e-9)[1]
ok, _, info = disc_closed_loop_gain(pl, U, gcl * (1 + 1e-6), h, T, dt, return_policy=True)
okf, kfail, infof = disc_closed_loop_gain(pl, U, gcl * (1 - 1e-6), h, T, dt, return_policy=True)
policy, e_dir = info["policy"], infof["direction"]
N = int(round(T / dt))
rng = np.random.default_rng(7)
n_paths = 20000


def ratios(w_fn, seed):
    r = np.random.default_rng(seed)
    Ez, Ew = simulate(pl, U, h, T, dt, w_fn, n_paths, r)
    lit = np.sqrt(Ez).mean() / np.sqrt(Ew).mean()
    ms = np.sqrt(Ez.mean() / Ew.mean())
    # bootstrap standard error of the literal ratio
    idx = rng.integers(0, n_paths, (200, n_paths))
    bs = np.sqrt(Ez)[idx].mean(1) / np.sqrt(Ew)[idx].mean(1)
    return dict(literal=float(lit), literal_se=float(bs.std()), mean_square=float(ms))


def kick(k, X):
    return np.full((X.shape[0], 1), 1.0 / np.sqrt(dt)) if k == 0 else np.zeros((X.shape[0], 1))


rows = {}
# 1. the mean-square worst case (impulse at the critical stage + maximizing feedback)
def w_ms(k, X):
    if k < kfail:
        return np.zeros((X.shape[0], 1))
    if k == kfail:
        return np.tile(e_dir / np.sqrt(dt), (X.shape[0], 1))
    return X @ policy[k].T
rows["ms_worst"] = ratios(w_ms, 1)
# 2. deterministic disturbances
rows["det_kick"] = ratios(kick, 2)
rows["det_const"] = ratios(lambda k, X: np.ones((X.shape[0], 1)), 3)
# 3. adaptive families: kick, then state feedback theta*x, optionally gated on |x| < tau ("top-up")
for theta in [0.5, 1.0, 2.0, 3.0]:
    for tau in [np.inf, 0.5, 0.2]:
        def w_ad(k, X, th=theta, ta=tau):
            if k == 0:
                return np.full((X.shape[0], 1), 1.0 / np.sqrt(dt))
            x = X[:, :1]
            return th * x * (np.abs(x) < ta)
        rows[f"adaptive_theta{theta}_tau{tau}"] = ratios(w_ad, 10 + int(10 * theta) + (0 if tau == np.inf else int(100 * tau)))
# 4. "betting": kick, then push only on paths whose state grew (sign-aligned constant push)
for c in [0.5, 2.0]:
    def w_bet(k, X, cc=c):
        if k == 0:
            return np.full((X.shape[0], 1), 1.0 / np.sqrt(dt))
        x = X[:, :1]
        return cc * np.sign(x) * (np.abs(x) > 0.3)
    rows[f"bet_c{c}"] = ratios(w_bet, 100 + int(10 * c))
out = dict(gamma_star_cont_dt=gs, design_gamma=g_design, exact_discrete_ms_gain=gcl, rows=rows,
           note="Exploratory. literal = mean(sqrt(int|z|^2)) / mean(sqrt(int|w|^2)); "
                "mean_square = sqrt(mean int|z|^2 / mean int|w|^2). Same paths for both.")
best = max(rows.items(), key=lambda kv: kv[1]["literal"])
out["max_literal_found"] = dict(family=best[0], **best[1])
print(json.dumps(out, indent=1))
with open(sys.argv[1], "w") as f:
    json.dump(out, f, indent=1)
