#!/usr/bin/env python3
"""Check the paired syndrome-plane orbit among fractional-method residuals."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json','218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8')
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
OUT=ROOT/'frontier-20261028-fourfactor-paired-plane-orbit-check-result.json'

def main():
    raw=(ROOT/SRC[0]).read_bytes()
    if sha256(raw).hexdigest()!=SRC[1]:raise ValueError('HASH')
    src=json.loads(raw);lookup={tuple(sorted(T)):i for i,T in enumerate(TRI)}
    E=frozenset((12,576,588));orbit=set()
    for p in P:
        image=[tuple(sorted(p[v-1] for v in T)) for T in TRI]
        if set(image)!=set(lookup):raise ValueError('FACTOR_ACTION')
        f=[lookup[t] for t in image]
        orbit.add(frozenset(sum(1<<f[i] for i in range(10) if m>>i&1) for m in E))
    if orbit!={frozenset((12,576,588)),frozenset((68,520,588))}:raise ValueError('ORBIT')
    residual=set()
    for r in src['cases']:
        if r['color'] is not None:continue
        F=r['factors'];plane=frozenset(sum(1<<(F[i]-1) for i in range(4) if m>>i&1) for m in r['syndrome_plane'])
        residual.add(plane)
    if len(residual)!=41 or not orbit<=residual:raise ValueError('RESIDUAL')
    out={'all_checked':True,'orbit_size':len(orbit),'planes':[sorted(x) for x in sorted(orbit,key=lambda x:tuple(sorted(x)))],
         'previous_fractional_method_residual':len(residual),'remaining_residual_after_this_orbit':len(residual-orbit),
         'limits':'Combinatorial orbit coverage only; entropy theorem must be applied through graph/factor relabeling and remains under scientific review.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
