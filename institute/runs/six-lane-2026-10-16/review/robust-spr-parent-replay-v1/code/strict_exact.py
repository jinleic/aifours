"""Exact certificate that a robustly stable (generalized) rectangle family has NO real numerator
of exact degree n with Re(b/a) > 0 on the imaginary axis for all members.

Data: rational endpoint components E-, E+, O-, O+ (polynomials in t), with E- <= E+ and
O- <= O+ on [0, inf).  The family is {E(-s^2) + s O(-s^2) : E between E-, E+, O between O-, O+}
(as a convex polytope of polynomials its value set at s = iw is the rectangle, so the four
corners are the extreme members for every fixed numerator).

Checked exactly (python-flint):
  * stability: each corner polynomial passes the exact Routh test (all first-column entries > 0);
  * widths W_E, W_O nonnegative on [0, inf) (exact factor + Sturm) and their coefficient signs;
  * certificate: rational nodes t_k >= 0, corners c_k, weights mu_k > 0, mu_inf >= 0 with
      sum_k mu_k F(c_k, t_k) + mu_inf e_n = 0   exactly,
    where b . F(c, t) = P_{c,b}(t).  Then any b with all P_{c_k,b}(t_k) > 0 has [s^n] b < 0,
    so no exact-degree-n numerator with positive leading coefficient exists (and a common SPR
    numerator must have positive leading coefficient: Re(b/a) -> [s^n]b at w -> inf).
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction

import flint
import numpy as np
from scipy.optimize import linprog

from closed_exact import fq, nullspace_q, nonneg_halfline_exact


def spoly_from_EO(E, O, n):
    """s-coefficients (fmpq list, length n+1) of E(-s^2) + s O(-s^2)."""
    c = [flint.fmpq(0)] * (n + 1)
    for l in range(E.degree() + 1):
        if 2 * l <= n:
            c[2 * l] = (-1) ** l * E[l]
    for l in range(O.degree() + 1):
        if 2 * l + 1 <= n:
            c[2 * l + 1] = (-1) ** l * O[l]
    return c


def routh_positive(c):
    """Exact Routh test for real polynomial with coefficients c (ascending, leading c[-1] > 0).
    Returns True iff all first-column entries are positive (=> Hurwitz)."""
    a = list(reversed(c))  # descending
    n = len(a) - 1
    r1 = a[0::2]
    r2 = a[1::2]
    first = [r1[0]]
    if any(v <= 0 for v in a):
        return False
    rows = [r1, r2]
    while len(rows) < n + 1:
        p, q = rows[-2], rows[-1]
        if q[0] == 0:
            return False
        new = []
        for j in range(len(p) - 1):
            qj1 = q[j + 1] if j + 1 < len(q) else flint.fmpq(0)
            new.append((q[0] * p[j + 1] - p[0] * qj1) / q[0])
        if not new:
            new = [flint.fmpq(0)]
        rows.append(new)
    return all(rw[0] > 0 for rw in rows)



def bands_disjoint_exact(Em, Ep, Om, Op):
    """Zero exclusion for the rectangle family, certified with arb root enclosures:
    every positive root of each endpoint component is simple and real-isolated; the E-bands
    [k-th root of E-, k-th root of E+] (sorted) and O-bands alternate E,O,E,... strictly, with
    no overlap.  Returns (ok, detail)."""
    def pos_roots(p):
        den = p.denom()
        pz = flint.fmpz_poly([int(p[i] * den) for i in range(p.degree() + 1)])
        rr = pz.complex_roots()
        rr = [(r.real, m) for r, m in rr if r.imag.contains(0)]
        out = []
        for r, m in rr:
            if m != 1:
                return None
            if r > 0:
                out.append(r)
            elif not (r < 0):
                return None   # ball straddles 0: undecided
        return out
    R = {k: pos_roots(p) for k, p in (('Em', Em), ('Ep', Ep), ('Om', Om), ('Op', Op))}
    if any(v is None for v in R.values()):
        return False, 'multiple or undecided roots'
    if len(R['Em']) != len(R['Ep']) or len(R['Om']) != len(R['Op']):
        return False, 'root counts differ'
    bands = []
    for a, b in zip(R['Em'], R['Ep']):
        bands.append(('E', min(a, b) if (a < b or b < a) else a, max(a, b) if (a < b or b < a) else b))
    for a, b in zip(R['Om'], R['Op']):
        bands.append(('O', min(a, b) if (a < b or b < a) else a, max(a, b) if (a < b or b < a) else b))
    # sort by certified lower ends (fallback to midpoints)
    bands.sort(key=lambda z: float(z[1].mid()))
    kinds = ''.join(z[0] for z in bands)
    alt = all(kinds[i] != kinds[i + 1] for i in range(len(kinds) - 1)) and kinds[:1] == 'E'
    sep = all(bands[i][2] < bands[i + 1][1] for i in range(len(bands) - 1))
    return bool(alt and sep), kinds

def Fvec(E, O, t, n):
    """F(c, t): coefficient vector of P_{c,b}(t) in b's s-coefficients."""
    e = E(t); o = O(t)
    return [(-1) ** (k // 2) * t ** (k // 2) * e if k % 2 == 0 else
            (-1) ** (k // 2) * t ** (k // 2 + 1) * o for k in range(n + 1)]


def float_dual(corners, n, grid, tau2=1.0):
    """Float LP: min ||sum mu v||_1 s.t. mu >= 0, sum mu = 1 over unit-normalised vectors
    v = F(c,t) D (D = diag(tau^-k), frequency-scaled coordinates) and e_n.  Column/row scalings
    do not change positive dependence.  Returns (residual, support list of (key, t))."""
    tau = np.sqrt(tau2)
    D = tau ** (-np.arange(n + 1.0))
    rows, lab = [], []
    for key, (E, O) in corners.items():
        Ec = np.array([float(E[i]) for i in range(E.degree() + 1)])
        Oc = np.array([float(O[i]) for i in range(O.degree() + 1)])
        Ev = np.polynomial.polynomial.polyval(grid, Ec)
        Ov = np.polynomial.polynomial.polyval(grid, Oc)
        for t, e, o in zip(grid, Ev, Ov):
            v = np.array([(-1) ** (k // 2) * t ** (k // 2) * e if k % 2 == 0 else
                          (-1) ** (k // 2) * t ** (k // 2 + 1) * o for k in range(n + 1)])
            rows.append(v * D); lab.append((key, float(t)))
    en = np.zeros(n + 1); en[n] = 1.0
    rows.append(en); lab.append(('inf', None))
    V = np.array(rows)
    Vs = V
    nr = np.linalg.norm(Vs, axis=1)
    keep = nr > 0
    Vs = Vs[keep] / nr[keep][:, None]
    lab = [l for l, k in zip(lab, keep) if k]
    m, d = Vs.shape
    c = np.concatenate([np.zeros(m), np.ones(2 * d)])
    Aeq = np.zeros((d + 1, m + 2 * d))
    Aeq[:d, :m] = Vs.T; Aeq[:d, m:m + d] = -np.eye(d); Aeq[:d, m + d:] = np.eye(d)
    Aeq[d, :m] = 1
    beq = np.zeros(d + 1); beq[d] = 1
    r = linprog(c, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * (m + 2 * d), method='highs')
    mu = r.x[:m]
    idx = [i for i in np.argsort(-mu) if mu[i] > 1e-10][: n + 3]
    return r.fun, [lab[i] for i in idx]


def certify(n, Em, Ep, Om, Op, grid=None, tscale=(1.0, 1.0)):
    out = {}
    corners = {'--': (Em, Om), '-+': (Em, Op), '+-': (Ep, Om), '++': (Ep, Op)}
    WE, WO = Ep - Em, Op - Om
    out['WE'] = [str(WE[i]) for i in range(WE.degree() + 1)]
    out['WO'] = [str(WO[i]) for i in range(WO.degree() + 1)]
    out['WE_halfline_nonneg'] = nonneg_halfline_exact(WE)
    out['WO_halfline_nonneg'] = nonneg_halfline_exact(WO)
    out['WE_coeffwise_nonneg'] = all(WE[i] >= 0 for i in range(WE.degree() + 1))
    out['WO_coeffwise_nonneg'] = all(WO[i] >= 0 for i in range(WO.degree() + 1))
    out['corners_routh'] = {k: routh_positive(spoly_from_EO(E, O, n)) for k, (E, O) in corners.items()}
    bd = bands_disjoint_exact(Em, Ep, Om, Op)
    out['bands_strictly_disjoint_alternating'] = bd[0]
    out['band_kinds'] = bd[1]
    tlo, thi = tscale
    if grid is None:
        grid = np.concatenate([[0.0], np.logspace(np.log10(tlo) - 3, np.log10(thi) + 3, 6000)])
    fres, supp = float_dual(corners, n, grid, tau2=np.sqrt(tlo * thi))
    out['float_dual_residual'] = fres
    vecs, labs = [], []
    for key, t in supp:
        if key == 'inf':
            v = [flint.fmpq(0)] * (n + 1); v[n] = flint.fmpq(1)
            vecs.append(v); labs.append(('inf', None))
        else:
            tq = fq(Fraction(t).limit_denominator(10 ** 9))
            E, O = corners[key]
            vecs.append(Fvec(E, O, tq, n)); labs.append((key, str(tq)))
    rows = [[v[i] for v in vecs] for i in range(n + 1)]
    nb = nullspace_q(rows, len(vecs))
    cert = None
    for mu in nb:
        if all(m >= 0 for m in mu) and any(m > 0 for m in mu):
            cert = mu; break
        if all(m <= 0 for m in mu) and any(m < 0 for m in mu):
            cert = [-m for m in mu]; break
    out['support'] = labs
    out['weights'] = [str(m) for m in cert] if cert else None
    ok = cert is not None
    if ok:
        # exact recheck of the identity
        for i in range(n + 1):
            assert sum(cert[j] * vecs[j][i] for j in range(len(vecs))) == 0
        # finite weights positive at least on one finite node
        ok = any(cert[j] > 0 and labs[j][0] != 'inf' for j in range(len(vecs)))
    out['nullspace_dim'] = len(nb)
    out['strict_infeasible_certified'] = bool(ok and all(out['corners_routh'].values())
                                              and out['bands_strictly_disjoint_alternating'])
    return out


def shrink(Em, Ep, Om, Op, lam):
    Ec, Oc = (Em + Ep) * flint.fmpq(1, 2), (Om + Op) * flint.fmpq(1, 2)
    WE, WO = (Ep - Em) * flint.fmpq(1, 2), (Op - Om) * flint.fmpq(1, 2)
    return Ec - WE * lam, Ec + WE * lam, Oc - WO * lam, Oc + WO * lam


if __name__ == '__main__':
    from closed_exact import band_roots, xpoly
    spec = json.load(open(sys.argv[1]))
    lam = fq(sys.argv[3]) if len(sys.argv) > 3 else fq('99/100')
    n = spec['n']
    x = [fq(v) for v in spec['x']]; L = [fq(v) for v in spec['leads']]
    Er, Epr, Or, Opr = band_roots(x, n)
    Em, Ep, Om, Op = xpoly(Er, L[0]), xpoly(Epr, L[1]), xpoly(Or, L[2]), xpoly(Opr, L[3])
    Em, Ep, Om, Op = shrink(Em, Ep, Om, Op, lam)
    out = certify(n, Em, Ep, Om, Op, tscale=(float(min(x)), float(max(x))))
    out['shrink_factor'] = str(lam)
    out['source_spec'] = spec
    json.dump(out, open(sys.argv[2], 'w'), indent=1)
    print(json.dumps({k: out[k] for k in ('WE_halfline_nonneg', 'WO_halfline_nonneg',
                                          'WE_coeffwise_nonneg', 'WO_coeffwise_nonneg',
                                          'corners_routh', 'float_dual_residual', 'support',
                                          'nullspace_dim', 'strict_infeasible_certified')},
                     indent=1))
