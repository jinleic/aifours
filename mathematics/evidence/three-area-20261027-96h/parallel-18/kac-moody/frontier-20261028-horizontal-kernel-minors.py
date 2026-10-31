#!/usr/bin/env python3
"""Exact symbolic f3 minors on actual joint f1/f2 quotient kernels.

All full original ideals and ordinary target relations are retained.  In each
r,s threshold class, horizontal rows and quotient ideal spans are constant;
the remaining f3 matrix is affine in r,s.  Output is a replayable certificate,
not an independent proof or a source/novelty audit.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('minors', ROOT / 'frontier-20261028-symbolic-minors.py')
minors = importlib.util.module_from_spec(spec)
spec.loader.exec_module(minors)
lift = minors.lift


def restrict(vector, selected):
    return {key: c for key, c in vector.items() if key[0] in selected}


def case(degree, rclass, sclass):
    r0 = 4 if rclass == '>=4' else rclass
    s0 = 4 if sclass == '>=4' else sclass
    matrix = lambda r, s: ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    ideals = lift.ideal_bases(degree, matrix(r0, s0))
    source_ideal = ideals.get(degree, lift.Span())
    target_ideal = lift.direct_sum_ideal(ideals, degree)
    source_span = lift.Span()
    for row in source_ideal.rows.values(): source_span.add(row)
    complement = []
    for word, vector in lift.lie_basis(degree):
        if source_span.add(vector) is not None:
            complement.append((word, vector))
    if not complement:
        return {'r_class': rclass, 's_class': sclass,
                'quotient_source_dim': 0, 'horizontal_kernel_dim': 0, 'status': 'ZERO_SOURCE'}
    quotient_delta = [target_ideal.reduce(lift.delta(v, matrix(r0, s0))) for _, v in complement]
    horizontal_columns = [restrict(v, (0, 1)) for v in quotient_delta]
    coefficients = lift.kernel_with_coefficients(horizontal_columns)
    vectors = [lift.combine([v for _, v in complement], coeff) for coeff in coefficients]
    k = len(vectors)
    if not k:
        return {'r_class': rclass, 's_class': sclass, 'quotient_source_dim': len(complement),
                'horizontal_kernel_dim': 0, 'status': 'ZERO_HORIZONTAL_KERNEL'}
    base = [restrict(target_ideal.reduce(lift.delta(v, matrix(r0, s0))), (2,)) for v in vectors]
    dr = [minors.diff(restrict(target_ideal.reduce(lift.delta(v, matrix(r0 + 1, s0))), (2,)), base[j])
          if rclass == '>=4' else {} for j, v in enumerate(vectors)]
    ds = [minors.diff(restrict(target_ideal.reduce(lift.delta(v, matrix(r0, s0 + 1))), (2,)), base[j])
          if sclass == '>=4' else {} for j, v in enumerate(vectors)]
    pivots = lift.Span()
    for v in base:
        if pivots.add(v) is None:
            return {'r_class': rclass, 's_class': sclass, 'quotient_source_dim': len(complement),
                    'horizontal_kernel_dim': k, 'status': 'BASELINE_SINGULAR'}
    rows = sorted(pivots.rows)
    polys = []
    for row in rows:
        entries = []
        for j in range(k):
            p = {}
            if base[j].get(row, 0): p[(0, 0)] = base[j][row]
            if dr[j].get(row, 0): p[(1, 0)] = dr[j][row]
            if ds[j].get(row, 0): p[(0, 1)] = ds[j][row]
            entries.append(p)
        polys.append(entries)
    det = minors.determinant(polys)
    assert det.get((0, 0), 0)
    signs = {1 if c > 0 else -1 for c in det.values()}
    return {
        'r_class': rclass, 's_class': sclass,
        'quotient_source_dim': len(complement), 'horizontal_kernel_dim': k,
        'source_basis_lyndon_words': [''.join(map(str, w)) for w, _ in complement],
        'horizontal_kernel_coefficients': [
            {str(j): lift.rational_text(c) for j, c in sorted(coeff.items())} for coeff in coefficients],
        'target_word_pivots': [f'{i + 1}:' + ''.join(map(str, w)) for i, w in rows],
        'determinant_coefficients': [
            {'x_power': i, 'y_power': j, 'coefficient': lift.rational_text(c)}
            for (i, j), c in sorted(det.items())],
        'status': 'CERTIFIED_ONE_SIGN' if len(signs) == 1 else 'MIXED_SIGNS_NEEDS_ANALYSIS',
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--a', type=int, default=2)
    p.add_argument('--b', type=int, default=2)
    p.add_argument('--n', type=int, default=4)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    degree = (args.a, args.b, args.n)
    if min(degree) < 1 or sum(degree) > 9 or args.n > 4:
        p.error('bounded positive degrees only, total degree <=9 and n<=4')
    classes = (1, 2, 3, '>=4')
    cases = [case(degree, r, s) for r, s in itertools.product(classes, repeat=2)]
    good = ('ZERO_SOURCE', 'ZERO_HORIZONTAL_KERNEL', 'CERTIFIED_ONE_SIGN')
    result = {'degree': degree, 'cases': cases,
              'all_classes_covered': all(c['status'] in good for c in cases),
              'method': 'exact full-ideal quotient, actual joint f1/f2 kernel, symbolic f3 minors',
              'not_a_formal_proof_or_external_review': True}
    dest = args.output.resolve()
    if dest.parent != ROOT or not dest.name.startswith('frontier-20261028-') or dest.exists():
        p.error('new frontier-20261028-* output in owner root required')
    dest.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'degree={degree} classes={len(cases)} covered={sum(c["status"] in good for c in cases)}; {dest.name}')


if __name__ == '__main__':
    main()
