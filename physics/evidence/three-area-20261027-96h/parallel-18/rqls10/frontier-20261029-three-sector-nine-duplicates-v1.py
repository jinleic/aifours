#!/usr/bin/env python3
"""D=9 extension of the 3D-sector repeated-ray graph bound.

All weighted C4-free graphs with at most seven vertices and total weight nine
are enumerated. Eight and nine vertices are bounded by separate written
C4-extremal lemmas. This is a necessary-condition filter, not an array witness.
"""
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

OUT = Path(__file__).resolve().with_suffix('.json')
if OUT.exists():
    raise FileExistsError(OUT)


def partitions(total, count, first=1):
    if count == 0:
        if total == 0:
            yield ()
        return
    for x in range(first, total//count + 1):
        for tail in partitions(total-x, count-1, x):
            yield (x,) + tail


def objective(adj, weights):
    n = len(weights)
    covered = set()
    value = 0
    for i,j,k in itertools.combinations(range(n),3):
        if (adj[i] >> j & 1) and (adj[i] >> k & 1) and (adj[j] >> k & 1):
            covered.update(((i,j),(i,k),(j,k)))
            a,b,c = (weights[q]+1 for q in (i,j,k))
            value += min(a*b,a*c,b*c,3*a,3*b,3*c)-1
    for i,j in itertools.combinations(range(n),2):
        if (adj[i] >> j & 1) and (i,j) not in covered:
            value += min(weights[i],weights[j])
    return value


def solve(n):
    pairs = list(itertools.combinations(range(n),2))
    weights = list(partitions(9,n))
    best = {w:(-1,None) for w in weights}
    adj = [0]*n
    leaves = 0
    def visit(k):
        nonlocal leaves
        if k == len(pairs):
            leaves += 1
            for w in weights:
                value = objective(adj,w)
                if value > best[w][0]:
                    best[w] = (value,tuple(adj))
            return
        u,v = pairs[k]
        visit(k+1)
        # C4 appears after adding uv iff there is already a three-edge u-v path.
        neighbors = adj[u]
        bad = False
        while neighbors:
            bit = neighbors & -neighbors
            a = bit.bit_length()-1
            neighbors -= bit
            if adj[a] & adj[v]:
                bad = True
                break
        if not bad:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
            visit(k+1)
            adj[u] ^= 1 << v
            adj[v] ^= 1 << u
    visit(0)
    return best,leaves

records = []
per_r = []
for n in range(1,8):
    values,leaves = solve(n)
    maximum = max(v[0] for v in values.values())
    per_r.append({'repeat_ray_types':n,'graphs':leaves,'max_cost':maximum})
    for w,(value,adj) in sorted(values.items()):
        records.append({'weights':list(w),'maximum_cost':value,
                        'attaining_edges':[[i,j] for i,j in itertools.combinations(range(n),2)
                                           if adj[i] >> j & 1]})
assert [r['max_cost'] for r in per_r] == [0,4,11,10,13,12,11]

# Explicit nine-vertex 13-edge C4-free graph checks the sharpness of the
# separate written bound ex(9,C4)<=13.
control = [(0,3),(0,4),(0,5),(0,7),(1,6),(1,8),(2,7),
           (2,8),(3,5),(3,6),(4,7),(6,8),(7,8)]
adj = [0]*9
for a,b in control:
    adj[a] |= 1 << b
    adj[b] |= 1 << a
assert len(control)==13 and all((adj[a]&adj[b]).bit_count() <= 1
                                for a,b in itertools.combinations(range(9),2))
assert objective(adj,(1,)*9)==13

# At r=8 the sole weight partition is (1,1,1,1,1,1,1,2); its cost
# is exactly the edge count. Written ex(8,C4)<=11. At r=9 all weights
# are 1 and the written ex(9,C4)<=13 gives cost<=13.
M9 = max(13,11,*(x['max_cost'] for x in per_r))
assert M9 == 13
out = {
    'status':'EXACT_D9_SMALL_GRAPHS_PASS_UNREVIEWED',
    'native_clock':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'weighted_partition_extrema':records,
    'per_repeat_vertex_count':per_r,
    'eight_vertex_cost_upper':11,
    'nine_vertex_cost_upper':13,
    'nine_vertex_13_edge_positive_control':control,
    'M9_upper':M9,
    'scope':'D=9 repeated-ray graph bound; r=8 and r=9 upper bounds are written proofs, not enumerated here.'
}
with OUT.open('x',encoding='utf-8') as f:
    json.dump(out,f,indent=2)
    f.write('\n')
print(json.dumps({k:out[k] for k in ('status','native_clock','source_sha256','per_repeat_vertex_count','M9_upper')},indent=2))
