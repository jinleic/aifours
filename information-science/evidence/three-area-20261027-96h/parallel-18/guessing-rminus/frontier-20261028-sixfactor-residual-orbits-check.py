#!/usr/bin/env python3
"""Check factor-preserving automorphism orbits of seven residual 6-factor cases."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-two-syndrome-mobius-census-result.json','a1be7e3a7dc9b491cbe3395d2c9342c7fd419b086ea3144ec4971c79df31e957')
OUT=ROOT/'frontier-20261028-sixfactor-residual-orbits-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),
   (8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
REPS=((1,2,5,6,8,9),(1,3,4,6,7,10),(2,3,4,6,7,10),(2,3,5,6,9,10))


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);E={tuple(sorted((v,w))) for v in N for w in N[v]};ts={tuple(sorted(T)):i+1 for i,T in enumerate(TRI)};fp=[]
    for p in P:
        if set(p)!=set(N) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('AUTOMORPHISM')
        moved=[tuple(sorted(p[v-1] for v in T)) for T in TRI]
        if set(moved)!=set(ts):raise ValueError('FACTORS')
        fp.append(tuple(ts[T] for T in moved))
    target={tuple(r['factors']) for r in src['cases'] if r['factor_mask'].bit_count()==6 and r['color'] is None}
    if len(target)!=7:raise ValueError('TARGET')
    orbits=[]
    for rep in REPS:
        orb={tuple(sorted(p[t-1] for t in rep)) for p in fp}
        if orbits and orb&set().union(*orbits):raise ValueError('OVERLAP')
        orbits.append(orb)
    if set().union(*orbits)!=target or [len(x) for x in orbits]!=[1,2,2,2]:raise ValueError('COVERAGE')
    out={'source_receipt_sha256':SOURCE[1],'residual_cases':len(target),'factor_preserving_automorphisms':len(P),
         'representative_orbits':[{'representative':r,'members':sorted(o)} for r,o in zip(REPS,orbits)],
         'all_checked':True,'limits':'Exact graph/factor orbit coverage only; the weighted-flow oracle and entropy implications are separate.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
