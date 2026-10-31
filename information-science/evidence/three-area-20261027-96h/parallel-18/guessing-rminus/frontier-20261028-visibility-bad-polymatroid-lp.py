#!/usr/bin/env python3
"""Bounded LP proposals of positive-gap polymatroids for bad visibility sets.

Same rows as the visibility LP plus the normalization H(X_V)<=20, so the
optimum is a finite polymatroid with Delta>0. Floating only.
Usage: python3 script.py OUT.json "1,2,3,4,8,9" ...
"""
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('vis',ROOT/'frontier-20261028-visibility-set-stable-lp.py');vis=module_from_spec(spec);spec.loader.exec_module(vis)
highspy=vis.highspy;N=vis.N;TRI=vis.TRI;P=vis.P;S=vis.S;V=vis.V;FULL=vis.FULL;mask=vis.mask;move=vis.move

def solve(W,group):
    canon={m:min(move(m,p) for p in group) for m in range(1,FULL+1)}
    reps=sorted(set(canon.values()));index={r:i for i,r in enumerate(reps)};n=len(reps)
    rows=[];cols=[];data=[];lo=[];hi=[];seen=set();inf=highspy.kHighsInf
    def row(terms,l,h):
        clean={}
        for m,c in terms:
            if m:k=index[canon[m]];clean[k]=clean.get(k,0)+c
        key=(tuple(sorted((k,c) for k,c in clean.items() if c)),l,h)
        if not key[0] or key in seen:return
        seen.add(key);r=len(lo)
        for k,c in key[0]:rows.append(r);cols.append(k);data.append(c)
        lo.append(l);hi.append(h)
    for i in range(11):row([(FULL,1),(FULL^(1<<i),-1)],0,inf)
    for i,j in combinations(range(11),2):
        a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
        while True:
            row([(k|a,1),(k|b,1),(k|a|b,-1),(k,-1)],0,inf)
            if not k:break
            k=(k-1)&rest
    for v in range(1,11):
        nm=mask(N[v]);row([(nm|1<<(v-1),1),(nm,-1)],0,0)
        L=mask({u for t in TRI if v in t for u in t if u!=v});row([(L|S|1<<(v-1),1),(L|S,-1)],0,0)
        if v in W:row([(nm|S,1),(nm,-1)],0,0)
    row([(V|S,1),(V,-1)],0,0);row([(V,1)],-inf,20)
    counts=np.bincount(np.array(cols,dtype=np.int32),minlength=n);starts=np.zeros(n+1,dtype=np.int32);starts[1:]=np.cumsum(counts,dtype=np.int32)
    cursor=starts[:-1].copy();idx=np.empty(len(data),dtype=np.int32);val=np.empty(len(data))
    for c,r,d in zip(cols,rows,data):k=cursor[c];idx[k]=r;val[k]=d;cursor[c]+=1
    obj=np.zeros(n);obj[index[canon[V]]]=1
    for i in range(10):obj[index[canon[1<<i]]]-=2/3
    lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(lo);lp.col_cost_=obj
    lp.col_lower_=np.full(n,-inf);lp.col_upper_=np.full(n,inf);lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi)
    lp.sense_=highspy.ObjSense.kMaximize;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=starts;lp.a_matrix_.index_=idx;lp.a_matrix_.value_=val
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',45.0);h.passModel(lp);h.run()
    status=h.modelStatusToString(h.getModelStatus());out={'W':sorted(W),'group':group,'status_float_unverified':status,'objective_float_unverified':float(h.getInfo().objective_function_value),'orbit_representatives':reps}
    if status=='Optimal':out['primal']=[float(x) for x in h.getSolution().col_value]
    return out

def main():
    out=ROOT/sys.argv[1];cases=[]
    for text in sys.argv[2:]:
        W={int(x) for x in text.split(',')};stab=[p for p in P if {p[v-1] for v in W}==W]
        r=solve(W,stab);cases.append(r);print(json.dumps({k:v for k,v in r.items() if k in ('W','status_float_unverified','objective_float_unverified')}),flush=True)
    with out.open('x',encoding='utf-8') as f:json.dump({'cases':cases,'limits':'Floating primal proposals; exact rational polymatroid check required.'},f,indent=2);f.write('\n')


if __name__=='__main__':main()
