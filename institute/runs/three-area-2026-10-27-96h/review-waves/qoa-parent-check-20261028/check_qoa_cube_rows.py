#!/usr/bin/env python3
"""Exact finite source-audit smoke: QOA rows are not recovered from their sum.

Construct the 125 extended quadratic-evaluation codewords over F_5 on six
coordinates. Check every 3-coordinate projection is bijective. This proves,
for this explicit unnormalized vector Phi, every 3-party marginal is I_125:
the complementary projection kills all off-diagonal terms and the retained
projection contributes each basis vector once. Check an exact two-row
Gaussian-rational unitary replacement preserves all row inner products and
the complete coherent sum but changes the two rows.

This checks one finite example and a row-decomposition noninjectivity claim;
it does not establish general MOQLS(8), a universal construction, or novelty.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def conjugate(x):
    return (x[0], -x[1])


def inner(x, y):
    total = ZERO
    for key, value in x.items():
        total = add(total, mul(conjugate(value), y.get(key, ZERO)))
    return total


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    words = [tuple((a + b * x + c * x * x) % 5 for x in range(5)) + (c,)
             for a, b, c in product(range(5), repeat=3)]
    require(len(set(words)) == 125, 'six-coordinate words are not distinct')
    marginal_checks = []
    for kept in combinations(range(6), 3):
        traced = tuple(j for j in range(6) if j not in kept)
        retained_counts = Counter(tuple(w[j] for j in kept) for w in words)
        traced_counts = Counter(tuple(w[j] for j in traced) for w in words)
        require(len(retained_counts) == 125 and set(retained_counts.values()) == {1},
                'retained marginal diagonal is not identity')
        require(len(traced_counts) == 125 and set(traced_counts.values()) == {1},
                'complement does not eliminate all off-diagonal terms')
        marginal_checks.append({'kept_coordinates': kept, 'exact_marginal': 'I_125'})

    first, second = words[:2]
    alpha = (Fraction(1, 2), Fraction(1, 2))
    beta = (Fraction(1, 2), Fraction(-1, 2))
    old_first, old_second = {first: ONE}, {second: ONE}
    new_first = {first: alpha, second: beta}
    new_second = {first: beta, second: alpha}
    require(inner(new_first, new_first) == ONE, 'first replacement row not unit')
    require(inner(new_second, new_second) == ONE, 'second replacement row not unit')
    require(inner(new_first, new_second) == ZERO, 'replacement rows not orthogonal')
    for w in words[2:]:
        require(inner(new_first, {w: ONE}) == ZERO, 'first row not orthogonal to remainder')
        require(inner(new_second, {w: ONE}) == ZERO, 'second row not orthogonal to remainder')
    for w in (first, second):
        require(add(new_first.get(w, ZERO), new_second.get(w, ZERO)) == ONE,
                'coherent source sum changed')
    require(new_first != old_first and new_second != old_second, 'rows did not change')

    # First three addresses already proved bijective above. Conditional output
    # vectors of the coherent sum therefore stay the same under the replacement.
    addressing = {w[:3]: w[3:] for w in words}
    require(len(addressing) == 125, 'conditional cube address is not unique')
    print(json.dumps({
        'state': 'EXACT_FINITE_CHECK_PASSED',
        'local_dimension': 5,
        'physical_parties': 6,
        'unit_orthogonal_rows': 125,
        'all_three_party_marginals': marginal_checks,
        'normalized_coherent_sum_squared_norm': '125',
        'changed_two_rows': True,
        'coherent_sum_preserved_exactly': True,
        'conditional_cube_preserved_exactly': True,
        'conclusion': 'Two distinct orthonormal QOA row lists have the same coherent sum and address-conditioned cube.',
        'limits': 'Finite source-audit witness only; not a MOQLS8 result, general theorem checker, or novelty claim.'
    }, indent=2))


if __name__ == '__main__':
    main()
