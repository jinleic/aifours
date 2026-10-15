"""Deterministic sub-case (A0 = B0 = 0) of example 2: the infinite-horizon threshold gamma*_inf(h)
from the stationary advanced GARE (limit of finite-horizon solutions) must decrease with h, from
the full-information H-infinity level (h = 0) towards the classical non-causal bound
    gamma_nc = sup_w || (I - G_u (G_u^* G_u)^{-1} G_u^*) G_v (jw) ||,
computed independently by a frequency sweep (z = G_v v + G_u u with u free and non-causal).

Command (from this directory):
  PYTHONPATH=. .../venv/bin/python check_deterministic_limit.py ../evidence/deterministic_limit.json
"""
import json
import sys

import numpy as np

from shp import Plant, bisect_gamma, limit_solution, stabilizing_tests

A = np.array([[0.0, 1.0], [-2.0, -0.4]])
B = np.array([[0.0], [1.0]])
C = np.array([[1.0], [0.5]])
D0 = np.array([[1.0, 0.0], [0.0, 0.3]])
D1 = np.array([[0.0], [1.0]])
pl = Plant(A=A, B=B, C=C, A0=np.zeros((2, 2)), B0=np.zeros((2, 1)), D0=D0, D1=D1)

# non-causal bound (frequency sweep, fine grid + local refinement)
def gain(w):
    R = np.linalg.inv(1j * w * np.eye(2) - A)
    Gv = D0 @ R @ C
    Gu = D0 @ R @ B + D1
    Pi = Gu @ np.linalg.solve(Gu.conj().T @ Gu, Gu.conj().T)
    return np.linalg.norm((np.eye(2) - Pi) @ Gv, 2)

ws = np.concatenate([[0.0], np.logspace(-3, 3, 20001)])
gs = np.array([gain(w) for w in ws])
i = int(np.argmax(gs))
lo, hi = ws[max(i - 1, 0)], ws[min(i + 1, len(ws) - 1)]
for _ in range(100):  # golden-section refinement
    m1, m2 = lo + 0.382 * (hi - lo), lo + 0.618 * (hi - lo)
    if gain(m1) > gain(m2):
        hi = m2
    else:
        lo = m1
gamma_nc = max(gs.max(), gain(0.5 * (lo + hi)))

out = {"gamma_noncausal": float(gamma_nc), "argmax_omega": float(0.5 * (lo + hi)), "rows": []}
dt = 0.005
for h in [0.0, 0.5, 1.0, 2.0, 4.0]:
    lo_g, hi_g = bisect_gamma(lambda g: limit_solution(pl, g, h, dt, T_max=400.0)[0], 0.5 * gamma_nc, 5.0, tol=1e-5)
    ok, P, info = limit_solution(pl, hi_g * 1.001, h, dt, T_max=400.0)
    st = stabilizing_tests(pl, P, hi_g * 1.001, h)
    out["rows"].append(dict(h=h, gamma_inf_star=hi_g, AP_max_real_at_1p001=st["AP_max_real"],
                            residual=st["residual"]))
    print(h, hi_g, st["AP_max_real"], flush=True)
print(json.dumps(out, indent=1))
with open(sys.argv[1], "w") as f:
    json.dump(out, f, indent=1)
