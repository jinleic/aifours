#!/usr/bin/env python3
"""Shannon LP for R-minus with edge 3--4 deleted: max Delta (proposal only)."""
from itertools import combinations
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-edge-deleted-lp-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
V=(1<<10)-1

def main():
    E={tuple(sorted((u,v))) for u in N for v in N[u]};covered={tuple(sorted(e)) for t in TRI for e in combinations(t,2)}
    uncovered=sorted(E-covered)
    M={v:tuple(u for u in N[v] if tuple(sorted((u,v))) in covered) for v in N}
    inf=highspy.kHighsInf;rows=[];cols=[];data=[];lo=[];hi=[];names=[]
    def row(terms,l,h,name):
        r=len(lo);clean={}
        for m,c in terms:
            if m:clean[m]=clean.get(m,0)+c
        for m,c in clean.items():
            if c:rows.append(r);cols.append(m-1);data.append(c)
        lo.append(l);hi.append(h);names.append(name)
    for i in range(10):row([(V,1),(V^(1<<i),-1)],0,inf,('mono',i))
    for i,j in combinations(range(10),2):
        a,b=1<<i,1<<j;rest=V^a^b;k=rest
        while True:
            row([(k|a,1),(k|b,1),(k|a|b,-1),(k,-1)],0,inf,('cmi',i,j,k))
            if not k:break
            k=(k-1)&rest
    for v in N:
        nm=sum(1<<(u-1) for u in M[v]);row([(nm|1<<(v-1),1),(nm,-1)],0,0,('triangle-graph-fd',v))
    n=V;counts=np.bincount(np.array(cols,dtype=np.int32),minlength=n);starts=np.zeros(n+1,dtype=np.int32);starts[1:]=np.cumsum(counts,dtype=np.int32)
    cursor=starts[:-1].copy();idx=np.empty(len(data),dtype=np.int32);val=np.empty(len(data))
    for c,r,d in zip(cols,rows,data):k=cursor[c];idx[k]=r;val[k]=d;cursor[c]+=1
    obj=np.zeros(n);obj[V-1]=1
    for i in range(10):obj[(1<<i)-1]-=2/3
    lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(lo);lp.col_cost_=obj;lp.col_lower_=np.full(n,-inf);lp.col_upper_=np.full(n,inf)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.sense_=highspy.ObjSense.kMaximize
    lp.a_matrix_.format_=highspy.MatrixFormat.kColwise;lp.a_matrix_.start_=starts;lp.a_matrix_.index_=idx;lp.a_matrix_.value_=val
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',60.);h.passModel(lp);h.run()
    st=h.modelStatusToString(h.getModelStatus());out={'uncovered_edges':uncovered,'status_float_unverified':st,'objective_float_unverified':float(h.getInfo().objective_function_value)}
    if st=='Optimal':out['dual_support']=[{'name':names[i],'float':float(x)} for i,x in enumerate(h.getSolution().row_dual) if abs(x)>1e-9]
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='dual_support'}))


if __name__=='__main__':main()
