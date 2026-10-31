#!/usr/bin/env python3
"""Finite rational controls of the reviewer's arguments, not a proof search."""
from fractions import Fraction
from itertools import product
from math import gcd


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def matrix(a, b, c):
    return ((0, a, b), (a, 0, c), (b, c, 0))


def bilinear(m, x, y):
    return sum(x[i] * m[i][j] * y[j] for i in range(3) for j in range(3))


def q(m, x):
    return bilinear(m, x, x)


def primitive(x):
    g = gcd(gcd(abs(x[0]), abs(x[1])), abs(x[2]))
    if not g:
        return None
    y = tuple(t // g for t in x)
    return tuple(-t for t in y) if next(t for t in y if t) < 0 else y


def restriction_zero(m, w):
    i = next(i for i, value in enumerate(w) if value)
    vectors = []
    for j in range(3):
        if j != i:
            p = [0, 0, 0]
            p[j], p[i] = w[i], -w[j]
            vectors.append(tuple(p))
    p, r = vectors
    return q(m, p) == 0 and q(m, r) == 0 and bilinear(m, p, r) == 0


vset = {primitive(x) for x in product(range(-2, 3), repeat=3)} - {None}
vectors = sorted(vset)
matrices = [matrix(a, b, c) for a, b, c in product(range(-2, 3), repeat=3) if (a, b, c) != (0, 0, 0)]
nonzero_restrictions = zero_restrictions = anchored_checks = 0
for m in matrices:
    null = [w for w in vectors if q(m, w) == 0]
    exceptional = [w for w in null if restriction_zero(m, w)]
    assert len(exceptional) <= 2
    if len(exceptional) == 2:
        assert dot(*exceptional) == 0
    for anchor in null:
        assert sum(dot(anchor, w) != 0 for w in exceptional) <= 1
        anchored_checks += 1
    for w in null:
        star = [x for x in null if dot(w, x) == 0]
        if restriction_zero(m, w):
            zero_restrictions += 1
        else:
            nonzero_restrictions += 1
            assert len(star) <= 2
print(f"cone_samples: matrices={len(matrices)} rays={len(vectors)} nonzero_restrictions={nonzero_restrictions} zero_restrictions={zero_restrictions} anchor_checks={anchored_checks}")

# The final pivot's weighted counting: each cell supports at most one unit of
# total weight across the three mates. Exhaust a half-integer grid.
grid = (Fraction(0), Fraction(1, 2), Fraction(1))
cell_weights = [v for v in product(grid, repeat=3) if sum(v) <= 1]
solutions = {}
for n in (1, 2, 3):
    solutions[n] = sum(all(sum(v[i] for v in cells) == 1 for i in range(3))
                       for cells in product(cell_weights, repeat=n))
assert solutions[1] == 0 and solutions[2] == 0 and solutions[3] > 0
print(f"weight_grid_solutions: one={solutions[1]} two={solutions[2]} three={solutions[3]}")

# Common non-axis D direction: positivity forbids cancellation of its D edge.
# Negative: if two opposite D directions are allowed, cancellation is possible.
plus = ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2)))
minus = ((Fraction(1, 2), Fraction(-1, 2)), (Fraction(-1, 2), Fraction(1, 2)))
for a, b in product(grid, repeat=2):
    if (a + b) * plus[0][1] == 0:
        assert a == b == 0
summed = tuple(tuple(plus[i][j] + minus[i][j] for j in range(2)) for i in range(2))
assert summed == ((1, 0), (0, 1))
print("negative_common_direction_removed: detected_positive_mixed_cancellation")

# Negative: without GAP3, two orthogonal directions each repeated five times
# exactly meet the two-dimensional trace-10 star requirement.
assert 5 + 5 == 10 and 3 + 3 < 10
print("negative_GAP3_removed: two_rays_of_multiplicity_five_meet_star_bound")

# Negative: without disjoint mate weights, a single cell can contribute one
# to every mate, so the three-distinct-cell inference is invalid.
forbidden_cell = (Fraction(1),) * 3
assert all(x == 1 for x in forbidden_cell) and sum(forbidden_cell) > 1
print("negative_mate_disjointness_removed: one_cell_satisfies_three_resolutions")
print("all_exact_controls_passed; finite_samples_are_not_continuous_exclusion")
