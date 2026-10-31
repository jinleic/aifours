#!/usr/bin/env python3
"""Enumerate symmetry-invariant syndrome color partitions with local bicover."""
from itertools import product
from pathlib import Path
import json

TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
OUT=Path(__file__).resolve().parent/'frontier-20261028-three-syndrome-symmetric-color-census-result.json'
EXPECTED={((1,2,5,6,8,9),(3,4,7,10)),((1,2,6,8),(3,4,7,10),(5,9)),
          ((1,2,5,6,8,9),(3,10),(4,7)),((1,2,6,8),(3,10),(4,5,7,9))}

def main():
    lookup={tuple(sorted(t)):i+1 for i,t in enumerate(TRI)};actions=[]
    for p in P:
        moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(moved)!=set(lookup):raise ValueError('FACTOR_ACTION')
        actions.append(tuple(lookup[t] for t in moved))
    unseen=set(range(1,11));orbits=[]
    while unseen:
        t=min(unseen);orb={f[t-1] for f in actions}
        if not orb<=unseen:raise ValueError('ORBIT_OVERLAP')
        orbits.append(tuple(sorted(orb)));unseen-=orb
    seen=set();passing=0
    for colors in product(range(3),repeat=len(orbits)):
        c={t:colors[i] for i,o in enumerate(orbits) for t in o}
        if not all(len({c[i+1] for i,t in enumerate(TRI) if v in t})>=2 for v in range(1,11)):continue
        passing+=1;blocks=tuple(sorted(tuple(i for i in range(1,11) if c[i]==j) for j in set(colors)))
        seen.add(blocks)
    if seen!=EXPECTED:raise ValueError('PARTITIONS')
    bad=set(EXPECTED);bad.remove(next(iter(bad)))
    if seen==bad:raise ValueError('MUTATION_CONTROL')
    out={'all_checked':True,'factor_orbits':orbits,'color_assignments':3**len(orbits),'bicover_assignments':passing,
         'partitions_up_to_color_relabeling':sorted(seen),'negative_control':'missing partition rejected',
         'limits':'Only colorings constant on each factor-preserving-group orbit with no constant syndrome coordinates and at least two colors incident at every vertex; not all 3-syndrome patterns.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
