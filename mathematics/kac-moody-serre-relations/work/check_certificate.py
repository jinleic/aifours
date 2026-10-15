#!/usr/bin/env python3
"""Independent, scope-bound exact-Q checker for bounded I=K certificates.

No producer imports. Lowering is derived in associative words by commuting
Cartan factors right, not by the producer's recursive bracket derivation.
Exact Serre spans are recomputed. Once lower-degree I=K is established,
injectivity on L_alpha/I_alpha proves the next equality; testing only these
quotient columns avoids repeatedly checking the already-proved ideal.
This checker explicitly REFUSES nonzero-defect certificates. Such a candidate
requires a different witness audit, not a misleading equality PASS.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import itertools
import json
import math
import time
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def accumulate(out, source, coefficient=1):
    for key, value in source.items():
        updated = out.get(key, Q(0)) + coefficient * value
        if updated:
            out[key] = updated
        else:
            out.pop(key, None)
    return out


def comm(left, right):
    result = defaultdict(Q)
    for u, a in left.items():
        for v, b in right.items():
            result[u + v] += a * b
            result[v + u] -= b * a
    return {word: value for word, value in result.items() if value}


def suffix_lyndon(word):
    return bool(word) and all(word < word[k:] for k in range(1, len(word)))


@lru_cache(None)
def tensor(word):
    if len(word) == 1:
        return {word: Q(1)}
    suffix = max((word[k:] for k in range(1, len(word)) if suffix_lyndon(word[k:])), key=len)
    return comm(tensor(word[:-len(suffix)]), tensor(suffix))


class ExactSpan:
    def __init__(self, vectors=()):
        self.pivots = {}
        for vector in vectors:
            self.insert(vector)

    def remainder(self, vector):
        row = {key: Q(value) for key, value in vector.items() if value}
        for pivot, basis in sorted(self.pivots.items()):
            if row.get(pivot):
                accumulate(row, basis, -row[pivot])
        return row

    def insert(self, vector):
        row = self.remainder(vector)
        if row:
            pivot = min(row)
            leading = row[pivot]
            self.pivots[pivot] = {key: value / leading for key, value in row.items()}

    def rank(self):
        return len(self.pivots)


def decode_rows(encoded, dimension):
    result = []
    for encoded_row in encoded:
        row = {}
        for index, coefficient in encoded_row:
            require(isinstance(index, int) and 0 <= index < dimension, 'bad basis index')
            require(index not in row, 'duplicate basis coordinate')
            value = Q(coefficient)
            require(value != 0, 'explicit zero basis entry')
            row[index] = value
        result.append(row)
    return result


def word_lowering(poly, i, matrix):
    output, tail = {}, {}
    for word, coefficient in poly.items():
        suffix_weight = 0
        for position in reversed(range(len(word))):
            if word[position] == i:
                shorter = word[:position] + word[position+1:]
                accumulate(output, {shorter: coefficient}, -suffix_weight)
                accumulate(tail, {shorter: coefficient}, -1)
            suffix_weight += matrix[i][word[position]]
    require(not tail, 'nonzero Cartan tail in height>1 Lie polynomial')
    return output


def mobius(number):
    factors, divisor = 0, 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            number //= divisor
            factors += 1
            if number % divisor == 0:
                return 0
        divisor += 1
    if number > 1:
        factors += 1
    return -1 if factors % 2 else 1


def witt_dimension(alpha):
    height, divisor_gcd = sum(alpha), math.gcd(*alpha)
    total = 0
    for divisor in range(1, divisor_gcd+1):
        if divisor_gcd % divisor == 0:
            denominator = math.prod(math.factorial(a//divisor) for a in alpha)
            total += mobius(divisor) * (math.factorial(height//divisor)//denominator)
    require(total % height == 0, 'nonintegral Witt dimension')
    return total//height


class TensorCoordinates:
    """Independent monic-triangular coordinate solver, with cached generator maps."""
    def __init__(self, height):
        self.words = {}
        for degree in range(1, height+1):
            for word in itertools.product(range(3), repeat=degree):
                if suffix_lyndon(word):
                    alpha = tuple(word.count(i) for i in range(3))
                    self.words.setdefault(alpha, []).append(word)
        self.ordered = sorted(self.words, key=lambda alpha: (sum(alpha), alpha))
        self.ad_maps = {}
        for alpha, words in self.words.items():
            require(len(words) == witt_dimension(alpha), 'free-Lie dimension mismatch')
            require(all(min(tensor(word)) == word and tensor(word)[word] == 1 for word in words), 'Lyndon triangularity')

    def solve(self, polynomial, alpha):
        remaining, coordinates = dict(polynomial), {}
        for index, word in enumerate(self.words.get(alpha, ())):
            coefficient = remaining.get(word, 0)
            if coefficient:
                coordinates[index] = coefficient
                accumulate(remaining, tensor(word), -coefficient)
        require(not remaining, 'tensor polynomial outside the complete Lie basis')
        return coordinates

    def raise_row(self, i, previous, row):
        result = {}
        alpha = tuple(a+int(j == i) for j, a in enumerate(previous))
        for index, coefficient in row.items():
            word = self.words[previous][index]
            key = (i, word)
            if key not in self.ad_maps:
                self.ad_maps[key] = self.solve(comm({(i,): Q(1)}, tensor(word)), alpha)
            accumulate(result, self.ad_maps[key], coefficient)
        return result


def check_scope(data, height, expected):
    require(data.get('field') == 'Q' and data.get('prime') is None, 'Q certificate required')
    require(data.get('height') == height, 'certificate height differs from requested scope')
    require(set(data.get('matrices', {})) == set(expected), 'matrix set differs from requested scope')
    for name, matrix in expected.items():
        require(data['matrices'][name].get('matrix') == matrix, f'fixed matrix mismatch: {name}')
        require(len(matrix) == 3 and all(len(row) == 3 for row in matrix), 'rank must be three')
        require(all(matrix[i][i] == 2 for i in range(3)), 'GCM diagonal')
        require(all(isinstance(matrix[i][j], int) and matrix[i][j] <= 0 and
                    ((matrix[i][j] == 0) == (matrix[j][i] == 0))
                    for i in range(3) for j in range(3) if i != j), 'GCM off-diagonal')


def validate(data, height, expected, coordinates):
    check_scope(data, height, expected)
    counts = {'matrices': 0, 'root_degrees': 0, 'quotient_descent_columns': 0,
              'serre_generators_checked': 0, 'certificate_ideal_rows': 0}
    output = {}
    for name, matrix in expected.items():
        records = data['matrices'][name]['records']
        require([tuple(r['alpha']) for r in records] == coordinates.ordered, 'missing, duplicate, or reordered root degree')
        ideals = {}
        totals = {}
        for record in records:
            alpha = tuple(record['alpha'])
            words = coordinates.words[alpha]
            require(record['words'] == [''.join(map(str, word)) for word in words], 'incorrect Lyndon list')
            dimension = len(words)
            i_rows = decode_rows(record['ideal_basis'], dimension)
            k_rows = decode_rows(record['radical_basis'], dimension)
            i_span, k_span = ExactSpan(i_rows), ExactSpan(k_rows)
            require(i_span.rank() == len(i_rows) and k_span.rank() == len(k_rows), 'dependent certificate rows')
            require(record['extra_relations'] == 0 and i_span.rank() == k_span.rank(), 'nonzero-defect certificate requires witness audit, not equality checker')
            require(all(not i_span.remainder(row) for row in k_rows), 'radical rows do not equal Serre span')

            generated = []
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    exponent = 1-matrix[i][j]
                    source_degree = tuple(exponent if k == i else 1 if k == j else 0 for k in range(3))
                    if alpha == source_degree:
                        polynomial = {(j,): Q(1)}
                        for _ in range(exponent):
                            polynomial = comm({(i,): Q(1)}, polynomial)
                        generated.append(coordinates.solve(polynomial, alpha))
                previous = tuple(a-int(k == i) for k, a in enumerate(alpha))
                if previous in ideals:
                    generated.extend(coordinates.raise_row(i, previous, row) for row in ideals[previous].pivots.values())
            expected_ideal = ExactSpan(generated)
            require(expected_ideal.rank() == i_span.rank(), f'{name}/{alpha}: wrong Serre rank')
            require(all(not expected_ideal.remainder(row) for row in i_rows), 'extraneous ideal row')
            require(all(not i_span.remainder(row) for row in generated), 'missing ideal generator')
            quotient = [j for j in range(dimension) if j not in i_span.pivots]
            if sum(alpha) == 1:
                require(i_span.rank() == 0, 'simple-root ideal must vanish')
                quotient_rank = dimension
            else:
                images = []
                for index in quotient:
                    image = {}
                    for i in range(3):
                        if alpha[i] == 0:
                            continue
                        previous = tuple(a-int(j == i) for j, a in enumerate(alpha))
                        raw = word_lowering(tensor(words[index]), i, matrix)
                        lowered = coordinates.solve(raw, previous)
                        if previous in ideals:
                            lowered = ideals[previous].remainder(lowered)
                        else:
                            require(not lowered, 'descent into absent space')
                        image.update({(i, j): value for j, value in lowered.items()})
                    images.append(image)
                quotient_rank = ExactSpan(images).rank()
                require(quotient_rank == len(quotient), f'{name}/{alpha}: exact projected descent is not injective')
                counts['quotient_descent_columns'] += len(quotient)
            # I is lowering-stable by the proven Serre identities; lower-degree
            # equality has just been certified. Injectivity on L/I proves K=I.
            fields = {'free_dim': dimension, 'serre_ideal_rank': i_span.rank(),
                      'maximal_ideal_rank': i_span.rank(), 'serre_dim': len(quotient),
                      'contragredient_dim': len(quotient), 'descent_rank': quotient_rank,
                      'extra_relations': 0}
            require(all(record[key] == value for key, value in fields.items()), 'reported dimension mismatch')
            ideals[alpha] = i_span
            row = totals.setdefault(str(sum(alpha)), {'serre': 0, 'contragredient': 0})
            row['serre'] += len(quotient)
            row['contragredient'] += len(quotient)
            counts['root_degrees'] += 1
            counts['serre_generators_checked'] += len(generated)
            counts['certificate_ideal_rows'] += len(i_rows)
        output[name] = totals
        counts['matrices'] += 1
        print(json.dumps({'checked_matrix': name, 'height': height, 'degrees': len(records)}), flush=True)
    return {'counts': counts, 'graded_dimensions': output}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--height', type=int, required=True)
    parser.add_argument('--matrices', nargs='+', required=True)
    parser.add_argument('--spec', type=Path, default=Path('work/matrices.json'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--negative-controls', action='store_true')
    args = parser.parse_args()
    started = time.monotonic()
    compressed = args.certificate.read_bytes()
    data = json.loads(gzip.decompress(compressed))
    spec_bytes = args.spec.read_bytes()
    specification = json.loads(spec_bytes)['matrices']
    require(len(set(args.matrices)) == len(args.matrices), 'duplicate requested matrix')
    expected = {name: specification[name] for name in args.matrices}
    check_scope(data, args.height, expected)
    coordinates = TensorCoordinates(args.height)
    checked = validate(data, args.height, expected, coordinates)
    rejected = []
    if args.negative_controls:
        for mutation in ('field', 'missing_root', 'dimension', 'missing_matrix', 'changed_matrix', 'height'):
            modified = copy.deepcopy(data)
            first_name = next(iter(modified['matrices']))
            first = modified['matrices'][first_name]
            if mutation == 'field':
                modified['field'] = 'F_2'
            elif mutation == 'missing_root':
                first['records'].pop()
            elif mutation == 'dimension':
                first['records'][0]['contragredient_dim'] += 1
            elif mutation == 'missing_matrix':
                del modified['matrices'][first_name]
            elif mutation == 'changed_matrix':
                first['matrix'][0][1] -= 1
            else:
                modified['height'] -= 1
            try:
                validate(modified, args.height, expected, coordinates)
            except ValueError as error:
                rejected.append({'mutation': mutation, 'rejected': True, 'reason': str(error)})
            else:
                raise AssertionError(f'negative control accepted: {mutation}')
    result = {'status': 'PASS', 'certificate': str(args.certificate),
              'certificate_sha256': hashlib.sha256(compressed).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'spec_sha256': hashlib.sha256(spec_bytes).hexdigest(),
              'requested_height': args.height, 'requested_matrices': args.matrices,
              'field': 'Q', 'independence': 'No producer imports; exact word-deletion lowerings; independently regenerated ideal spans; quotient injectivity plus proven I-stability',
              'claim_scope': 'Only zero-extra-relation equality certificates; defect certificates are refused',
              'elapsed_seconds': round(time.monotonic()-started, 3), 'processes': 1,
              'negative_controls': rejected, **checked}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
