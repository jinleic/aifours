"""Exact certificate of closed infeasibility for a fully-closed (generalized or box) family.

Claim certified (for the given rational data only):
  every real b with deg b <= n and P_{c,b}(t) >= 0 on [0, inf) for all four corners c is b = 0.
Proof structure checked here in exact rational arithmetic (python-flint):
  1. every interior band point x_j is a common root of the touching corner's two components,
     so P_{c_j,b}(x_j) = 0 and nonnegativity forces P'_{c_j,b}(x_j) = 0 (x_j > 0 interior);
     these n-2 linear conditions have an exactly computed 3-dimensional kernel;
  2. on the kernel, each residual R_c = P_c / prod_{contacts of c} (t - x_j)^2 is an exact
     polynomial division (remainder checked = 0);
  3. support points (c_k, t_k), t_k >= 0 rational, with exact weights mu_k > 0 such that
     sum_k mu_k R_{c_k}(t_k; y) = 0 identically in y, and the vectors span Q^3.
     Then a closed numerator y has R_{c_k}(t_k; y) >= 0 summing to zero, hence all zero,
     hence y = 0 by the rank condition.
Also reports W_E, W_O coefficients and whether they are >= 0 on [0, inf) (Sturm, exact).
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction

import flint
import numpy as np
from scipy.optimize import linprog


def fq(v):
    if isinstance(v, str):
        return flint.fmpq(Fraction(v).numerator, Fraction(v).denominator)
    fr = Fraction(v).limit_denominator(10 ** 12) if isinstance(v, float) else Fraction(v)
    return flint.fmpq(fr.numerator, fr.denominator)


def band_roots(x, n):
    DE, DO = n // 2, (n - 1) // 2
    Em, Ep, Om, Op = [], [], [], []
    for k in range(1, DE + 1):
        L, R = x[2 * k - 2], x[2 * k - 1]
        (Em.append(L), Ep.append(R)) if k % 2 == 1 else (Ep.append(L), Em.append(R))
    for k in range(1, DO + 1):
        L, R = x[2 * k - 1], x[2 * k]
        (Om.append(L), Op.append(R)) if k % 2 == 1 else (Op.append(L), Om.append(R))
    return Em, Ep, Om, Op


def xpoly(roots, lead):
    p = flint.fmpq_poly([lead])
    for r in roots:
        p *= flint.fmpq_poly([r, -1])
    return p


def sturm_count_pos(p):
    """Number of distinct real roots of p in (0, inf), exact (Sturm sequence)."""
    p = flint.fmpq_poly(p)
    if p.degree() <= 0:
        return 0
    g = flint.fmpq_poly.gcd(p, p.derivative())
    p = p / g if g.degree() > 0 else p   # squarefree part
    seq = [p, p.derivative()]
    while seq[-1].degree() > 0:
        r = -(seq[-2] % seq[-1])
        if r == 0:
            break
        seq.append(r)

    def sign_changes(vals):
        s = [v for v in vals if v != 0]
        return sum(1 for a, b in zip(s, s[1:]) if (a > 0) != (b > 0))
    at0 = [q(0) for q in seq]
    atinf = [q[q.degree()] for q in seq]
    # roots exactly at 0 are excluded: Sturm counts roots in (0, inf] when p(0) != 0;
    # if p(0) == 0 use a tiny positive point instead via deflation
    if p(0) == 0:
        p0 = p / flint.fmpq_poly([0, 1])
        return sturm_count_pos(p0)
    return sign_changes(at0) - sign_changes(atinf)


def nonneg_halfline_exact(p):
    """p >= 0 on [0, inf) exactly: p(0) >= 0, leading coefficient >= 0 and no positive root
    of odd multiplicity."""
    if p == 0:
        return True
    if p[p.degree()] < 0 or p(0) < 0:
        return False
    fac = p.factor()
    for q, mult in fac[1]:
        if mult % 2 == 1 and sturm_count_pos(q) > 0:
            return False
    return True


def nullspace_q(rows, ncols):
    """Basis (list of vectors) of the right nullspace of a rational matrix, via rref."""
    if not rows:
        return [[flint.fmpq(1 if i == j else 0) for i in range(ncols)] for j in range(ncols)]
    R, rank = flint.fmpq_mat(rows).rref()
    pivots = []
    r = 0
    for c in range(ncols):
        if r < rank and R[r, c] != 0:
            pivots.append(c); r += 1
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [flint.fmpq(0)] * ncols
        v[f] = flint.fmpq(1)
        for i, pc in enumerate(pivots):
            v[pc] = -R[i, f]
        basis.append(v)
    return basis


def comps(b, n):
    """E_b, O_b as fmpq_poly in t for coefficient vector b (length n+1, fmpq)."""
    E = flint.fmpq_poly([(-1) ** l * b[2 * l] for l in range((n + 2) // 2) if 2 * l <= n])
    O = flint.fmpq_poly([(-1) ** l * b[2 * l + 1] for l in range((n + 1) // 2) if 2 * l + 1 <= n])
    return E, O


def certify(n, x, leads, support=None, grid=None):
    x = [fq(v) for v in x]
    leads = [fq(v) for v in leads]
    Er, Epr, Or, Opr = band_roots(x, n)
    Em, Ep = xpoly(Er, leads[0]), xpoly(Epr, leads[1])
    Om, Op = xpoly(Or, leads[2]), xpoly(Opr, leads[3])
    WE, WO = Ep - Em, Op - Om
    E = {'-': Em, '+': Ep}; O = {'-': Om, '+': Op}
    # touching corners
    touch = []
    for xj in x[1:n - 1]:
        ke = [k for k in E if E[k](xj) == 0]
        ko = [k for k in O if O[k](xj) == 0]
        assert len(ke) == 1 and len(ko) == 1, 'not a fully-closed configuration'
        touch.append((ke[0] + ko[0], xj))
    # contact rows: E_b(x) E_c'(x) + x O_b(x) O_c'(x) as linear form in b
    rows = []
    for key, xj in touch:
        dE = E[key[0]].derivative()(xj); dO = O[key[1]].derivative()(xj)
        row = []
        for k in range(n + 1):
            l = k // 2
            row.append((-1) ** l * xj ** l * dE if k % 2 == 0 else (-1) ** l * xj ** (l + 1) * dO)
        rows.append(row)
    basis = nullspace_q(rows, n + 1)
    nullity = len(basis)
    assert nullity == 3, f'kernel dimension {nullity}'
    # residual polys
    res = {}
    for ke in '-+':
        for ko in '-+':
            key = ke + ko
            q = flint.fmpq_poly([1])
            for kk, xj in touch:
                if kk == key:
                    q *= flint.fmpq_poly([-xj, 1]) ** 2
            Rs = []
            for bvec in basis:
                Eb, Ob = comps(bvec, n)
                P = Eb * E[ke] + flint.fmpq_poly([0, 1]) * Ob * O[ko]
                quo, rem = divmod(P, q)
                assert rem == 0
                Rs.append(quo)
            res[key] = Rs
    out = {'n': n, 'x': [str(v) for v in x], 'leads': [str(v) for v in leads],
           'WE': [str(WE[i]) for i in range(WE.degree() + 1)],
           'WO': [str(WO[i]) for i in range(WO.degree() + 1)],
           'WE_coeffwise_nonneg': all(WE[i] >= 0 for i in range(WE.degree() + 1)),
           'WO_coeffwise_nonneg': all(WO[i] >= 0 for i in range(WO.degree() + 1)),
           'WE_halfline_nonneg': nonneg_halfline_exact(WE),
           'WO_halfline_nonneg': nonneg_halfline_exact(WO),
           'touching': [(k, str(v)) for k, v in touch], 'kernel_dim': nullity}
    if support is None:
        support = float_support(res, x, grid)
    vecs = []
    for key, t in support:
        tq = fq(t)
        vecs.append([R(tq) for R in res[key]])
    M = flint.fmpq_mat([[v[i] for v in vecs] for i in range(3)])
    rank = M.rank()
    # weights: nullspace of M (3 x m)
    nb = nullspace_q([[v[i] for v in vecs] for i in range(3)], len(vecs))
    nul = len(nb)
    cert = None
    for mu in nb:
        if all(m > 0 for m in mu) or all(m < 0 for m in mu):
            if mu[0] < 0:
                mu = [-m for m in mu]
            cert = mu
            break
    out['support'] = [(k, str(fq(t))) for k, t in support]
    out['support_rank'] = rank
    out['weights'] = [str(m) for m in cert] if cert else None
    out['closed_infeasible_certified'] = bool(cert is not None and rank == 3 and nul == 1)
    return out, res


def float_support(res, x, grid=None):
    """Find (key, t) support of a positive dependence among residual functionals by LP."""
    xs = [float(v) for v in x]
    if grid is None:
        g = np.logspace(np.log10(min(xs)) - 3, np.log10(max(xs)) + 3, 4000)
        g = np.concatenate([[0.0], g])
    else:
        g = grid
    V, lab = [], []
    for key, Rs in res.items():
        coeffs = [np.array([float(R[i]) for i in range(R.degree() + 1)]) for R in Rs]
        vals = np.array([np.polynomial.polynomial.polyval(g, c) for c in coeffs]).T
        nr = np.linalg.norm(vals, axis=1)
        ok = nr > 0
        V.append(vals[ok] / nr[ok][:, None]); lab += [(key, t) for t in g[ok]]
    V = np.vstack(V)
    m = V.shape[0]
    # min ||V^T mu||_1 s.t. mu >= 0, sum mu = 1
    c = np.concatenate([np.zeros(m), np.ones(6)])
    Aeq = np.zeros((4, m + 6))
    Aeq[:3, :m] = V.T
    Aeq[:3, m:m + 3] = -np.eye(3)
    Aeq[:3, m + 3:] = np.eye(3)
    Aeq[3, :m] = 1
    beq = np.array([0, 0, 0, 1.0])
    r = linprog(c, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * (m + 6), method='highs')
    mu = r.x[:m]
    idx = np.argsort(-mu)[:4]
    return [(lab[i][0], float(lab[i][1])) for i in idx if mu[i] > 1e-12]


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    out, _ = certify(spec['n'], spec['x'], spec['leads'], spec.get('support'))
    json.dump(out, open(sys.argv[2], 'w'), indent=1)
    print(json.dumps({k: out[k] for k in ('WE_coeffwise_nonneg', 'WO_coeffwise_nonneg',
                                          'WE_halfline_nonneg', 'WO_halfline_nonneg',
                                          'support', 'support_rank', 'weights',
                                          'closed_infeasible_certified')}, indent=1))
