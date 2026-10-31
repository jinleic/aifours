#!/usr/bin/env python3
"""Independent finite checks of the reviewed incidence/count argument; not a proof."""
from itertools import combinations, product
from math import comb


def blocks_for_cells(cells, n):
    return [
        {i for i, cell in enumerate(cells) if cell[family] == value}
        for family in range(3)
        for value in range(n)
    ]


def graph_from_blocks(size, blocks):
    adj = [set() for _ in range(size)]
    for block in blocks:
        for a, b in combinations(sorted(block), 2):
            adj[a].add(b)
            adj[b].add(a)
    return adj


def c4_witness(adj):
    for a, c in combinations(range(len(adj)), 2):
        shared = sorted(adj[a] & adj[c])
        if len(shared) >= 2:
            return (a, shared[0], c, shared[1])
    return None


def wedge_count(adj):
    return sum(comb(len(neighbors), 2) for neighbors in adj)


def projective_plane_graph(q):
    def normalize(v):
        lead = next(x for x in v if x)
        inverse = pow(lead, -1, q)
        return tuple(x * inverse % q for x in v)

    projective = sorted({normalize(v) for v in product(range(q), repeat=3) if any(v)})
    m = len(projective)
    adj = [set() for _ in range(2 * m)]
    for i, point in enumerate(projective):
        for j, line in enumerate(projective):
            if sum(a * b for a, b in zip(point, line)) % q == 0:
                adj[i].add(m + j)
                adj[m + j].add(i)
    return projective, adj


# A synthetic 30-cell, 30-context incidence pattern with the claimed local
# properties. It is not asserted to extend to a Latin square or to rays.
cells = [(r, (r + t) % 10, (r + 3 * t) % 10) for r in range(10) for t in range(3)]
blocks = blocks_for_cells(cells, 10)
assert len(set(cells)) == 30
assert all(len(block) == 3 for block in blocks)
assert max(len(a & b) for a, b in combinations(blocks, 2)) == 1
adj = graph_from_blocks(len(cells), blocks)
assert all(len(neighbors) == 6 for neighbors in adj)
assert wedge_count(adj) == 450 and comb(len(adj), 2) == 435
witness = c4_witness(adj)
assert witness is not None
print('SYNTHETIC_30: vertices=30 contexts=30 context_size=3 max_context_intersection=1 degree=6')
print('SYNTHETIC_30: wedges=450 pair_capacity=435 excess=15')
print('NEG_30_C4_FREE: rejected_for_common_neighbors witness_indices=%s witness_cells=%s' %
      (witness, tuple(cells[i] for i in witness)))

# Positive C4-free graph control: incidence graph of PG(2,5), independently
# generated as normalized projective triples over F_5.
projective, plane_adj = projective_plane_graph(5)
assert len(projective) == 31 and len(plane_adj) == 62
assert all(len(neighbors) == 6 for neighbors in plane_adj)
assert c4_witness(plane_adj) is None
assert wedge_count(plane_adj) == 930 and comb(len(plane_adj), 2) == 1891
print('POS_C4_FREE: PG(2,5) incidence vertices=62 degree=6 wedges=930 pair_capacity=1891 witness=none')

# Intended-reason negative: a duplicated position makes two differently
# labeled contexts intersect in two vertices and violates cell uniqueness.
bad_cells = list(cells)
bad_cells[1] = bad_cells[0]
bad_blocks = blocks_for_cells(bad_cells, 10)
bad_max_intersection = max(len(a & b) for a, b in combinations(bad_blocks, 2))
assert len(set(bad_cells)) == 29 and bad_max_intersection == 2
print('NEG_DUPLICATED_CELL: rejected_for_duplicate_position_and_context_intersection distinct=29 max_intersection=2')

# Intended-reason negative: deleting an edge from the synthetic incidence
# graph invalidates the six-regularity check at exactly its two endpoints.
bad_adj = [set(neighbors) for neighbors in adj]
a, b = next((i, j) for i in range(len(adj)) for j in sorted(adj[i]) if i < j)
bad_adj[a].remove(b)
bad_adj[b].remove(a)
wrong_degree = [i for i, neighbors in enumerate(bad_adj) if len(neighbors) != 6]
assert wrong_degree == [a, b]
print('NEG_MISSING_EDGE: rejected_for_degree vertices=%s degrees=%s' %
      (tuple(wrong_degree), tuple(len(bad_adj[i]) for i in wrong_degree)))

# Exact illustrative real-vector instance of the three-dimensional
# common-orthogonal-complement argument, not a substitute for the proof.
def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def cross(x, y):
    return (x[1]*y[2] - x[2]*y[1], x[2]*y[0] - x[0]*y[2], x[0]*y[1] - x[1]*y[0])

v_a, v_c, v_b, v_d = (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 2)
assert [dot(v_a, v_b), dot(v_b, v_c), dot(v_c, v_d), dot(v_d, v_a)] == [0, 0, 0, 0]
assert cross(v_b, v_d) == (0, 0, 0)
v_d_bad = (0, 1, 2)
assert cross(v_b, v_d_bad) != (0, 0, 0) and dot(v_c, v_d_bad) == 1
print('GEOMETRY: all_four_C4_orthogonalities_hold_implies_sample_parallel')
print('NEG_NONPARALLEL_VECTOR: rejected_for_broken_c_d_orthogonality dot=1')
print('CONTROL_COMPLETED')
