#!/usr/bin/env python3
"""Independently replay actual horizontal-kernel symbolic minors.

Uses independent nested-word/ideal construction and Gauss-Jordan from the
standalone 214 replay, not the producer's Lie engine.  Reconstructs the FULL
f1/f2 quotient map, verifies the advertised kernel basis spans its entire
kernel, and exactly interpolates each f3 determinant polynomial.
"""
import importlib.util
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('independent', ROOT / 'frontier-20261028-214-independent-replay.py')
ind = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ind)


def combo(vectors, coefficients):
    out = {}
    for k, c in coefficients.items():
        ind.add_scaled(out, vectors[int(k)], Q(c))
    return out


def direct_target(degree, r, s):
    output = []
    for i in range(3):
        target = list(degree)
        target[i] -= 1
        if min(target) < 0:
            continue
        for v in ind.formal_ideal_generators(tuple(target), r, s):
            output.append({f'{i + 1}:{w}': c for w, c in v.items()})
    return ind.ReducedSpace(output)


def limited(vector, prefixes):
    return {k: v for k, v in vector.items() if k.startswith(prefixes)}


def replay(degree, case):
    ind.ALPHA = tuple(degree)
    rc, sc = case['r_class'], case['s_class']
    r0 = 4 if rc == '>=4' else rc
    s0 = 4 if sc == '>=4' else sc
    source = ind.ReducedSpace(ind.nested(w) for w in ind.words(ind.ALPHA))
    ideal_generators = ind.formal_ideal_generators(ind.ALPHA, r0, s0)
    ideal = ind.ReducedSpace(ideal_generators)
    for v in ideal.pivots.values(): assert not source.remainder(v)
    m = case['quotient_source_dim']
    assert len(source) - len(ideal) == m
    if case['status'] == 'ZERO_SOURCE':
        assert m == 0
        return {'r_class': rc, 's_class': sc, 'status': 'PASS_ZERO_SOURCE', 'determinant_checks': 0}
    basis = [ind.standard_bracket(w) for w in case['source_basis_lyndon_words']]
    combined = ind.ReducedSpace(ideal_generators)
    for v in basis:
        assert not source.remainder(v)
        assert combined.insert(v)
    assert len(combined) == len(source)
    target = direct_target(degree, r0, s0)
    def projected(v, r, s):
        return target.remainder(ind.delta(v, r, s))
    directions = [(r0, s0)]
    if rc == '>=4': directions.append((r0 + 1, s0))
    if sc == '>=4': directions.append((r0, s0 + 1))
    for r, s in directions:
        for v in ideal.pivots.values(): assert not projected(v, r, s)
    horiz = [limited(projected(v, r0, s0), ('1:', '2:')) for v in basis]
    horizontal_rank = len(ind.ReducedSpace(horiz))
    k = case['horizontal_kernel_dim']
    assert m - horizontal_rank == k, ('horizontal kernel dimension', degree, rc, sc)
    if case['status'] == 'ZERO_HORIZONTAL_KERNEL':
        assert k == 0
        return {'r_class': rc, 's_class': sc, 'status': 'PASS_ZERO_HORIZONTAL_KERNEL',
                'determinant_checks': 0}
    coeffs = case['horizontal_kernel_coefficients']
    assert len(coeffs) == k
    coeff_vectors = [{int(j): Q(c) for j, c in row.items()} for row in coeffs]
    assert len(ind.ReducedSpace(coeff_vectors)) == k, 'kernel vectors dependent'
    vectors = [combo(basis, row) for row in coeff_vectors]
    for v in vectors:
        for r, s in directions:
            assert not limited(projected(v, r, s), ('1:', '2:')), 'horizontal vector not in quotient kernel'
    rows = case['target_word_pivots']
    assert len(rows) == k and len(set(rows)) == k and all(x.startswith('3:') for x in rows)
    polynomial = case['determinant_coefficients']
    assert Q(next(x['coefficient'] for x in polynomial if x['x_power'] == 0 and x['y_power'] == 0)) != 0
    assert all(Q(x['coefficient']) > 0 for x in polynomial) or all(Q(x['coefficient']) < 0 for x in polynomial)
    xs = range(k + 1) if rc == '>=4' else range(1)
    ys = range(k + 1) if sc == '>=4' else range(1)
    checks = 0
    for x, y in itertools.product(xs, ys):
        r = r0 + x if rc == '>=4' else r0
        s = s0 + y if sc == '>=4' else s0
        cols = [limited(projected(v, r, s), ('3:',)) for v in vectors]
        mat = [[cols[j].get(row, Q(0)) for j in range(k)] for row in rows]
        assert ind.determinant(mat) == ind.eval_polynomial(polynomial, x, y), ('minor mismatch', degree, rc, sc, x, y)
        checks += 1
    return {'r_class': rc, 's_class': sc, 'quotient_source_dim': m,
            'horizontal_kernel_dim': k, 'status': 'PASS_SPAN_GRID_AND_SIGN',
            'determinant_checks': checks}


def main():
    source = json.loads((ROOT / 'frontier-20261028-224-horizontal-minors-v1.json').read_text(encoding='utf-8'))
    alternate = json.loads((ROOT / 'frontier-20261028-224-alternate-minors-v1.json').read_text(encoding='utf-8'))
    alt = {(c['r_class'], c['s_class']): c for c in alternate['cases']}
    cases = [alt.get((c['r_class'], c['s_class']), c) for c in source['cases']]
    assert len(cases) == 16
    rows = [replay(source['degree'], c) for c in cases]
    out = ROOT / 'frontier-20261028-224-horizontal-independent-replay-v1.json'
    if out.exists(): raise FileExistsError(out)
    out.write_text(json.dumps({'degree': source['degree'], 'cases': rows,
                              'all_classes_passed': True,
                              'determinant_evaluations': sum(r['determinant_checks'] for r in rows),
                              'not_a_formal_proof_or_external_review': True}, indent=2) + '\n', encoding='utf-8')
    print('PASS: 16 classes; joint horizontal quotient kernel and',
          sum(r['determinant_checks'] for r in rows), 'exact determinants;', out.name)


if __name__ == '__main__': main()
