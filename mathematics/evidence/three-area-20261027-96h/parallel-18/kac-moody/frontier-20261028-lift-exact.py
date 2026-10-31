#!/usr/bin/env python3
"""Exact bounded original level-four reached-target experiment.

Free positive Lie algebra in the tensor algebra; lexicographic Lyndon
brackets.  ALL six actual positive Serre seeds and their iterated adjoint
closure by the three simple positive generators are retained.  All ranks
are over Q using fractions.Fraction, and target relations are kept in the
same direct sum as the three actual lowerings.  See the companion report for
scope and for the proof of the tensor-word lowering formula.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path

Q = Fraction


def clean(v):
    return {k: Q(c) for k, c in v.items() if c}


def minus_scaled(v, w, factor):
    for k, c in w.items():
        x = v.get(k, Q(0)) - factor * c
        if x:
            v[k] = x
        else:
            v.pop(k, None)


class Span:
    """Exact echelon span with deterministic, least-word pivots."""
    def __init__(self):
        self.rows = {}

    def reduce(self, vector):
        v = clean(vector)
        for pivot in sorted(self.rows):
            if pivot in v:
                minus_scaled(v, self.rows[pivot], v[pivot])
        return v

    def add(self, vector):
        v = self.reduce(vector)
        if not v:
            return None
        pivot = min(v)
        d = v[pivot]
        row = {k: c / d for k, c in v.items()}
        self.rows[pivot] = row
        return row

    def __len__(self):
        return len(self.rows)


def multiply(a, b):
    out = {}
    for w, c in a.items():
        for z, d in b.items():
            key = w + z
            out[key] = out.get(key, 0) + c * d
    return {w: c for w, c in out.items() if c}


def bracket(a, b):
    out = multiply(a, b)
    for w, c in multiply(b, a).items():
        out[w] = out.get(w, 0) - c
    return {w: c for w, c in out.items() if c}


def letter(i):
    return {(i,): 1}


def weight(word):
    return tuple(word.count(i) for i in (1, 2, 3))


def fits(a, b):
    return all(x <= y for x, y in zip(a, b))


def words_with_weight(counts):
    counts = list(counts)
    word = []

    def walk():
        if sum(counts) == 0:
            yield tuple(word)
            return
        for i in range(3):
            if counts[i]:
                counts[i] -= 1
                word.append(i + 1)
                yield from walk()
                word.pop()
                counts[i] += 1

    yield from walk()


def is_lyndon(word):
    return all(word < word[k:] for k in range(1, len(word)))


@lru_cache(maxsize=None)
def lyndon_bracket(word):
    if len(word) == 1:
        return letter(word[0])
    # Standard factorization: longest proper Lyndon suffix.
    for i in range(1, len(word)):
        if is_lyndon(word[i:]):
            result = bracket(lyndon_bracket(word[:i]), lyndon_bracket(word[i:]))
            assert result.get(word) == 1 and min(result) == word
            return result
    raise AssertionError(f"No Lyndon suffix for {word}")


def lie_basis(counts):
    return [(w, lyndon_bracket(w)) for w in words_with_weight(counts) if is_lyndon(w)]


def seed(i, j, exponent):
    v = letter(j)
    for _ in range(exponent):
        v = bracket(letter(i), v)
    return v


def ideal_bases(bound, matrix):
    """Exact graded span of the full positive Serre ideal inside bound.

    Jacobi implies that iterated adjoints of simple generators on the six
    seeds span the generated Lie ideal.  Incremental elimination before
    further adjoints is exact because the bracket is linear.
    """
    spaces = {}
    queue = deque()

    def insert(degree, vector):
        if not vector or not fits(degree, bound):
            return
        space = spaces.setdefault(degree, Span())
        row = space.add(vector)
        if row is not None:
            queue.append((degree, row))

    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            exponent = 1 - matrix[i][j]
            degree = tuple(exponent * (k == i) + (k == j) for k in range(3))
            if fits(degree, bound):
                insert(degree, seed(i + 1, j + 1, exponent))

    while queue:
        degree, vector = queue.popleft()
        for i in range(3):
            if degree[i] < bound[i]:
                nxt = list(degree)
                nxt[i] += 1
                insert(tuple(nxt), bracket(letter(i + 1), vector))
    return spaces


def lowering(vector, i, matrix):
    """Compute [f_i,x] for positive Lie x of word length at least two.

    In the enveloping algebra [f_i,e_j]=-delta_ij h_i.  Move each h_i
    to the right.  The remaining right-h coefficient is explicitly checked
    to vanish on each input Lie polynomial, rather than assumed.
    """
    assert all(len(w) >= 2 for w in vector)
    out = {}
    htail = {}
    for word, c in vector.items():
        for k, letter_id in enumerate(word):
            if letter_id == i + 1:
                shorter = word[:k] + word[k + 1:]
                htail[shorter] = htail.get(shorter, 0) - c
                suffix_weight = sum(matrix[i][j - 1] for j in word[k + 1:])
                out[shorter] = out.get(shorter, 0) - c * suffix_weight
    assert not any(htail.values()), "right-Cartan coefficient did not cancel"
    return {w: Q(c) for w, c in out.items() if c}


def delta(vector, matrix):
    result = {}
    for i in range(3):
        for word, c in lowering(vector, i, matrix).items():
            result[(i, word)] = c
    return result


def direct_sum_ideal(spaces, degree):
    result = Span()
    for i in range(3):
        if degree[i] == 0:
            continue
        target = list(degree)
        target[i] -= 1
        source = spaces.get(tuple(target), Span())
        for row in source.rows.values():
            result.add({(i, word): c for word, c in row.items()})
    return result


def rank(vectors):
    span = Span()
    for v in vectors:
        span.add(v)
    return len(span)


def rational_text(q):
    q = Q(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def kernel_with_coefficients(vectors):
    """Basis of coefficient-space null relations, with exact certificates."""
    rows = {}
    null = []
    for column, vector in enumerate(vectors):
        v = clean(vector)
        coeff = {column: Q(1)}
        for pivot in sorted(rows):
            if pivot in v:
                q = v[pivot]
                row, relation = rows[pivot]
                minus_scaled(v, row, q)
                minus_scaled(coeff, relation, q)
        if not v:
            null.append(coeff)
        else:
            p = min(v)
            q = v[p]
            rows[p] = ({k: x / q for k, x in v.items()},
                       {k: x / q for k, x in coeff.items()})
    return null


def combine(vectors, coeff):
    result = {}
    for j, c in coeff.items():
        for key, value in vectors[j].items():
            result[key] = result.get(key, Q(0)) + c * value
    return {k: Q(v) for k, v in result.items() if v}


def run_case(degree, r, s):
    matrix = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    source = lie_basis(degree)
    if not source:
        return {"degree": degree, "r": r, "s": s, "source_dim": 0}
    ideals = ideal_bases(degree, matrix)
    ialpha = ideals.get(degree, Span())
    target = direct_sum_ideal(ideals, degree)
    derivatives = [delta(v, matrix) for _, v in source]
    ideal_derivatives = [delta(v, matrix) for v in ialpha.rows.values()]
    for v in ideal_derivatives:
        assert not target.reduce(v), "Serre ideal was not stable under lowering"
    d_rank = rank(derivatives)
    di_rank = rank(ideal_derivatives)
    mod_t = [target.reduce(v) for v in derivatives]
    quotient_rank = rank(mod_t)
    reached_dim = d_rank - quotient_rank
    lift_obstruction_dim = reached_dim - di_rank
    free_kernel_dim = len(source) - d_rank
    ideal_kernel_dim = len(ialpha) - di_rank
    quotient_kernel_dim = len(source) - quotient_rank - len(ialpha)
    assert min(lift_obstruction_dim, free_kernel_dim, ideal_kernel_dim,
               quotient_kernel_dim) >= 0
    assert quotient_kernel_dim == (free_kernel_dim - ideal_kernel_dim
                                   + lift_obstruction_dim)
    src_span = Span()
    for _, v in source:
        assert src_span.add(v) is not None
    for v in ialpha.rows.values():
        assert not src_span.reduce(v), "ideal vector not in Lyndon free source"
    witnesses = []
    if quotient_kernel_dim:
        derivative_ideal_span = Span()
        for v in ideal_derivatives:
            derivative_ideal_span.add(v)
        for coeff in kernel_with_coefficients(mod_t):
            src = combine([v for _, v in source], coeff)
            if ialpha.reduce(src):
                deriv = combine(derivatives, coeff)
                witnesses.append({
                    "lyndon_source_coefficients": {
                        ''.join(map(str, source[j][0])): rational_text(c)
                        for j, c in sorted(coeff.items())
                    },
                    "nonzero_lift_obstruction": bool(derivative_ideal_span.reduce(deriv)),
                })
                if len(witnesses) == 4:
                    break
    return {
        "degree": degree, "r": r, "s": s,
        "source_dim": len(source), "ideal_dim": len(ialpha),
        "target_ideal_dim": len(target), "delta_rank": d_rank,
        "delta_ideal_rank": di_rank, "delta_mod_target_rank": quotient_rank,
        "reached_target_dim": reached_dim,
        "lift_obstruction_dim": lift_obstruction_dim,
        "free_kernel_dim": free_kernel_dim, "ideal_kernel_dim": ideal_kernel_dim,
        "quotient_kernel_dim": quotient_kernel_dim,
        "quotient_kernel_examples_lyndon_basis": witnesses,
        "source_lyndon_words": [''.join(map(str, w)) for w, _ in source],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a', type=int, default=1)
    parser.add_argument('--b', type=int, default=1)
    parser.add_argument('--max-r', type=int, default=4)
    parser.add_argument('--max-s', type=int, default=4)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    degree = (args.a, args.b, 4)
    if min(args.a, args.b, args.max_r, args.max_s) < 1:
        parser.error('a, b and parameter caps must be positive')
    if sum(degree) > 9 or args.max_r > 6 or args.max_s > 6:
        parser.error('bounded run only: total degree <= 9; parameter caps <= 6')
    results = [run_case(degree, r, s)
               for r, s in product(range(1, args.max_r + 1), range(1, args.max_s + 1))]
    report = {
        'method': 'exact rational sparse echelon; Lyndon basis in tensor algebra; all Serre-ideal descendants; coherent full three-target quotient',
        'parameters_are_tested_not_a_universal_proof': True,
        'basis_and_ideal_scope': 'positive root degrees only; ALL targets in these cases are positive',
        'selected_degree': degree, 'cases': results,
    }
    text = json.dumps(report, indent=2) + '\n'
    if args.output:
        root = Path(__file__).resolve().parent
        dest = args.output.resolve()
        if dest.parent != root or not dest.name.startswith('frontier-20261028-'):
            parser.error('output must be frontier-20261028-* in the owner root')
        if dest.exists():
            parser.error('refusing to overwrite an existing artifact')
        dest.write_text(text, encoding='utf-8')
        print(f'WROTE {dest} cases={len(results)}')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
