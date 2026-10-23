"""Experiment CANON (exploratory, float + optional exact): for a fully-closed configuration,
the CANONICAL numerator pins the phase of b at ALL n band points:
  interior x_j (j=1..n-2): double-contact condition E_b(x_j) + r_j O_b(x_j) = 0;
  x_0 (left end of the first E-band):        E_b(x_0) = 0;
  x_{n-1} (right end of the last band):      O_b(x_{n-1}) = 0 if n odd (last band is O),
                                             E_b(x_{n-1}) = 0 if n even (last band is E).
That is n linear conditions on n+1 coefficients: b is unique up to scale.  Test whether +-b is
a closed numerator (all four corner pairings >= 0 on a fine grid incl. near band points).
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as NP

from fclosed import contact_matrix, corners, touching


def canonical_b(x, n, Em, Ep, Om, Op):
    A = contact_matrix(x, n, Em, Ep, Om, Op)
    rows = list(A)
    # E_b(x0) = 0
    r0 = np.zeros(n + 1)
    for k in range(0, n + 1, 2):
        l = k // 2
        r0[k] = (-1) ** l * x[0] ** l
    rows.append(r0 / np.abs(r0).max())
    rl = np.zeros(n + 1)
    xl = x[-1]
    if n % 2 == 1:
        for k in range(1, n + 1, 2):
            l = k // 2
            rl[k] = (-1) ** l * xl ** l
    else:
        for k in range(0, n + 1, 2):
            l = k // 2
            rl[k] = (-1) ** l * xl ** l
    rows.append(rl / np.abs(rl).max())
    M = np.array(rows)
    S = np.sqrt(x[0] * x[-1]); tau = np.sqrt(S)
    D = np.diag(tau ** (-np.arange(n + 1.0)))
    u, s, vt = np.linalg.svd(M @ D)
    b = D @ vt[-1]
    if b[-1] < 0 or (abs(b[-1]) < 1e-14 * np.abs(b).max() and b[-2] < 0):
        b = -b
    return b, s[-1] / s[0]


def check(x, n, Em, Ep, Om, Op, b, npts=20000):
    from sprcore import EO
    x = np.asarray(x, float)
    g = np.logspace(np.log10(x[0]) - 4, np.log10(x[-1]) + 4, npts)
    near = np.concatenate([xj * (1 + s * np.logspace(-8, -1, 60)) for xj in x for s in (-1, 1)])
    g = np.unique(np.concatenate([[0.0], g, near]))
    Eb, Ob = EO(b)
    Ebv, Obv = NP.polyval(g, Eb), NP.polyval(g, Ob)
    worst = {}
    for key, (E, O) in corners(Em, Ep, Om, Op).items():
        Ev, Ov = NP.polyval(g, E), NP.polyval(g, O)
        P = Ebv * Ev + g * Obv * Ov
        mag = np.sqrt(Ebv ** 2 + g * Obv ** 2) * np.sqrt(Ev ** 2 + g * Ov ** 2)
        rel = P / (mag + 1e-300)
        i = int(np.argmin(rel))
        worst[key] = (float(rel[i]), float(g[i]))
    return worst
