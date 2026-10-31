#!/usr/bin/env python3
"""Check automorphism closure of one three-state syndrome partition pattern."""
from itertools import combinations
from pathlib import Path
import json

TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
U=frozenset((1,2,5,6,8,9));V=frozenset((3,4,7,10))
OUT=Path(__file__).resolve().parent/'frontier-20261028-three-syndrome-bipartition-symmetry-check-result.json'

def main():
    E={tuple(sorted((u,v))) for u in N for v in N[u]};lookup={tuple(sorted(t)):i+1 for i,t in enumerate(TRI)};pairs=set()
    for p in P:
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH')
        image=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(image)!=set(lookup):raise ValueError('TRIANGLES')
        f=[lookup[t] for t in image];a=frozenset(f[t-1] for t in U);b=frozenset(f[t-1] for t in V)
        pairs.add(tuple(sorted((tuple(sorted(a)),tuple(sorted(b))))))
        if any(not any(x in TRI[t-1] for t in a) or not any(x in TRI[t-1] for t in b) for x in N):raise ValueError('BICOVER')
    if len(pairs)!=1:raise ValueError('ORBIT')
    plane={0,1,2,3};triples=list(combinations(sorted(plane),3))
    if len(triples)!=4 or any(not any({x^b for x in t}=={0,1,2} for b in plane) for t in triples):raise ValueError('AFFINE_TRIPLES')
    out={'all_checked':True,'factor_preserving_automorphisms':len(P),'unordered_partition_orbit_size':len(pairs),
         'vertices_meeting_both_colors':len(N),'three_distinct_points_per_affine_translate':4,
         'limits':'Combinatorial orbit/bicover and affine-plane count only; entropy theorem and certificate require separate scientific review.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
