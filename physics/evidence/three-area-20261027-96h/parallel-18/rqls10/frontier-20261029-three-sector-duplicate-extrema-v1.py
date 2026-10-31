#!/usr/bin/env python3
"""Exact finite extremum used to strengthen the universal 3D-sector bound.

Enumerate every labeled C4-free graph on r<=7 vertices and every nondecreasing
positive integer weight tuple of sum<=8. Vertices represent repeated sector
rays, weight=multiplicity-1. Context-ray triples are graph triangles or edges
whose third ray is not repeated. Compute the exact upper cost from the written
lemma. The r=8, sum=8 case is bounded by the separate written ex(8,C4)<=11
proof; its 11-edge positive control is checked here.
"""
import hashlib
import itertools
import json
import math
import subprocess
from pathlib import Path

OUT = Path(__file__).resolve().with_suffix('.json')
if OUT.exists():
    raise FileExistsError(OUT)


def partitions(total, count, minimum=1):
    if count == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total // count + 1):
        for rest in partitions(total-first, count-1, first):
            yield (first,) + rest


def cost(adjacency, weight):
    n = len(weight)
    pairs = list(itertools.combinations(range(n), 2))
    covered = set()
    value = 0
    for a, b, c in itertools.combinations(range(n), 3):
        if adjacency[a] >> b & 1 and adjacency[a] >> c & 1 and adjacency[b] >> c & 1:
            covered.update(((a, b), (a, c), (b, c)))
            m = [weight[a]+1, weight[b]+1, weight[c]+1]
            value += min(m[0]*m[1], m[0]*m[2], m[1]*m[2], *(3*x for x in m))-1
    for a, b in pairs:
        if adjacency[a] >> b & 1 and (a, b) not in covered:
            value += min(weight[a], weight[b])
    return value


def enumerate_graphs(n):
    edges = list(itertools.combinations(range(n), 2))
    adjacency = [0]*n
    weights = [p for total in range(n, 9) for p in partitions(total, n)]
    best = {w: (-1, None) for w in weights}
    leaf_count = 0
    node_count = 0

    def visit(i):
        nonlocal leaf_count, node_count
        node_count += 1
        if i == len(edges):
            leaf_count += 1
            for weight in weights:
                value = cost(adjacency, weight)
                if value > best[weight][0]:
                    best[weight] = (value, tuple(adjacency))
            return
        u, v = edges[i]
        visit(i+1)
        # Adding u--v makes a C4 iff a length-3 u--v path already exists.
        neighbors = adjacency[u]
        closes_cycle = False
        while neighbors:
            bit = neighbors & -neighbors
            a = bit.bit_length()-1
            neighbors -= bit
            if adjacency[a] & adjacency[v]:
                closes_cycle = True
                break
        if not closes_cycle:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
            visit(i+1)
            adjacency[u] ^= 1 << v
            adjacency[v] ^= 1 << u

    visit(0)
    return best, leaf_count, node_count


best_all = {}
graph_counts = []
for n in range(1, 8):
    best, leaves, nodes = enumerate_graphs(n)
    best_all.update(best)
    graph_counts.append({'vertices': n, 'c4_free_labeled_graphs': leaves, 'search_nodes': nodes})

# The 8-vertex case has all weights 1. Written proof supplies upper bound 11;
# this explicitly checks an 11-edge C4-free witness for that extremum.
positive_edges = [(0, 3), (0, 5), (0, 6), (1, 2), (1, 4), (1, 5),
                  (1, 7), (2, 7), (3, 7), (4, 5), (5, 6)]
positive_adj = [0]*8
for u, v in positive_edges:
    positive_adj[u] |= 1 << v
    positive_adj[v] |= 1 << u
assert len(positive_edges) == 11
assert all((positive_adj[u] & positive_adj[v]).bit_count() <= 1
           for u, v in itertools.combinations(range(8), 2))
assert cost(positive_adj, (1,)*8) == 11

partitions_out = []
for weight, (best, adjacency) in sorted(best_all.items(), key=lambda p: (sum(p[0]), len(p[0]), p[0])):
    partitions_out.append({'weights': list(weight), 'maximum_cost': best,
                           'attaining_edges': [[u, v] for u, v in itertools.combinations(range(len(weight)), 2)
                                               if adjacency[u] >> v & 1]})

checks = []
for duplicate_count in range(9):
    if duplicate_count == 0:
        M = 0
    elif duplicate_count == 8:
        M = max(11, *(v[0] for w, v in best_all.items() if sum(w) == 8))
    else:
        M = max(v[0] for w, v in best_all.items() if sum(w) == duplicate_count)
    K = 30 - duplicate_count
    Fmin = 30 - M
    q, remainder = divmod(3*Fmin, K)
    minimum = ((K-remainder)*q*(2*q-1)
               + remainder*(q+1)*(2*(q+1)-1))
    upper = math.comb(K, 2)
    assert minimum > upper
    checks.append({'duplicates': duplicate_count, 'sector_rays': K,
                   'duplicate_context_cost_upper': M, 'distinct_ray_bases_lower': Fmin,
                   'common_neighbor_pair_lower': minimum,
                   'common_neighbor_pair_upper': upper})

out = {
    'status': 'EXACT_SMALL_GRAPH_EXTREMA_PASS_UNREVIEWED',
    'native_clock': subprocess.check_output(['/bin/date'], text=True).rstrip('\n'),
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'graph_counts': graph_counts,
    'weight_partition_extrema': partitions_out,
    'eight_vertex_upper_bound': '11 by the written maximum-degree proof; not enumerated in this file',
    'eight_vertex_eleven_edge_positive_control': positive_edges,
    'duplicate_cases_zero_through_eight': checks,
    'scope': 'C4-free repeated-ray graph over-approximation, D<=8; no unrestricted RQLS10 impossibility.',
}
with OUT.open('x', encoding='utf-8') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(json.dumps({k: out[k] for k in ('status', 'native_clock', 'source_sha256', 'graph_counts',
                                      'duplicate_cases_zero_through_eight')}, indent=2))
