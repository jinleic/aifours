#!/usr/bin/env python3
"""Independent exact incidence model for GL(3,2) index-seven cosets.

This uses F2 point/covector labels and intersection equations, not the matrix
or subgroup enumerator. The written proof must establish that model's scope.
"""
from collections import Counter

pts = range(1, 8)
vertices = [(0, p, a) for p in pts for a in pts] + [
    (1, alpha, beta) for alpha in pts for beta in pts
]


def dot(x, y):
    return (x & y).bit_count() % 2


def disjoint(x, y):
    typ, first, second = x
    t2, third, fourth = y
    if typ == t2:
        return (first == third) != (second == fourth)
    if typ == 1:
        return disjoint(y, x)
    # point label p->a; covector label alpha after T equals beta
    return dot(fourth, first) != dot(third, second)


adj = [0] * len(vertices)
for i, v in enumerate(vertices):
    for j in range(i):
        if disjoint(v, vertices[j]):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
counts = Counter()


def visit(chosen, available, common):
    if len(chosen) == 6:
        counts[common.bit_count()] += 1
        return
    while available:
        bit = available & -available
        available ^= bit
        j = bit.bit_length() - 1
        visit(chosen + [j], available & adj[j], common & adj[j])


visit([], (1 << len(vertices)) - 1, (1 << len(vertices)) - 1)
print("point_and_covector_labels:", len(vertices))
print("six_set_completion_counts:", dict(sorted(counts.items())))
if sum(counts.values()) != 1568 or counts != {1: 1568}:
    raise SystemExit("FAIL: six-coset completion counts")
print("PASS: every six-clique has exactly one seventh label")
