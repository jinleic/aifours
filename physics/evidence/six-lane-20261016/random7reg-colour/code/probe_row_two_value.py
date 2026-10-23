"""EXPLORATORY probe (floats, evidence only): risk check for route (b1) of review/D8_SCREEN.md.

For R_g with g(m) = beta ln m + gamma m (retuned values), a row maximiser satisfies, per coordinate,
  F(r) := h'(r) + Y'(r) (kappa + 2 mu3 Y(r)) = lambda,
  h'(r) = ((d-1)/4)(ln r + 1) - (d/4)(g(r) + r g'(r)),  Y = r^beta e^{gamma r},
where kappa = mu1 + 2 mu2 s_p and mu3 come from the aggregate multipliers:
  mu1 = (d/2)(3/2) S / Q,  mu2 = -(d/2)/Q,  mu3 = (d/2)/Q.
Two-valued rows follow if F has at most one interior turning point on (0,1) (then F = lambda has <= 2 roots).
We sample (kappa, mu3) from random row-stochastic matrices (all rows p) and count the turning points of F on a fine
log-spaced grid. A count > 1 anywhere flags the route as needing extra work.
Writes ../evidence/probe_row_two_value.json.
"""
import json
import math
import os

import numpy as np

D = 8


def main():
    par = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence",
                                      "explore_d8_rowrelax.json")))["U3 retuned (beta, gamma) for row-stochastic margin"]
    beta, gamma = par
    rng = np.random.default_rng(4)
    r = np.concatenate([np.logspace(-12, -1, 3000), np.linspace(0.1, 1 - 1e-9, 6000)])
    g = beta * np.log(r) + gamma * r
    gp = beta / r + gamma
    hprime = (D - 1) / 4 * (np.log(r) + 1) - D / 4 * (g + r * gp)
    Y = np.exp(g)
    Yp = Y * gp
    samples, worst = 0, 0
    worst_case = None
    kap_rng, mu_rng = [1e9, -1e9], [1e9, -1e9]
    for _ in range(3000):
        M = np.array([rng.dirichlet(np.ones(4) * rng.choice([0.1, 0.5, 1.0, 4.0])) for _ in range(4)])
        if rng.random() < 0.3:
            M[rng.integers(4)] = 0.25
        Ym = M ** beta * np.exp(gamma * M)
        s = Ym.sum(axis=1)
        S = s.sum()
        Q = 0.75 * S * S - np.sum(s * s) + np.sum(Ym * Ym)
        mu1, mu2, mu3 = (D / 2) * 1.5 * S / Q, -(D / 2) / Q, (D / 2) / Q
        for p in range(4):
            kappa = mu1 + 2 * mu2 * s[p]
            kap_rng = [min(kap_rng[0], kappa), max(kap_rng[1], kappa)]
            mu_rng = [min(mu_rng[0], mu3), max(mu_rng[1], mu3)]
            F = hprime + Yp * (kappa + 2 * mu3 * Y)
            dF = np.diff(F)
            sgn = np.sign(dF)
            sgn = sgn[sgn != 0]
            turns = int(np.sum(sgn[1:] != sgn[:-1]))
            samples += 1
            if turns > worst:
                worst = turns
                worst_case = {"kappa": float(kappa), "mu3": float(mu3), "turning points": turns}
    out = {"note": "EXPLORATORY probe; floats; evidence only", "g (beta, gamma)": par, "row samples": samples,
           "max turning points of F on (0,1)": worst, "worst case": worst_case,
           "kappa range sampled": kap_rng, "mu3 range sampled": mu_rng}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "probe_row_two_value.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
