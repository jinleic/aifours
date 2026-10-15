"""Fully-closed ("all gaps touching") marginal boxes and their closed synthesis problem.

A monic degree-n box is robustly Hurwitz iff the root bands of E-,E+ (even) and O-,O+
(odd) are disjoint and alternate E,O,E,O,... (Kharitonov + Hermite-Biehler).  In the
fully-closed limit the n-1 bands tile [x_0, x_{n-1}]:
    E-band k = [x_{2k-2}, x_{2k-1}],  O-band k = [x_{2k-1}, x_{2k}].
E- vanishes at the left end of odd E-bands and the right end of even ones, E+ at the other
ends; the same rule holds for O-, O+.  The box is realizable iff E+ - E- and O+ - O- have
nonnegative t-coefficients (coefficient widths) and the fixed monic leading term agrees.

Closed-limit criterion (proved in README): if such a marginal box K0 admits no nonzero
beta (deg <= n) with P_c(t) = F E_c + t G O_c >= 0 on [0, inf) for all 4 corners, then
stable boxes K_eps -> K0 are not synthesizable for small eps.  This module tests the
closed problem on a grid (a relaxation: grid-infeasible => closed-infeasible).
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as P
from scipy.optimize import linprog


def parts_degrees(n):
    DE = n // 2          # deg E
    DO = (n - 1) // 2    # deg O
    return DE, DO


def band_roots(x, n):
    """Root lists of E-, E+, O-, O+ for the tiling points x[0..n-1]."""
    DE, DO = parts_degrees(n)
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


def build_endpoints(x, n, lead_lo, lead_hi):
    """Endpoint polynomials (ascending in t).  The monic part has leading coefficient
    (-1)^deg; the a1-part has leading coefficient (-1)^deg * a1 with a1 in [lead_lo, lead_hi].
    For E_- / O_- the a1-part takes the value minimizing (-1)^deg a1, i.e. lead_lo if deg is
    even, lead_hi if deg is odd (and E_+ / O_+ the other)."""
    DE, DO = parts_degrees(n)
    Em, Ep, Om, Op = band_roots(x, n)

    def mk(roots, lead):
        return P.polyfromroots(roots) * lead

    # which part is monic? n even: E top = c_n = 1 (monic); n odd: O top = c_n = 1
    if n % 2 == 0:
        sE = (-1) ** DE
        Emp, Epp = mk(Em, sE), mk(Ep, sE)
        sO = (-1) ** DO
        if DO % 2 == 0:
            Omp, Opp = mk(Om, sO * lead_lo), mk(Op, sO * lead_hi)
        else:
            Omp, Opp = mk(Om, sO * lead_hi), mk(Op, sO * lead_lo)
    else:
        sO = (-1) ** DO
        Omp, Opp = mk(Om, sO), mk(Op, sO)
        sE = (-1) ** DE
        if DE % 2 == 0:
            Emp, Epp = mk(Em, sE * lead_lo), mk(Ep, sE * lead_hi)
        else:
            Emp, Epp = mk(Em, sE * lead_hi), mk(Ep, sE * lead_lo)
    return Emp, Epp, Omp, Opp


def realizable(Em, Ep, Om, Op, tol=1e-12):
    dE = Ep - Em
    dO = Op - Om
    scale = max(np.abs(Em).max(), np.abs(Ep).max(), np.abs(Om).max(), np.abs(Op).max())
    return bool(np.all(dE >= -tol * scale) and np.all(dO >= -tol * scale)), dE, dO


def box_from_endpoints(Em, Ep, Om, Op, n):
    """Coefficient intervals lo/hi (ascending s-powers) from endpoint polynomials."""
    lo = np.zeros(n + 1)
    hi = np.zeros(n + 1)
    for k in range(n + 1):
        l = k // 2
        sgn = (-1) ** l
        if k % 2 == 0:
            mn, mx = Em[l], Ep[l]
        else:
            mn, mx = Om[l], Op[l]
        if sgn > 0:
            lo[k], hi[k] = mn, mx
        else:
            lo[k], hi[k] = -mx, -mn
    return lo, hi


def contact_rows(x, n, Em, Ep, Om, Op):
    """For each interior touching point x_i (i = 1..n-2) the marginal corner has
    E_c(x_i) = 0 = O_c(x_i); P_c >= 0 forces P_c'(x_i) = F(x_i) E_c'(x_i) + x_i G(x_i) O_c'(x_i)
    = 0.  Returns the rows (linear forms in beta) of these equalities."""
    Es, Os = (Em, Ep), (Om, Op)
    rows = []
    for xi in x[1:n - 1]:
        ie = int(np.argmin([abs(P.polyval(xi, E)) for E in Es]))
        io = int(np.argmin([abs(P.polyval(xi, O)) for O in Os]))
        dE = P.polyval(xi, P.polyder(Es[ie]))
        dO = P.polyval(xi, P.polyder(Os[io]))
        r = np.empty(n + 1)
        for k in range(n + 1):
            l = k // 2
            if k % 2 == 0:
                r[k] = (-1) ** l * xi ** l * dE
            else:
                r[k] = (-1) ** l * xi ** (l + 1) * dO
        rows.append(r / np.abs(r).max())
    return np.array(rows).reshape(-1, n + 1)


def closed_lp(Em, Ep, Om, Op, n, grid, x=None, sign_free=False):
    """max s s.t. P_c(t)/|K_c(jw)|^2 >= s on the grid for all corners, sum beta = 1 and
    beta >= 0 (or beta free with |beta_k| <= 1e3 and sum = 1 if sign_free).  If x is given,
    the exact double-contact equalities at the interior touching points are imposed.
    Returns (status, s, beta); status != 0 => grid-infeasible closed problem."""
    Es, Os = (Em, Ep), (Om, Op)
    rows = []
    t = grid
    for i in (0, 1):
        for j in (0, 1):
            Ev = P.polyval(t, Es[i])
            Ov = P.polyval(t, Os[j])
            den = Ev * Ev + t * Ov * Ov
            R = np.empty((t.size, n + 1))
            for k in range(n + 1):
                l = k // 2
                if k % 2 == 0:
                    R[:, k] = (-1) ** l * t ** l * Ev
                else:
                    R[:, k] = (-1) ** l * t ** (l + 1) * Ov
            ok = den > 0
            R = R[ok] / den[ok][:, None]
            rows.append(R)
    R = np.vstack(rows)
    m = R.shape[0]
    A = np.hstack([-R, np.ones((m, 1))])
    b = np.zeros(m)
    Aeq = [np.concatenate([np.ones(n + 1), [0.0]])]
    beq = [1.0]
    if x is not None:
        for r in contact_rows(x, n, Em, Ep, Om, Op):
            Aeq.append(np.concatenate([r, [0.0]]))
            beq.append(0.0)
    c = np.zeros(n + 2)
    c[-1] = -1.0
    if sign_free:
        bounds = [(-1e3, 1e3)] * (n + 1) + [(None, 1e6)]
    else:
        bounds = [(0, None)] * (n + 1) + [(None, 1e6)]
    res = linprog(c, A_ub=A, b_ub=b, A_eq=np.array(Aeq), b_eq=beq, bounds=bounds,
                  method="highs")
    if res.status != 0:
        return res.status, None, None
    return 0, res.x[-1], res.x[:-1]


def closed_grid(x, npts=3000, near_rel=(1e-2, 3e-3, 1e-3, 3e-4, 1e-4)):
    """Log grid plus points near (never at) the touching points x_i: at x_i both P_c and
    |K_c|^2 vanish for the marginal corner and the quotient is pure roundoff."""
    x = np.asarray(x, float)
    g = np.logspace(np.log10(x.min()) - 4, np.log10(x.max()) + 4, npts)
    d = np.array(near_rel)
    near = np.concatenate([xi * (1 + np.concatenate([-d, d])) for xi in x])
    g = np.concatenate([[0.0], g, near])
    # drop grid points within 1e-5 relative distance of a touching point
    keep = np.ones(g.size, bool)
    for xi in x:
        keep &= np.abs(g - xi) > 1e-5 * xi
    return np.unique(g[keep])
