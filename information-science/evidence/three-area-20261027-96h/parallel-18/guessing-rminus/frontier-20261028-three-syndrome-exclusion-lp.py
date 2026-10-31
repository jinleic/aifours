#!/usr/bin/env python3
"""Numerical entropy outer relaxation from all two-state syndrome fibers."""
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-three-syndrome-exclusion-lp-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),
   (8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
V=(1<<10)-1;S=1<<10;FULL=(1<<11)-1

def mask(vertices):return sum(1<<(v-1) for v in vertices)
def move(m,p):return sum(1<<(p[i]-1) for i in range(10) if m&(1<<i))


def main():
    started=monotonic();inf=highspy.kHighsInf
    canon={m:min(move(m,p) for p in P) for m in range(V+1)}
    base=sorted(set(canon.values()));keys=[(a,b) for b in range(3) for a in base if a or b];index={k:i for i,k in enumerate(keys)}
    n=len(keys);rows=[];cols=[];data=[];lower=[];upper=[];names=[];seen=set()
    def row(terms,lo,hi,name):
        clean={}
        for a,b,c in terms:
            if a or b:
                x=index[canon[a],b];clean[x]=clean.get(x,0)+c
        key=(tuple(sorted((i,c) for i,c in clean.items() if c)),lo,hi)
        if not key[0] or key in seen:return
        seen.add(key);r=len(lower)
        for col,c in key[0]:rows.append(r);cols.append(col);data.append(c)
        lower.append(lo);upper.append(hi);names.append(name)
    def H(m,b):return (m&V,b if m&S else 0)
    for branch in range(1,3):
        for i in range(11):
            a=1<<i;x,y=H(FULL,branch),H(FULL^a,branch)
            row([(*x,1),(*y,-1)],0,inf,('mono',branch,i))
        for i,j in combinations(range(11),2):
            a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
            while True:
                x,y,z,w=(H(k|a,branch),H(k|b,branch),H(k|a|b,branch),H(k,branch))
                row([(*x,1),(*y,1),(*z,-1),(*w,-1)],0,inf,('cmi',branch,i,j,k))
                if not k:break
                k=(k-1)&rest
        row([(V,branch,1),(V,0,-1)],0,0,('aux-determined',branch))
        row([(V,0,3),(0,branch,17)]+[(1<<i,branch,-2) for i in range(10)],-inf,0,('conditional-gap-gate',branch))
    for v in range(1,11):
        a=1<<(v-1);nm=mask(N[v]);row([(nm|a,0,1),(nm,0,-1)],0,0,('graph-fd',v))
    # Branch 2 is the arithmetic mean of the three indicator entropy vectors.
    # One-hot exclusion gives 9 H(Z|A) >= 5 H(S|A).
    for a in range(V+1):
        row([(a,2,1),(a,1,-1)],-inf,0,('indicator-data-processing',a))
        row([(a,1,5),(a,2,-9),(a,0,4)],-inf,0,('onehot-exclusion-5to3',a))
    row([(0,1,1)],-inf,1,('normalization',))
    counts=np.bincount(np.array(cols,dtype=np.int32),minlength=n);starts=np.zeros(n+1,dtype=np.int32);starts[1:]=np.cumsum(counts,dtype=np.int32)
    cursor=starts[:-1].copy();indices=np.empty(len(data),dtype=np.int32);values=np.empty(len(data),dtype=float)
    for col,ri,c in zip(cols,rows,data):
        pos=cursor[col];indices[pos]=ri;values[pos]=c;cursor[col]+=1
    objective=np.zeros(n);objective[index[canon[V],0]]=1
    for i in range(10):objective[index[canon[1<<i],0]]-=2/3
    lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(lower);lp.col_cost_=objective
    lp.col_lower_=np.full(n,-inf);lp.col_upper_=np.full(n,inf);lp.row_lower_=np.array(lower);lp.row_upper_=np.array(upper)
    lp.sense_=highspy.ObjSense.kMaximize;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=starts;lp.a_matrix_.index_=indices;lp.a_matrix_.value_=values
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',30.)
    solver.passModel(lp);solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    out={'status_float_unverified':status,'objective_float_unverified':float(solver.getInfo().objective_function_value),'variables':n,'rows':len(lower),'keys':keys,'elapsed_seconds':monotonic()-started,
         'limits':'Numerical averaged-indicator outer relaxation only, conditional on the unreviewed two-syndrome theorem. No entropy law, no guessing gain or no-go and no exact optimality claim.'}
    if status=='Optimal':
        sol=solver.getSolution();out['primal']=[float(x) for x in sol.col_value];out['dual_support']=[{'row':names[i],'float':float(x)} for i,x in enumerate(sol.row_dual) if abs(x)>1e-8]
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('keys','primal','dual_support')},indent=2))


if __name__=='__main__':main()
