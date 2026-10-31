#!/usr/bin/env python3
"""Bounded six-support FD partition search; integer verification of incumbents.

Floating entropies and MIP status only guide proposals. A rational law has
Delta>0 iff the exact integer comparison computed below is strict.
"""
from itertools import combinations
from math import log,prod
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-six-point-fd-search-result.json'
N=((1,2,3,4,5,6),(0,2,6,8,9),(0,1,3,7,8),(0,2,4,7,9),
   (0,3,5,8,9),(0,4,6,7,8),(0,1,5,7,9),(2,3,5,6,8,9),
   (1,2,4,5,7),(1,3,4,6,7))
WEIGHTS=((1,1,1,1,1,1),(2,1,1,1,1,1),(5,2,2,1,1,1),(8,4,2,1,1,1),(16,8,4,2,1,1),(49,1,1,1,1,1),(5,5,1,1,1,1),(9,7,5,3,2,1))
CASE_SECONDS=5.


def partitions(n):
    result=[]
    def visit(a):
        if len(a)==n:result.append(tuple(a));return
        for v in range(max(a)+2):visit(a+[v])
    visit([0]);return result


def entropy_cost(a,t):
    m=sum(a);blocks=[sum(a[i] for i in range(6) if t[i]==v) for v in sorted(set(t))]
    return sum(-(b/m)*log(b/m) for b in blocks)


def exact_check(a,selected):
    if len(selected)!=10 or any(len(t)!=6 for t in selected):raise ValueError('INPUT')
    words=[tuple(selected[v][u] for v in range(10)) for u in range(6)]
    if len(set(words))!=6:raise ValueError('NOT_SIX_WORDS')
    for x,y in combinations(range(6),2):
        for i,neighbors in enumerate(N):
            if selected[i][x]!=selected[i][y] and all(selected[j][x]==selected[j][y] for j in neighbors):raise ValueError(('FD',x,y,i))
    m=sum(a);left=1
    for t in selected:
        for v in set(t):
            block=sum(a[i] for i in range(6) if t[i]==v);left*=block**(2*block)
    right=m**(17*m)*prod(v**(3*v) for v in a)
    return {'weight_numerators':list(a),'partitions':[list(t) for t in selected],
            'support_words':[list(w) for w in words],
            'exact_gap_test_left_gt_right':left>right,'left_integer':str(left),'right_integer':str(right)}


def main():
    start=monotonic();P=partitions(6);s=len(P)
    if s!=203 or len(set(P))!=203:raise ValueError('BELL6')
    pairs=list(combinations(range(6),2));starts=[];inds=[];vals=[];lower=[];upper=[]
    def row(d,lo,hi):
        starts.append(len(inds))
        for k,v in sorted(d.items()):
            if v:inds.append(k);vals.append(float(v))
        lower.append(float(lo));upper.append(float(hi))
    for i in range(10):row({i*s+t:1 for t in range(s)},1,1)
    for x,y in pairs:
        distinguishing=[t for t,part in enumerate(P) if part[x]!=part[y]]
        for i,neighbors in enumerate(N):
            d={i*s+t:-1 for t in distinguishing}
            for j in neighbors:
                for t in distinguishing:d[j*s+t]=1
            row(d,0,highspy.kHighsInf)
        row({i*s+t:1 for i in range(10) for t in distinguishing},1,highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=10*s,len(starts)
    lp.col_lower_=np.zeros(10*s);lp.col_upper_=np.ones(10*s);lp.integrality_=[highspy.HighsVarType.kInteger]*(10*s)
    lp.row_lower_,lp.row_upper_=np.array(lower),np.array(upper);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32);lp.a_matrix_.index_=np.array(inds,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float);lp.sense_=highspy.ObjSense.kMinimize
    # A six-word restriction of the ternary XOR code on graph triangle 1,2,3.
    points=((0,0),(0,1),(0,2),(1,0),(1,1),(2,0))
    def canon(seq):
        lab={};out=[]
        for x in seq:
            if x not in lab:lab[x]=len(lab)
            out.append(lab[x])
        return tuple(out)
    seed_parts=[canon([x for x,y in points]),canon([y for x,y in points]),canon([(-x-y)%3 for x,y in points])]+[(0,)*6]*7
    exact_check((1,)*6,seed_parts)
    seed=np.zeros(10*s)
    for i,t in enumerate(seed_parts):seed[i*s+P.index(t)]=1
    results=[];witness=None
    for a in WEIGHTS:
        lp.col_cost_=np.array([entropy_cost(a,t) for _ in range(10) for t in P])
        solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',CASE_SECONDS)
        solver.passModel(lp);seed_status=str(solver.setSolution(10*s,np.arange(10*s,dtype=np.int32),seed))
        t0=monotonic();solver.run();solution=solver.getSolution()
        entry={'weights':list(a),'status_float_unverified':solver.modelStatusToString(solver.getModelStatus()),
               'seed_status':seed_status,'elapsed_seconds':monotonic()-t0}
        if solution.value_valid:
            chosen=[]
            for i in range(10):
                hit=[t for t in range(s) if solution.col_value[i*s+t]>.5]
                if len(hit)!=1:raise ValueError('ONEHOT')
                chosen.append(P[hit[0]])
            checked=exact_check(a,chosen);entry['exact_incumbent']=checked
            if checked['exact_gap_test_left_gt_right']:witness=checked;results.append(entry);break
        results.append(entry)
    out={'partition_count':len(P),'cases':results,'strict_gap_witness':witness,'per_case_time_limit_seconds':CASE_SECONDS,
         'elapsed_seconds':monotonic()-start,
         'limits':'Only eight selected six-support rational weight vectors were searched with bounded floating MIP; no nonexistence inference. Any strict integer incumbent needs separate exact graph, arithmetic and balancing verification.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
