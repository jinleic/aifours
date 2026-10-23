"""Consolidated exact replay of the lane's preserved certificates, with positive and negative
(mutation) controls.  All decisive checks are exact rational arithmetic (python-flint); float
code only proposes rational support points / numerators that are then re-verified exactly.

Usage: python verify_all.py OUT.json
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from fractions import Fraction

import flint
import numpy as np

import closed_exact as CE
import strict_exact as SE

LANE = '..'


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def fam_from_spec(spec):
    n = spec['n']
    x = [CE.fq(v) for v in spec['x']]
    L = [CE.fq(v) for v in spec['leads']]
    Er, Epr, Or, Opr = CE.band_roots(x, n)
    return n, x, (CE.xpoly(Er, L[0]), CE.xpoly(Epr, L[1]), CE.xpoly(Or, L[2]), CE.xpoly(Opr, L[3]))


def pairing(b, E, O, n):
    Eb, Ob = CE.comps(b, n)
    return Eb * E + flint.fmpq_poly([0, 1]) * Ob * O


def strictly_positive_halfline(p):
    """p > 0 on [0, inf) exactly: p(0) > 0, leading coefficient > 0, no positive real root."""
    if p == 0 or p(0) <= 0 or p[p.degree()] <= 0:
        return False
    return CE.sturm_count_pos(p) == 0


def check_identity(vecs, mu):
    m = len(vecs[0])
    return all(sum(mu[j] * vecs[j][i] for j in range(len(vecs))) == 0 for i in range(m))


def g1_closed(name):
    spec = json.load(open(f'{LANE}/evidence/genrect/spec_{name}.json'))
    out, res = CE.certify(spec['n'], spec['x'], spec['leads'],
                          support=json.load(open(f'{LANE}/evidence/genrect/cert_{name}.json'))['support'])
    rec = {k: out[k] for k in ('WE_coeffwise_nonneg', 'WO_coeffwise_nonneg', 'WE_halfline_nonneg',
                               'WO_halfline_nonneg', 'support_rank', 'closed_infeasible_certified')}
    # mutation control: perturb first weight -> identity must fail
    vecs = [[R(CE.fq(t)) for R in res[k]] for k, t in out['support']]
    mu = [CE.fq(w) for w in out['weights']]
    rec['identity_exact'] = check_identity(vecs, mu)
    mu2 = [mu[0] * flint.fmpq(1001, 1000)] + mu[1:]
    rec['mutation_weight_breaks_identity'] = not check_identity(vecs, mu2)
    # mutation control: drop one support point -> no positive dependence among the rest
    nb = CE.nullspace_q([[v[i] for v in vecs[1:]] for i in range(3)], len(vecs) - 1)
    rec['mutation_drop_point_no_dependence'] = (len(nb) == 0)
    rec['valid_generalized_family'] = bool(out['WE_halfline_nonneg'] and out['WO_halfline_nonneg'])
    return rec


def g1_strict():
    spec = json.load(open(f'{LANE}/evidence/genrect/spec_n6_gen_s21.json'))
    n, x, fam = fam_from_spec(spec)
    rec = {}
    for lam in ('999/1000',):
        F = SE.shrink(*fam, CE.fq(lam))
        stored = json.load(open(f'{LANE}/evidence/genrect/strict_n6_gen_s21_lam999_1000.json'))
        corners = {'--': (F[0], F[2]), '-+': (F[0], F[3]), '+-': (F[1], F[2]), '++': (F[1], F[3])}
        vecs = []
        for key, t in stored['support']:
            E, O = corners[key]
            vecs.append(SE.Fvec(E, O, CE.fq(t), n))
        mu = [CE.fq(w) for w in stored['weights']]
        rec['lam'] = lam
        rec['weights_positive'] = all(m > 0 for m in mu)
        rec['identity_exact'] = check_identity(vecs, mu)
        rec['mutation_weight_breaks_identity'] = not check_identity(vecs, [mu[0] * 2] + mu[1:])
        rec['corners_routh'] = {k: SE.routh_positive(SE.spoly_from_EO(E, O, n)) for k, (E, O) in corners.items()}
        rec['bands_disjoint'] = SE.bands_disjoint_exact(*F)[0]
        WE, WO = F[1] - F[0], F[3] - F[2]
        rec['WE_halfline_nonneg'] = CE.nonneg_halfline_exact(WE)
        rec['WO_halfline_nonneg'] = CE.nonneg_halfline_exact(WO)
        rec['WE_coeffwise_nonneg'] = all(WE[i] >= 0 for i in range(WE.degree() + 1))
        rec['WO_coeffwise_nonneg'] = all(WO[i] >= 0 for i in range(WO.degree() + 1))
    # positive control: at shrink 9/10 the same family IS synthesizable: exhibit a rational strict
    # numerator and verify all four pairings > 0 on [0, inf) exactly
    F = SE.shrink(*fam, CE.fq('9/10'))
    b = positive_control_numerator(F, n)
    ok = b is not None
    if ok:
        corners = [(F[0], F[2]), (F[0], F[3]), (F[1], F[2]), (F[1], F[3])]
        ok = all(strictly_positive_halfline(pairing(b, E, O, n)) for E, O in corners) and b[n] > 0
    rec['positive_control_shrink_9_10_strict_numerator_exact'] = ok
    return rec


def positive_control_numerator(F, n):
    """Float LP on a grid for a strict numerator, rationalised; returns fmpq list or None."""
    from scipy.optimize import linprog
    Ef = [np.array([float(p[i]) for i in range(p.degree() + 1)]) for p in F]
    corners = [(Ef[0], Ef[2]), (Ef[0], Ef[3]), (Ef[1], Ef[2]), (Ef[1], Ef[3])]
    g = np.concatenate([[0.0], np.logspace(-3, 4, 4000), np.linspace(18, 24, 3000)])
    tau = np.sqrt(np.sqrt(1e-3 * 1e4)); D = tau ** (-np.arange(n + 1.0))
    rows = []
    for E, O in corners:
        Ev, Ov = np.polynomial.polynomial.polyval(g, E), np.polynomial.polynomial.polyval(g, O)
        M = np.empty((g.size, n + 1))
        for k in range(n + 1):
            l = k // 2
            M[:, k] = (-1) ** l * g ** l * (Ev if k % 2 == 0 else g * Ov)
        M = M * D
        rows.append(M / np.linalg.norm(M, axis=1, keepdims=True))
    en = np.zeros(n + 1); en[n] = 1.0
    R = np.vstack(rows + [en[None, :] * D])
    Q, T = np.linalg.qr(R)
    Qn = Q / np.linalg.norm(Q, axis=1, keepdims=True)
    m, d = Qn.shape
    res = linprog(np.r_[np.zeros(d), -1.0], A_ub=np.hstack([-Qn, np.ones((m, 1))]),
                  b_ub=np.zeros(m), bounds=[(-1, 1)] * d + [(None, 1.0)], method='highs')
    if res.status != 0 or res.x[-1] <= 0:
        return None
    bf = D * np.linalg.solve(T, res.x[:-1])
    bf = bf / np.abs(bf).max()
    return [CE.fq(Fraction(v).limit_denominator(10 ** 12)) for v in bf]


def fullyclosed_exact(x, leads, n):
    x = [CE.fq(v) if not isinstance(v, flint.fmpq) else v for v in x]
    L = [CE.fq(v) if not isinstance(v, flint.fmpq) else v for v in leads]
    Er, Epr, Or, Opr = CE.band_roots(x, n)
    E = {'-': CE.xpoly(Er, L[0]), '+': CE.xpoly(Epr, L[1])}
    O = {'-': CE.xpoly(Or, L[2]), '+': CE.xpoly(Opr, L[3])}
    rows, touch = [], []
    for xj in x[1:n - 1]:
        ke = [k for k in E if E[k](xj) == 0][0]; ko = [k for k in O if O[k](xj) == 0][0]
        dE = E[ke].derivative()(xj); dO = O[ko].derivative()(xj)
        rows.append([(-1) ** (k // 2) * xj ** (k // 2) * dE if k % 2 == 0 else
                     (-1) ** (k // 2) * xj ** (k // 2 + 1) * dO for k in range(n + 1)])
        touch.append((ke + ko, xj))
    return E, O, rows, touch


def closed_numerator_exact(E, O, touch, b, n):
    """Exact proof that b is a closed numerator: each corner residual >= 0 on [0, inf)."""
    for ke in '-+':
        for ko in '-+':
            P = pairing(b, E[ke], O[ko], n)
            q = flint.fmpq_poly([1])
            for kk, xj in touch:
                if kk == ke + ko:
                    q *= flint.fmpq_poly([-xj, 1]) ** 2
            quo, rem = divmod(P, q)
            if rem != 0 or not CE.nonneg_halfline_exact(quo):
                return False
    return True


def span_candidate(E, rows, n):
    comp = CE.nullspace_q([[E['-'][l] for l in range(E['-'].degree() + 1)],
                           [E['+'][l] for l in range(E['+'].degree() + 1)]], E['-'].degree() + 1)
    extra = [[(-1) ** (k // 2) * v[k // 2] if k % 2 == 0 else flint.fmpq(0) for k in range(n + 1)]
             for v in comp]
    basis = CE.nullspace_q(rows + extra, n + 1)
    assert len(basis) == 1
    return basis[0]


def pinall_candidate(x, rows, n):
    r0 = [(-1) ** (k // 2) * x[0] ** (k // 2) if k % 2 == 0 else flint.fmpq(0) for k in range(n + 1)]
    rl = [(-1) ** (k // 2) * x[-1] ** (k // 2) if k % 2 == 1 else flint.fmpq(0) for k in range(n + 1)]
    basis = CE.nullspace_q(rows + [r0, rl], n + 1)
    assert len(basis) == 1
    return basis[0]


def min_over_rationals(E, O, b, n, ts):
    worst = None
    for ke in '-+':
        for ko in '-+':
            P = pairing(b, E[ke], O[ko], n)
            for t in ts:
                v = P(t)
                if worst is None or v < worst[0]:
                    worst = (v, ke + ko, t)
    return worst


def candidates():
    rec = {}
    n = 7
    ts = [CE.fq(Fraction(v).limit_denominator(1000)) for v in np.logspace(-3, 6, 600)]
    # case1 box (closed-feasible by float LP; candidate fails exactly)
    c1 = json.load(open(f'{LANE}/evidence/canon/case1_box.json'))
    x = [CE.fq(Fraction(v).limit_denominator(10 ** 6)) for v in c1['x']]
    L = [CE.fq(Fraction(c1['lam_m']).limit_denominator(10 ** 6)),
         CE.fq(Fraction(c1['lam_p']).limit_denominator(10 ** 6)), flint.fmpq(1), flint.fmpq(1)]
    E, O, rows, touch = fullyclosed_exact(x, L, n)
    WE, WO = E['+'] - E['-'], O['+'] - O['-']
    rec['case1_box_coeffwise'] = bool(all(WE[i] >= 0 for i in range(WE.degree() + 1)) and
                                      all(WO[i] >= 0 for i in range(WO.degree() + 1)))
    b = span_candidate(E, rows, n)
    for sgn, tag in ((1, 'plus'), (-1, 'minus')):
        w = min_over_rationals(E, O, [sgn * v for v in b], n, ts)
        rec[f'span_candidate_case1_{tag}_min'] = {'value_negative': bool(w[0] < 0), 'corner': w[1],
                                                  't': str(w[2])}
    bp = pinall_candidate(x, rows, n)
    for sgn, tag in ((1, 'plus'), (-1, 'minus')):
        w = min_over_rationals(E, O, [sgn * v for v in bp], n, ts)
        rec[f'pinall_candidate_case1_{tag}_min'] = {'value_negative': bool(w[0] < 0), 'corner': w[1],
                                                    't': str(w[2])}
    # positive control for the span candidate: on the O11 box it is an exact closed numerator
    xo = [CE.fq(v) for v in (1, 11, 12, 134, 137, 1505, 1508)]
    Lo = [CE.fq(2240), CE.fq(400), flint.fmpq(1), flint.fmpq(1)]
    E2, O2, rows2, touch2 = fullyclosed_exact(xo, Lo, n)
    b2 = span_candidate(E2, rows2, n)
    ok = closed_numerator_exact(E2, O2, touch2, b2, n) or closed_numerator_exact(E2, O2, touch2, [-v for v in b2], n)
    rec['span_candidate_O11_exact_closed_numerator'] = ok
    # the case1 box itself IS closed-feasible: exact kernel basis, rational combination from a
    # float preconditioned LP, exact residual nonnegativity (so the candidates' failure is theirs)
    rec['case1_box_exact_closed_numerator'] = case1_feasible(E, O, rows, touch, x, n)
    return rec


def case1_feasible(E, O, rows, touch, x, n):
    from scipy.optimize import linprog
    basis = CE.nullspace_q(rows, n + 1)
    Bf = np.array([[float(v) for v in bv] for bv in basis]).T        # (n+1) x 3
    xs = [float(v) for v in x]
    g = np.unique(np.concatenate([[0.0], np.logspace(np.log10(xs[0]) - 4, np.log10(xs[-1]) + 4, 6000)]
                                 + [np.outer(xs, 1 + s * np.logspace(-6, -1, 40)).ravel()
                                    for s in (-1, 1)]))
    rows_f, Ef = [], {k: np.array([float(p[i]) for i in range(p.degree() + 1)]) for k, p in E.items()}
    Of = {k: np.array([float(p[i]) for i in range(p.degree() + 1)]) for k, p in O.items()}
    for ke in '-+':
        for ko in '-+':
            Ev = np.polynomial.polynomial.polyval(g, Ef[ke]); Ov = np.polynomial.polynomial.polyval(g, Of[ko])
            M = np.empty((g.size, n + 1))
            for k in range(n + 1):
                l = k // 2
                M[:, k] = (-1) ** l * g ** l * (Ev if k % 2 == 0 else g * Ov)
            q = np.ones_like(g)
            for kk, xj in touch:
                if kk == ke + ko:
                    q *= (g - float(xj)) ** 2
            R = (M @ Bf) / q[:, None]
            rows_f.append(R / np.linalg.norm(R, axis=1, keepdims=True))
    R = np.vstack(rows_f)
    Q, T = np.linalg.qr(R)
    Qn = Q / np.linalg.norm(Q, axis=1, keepdims=True)
    res = linprog(np.r_[np.zeros(3), -1.0], A_ub=np.hstack([-Qn, np.ones((Qn.shape[0], 1))]),
                  b_ub=np.zeros(Qn.shape[0]), bounds=[(-1, 1)] * 3 + [(None, 1.0)], method='highs')
    if res.status != 0 or res.x[-1] <= 0:
        return False
    yf = np.linalg.solve(T, res.x[:-1]); yf = yf / np.abs(yf).max()
    y = [CE.fq(Fraction(v).limit_denominator(10 ** 9)) for v in yf]
    b = [sum(y[j] * basis[j][i] for j in range(3)) for i in range(n + 1)]
    return closed_numerator_exact(E, O, touch, b, n)


def main():
    t0 = time.time()
    out = {'started': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'flint': flint.__version__}
    out['G1_closed_s21'] = g1_closed('n6_gen_s21')
    out['G1_closed_s22'] = g1_closed('n6_gen_s22')
    out['G1_strict'] = g1_strict()
    out['candidates_n7'] = candidates()
    files = ['evidence/genrect/spec_n6_gen_s21.json', 'evidence/genrect/spec_n6_gen_s22.json',
             'evidence/genrect/cert_n6_gen_s21.json', 'evidence/genrect/cert_n6_gen_s22.json',
             'evidence/genrect/strict_n6_gen_s21_lam999_1000.json', 'evidence/canon/case1_box.json',
             'code/closed_exact.py', 'code/strict_exact.py', 'code/verify_all.py']
    out['sha256'] = {f: sha(f'{LANE}/{f}') for f in files}
    out['seconds'] = round(time.time() - t0, 2)
    json.dump(out, open(sys.argv[1], 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
