#!/usr/bin/env python3
"""Exact rational near-classical four-array diagnostic, not a quantum witness."""
import argparse
import hashlib
import json
import math
import pathlib
from fractions import Fraction

N = 8
EXPECTED_INPUT_SHA = '5c60f8daa90b66ea7dbd69ad40a62b85bcb1ba2a57fcdcd0a7b75ad1c02442bd'


def inner(a, b):
    return sum((coefficient * b.get(i, Fraction(0)) for i, coefficient in a.items()), Fraction(0))


def qstr(value):
    return str(value.numerator) if value.denominator == 1 else f'{value.numerator}/{value.denominator}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    data = pathlib.Path(args.input).read_bytes()
    input_sha = hashlib.sha256(data).hexdigest()
    if input_sha != EXPECTED_INPUT_SHA:
        raise ValueError('baseline receipt SHA mismatch')
    labels = json.loads(data)['squares_as_symbol_tables']
    if len(labels) != 4 or any(len(s) != N or any(len(row) != N for row in s) for s in labels):
        raise ValueError('incorrect table dimensions')
    arrays = [[[{labels[a][i][j]: Fraction(1)} for j in range(N)]
               for i in range(N)] for a in range(4)]
    # A deliberately nonfeasible exact rational perturbation; the first row stays fixed.
    a, i, j = 0, 1, 0
    p = labels[a][i][j]
    q = (p + 1) % N
    t = Fraction(1, 256)
    cos = (1 - t * t) / (1 + t * t)
    sin = 2 * t / (1 + t * t)
    arrays[a][i][j] = {p: cos, q: sin}
    if any(arrays[a][0][j] != {labels[a][0][j]: Fraction(1)}
           for a in range(4) for j in range(N)):
        raise ValueError('first-row anchor is not exact')
    norm_errors = sum(inner(v, v) != 1 for square in arrays for row in square for v in row)
    if norm_errors:
        raise ValueError('a cell does not have exact unit norm')
    leakage2 = max(sum((value * value for index, value in arrays[a][i][j].items()
                        if index != labels[a][i][j]), Fraction(0))
                   for a in range(4) for i in range(N) for j in range(N))
    root_num, root_den = math.isqrt(leakage2.numerator), math.isqrt(leakage2.denominator)
    if root_num * root_num != leakage2.numerator or root_den * root_den != leakage2.denominator:
        raise ValueError('constructed leakage has no exact rational square root')
    delta = Fraction(root_num, root_den)
    if delta > Fraction(1, 4 * N):
        raise ValueError('constructed input lies outside theorem neighborhood')
    row_max = col_max = product_max = Fraction(0)
    row_diagonal_errors = product_diagonal_errors = 0
    for square in arrays:
        for line in range(N):
            for u in range(N):
                for v in range(N):
                    r = inner(square[line][u], square[line][v])
                    c = inner(square[u][line], square[v][line])
                    if u == v:
                        row_diagonal_errors += (r != 1) + (c != 1)
                    else:
                        row_max = max(row_max, abs(r))
                        col_max = max(col_max, abs(c))
    for aa in range(4):
        for bb in range(aa + 1, 4):
            for x in range(N * N):
                xx, xy = divmod(x, N)
                for y in range(N * N):
                    yx, yy = divmod(y, N)
                    value = (inner(arrays[aa][xx][xy], arrays[aa][yx][yy]) *
                             inner(arrays[bb][xx][xy], arrays[bb][yx][yy]))
                    if x == y:
                        product_diagonal_errors += value != 1
                    else:
                        product_max = max(product_max, abs(value))
    if row_diagonal_errors or product_diagonal_errors:
        raise ValueError('Gram diagonal did not retain exact unit norms')
    residual = max(row_max, col_max, product_max)
    lower = 3 * delta / (32 * N)
    stronger = (1 - 2 * delta * delta) * (delta / (2 * N) - delta * delta * (1 + 2 * delta))
    if not (residual >= lower and residual >= stronger and residual > 0):
        raise ValueError('quantitative residual inequality failed')
    result = {
        'result': 'PASS_EXACT_NEARBY_NONFEASIBLE_DIAGNOSTIC',
        'source_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': input_sha, 'perturbed_cell': [a, i, j],
        'original_and_added_symbol': [p, q], 'parameter_t': qstr(t),
        'cos': qstr(cos), 'sin': qstr(sin), 'delta': qstr(delta),
        'all_cell_norm_errors': norm_errors, 'first_row_reference_exact': True,
        'row_max_offdiagonal': qstr(row_max), 'column_max_offdiagonal': qstr(col_max),
        'pair_product_max_offdiagonal': qstr(product_max),
        'row_column_gram_entries_checked': 2 * 4 * N * N * N,
        'pair_product_gram_entries_checked': 6 * (N * N) ** 2,
        'max_residual': qstr(residual), 'simple_proved_lower_bound': qstr(lower),
        'sharper_proved_lower_bound': qstr(stronger),
        'arithmetic': 'exact real fractions; no rounding',
        'limits': 'One deliberately invalid nearby input; this is not a nonclassical MOQLS witness or universal proof.',
    }
    with pathlib.Path(args.output).open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
