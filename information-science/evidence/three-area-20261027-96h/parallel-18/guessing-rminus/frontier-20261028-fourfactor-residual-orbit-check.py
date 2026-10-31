#!/usr/bin/env python3
"""Check automorphism orbits of 41 four-factor fractional-method residuals."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json','218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8')
DIRECT=('frontier-20261028-fourfactor-plane-fractional-check-result.json','a7fe6d5a76a804d6f853ee97c07fde10a6358d39fa852b6846335835c15ce9d5')
OUT=ROOT/'frontier-20261028-fourfactor-residual-orbit-check-result.json'
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))

def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('HASH')
    return json.loads(raw)

def main():
    src=pin(SRC);direct=pin(DIRECT)
    if not direct['all_checked'] or direct['certificate_sha256']!='863f74fe993c7b6adbd867b97fa0b83de54fe8c65f4c699e66b41ebb8a8db4f4':raise ValueError('FRACTIONAL_RECEIPT')
    E={tuple(sorted((u,v))) for u in N for v in N[u]};look={tuple(sorted(t)):i for i,t in enumerate(TRI)};actions=[]
    for p in P:
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH')
        image=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(image)!=set(look):raise ValueError('FACTORS')
        actions.append(tuple(look[t] for t in image))
    residual=set()
    for x in src['cases']:
        if x['color'] is not None:continue
        F=x['factors'];residual.add(frozenset(sum(1<<(F[i]-1) for i in range(4) if m>>i&1) for m in x['syndrome_plane']))
    if len(residual)!=41:raise ValueError('COUNT')
    def image(x,f):return frozenset(sum(1<<f[i] for i in range(10) if m>>i&1) for m in x)
    unvisited=set(residual);orbits=[]
    while unvisited:
        rep=min(unvisited,key=lambda x:tuple(sorted(x)));orbit={image(rep,f) for f in actions}
        if not orbit<=unvisited:raise ValueError('ORBIT')
        unvisited-=orbit;orbits.append({'representative':sorted(rep),'members':[sorted(o) for o in sorted(orbit,key=lambda x:tuple(sorted(x)))]})
    sizes=Counter(len(x['members']) for x in orbits)
    if sizes!={1:1,2:4,4:8}:raise ValueError('ORBIT_COUNTS')
    out={'all_checked':True,'residual_planes':41,'orbits':orbits,'orbit_size_counts':dict(sizes),'limits':'Exact combinatorial orbit accounting, not a proof of any remaining entropy case.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'all_checked':True,'residual_planes':41,'orbit_count':len(orbits),'orbit_size_counts':dict(sizes)},indent=2))


if __name__=='__main__':main()
