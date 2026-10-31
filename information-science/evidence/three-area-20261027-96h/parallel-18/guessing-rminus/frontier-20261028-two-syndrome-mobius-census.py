#!/usr/bin/env python3
"""Exact support-mask Mobius census and 3-color witnesses for k<=6 covers."""
from itertools import product
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-two-syndrome-mobius-census-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def allowed(J):
    fs=[i for i in range(10) if J>>i&1];k=len(fs);full=(1<<k)-1
    inc=[sum(1<<j for j,t in enumerate(fs) if v in TRI[t]) for v in range(1,11)]
    union=[0]*1024;bits=[0]*1024
    for M in range(1,1024):
        bit=M&-M;v=bit.bit_length()-1;prev=M^bit;union[M]=union[prev]|inc[v];bits[M]=bits[prev]+inc[v].bit_count()
    f0=[1<<(bits[M]-union[M].bit_count()) for M in range(1024)]
    f1=[f0[M] if union[M]==full else 0 for M in range(1024)]
    for i in range(10):
        for M in range(1024):
            if M>>i&1:f0[M]-=f0[M^(1<<i)];f1[M]-=f1[M^(1<<i)]
    if min(f0)<0 or min(f1)<0:raise ValueError('MOBIUS_NEGATIVE')
    nb=[sum(1<<(u-1) for u in N[v]) for v in range(1,11)]
    return [M for M in range(1,1024) if (f0[M] or f1[M]) and all(M&nb[v] for v in range(10) if M>>v&1)]


def main():
    color_values=np.array([(0,)+c for c in product(range(3),repeat=9)],np.uint8);color_masks=np.zeros((3,len(color_values)),np.uint16)
    for i in range(10):
        for c in range(3):color_masks[c]|=(color_values[:,i]==c).astype(np.uint16)<<i
    records=[];by_size={}
    for J in range(1,1024):
        k=J.bit_count()
        if k>6:continue
        covered=set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))
        if covered!=set(N):continue
        masks=allowed(J);mins=[]
        for D in sorted(masks,key=lambda x:(x.bit_count(),x)):
            if not any(M&D==M for M in mins):mins.append(D)
        valid=np.ones(len(color_values),bool)
        for D in mins:
            valid &=np.all((color_masks&D)!=D,axis=0)
            if not np.any(valid):break
        color=color_values[int(np.flatnonzero(valid)[0])].tolist() if np.any(valid) else None
        records.append({'factor_mask':J,'factors':[i+1 for i in range(10) if J>>i&1],
                        'allowed_difference_masks':masks,'color':color})
        key=str(k);by_size.setdefault(key,{'covers':0,'colorable':0,'no_universal_color':0});by_size[key]['covers']+=1
        by_size[key]['colorable' if color is not None else 'no_universal_color']+=1
    if by_size!={'4':{'covers':19,'colorable':19,'no_universal_color':0},
                '5':{'covers':90,'colorable':90,'no_universal_color':0},
                '6':{'covers':145,'colorable':138,'no_universal_color':7}}:raise ValueError(('COUNTS',by_size))
    out={'factor_subsets_checked':sum(1 for J in range(1,1024) if J.bit_count()<=6),'cover_counts':by_size,
         'cases':records,'all_checked':True,
         'limits':'Exact support-mask counts and universal color witnesses only; conditional entropy and no-gap implications are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
