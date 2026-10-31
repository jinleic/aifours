#!/usr/bin/env python3
"""Two-minor resultant certificate for the level-six (2,2,6) primitive map.

Inputs are the independently replayed 235-row affine target matrix, the pinned
first selected 34x34 minor and its pinned 21-degree factor R.  A SECOND minor
(selected rows, slot 0 replaced by target word 00601) is computed exactly by
total-degree interpolation and factored.  The exact resultant H=Res_y(R,R2) is
computed by exact univariate resultants on an integer grid plus interpolation.
All explicit linear factors are divided out exactly and a p-adic Hensel
certificate shows the cofactor has no integer root.  This is exact computation
for review, not a formal proof; source identification stays a written input.
"""
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


h = load('helpers', 'frontier-20261028-level5-35-alternate-minor-search.py')
S = load('sympyhelper', 'frontier-review-f18-ph7-independent-check.py').S

PINS = {
    'frontier-20261028-level6-226-ratio-cone-certificate-v1.json':
        'ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b',
    'frontier-20261028-level6-free-22-pencil-v1.json':
        'b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc',
    'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json':
        '5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297',
}
LINEAR = [(1, 5, 11), (1, 6, 18), (1, 4, 18), (1, 3, 3), (1, 2, 2), (1, 1, 1), (4, 19, 16)]


def pinned(name):
    raw = (ROOT / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PINS[name], name
    return json.loads(raw)


def evalmod(c, x, m):
    z = 0
    for a in reversed(c):
        z = (z * x + a) % m
    return z


def trim(v):
    while v and v[-1] == 0:
        v.pop()
    return v


def gcd_modp(a, b, p):
    a = trim([x % p for x in a])
    b = trim([x % p for x in b])
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


def divide_linear(c, a, b):
    """Exact division of integer poly c (low-to-high) by (a*x+b); return quotient or None."""
    n = len(c) - 1
    q = [Q(0)] * n
    rem = [Q(v) for v in c]
    for i in range(n, 0, -1):
        q[i - 1] = rem[i] / a
        rem[i] -= q[i - 1] * a
        rem[i - 1] -= q[i - 1] * b
    if rem[0] != 0 or any(v.denominator != 1 for v in q):
        return None
    return [int(v) for v in q]


def main():
    out = ROOT / 'frontier-20261028-level6-226-two-minor-resultant-v1.json'
    if out.exists():
        raise FileExistsError(out)
    C = pinned('frontier-20261028-level6-226-ratio-cone-certificate-v1.json')
    P = pinned('frontier-20261028-level6-free-22-pencil-v1.json')
    RJ = pinned('frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json')
    rows = {w: [[Q(q) for q in e] for e in row]
            for w, row in zip(C['target_word_rows'], C['full_target_affine_entries'])}
    assert len(rows) == 235
    selected = P['selected_target_words']
    assert len(selected) == 34 and '00601' not in selected
    for w, m in zip(selected, P['matrix']):
        assert rows[w] == [[Q(q) for q in e] for e in m]
    trial = selected[:]
    trial[0] = '00601'
    x, y = S.symbols('x y')

    def minor(words):
        data, scale = h.int_rows([rows[w] for w in words])
        coeff = h.polynomial(data, scale, {})
        return S.Poly(sum(S.Rational(q.numerator, q.denominator) * x**i * y**j
                          for (i, j), q in coeff.items()), x, y)

    P1 = minor(selected)
    P2 = minor(trial)
    R = S.Poly(sum(S.Integer(int(t['coefficient'])) * x**t['x_power'] * y**t['y_power']
                   for t in RJ['R_coefficients']), x, y)
    assert P1 == S.Poly(393216 * (x + 5)**4 * (y + 5)**7 * (2 * x + 2 * y + 19)**2, x, y) * R
    cof2 = S.Poly(-3145728 * (x + 5)**3 * (y + 5)**7 * (2 * x + 2 * y + 19)**2, x, y)
    R2, rem = S.div(P2, cof2)
    assert rem.is_zero and R2 * cof2 == P2
    R2d = {m: c for m, c in zip(R2.monoms(), R2.coeffs())}
    assert all(c.is_Integer for c in R2d.values())
    R2d = {m: int(c) for m, c in R2d.items()}
    assert math.gcd(*R2d.values()) == 1
    assert max(i + j for i, j in R2d) == 22 and R2d.get((0, 22)) == 44255232
    assert all(j < 22 for (i, j) in R2d if (i, j) != (0, 22))
    Rd = {m: int(c) for m, c in zip(R.monoms(), R.coeffs())}
    assert max(i + j for i, j in Rd) == 21 and Rd.get((0, 21)) == 2107392

    def spec(d, x0, n):
        v = [0] * (n + 1)
        for (i, j), c in d.items():
            v[j] += c * x0**i
        return v

    def resultant(x0):
        f = S.Poly(list(reversed(spec(Rd, x0, 21))), y)
        g = S.Poly(list(reversed(spec(R2d, x0, 22))), y)
        assert f.degree() == 21 and g.degree() == 22
        return int(S.resultant(f, g))

    bound = 21 * 22
    values = [resultant(x0) for x0 in range(bound + 9)]
    work = values[:bound + 1]
    delta = []
    while work:
        delta.append(work[0])
        work = [b - a for a, b in zip(work, work[1:])]
    coef = [Q(0)] * (bound + 1)
    ff = [1]
    fact = 1
    for k, dk in enumerate(delta):
        if k:
            fact *= k
            nxt = [0] * (len(ff) + 1)
            for j, c in enumerate(ff):
                nxt[j] -= (k - 1) * c
                nxt[j + 1] += c
            ff = nxt
        if dk:
            for j, c in enumerate(ff):
                coef[j] += Q(dk * c, fact)
    assert all(c.denominator == 1 for c in coef)
    H = trim([int(c) for c in coef])
    assert all(sum(c * x0**i for i, c in enumerate(H)) == v for x0, v in enumerate(values))
    H2 = H[:]
    for a, b, m in LINEAR:
        for _ in range(m):
            H2 = divide_linear(H2, a, b)
            assert H2 is not None
        assert divide_linear(H2, a, b) is None
    lc = abs(H2[-1])
    cauchy = 1 + -(-max(abs(c) for c in H2[:-1]) // lc)
    dH2 = [i * H2[i] for i in range(1, len(H2))]
    p = 1000
    while True:
        p += 1
        if all(p % d for d in range(2, math.isqrt(p) + 1)) and H2[-1] % p and len(gcd_modp(H2, dH2, p)) == 1:
            break
    roots = [r for r in range(p) if evalmod(H2, r, p) == 0]
    modulus = p
    while modulus <= 2 * cauchy:
        modulus *= p
    lifts = []
    for r in roots:
        a, m = r, p
        while m < modulus:
            m = min(m * m, modulus)
            a = (a - evalmod(H2, a, m) * pow(evalmod(dH2, a, m), -1, m)) % m
        if a > modulus // 2:
            a -= modulus
        within = abs(a) <= cauchy
        is_root = within and sum(c * a**i for i, c in enumerate(H2)) == 0
        lifts.append({'root_mod_p': r, 'symmetric_lift': str(a), 'within_cauchy_bound': within,
                      'exact_root': is_root})
    assert not any(e['exact_root'] for e in lifts)
    result = {
        'degree': [2, 2, 6], 'variables': 'x=r-6,y=s-6',
        'second_minor_rows': trial, 'replaced_slot_zero_based': 0, 'replaced_word': selected[0],
        'new_word': '00601', 'P2_terms': len(P2.terms()),
        'P2_coefficients': [{'x_power': i, 'y_power': j, 'coefficient': str(c)}
                            for (i, j), c in sorted(zip(P2.monoms(), P2.coeffs()))],
        'P2_factorization': '-3145728*(x+5)^3*(y+5)^7*(2x+2y+19)^2*R2',
        'R2_coefficients': [{'x_power': i, 'y_power': j, 'coefficient': str(c)}
                            for (i, j), c in sorted(R2d.items())],
        'R2_total_degree': 22, 'R2_y_leading_constant': 44255232,
        'H_definition': 'H(x)=Res_y(R,R2) with formal y-degrees 21,22 (both leading coefficients constant)',
        'H_degree': len(H) - 1, 'H_degree_bound': bound, 'H_grid_values_checked': len(values),
        'H_coefficients_low_to_high': [str(c) for c in H],
        'explicit_linear_factors_a_x_plus_b_multiplicity': LINEAR,
        'H2_degree': len(H2) - 1, 'H2_leading_coefficient': str(H2[-1]),
        'H2_cauchy_root_bound_digits': len(str(cauchy)), 'hensel_prime': p,
        'H2_squarefree_mod_p': True, 'H2_roots_mod_p': len(roots),
        'hensel_modulus_digits': len(str(modulus)), 'lifts': lifts,
        'conclusion': 'H(x0)!=0 for every integer x0>=0: all listed linear factors are positive there and H2 has no integer root',
        'status': 'NO_COMMON_ZERO_OF_R_AND_R2_ON_ANY_INTEGER_FIBRE_X_GE_0',
        'scope': 'exact polynomial/resultant certificate on the pinned replayed affine matrix; source identification is a written input',
        'not_formal_or_external_model_review': True,
    }
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS H degree', len(H) - 1, 'H2 degree', len(H2) - 1, 'p', p, 'roots', len(roots),
          'within-bound lifts', sum(e['within_cauchy_bound'] for e in lifts), out.name, flush=True)


if __name__ == '__main__':
    main()
