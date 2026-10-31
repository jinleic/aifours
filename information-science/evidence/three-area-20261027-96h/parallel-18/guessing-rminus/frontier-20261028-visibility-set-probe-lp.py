#!/usr/bin/env python3
"""Numerical proposals: which syndrome-visibility vertex sets force Delta<=0.

Full ten-factor q8 model with S = full syndrome vector (any support).
Rows: 11-variable Shannon, original graph FDs, full local component FDs
H(X_v|X_L(v),S)=0, H(S|X_V)=0, and H(S|X_N(v))=0 for v in W only.
Outputs are floating proposals; exact certificates are checked separately.
"""
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-visibility-set-probe-lp-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
S=1<<10;V=S-1;FULL=(1<<11)-1

def mask(vs):return sum(1<<(v-1) for v in vs)
def move(m,p):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m>>i&1)

def solve(W,group,limit=20.0):
    canon={m:min(move(m,p) for p in group) for m in range(1,FULL+1)}
    reps=sorted(set(canon.values()));index={r:i for i,r in enumerate(reps)};n=len(reps)
    rows=[];cols=[];data=[];lo=[];hi=[];names=[];seen=set();inf=highspy.kHighsInf
    def row(terms,l,h,name):
        clean={}
        for m,c in terms:
            if m:k=index[canon[m]];clean[k]=clean.get(k,0)+c
        key=(tuple(sorted((k,c) for k,c in clean.items() if c)),l,h)
        if not key[0] or key in seen:return
        seen.add(key);r=len(lo)
        for k,c in key[0]:rows.append(r);cols.append(k);data.append(c)
        lo.append(l);hi.append(h);names.append(name)
    for i in range(11):row([(FULL,1),(FULL^(1<<i),-1)],0,inf,('mono',i))
    for i,j in combinations(range(11),2):
        a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
        while True:
            row([(k|a,1),(k|b,1),(k|a|b,-1),(k,-1)],0,inf,('cmi',i,j,k))
            if not k:break
            k=(k-1)&rest
    for v in range(1,11):
        nm=mask(N[v]);row([(nm|1<<(v-1),1),(nm,-1)],0,0,('fd',v))
        L=mask({u for t in TRI if v in t for u in t if u!=v})
        row([(L|S|1<<(v-1),1),(L|S,-1)],0,0,('local-fd',v))
        if v in W:row([(nm|S,1),(nm,-1)],0,0,('syndrome-neighborhood',v))
    row([(V|S,1),(V,-1)],0,0,('syndrome-global-fd',))
    counts=np.bincount(np.array(cols,dtype=np.int32),minlength=n);starts=np.zeros(n+1,dtype=np.int32);starts[1:]=np.cumsum(counts,dtype=np.int32)
    cursor=starts[:-1].copy();idx=np.empty(len(data),dtype=np.int32);val=np.empty(len(data))
    for c,r,d in zip(cols,rows,data):k=cursor[c];idx[k]=r;val[k]=d;cursor[c]+=1
    obj=np.zeros(n);obj[index[canon[V]]]=1
    for i in range(10):obj[index[canon[1<<i]]]-=2/3
    lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(lo);lp.col_cost_=obj
    lp.col_lower_=np.full(n,-inf);lp.col_upper_=np.full(n,inf);lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi)
    lp.sense_=highspy.ObjSense.kMaximize;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=starts;lp.a_matrix_.index_=idx;lp.a_matrix_.value_=val
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit)
    h.setOptionValue('dual_feasibility_tolerance',1e-9);h.setOptionValue('primal_feasibility_tolerance',1e-9)
    h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus())
    out={'W':sorted(W),'group_size':len(group),'status_float_unverified':status,'objective_float_unverified':float(h.getInfo().objective_function_value),'orbit_representatives':reps}
    if status=='Optimal':
        sol=h.getSolution();out['dual_support']=[{'name':names[i],'float':float(x)} for i,x in enumerate(sol.row_dual) if abs(x)>1e-9]
    return out


def main():
    start=monotonic();cases=[]
    tests=[(7,),(4,),(1,4),(3,9),(6,7),(1,8),(2,5,6,7,9,10),(2,3,4,5,6,7,8,9,10),(1,2,4,5,6,7,8,9,10),(1,2,3,5,6,7,8,9,10)]
    for W in tests:
        stab=[p for p in P if {p[v-1] for v in W}==set(W)]
        r=solve(set(W),stab,limit=12.0);cases.append(r);print(json.dumps({k:v for k,v in r.items() if k not in ('dual_support','orbit_representatives')}),flush=True)
    out={'cases':cases,'elapsed_seconds':monotonic()-start,'limits':'Floating proposals only; exact rational certificates and written row validity are separate.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')


if __name__=='__main__':main()
