"""Locate the first failing shrink factor theta* of the G1 generalized family (n=6) and extract
the near-critical weak numerator's contact structure (corners, frequencies, regions, b-quadrant
indices), to compare with the census configurations.  Float, exploratory.
"""
from __future__ import annotations

import json

import numpy as np
from numpy.polynomial import polynomial as NP
from scipy.optimize import linprog

from closed_exact import fq, band_roots, xpoly
from strict_exact import shrink


def to_float(p):
    return np.array([float(p[i]) for i in range(p.degree() + 1)])


def rows(Em, Ep, Om, Op, n, grid):
    out, lab = [], []
    tau = np.sqrt(np.sqrt(max(grid[1], 1e-9) * grid[-1]))
    D = tau ** (-np.arange(n + 1.0))
    for key, (E, O) in {'--': (Em, Om), '-+': (Em, Op), '+-': (Ep, Om), '++': (Ep, Op)}.items():
        Ev, Ov = NP.polyval(grid, E), NP.polyval(grid, O)
        M = np.empty((grid.size, n + 1))
        for k in range(n + 1):
            l = k // 2
            M[:, k] = (-1) ** l * grid ** l * (Ev if k % 2 == 0 else grid * Ov)
        M = M * D
        nr = np.linalg.norm(M, axis=1)
        out.append(M / nr[:, None]); lab += [(key, t) for t in grid]
    return np.vstack(out), lab, D


def margin(R):
    Q, T = np.linalg.qr(R)
    Qn = Q / np.linalg.norm(Q, axis=1, keepdims=True)
    m, d = Qn.shape
    res = linprog(np.r_[np.zeros(d), -1.0], A_ub=np.hstack([-Qn, np.ones((m, 1))]),
                  b_ub=np.zeros(m), bounds=[(-1, 1)] * d + [(None, 1.0)], method='highs')
    return res.x[-1], np.linalg.solve(T, res.x[:-1])


def main():
    spec = json.load(open('../evidence/genrect/spec_n6_gen_s21.json'))
    n = 6
    x = [fq(v) for v in spec['x']]; L = [fq(v) for v in spec['leads']]
    Er, Epr, Or, Opr = band_roots(x, n)
    base = (xpoly(Er, L[0]), xpoly(Epr, L[1]), xpoly(Or, L[2]), xpoly(Opr, L[3]))
    grid = np.unique(np.concatenate([[0.0], np.logspace(-3, 4, 6000),
                                     np.linspace(19, 23, 4000)]))
    lo, hi = 0.9, 0.999
    for _ in range(30):
        th = 0.5 * (lo + hi)
        Em, Ep, Om, Op = [to_float(p) for p in shrink(*base, fq(str(th)))]
        R, lab, D = rows(Em, Ep, Om, Op, n, grid)
        m, y = margin(R)
        if m > 1e-9:
            lo = th
        else:
            hi = th
    th = lo
    Em, Ep, Om, Op = [to_float(p) for p in shrink(*base, fq(str(th)))]
    R, lab, D = rows(Em, Ep, Om, Op, n, grid)
    m, y = margin(R)
    b = D * y          # rows were built in scaled coordinates b_k = D_k * y_k
    contacts = []
    from sprcore import EO
    Eb, Ob = EO(b)
    fine = np.unique(np.concatenate([np.logspace(-3, 4, 200000), np.linspace(19, 23, 200000)]))
    Ebv, Obv = NP.polyval(fine, Eb), NP.polyval(fine, Ob)
    mb = np.sqrt(Ebv ** 2 + fine * Obv ** 2)
    for key, (E, O) in {'--': (Em, Om), '-+': (Em, Op), '+-': (Ep, Om), '++': (Ep, Op)}.items():
        Ev, Ov = NP.polyval(fine, E), NP.polyval(fine, O)
        c = (Ebv * Ev + fine * Obv * Ov) / (mb * np.sqrt(Ev ** 2 + fine * Ov ** 2))
        for i in range(1, fine.size - 1):
            if c[i] <= c[i - 1] and c[i] <= c[i + 1] and c[i] < 2e-3:
                q = int(np.floor(2 * np.unwrap(np.arctan2(fine[:i + 1] ** 0.5 * Obv[:i + 1],
                                                         Ebv[:i + 1]))[-1] / np.pi))
                contacts.append((float(fine[i]), key, float(c[i]), q))
    contacts.sort()
    xf = [float(v) for v in x]
    print('theta* ~', th, 'margin', m)
    print('band points', np.round(xf, 4))
    for t, key, c, q in contacts:
        print(f'  t={t:.5f} corner {key} cos={c:.2e} b-quadrant {q}')
    json.dump({'theta_star': th, 'contacts': contacts, 'b': b.tolist(), 'x': xf},
              open('../evidence/genrect/g1_critical.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
