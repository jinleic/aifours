#!/usr/bin/env python3
"""Exact universal 3-color screen for every 4-factor syndrome plane cover."""
from itertools import combinations,product
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-three-syndrome-fourfactor-color-screen-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))

def geometry(factors):
    Ts=[TRI[t-1] for t in factors];pos={};k=0
    for v in range(1,11):pos[v]=tuple(range(k,k+sum(v in T for T in Ts)));k+=len(pos[v])
    if k!=12 or any(not pos[v] for v in pos):raise ValueError('GEOMETRY')
    def syndrome(x):
        y=0
        for j,T in enumerate(Ts):
            p=0
            for v in T:p^=x>>pos[v][[i for i,U in enumerate(Ts) if v in U].index(j)]&1
            y|=p<<j
        return y
    masks=[sum(1<<b for b in pos[v]) for v in range(1,11)]
    groups=[set() for _ in range(16)]
    for x in range(1,4096):
        active=sum(1<<i for i in range(10) if x&masks[i]);valid=True
        for v in range(1,11):
            if active>>(v-1)&1 and not any(active>>(u-1)&1 for u in N[v]):valid=False;break
        if valid:groups[syndrome(x)].add(active)
    return groups


def main():
    color_values=np.array([(0,)+x for x in product(range(3),repeat=9)],dtype=np.uint8);color_masks=np.zeros((3,len(color_values)),dtype=np.uint16)
    for v in range(10):
        for c in range(3):color_masks[c]|=(color_values[:,v]==c).astype(np.uint16)<<v
    records=[];covers=[]
    for factors in combinations(range(1,11),4):
        if set().union(*(set(TRI[t-1]) for t in factors))!=set(range(1,11)):continue
        covers.append(factors);groups=geometry(factors)
        for a,b in combinations(range(1,16),2):
            c=a^b
            if b>=c or (a|b|c)!=15:continue
            allowed=groups[0]|groups[a]|groups[b]|groups[c]
            mins=[]
            for D in sorted(allowed,key=lambda x:(x.bit_count(),x)):
                if not any(M&D==M for M in mins):mins.append(D)
            valid=np.ones(len(color_values),bool)
            for D in mins:
                valid&=np.all((color_masks&D)!=D,axis=0)
                if not np.any(valid):break
            selected=int(np.flatnonzero(valid)[0]) if np.any(valid) else None
            records.append({'factors':factors,'syndrome_plane':[a,b,c],'allowed_masks':sorted(allowed),'color':color_values[selected].tolist() if selected is not None else None})
    if len(covers)!=19 or len(records)!=247:raise ValueError('COUNT')
    out={'all_checked':True,'factor_covers':len(covers),'covering_direction_planes':len(records),'universal_colors_found':sum(r['color'] is not None for r in records),
         'cases':records,'limits':'Exact 4-factor difference-mask enumeration and universal color proposals; independently replay all masks and colors before any theorem.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
