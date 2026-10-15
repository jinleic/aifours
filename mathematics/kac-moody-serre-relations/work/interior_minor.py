#!/usr/bin/env python3
"""Try an exact sign-definite maximal minor at the first interior degree 222.

Each of the six off-diagonal magnitudes is either 1 (mask bit set) or 2+x,
with x>=0. Serre ideals through degree222 depend only on these six mask bits.
A positive-coefficient determinant with positive constant is a sufficient,
not necessary, uniform injectivity certificate on the selected parameter cell.
Run with uv run --with sympy python work/interior_minor.py --mask 0 --output DIR.
"""
import argparse
import gzip
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp
from graded_lie import Field, FreeLie, RowSpace, compute_matrix, descend_factory


EDGES = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))


def unpack(rows):
    return [{j: Fraction(v) for j, v in row} for row in rows]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mask', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert 0 <= args.mask < 64
    start = time.monotonic()
    matrix = [[2 if i == j else -2 for j in range(3)] for i in range(3)]
    variable_edges = []
    for bit, (i, j) in enumerate(EDGES):
        if args.mask >> bit & 1:
            matrix[i][j] = -1
        else:
            variable_edges.append((i, j))
    free = FreeLie(3, 6)
    records = compute_matrix(matrix, free, Field())
    by_degree = {tuple(r['alpha']): r for r in records}
    ideals = {alpha: RowSpace(Field(), unpack(record['ideal_basis'])) for alpha, record in by_degree.items()}
    alpha = (2, 2, 2)
    columns = [j for j in range(len(free.words[alpha])) if j not in ideals[alpha].rows]
    target_coordinates = []
    for i in range(3):
        previous = tuple(2 - int(i == k) for k in range(3))
        target_coordinates.extend((i, j) for j in range(len(free.words[previous])) if j not in ideals[previous].rows)

    def image_matrix(cartan):
        lowering = descend_factory(tuple(map(tuple, cartan)))
        result = []
        for basis_index in columns:
            image = {}
            for i in range(3):
                previous = tuple(2 - int(i == k) for k in range(3))
                raw = free.coordinates(lowering(i, free.words[alpha][basis_index]), previous)
                reduced = ideals[previous].reduce(raw)
                image.update({(i, j): sp.Rational(value.numerator, value.denominator) for j, value in reduced.items()})
            result.append([image.get(key, 0) for key in target_coordinates])
        return sp.Matrix(result).T

    baseline = image_matrix(matrix)
    _, chosen_rows = baseline.T.rref()
    rank = len(chosen_rows)
    variables = sp.symbols('x0:'+str(len(variable_edges)))
    symbolic = baseline.copy()
    for variable, (i, j) in zip(variables, variable_edges):
        shifted = [row[:] for row in matrix]
        shifted[i][j] -= 1
        symbolic += variable * (image_matrix(shifted) - baseline)
    result = {'date': '2026-10-14', 'mask': args.mask, 'baseline_matrix': matrix,
              'variable_edges': variable_edges, 'degree': alpha, 'quotient_dimension': len(columns),
              'baseline_descent_rank': rank, 'chosen_rows': list(chosen_rows),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'claim_limit': 'A failed sign test does not refute injectivity or the book conjecture.'}
    if rank != len(columns):
        result['status'] = 'BASELINE_RANK_DEFECT_REQUIRES_EXACT_AUDIT'
    elif not columns:
        result['status'] = 'ZERO_QUOTIENT'
    else:
        minor = symbolic.extract(list(chosen_rows), list(range(len(columns))))
        determinant = sp.expand(minor.det(method='domain-ge'))
        constant = determinant.subs({v: 0 for v in variables})
        orientation = 1 if constant > 0 else -1
        polynomial = sp.Poly(orientation * determinant, *variables) if variables else None
        coefficients = polynomial.terms() if polynomial is not None else [((), orientation * determinant)]
        positive = all(coefficient >= 0 for _, coefficient in coefficients) and orientation * constant > 0
        result.update({'status': 'POSITIVE_MINOR_CANDIDATE' if positive else 'SIGN_TEST_INCONCLUSIVE',
                       'orientation': orientation, 'constant': str(orientation * constant),
                       'monomials': len(coefficients),
                       'negative_coefficients': sum(1 for _, coefficient in coefficients if coefficient < 0),
                       'polynomial_terms': [[list(powers), str(coefficient)] for powers, coefficient in coefficients],
                       'minor': [[str(x) for x in row] for row in minor.tolist()]})
    result['elapsed_seconds'] = round(time.monotonic()-start, 3)
    args.output.mkdir(parents=True, exist_ok=True)
    path=args.output/f'mask-{args.mask}.json.gz'
    with gzip.open(path, 'wt') as stream:
        json.dump(result, stream, sort_keys=True)
    print(json.dumps({key: value for key, value in result.items() if key not in ('minor','polynomial_terms')}, indent=2))


if __name__ == '__main__':
    main()
