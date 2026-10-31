#!/usr/bin/env python3
"""Classify color partitions invariant under graph-induced factor permutations."""
from itertools import product
from pathlib import Path
import json

TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
OUT=Path(__file__).resolve().parent/'frontier-20261028-three-syndrome-equivariant-color-census-result.json'

def main():
    lookup={tuple(sorted(t)):i for i,t in enumerate(TRI)};actions=[]
    for p in P:
        moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(moved)!=set(lookup):raise ValueError('FACTOR_ACTION')
        actions.append(tuple(lookup[t] for t in moved))
    parts=set();valid=0
    for colors in product(range(3),repeat=10):
        if len(set(colors))<2 or any(len({colors[i] for i,t in enumerate(TRI) if v in t})<2 for v in range(1,11)):continue
        good=True
        for action in actions:
            f={};inv={}
            for i in range(10):
                a,b=colors[i],colors[action[i]]
                if (a in f and f[a]!=b) or (b in inv and inv[b]!=a):good=False;break
                f[a]=b;inv[b]=a
            if not good:break
        if not good:continue
        valid+=1;parts.add(tuple(sorted(tuple(i+1 for i,c in enumerate(colors) if c==j) for j in set(colors))))
    if len(parts)!=7:raise ValueError('PARTITION_COUNT')
    out={'all_checked':True,'assignments_checked':3**10,'equivariant_bicover_assignments':valid,'partitions_up_to_state_relabeling':sorted(parts),
         'limits':'Only factor-color partitions preserved by all four factor automorphisms, with no constant coordinates and local bicover; entropy claims checked separately.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
