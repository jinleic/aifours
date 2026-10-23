"""Fully-closed (all n-2 gaps closed) monic boxes: construction, realizability, contact kernel,
closed feasibility LP restricted to the kernel.  Float exploration only (no certificates).

Band rule (prior dossier Prop. D): points x_0 < ... < x_{n-1}; E-band k = [x_{2k-2}, x_{2k-1}],
O-band k = [x_{2k-1}, x_{2k}]; E- vanishes at the left end of odd E-bands and the right end of
even ones, E+ at the other ends; same for O-, O+.
Components are written as  C(t) = lead * prod (x_r - t)  so that C(0) > 0 for lead > 0.
Monic: for n odd the O components have lead 1 (O_p = -t^D + ..., D = (n-1)/2 odd... we use the
(x - t) form, whose leading coefficient is (-1)^deg, matching sign of a Hurwitz component).
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as NP
from scipy.optimize import linprog

from sprcore import EO, from_EO


def degs(n):
    return n // 2, (n - 1) // 2


def band_roots(x, n):
    DE, DO = degs(n)
    Em, Ep, Om, Op = [], [], [], []
    for k in range(1, DE + 1):
        L, R = x[2 * k - 2], x[2 * k - 1]
        if k % 2 == 1:
            Em.append(L); Ep.append(R)
        else:
            Ep.append(L); Em.append(R)
    for k in range(1, DO + 1):
        L, R = x[2 * k - 1], x[2 * k]
        if k % 2 == 1:
            Om.append(L); Op.append(R)
        else:
            Op.append(L); Om.append(R)
    return Em, Ep, Om, Op


def xpoly(roots, lead):
    """lead * prod (r - t), ascending in t."""
    p = np.array([float(lead)])
    for r in roots:
        p = NP.polymul(p, np.array([r, -1.0]))
    return p


def endpoints(x, n, lam_m, lam_p):
    """Endpoint components for points x.  The free leading coefficient belongs to E when n is
    odd (E lead = a_1, O lead = 1) and to O when n is even (O lead = a_1, E lead = 1).
    lam_m, lam_p: leads of the '-' and '+' endpoints of the free component (positive)."""
    Em, Ep, Om, Op = band_roots(x, n)
    if n % 2 == 1:
        return xpoly(Em, lam_m), xpoly(Ep, lam_p), xpoly(Om, 1.0), xpoly(Op, 1.0)
    return xpoly(Em, 1.0), xpoly(Ep, 1.0), xpoly(Om, lam_m), xpoly(Op, lam_p)


def widths(Em, Ep, Om, Op):
    return NP.polysub(Ep, Em), NP.polysub(Op, Om)


def realizable(Em, Ep, Om, Op, tol=1e-12):
    dE, dO = widths(Em, Ep, Om, Op)
    sc = max(np.abs(np.concatenate([Em, Ep, Om, Op])).max(), 1.0)
    return bool(np.all(dE >= -tol * sc) and np.all(dO >= -tol * sc))


def corners(Em, Ep, Om, Op):
    return {'--': (Em, Om), '-+': (Em, Op), '+-': (Ep, Om), '++': (Ep, Op)}


def touching(x, n, Em, Ep, Om, Op):
    """For each interior x_j return (key of touching corner, r_j = x O'/E')."""
    out = []
    E = {'-': Em, '+': Ep}
    O = {'-': Om, '+': Op}
    for xj in x[1:n - 1]:
        ke = min(E, key=lambda k: abs(NP.polyval(xj, E[k])))
        ko = min(O, key=lambda k: abs(NP.polyval(xj, O[k])))
        dE = NP.polyval(xj, NP.polyder(E[ke]))
        dO = NP.polyval(xj, NP.polyder(O[ko]))
        out.append((ke + ko, xj * dO / dE))
    return out


def basis_row(t, Ev, Ov, deg):
    """Row of P_{c,b}(t) as a linear form in b's s-coefficients b[0..deg]."""
    t = np.atleast_1d(t)
    R = np.empty((t.size, deg + 1))
    for k in range(deg + 1):
        l = k // 2
        if k % 2 == 0:
            R[:, k] = (-1) ** l * t ** l * Ev
        else:
            R[:, k] = (-1) ** l * t ** (l + 1) * Ov
    return R


def contact_matrix(x, n, Em, Ep, Om, Op):
    rows = []
    for (key, r), xj in zip(touching(x, n, Em, Ep, Om, Op), x[1:n - 1]):
        # E_b(x) + r O_b(x) = 0 as a form in b
        row = np.zeros(n + 1)
        for k in range(n + 1):
            l = k // 2
            if k % 2 == 0:
                row[k] = (-1) ** l * xj ** l
            else:
                row[k] = r * (-1) ** l * xj ** l
        rows.append(row / np.abs(row).max())
    return np.array(rows)


def kernel(A):
    u, s, vt = np.linalg.svd(A)
    rank = int(np.sum(s > s[0] * 1e-13))
    return vt[rank:].T, s


def grid_for(x, npts=2500):
    x = np.asarray(x, float)
    g = np.logspace(np.log10(x.min()) - 3, np.log10(x.max()) + 3, npts)
    near = []
    for xj in x:
        for d in (1e-1, 3e-2, 1e-2, 3e-3, 1e-3):
            near += [xj * (1 - d), xj * (1 + d)]
    g = np.concatenate([[0.0], g, near])
    keep = np.ones(g.size, bool)
    for xj in x:
        keep &= np.abs(g - xj) > 1e-6 * xj
    return np.unique(g[keep])


def closed_kernel_lp(x, n, Em, Ep, Om, Op, grid=None, residual=True):
    """Maximise s over b = K y (K = contact kernel basis), |y|_inf <= 1, subject to
    P_c(t)/(norm) >= s on the grid.  With residual=True each corner row is divided by
    prod over that corner's contacts (t - x_j)^2 and by |c(iw)|/prod|x_j - t| * (1+t)^(n/2)."""
    if grid is None:
        grid = grid_for(x)
    A = contact_matrix(x, n, Em, Ep, Om, Op)
    K, sv = kernel(A)
    tc = touching(x, n, Em, Ep, Om, Op)
    rows = []
    for key, (E, O) in corners(Em, Ep, Om, Op).items():
        Ev = NP.polyval(grid, E); Ov = NP.polyval(grid, O)
        R = basis_row(grid, Ev, Ov, n) @ K
        if residual:
            cont = [xj for (kk, _), xj in zip(tc, x[1:n - 1]) if kk == key]
            q = np.ones_like(grid)
            for xj in cont:
                q *= (grid - xj) ** 2
            mag = np.sqrt(Ev ** 2 + grid * Ov ** 2)
            qq = np.ones_like(grid)
            for xj in cont:
                qq *= np.abs(grid - xj)
            den = q * (mag / qq) * (1 + grid) ** (n / 2.0)
        else:
            den = np.sqrt(Ev ** 2 + grid * Ov ** 2) * (1 + grid) ** (n / 2.0)
        rows.append(R / den[:, None])
    R = np.vstack(rows)
    d = K.shape[1]
    m = R.shape[0]
    Aub = np.hstack([-R, np.ones((m, 1))])
    c = np.zeros(d + 1); c[-1] = -1
    bounds = [(-1, 1)] * d + [(None, 1.0)]
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(m), bounds=bounds, method='highs')
    if res.status != 0:
        return None, None, K
    y = res.x[:-1]
    return res.x[-1], K @ y, K


def kernel_scaled(x, n, Em, Ep, Om, Op):
    """Contact kernel computed in scaled coordinates b_k = tau^(-k) beta_k, tau = sqrt(S),
    S = sqrt(x_0 x_{n-1}); returns (Kb, sv) with Kb columns in raw b-coordinates."""
    S = np.sqrt(x[0] * x[-1])
    tau = np.sqrt(S)
    D = np.diag(tau ** (-np.arange(n + 1.0)))
    A = contact_matrix(x, n, Em, Ep, Om, Op) @ D
    A = A / np.abs(A).max(axis=1, keepdims=True)
    Kb, sv = kernel(A)
    return D @ Kb, sv


def residual_rows(x, n, Em, Ep, Om, Op, K, grid=None):
    """Unit-normalised rows of the four corner pairings restricted to the kernel K,
    after dividing out each corner's squared contact factors.  Returns (rows, keys, tvals)."""
    if grid is None:
        grid = grid_for(x)
    tc = touching(x, n, Em, Ep, Om, Op)
    out, keys, tv = [], [], []
    for key, (E, O) in corners(Em, Ep, Om, Op).items():
        Ev = NP.polyval(grid, E); Ov = NP.polyval(grid, O)
        R = basis_row(grid, Ev, Ov, n) @ K
        q = np.ones_like(grid)
        for (kk, _), xj in zip(tc, x[1:n - 1]):
            if kk == key:
                q *= (grid - xj) ** 2
        R = R / q[:, None]
        nr = np.linalg.norm(R, axis=1)
        ok = nr > 0
        out.append(R[ok] / nr[ok][:, None]); keys += [key] * int(ok.sum()); tv.append(grid[ok])
    return np.vstack(out), np.array(keys), np.concatenate(tv)


def sphere_margin(R, nstart=4000, seed=0, refine=True):
    """max over unit y of min(R y): 3-dim kernel => search the sphere, then refine with LP
    in a local chart.  Returns (margin, y)."""
    rng = np.random.default_rng(seed)
    Y = rng.normal(size=(nstart, R.shape[1]))
    Y /= np.linalg.norm(Y, axis=1, keepdims=True)
    vals = (R @ Y.T).min(axis=0)
    i = int(np.argmax(vals))
    y = Y[i]
    best = vals[i]
    if refine:
        m, d = R.shape
        Aub = np.hstack([-R, np.ones((m, 1))])
        c = np.zeros(d + 1); c[-1] = -1
        Aeq = np.concatenate([y, [0.0]])[None, :]
        res = linprog(c, A_ub=Aub, b_ub=np.zeros(m), A_eq=Aeq, b_eq=[1.0],
                      bounds=[(-10, 10)] * d + [(None, 1.0)], method='highs')
        if res.status == 0:
            y2 = res.x[:-1]; y2 /= np.linalg.norm(y2)
            v2 = (R @ y2).min()
            if v2 > best:
                best, y = v2, y2
    return float(best), y


def lp_margin(R):
    """max s s.t. R y >= s, -1 <= y <= 1.  s > 0 iff the open cone {R y > 0} is nonempty
    (on the given rows); s == 0 otherwise.  Returns (s, y)."""
    m, d = R.shape
    Aub = np.hstack([-R, np.ones((m, 1))])
    c = np.zeros(d + 1); c[-1] = -1
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(m), bounds=[(-1, 1)] * d + [(None, 1.0)],
                  method='highs')
    if res.status != 0:
        return None, None
    return float(res.x[-1]), res.x[:-1]


def farkas_residual(R):
    """min ||R^T mu||_1 over mu >= 0, sum mu = 1 (rows of R unit-normalised).  ~0 iff
    0 is in the convex hull of the rows (no strictly positive y).  Returns (value, mu)."""
    m, d = R.shape
    c = np.concatenate([np.zeros(m), np.ones(2 * d)])
    Aeq = np.zeros((d + 1, m + 2 * d))
    Aeq[:d, :m] = R.T
    Aeq[:d, m:m + d] = -np.eye(d)
    Aeq[:d, m + d:] = np.eye(d)
    Aeq[d, :m] = 1
    beq = np.zeros(d + 1); beq[d] = 1
    r = linprog(c, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * (m + 2 * d), method='highs')
    if r.status != 0:
        return None, None
    return float(r.fun), r.x[:m]


def lp_margin_precond(R):
    """lp_margin after QR preconditioning (R = Q T, y = T b): positivity of the max-min value is
    invariant under the invertible change of variables; values are better scaled."""
    Q, T = np.linalg.qr(R)
    nr = np.linalg.norm(Q, axis=1)
    ok = nr > 0
    s, y = lp_margin(Q[ok] / nr[ok][:, None])
    if s is None:
        return None, None
    return s, np.linalg.solve(T, y)
