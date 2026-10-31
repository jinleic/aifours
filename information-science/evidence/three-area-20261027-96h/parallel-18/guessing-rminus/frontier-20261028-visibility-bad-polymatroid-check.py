#!/usr/bin/env python3
"""Exact check of positive-gap polymatroids for maximal bad visibility sets.

Usage: python3 script.py OUT.json CANDIDATES.json SHA
The candidate file lists, per bad set W, the full rational entropy vector on
all 2,047 nonempty subsets of (X_1..X_10,S).
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
S=1<<10;V=S-1;FULL=(1<<11)-1

def vm(vs):return sum(1<<(v-1) for v in vs)

def check(W,h):
    if len(h)!=FULL+1 or h[0]!=0:raise ValueError('VECTOR')
    for i in range(11):
        if h[FULL]<h[FULL^(1<<i)]:raise ValueError('MONOTONE')
    count=0
    for i,j in combinations(range(11),2):
        a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
        while True:
            if h[k|a]+h[k|b]-h[k|a|b]-h[k]<0:raise ValueError('CMI')
            count+=1
            if not k:break
            k=(k-1)&rest
    for v in range(1,11):
        n=vm(N[v]);L=vm({u for t in TRI if v in t for u in t if u!=v});b=1<<(v-1)
        if h[n|b]!=h[n]:raise ValueError('GRAPH_FD')
        if h[L|S|b]!=h[L|S]:raise ValueError('LOCAL_FD')
        if v in W and h[n|S]!=h[n]:raise ValueError('VISIBILITY')
    if h[V|S]!=h[V]:raise ValueError('GLOBAL')
    gap=h[V]-Fraction(2,3)*sum(h[1<<i] for i in range(10))
    if gap<=0:raise ValueError('NO_GAP')
    return {'W':sorted(W),'gap':str(gap),'syndrome_entropy':str(h[S]),'elemental_cmi':count}

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    doc=json.loads(raw);results=[];controls={}
    for case in doc['cases']:
        W=set(case['W']);h=[Fraction(0)]+[Fraction(x) for x in case['entropy_vector']]
        results.append(check(W,h))
        bad=list(h);v=min(W);n=vm(N[v]);bad[n|S]=bad[n]+1
        try:check(W,bad)
        except ValueError as e:controls[str(sorted(W))]=str(e)
        else:raise ValueError('CONTROL')
    report={'candidates_sha256':sys.argv[3],'all_checked':True,'cases':results,'negative_controls':controls,
            'limits':'Abstract rational polymatroids satisfying the listed visibility-system rows; not entropic, not FD laws, not gain witnesses.'}
    with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
