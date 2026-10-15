"""Scale-free angular synthesis margin for monic interval boxes.

delta*(box) = sup over real beta (deg <= n) of min over t >= 0 and the 4 Kharitonov
corners of (pi/2 - |arg(beta(jw)) - arg(K_c(jw))|).  A common SPR numerator exists iff
delta* > 0 (for exact degree n: a solution of degree < n can be perturbed by eps*s^n).

delta_win(box) = min over t of (pi - span(t))/2, where span(t) is the angular width of the
Kharitonov rectangle; delta* <= delta_win always.  rho = delta*/delta_win in (-inf, 1].

All quantities are computed on a finite t-grid, so delta*_grid >= delta* (relaxation).
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as P
from scipy.optimize import linprog

from sprlib import corner_parts, special_points


def default_grid(lo, hi, npts=1500, lo_exp=-7, hi_exp=7):
    g = np.concatenate([[0.0], np.logspace(lo_exp, hi_exp, npts)])
    sp = special_points(lo, hi)
    if len(sp):
        g = np.unique(np.concatenate([g, sp[sp > 0]]))
    return g


def corner_values(lo, hi, grid):
    """Complex K_c(jw) for the 4 corners on the grid, shape (4, m)."""
    w = np.sqrt(grid)
    out = []
    for E, O in corner_parts(lo, hi):
        out.append(P.polyval(grid, E) + 1j * w * P.polyval(grid, O))
    return np.array(out)


def basis_values(n, grid):
    """(j w)^k for k = 0..n, shape (n+1, m)."""
    w = np.sqrt(grid)
    return np.array([(1j * w) ** k for k in range(n + 1)])


def span_and_window(Kv):
    """Angular span of the rectangle at each grid point and window half-width."""
    ref = np.angle(Kv.mean(axis=0))  # center direction (rectangle excludes 0)
    rel = np.angle(Kv * np.exp(-1j * ref)[None, :])
    span = rel.max(axis=0) - rel.min(axis=0)
    return span, (np.pi - span) / 2.0


def feasible_at(delta, Kv, Bv, norm):
    """LP: max s s.t. Re(beta conj(K e^{+-j delta}))/norm >= s, |beta_k| <= 1."""
    n1 = Bv.shape[0]
    rows = []
    for sgn in (+1.0, -1.0):
        Kr = Kv * np.exp(1j * sgn * delta)
        # Re(beta(jw) * conj(Kr)) = sum_k beta_k Re(B_k conj(Kr))
        R = np.real(Bv[None, :, :] * np.conj(Kr)[:, None, :])  # (4, n+1, m)
        R = R / norm[:, None, :]
        rows.append(np.transpose(R, (0, 2, 1)).reshape(-1, n1))
    R = np.vstack(rows)
    m = R.shape[0]
    A = np.hstack([-R, np.ones((m, 1))])
    b = np.zeros(m)
    c = np.zeros(n1 + 1)
    c[-1] = -1.0
    bounds = [(-1.0, 1.0)] * n1 + [(None, 1.0)]
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    if res.status != 0:
        return 0.0, None
    return res.x[-1], res.x[:n1]


def delta_star(lo, hi, grid=None, tol=1e-6, return_beta=False):
    n = len(lo) - 1
    if grid is None:
        grid = default_grid(lo, hi)
    Kv = corner_values(lo, hi, grid)
    Bv = basis_values(n, grid)
    # per-corner normalization: rows become |beta(jw)| cos(angle -+ delta) / (1+t)^(n/2),
    # independent of the size of each corner value (a vanishing corner is not down-weighted)
    norm = np.abs(Kv) * (1.0 + grid)[None, :] ** (n / 2.0)
    span, win = span_and_window(Kv)
    dwin = float(win.min())
    s0, b0 = feasible_at(0.0, Kv, Bv, norm)
    if s0 <= 1e-12:
        out = (-1.0, dwin, None)  # infeasible on the grid at delta = 0
        return out if return_beta else out[:2]
    lo_d, hi_d, best = 0.0, max(dwin, 1e-12) * 1.0000001, b0
    while hi_d - lo_d > tol * max(dwin, 1e-12):
        mid = 0.5 * (lo_d + hi_d)
        s, b = feasible_at(mid, Kv, Bv, norm)
        if s > 1e-12:
            lo_d, best = mid, b
        else:
            hi_d = mid
    out = (lo_d, dwin, best)
    return out if return_beta else out[:2]


def actual_slack(beta, lo, hi, grid):
    """Exact (grid) angular slack of a given beta: min_t,c (pi/2 - |arg beta - arg K_c|)."""
    n = len(lo) - 1
    Kv = corner_values(lo, hi, grid)
    Bv = basis_values(n, grid)
    bv = (np.asarray(beta)[:, None] * Bv).sum(axis=0)
    ang = np.abs(np.angle(bv[None, :] * np.conj(Kv)))
    sl = np.pi / 2 - ang
    i = np.unravel_index(np.argmin(sl), sl.shape)
    return float(sl[i]), int(i[0]), float(grid[i[1]])
