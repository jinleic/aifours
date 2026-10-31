#!/usr/bin/env python3
"""Exact fiber and marginal-count checks for a rare-syndrome FD law."""
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-rare-syndrome-counterexample-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
INC={v:[t for t,T in enumerate(TRI) if v in T] for v in range(1,11)}


def fiber(v,w):
    options=[]
    for t,T in enumerate(TRI):
        choices=[]
        for a,b in product(range(2),repeat=2):
            bits=(a,b,a^b)
            if all(bits[k]==((w[u-1]>>INC[u].index(t))&1) for k,u in enumerate(T) if u in N[v]):choices.append(bits)
        options.append(choices)
    words=set()
    for choices in product(*options):
        x=[0]*10
        for t,T in enumerate(TRI):
            for k,vv in enumerate(T):x[vv-1]|=choices[t][k]<<INC[vv].index(t)
        words.add(tuple(x))
    return words


def verify(fibers,w):
    if len(fibers)!=3 or [len(x) for x in fibers]!=[4,32,32]:raise ValueError('FIBER_SIZES')
    C=set().union(*fibers)
    if len(C)!=68:raise ValueError('FIBER_DISJOINTNESS')
    for i,F in zip((1,2,3),fibers):
        for x in F:
            if any(x[u-1]!=w[u-1] for u in N[i]) or x[i-1]==w[i-1]:raise ValueError('CONFLICT')
            for t,T in enumerate(TRI):
                if sum((x[u-1]>>INC[u].index(t))&1 for u in T)%2:raise ValueError('XOR')
    m=(1<<20)-68;counts=[[1<<17]*8 for _ in range(10)]
    for x in C:
        for i in range(10):counts[i][x[i]]-=1
    if any(sum(row)!=m or min(row)*9<=m for row in counts):raise ValueError('MARGINAL_BOUND')
    return {'fiber_sizes':[len(x) for x in fibers],'removed_codewords':len(C),'old_support_size':m,
            'minimum_marginal_count':min(min(row) for row in counts),'all_old_marginal_atoms_above_one_ninth':True,
            'outside_word':w,'outside_weight':'1/2^128'}


def main():
    w=(1,0,0,0,0,0,0,0,0,0);fibers=[fiber(v,w) for v in (1,2,3)];checks=verify(fibers,w);controls={}
    bad=[set(x) for x in fibers];bad[0].pop()
    try:verify(bad,w)
    except ValueError as exc:
        if str(exc)!='FIBER_SIZES':raise ValueError('WRONG_REASON')
        controls['removed_fiber_word']='FIBER_SIZES'
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact finite fibers and marginal counts; entropy asymptotics and full FD support proof are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
