#!/usr/bin/env python3
"""Independent finite support/graph controls; no author input or code is read."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
import json


def columns(rows, n):
    return [sum(((row >> j) & 1) << i for i, row in enumerate(rows))
            for j in range(n)]


def no_single_overlap(masks):
    return all((a & b).bit_count() != 1 for a, b in combinations(masks, 2))


def admissible_support(rows, n, low, high):
    cols = columns(rows, n)
    return (all(low <= x.bit_count() <= high for x in rows + cols)
            and no_single_overlap(rows) and no_single_overlap(cols))


def connected(rows, n):
    cols = columns(rows, n)
    reached = {0}
    pending = [0]
    while pending:
        x = pending.pop()
        if x < n:
            neighbors = [n + j for j in range(n) if (rows[x] >> j) & 1]
        else:
            neighbors = [i for i in range(n) if (cols[x - n] >> i) & 1]
        for y in neighbors:
            if y not in reached:
                reached.add(y)
                pending.append(y)
    return len(reached) == 2 * n


# Unitary necessary conditions for two 3-ONBs with no common ray:
# no row/column has degree 1; distinct rows/columns cannot overlap in one place.
three_patterns = []
for zero_mask in range(1 << 9):
    rows = [sum(1 << j for j in range(3)
                if not ((zero_mask >> (3 * i + j)) & 1)) for i in range(3)]
    if admissible_support(rows, 3, 2, 3):
        three_patterns.append(zero_mask)
assert len(three_patterns) == 10
assert sorted(z.bit_count() for z in three_patterns) == [0] + [1] * 9
# Negative: two diagonal zeros preserve degrees >=2 but make row overlap exactly 1.
two_zero_rows = [0b110, 0b101, 0b111]
assert all(x.bit_count() >= 2 for x in two_zero_rows + columns(two_zero_rows, 3))
assert (two_zero_rows[0] & two_zero_rows[1]).bit_count() == 1
assert not admissible_support(two_zero_rows, 3, 2, 3)
# Negative to an unjustified 'zero-free is impossible from unitarity alone':
assert 0 in three_patterns

# All 5x5 row-support multisets of degree 2 or 3; these already account
# for row permutations. Impose column degrees and necessary row/column
# orthogonality, then check connectivity of the bipartite support graph.
row_types = [m for m in range(1 << 5) if m.bit_count() in (2, 3)]
five_admissible = []
five_connected = []
for rows_t in combinations_with_replacement(row_types, 5):
    rows = list(rows_t)
    if admissible_support(rows, 5, 2, 3):
        five_admissible.append(rows)
        if connected(rows, 5):
            five_connected.append(rows)
assert five_admissible and not five_connected

# Negative: an actual rational orthogonal 2+3 block has every row and column
# at most 3 nonzeros, so the connectedness hypothesis cannot be omitted.
f = Fraction
u = [[f(0) for _ in range(5)] for _ in range(5)]
u[0][0], u[0][1], u[1][0], u[1][1] = f(3, 5), f(4, 5), -f(4, 5), f(3, 5)
for i in range(2, 5):
    for j in range(2, 5):
        u[i][j] = (f(1) if i == j else f(0)) - f(2, 3)
assert all(sum(u[i][k] * u[j][k] for k in range(5)) == (i == j)
           for i in range(5) for j in range(5))
block_rows = [sum((1 << j) for j in range(5) if u[i][j]) for i in range(5)]
assert admissible_support(block_rows, 5, 2, 3) and not connected(block_rows, 5)
# Negative: a connected 3-regular support is not enough for unitarity;
# the obstruction is exactly a pair of rows with one common nonzero.
cyclic_rows = [sum(1 << ((i + j) % 5) for j in range(3)) for i in range(5)]
assert connected(cyclic_rows, 5)
assert all(x.bit_count() == 3 for x in cyclic_rows + columns(cyclic_rows, 5))
assert any((a & b).bit_count() == 1 for a, b in combinations(cyclic_rows, 2))
assert not admissible_support(cyclic_rows, 5, 2, 3)

# Seven-ray graph control. Vertex 6 is the unique degree-2 vertex; the other
# six have degree 3, so each graph has exactly ten edges. Every degree-3
# vertex must have exactly one edge among its three neighbors, as forced by
# the three-ray two-plane statement. Compare the two resulting triangles.
edges7 = list(combinations(range(7), 2))
degree_cases = 0
local_cases = 0
cross_values = {}
false_cross_unitaries = 0
negative_edges = None
for chosen in combinations(edges7, 10):
    adjacency = [0] * 7
    for a, b in chosen:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a
    if [x.bit_count() for x in adjacency] != [3] * 6 + [2]:
        continue
    degree_cases += 1
    local = True
    for v in range(6):
        neighbors = [j for j in range(7) if (adjacency[v] >> j) & 1]
        count = sum((adjacency[a] >> b) & 1 for a, b in combinations(neighbors, 2))
        if count != 1:
            local = False
            break
    if not local:
        if negative_edges is None:
            negative_edges = [list(e) for e in chosen]
        continue
    local_cases += 1
    triangles = [t for t in combinations(range(7), 3)
                 if all((adjacency[a] >> b) & 1 for a, b in combinations(t, 2))]
    assert len(triangles) == 2 and not (set(triangles[0]) & set(triangles[1]))
    assert 6 not in set(triangles[0]) | set(triangles[1])
    t, s = triangles
    cross = sum((adjacency[a] >> b) & 1 for a in t for b in s)
    assert cross >= 2
    cross_values[cross] = cross_values.get(cross, 0) + 1
    # Orthogonality edges between the triangles are zeros of a 3x3
    # transition; the triangles are disjoint, so no row/column degree 1.
    zrows = [sum(1 << j for j, b in enumerate(s) if (adjacency[a] >> b) & 1)
             for a in t]
    nzrows = [0b111 ^ z for z in zrows]
    if admissible_support(nzrows, 3, 2, 3):
        false_cross_unitaries += 1
assert degree_cases > local_cases > 0
assert negative_edges is not None and false_cross_unitaries == 0

print(json.dumps({
    "three_by_three": {"admissible_patterns": len(three_patterns),
                       "zero_counts": {"0": 1, "1": 9},
                       "negative_two_zeros": "rejected: row overlap exactly one",
                       "negative_full_support": "retained: unitarity alone does not remove it"},
    "five_by_five": {"row_multisets_considered": 42504,
                     "necessary_orthogonality_admissible": len(five_admissible),
                     "connected_admissible": len(five_connected),
                     "negative_actual_2_plus_3": "retained when connectedness is omitted",
                     "negative_connected_cyclic": "rejected: row overlap exactly one"},
    "seven_ray_graph": {"degree_sequence_graphs": degree_cases,
                        "local_triangle_graphs": local_cases,
                        "cross_edge_frequencies": cross_values,
                        "cross_supports_admissible_as_distinct_3_bases": false_cross_unitaries,
                        "negative_degree_only_edges": negative_edges,
                        "negative_reason": "degree sequence alone need not satisfy the local triangle property"}
}, sort_keys=True, indent=2))
