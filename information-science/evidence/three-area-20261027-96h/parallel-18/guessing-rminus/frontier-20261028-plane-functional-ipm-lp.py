#!/usr/bin/env python3
"""Mixed-block functional LP for residual binary syndrome planes (proposals).

Coloring: each selected factor's parity is one of the three nonzero
functionals of the two-bit syndrome S=(A,B): type 0=A, 1=B, 2=A+B.
Branches: 0 none, 1 S, 2..4 functionals. Rows: per-branch Shannon,
functional determined by Y_V, S gate (fixed parities), functional gates
Delta(Y|l)<=0 (imports the two-syndrome theorem on each fiber), graph FDs,
functional/state visibility at neighbourhoods, functional from its selected
triangles, J-local component FDs given S, and functional relations
(data processing, refined CMI, pair determination of S).
Usage: python3 script.py OUT.json BUDGET "colors" ...  where colors is a
10-character string over {-,0,1,2}. Floating proposals only.
"""
from itertools import combinations,permutations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
V=(1<<10)-1;S=1<<10;FULL=(1<<11)-1
LOOK={tuple(sorted(t)):i for i,t in enumerate(TRI)}
FP=[tuple(LOOK[tuple(sorted(p[v-1] for v in t))] for t in TRI) for p in P]
def mask(vs):return sum(1<<(v-1) for v in vs)
def move(m,p):return sum(1<<(p[i]-1) for i in range(10) if m>>i&1)

def actions(col):
    out=[]
    for p,f in zip(P,FP):
        for perm in permutations(range(3)):
            new=[None]*10
            for t in range(10):new[f[t]]=None if col[t] is None else perm[col[t]]
            if new==list(col):out.append((p,perm))
    return out

def solve(col,limit):
    acts=actions(col)
    def tr(a,b,p,cp):return (move(a,p),2+cp[b-2] if b>=2 else b)
    def canon(a,b):return min(tr(a,b,p,cp) for p,cp in acts)
    keys=sorted({canon(a,b) for a in range(V+1) for b in range(5) if a or b});index={k:i for i,k in enumerate(keys)};n=len(keys)
    rows=[];cols=[];data=[];lo=[];hi=[];names=[];seen=set();inf=highspy.kHighsInf
    def row(terms,l,h,name):
        clean={}
        for a,b,c in terms:
            if a or b:x=index[canon(a,b)];clean[x]=clean.get(x,0)+c
        key=(tuple(sorted((i,c) for i,c in clean.items() if c)),l,h)
        if not key[0] or key in seen:return
        seen.add(key);r=len(lo)
        for k,c in key[0]:rows.append(r);cols.append(k);data.append(c)
        lo.append(l);hi.append(h);names.append(name)
    def H(m,b):return (m&V,b if m&S else 0)
    for br in range(1,5):
        for i in range(11):row([(*H(FULL,br),1),(*H(FULL^(1<<i),br),-1)],0,inf,('mono',br,i))
        for i,j in combinations(range(11),2):
            a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
            while True:
                row([(*H(k|a,br),1),(*H(k|b,br),1),(*H(k|a|b,br),-1),(*H(k,br),-1)],0,inf,('cmi',br,i,j,k))
                if not k:break
                k=(k-1)&rest
        row([(V,br,1),(V,0,-1)],0,0,('aux-determined',br))
        row([(V,0,3),(0,br,17)]+[(1<<i,br,-2) for i in range(10)],-inf,0,('gate',br))
    for v in range(1,11):
        nm=mask(N[v]);row([(nm|1<<(v-1),0,1),(nm,0,-1)],0,0,('graph-fd',v))
        types={col[t] for t,T in enumerate(TRI) if v in T and col[t] is not None}
        for c in types:row([(nm,2+c,1),(nm,0,-1)],0,0,('functional-neighborhood',v,c))
        if len(types)>=2:row([(nm,1,1),(nm,0,-1)],0,0,('state-neighborhood',v))
        L=mask({u for t,T in enumerate(TRI) if col[t] is not None and v in T for u in T if u!=v})
        row([(L|1<<(v-1),1,1),(L,1,-1)],0,0,('mixed-local-fd',v))
    for t,T in enumerate(TRI):
        if col[t] is not None:m=mask(T);row([(m,2+col[t],1),(m,0,-1)],0,0,('functional-triangle',t+1))
    for a in range(V+1):
        for j in (2,3,4):
            row([(a,j,1),(a,1,-1)],-inf,0,('data-processing',a,j))
        for j,k in combinations((2,3,4),2):row([(a,1,1),(a,j,-1),(a,k,-1),(a,0,1)],-inf,0,('pair-determines-state',a,j,k))
    cnt=np.bincount(np.array(cols,dtype=np.int32),minlength=n);st=np.zeros(n+1,dtype=np.int32);st[1:]=np.cumsum(cnt,dtype=np.int32)
    cur=st[:-1].copy();idx=np.empty(len(data),dtype=np.int32);val=np.empty(len(data))
    for c,r,d in zip(cols,rows,data):k=cur[c];idx[k]=r;val[k]=d;cur[c]+=1
    obj=np.zeros(n);obj[index[canon(V,0)]]=1
    for i in range(10):obj[index[canon(1<<i,0)]]-=2/3
    lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(lo);lp.col_cost_=obj;lp.col_lower_=np.full(n,-inf);lp.col_upper_=np.full(n,inf)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.sense_=highspy.ObjSense.kMaximize
    lp.a_matrix_.format_=highspy.MatrixFormat.kColwise;lp.a_matrix_.start_=st;lp.a_matrix_.index_=idx;lp.a_matrix_.value_=val
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit)
    h.setOptionValue('dual_feasibility_tolerance',1e-9);h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on')
    h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus())
    out={'colors':list(col),'actions':[[list(p),list(cp)] for p,cp in acts],'status':status,'objective':float(h.getInfo().objective_function_value),'variables':n,'rows':len(lo)}
    if status=='Optimal':
        out['keys']=keys;out['dual_support']=[{'name':names[i],'float':float(x)} for i,x in enumerate(h.getSolution().row_dual) if abs(x)>1e-9]
    return out

def main():
    out=ROOT/sys.argv[1];budget=float(sys.argv[2]);start=monotonic();res=[]
    for text in sys.argv[3:]:
        if monotonic()-start>budget:break
        col=tuple(None if ch=='-' else int(ch) for ch in text)
        r=solve(col,60.0);res.append(r);print(json.dumps({k:v for k,v in r.items() if k in ('colors','status','objective','variables','rows')}),flush=True)
    with out.open('x',encoding='utf-8') as f:json.dump({'cases':res,'limits':'Floating proposals; functional gates import the two-syndrome theorem.'},f);f.write('\n')


if __name__=='__main__':main()
