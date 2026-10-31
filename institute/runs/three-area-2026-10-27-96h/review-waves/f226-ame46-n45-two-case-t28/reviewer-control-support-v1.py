#!/usr/bin/env python3
"""Reviewer-owned exact necessary-support checks, not author code."""
from itertools import combinations, product
import json


def reason(n, rows):
    if any(sum((row >> c) & 1 for row in rows) < 2 for c in range(n)):
        return "column-degree-below-two"
    if any((a & b).bit_count() == 1 for a, b in combinations(rows, 2)):
        return "single-row-overlap"
    return "necessary-conditions-hold"


def mask(indices):
    return sum(1 << c for c in indices)


def count_supports(n):
    pairs = [mask(s) for s in combinations(range(n), 2)]
    triples = [mask(s) for s in combinations(range(n), 3)]
    zero = sum(reason(n, rows) == "necessary-conditions-hold"
               for rows in product(pairs, repeat=n))
    # A single degree-three row can be relabeled as row 0.
    one = (sum(reason(n, (triple,) + rest) == "necessary-conditions-hold"
               for triple in triples for rest in product(pairs, repeat=n-1))
           if n else 0)
    return {"dimension": n, "zero_excess": zero, "one_excess": one}


counts = [count_supports(n) for n in range(6)]
expected_zero = [1, 0, 1, 0, 18, 0]
assert [r["zero_excess"] for r in counts] == expected_zero
assert all(r["one_excess"] == 0 for r in counts)

checks = {}
checks["positive_2x2_support"] = reason(2, (mask((0, 1)), mask((0, 1))))
checks["positive_4x4_support"] = reason(4, (mask((0, 1)), mask((0, 1)),
                                                  mask((2, 3)), mask((2, 3))))
checks["negative_degree_two_triangle"] = reason(3, (mask((0, 1)), mask((1, 2)),
                                                         mask((0, 2))))
checks["negative_one_excess_overlap"] = reason(3, (mask((0, 1, 2)), mask((0, 1)),
                                                         mask((1, 2))))
checks["negative_missing_column"] = reason(4, (mask((0, 1)), mask((0, 1)),
                                                      mask((2, 3)), mask((0, 1))))
assert checks["positive_2x2_support"] == "necessary-conditions-hold"
assert checks["positive_4x4_support"] == "necessary-conditions-hold"
assert checks["negative_degree_two_triangle"] == "single-row-overlap"
assert checks["negative_one_excess_overlap"] == "single-row-overlap"
assert checks["negative_missing_column"] == "column-degree-below-two"

# H/sqrt(2) is an exact 2x2 unitary; the integer numerator check avoids floats.
h = ((1, 1), (1, -1))
assert [[sum(h[i][k] * h[j][k] for k in range(2)) for j in range(2)]
        for i in range(2)] == [[2, 0], [0, 2]]
print(json.dumps({"scope": "labeled necessary-support patterns, n=0..5; one-excess row 0 fixed",
                  "counts": counts, "intended_reason_checks": checks,
                  "hadamard_numerator_gram": [[2, 0], [0, 2]],
                  "status": "completed"}, sort_keys=True))
