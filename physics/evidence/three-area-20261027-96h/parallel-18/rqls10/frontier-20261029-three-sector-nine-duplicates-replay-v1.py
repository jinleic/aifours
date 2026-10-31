#!/usr/bin/env python3
"""Independent direct adjacency-mask replay of D=9 graph maxima."""
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / 'frontier-20261029-three-sector-nine-duplicates-v1.json'
OUT = ROOT / 'frontier-20261029-three-sector-nine-duplicates-replay-v1.json'
EXPECTED = '338dcb9f7d232c206627b9d1fe827b0a4ea6e13d6c56c34d22c1b89926c2122a'
if OUT.exists():
    raise FileExistsError(OUT)
raw = CERT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED
cert = json.loads(raw)


def c4free(adj):
    return all((adj[a]&adj[b]).bit_count()<2 for a,b in itertools.combinations(range(len(adj)),2))


def cost(adj,w):
    edges = [(i,j) for i,j in itertools.combinations(range(len(w)),2) if adj[i] >> j & 1]
    triangles = set()
    result = 0
    for i,j in edges:
        common = adj[i]&adj[j]
        assert common.bit_count()<=1
        if common:
            triangles.add(tuple(sorted((i,j,common.bit_length()-1))))
        else:
            result += min(w[i],w[j])
    for tri in triangles:
        m = [w[i]+1 for i in tri]
        result += min(*(m[a]*m[b] for a,b in itertools.combinations(range(3),2)),
                      *(3*x for x in m))-1
    return result


reported = {tuple(r['weights']):r['maximum_cost'] for r in cert['weighted_partition_extrema']}
observed = {}
counts = []
for n in range(1,8):
    pairs = list(itertools.combinations(range(n),2))
    weights = set()
    for seps in itertools.combinations(range(1,9),n-1):
        points = (0,)+seps+(9,)
        weights.add(tuple(sorted(points[i+1]-points[i] for i in range(n))))
    best = {w:-1 for w in weights}
    accepted = 0
    for mask in range(1<<len(pairs)):
        adj = [0]*n
        z = mask
        while z:
            bit = z&-z
            a,b = pairs[bit.bit_length()-1]
            z -= bit
            adj[a] |= 1<<b
            adj[b] |= 1<<a
        if not c4free(adj):
            continue
        accepted += 1
        for w in best:
            best[w] = max(best[w],cost(adj,w))
    observed.update(best)
    counts.append({'repeat_ray_types':n,'graphs':accepted,'max_cost':max(best.values())})
assert observed == reported
assert counts == cert['per_repeat_vertex_count']
assert max(observed.values()) <= 13
# Independent check of the nine-vertex positive graph; its upper bound is written.
adj = [0]*9
for a,b in cert['nine_vertex_13_edge_positive_control']:
    adj[a] |= 1<<b
    adj[b] |= 1<<a
assert c4free(adj) and sum(a.bit_count() for a in adj)==26 and cost(adj,(1,)*9)==13
cycle = [0]*4
for a,b in ((0,1),(1,2),(2,3),(3,0)):
    cycle[a] |= 1<<b
    cycle[b] |= 1<<a
assert not c4free(cycle)

out = {
    'status':'INDEPENDENT_D9_GRAPH_REPLAY_PASS_UNREVIEWED',
    'native_clock':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),
    'certificate_sha256':EXPECTED,
    'replay_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'weight_partitions_checked':len(observed),
    'per_repeat_vertex_count':counts,
    'controls':['13-edge C4-free graph','4-cycle rejected'],
    'limitation':'r=8,9 upper bounds and the 21-vertex near-equality contradiction are written mathematics, not enumerated here.'
}
with OUT.open('x',encoding='utf-8') as f:
    json.dump(out,f,indent=2)
    f.write('\n')
print(json.dumps(out,indent=2))
