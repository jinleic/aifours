#!/usr/bin/env python3
"""Exact graph/factor automorphisms and four-factor cover orbits."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-mincover-orbits-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
GEN=((8,10,7,6,9,3,4,1,2,5),(1,5,6,7,2,3,4,8,9,10))
SEARCH_REPS=((2,3,5,6),(1,3,6,7),(3,4,6,7),(3,5,6,7),(2,5,6,9),(3,4,7,10))


def compute():
    E={tuple(sorted((u,v))) for u in N for v in N[u]};identity=tuple(range(1,11));G={identity};todo=[identity]
    while todo:
        p=todo.pop()
        for g in GEN:
            q=tuple(g[p[i]-1] for i in range(10))
            if q not in G:G.add(q);todo.append(q)
    if len(G)!=8 or any({tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E for p in G):raise ValueError('AUTOMORPHISMS')
    ts={tuple(sorted(T)):i for i,T in enumerate(TRI)};P=[]
    for p in G:
        moved=[tuple(sorted(p[v-1] for v in T)) for T in TRI]
        if set(moved)==set(ts):P.append(tuple(ts[T] for T in moved))
    if len(P)!=4:raise ValueError('FACTOR_GROUP')
    covers=[]
    for J in combinations(range(10),4):
        U=set().union(*(set(TRI[t]) for t in J))
        if U==set(N):covers.append(J)
    if len(covers)!=19:raise ValueError('COVERS')
    for J in covers:
        d=[sum(v in TRI[t] for t in J) for v in N]
        if sorted(d)!=[1]*8+[2]*2:raise ValueError('BIT_PATTERN')
        hi=[v for v in N if sum(v in TRI[t] for t in J)==2]
        if hi[1] not in N[hi[0]]:raise ValueError('HIGH_NONEDGE')
    remain=set(covers);orbits=[]
    while remain:
        x=min(remain);orb={tuple(sorted(p[t] for t in x)) for p in P}
        if not orb<=remain:raise ValueError('ORBIT')
        orbits.append(sorted(orb));remain-=orb
    if sorted(map(len,orbits))!=[1,2,4,4,4,4]:raise ValueError('ORBIT_SIZES')
    assignments=[next((i for i,o in enumerate(orbits) if tuple(t-1 for t in rep) in o),None) for rep in SEARCH_REPS]
    if None in assignments or len(set(assignments))!=6:raise ValueError('SEARCH_REPRESENTATIVES')
    return {'graph_group_order':len(G),'factor_preserving_group_order':len(P),'four_factor_covers':len(covers),
            'vertex_bit_pattern':'eight 1-bit, two 2-bit; the two 2-bit vertices adjacent','search_representatives':SEARCH_REPS,
            'orbits':[{'representative_one_based':[t+1 for t in o[0]],'size':len(o),
                       'members_one_based':[[t+1 for t in J] for J in o]} for o in orbits]}


def main():
    checks=compute();out={'exact_checks':checks,'all_checked':True,
                         'limits':'Graph/factor orbit and degree census only; entropy conditioning and witness equivalence are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(checks,indent=2))


if __name__=='__main__':main()
