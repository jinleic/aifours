#!/usr/bin/env python3
"""Bounded MIP search for a smaller five-wheel-forcing triangle-code support."""
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-wheel-difference-cover-search-result.json'
T=((1,2,3),(1,3,4),(2,3,9),(3,4,8),(3,8,9));W=(1,2,3,4,8,9)
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
EDGES=tuple((a,b) for a,b in combinations(W,2) if b in N[a])


def pattern(t,e):
    a,b,c=T[t];return {(a,b):1,(a,c):2,(b,c):3}[tuple(e)]<<(2*t)


def decode(x):
    out=[0]*10
    for t,(a,b,c) in enumerate(T):
        bits=(x>>(2*t))&3
        if bits&1:out[a-1]^=1<<t;out[b-1]^=1<<t
        if bits&2:out[a-1]^=1<<t;out[c-1]^=1<<t
    return tuple(out)


def verify(selected):
    if len(set(selected))!=len(selected) or any(not 0<=x<1024 for x in selected):raise ValueError('WORDS')
    words=[decode(x) for x in selected];forced=set()
    for u,v in combinations(words,2):
        D=tuple(i+1 for i in range(10) if u[i]!=v[i])
        if any(not any(w in D for w in N[x]) for x in D):raise ValueError('FD')
        if len(D)==2:forced.add(D)
    if not set(EDGES)<=forced:raise ValueError('WHEEL')
    return words


def main():
    start=monotonic();moves=[]
    for e in EDGES:
        basis=[pattern(t,e) for t in range(len(T)) if set(e)<=set(T[t])]
        if not basis:raise ValueError('MOVE')
        for mask in range(1,1<<len(basis)):
            x=0
            for i,b in enumerate(basis):
                if mask>>i&1:x^=b
            moves.append((e,x))
    pairs=[]
    for e,x in moves:
        for u in range(1024):
            v=u^x
            if u<v:pairs.append((u,v,e))
    if len(moves)!=20 or len(pairs)!=10240:raise ValueError(('COUNTS',len(moves),len(pairs)))
    n=1024+len(pairs);starts=[];inds=[];vals=[];lo=[];hi=[]
    def row(d,l,u):
        starts.append(len(inds))
        for k,v in d.items():inds.append(k);vals.append(float(v))
        lo.append(float(l));hi.append(float(u))
    for j,(u,v,e) in enumerate(pairs):
        row({1024+j:1,u:-1},-highspy.kHighsInf,0);row({1024+j:1,v:-1},-highspy.kHighsInf,0)
    for e in EDGES:row({1024+j:1 for j,(_,_,f) in enumerate(pairs) if f==e},1,highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=n,len(starts);lp.col_cost_=np.array([1.]*1024+[0.]*len(pairs))
    low=np.zeros(n);high=np.ones(n);low[0]=1;lp.col_lower_,lp.col_upper_=low,high;lp.integrality_=[highspy.HighsVarType.kInteger]*n
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],np.int32);lp.a_matrix_.index_=np.array(inds,np.int32);lp.a_matrix_.value_=np.array(vals,float)
    seedp=((0,(1,2)),(1,(1,3)),(1,(1,4)),(2,(2,3)),(2,(2,9)),(3,(4,8)),(4,(3,8)),(4,(3,9)))
    seed={0}|{pattern(t,e) for t,e in seedp};verify(sorted(seed));initial=np.zeros(n)
    for x in seed:initial[x]=1
    for j,(u,v,e) in enumerate(pairs):
        if u in seed and v in seed:initial[1024+j]=1
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',20.)
    solver.passModel(lp);seed_status=str(solver.setSolution(n,np.arange(n,dtype=np.int32),initial));solver.run();sol=solver.getSolution()
    selected=[i for i in range(1024) if sol.col_value[i]>.5] if sol.value_valid else []
    words=verify(selected) if selected else []
    out={'triangle_factors':T,'wheel_edges':EDGES,'move_count':len(moves),'move_pairs':len(pairs),
         'solver_status_float_unverified':solver.modelStatusToString(solver.getModelStatus()),'seed_status':seed_status,
         'selected_codewords':selected,'selected_words':words,'support_size':len(selected),'elapsed_seconds':monotonic()-start,
         'limits':'A finite-support coloring-method obstruction in this restricted linear code only; no lower-bound proof, strict-gain law or global guessing-number conclusion.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
