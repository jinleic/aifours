"""Experiment CRS (exploratory, float): direct search for Theorem-J critical data of alternative
(A) in a monic interval box: numerator b (deg <= n), m = n+1 nodes t_1 < ... < t_m > 0, the
touching corner at each node = anti-corner of b (signs of E_b, O_b), DOUBLE contacts
P_{c_i,b}(t_i) = P'_{c_i,b}(t_i) = 0, alternating orientation, P_{c,b} >= 0 for all corners on a
grid, box widths >= 0 and the box robustly stable.  Given (b, nodes) the 2m contact equations
are LINEAR in the box (lower/upper coefficient vectors), solved by least squares.

A zero objective with stable box would be a candidate counterexample (to be certified
exactly); positive minima are only search evidence.

Usage: python crs.py N SEED RESTARTS FEVALS OUT.json
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from sprcore import EO, lambda_stab


def comp_matrix(n):
    """For each coefficient index k of the monic box (k = 0..n-1, s^k), whether it belongs to
    E (k even) or O (k odd) and its sign in the t-component: (-1)^(k//2)."""
    return [((k % 2), (-1) ** (k // 2)) for k in range(n)]


def endpoint_rows(n, t, which_E, which_O):
    """Linear forms (in z = (lo[0..n-1], hi[0..n-1])) giving E_x(t), E_x'(t), O_y(t), O_y'(t)
    for x = which_E in {'-','+'}, y = which_O, plus the constant (monic) parts."""
    zE = np.zeros(2 * n); zEd = np.zeros(2 * n); zO = np.zeros(2 * n); zOd = np.zeros(2 * n)
    cE = cEd = cO = cOd = 0.0
    for k in range(n + 1):
        l = k // 2
        sgn = (-1) ** l
        val, der = t ** l, (l * t ** (l - 1) if l > 0 else 0.0)
        if k == n:   # monic coefficient 1
            if k % 2 == 0:
                cE += sgn * val; cEd += sgn * der
            else:
                cO += sgn * val; cOd += sgn * der
            continue
        # E- takes lo where sgn > 0 else hi; E+ the opposite
        if k % 2 == 0:
            want = which_E
            use_lo = (sgn > 0) == (want == '-')
            idx = k if use_lo else n + k
            zE[idx] += sgn * val; zEd[idx] += sgn * der
        else:
            want = which_O
            use_lo = (sgn > 0) == (want == '-')
            idx = k if use_lo else n + k
            zO[idx] += sgn * val; zOd[idx] += sgn * der
    return (zE, cE), (zEd, cEd), (zO, cO), (zOd, cOd)


def solve_box(b, ts, n):
    Eb, Ob = EO(b)
    dEb, dOb = NP.polyder(Eb), NP.polyder(Ob)
    A, rhs, corners, scales = [], [], [], []
    for t in ts:
        e, o = NP.polyval(t, Eb), NP.polyval(t, Ob)
        de, do = NP.polyval(t, dEb), NP.polyval(t, dOb)
        cx = '-' if e > 0 else '+'
        cy = '-' if o > 0 else '+'
        corners.append(cx + cy)
        (zE, cE), (zEd, cEd), (zO, cO), (zOd, cOd) = endpoint_rows(n, t, cx, cy)
        # P = e*E + t*o*O ;  P' = de*E + e*E' + o*O + t*do*O + t*o*O'
        r1 = e * zE + t * o * zO
        c1 = e * cE + t * o * cO
        r2 = de * zE + e * zEd + o * zO + t * do * zO + t * o * zOd
        c2 = de * cE + e * cEd + o * cO + t * do * cO + t * o * cOd
        s1 = np.abs(r1).max() + abs(c1) + 1e-300
        s2 = np.abs(r2).max() + abs(c2) + 1e-300
        A += [r1 / s1, r2 / s2]; rhs += [-c1 / s1, -c2 / s2]
    A = np.array(A); rhs = np.array(rhs)
    z, res, rk, sv = np.linalg.lstsq(A, rhs, rcond=None)
    r = A @ z - rhs
    return z[:n], z[n:], float(np.linalg.norm(r) / np.sqrt(len(r))), corners


def orientation(b, a, t):
    Eb, Ob = EO(b); Ea, Oa = EO(a)
    return np.sign(NP.polyval(t, Ob) * NP.polyval(t, Ea) - NP.polyval(t, Eb) * NP.polyval(t, Oa))


def objective(p, n, grid, detail=False):
    m = n + 1
    b = p[:n + 1].copy()
    nb = np.linalg.norm(b)
    if nb == 0:
        return 10.0, None
    b /= nb
    ts = np.exp(np.cumsum(np.concatenate([[p[n + 1]], np.exp(np.clip(p[n + 2:], -10, 3))])))
    lo, hi, res, corners = solve_box(b, ts, n)
    pen = 0.0
    w = hi - lo
    sc = np.abs(np.concatenate([lo, hi])).max() + 1e-300
    pen += np.sum(np.maximum(0.0, -w)) / sc
    pen += np.sum(np.maximum(0.0, -lo)) / sc     # Hurwitz needs positive coefficients
    lam = lambda_stab(np.minimum(lo, hi), np.maximum(lo, hi), tgrid=grid[1:]) if pen == 0 else 0.0
    pen += max(0.0, 1.02 - lam)
    # global weak positivity on grid, normalised
    if pen == 0:
        from sprcore import corner_polys, pairing
        cps = corner_polys(lo, hi)
        worst = 0.0
        for c in cps.values():
            P = pairing(b, c)
            Pv = NP.polyval(grid, P)
            Ev, Ov = EO(c)
            mag = np.sqrt(NP.polyval(grid, Ev) ** 2 + grid * NP.polyval(grid, Ov) ** 2)
            Ebv, Obv = EO(b)
            magb = np.sqrt(NP.polyval(grid, Ebv) ** 2 + grid * NP.polyval(grid, Obv) ** 2)
            worst = min(worst, float(np.min(Pv / (mag * magb + 1e-300))))
        pen += -worst
        # alternation of orientation
        sig = []
        for t, key in zip(ts, corners):
            c = cps[key]
            sig.append(orientation(b, c, t))
        alt = sum(1 for a1, a2 in zip(sig, sig[1:]) if a1 == a2)
        pen += 0.1 * alt
    val = res + pen
    if detail:
        return val, {'b': b.tolist(), 'ts': ts.tolist(), 'lo': lo.tolist(), 'hi': hi.tolist(),
                     'residual': res, 'penalty': pen, 'corners': corners, 'lam': lam}
    return val, None


def main():
    n = int(sys.argv[1]); seed = int(sys.argv[2]); restarts = int(sys.argv[3])
    fevals = int(sys.argv[4]); out = sys.argv[5]
    import cma
    rng = np.random.default_rng(seed)
    grid = np.concatenate([[0.0], np.logspace(-4, 4, 1200)])
    runs = []
    best = (np.inf, None)
    for r in range(restarts):
        # start: b = a random Hurwitz polynomial, nodes spread log-uniformly
        roots = []
        for _ in range(n // 2):
            a, wv = np.exp(rng.normal(-1, 1)), np.exp(rng.normal(0, 1))
            roots += [-a + 1j * wv, -a - 1j * wv]
        if n % 2:
            roots.append(-np.exp(rng.normal(0, 1)))
        b0 = np.real(NP.polyfromroots(roots))
        p0 = np.concatenate([b0 / np.linalg.norm(b0), [rng.normal(-2, 1)],
                             rng.normal(-0.5, 0.5, n)])
        es = cma.CMAEvolutionStrategy(p0, 0.3, {'seed': seed * 100 + r, 'maxfevals': fevals,
                                                'verbose': -9})
        es.optimize(lambda q: objective(q, n, grid)[0])
        val, info = objective(es.result.xbest, n, grid, detail=True)
        runs.append({'restart': r, 'value': val, 'info': info})
        if val < best[0]:
            best = (val, info)
        json.dump({'n': n, 'seed': seed, 'fevals': fevals, 'best_value': best[0],
                   'best': best[1], 'runs': runs}, open(out, 'w'), indent=1)
    print(n, seed, 'best', best[0], [round(rr['value'], 6) for rr in runs])


if __name__ == '__main__':
    main()
