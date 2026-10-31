#!/usr/bin/env python3
"""General exact two-minor resultant certificate for one level-six primitive type.

For degree (a,b,6) on r,s>=6 (x=r-6,y=s-6) this computes two actual maximal
minors of the full affine D3 pencil (the baseline selected rows and the same
rows with one slot replaced), factors both exactly, separates factors that are
strictly positive on the closed quadrant (all coefficients positive) from the
remaining "bad" factors, and for every bad pair computes the exact resultant in
a variable where both leading coefficients are constant.  Integer roots of each
resultant are determined by its exact squarefree part and a Hensel/Cauchy
certificate.  Any common integer zero in the quadrant is reported and the full
matrix rank is computed there exactly.  Exact computation for review, not a
formal proof; source identification is a separate written input.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


al6 = load('al6', 'frontier-20261028-level6-alternate-type-minor-search.py')
h = al6.h
S = load('sympyhelper', 'frontier-review-f18-ph7-independent-check.py').S
x, y = S.symbols('x y')


def trim(v):
    while v and v[-1] == 0:
        v.pop()
    return v


def evalmod(c, t, m):
    z = 0
    for a in reversed(c):
        z = (z * t + a) % m
    return z


def gcd_modp(a, b, p):
    a = trim([v % p for v in a])
    b = trim([v % p for v in b])
    while b:
        inv = pow(b[-1], -1, p)
        while len(a) >= len(b) and a:
            d = len(a) - len(b)
            f = a[-1] * inv % p
            for j, c in enumerate(b):
                a[j + d] = (a[j + d] - f * c) % p
            a = trim(a)
        a, b = b, a
    return a


def interpolate(values, n):
    work = values[:n + 1]
    delta = []
    while work:
        delta.append(work[0])
        work = [b - a for a, b in zip(work, work[1:])]
    facts = [1] * (n + 1)
    for k in range(1, n + 1):
        facts[k] = facts[k - 1] * k
    acc = [0] * (n + 1)
    ff = [1]
    for k, dk in enumerate(delta):
        if k:
            nxt = [0] * (len(ff) + 1)
            for j, c in enumerate(ff):
                nxt[j] -= (k - 1) * c
                nxt[j + 1] += c
            ff = nxt
        if dk:
            sc = dk * (facts[n] // facts[k])
            for j, c in enumerate(ff):
                if c:
                    acc[j] += sc * c
    out = []
    for a in acc:
        q, r = divmod(a, facts[n])
        assert r == 0
        out.append(q)
    return trim(out)


def peval(c, t):
    z = 0
    for a in reversed(c):
        z = z * t + a
    return z


def integer_roots(c):
    """All integer roots of a squarefree integer polynomial via Cauchy bound and Hensel uniqueness."""
    dc = [i * c[i] for i in range(1, len(c))]
    cauchy = 1 + -(-max(abs(v) for v in c[:-1]) // abs(c[-1]))
    p = 1000
    while True:
        p += 1
        if all(p % d for d in range(2, math.isqrt(p) + 1)) and c[-1] % p and len(gcd_modp(c, dc, p)) == 1:
            break
    roots = [r for r in range(p) if evalmod(c, r, p) == 0]
    modulus = p
    while modulus <= 2 * cauchy:
        modulus *= p
    found = []
    for r in roots:
        a, m = r, p
        while m < modulus:
            m = min(m * m, modulus)
            a = (a - evalmod(c, a, m) * pow(evalmod(dc, a, m), -1, m)) % m
        if a > modulus // 2:
            a -= modulus
        if abs(a) <= cauchy and peval(c, a) == 0:
            found.append(a)
    return sorted(found), {'prime': p, 'roots_mod_p': len(roots), 'cauchy_digits': len(str(cauchy)),
                           'modulus_digits': len(str(modulus))}


def poly_terms(poly):
    return [{'x_power': i, 'y_power': j, 'coefficient': str(c)}
            for (i, j), c in sorted(zip(poly.monoms(), poly.coeffs()))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--slot', type=int, required=True)
    ap.add_argument('--word', required=True)
    args = ap.parse_args()
    name = f'frontier-20261028-level6-free-{args.a}{args.b}-pencil-v1.json'
    raw = (ROOT / name).read_bytes()
    P = json.loads(raw)
    out = ROOT / f'frontier-20261028-level6-{args.a}{args.b}6-two-minor-certificate-v1.json'
    if out.exists():
        raise FileExistsError(out)
    rows = al6.full_rows(P)
    selected = P['selected_target_words']
    assert args.word in rows and args.word not in selected
    trial = selected[:]
    trial[args.slot] = args.word

    def minor(words):
        data, scale = h.int_rows([rows[w] for w in words])
        coeff = h.polynomial(data, scale, {})
        return S.Poly(sum(S.Rational(q.numerator, q.denominator) * x**i * y**j
                          for (i, j), q in coeff.items()), x, y)

    minors = {'P1': minor(selected), 'P2': minor(trial)}
    factor_report = {}
    bad = {}
    for key, poly in minors.items():
        content, factors = S.factor_list(poly.as_expr())
        rebuilt = S.Poly(content, x, y)
        entries = []
        bad[key] = []
        for g, m in factors:
            gp = S.Poly(g, x, y)
            rebuilt *= gp**m
            coeffs = gp.coeffs()
            positive = gp.coeff_monomial(1) != 0 and (all(c > 0 for c in coeffs) or all(c < 0 for c in coeffs))
            entries.append({'multiplicity': m, 'total_degree': gp.total_degree(), 'terms': len(coeffs),
                            'strictly_positive_on_quadrant': positive, 'coefficients': poly_terms(gp)})
            if not positive:
                bad[key].append(gp)
        assert rebuilt == poly
        factor_report[key] = {'content': str(content), 'factors': entries, 'terms': len(poly.terms())}
    pairs = []
    unresolved = []
    for B in bad['P1']:
        for C in bad['P2']:
            assert S.gcd(B, C).total_degree() == 0, 'shared bad factor'
            var = None
            for v in (x, y):
                if S.Poly(B, v).LC().is_number and S.Poly(C, v).LC().is_number:
                    var = v
                    break
            assert var is not None, 'no variable with constant leading coefficients'
            other = y if var == x else x
            Bd = {m: int(c) for m, c in zip(B.monoms(), B.coeffs())}
            Cd = {m: int(c) for m, c in zip(C.monoms(), C.coeffs())}
            idx = 0 if var == x else 1
            mB, mC = S.Poly(B, var).degree(), S.Poly(C, var).degree()
            t = S.Symbol('t')

            def spec(d, t0, n):
                v = [0] * (n + 1)
                for mon, c in d.items():
                    v[mon[idx]] += c * t0**mon[1 - idx]
                return v

            bound = B.total_degree() * C.total_degree()
            values = []
            for t0 in range(bound + 9):
                f = S.Poly(list(reversed(spec(Bd, t0, mB))), t)
                g = S.Poly(list(reversed(spec(Cd, t0, mC))), t)
                assert f.degree() == mB and g.degree() == mC
                values.append(int(S.resultant(f, g)))
            H = interpolate(values, bound)
            assert H and all(peval(H, t0) == v for t0, v in enumerate(values))
            HP = S.Poly(list(reversed(H)), t, domain=S.ZZ)
            G = S.gcd(HP, HP.diff(t))
            W, rem = S.div(HP, G)
            assert rem.is_zero
            Wc = [int(c) for c in reversed(W.all_coeffs())]
            roots, cert = integer_roots(Wc)
            linear = []
            for g, m in S.factor_list(G.as_expr())[1]:
                gp = S.Poly(g, t)
                if gp.degree() == 1:
                    a_, b_ = [int(c) for c in gp.all_coeffs()]
                    linear.append([a_, b_, m + 1])
            fibres = []
            for t0 in [r for r in roots if r >= 0]:
                fB = S.Poly(list(reversed(spec(Bd, t0, mB))), t)
                fC = S.Poly(list(reversed(spec(Cd, t0, mC))), t)
                common = S.gcd(fB, fC)
                ints = [int(r) for r in S.Poly(common, t).ground_roots() if r.is_integer and r >= 0] if common.degree() > 0 else []
                fibres.append({'fixed_' + str(other): t0, 'common_gcd_degree': common.degree(),
                               'nonnegative_integer_common_roots': ints})
                for r in ints:
                    point = (r, t0) if var == x else (t0, r)
                    unresolved.append(point)
            pairs.append({'P1_factor_total_degree': B.total_degree(), 'P2_factor_total_degree': C.total_degree(),
                          'eliminated_variable': str(var), 'resultant_variable': str(other),
                          'resultant_degree': len(H) - 1, 'resultant_degree_bound': bound,
                          'grid_values_checked': len(values),
                          'resultant_coefficients_low_to_high': [str(c) for c in H],
                          'repeated_part_degree': G.degree(), 'repeated_part_linear_factors_a_t_plus_b_mult_in_H': linear,
                          'squarefree_part_degree': W.degree(), 'squarefree_part_integer_roots': roots,
                          'hensel_certificate': cert, 'nonnegative_integer_root_fibres': fibres})
    ranks = []
    for (x0, y0) in sorted(set(unresolved)):
        mat = [[e[0] + x0 * e[1] + y0 * e[2] for e in rows[w]] for w in rows]
        span = al6.lift.Span()
        for j in range(len(mat[0])):
            span.add({i: mat[i][j] for i in range(len(mat)) if mat[i][j]})
        ranks.append({'x': x0, 'y': y0, 'rank': len(span), 'columns': len(mat[0])})
    k = len(rows[selected[0]])
    injective_everywhere = all(r['rank'] == k for r in ranks)
    status = 'ALL_INTEGER_QUADRANT_POINTS_FULL_RANK' if injective_everywhere else 'RANK_DEFECT_FOUND'
    result = {
        'degree': [args.a, args.b, 6], 'variables': 'x=r-6,y=s-6', 'pencil': name,
        'pencil_sha256': hashlib.sha256(raw).hexdigest(), 'full_target_rows': len(rows), 'columns': k,
        'selected_rows': selected, 'second_minor_rows': trial, 'replaced_slot': args.slot, 'new_word': args.word,
        'minor_factorizations': factor_report, 'bad_pairs': pairs,
        'common_integer_quadrant_zeros_of_bad_pairs': [list(p) for p in sorted(set(unresolved))],
        'direct_rank_checks': ranks, 'status': status,
        'scope': 'exact certificate on the free-Levi pencil; actual source identification for r,s>=6 is a written input',
        'not_formal_or_external_model_review': True,
    }
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('DONE', (args.a, args.b, 6), status, 'pairs', len(pairs), 'unresolved', len(set(unresolved)), out.name, flush=True)


if __name__ == '__main__':
    main()
