"""Frozen numerical evidence for work/theory.md.  All parameters are fixed below; no tuning.

Command (from this directory):
  OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4 PYTHONPATH=. \
    /Users/jinleic/jinleic-workspace/scratch/ai4s-stochastic-hinf-preview-control/venv/bin/python \
    run_evidence.py ../evidence/numerics.json

Experiments
  E1  finite-horizon threshold gamma*: continuous advanced GRDE vs independent discrete
      augmented-state game (and, for h = 0, the classical GRDE), dt in {0.02, 0.01, 0.005},
      Richardson-extrapolated to dt -> 0.
  E2  escape time of the GRDE vs first failing stage of the discrete game, gamma < gamma*.
  E3  exact discrete closed-loop gain of the discretised continuous controller u*.
  E4  near-worst-case disturbance (from the closed-loop max-DP) + Monte Carlo ratio; random
      disturbances for contrast.
  E5  infinite horizon: P_inf = lim P_T, stationary residual, (T1) A_P Hurwitz, (T2) rho(T_P) < 1,
      threshold gamma*_inf(h); long-horizon discrete game thresholds; h = 0 cross-check against the
      scalar stochastic GARE solved in closed form.
  E6  deterministic reduction (A0 = B0 = 0): advanced GRDE vs the H_eff Riccati P = Y X^{-1}.
"""
from __future__ import annotations

import json
import platform
import sys
import time

import numpy as np
import scipy
from scipy.linalg import expm

from shp import (Plant, bisect_gamma, continuous_controller_gains, disc_closed_loop_gain, disc_game,
                 limit_solution, simulate, solve_grde, stabilizing_tests, standard_grde)

T0 = time.time()
OUT = {"meta": {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
                "platform": platform.platform(), "started_unix": T0}}


def log(*a):
    print(f"[{time.time() - T0:7.1f}s]", *a, flush=True)


EX = {
    # scalar, control-dependent noise, unstable drift
    "ex1": dict(A=[[1.0]], B=[[1.0]], C=[[1.0]], A0=[[0.5]], B0=[[0.4]], D0=[[1.0], [0.0]], D1=[[0.0], [1.0]]),
    # two states, unmatched disturbance, B0 != 0, D1'D0 != 0
    "ex2": dict(A=[[0.0, 1.0], [-2.0, -0.4]], B=[[0.0], [1.0]], C=[[1.0], [0.5]],
                A0=[[0.2, 0.0], [0.3, 0.2]], B0=[[0.0], [0.3]], D0=[[1.0, 0.0], [0.0, 0.3]], D1=[[0.0], [1.0]]),
    # two states, two disturbance channels
    "ex3": dict(A=[[0.0, 1.0], [-2.0, -0.4]], B=[[0.0], [1.0]], C=[[1.0, 0.0], [0.5, 1.0]],
                A0=[[0.2, 0.0], [0.3, 0.2]], B0=[[0.0], [0.3]], D0=[[1.0, 0.0], [0.0, 0.3]], D1=[[0.0], [1.0]]),
}
T_FIN = 3.0
DTS = [0.02, 0.01, 0.005]
HS = [0.0, 0.5, 1.0]
BRACKET = (0.05, 20.0)
TOL = 1e-7


def richardson(vals):
    """vals at dt, dt/2, dt/4 -> first- and second-order extrapolations."""
    a, b, c = vals
    r1 = 2 * c - b
    r2 = (8 * c - 6 * b + a) / 3
    return r1, r2


# ---------------------------------------------------------------- E1 / E2
E1 = {}
for name in ["ex1", "ex2", "ex3"]:
    pl = Plant(**EX[name])
    E1[name] = {}
    hs = HS if name != "ex3" else [0.5]
    for h in hs:
        rec = {"cont": [], "disc": [], "std": []}
        for dt in DTS:
            gc = bisect_gamma(lambda g: solve_grde(pl, g, h, T_FIN, dt)["ok"], *BRACKET, tol=TOL)[1]
            gd = bisect_gamma(lambda g: disc_game(pl, g, h, T_FIN, dt)[0], *BRACKET, tol=TOL)[1]
            rec["cont"].append(gc)
            rec["disc"].append(gd)
            if h == 0.0:
                rec["std"].append(bisect_gamma(lambda g: standard_grde(pl, g, T_FIN, dt)[0], *BRACKET, tol=TOL)[1])
            log(name, "h", h, "dt", dt, "cont", f"{gc:.7f}", "disc", f"{gd:.7f}")
        rec["cont_extrap_1st_2nd"] = richardson(rec["cont"])
        rec["disc_extrap_1st_2nd"] = richardson(rec["disc"])
        if rec["std"]:
            rec["std_extrap_1st_2nd"] = richardson(rec["std"])
        r_c, r_d = rec["cont_extrap_1st_2nd"][1], rec["disc_extrap_1st_2nd"][1]
        rec["rel_diff_2nd_order_extrap"] = abs(r_c - r_d) / r_c
        # E2: escape times below threshold (dt = 0.01)
        dt = 0.01
        gs = rec["cont"][1]
        esc = []
        for fac in [0.98, 0.9, 0.8]:
            g = gs * fac
            sc = solve_grde(pl, g, h, T_FIN, dt)
            ok, kf, _ = disc_game(pl, g, h, T_FIN, dt)
            esc.append(dict(gamma=g, cont_escape_t=sc["t_escape"], disc_fail_t=None if kf is None else kf * dt))
        rec["escape_times_dt0.01"] = esc
        E1[name][str(h)] = rec
OUT["E1_E2_finite_horizon_thresholds"] = E1
log("E1/E2 done")

# ---------------------------------------------------------------- E3 / E4
E3 = {}
rng = np.random.default_rng(20261014)
for name in ["ex1", "ex2"]:
    pl = Plant(**EX[name])
    h, dt = 0.5, 0.01
    gs_c = E1[name][str(h)]["cont"][1]
    gs_d = E1[name][str(h)]["disc"][1]
    rows = []
    for fac in [1.002, 1.01, 1.05, 1.2]:
        g = gs_c * fac
        sol = solve_grde(pl, g, h, T_FIN, dt, store=True)
        U = continuous_controller_gains(pl, sol, dt)
        gcl = bisect_gamma(lambda gg: disc_closed_loop_gain(pl, U, gg, h, T_FIN, dt)[0], *BRACKET, tol=TOL)[1]
        rows.append(dict(design_gamma=g, closed_loop_gain=gcl, ratio=gcl / g))
        log(name, "design", f"{g:.6f}", "achieved", f"{gcl:.6f}")
    rec = dict(h=h, dt=dt, gamma_star_cont_dt=gs_c, gamma_star_disc_dt=gs_d, rows=rows)
    # E4: near-worst-case disturbance for the controller designed at 1.01 gamma*
    g = gs_c * 1.01
    sol = solve_grde(pl, g, h, T_FIN, dt, store=True)
    U = continuous_controller_gains(pl, sol, dt)
    gcl = bisect_gamma(lambda gg: disc_closed_loop_gain(pl, U, gg, h, T_FIN, dt)[0], *BRACKET, tol=1e-9)[1]
    g_test = gcl * (1 + 1e-6)
    ok, _, info = disc_closed_loop_gain(pl, U, g_test, h, T_FIN, dt, return_policy=True)
    okf, kfail, infof = disc_closed_loop_gain(pl, U, gcl * (1 - 1e-6), h, T_FIN, dt, return_policy=True)
    policy = info["policy"]
    e_dir = infof["direction"]
    N = int(round(T_FIN / dt))
    Nw = int(round(h / dt))

    def w_worst(k, X, kf=kfail, pol=policy, e=e_dir):
        if k < kf:
            return np.zeros((X.shape[0], pl.m))
        if k == kf:
            return np.tile(e / np.sqrt(dt), (X.shape[0], 1))
        return X @ pol[k].T

    n_paths = 40000
    Ez, Ew = simulate(pl, U, h, T_FIN, dt, w_worst, n_paths, rng)
    ratio = np.sqrt(Ez.mean() / Ew.mean())
    # bootstrap-free delta-method standard error of the ratio
    cz, cw = Ez.mean(), Ew.mean()
    var = np.var(Ez) / cz**2 + np.var(Ew) / cw**2 - 2 * np.cov(Ez, Ew)[0, 1] / (cz * cw)
    se = 0.5 * ratio * np.sqrt(var / n_paths)
    # contrast: random disturbances
    def w_white(k, X):
        return rng.standard_normal((X.shape[0], pl.m))

    def w_sine(k, X):
        return np.tile(np.sin(2.0 * k * dt) * np.ones(pl.m), (X.shape[0], 1))
    Ez2, Ew2 = simulate(pl, U, h, T_FIN, dt, w_white, 20000, rng)
    Ez3, Ew3 = simulate(pl, U, h, T_FIN, dt, w_sine, 20000, rng)
    rec["E4"] = dict(controller_design_gamma=g, exact_discrete_closed_loop_gain=gcl, critical_stage=kfail,
                     critical_time=kfail * dt, mc_paths=n_paths, mc_ratio_worst=ratio, mc_ratio_worst_se=se,
                     mc_ratio_white=float(np.sqrt(Ez2.mean() / Ew2.mean())),
                     mc_ratio_sine=float(np.sqrt(Ez3.mean() / Ew3.mean())))
    log(name, "E4", rec["E4"])
    E3[name] = rec
OUT["E3_E4_controller_and_worst_case"] = E3
log("E3/E4 done")

# ---------------------------------------------------------------- E5 infinite horizon
E5 = {}
pl = Plant(**EX["ex1"])
dt = 0.005
for h in HS:
    lo, hi = bisect_gamma(lambda g: limit_solution(pl, g, h, dt, T_max=400.0)[0], 0.7, 3.0, tol=1e-5)
    rows = []
    for fac in [1.0005, 1.002, 1.01, 1.05, 1.5]:
        g = hi * fac
        ok, P, info = limit_solution(pl, g, h, dt, T_max=400.0)
        st = stabilizing_tests(pl, P, g, h)
        rows.append(dict(gamma=g, P=st["P"], residual=st["residual"], AP_max_real=st["AP_max_real"],
                         rho_T=st["rho_T"], internal_stab_max_real=st["internal_stab_max_real"],
                         AP_vs_Heff=st["AP_vs_Heff"], T_used=info.get("T_used")))
    E5[str(h)] = dict(gamma_inf_star_bracket=[lo, hi], rows=rows)
    log("E5 h", h, "gamma_inf*", hi, "rho near threshold", rows[0]["rho_T"])
# long-horizon discrete game (independent): finite-T thresholds increase towards gamma*_inf
E5["disc_long_horizon"] = {}
for h, dtd in [(0.0, 0.01), (0.5, 0.01), (1.0, 0.01)]:
    vals = {}
    for T in [10.0, 20.0, 40.0]:
        vals[str(T)] = bisect_gamma(lambda g: disc_game(pl, g, h, T, dtd)[0], 0.5, 3.0, tol=1e-5)[1]
    E5["disc_long_horizon"][str(h)] = dict(dt=dtd, thresholds_by_T=vals)
    log("E5 disc long horizon h", h, vals)
# h = 0 closed-form cross-check (scalar): GARE roots + worst-case-loop ms-stability
a, b, c, a0, b0 = 1.0, 1.0, 1.0, 0.5, 0.4


def gare_scalar(P, g):
    Rh = 1.0 + b0 * P * b0
    S = b0 * P * a0
    L = b * P + S
    return 2 * a * P + a0 * P * a0 + 1.0 - L * L / Rh + (P * c) ** 2 / g**2


def scalar_stabilizing(g):
    # roots of gare_scalar on P >= 0 (multiply by Rh: cubic)
    Ps = np.linspace(0, 200, 400001)
    vals = gare_scalar(Ps, g)
    roots = []
    for i in np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]:
        lo_, hi_ = Ps[i], Ps[i + 1]
        for _ in range(100):
            mid = 0.5 * (lo_ + hi_)
            if np.sign(gare_scalar(mid, g)) == np.sign(gare_scalar(lo_, g)):
                lo_ = mid
            else:
                hi_ = mid
        roots.append(0.5 * (lo_ + hi_))
    good = []
    for P in roots:
        Rh = 1.0 + b0 * P * b0
        F = -(b * P + b0 * P * a0) / Rh
        aw = a + b * F + c * c * P / g**2
        a0w = a0 + b0 * F
        if 2 * aw + a0w**2 < 0:  # scalar mean-square stability of (aw, a0w)
            good.append(P)
    return roots, good


g_lo, g_hi = 0.7, 3.0
for _ in range(60):
    mid = 0.5 * (g_lo + g_hi)
    if scalar_stabilizing(mid)[1]:
        g_hi = mid
    else:
        g_lo = mid
E5["h0_closed_form"] = dict(gamma_inf_star=g_hi, roots_at_1p5=scalar_stabilizing(1.5)[0],
                            stabilizing_at_1p5=scalar_stabilizing(1.5)[1])
log("E5 closed form h=0 gamma*", g_hi)
OUT["E5_infinite_horizon"] = E5

# ---------------------------------------------------------------- E6 deterministic reduction
pl = Plant(A=[[0.0, 1.0], [-2.0, -0.4]], B=[[0.0], [1.0]], C=[[1.0], [0.5]], A0=np.zeros((2, 2)),
           B0=np.zeros((2, 1)), D0=[[1.0, 0.0], [0.0, 0.3]], D1=[[0.0], [1.0]])
h, dt, g = 0.5, 0.001, 1.5
sol = solve_grde(pl, g, h, T_FIN, dt)
H0 = pl.blocks(np.zeros((2, 2)))[4]
Hg = H0.copy()
Hg[:2, 2:] += pl.C @ pl.C.T / g**2
Heff = np.linalg.solve(expm(H0 * h), Hg @ expm(H0 * h))
N = int(round(T_FIN / dt))
Nw = int(round(h / dt))
# backward: for t >= T-h the plain H0; before, H_eff
XY = np.vstack([np.eye(2), np.zeros((2, 2))])
diffs = []
for i in range(N - 1, -1, -1):
    Hm = H0 if (i + Nw > N) else Heff
    XY = expm(-Hm * dt) @ XY
    if i % 100 == 0:
        Pxy = XY[2:] @ np.linalg.inv(XY[:2])
        diffs.append(float(np.abs(Pxy - sol["P"][i]).max()))
E6 = dict(gamma=g, h=h, dt=dt, max_abs_diff=max(diffs), P0_grde=sol["P"][0].tolist())
OUT["E6_deterministic_Heff"] = E6
log("E6", E6)

OUT["meta"]["runtime_s"] = time.time() - T0
with open(sys.argv[1], "w") as f:
    json.dump(OUT, f, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
log("wrote", sys.argv[1])
