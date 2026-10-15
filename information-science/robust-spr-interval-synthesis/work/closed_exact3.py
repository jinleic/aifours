"""High-precision re-test of one fully-closed marginal box: reduce the closed problem to the
3-dimensional space of numerators satisfying the n-2 exact double contacts, then decide
whether some nonzero beta in that space has P_c >= 0 for all corners on a fine t-grid.

Usage: python closed_exact3.py RECORDS.jsonl N IT [DPS]
Reads the record with field it == IT from RECORDS.jsonl (written by closed_mcmc.py).
Prints: realizability check, band ordering, contact-matrix rank, and
    m* = max over unit lambda in R^3 of min over (t, c) of the unit-normalized rows,
by (i) LP with |lambda_k| <= 1 and (ii) a dense sphere scan with local refinement.
m* < 0 means the closed problem is infeasible on the grid (=> closed-infeasible, since the grid
problem is a relaxation), m* >= 0 means grid-feasible.
"""
from __future__ import annotations

import json
import sys

import mpmath as mp
import numpy as np
from scipy.optimize import linprog, minimize

from closed_limit import band_roots, parts_degrees


def decode_mp(u, n):
    inc = [mp.e ** mp.mpf(min(max(v, -6.0), 2.3)) for v in u[:n - 1]]
    x = [mp.mpf(1)]
    for d in inc:
        x.append(x[-1] * (1 + d))
    g = mp.e ** (mp.fsum([mp.log(v) for v in x]) / len(x))
    x = [v / g for v in x]
    llo = mp.e ** mp.mpf(min(max(u[n - 1], -6.0), 6.0))
    lhi = llo * (1 + mp.e ** mp.mpf(min(max(u[n], -8.0), 4.0)))
    return x, llo, lhi


def poly_from_roots(roots, lead):
    c = [mp.mpf(1)]
    for r in roots:
        new = [mp.mpf(0)] * (len(c) + 1)
        for i, a in enumerate(c):
            new[i + 1] += a
            new[i] -= r * a
        c = new
    return [lead * a for a in c]


def endpoints_mp(x, n, llo, lhi):
    DE, DO = parts_degrees(n)
    Em, Ep, Om, Op = band_roots(x, n)
    if n % 2 == 0:
        sE, sO = (-1) ** DE, (-1) ** DO
        E = (poly_from_roots(Em, sE), poly_from_roots(Ep, sE))
        if DO % 2 == 0:
            O = (poly_from_roots(Om, sO * llo), poly_from_roots(Op, sO * lhi))
        else:
            O = (poly_from_roots(Om, sO * lhi), poly_from_roots(Op, sO * llo))
    else:
        sO, sE = (-1) ** DO, (-1) ** DE
        O = (poly_from_roots(Om, sO), poly_from_roots(Op, sO))
        if DE % 2 == 0:
            E = (poly_from_roots(Em, sE * llo), poly_from_roots(Ep, sE * lhi))
        else:
            E = (poly_from_roots(Em, sE * lhi), poly_from_roots(Ep, sE * llo))
    return E, O


def pval(c, t):
    return mp.polyval(list(reversed(c)), t)


def pder(c):
    return [k * c[k] for k in range(1, len(c))]


def basis_row(n, t, Ev, Ov):
    r = []
    for k in range(n + 1):
        l = k // 2
        if k % 2 == 0:
            r.append((-1) ** l * t ** l * Ev)
        else:
            r.append((-1) ** l * t ** (l + 1) * Ov)
    return r


def main():
    path, n, it = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    mp.mp.dps = int(sys.argv[4]) if len(sys.argv) > 4 else 60
    rec = next(json.loads(l) for l in open(path) if json.loads(l)["it"] == it)
    x, llo, lhi = decode_mp(rec["u"], n)
    (Em, Ep), (Om, Op) = endpoints_mp(x, n, llo, lhi)
    dE = [b - a for a, b in zip(Em, Ep)]
    dO = [b - a for a, b in zip(Om, Op)]
    print("min width E:", mp.nstr(min(dE[:-1] if n % 2 == 0 else dE), 5),
          " min width O:", mp.nstr(min(dO if n % 2 == 0 else dO[:-1]), 5))
    print("x:", [mp.nstr(v, 8) for v in x])
    # contact equations
    Es, Os = (Em, Ep), (Om, Op)
    C = []
    for xi in x[1:n - 1]:
        ie = min((0, 1), key=lambda i: abs(pval(Es[i], xi)))
        io = min((0, 1), key=lambda i: abs(pval(Os[i], xi)))
        assert abs(pval(Es[ie], xi)) < mp.mpf(10) ** (-mp.mp.dps // 2)
        assert abs(pval(Os[io], xi)) < mp.mpf(10) ** (-mp.mp.dps // 2)
        row = basis_row(n, xi, pval(pder(Es[ie]), xi), pval(pder(Os[io]), xi))
        nr = mp.sqrt(mp.fsum([v * v for v in row]))
        C.append([v / nr for v in row])
    Cm = mp.matrix(C)
    U, S, V = mp.svd_r(Cm, full_matrices=True)
    print("contact singular values:", [mp.nstr(S[i], 5) for i in range(len(S))])
    null = [[V[r, c] for c in range(n + 1)] for r in range(n - 2, n + 1)]  # last 3 rows of V
    # residual check
    for vec in null:
        res = max(abs(mp.fsum([C[i][k] * vec[k] for k in range(n + 1)])) for i in range(n - 2))
        assert res < mp.mpf(10) ** (-mp.mp.dps // 2), res
    # grid
    lx = [mp.log10(v) for v in x]
    ts = [mp.mpf(10) ** (lx[0] - 3 + (lx[-1] - lx[0] + 6) * mp.mpf(i) / 3999) for i in range(4000)]
    for xi in x:
        for d in [1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 1e-6]:
            ts += [xi * (1 - mp.mpf(d)), xi * (1 + mp.mpf(d))]
    ts = [mp.mpf(0)] + sorted(ts)
    rows = []
    for t in ts:
        for i in (0, 1):
            for j in (0, 1):
                Ev, Ov = pval(Es[i], t), pval(Os[j], t)
                den = Ev * Ev + t * Ov * Ov
                if den == 0:
                    continue
                b = basis_row(n, t, Ev, Ov)
                r = [mp.fsum([b[k] * vec[k] for k in range(n + 1)]) / den for vec in null]
                nr = mp.sqrt(mp.fsum([v * v for v in r]))
                if nr > 0:
                    rows.append([float(v / nr) for v in r])
    R = np.array(rows)
    print("rows:", R.shape)
    # (i) LP: max s s.t. R lam >= s, |lam| <= 1
    res = linprog([0, 0, 0, -1], A_ub=np.hstack([-R, np.ones((len(R), 1))]), b_ub=np.zeros(len(R)),
                  bounds=[(-1, 1)] * 3 + [(None, 1)], method="highs")
    print("LP max-min (box-normalized):", res.x[-1], "lambda:", res.x[:3])
    # (ii) sphere scan of f(lam) = min R lam on the unit sphere
    th = np.linspace(0, np.pi, 361)
    ph = np.linspace(0, 2 * np.pi, 721)
    T, Ph = np.meshgrid(th, ph, indexing="ij")
    L = np.stack([np.sin(T) * np.cos(Ph), np.sin(T) * np.sin(Ph), np.cos(T)], -1).reshape(-1, 3)
    f = (L @ R.T).min(axis=1)
    k = int(np.argmax(f))
    best = (f[k], L[k])
    def negf(v):
        v = v / np.linalg.norm(v)
        return -float((R @ v).min())
    r2 = minimize(negf, L[k], method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14,
                                                             "maxiter": 20000})
    print("sphere max of min-row: grid %.6e  refined %.6e" % (best[0], -r2.fun))
    lam = r2.x / np.linalg.norm(r2.x)
    beta = [mp.fsum([lam[q] * null[q][k] for q in range(3)]) for k in range(n + 1)]
    print("best beta (normalized):", [mp.nstr(v, 6) for v in beta])


if __name__ == "__main__":
    main()
