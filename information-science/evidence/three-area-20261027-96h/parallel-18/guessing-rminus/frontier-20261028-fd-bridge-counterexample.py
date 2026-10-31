#!/usr/bin/env python3
"""Exact fixed-support uniformization counterexample for the R-minus FD bridge.

Reads no historical mathematical outputs. All graph/word/decoder checks and
factorial comparisons use integer arithmetic; creates one exclusive JSON receipt.
"""
from collections import Counter
from itertools import combinations, product
from math import comb, factorial
import json
from pathlib import Path

NEIGHBOURS = {
    1: (2, 3, 4, 5, 6, 7),
    2: (1, 3, 7, 9, 10),
    3: (1, 2, 4, 8, 9),
    4: (1, 3, 5, 8, 10),
    5: (1, 4, 6, 9, 10),
    6: (1, 5, 7, 8, 9),
    7: (1, 2, 6, 8, 10),
    8: (3, 4, 6, 7, 9, 10),
    9: (2, 3, 5, 6, 8),
    10: (2, 4, 5, 7, 8),
}
SUPPORT_ONES = ((1, 2), (1, 3), (4,), (5,))
WEIGHTS = (2, 2, 1, 1)


def observations(word, vertex):
    return tuple(word[u - 1] for u in NEIGHBOURS[vertex])


def main():
    vertices = set(range(1, 11))
    assert set(NEIGHBOURS) == vertices
    assert all(v not in ns and len(set(ns)) == len(ns) for v, ns in NEIGHBOURS.items())
    assert all(v in NEIGHBOURS[u] for u, ns in NEIGHBOURS.items() for v in ns)
    edges = sorted((u, v) for u, ns in NEIGHBOURS.items() for v in ns if u < v)
    assert len(edges) == 26 and (3, 4) in edges and (9, 10) not in edges
    support = [tuple(int(v in s) for v in range(1, 11)) for s in SUPPORT_ONES]
    assert len(set(support)) == 4

    # Each lookup uses the FULL ordered original neighbourhood, with zero as
    # completion on observations not appearing in this support.
    tables = {v: {} for v in vertices}
    for word in support:
        for v in vertices:
            key = observations(word, v)
            value = word[v - 1]
            old = tables[v].setdefault(key, value)
            assert old == value, (v, key, old, value)
    pair_checks = 0
    for a, b in combinations(support, 2):
        for v in vertices:
            pair_checks += 1
            assert observations(a, v) != observations(b, v) or a[v - 1] == b[v - 1]
    winning = [w for w in product((0, 1), repeat=10)
               if all(tables[v].get(observations(w, v), 0) == w[v - 1]
                      for v in vertices)]
    assert set(support) <= set(winning)
    totals = [sum(weight * w[v - 1] for w, weight in zip(support, WEIGHTS))
              for v in range(1, 11)]
    uniform_ones = [sum(w[v - 1] for w in support) for v in range(1, 11)]
    assert sum(WEIGHTS) == 6
    assert totals == [4, 2, 2, 1, 1, 0, 0, 0, 0, 0]
    assert uniform_ones == [2, 1, 1, 1, 1, 0, 0, 0, 0, 0]

    # Rows of the biased-law type are (2b,2b,b,b), n=6b. Their full joint
    # type class has M points, and the largest marginal type class has Q points.
    first = None
    for b in range(1, 1001):
        n = 6 * b
        counts = (2 * b, 2 * b, b, b)
        M = factorial(n)
        for count in counts:
            M //= factorial(count)
        Q = comb(n, 2 * b)
        assert Q >= comb(n, b)
        assert M == factorial(n) // (factorial(2 * b) ** 2 * factorial(b) ** 2)
        if M > Q * Q:
            first = (b, n, counts, M, Q)
            break
    assert first is not None
    b, n, counts, M, Q = first
    result = {
        "graph": "R-minus; one-based vertices, original undirected neighbours",
        "edges": edges,
        "support_ones": SUPPORT_ONES,
        "weight_numerators_denominator": {"numerators": WEIGHTS, "denominator": 6},
        "weighted_one_counts": totals,
        "uniform_one_counts": uniform_ones,
        "fd_pair_vertex_checks": pair_checks,
        "lookup_distinct_observations": {str(v): len(tables[v]) for v in sorted(vertices)},
        "binary_full_domain_completion_default": 0,
        "binary_completion_winning_count": len(winning),
        "binary_completion_winning_ones": [tuple(v for v in range(1, 11) if w[v - 1]) for w in winning],
        "type_class": {
            "first_b_with_M_gt_Q_squared_in_1_to_1000": b,
            "n": n,
            "row_counts": counts,
            "joint_M": str(M),
            "largest_marginal_Q": str(Q),
            "Q_squared": str(Q * Q),
            "positive_gap_M_minus_Q_squared": str(M - Q * Q),
            "exact_integer_comparison": M > Q * Q,
        },
        "limits": "This tests one original-graph FD law and one explicit type. It does not improve the inherited 20/3 R-minus lower bound or establish an upper bound.",
    }
    target = Path(__file__).with_name("frontier-20261028-fd-bridge-counterexample-result.json")
    with target.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
