#!/usr/bin/env python3
"""Exact-check positive-gap polymatroids for a specified syndrome outer relaxation."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-two-syndrome-symmetric-lp-result.json','82c2f65850380925bc4ecf76384c1b2e394f23e62aeffdfea7f8d548dcaccc3f')
OUT=ROOT/'frontier-20261028-two-syndrome-polymatroid-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),
   (8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
S=1<<10;V=S-1;FULL=(1<<11)-1

def mask(vertices):return sum(1<<(v-1) for v in vertices)

def check(h,case):
    if h[0]!=0:raise ValueError('ZERO')
    for i in range(11):
        if h[FULL]<h[FULL^(1<<i)]:raise ValueError('MONOTONICITY')
    count=0
    for i,j in combinations(range(11),2):
        a,b=1<<i,1<<j;k=FULL^a^b
        while True:
            if h[k|a]+h[k|b]-h[k|a|b]-h[k]<0:raise ValueError('CMI')
            count+=1
            if not k:break
            k=(k-1)&(FULL^a^b)
    for v in range(1,11):
        nm=mask(N[v]);a=1<<(v-1)
        if h[nm|a]!=h[nm]:raise ValueError('GRAPH_FD')
        if h[nm|S]!=h[nm]:raise ValueError('SYNDROME_NEIGHBORHOOD')
        cap=sum(v in TRI[t-1] for t in case)
        if h[a]>cap:raise ValueError('SYMBOL_CAP')
    for t in case:
        m=mask(TRI[t-1])
        if h[m|S]!=h[m]:raise ValueError('SYNDROME_TRIANGLE')
    if 3*h[V]+17*h[S]-2*sum(h[S|(1<<i)] for i in range(10))>0:raise ValueError('SYNDROME_GATE')
    if h[S]>1:raise ValueError('BINARY_CAP')
    for a in range(1,V+1):
        rank=sum(min((a&mask(TRI[t-1])).bit_count(),2) for t in case)
        if h[a|S]-h[S]>rank:raise ValueError('CONDITIONAL_PROJECTION_RANK')
    gap=h[V]-Fraction(2,3)*sum(h[1<<i] for i in range(10))
    if gap<=0:raise ValueError('NO_GAP')
    return {'gap':str(gap),'syndrome_entropy':str(h[S]),'elemental_cmi':count,'conditional_projection_caps':V,'actual_vertex_caps_checked':10}


def main():
    raw=(ROOT/SRC[0]).read_bytes()
    if sha256(raw).hexdigest()!=SRC[1]:raise ValueError('HASH')
    doc=json.loads(raw);tri_lookup={tuple(sorted(t)):i+1 for i,t in enumerate(TRI)};out=[];first=None
    for result in doc['cases']:
        case=tuple(result['factors']);J=set(case);group=[]
        for p in P:
            fp=[tri_lookup[tuple(sorted(p[v-1] for v in tri))] for tri in TRI]
            if {fp[t-1] for t in J}==J:group.append(p)
        def move(m,p):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m&(1<<i))
        canonical={m:min(move(m,p) for p in group) for m in range(1,FULL+1)}
        reps=result['orbit_representatives']
        if sorted(set(canonical.values()))!=reps:raise ValueError('ORBITS')
        vals={r:Fraction(x).limit_denominator(100000) for r,x in zip(reps,result['primal'])}
        if len(vals)!=len(reps):raise ValueError('COORDINATES')
        h=[Fraction(0)]+[vals[canonical[m]] for m in range(1,FULL+1)]
        details=check(h,case);out.append({'factors':case,'group_size':len(group),**details})
        if first is None:first=(h,case)
    bad=list(first[0]);bad[S]=Fraction(-1)
    try:check(bad,first[1])
    except ValueError as e:control=str(e)
    else:raise ValueError('MUTATION_ACCEPTED')
    result={'numerical_input_sha256':SRC[1],'cases':out,'all_checked':True,'negative_control':control,
            'limits':'These are rational polymatroids in the explicitly listed outer relaxation, not entropic laws, FD strategies, no-gain results, full-copy LP points, or certified optima.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
