#!/usr/bin/env python3
"""Independent integer replay of the small repeated-ray graph extrema.

No author checker is imported. Every graph on at most seven vertices is
enumerated directly by adjacency-bit masks and C4 tested using common
neighbors. Triangle costs are counted by edge-common-neighbor intersections.
"""
import hashlib
import itertools
import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / 'frontier-20261029-three-sector-duplicate-extrema-v1.json'
OUT = ROOT / 'frontier-20261029-three-sector-duplicate-extrema-replay-v1.json'
EXPECTED = 'c7c2b0e8bd236928e82b0ec978368629486af6a16502ad8e49989b4af750a0bc'
if OUT.exists():
    raise FileExistsError(OUT)
raw = CERT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED
cert = json.loads(raw)


def four_cycle_free(adjacency):
    return all((adjacency[a] & adjacency[b]).bit_count() < 2
               for a, b in itertools.combinations(range(len(adjacency)), 2))


def independent_cost(adjacency, weight):
    edges = [(a,b) for a,b in itertools.combinations(range(len(weight)), 2)
             if adjacency[a] >> b & 1]
    triangles = set()
    singles = []
    for a,b in edges:
        common = adjacency[a] & adjacency[b]
        assert common.bit_count() <= 1
        if common:
            c = common.bit_length()-1
            triangles.add(tuple(sorted((a,b,c))))
        else:
            singles.append((a,b))
    total = sum(min(weight[a], weight[b]) for a,b in singles)
    for tri in triangles:
        mult = [weight[i]+1 for i in tri]
        pair_cap = min(mult[i]*mult[j] for i,j in itertools.combinations(range(3),2))
        context_cap = min(3*m for m in mult)
        total += min(pair_cap, context_cap)-1
    return total


def weight_tuples(n):
    out = set()
    for total in range(n, 9):
        for separators in itertools.combinations(range(1, total), n-1):
            pts = (0,) + separators + (total,)
            weight = tuple(sorted(pts[i+1]-pts[i] for i in range(n)))
            out.add(weight)
    return sorted(out)

reported = {tuple(x['weights']): x['maximum_cost'] for x in cert['weight_partition_extrema']}
observed = {}
counts = []
for n in range(1, 8):
    edges = list(itertools.combinations(range(n), 2))
    best = {w: -1 for w in weight_tuples(n)}
    accepted = 0
    for mask in range(1 << len(edges)):
        adjacency = [0]*n
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            a,b = edges[bit.bit_length()-1]
            remaining -= bit
            adjacency[a] |= 1 << b
            adjacency[b] |= 1 << a
        if not four_cycle_free(adjacency):
            continue
        accepted += 1
        for w in best:
            value = independent_cost(adjacency, w)
            if value > best[w]:
                best[w] = value
    observed.update(best)
    counts.append({'vertices': n, 'c4_free_labeled_graphs': accepted})
    assert accepted == cert['graph_counts'][n-1]['c4_free_labeled_graphs']
assert observed == reported

# Intended graph controls: reject a 4-cycle, accept a triangle and an
# 8-vertex 11-edge C4-free graph, and verify a nontrivial weighted triangle.
cycle = [0]*4
for a,b in ((0,1),(1,2),(2,3),(3,0)):
    cycle[a] |= 1 << b
    cycle[b] |= 1 << a
assert not four_cycle_free(cycle)
triangle = [0b110, 0b101, 0b011]
assert four_cycle_free(triangle)
assert independent_cost(triangle, (2,2,1)) == 5
positive = [0]*8
for a,b in cert['eight_vertex_eleven_edge_positive_control']:
    positive[a] |= 1 << b
    positive[b] |= 1 << a
assert sum(x.bit_count() for x in positive) == 22 and four_cycle_free(positive)
assert independent_cost(positive, (1,)*8) == 11

for row in cert['duplicate_cases_zero_through_eight']:
    D = row['duplicates']
    candidate = [v for w,v in observed.items() if sum(w) == D]
    M = 0 if D == 0 else max(candidate + ([11] if D == 8 else []))
    assert M == row['duplicate_context_cost_upper']
    K = 30-D
    F = 30-M
    q,r = divmod(3*F,K)
    lower = (K-r)*q*(2*q-1)+r*(q+1)*(2*q+1)
    assert lower == row['common_neighbor_pair_lower'] > math.comb(K,2)

result = {
    'status': 'INDEPENDENT_DIRECT_GRAPH_ENUMERATION_PASS_UNREVIEWED',
    'native_clock': subprocess.check_output(['/bin/date'], text=True).rstrip('\n'),
    'certificate_sha256': EXPECTED,
    'replay_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'c4_free_graph_counts': counts,
    'weight_partitions_checked': len(observed),
    'duplicate_cases_checked': 9,
    'controls': ['4-cycle rejected', 'weighted triangle cost five', '8-vertex 11-edge positive graph'],
    'limitation': 'The ex(8,C4)<=11 upper bound is written mathematics, not enumerated in this replay; same-harness review only.',
}
with OUT.open('x', encoding='utf-8') as f:
    json.dump(result, f, indent=2)
    f.write('\n')
print(json.dumps(result, indent=2))
