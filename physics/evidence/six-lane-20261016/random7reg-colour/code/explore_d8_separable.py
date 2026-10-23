"""EXPLORATORY (floats, evidence only): fully row-separable relaxations of the closed-form dual bound at d = 8.

With Y = m^beta e^{gamma m} (retuned g from explore_d8_rowrelax.json), per row r in Delta_4:
  a(r) = sum_q [((d-1)/4) r_q ln r_q - (d/4) r_q g(r_q)],  s(r) = sum_q Y(r_q),  t(r) = sum_q Y(r_q)^2,
and R_g(M) = K + sum_p a(r_p) + (d/2) ln((3/4) S^2 - sum s_p^2 + sum t_p),  S = sum_p s_p.
V1 (AM-QM on the cross term, S^2 <= 4 sum s_p^2):
  R'_g(M) = K + sum_p a(r_p) + (d/2) ln(sum_p b(r_p)),  b(r) = 2 s(r)^2 + t(r);  two-aggregate structure.
V2 (V1 + tangent line of ln at the centre value Q_J): fully separable
  W(M) = K + (d/2)(ln Q_J - 1) + sum_p [a(r_p) + (d/(2 Q_J)) b(r_p)]  =: K' + sum_p omega(r_p).
For V2 the target reduces to a per-row inequality omega(r) <= omega(U) - c |r - U|^2 on Delta_4.
Reports min normalised margins (multistart on row-stochastic matrices; for V2 a fine simplex grid on one row).
Writes ../evidence/explore_d8_separable.json.  Single-threaded, finite loops.
"""
import json
import math
import os
import time

import numpy as np
from scipy.optimize import minimize

import explore_exact_exponent as E
from explore_d8_dualfamilies import PSIJ, C, D, K
from explore_d8_tune import R_g, min_ratio
from explore_d8_rowrelax import starts_rows

J = E.J


def pieces(r, par):
    beta, gamma = par
    r = np.clip(np.asarray(r, dtype=float), 1e-300, None)
    g = beta * np.log(r) + gamma * r
    Y = np.exp(g)
    a = np.sum((D - 1) / 4 * r * np.log(r) - D / 4 * r * g)
    return a, Y.sum(), np.sum(Y * Y)


CONST = C - (D / 2) * math.log(4 * D) + D / 2


def R_prime(M, par):
    tot_a, tot_b = 0.0, 0.0
    for row in M:
        a, s, t = pieces(row, par)
        tot_a += a
        tot_b += 2 * s * s + t
    return CONST + tot_a + (D / 2) * math.log(tot_b)


def main():
    t0 = time.time()
    rng = np.random.default_rng(808080)
    par = tuple(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence",
                                            "explore_d8_rowrelax.json")))["U3 retuned (beta, gamma) for row-stochastic margin"])
    out = {"note": "EXPLORATORY numerics (floats); evidence only; no claim.", "g (beta, gamma)": par}
    out["R_g(J) - Psi(J)"] = R_g(J, par) - PSIJ
    out["R'_g(J) - Psi(J)"] = R_prime(J, par) - PSIJ
    rpts = starts_rows(rng, 96)
    out["V1 R'_g (AM-QM) on row-stochastic, 96 starts: min normalised margin"] = min_ratio(lambda M: R_prime(M, par), rpts, rows_only=True)
    # V2: per-row omega
    aU, sU, tU = pieces([0.25] * 4, par)
    QJ = 4 * (2 * sU * sU + tU)

    def omega(r):
        a, s, t = pieces(r, par)
        return a + (D / (2 * QJ)) * (2 * s * s + t)
    oU = omega([0.25] * 4)
    worst = (1e9, None)
    N = 120
    for i in range(N + 1):
        for j in range(N + 1 - i):
            for k in range(N + 1 - i - j):
                r = np.array([i, j, k, N - i - j - k], dtype=float) / N
                n2 = float(np.sum((r - 0.25) ** 2))
                if n2 < 1e-12:
                    continue
                val = (oU - omega(r)) / n2
                if val < worst[0]:
                    worst = (val, r.tolist())
    out["V2 per-row: min over simplex grid (denominator 120) of (omega(U) - omega(r)) / |r-U|^2"] = worst
    # local coefficient of omega at U along a tangent direction
    vals = []
    for _ in range(5):
        v = rng.normal(size=4)
        v -= v.mean()
        v /= np.linalg.norm(v)
        e = 1e-4
        vals.append((omega(0.25 + e * v) + omega(0.25 - e * v) - 2 * oU) / (2 * e * e))
    out["V2 per-row quadratic coefficient at U (should be < 0)"] = vals
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_d8_separable.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
