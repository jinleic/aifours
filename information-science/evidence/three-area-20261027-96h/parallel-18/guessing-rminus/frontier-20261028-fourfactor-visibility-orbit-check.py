#!/usr/bin/env python3
"""Exact visibility-hypothesis and factor-automorphism coverage of 41 planes."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json','218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8')
DUAL=('frontier-20261028-fourfactor-visibility-dual-check-result.json','b2cb45c7876f705401d1b595c46024b62c27e1976b7049e7f9c8cd59e185680e')
OUT=ROOT/'frontier-20261028-fourfactor-visibility-orbit-check-result.json'
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))

def pin(x):
    raw=(ROOT/x[0]).read_bytes()
    if sha256(raw).hexdigest()!=x[1]:raise ValueError('HASH')
    return json.loads(raw)

def main():
    src=pin(SRC);dual=pin(DUAL)
    if not dual['all_checked'] or [x['factors'] for x in dual['cases']]!=[[2,5,6,9],[3,4,7,10]]:raise ValueError('DUALS')
    E={tuple(sorted((u,v))) for u in N for v in N[u]};lookup={tuple(sorted(t)):i for i,t in enumerate(TRI)};actions=[]
    for p in P:
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH')
        moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(moved)!=set(lookup):raise ValueError('FACTOR_AUTOMORPHISM')
        actions.append(tuple(lookup[t] for t in moved))
    records=[];residual=set()
    for x in src['cases']:
        if x['color'] is not None:continue
        F=tuple(x['factors']);p=frozenset(sum(1<<(F[i]-1) for i in range(4) if m>>i&1) for m in x['syndrome_plane'])
        residual.add(p);records.append((F,p))
    if len(residual)!=41:raise ValueError('RESIDUAL_COUNT')
    def image(plane,f):return frozenset(sum(1<<f[i] for i in range(10) if m>>i&1) for m in plane)
    selected={};covered=set()
    for F,vs in (((2,5,6,9),(5,9)),((3,4,7,10),(6,7))):
        here=set()
        for factors,plane in records:
            if factors!=F:continue
            if all(all(m & sum(1<<(t-1) for t in F if v in TRI[t-1]) for m in plane) for v in vs):here.add(plane)
        selected[str(F)]=[sorted(p) for p in sorted(here,key=lambda z:tuple(sorted(z)))]
        for plane in here:covered|={image(plane,f) for f in actions}
    if [len(x) for x in selected.values()]!=[3,7] or len(covered)!=13 or not covered<=residual:raise ValueError('COVERAGE')
    out={'all_checked':True,'direct_visibility_planes':selected,'covered_planes':[sorted(p) for p in sorted(covered,key=lambda z:tuple(sorted(z)))],
         'covered_count':len(covered),'remaining_residual':len(residual-covered),'limits':'Exact projection-injectivity and graph/factor orbits; actual entropy certificate application and tensorization require written review.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('covered_planes','direct_visibility_planes')},indent=2))


if __name__=='__main__':main()
