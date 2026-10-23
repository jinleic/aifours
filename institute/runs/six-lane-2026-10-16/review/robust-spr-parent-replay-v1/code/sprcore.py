"""Core utilities for the six-lane robust-SPR lane (float exploration + exact checks).

Conventions (match prior dossier work/theory.md):
  * a polynomial in s is an ascending coefficient array p[0..deg] (p[k] = coefficient of s^k);
  * a monic degree-n box is given by lo[k], hi[k] for k = 0..n-1 (the s^n coefficient is 1);
  * for p(s) real: p(iw) = E_p(t) + i w O_p(t), t = w^2, with
        E_p(t) = sum_l (-1)^l p[2l] t^l,   O_p(t) = sum_l (-1)^l p[2l+1] t^l;
  * pairing P_{a,b}(t) = E_b E_a + t O_b O_a = Re(b(iw) conj a(iw)).
Polynomials in t are ascending arrays too.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as NP


def EO(p):
    """Even/odd component polynomials (ascending in t) of an s-polynomial p."""
    p = np.asarray(p, dtype=float)
    E = np.array([(-1) ** l * p[2 * l] for l in range((len(p) + 1) // 2)])
    O = np.array([(-1) ** l * p[2 * l + 1] for l in range(len(p) // 2)])
    if O.size == 0:
        O = np.zeros(1)
    return E, O


def from_EO(E, O, n):
    """Inverse of EO for degree <= n."""
    p = np.zeros(n + 1)
    for l, c in enumerate(E):
        if 2 * l <= n:
            p[2 * l] = (-1) ** l * c
    for l, c in enumerate(O):
        if 2 * l + 1 <= n:
            p[2 * l + 1] = (-1) ** l * c
    return p


def kharitonov_EO(lo, hi):
    """Endpoint components (E-, E+, O-, O+) of the monic box with lower coefficients lo, hi
    (length n arrays for s^0..s^(n-1)).  E- <= E_a <= E+ and O- <= O_a <= O+ on t >= 0."""
    lo = np.asarray(lo, float)
    hi = np.asarray(hi, float)
    n = lo.size
    lo1 = np.append(lo, 1.0)
    hi1 = np.append(hi, 1.0)
    Em, Ep, Om, Op = [], [], [], []
    for l in range((n + 2) // 2):
        k = 2 * l
        if k > n:
            break
        s = (-1) ** l
        a, b = s * lo1[k], s * hi1[k]
        Em.append(min(a, b)); Ep.append(max(a, b))
    for l in range((n + 1) // 2):
        k = 2 * l + 1
        if k > n:
            break
        s = (-1) ** l
        a, b = s * lo1[k], s * hi1[k]
        Om.append(min(a, b)); Op.append(max(a, b))
    return (np.array(Em), np.array(Ep), np.array(Om), np.array(Op))


def corner_polys(lo, hi):
    """The four Kharitonov corner s-polynomials, keyed '--','-+','+-','++' (E sign, O sign)."""
    n = len(lo)
    Em, Ep, Om, Op = kharitonov_EO(lo, hi)
    out = {}
    for ke, E in (('-', Em), ('+', Ep)):
        for ko, O in (('-', Om), ('+', Op)):
            out[ke + ko] = from_EO(E, O, n)
    return out


def pairing(b, a):
    """P_{a,b}(t) ascending in t."""
    Eb, Ob = EO(b)
    Ea, Oa = EO(a)
    return NP.polyadd(NP.polymul(Eb, Ea), NP.polymulx(NP.polymul(Ob, Oa)))


def is_hurwitz_float(p, tol=0.0):
    r = np.roots(np.asarray(p, float)[::-1])
    return bool(np.all(r.real < -tol)), r


def lambda_stab(lo, hi, tgrid=None):
    """Radial stability factor of the box with centre c0 = (lo+hi)/2 and radii r = (hi-lo)/2:
    sup{lam : c0 + lam*[-r, r] robustly Hurwitz}, by zero exclusion on a t-grid (float).
    Requires c0 Hurwitz (returns 0 otherwise).  lam > 1 <=> the box itself is robustly stable
    (up to grid resolution)."""
    lo = np.asarray(lo, float); hi = np.asarray(hi, float)
    n = lo.size
    c0 = np.append((lo + hi) / 2, 1.0)
    r = np.append((hi - lo) / 2, 0.0)
    ok, _ = is_hurwitz_float(c0)
    if not ok:
        return 0.0
    Ec, Oc = EO(c0)
    # radius polynomials: R_E(t) = sum r_{2l} t^l, R_O(t) = sum r_{2l+1} t^l
    RE = np.array([r[2 * l] for l in range(len(Ec))])
    RO = np.array([r[2 * l + 1] for l in range(len(Oc))]) if n >= 1 else np.zeros(1)
    if tgrid is None:
        tgrid = np.logspace(-8, 8, 20001)
    Ev = np.abs(NP.polyval(tgrid, Ec)); Ov = np.abs(NP.polyval(tgrid, Oc))
    REv = NP.polyval(tgrid, RE); ROv = NP.polyval(tgrid, RO)
    with np.errstate(divide='ignore', invalid='ignore'):
        rE = np.where(REv > 0, Ev / REv, np.inf)
        rO = np.where(ROv > 0, Ov / ROv, np.inf)
    lam = np.min(np.maximum(rE, rO))
    lam0 = Ec[0] / RE[0] if RE[0] > 0 else np.inf
    return float(min(lam, lam0))


def spr_lp(lo, hi, tgrid, deg=None, normalize='angle', fix_lead=False):
    """Grid LP: maximise s subject to Re(b conj c)(iw)/(|b-free norm|) >= s at every grid
    point and corner, with sum(b) = 1 (b >= 0 not imposed).  Uses per-row normalisation by
    |c(iw)| * (1+t)^(n/2) so the margin is scale-aware.  Returns (s, b)."""
    from scipy.optimize import linprog
    n = len(lo)
    deg = n if deg is None else deg
    cps = corner_polys(lo, hi)
    rows = []
    t = np.asarray(tgrid, float)
    for key, c in cps.items():
        Ec, Oc = EO(c)
        Ev = NP.polyval(t, Ec); Ov = NP.polyval(t, Oc)
        R = np.empty((t.size, deg + 1))
        for k in range(deg + 1):
            l = k // 2
            if k % 2 == 0:
                R[:, k] = (-1) ** l * t ** l * Ev
            else:
                R[:, k] = (-1) ** l * t ** (l + 1) * Ov
        den = np.sqrt(Ev ** 2 + t * Ov ** 2) * (1 + t) ** (deg / 2.0)
        rows.append(R / den[:, None])
    R = np.vstack(rows)
    m = R.shape[0]
    A = np.hstack([-R, np.ones((m, 1))])
    bub = np.zeros(m)
    Aeq = [np.concatenate([np.ones(deg + 1), [0.0]])]
    beq = [1.0]
    c = np.zeros(deg + 2); c[-1] = -1.0
    bounds = [(-1e4, 1e4)] * (deg + 1) + [(None, 1.0)]
    res = linprog(c, A_ub=A, b_ub=bub, A_eq=np.array(Aeq), b_eq=beq, bounds=bounds,
                  method='highs')
    if res.status != 0:
        return None, None
    return res.x[-1], res.x[:-1]
