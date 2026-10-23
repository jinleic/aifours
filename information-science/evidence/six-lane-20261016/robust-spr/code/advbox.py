"""Experiment A1p (exploratory, float): adversarial search over GENERAL monic interval boxes
(not only fully closed) at a fixed radial stability factor lam_stab = 1 + eta, minimising the
signed angular SPR margin delta*(K) computed by LP bisection on a frequency grid.

delta*(K) = sup{delta : exists real b, deg b <= n, with |arg b(iw) - arg c(iw)| <= pi/2 - delta
             for every grid frequency and every Kharitonov corner c}.
The grid is a relaxation: a NEGATIVE grid value certifies (up to LP float accuracy) that no
common numerator exists for that box; positive values are only grid evidence.
Calibration: n = 5, 6 boxes are claimed synthesizable (2026 preprints) -> must stay >= 0.

Box parametrisation: centre = monic polynomial from roots (log-damping, log-frequency params),
radii direction r = exp(params) * |centre coeff|; then radii scaled so lam_stab == 1 + eta.

Usage: python advbox.py N ETA SEED RESTARTS FEVALS OUT.json
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP
from scipy.optimize import linprog

from sprcore import EO, corner_polys, lambda_stab


def centre_from_params(p, n):
    """Monic Hurwitz polynomial from params: for each complex pair (log omega, damping-ratio
    logit) with damping ratio zeta in (0.01, 0.99); log alpha for a real root when n is odd."""
    roots = []
    k = 0
    for _ in range(n // 2):
        w = np.exp(p[k]); z = 0.01 + 0.98 / (1.0 + np.exp(-p[k + 1])); k += 2
        a = z * w / np.sqrt(1 - z * z)
        roots += [-a + 1j * w, -a - 1j * w]
    if n % 2 == 1:
        roots.append(-np.exp(p[k])); k += 1
    c = np.real(NP.polyfromroots(roots))
    return c, k


def corners_hurwitz(lo, hi):
    for c in corner_polys(lo, hi).values():
        if np.max(np.roots(c[::-1]).real) >= 0:
            return False
    return True


def lam_stab_exact(c, dirn, n, iters=50):
    """sup{lam : corners of c +- lam*dirn are Hurwitz} by bisection on corner roots (float)."""
    lo_l, hi_l = 0.0, 1.0
    while corners_hurwitz(c[:n] - hi_l * dirn, c[:n] + hi_l * dirn):
        hi_l *= 2.0
        if hi_l > 1e12:
            return np.inf
    for _ in range(iters):
        m = 0.5 * (lo_l + hi_l)
        if corners_hurwitz(c[:n] - m * dirn, c[:n] + m * dirn):
            lo_l = m
        else:
            hi_l = m
    return lo_l


def box_from_params(p, n, eta):
    c, k = centre_from_params(p, n)
    dirn = np.exp(np.clip(p[k:k + n], -30, 30)) * np.abs(c[:n])
    lam = lam_stab_exact(c, dirn, n)
    if not np.isfinite(lam) or lam <= 0:
        return None
    s = lam / (1.0 + eta)
    r = dirn * s
    return c[:n] - r, c[:n] + r


def adaptive_grid(lo, hi, base=900):
    g = [np.concatenate([[0.0], np.logspace(-5, 5, base)])]
    for c in corner_polys(lo, hi).values():
        for z in np.roots(c[::-1]):
            if z.imag > 0:
                w, a = z.imag, -z.real
                ks = np.linspace(-12, 12, 49)
                ww = w + ks * a
                g.append(ww[ww > 0] ** 2)
    return np.unique(np.concatenate(g))


def rows_for(lo, hi, grid, delta, n):
    cps = corner_polys(lo, hi)
    R = []
    tau = np.sqrt(np.sqrt(grid[1] * grid[-1]))
    D = tau ** (-np.arange(n + 1.0))
    w = np.sqrt(grid)
    for c in cps.values():
        Ec, Oc = EO(c)
        Ev = NP.polyval(grid, Ec); Ov = NP.polyval(grid, Oc)
        for sgn in (1.0, -1.0):
            # rotate corner value z = Ev + i w Ov by e^{i sgn delta}
            zr = Ev * np.cos(sgn * delta) - w * Ov * np.sin(sgn * delta)
            zi = Ev * np.sin(sgn * delta) + w * Ov * np.cos(sgn * delta)
            # Re(b conj z) = E_b zr + w O_b zi ; express in b coefficients
            M = np.empty((grid.size, n + 1))
            for k in range(n + 1):
                l = k // 2
                if k % 2 == 0:
                    M[:, k] = (-1) ** l * grid ** l * zr
                else:
                    M[:, k] = (-1) ** l * grid ** l * w * zi
            M = M * D
            nr = np.linalg.norm(M, axis=1)
            ok = nr > 0
            R.append(M[ok] / nr[ok][:, None])
    return np.vstack(R)


def feasible(lo, hi, grid, delta, n):
    R = rows_for(lo, hi, grid, delta, n)
    m, d = R.shape
    Aub = np.hstack([-R, np.ones((m, 1))])
    c = np.zeros(d + 1); c[-1] = -1
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(m), bounds=[(-1, 1)] * d + [(None, 1.0)],
                  method='highs')
    return res.status == 0 and res.x[-1] > 1e-9



def precond_margin(lo, hi, n, grid=None, delta=0.0):
    """LP margin after QR preconditioning of the constraint matrix (rows unit-normalised,
    then b = T^{-1} y with R = Q T).  Positivity of the max-min margin is invariant under the
    change of variables; the preconditioned value is well scaled.  Returns (margin, b)."""
    if grid is None:
        grid = adaptive_grid(lo, hi, base=2000)
    R = rows_for(lo, hi, grid, delta, n)
    Q, T = np.linalg.qr(R)
    Qn = Q / np.linalg.norm(Q, axis=1, keepdims=True)
    m, d = Qn.shape
    Aub = np.hstack([-Qn, np.ones((m, 1))])
    c = np.zeros(d + 1); c[-1] = -1
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(m), bounds=[(-1, 1)] * d + [(None, 1.0)],
                  method='highs')
    if res.status != 0:
        return None, None
    y = res.x[:-1]
    return float(res.x[-1]), np.linalg.solve(T, y)

def delta_star(lo, hi, n, grid=None, tol=2e-4):
    """Bisection on delta in [0, pi/2].  Returns -1.0 if the box is grid-INFEASIBLE already at
    delta = 0 (no common numerator on the grid: candidate counterexample)."""
    if grid is None:
        grid = adaptive_grid(lo, hi)
    if not corners_hurwitz(lo, hi):
        return 5.0   # not a stable box: excluded (should not happen after scaling)
    a, b = 0.0, np.pi / 2
    if not feasible(lo, hi, grid, a, n):
        return -1.0
    while b - a > tol:
        m = 0.5 * (a + b)
        if feasible(lo, hi, grid, m, n):
            a = m
        else:
            b = m
    return a


def main():
    n = int(sys.argv[1]); eta = float(sys.argv[2]); seed = int(sys.argv[3])
    restarts = int(sys.argv[4]); fevals = int(sys.argv[5]); out = sys.argv[6]
    import cma
    rng = np.random.default_rng(seed)
    npar = 2 * (n // 2) + (n % 2) + n
    best = (np.inf, None)
    runs = []

    def f(p):
        bx = box_from_params(p, n, eta)
        if bx is None:
            return 10.0
        lo, hi = bx
        # frequency normalisation: centre roots are O(1) by parametrisation clipping
        return delta_star(lo, hi, n)

    # bounded, well-conditioned parameter ranges: pair frequencies in [0.1, 10], damping ratio
    # >= ~0.056, real root in [0.1, 10], radii directions in [e^-5, e^1] relative to |coeff|
    lb, ub = [], []
    for _ in range(n // 2):
        lb += [-2.3, -3.0]; ub += [2.3, 6.0]
    if n % 2:
        lb += [-2.3]; ub += [2.3]
    lb += [-5.0] * n; ub += [1.0] * n
    for r in range(restarts):
        p0 = np.concatenate([rng.uniform(np.array(lb[:npar - n]) * 0.5, np.array(ub[:npar - n]) * 0.5),
                             rng.uniform(-3.0, 0.0, n)])
        es = cma.CMAEvolutionStrategy(p0, 0.8, {'seed': seed * 100 + r, 'maxfevals': fevals,
                                                'verbose': -9, 'bounds': [lb, ub]})
        es.optimize(f)
        pb = es.result.xbest
        val = es.result.fbest
        bx = box_from_params(pb, n, eta)
        rec = {'restart': r, 'delta_star': float(val), 'p': pb.tolist(),
               'lo': bx[0].tolist() if bx else None, 'hi': bx[1].tolist() if bx else None}
        runs.append(rec)
        if val < best[0]:
            best = (float(val), rec)
        json.dump({'n': n, 'eta': eta, 'seed': seed, 'fevals': fevals, 'best': best[1],
                   'best_delta': best[0], 'runs': runs}, open(out, 'w'), indent=1)
    print(n, eta, seed, 'best delta*', best[0], [round(rr['delta_star'], 5) for rr in runs])


if __name__ == '__main__':
    main()
