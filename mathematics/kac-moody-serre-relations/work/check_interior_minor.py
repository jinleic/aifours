#!/usr/bin/env python3
"""Exact independent checker for the mask-0 degree-222 minor.

Rebuilds the lowering matrix by the independent tensor-word implementation,
then computes its determinant by explicit fraction-free Bareiss elimination in
FLINT's integer multivariate polynomial ring. No SymPy or producer imports.
Scope: all six off-diagonal magnitudes >=2, one degree only.
"""
import argparse
import ast
import copy
import gzip
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import flint
from flint import fmpz_mpoly_ctx
from check_certificate import TensorCoordinates, tensor, word_lowering

EDGES = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_linear(text, ring, variables):
    """Parse only arithmetic expressions in the six named polynomial variables."""
    def walk(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return ring.constant(node.value)
        if isinstance(node, ast.Name) and node.id in variables:
            return variables[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -walk(node.operand)
        if isinstance(node, ast.BinOp):
            left, right = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
        raise ValueError('unexpected polynomial expression syntax')
    return walk(ast.parse(text, mode='eval').body)


def bareiss(matrix, ring):
    entries = [row[:] for row in matrix]
    n = len(entries)
    previous, sign = ring.constant(1), 1
    divisions = 0
    for k in range(n-1):
        pivot_row = next((i for i in range(k, n) if entries[i][k] != 0), None)
        require(pivot_row is not None, 'symbolic rank defect')
        if pivot_row != k:
            entries[k], entries[pivot_row] = entries[pivot_row], entries[k]
            sign = -sign
        pivot = entries[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = entries[i][j]*pivot - entries[i][k]*entries[k][j]
                quotient, remainder = divmod(numerator, previous)
                require(remainder == 0, 'Bareiss division was not exact')
                entries[i][j] = quotient
                divisions += 1
            entries[i][k] = ring.constant(0)
        previous = pivot
    return sign*entries[-1][-1], divisions


def claimed_polynomial(data, ring, determinant):
    terms = {}
    for powers, coefficient in data['polynomial_terms']:
        powers = tuple(powers)
        require(len(powers) == 6 and all(isinstance(p, int) and p >= 0 for p in powers), 'bad monomial')
        require(powers not in terms, 'duplicate monomial')
        value = int(coefficient)
        require(value > 0, 'polynomial is not coefficientwise positive')
        terms[powers] = value
    require(len(terms) == data['monomials'], 'monomial count mismatch')
    require(terms.get((0,)*6, 0) > 0, 'nonpositive constant')
    require(str(terms[(0,)*6]) == data['constant'], 'constant mismatch')
    require(data['orientation'] in (-1, 1), 'bad orientation')
    require(ring.from_dict(terms) == data['orientation']*determinant, 'determinant coefficient identity failed')
    return terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    encoded = args.certificate.read_bytes()
    data = json.loads(gzip.decompress(encoded))
    baseline = [[2 if i == j else -2 for j in range(3)] for i in range(3)]
    require(data['mask'] == 0 and data['baseline_matrix'] == baseline, 'wrong fixed parameter cell')
    require(tuple(map(tuple, data['variable_edges'])) == EDGES, 'wrong variable-edge dictionary')
    require(data['degree'] == [2, 2, 2] and data['quotient_dimension'] == 14, 'wrong root or dimension')
    coordinates = TensorCoordinates(6)
    alpha = (2, 2, 2)
    words = coordinates.words[alpha]
    require(len(words) == 14, 'wrong free dimension')
    targets = []
    for i in range(3):
        previous = tuple(2-int(i == j) for j in range(3))
        targets.extend((i, j) for j in range(len(coordinates.words[previous])))

    def numerical_matrix(cartan):
        result = [[0]*14 for _ in targets]
        for column, word in enumerate(words):
            image = {}
            for i in range(3):
                previous = tuple(2-int(i == j) for j in range(3))
                lowered = coordinates.solve(word_lowering(tensor(word), i, cartan), previous)
                image.update({(i, j): value for j, value in lowered.items()})
            for row, key in enumerate(targets):
                value = Fraction(image.get(key, 0))
                require(value.denominator == 1, 'unexpected nonintegral free lowering')
                result[row][column] = value.numerator
        return result

    constant = numerical_matrix(baseline)
    slopes = []
    for i, j in EDGES:
        shifted = [row[:] for row in baseline]
        shifted[i][j] -= 1
        value = numerical_matrix(shifted)
        slopes.append([[value[r][c]-constant[r][c] for c in range(14)] for r in range(len(targets))])
    ring = fmpz_mpoly_ctx.get(tuple('x'+str(i) for i in range(6)))
    generators = ring.gens()
    variables = dict(zip(('x'+str(i) for i in range(6)), generators))
    rows = data['chosen_rows']
    require(len(rows) == 14 and len(set(rows)) == 14 and all(0 <= r < len(targets) for r in rows), 'invalid maximal minor row set')
    rebuilt = []
    for r in rows:
        rebuilt.append([ring.constant(constant[r][c]) + sum((generators[k]*slopes[k][r][c] for k in range(6)), ring.constant(0)) for c in range(14)])
    require(len(data['minor']) == 14 and all(len(row) == 14 for row in data['minor']), 'wrong saved minor shape')
    require(all(parse_linear(data['minor'][r][c], ring, variables) == rebuilt[r][c] for r in range(14) for c in range(14)), 'saved minor differs from independent word-lowering matrix')
    flint.ctx.threads = 1
    determinant, divisions = bareiss(rebuilt, ring)
    terms = claimed_polynomial(data, ring, determinant)
    mutated = copy.deepcopy(data)
    mutated['polynomial_terms'][0][1] = str(int(mutated['polynomial_terms'][0][1])+1)
    try:
        claimed_polynomial(mutated, ring, determinant)
    except ValueError as error:
        control = {'tampered_coefficient_rejected': True, 'reason': str(error)}
    else:
        raise AssertionError('tampered polynomial accepted')
    result = {'status': 'PASS', 'scope': 'rank3 GCM, all a_ij<=-2 for i!=j, degree(2,2,2) only',
              'certificate_sha256': hashlib.sha256(encoded).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'word_checker_sha256': hashlib.sha256(Path('work/check_certificate.py').read_bytes()).hexdigest(),
              'arithmetic': 'exact integer multivariate polynomials; fraction-free Bareiss with all remainders checked zero',
              'python_flint_version': flint.__version__, 'threads': 1,
              'matrix_dimension': 14, 'monomials': len(terms), 'constant': terms[(0,)*6],
              'total_degree': max(map(sum, terms)), 'exact_divisions': divisions,
              'negative_control': control, 'elapsed_seconds': round(time.monotonic()-start, 3),
              'logical_bridge': 'Serre ideals vanish in degree222 and its immediate lowerings for this cell; coefficient-one theorem identifies the lower maximal quotients. Positive determinant proves joint-lowering injectivity in degree222, not at arbitrary height.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
