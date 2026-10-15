"""Core numerics for robust SPR synthesis over monic interval polynomial families.

Conventions (t = omega^2 >= 0):
  a polynomial with coefficients c[0..n] (c[k] multiplies s^k, c[n] = 1 for monic)
  satisfies a(j w) = E(t) + j w O(t) with
      E(t) = sum_l (-1)^l c[2l]   t^l,     O(t) = sum_l (-1)^l c[2l+1] t^l.
  For a box lo[k] <= c[k] <= hi[k] the pointwise extreme parts E-, E+, O-, O+ are the
  Kharitonov endpoint polynomials; for fixed numerator beta the worst member at every t
  is one of the four corners (E_i, O_j) (Lemma 2.2 of arXiv:2609.26541; elementary).

The synthesis margin of a box is
      tau*(box) = max_{beta monic, deg n} min_{t >= 0, corners} Re(beta(jw)/K(jw)).
A common SPR numerator exists iff tau* > 0 (a monic beta with all Re > 0 has min > 0 on
[0, inf] because Re -> 1 at infinity).  The LP below maximizes tau over a finite t-grid,
so tau_grid >= tau*; tau_grid < 0 already proves infeasibility (the grid problem is a
relaxation), and its dual gives a finite Gordan certificate.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as P
from scipy.optimize import linprog, minimize_scalar

CORNERS = [(0, 0), (0, 1), (1, 0), (1, 1)]  # (E index, O index); 0 = minus, 1 = plus


def endpoints(lo, hi):
    """Return E-, E+, O-, O+ as ascending coefficient arrays in t."""
    lo = np.asarray(lo, float)
    hi = np.asarray(hi, float)
    n = len(lo) - 1
    Em, Ep, Om, Op = [], [], [], []
    for k in range(n + 1):
        sgn = (-1) ** (k // 2)
        if sgn > 0:
            mn, mx = lo[k], hi[k]
        else:
            mn, mx = -hi[k], -lo[k]
        if k % 2 == 0:
            Em.append(mn)
            Ep.append(mx)
        else:
            Om.append(mn)
            Op.append(mx)
    return np.array(Em), np.array(Ep), np.array(Om), np.array(Op)


def corner_poly(E, O, n):
    """s-coefficients (ascending) of the polynomial with even part E and odd part O."""
    c = np.zeros(n + 1)
    for l, e in enumerate(E):
        if 2 * l <= n:
            c[2 * l] = (-1) ** l * e
    for l, o in enumerate(O):
        if 2 * l + 1 <= n:
            c[2 * l + 1] = (-1) ** l * o
    return c


def kharitonov(lo, hi):
    n = len(lo) - 1
    Em, Ep, Om, Op = endpoints(lo, hi)
    Es, Os = (Em, Ep), (Om, Op)
    return [corner_poly(Es[i], Os[j], n) for i, j in CORNERS]


def is_hurwitz(c, tol=0.0):
    """Numeric Hurwitz test via roots (c ascending)."""
    r = np.roots(np.asarray(c, float)[::-1])
    return bool(np.all(r.real < -tol))


def max_real_root(c):
    r = np.roots(np.asarray(c, float)[::-1])
    return float(np.max(r.real))


def box_is_stable(lo, hi):
    return all(is_hurwitz(k) for k in kharitonov(lo, hi))


def scaled_box(center, wlo, whi, lam):
    lo = np.array(center, float) - lam * np.asarray(wlo, float)
    hi = np.array(center, float) + lam * np.asarray(whi, float)
    return lo, hi


def stability_radius(center, wlo, whi, lam_hi=1e6, iters=60):
    """Largest lam with the box center +- lam*w robustly Hurwitz (bisection)."""
    if not box_is_stable(*scaled_box(center, wlo, whi, 0.0)):
        return 0.0
    lo_l, hi_l = 0.0, 1.0
    while box_is_stable(*scaled_box(center, wlo, whi, hi_l)):
        lo_l = hi_l
        hi_l *= 2.0
        if hi_l > lam_hi:
            return np.inf
    for _ in range(iters):
        mid = 0.5 * (lo_l + hi_l)
        if box_is_stable(*scaled_box(center, wlo, whi, mid)):
            lo_l = mid
        else:
            hi_l = mid
    return lo_l


def rows(t, E, O, n):
    """LP rows: value of Re((j w)^k / K(j w)) for k = 0..n at the points t (vectorized)."""
    t = np.atleast_1d(np.asarray(t, float))
    Ev = P.polyval(t, E)
    Ov = P.polyval(t, O)
    den = Ev * Ev + t * Ov * Ov
    R = np.empty((t.size, n + 1))
    for k in range(n + 1):
        l = k // 2
        if k % 2 == 0:
            R[:, k] = (-1) ** l * t ** l * Ev / den
        else:
            R[:, k] = (-1) ** l * t ** (l + 1) * Ov / den
    return R


def re_ratio(beta, t, E, O):
    """Re(beta(jw)/K(jw)) for beta ascending s-coefficients (length n+1)."""
    n = len(beta) - 1
    return rows(t, E, O, n) @ np.asarray(beta, float)


def corner_parts(lo, hi):
    Em, Ep, Om, Op = endpoints(lo, hi)
    Es, Os = (Em, Ep), (Om, Op)
    return [(Es[i], Os[j]) for i, j in CORNERS]


def special_points(lo, hi):
    """Positive real roots of the endpoint polynomials (band edges) and nearby points."""
    pts = []
    for poly in endpoints(lo, hi):
        if len(poly) > 1:
            r = P.polyroots(poly)
            for z in r:
                if abs(z.imag) < 1e-9 * (1 + abs(z.real)) and z.real > 0:
                    pts.append(z.real)
    pts = np.array(sorted(pts))
    extra = []
    for x in pts:
        extra.extend(x * (1 + np.array([-1e-3, -1e-5, 0, 1e-5, 1e-3])))
    return np.array(sorted(set(np.concatenate([pts, extra])) if len(pts) else []))


def solve_grid_lp(lo, hi, grid, tau_cap=1.0):
    """max tau s.t. Re(beta/K_c)(t) >= tau on the grid, beta monic. Returns dict."""
    n = len(lo) - 1
    blocks = []
    tags = []
    for ci, (E, O) in enumerate(corner_parts(lo, hi)):
        R = rows(grid, E, O, n)
        blocks.append(R)
        tags.extend([(ci, t) for t in grid])
    R = np.vstack(blocks)
    # scale rows for conditioning (does not change feasibility of Rb >= tau? it does change
    # tau-weighting); keep the unscaled rows so tau keeps the Re(beta/K) meaning.
    m = R.shape[0]
    # variables x = (beta_0..beta_{n-1}, tau); constraint: -R[:, :n] x_beta + tau <= R[:, n]
    A = np.hstack([-R[:, :n], np.ones((m, 1))])
    b = R[:, n]
    c = np.zeros(n + 1)
    c[-1] = -1.0
    bounds = [(None, None)] * n + [(None, tau_cap)]
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    if res.status != 0:
        return {"ok": False, "status": res.status, "message": res.message}
    beta = np.concatenate([res.x[:n], [1.0]])
    duals = -res.ineqlin.marginals  # y >= 0
    return {"ok": True, "tau": res.x[-1], "beta": beta, "duals": duals, "tags": tags}


def true_min(beta, lo, hi, tmin=1e-10, tmax=1e10, ngrid=20001):
    """Minimum over t in [0, inf) and the 4 corners of Re(beta/K), with local refinement."""
    grid = np.concatenate([[0.0], np.logspace(np.log10(tmin), np.log10(tmax), ngrid)])
    sp = special_points(lo, hi)
    if len(sp):
        grid = np.unique(np.concatenate([grid, sp]))
    best = (np.inf, None, None)
    worst_pts = []
    for ci, (E, O) in enumerate(corner_parts(lo, hi)):
        v = re_ratio(beta, grid, E, O)
        # local minima on the grid
        idx = np.where((v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
        idx = list(idx) + [0, len(grid) - 1]
        for i in idx:
            t0 = grid[i]
            val = v[i]
            if 0 < i < len(grid) - 1 and grid[i - 1] > 0:
                a, b = np.log(grid[i - 1]), np.log(grid[i + 1])
                f = lambda u: float(re_ratio(beta, np.exp(u), E, O)[0])
                r = minimize_scalar(f, bounds=(a, b), method="bounded",
                                    options={"xatol": 1e-13})
                if r.fun < val:
                    t0, val = float(np.exp(r.x)), float(r.fun)
            worst_pts.append((val, ci, t0))
            if val < best[0]:
                best = (val, ci, t0)
    worst_pts.sort()
    return best, worst_pts


def synthesis_margin(lo, hi, max_iter=40, tol=1e-10, verbose=False, grid0=None):
    """Exchange method for the semi-infinite LP. Returns (tau_grid, tau_true, beta, info)."""
    if grid0 is None:
        grid = np.concatenate([[0.0], np.logspace(-8, 8, 801)])
    else:
        grid = np.asarray(grid0, float)
    sp = special_points(lo, hi)
    if len(sp):
        grid = np.unique(np.concatenate([grid, sp]))
    hist = []
    for it in range(max_iter):
        sol = solve_grid_lp(lo, hi, grid)
        if not sol["ok"]:
            return None, None, None, {"error": sol}
        tau = sol["tau"]
        beta = sol["beta"]
        (mval, mci, mt), worst = true_min(beta, lo, hi)
        hist.append((it, tau, mval, len(grid)))
        if verbose:
            print(it, tau, mval, len(grid))
        if mval >= tau - tol * (1 + abs(tau)):
            return tau, mval, beta, {"grid": grid, "hist": hist, "sol": sol}
        new = [p[2] for p in worst if p[0] < tau - tol * (1 + abs(tau))][:50]
        grid = np.unique(np.concatenate([grid, new]))
    return tau, mval, beta, {"grid": grid, "hist": hist, "sol": sol, "maxiter": True}


def normalize_frequency(lo, hi):
    """Rescale s -> w0 s (monic) so that the center's constant term has modulus ~1."""
    n = len(lo) - 1
    c0 = 0.5 * (lo[0] + hi[0])
    w0 = c0 ** (1.0 / n) if c0 > 0 else 1.0
    k = np.arange(n + 1)
    f = w0 ** (k - n)
    return np.asarray(lo) * f, np.asarray(hi) * f, w0
