#!/usr/bin/env python3
"""Independent direct factor-cover and explicit-permutation orbit replay."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-mincover-orbits-check-result.json','b27391385dfadb3c3715e3ed49b998c14800dc6da9e8024cc4d50d5dc633f9f2')
OUT=ROOT/'frontier-20261028-mincover-orbits-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),
   (8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
REPS=((2,3,5,6),(1,3,6,7),(3,4,6,7),(3,5,6,7),(2,5,6,9),(3,4,7,10))


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw)['exact_checks'];E={tuple(sorted((v,w))) for v in N for w in N[v]};T={tuple(sorted(t)) for t in TRI};fp=[]
    for p in P:
        if set(p)!=set(N) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH_PERM')
        moved=[tuple(sorted(p[v-1] for v in tri)) for tri in TRI]
        if set(moved)!=T:raise ValueError('FACTOR_PERM')
        fp.append(tuple(TRI.index(tri)+1 for tri in moved))
    if any(tuple(p[q[i]-1] for i in range(10)) not in P for p in P for q in P):raise ValueError('GROUP_CLOSURE')
    covers=[]
    for J in combinations(range(1,11),4):
        if set().union(*(set(TRI[t-1]) for t in J))==set(N):covers.append(J)
    if len(covers)!=19:raise ValueError('COVERS')
    orbitlist=[]
    for rep in REPS:
        orbit={tuple(sorted(p[t-1] for t in rep)) for p in fp}
        if orbitlist and orbit&set().union(*orbitlist):raise ValueError('OVERLAP')
        orbitlist.append(orbit)
    if set().union(*orbitlist)!=set(covers) or sorted(map(len,orbitlist))!=[1,2,4,4,4,4]:raise ValueError('COVERAGE')
    for J in covers:
        d={v:sum(v in TRI[t-1] for t in J) for v in N}
        high=[v for v in N if d[v]==2]
        if sorted(d.values())!=[1]*8+[2]*2 or high[1] not in N[high[0]]:raise ValueError('BIT_PATTERN')
    if src['four_factor_covers']!=19 or src['factor_preserving_group_order']!=4:raise ValueError('SOURCE')
    out={'source_receipt_sha256':SOURCE[1],'four_subsets_checked':210,'four_factor_covers':len(covers),
         'explicit_factor_preserving_permutations_checked':len(P),'search_orbit_sizes':[len(o) for o in orbitlist],
         'all_checked':True,'limits':'Exact graph/factor orbit coverage only; probabilistic reduction is written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
