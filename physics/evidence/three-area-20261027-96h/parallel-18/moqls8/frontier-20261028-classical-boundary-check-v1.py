#!/usr/bin/env python3
"""Exact bounded check of one classical 4-MOQLS(8) and its anchored tangent graphs.

This is a reproducible finite example, not an exhaustive search or a proof of
an unrestricted MOQLS statement. All arithmetic is integer/rational. The
full pair-product Gram and row/column conditions are checked directly.
"""
import argparse
import hashlib
import json
import pathlib
import time
from fractions import Fraction

N = 8
SLOPES = (1, 2, 3, 4)


def gf8_mul(a, b):
    result = 0
    for _ in range(3):
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11  # x^3 + x + 1
    return result


def rank_q(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    width = len(a[0])
    rank = 0
    for column in range(width):
        pivot = next((i for i in range(rank, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][column]
        for j in range(column, width):
            a[rank][j] /= pivot_value
        for i in range(rank + 1, len(a)):
            if a[i][column]:
                multiple = a[i][column]
                for j in range(column, width):
                    a[i][j] -= multiple * a[rank][j]
        rank += 1
        if rank == len(a):
            break
    return rank


def check_grams(squares):
    row_errors = col_errors = pair_errors = 0
    for square in squares:
        for line in range(N):
            for j in range(N):
                for k in range(N):
                    row_errors += (square[line][j] == square[line][k]) != (j == k)
                    col_errors += (square[j][line] == square[k][line]) != (j == k)
    for a in range(len(squares)):
        for b in range(a + 1, len(squares)):
            for x in range(N * N):
                i, j = divmod(x, N)
                for y in range(N * N):
                    k, ell = divmod(y, N)
                    gram = (squares[a][i][j] == squares[a][k][ell] and
                            squares[b][i][j] == squares[b][k][ell])
                    pair_errors += gram != (x == y)
    return {'row_errors': row_errors, 'column_errors': col_errors,
            'pair_product_gram_errors': pair_errors}


def rank_and_components(squares, member, p, q):
    left = [(i, j) for i in range(N) for j in range(N)
            if squares[member][i][j] == p]
    right = [(i, j) for i in range(N) for j in range(N)
             if squares[member][i][j] == q]
    if len(left) != N or len(right) != N:
        raise ValueError('non-Latin symbol multiplicity')
    edges = []
    for li, x in enumerate(left):
        for ri, y in enumerate(right):
            matching_classes = int(x[0] == y[0]) + int(x[1] == y[1])
            for b in range(len(squares)):
                if b != member:
                    matching_classes += int(squares[b][x[0]][x[1]] ==
                                            squares[b][y[0]][y[1]])
            if matching_classes > 1:
                raise ValueError('two incidence classes share the same edge')
            if matching_classes:
                edges.append((li, N + ri))
    adjacency = [set() for _ in range(2 * N)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    degrees = sorted(len(neighbors) for neighbors in adjacency)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adjacency[u] - seen:
            seen.add(v)
            stack.append(v)
    anchors = {next(i for i, cell in enumerate(left) if cell[0] == 0),
               N + next(i for i, cell in enumerate(right) if cell[0] == 0)}
    columns = [i for i in range(2 * N) if i not in anchors]
    position = {v: i for i, v in enumerate(columns)}
    matrix = []
    for u, v in edges:
        row = [0] * len(columns)
        if u in position:
            row[position[u]] = 1
        if v in position:
            row[position[v]] = -1
        matrix.append(row)
    return {'edges': len(edges), 'degree_min': min(degrees),
            'degree_max': max(degrees), 'connected_vertices': len(seen),
            'anchored_complex_rank': rank_q(matrix),
            'anchored_complex_variables': len(columns)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.monotonic()
    if any(sorted(gf8_mul(a, b) for b in range(N)) != list(range(N))
           for a in range(1, N)):
        raise ValueError('multiplication table did not provide permutations')
    squares = [[[i ^ gf8_mul(a, j) for j in range(N)] for i in range(N)]
               for a in SLOPES]
    actual = check_grams(squares)
    if any(actual.values()):
        raise ValueError(f'classical input failed its full Gram check: {actual}')
    graph_results = [rank_and_components(squares, a, p, q)
                     for a in range(4) for p in range(N) for q in range(p + 1, N)]
    if any(r != {'edges': 40, 'degree_min': 5, 'degree_max': 5,
                 'connected_vertices': 16, 'anchored_complex_rank': 14,
                 'anchored_complex_variables': 14} for r in graph_results):
        raise ValueError('anchored graph/rank claim failed')
    duplicate_cell = [[row[:] for row in square] for square in squares]
    duplicate_cell[0][0][0] = duplicate_cell[0][0][1]
    bad_row = check_grams(duplicate_cell)
    if bad_row['row_errors'] == 0:
        raise ValueError('duplicate-cell control did not fail row check')
    repeated_square = [[row[:] for row in square] for square in squares]
    repeated_square[1] = [row[:] for row in repeated_square[0]]
    bad_pair = check_grams(repeated_square)
    if bad_pair['row_errors'] or bad_pair['column_errors'] or not bad_pair['pair_product_gram_errors']:
        raise ValueError('repeated-square control did not isolate pair-product failure')
    source_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    result = {
        'result': 'PASS_EXACT_FINITE_CONTROL_NOT_A_NONCLASSICAL_WITNESS',
        'source_sha256': source_hash,
        'dimension': N, 'number_of_squares': 4,
        'field_encoding': 'GF(2)[x]/(x^3+x+1), bit coefficients',
        'slopes': list(SLOPES), 'squares_as_symbol_tables': squares,
        'baseline_full_gram_check': actual,
        'row_and_column_gram_entries_checked': 2 * 4 * N * N * N,
        'pair_product_gram_entries_checked': 6 * (N * N) ** 2,
        'graphs_checked': len(graph_results), 'graph_summary': graph_results[0],
        'total_anchored_real_variables': 4 * 28 * 14 * 2,
        'total_anchored_real_tangent_rank': sum(r['anchored_complex_rank'] * 2
                                                for r in graph_results),
        'duplicate_cell_negative_control': bad_row,
        'repeated_square_negative_control': bad_pair,
        'arithmetic': 'integer labels and fractions.Fraction Gaussian elimination',
        'limits': 'One classical affine input only; no completeness of other Latin families and no nonclassical witness.',
        'elapsed_seconds': time.monotonic() - start,
    }
    output = pathlib.Path(args.output)
    with output.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'squares_as_symbol_tables'}, indent=2))


if __name__ == '__main__':
    main()
