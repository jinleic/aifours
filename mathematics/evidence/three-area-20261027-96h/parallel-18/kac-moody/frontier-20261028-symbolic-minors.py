#!/usr/bin/env python3
"""Find exact parameter-polynomial full-column minors for a fixed root degree.

For each threshold class r,s in {1,2,3,>=4}, the complete positive Serre
ideal at degree alpha_3=4 is constant.  Delta is affine in r,s.  All target
ideals are reduced in the ACTUAL direct sum, not individually optimized.
The determinant is computed as a polynomial in x=r-4 and y=s-4 using exact
fractions and subset dynamic programming.  A one-signed coefficient list
certifies nonvanishing for every nonnegative x,y, if its constant is nonzero.
"""
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lift_exact', ROOT / 'frontier-20261028-lift-exact.py')
lift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lift)


def add(p, q):
    out = dict(p)
    for mon, c in q.items():
        out[mon] = out.get(mon, Fraction(0)) + c
        if not out[mon]:
            del out[mon]
    return out


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, Fraction(0)) + a * b
    return {m: c for m, c in out.items() if c}


def scale(p, x):
    return {m: c * x for m, c in p.items() if c * x}


def determinant(matrix):
    n = len(matrix)
    states = {0: {(0, 0): Fraction(1)}}
    for i in range(n):
        nxt = {}
        for mask, partial in states.items():
            for j in range(n):
                if mask & (1 << j):
                    continue
                # Expanding in original column order; count earlier selected columns greater than j.
                inversion = sum(bool(mask & (1 << k)) for k in range(j + 1, n))
                term = mul(partial, matrix[i][j])
                if inversion & 1:
                    term = scale(term, -1)
                newmask = mask | (1 << j)
                nxt[newmask] = add(nxt.get(newmask, {}), term)
        states = nxt
    return states.get((1 << n) - 1, {})


def diff(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) - value
        if not out[key]:
            del out[key]
    return out


def term_text(q):
    q = Fraction(q)
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def case(degree, rclass, sclass):
    r0 = 4 if rclass == '>=4' else rclass
    s0 = 4 if sclass == '>=4' else sclass
    matrix = lambda r, s: ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    ideals = lift.ideal_bases(degree, matrix(r0, s0))
    source_ideal = ideals.get(degree, lift.Span())
    target_ideal = lift.direct_sum_ideal(ideals, degree)
    # Extend the ACTUAL ideal span with source vectors to get a quotient basis.
    source_span = lift.Span()
    for row in source_ideal.rows.values():
        source_span.add(row)
    complement = []
    for word, vector in lift.lie_basis(degree):
        if source_span.add(vector) is not None:
            complement.append((word, vector))
    m = len(complement)
    if not m:
        return {'r_class': rclass, 's_class': sclass, 'quotient_source_dim': 0,
                'status': 'ZERO_SOURCE'}
    base = [target_ideal.reduce(lift.delta(v, matrix(r0, s0))) for _, v in complement]
    dr = [diff(target_ideal.reduce(lift.delta(v, matrix(r0 + 1, s0))), base[j])
          if rclass == '>=4' else {} for j, (_, v) in enumerate(complement)]
    ds = [diff(target_ideal.reduce(lift.delta(v, matrix(r0, s0 + 1))), base[j])
          if sclass == '>=4' else {} for j, (_, v) in enumerate(complement)]
    pivots = lift.Span()
    for col in base:
        if pivots.add(col) is None:
            return {'r_class': rclass, 's_class': sclass, 'quotient_source_dim': m,
                    'status': 'BASELINE_SINGULAR'}
    rows = sorted(pivots.rows)
    assert len(rows) == m
    polys = []
    for row in rows:
        prow = []
        for j in range(m):
            p = {}
            if base[j].get(row, 0): p[(0, 0)] = base[j][row]
            if dr[j].get(row, 0): p[(1, 0)] = dr[j][row]
            if ds[j].get(row, 0): p[(0, 1)] = ds[j][row]
            prow.append(p)
        polys.append(prow)
    det = determinant(polys)
    assert det.get((0, 0), 0), 'selected minor was not invertible at its baseline'
    signs = {1 if c > 0 else -1 for c in det.values()}
    one_signed = len(signs) == 1
    return {
        'r_class': rclass, 's_class': sclass,
        'quotient_source_dim': m,
        'source_basis_lyndon_words': [''.join(map(str, word)) for word, _ in complement],
        'target_word_pivots': [f'{i + 1}:'.replace(' ', '') + ''.join(map(str, word)) for i, word in rows],
        'determinant_coefficients': [
            {'x_power': i, 'y_power': j, 'coefficient': term_text(c)}
            for (i, j), c in sorted(det.items())
        ],
        'x_means_r_minus_4': rclass == '>=4',
        'y_means_s_minus_4': sclass == '>=4',
        'status': 'CERTIFIED_ONE_SIGN' if one_signed else 'MIXED_SIGNS_NEEDS_ANALYSIS',
    }


def main():
    degree = (2, 1, 4)
    classes = (1, 2, 3, '>=4')
    cases = [case(degree, r, s) for r, s in itertools.product(classes, repeat=2)]
    result = {
        'selected_degree': degree,
        'method': 'exact symbolic full-column minor on full actual target quotient; x=r-4,y=s-4',
        'cases': cases,
        'all_parameter_classes_algebraically_covered': all(
            c['status'] in ('ZERO_SOURCE', 'CERTIFIED_ONE_SIGN') for c in cases),
        'not_a_machine_checked_formal_proof': True,
    }
    out = ROOT / 'frontier-20261028-214-symbolic-minors-v1.json'
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f"classes={len(cases)} one-signed-or-zero={sum(c['status'] in ('ZERO_SOURCE', 'CERTIFIED_ONE_SIGN') for c in cases)}; {out.name}")


if __name__ == '__main__':
    main()
