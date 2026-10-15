#!/usr/bin/env python3
"""Independent Q checker: no imports from graded_lie or compute.

Checks Serre ideal generation and full descent-kernel equality in associative
word coordinates. Lowering uses commuting h_i to the right in tensor words,
NOT the producer's recursive Lie-bracket derivation. Certificate dimensions
are accepted only after exact Fraction row-rank and inclusion checks.
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


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def accumulate(target, source, multiplier=1):
    for word, value in source.items():
        target[word] = target.get(word, Q(0)) + multiplier * value
        if not target[word]:
            del target[word]
    return target


def comm(left, right):
    result = defaultdict(Q)
    for u, a in left.items():
        for v, b in right.items():
            result[u + v] += a * b
            result[v + u] -= b * a
    return {w: a for w, a in result.items() if a}


def suffix_lyndon(word):
    return len(word) > 0 and all(word < word[k:] for k in range(1, len(word)))


@lru_cache(None)
def tensor(word):
    if len(word) == 1:
        return {word: Q(1)}
    candidates = [word[k:] for k in range(1, len(word)) if suffix_lyndon(word[k:])]
    suffix = max(candidates, key=len)
    prefix = word[:-len(suffix)]
    return comm(tensor(prefix), tensor(suffix))


class ExactSpan:
    def __init__(self, vectors=()):
        self.pivots = {}
        for vector in vectors:
            row = self.remainder(vector)
            if row:
                pivot = min(row)
                lead = row[pivot]
                self.pivots[pivot] = {key: Q(value) / lead for key, value in row.items()}

    def remainder(self, vector):
        row = {k: Q(v) for k, v in vector.items() if v}
        for pivot, basis in sorted(self.pivots.items()):
            if row.get(pivot):
                factor = row[pivot]
                accumulate(row, basis, -factor)
        return row

    def rank(self):
        return len(self.pivots)


def decode_basis(encoded, words):
    rows = []
    for row in encoded:
        polynomial = {}
        seen = set()
        for index, coefficient in row:
            require(isinstance(index, int) and 0 <= index < len(words), 'bad basis index')
            require(index not in seen, 'duplicate basis coordinate')
            seen.add(index)
            accumulate(polynomial, tensor(words[index]), Q(coefficient))
        rows.append(polynomial)
    return rows


def lower_tensor(poly, i, matrix):
    """[f_i,word] after moving h_i factors to the right.

    Its rightmost-h_i coefficient is zero for every Lie element of height>1.
    The remaining coefficient is minus the suffix Cartan weight at each
    occurrence of generator i. This checks signs independently of the producer.
    """
    output, cartan_tail = {}, {}
    for word, coefficient in poly.items():
        suffix_weight = 0
        for position in reversed(range(len(word))):
            if word[position] == i:
                shorter = word[:position] + word[position + 1:]
                accumulate(output, {shorter: coefficient}, -suffix_weight)
                accumulate(cartan_tail, {shorter: coefficient}, -1)
            suffix_weight += matrix[i][word[position]]
    require(not cartan_tail, 'nonzero Cartan tail: polynomial is not a positive Lie element of height>1')
    return output


def mobius(n):
    factors = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            factors += 1
            if n % divisor == 0:
                return 0
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        factors += 1
    return -1 if factors % 2 else 1


def witt_dimension(alpha):
    height = sum(alpha)
    divisor_gcd = math.gcd(*alpha)
    total = 0
    for d in range(1, divisor_gcd + 1):
        if divisor_gcd % d == 0:
            number = math.factorial(height // d)
            for a in alpha:
                number //= math.factorial(a // d)
            total += mobius(d) * number
    require(total % height == 0, 'nonintegral Witt formula')
    return total // height


def validate(data):
    require(data.get('field') == 'Q' and data.get('prime') is None, 'characteristic-zero checker requires Q certificate')
    height = data['height']
    require(isinstance(height, int) and height >= 1, 'invalid height')
    groups = {}
    for degree in range(1, height + 1):
        for word in itertools.product(range(3), repeat=degree):
            if suffix_lyndon(word):
                alpha = tuple(word.count(i) for i in range(3))
                groups.setdefault(alpha, []).append(word)
    ordered = sorted(groups, key=lambda alpha: (sum(alpha), alpha))
    counts = {'matrices': 0, 'root_degrees': 0, 'descent_columns': 0, 'serre_generators_checked': 0,
              'kernel_vectors_checked': 0}
    outputs = {}
    for name, instance in data['matrices'].items():
        matrix = instance['matrix']
        require(len(matrix) == 3 and all(len(row) == 3 for row in matrix), 'rank must be three')
        require(all(matrix[i][i] == 2 for i in range(3)), 'GCM diagonal')
        require(all(isinstance(matrix[i][j], int) and matrix[i][j] <= 0 and
                    ((matrix[i][j] == 0) == (matrix[j][i] == 0))
                    for i in range(3) for j in range(3) if i != j), 'GCM off-diagonal')
        records = instance['records']
        require([tuple(r['alpha']) for r in records] == ordered, 'missing, duplicated, or reordered root degree')
        ideal_rows, radical_rows, radical_spaces = {}, {}, {}
        totals = {}
        for record in records:
            alpha = tuple(record['alpha'])
            words = [tuple(map(int, word)) for word in record['words']]
            require(words == groups[alpha], 'incorrect Lyndon basis list')
            require(len(words) == witt_dimension(alpha), 'free-Lie dimension mismatch')
            require(all(min(tensor(w)) == w and tensor(w)[w] == 1 for w in words), 'Lyndon triangularity')
            m = len(words)
            producer_ideal = decode_basis(record['ideal_basis'], words)
            producer_radical = decode_basis(record['radical_basis'], words)
            i_span, k_span = ExactSpan(producer_ideal), ExactSpan(producer_radical)
            require(i_span.rank() == len(producer_ideal), 'dependent ideal certificate rows')
            require(k_span.rank() == len(producer_radical), 'dependent radical certificate rows')

            generated = []
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    exponent = 1 - matrix[i][j]
                    expected = tuple(exponent if k == i else 1 if k == j else 0 for k in range(3))
                    if alpha == expected:
                        polynomial = {(j,): Q(1)}
                        for _ in range(exponent):
                            polynomial = comm({(i,): Q(1)}, polynomial)
                        generated.append(polynomial)
                previous = tuple(a - int(k == i) for k, a in enumerate(alpha))
                for row in ideal_rows.get(previous, ()):
                    generated.append(comm({(i,): Q(1)}, row))
            expected_ideal = ExactSpan(generated)
            require(expected_ideal.rank() == i_span.rank(), f'{name}/{alpha}: Serre ideal rank')
            require(all(not expected_ideal.remainder(row) for row in producer_ideal), 'extraneous ideal row')
            require(all(not i_span.remainder(row) for row in generated), 'missing Serre ideal generator')
            counts['serre_generators_checked'] += len(generated)

            if sum(alpha) == 1:
                require(k_span.rank() == 0, 'simple-root radical must be zero')
                descent_rank = m
            else:
                def projected_descent(poly):
                    image = {}
                    for i in range(3):
                        if alpha[i] == 0:
                            continue
                        previous = tuple(a - int(k == i) for k, a in enumerate(alpha))
                        lowered = lower_tensor(poly, i, matrix)
                        if previous in radical_spaces:
                            lowered = radical_spaces[previous].remainder(lowered)
                        else:
                            require(not lowered, 'descent into absent homogeneous space')
                        image.update({(i, word): coefficient for word, coefficient in lowered.items()})
                    return image

                images = [projected_descent(tensor(word)) for word in words]
                descent_rank = ExactSpan(images).rank()
                require(k_span.rank() == m - descent_rank, f'{name}/{alpha}: radical nullity')
                require(all(not projected_descent(row) for row in producer_radical), 'non-kernel radical row')
                counts['descent_columns'] += m
                counts['kernel_vectors_checked'] += len(producer_radical)
            require(all(not k_span.remainder(row) for row in producer_ideal), 'Serre ideal not contained in radical')
            expected_fields = {'free_dim': m, 'serre_ideal_rank': i_span.rank(),
                               'maximal_ideal_rank': k_span.rank(), 'serre_dim': m - i_span.rank(),
                               'contragredient_dim': m - k_span.rank(), 'descent_rank': descent_rank,
                               'extra_relations': k_span.rank() - i_span.rank()}
            require(all(record[key] == value for key, value in expected_fields.items()), 'reported dimension mismatch')
            ideal_rows[alpha], radical_rows[alpha], radical_spaces[alpha] = producer_ideal, producer_radical, k_span
            degree = str(sum(alpha))
            row = totals.setdefault(degree, {'serre': 0, 'contragredient': 0})
            row['serre'] += m - i_span.rank()
            row['contragredient'] += m - k_span.rank()
            counts['root_degrees'] += 1
        outputs[name] = totals
        counts['matrices'] += 1
    return {'counts': counts, 'graded_dimensions': outputs}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--negative-controls', action='store_true')
    args = parser.parse_args()
    started = time.monotonic()
    compressed = args.certificate.read_bytes()
    data = json.loads(gzip.decompress(compressed))
    checked = validate(data)
    rejected = []
    if args.negative_controls:
        for mutation in ('field', 'missing_root', 'dimension'):
            modified = copy.deepcopy(data)
            first = next(iter(modified['matrices'].values()))
            if mutation == 'field':
                modified['field'] = 'F_2'
            elif mutation == 'missing_root':
                first['records'].pop()
            else:
                first['records'][0]['contragredient_dim'] += 1
            try:
                validate(modified)
            except ValueError as error:
                rejected.append({'mutation': mutation, 'rejected': True, 'reason': str(error)})
            else:
                raise AssertionError(f'negative control accepted: {mutation}')
    result = {'status': 'PASS', 'certificate': str(args.certificate),
              'certificate_sha256': hashlib.sha256(compressed).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'height': data['height'], 'field': 'Q', 'independence': 'No producer imports; associative-word lowering rather than recursive bracket lowering',
              'elapsed_seconds': round(time.monotonic() - started, 3), 'processes': 1,
              'negative_controls': rejected, **checked}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
