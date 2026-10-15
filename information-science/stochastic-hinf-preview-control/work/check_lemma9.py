"""Direct check of Lemma 9 (work/theory.md §5.1) with a NONZERO initial preview window.

Example 1, h = 0.5, stationary stabilizing P at gamma = 1.01 x (numerical gamma*_inf). The worst-case
closed loop (u*, w*) is simulated from x0 = 1 and committed window v_0 = 1 on [0, h) by Euler-Maruyama
at two step sizes, and compared with the theory:
  mean        ybar(s): H0-flow with forcing [C v_0; 0] on [0,h] from [x0; P x0 + g0]; for s >= h,
              ybar(s) = E[1;P] e^{A_P (s-h)} c with c = x0 + int_0^h (e^{-H0 r})_11 C v_0(r) dr
              (propagated inside the invariant subspace S, as Lemma 9 states);
  renewal     Sigma(s) = (Gs ybar(s))^2 + int_0^s (Gs Psi(s-r))^2 Sigma(r) dr,   sigma = A0 x + B0 u*;
  2nd moment  E x(s)^2 = ybar_x(s)^2 + int_0^s Psi_x(s-r)^2 Sigma(r) dr.

Command (from this directory):
  OMP_NUM_THREADS=4 PYTHONPATH=. .../venv/bin/python check_lemma9.py ../evidence/lemma9_check.json
"""
import json
import sys

import numpy as np
from scipy.linalg import expm

from shp import Plant, limit_solution, stabilizing_tests

pl = Plant(A=[[1.0]], B=[[1.0]], C=[[1.0]], A0=[[0.5]], B0=[[0.4]], D0=[[1.0], [0.0]], D1=[[0.0], [1.0]])
h = 0.5
gam = 1.01 * 1.319044494628906  # 1.01 x numerical gamma*_inf(h = 0.5) from evidence/numerics.json E5
ok, P, info = limit_solution(pl, gam, h, 0.00125, T_max=400.0)
assert ok
st = stabilizing_tests(pl, P, gam, h)
Pm = float(P[0, 0])
Rh, S, L, Ri, H0 = pl.blocks(P)
Hg = H0.copy()
Hg[0, 1] += 1.0 / gam**2
A, B, C, A0, B0 = 1.0, 1.0, 1.0, 0.5, 0.4
Rh, S, L, Ri = float(Rh[0, 0]), float(S[0, 0]), float(L[0, 0]), float(Ri[0, 0])
Gs = np.array([A0 - B0 * Ri * S, -B0 * Ri * B])
IP = np.array([1.0, Pm])
E = expm(H0 * h)
EIP = E @ IP
Heff = np.linalg.solve(E, Hg @ E)
AP = float((Heff @ IP)[0])  # restriction of H_eff to graph(P)
S_end = 8.0
X0 = 1.0


def kernels(dt):
    Nw = int(round(h / dt))
    taus = np.arange(Nw + 1) * dt
    Em = [expm(-H0 * t) for t in taus]
    Kker = np.array([np.array([Pm, -1.0]) @ M @ np.array([C, 0.0]) for M in Em])
    mker = np.array([Kker[-1] * M[0, 0] * C for M in Em])
    wq = np.full(Nw + 1, dt)
    wq[0] = wq[-1] = dt / 2
    return Nw, Kker, mker, wq, Em


def monte_carlo(dt, n_paths, seed, batch=50000):
    """Batched Euler-Maruyama with a circular window buffer; returns means and standard errors."""
    Nw, Kker, mker, wq, _ = kernels(dt)
    k = Kker[-1]
    Ns = int(round(S_end / dt))
    rng = np.random.default_rng(seed)
    sums = {q: np.zeros(Ns + 1) for q in ["x", "x2", "s2", "x4", "s4"]}
    done = 0
    wm = wq[:Nw] * mker[:Nw]
    wk = wq[:Nw] * Kker[:Nw]
    while done < n_paths:
        nb = min(batch, n_paths - done)
        x = np.full(nb, X0)
        V = np.ones((nb, Nw))  # circular buffer; slot (ptr + j) % Nw holds v(t + j dt)
        ptr = 0
        for i in range(Ns + 1):
            idx = (ptr + np.arange(Nw)) % Nw
            wm_r = np.empty(Nw)
            wk_r = np.empty(Nw)
            wm_r[idx] = wm
            wk_r[idx] = wk
            lin = k * x + V @ wm_r
            w = lin / (gam**2 - wq[Nw] * mker[Nw])  # implicit trapezoid for v(t+h) = w(t)
            g = V @ wk_r + wq[Nw] * Kker[Nw] * w
            u = -Ri * (L * x + B * g)
            sig = A0 * x + B0 * u
            x2, s2 = x * x, sig * sig
            sums["x"][i] += x.sum()
            sums["x2"][i] += x2.sum()
            sums["s2"][i] += s2.sum()
            sums["x4"][i] += (x2 * x2).sum()
            sums["s4"][i] += (s2 * s2).sum()
            if i == Ns:
                break
            v_now = V[:, ptr].copy()
            x = x + dt * (A * x + B * u + C * v_now) + sig * np.sqrt(dt) * rng.standard_normal(nb)
            V[:, ptr] = w  # the slot of v(t) is reused for v(t + h) = w(t)
            ptr = (ptr + 1) % Nw
        done += nb
    m = {q: sums[q] / n_paths for q in sums}
    se_x2 = np.sqrt(np.maximum(m["x4"] - m["x2"] ** 2, 0) / n_paths)
    se_s2 = np.sqrt(np.maximum(m["s4"] - m["s2"] ** 2, 0) / n_paths)
    return m["x"], m["x2"], m["s2"], se_x2, se_s2


def theory(dt):
    Nw, Kker, mker, wq, Em = kernels(dt)
    Ns = int(round(S_end / dt))
    s_grid = np.arange(Ns + 1) * dt
    g0 = float(np.sum(wq * Kker))  # int_0^h K(tau) v_0(tau) d tau, v_0 = 1
    c = X0 + float(np.sum(wq * np.array([M[0, 0] for M in Em]) * C))
    ybar = np.zeros((Ns + 1, 2))
    y = np.array([X0, Pm * X0 + g0])
    Eh0 = expm(H0 * dt)
    Mf = np.linalg.solve(H0, (Eh0 - np.eye(2))) @ np.array([C, 0.0])
    for i in range(Ns + 1):
        if i <= Nw:
            ybar[i] = y
            y = Eh0 @ y + Mf
        else:
            ybar[i] = EIP * c * np.exp(AP * (s_grid[i] - h))
    Psi = np.array([(expm(H0 * s) @ IP) if s <= h + 1e-12 else EIP * np.exp(AP * (s - h)) for s in s_grid])
    kern = (Psi @ Gs) ** 2
    forcing = (ybar @ Gs) ** 2
    Sig = np.zeros(Ns + 1)
    Sig[0] = forcing[0]
    for i in range(1, Ns + 1):
        acc = forcing[i] + dt * (0.5 * kern[i] * Sig[0] + np.dot(kern[i - 1:0:-1], Sig[1:i]))
        Sig[i] = acc / (1 - 0.5 * dt * kern[0])
    Ex2 = np.empty(Ns + 1)
    Ex2[0] = ybar[0, 0] ** 2
    for i in range(1, Ns + 1):
        Ex2[i] = ybar[i, 0] ** 2 + dt * (0.5 * Psi[i, 0] ** 2 * Sig[0] + np.dot(Psi[i - 1:0:-1, 0] ** 2, Sig[1:i])
                                        + 0.5 * Psi[0, 0] ** 2 * Sig[i])
    return s_grid, ybar[:, 0], Ex2, Sig, ybar[Nw], c


s_th, Ex_th, Ex2_th, Sig_th, ybar_h, c = theory(0.00125)
# consistency of the first-window endpoint with the subspace S (Lemma 9 step 2, round-2 formula)
off_S = float(np.abs(ybar_h - EIP * c).max())
marks = [0.25, 0.5, 1.0, 2.0, 4.0, 8.0]
out = dict(gamma=gam, P=Pm, A_P=AP, rho_T=st["rho_T"], AP_max_real=st["AP_max_real"],
           initial=dict(x0=X0, window="v_0 = 1 on [0, h)"), ybar_h_minus_EIPc=off_S, mc={})
for dt, seed, npth in [(0.0025, 2026, 200000), (0.00125, 2027, 100000)]:
    Ex, Ex2, Es2, se_x2, se_s2 = monte_carlo(dt, npth, seed)
    rows = []
    for s in marks:
        i = int(round(s / dt))
        j = int(round(s / 0.00125))
        rows.append(dict(s=s, E_x_mc=float(Ex[i]), E_x_theory=float(Ex_th[j]), E_x2_mc=float(Ex2[i]),
                         E_x2_mc_se=float(se_x2[i]), E_x2_theory=float(Ex2_th[j]), E_sigma2_mc=float(Es2[i]),
                         E_sigma2_mc_se=float(se_s2[i]), Sigma_theory=float(Sig_th[j])))
    out["mc"][str(dt)] = dict(n_paths=npth, rows=rows)
print(json.dumps(out, indent=1))
with open(sys.argv[1], "w") as f:
    json.dump(out, f, indent=1)
