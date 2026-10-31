#!/usr/bin/env python3
"""Numerically probe a binary-syndrome Shannon outer relaxation, never a proof."""
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy

N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
REPS=((1,2,5,6,8,9),(1,3,4,6,7,10),(2,3,4,6,7,10),(2,3,5,6,9,10))
S=1<<10;V=(1<<10)-1;FULL=(1<<11)-1
OUT=ROOT/'frontier-20261028-two-syndrome-increment-topFD-lp-result.json'
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))

def mask(vertices):return sum(1<<(v-1) for v in vertices)

def main():
    started=monotonic();records=[];inf=highspy.kHighsInf
    for case in REPS:
        tri_lookup={tuple(sorted(t)):i+1 for i,t in enumerate(TRI)}
        group=[]
        for p in P:
            fp=[tri_lookup[tuple(sorted(p[v-1] for v in tri))] for tri in TRI]
            if {fp[t-1] for t in case}==set(case):group.append(p)
        def move(m,p):return (m&S)|sum((1<<(p[i]-1)) for i in range(10) if m&(1<<i))
        canon={m:min(move(m,p) for p in group) for m in range(1,FULL+1)}
        reps=sorted(set(canon.values()));index={r:i for i,r in enumerate(reps)}
        orbit={m:index[c] for m,c in canon.items()};n=len(reps)
        rows=[];cols=[];data=[];lower=[];upper=[];names=[];seen=set()
        def row(terms,lo,hi,name):
            k=len(lower);clean={}
            for m,c in terms:
                if m:clean[orbit[m]]=clean.get(orbit[m],0)+c
            key=(tuple(sorted((m,c) for m,c in clean.items() if c)),lo,hi)
            if not key[0] or key in seen:return
            seen.add(key)
            for m,c in key[0]:rows.append(k);cols.append(m);data.append(c)
            lower.append(lo);upper.append(hi);names.append(name)
        for i in range(11):
            a=1<<i;row([(FULL,1),(FULL^a,-1)],0,inf,('mono',i))
        for i,j in combinations(range(11),2):
            a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
            while True:
                row([(k|a,1),(k|b,1),(k|a|b,-1),(k,-1)],0,inf,('cmi',i,j,k))
                if not k:break
                k=(k-1)&rest
        for v in range(1,11):
            nm=mask(N[v]);a=1<<(v-1)
            row([(nm|a,1),(nm,-1)],0,0,('fd',v))
            row([(nm|S,1),(nm,-1)],0,0,('syndrome-neighborhood',v))
        for t in case:
            m=mask(TRI[t-1]);row([(m|S,1),(m,-1)],0,0,('syndrome-triangle',t))
        row([(V,3),(S,17)]+[(S|(1<<i),-2) for i in range(10)],-inf,0,('global-syndrome-gate',))
        row([(V|S,1),(V,-1)],0,0,('syndrome-global-fd',))
        ranks=[sum(min((A&mask(TRI[t-1])).bit_count(),2) for t in case) for A in range(V+1)]
        for A in range(1,V+1):
            row([(A|S,1),(S,-1)],-inf,ranks[A],('conditional-projection-rank',A))
        for A in range(V+1):
            for i in range(10):
                a=1<<i
                if A&a:continue
                row([(A|a|S,1),(A|S,-1)],-inf,ranks[A|a]-ranks[A],('conditional-rank-increment',A,i+1))
        for i in range(10):row([(1<<i,1)],-inf,ranks[1<<i],('actual-singleton-cap',i+1))
        row([(S,1)],-inf,1,('binary-syndrome',))
        counts=np.bincount(np.array(cols,dtype=np.int32),minlength=n)
        starts=np.zeros(n+1,dtype=np.int32);starts[1:]=np.cumsum(counts,dtype=np.int32)
        cursor=starts[:-1].copy();indices=np.empty(len(data),dtype=np.int32);values=np.empty(len(data),dtype=float)
        for col,ri,coeff in zip(cols,rows,data):
            pos=cursor[col];indices[pos]=ri;values[pos]=coeff;cursor[col]+=1
        objective=np.zeros(n);objective[orbit[V]]=1
        for i in range(10):objective[orbit[1<<i]]-=2/3
        lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(lower)
        lp.col_cost_=objective;lp.col_lower_=np.full(n,-inf);lp.col_upper_=np.full(n,inf)
        lp.row_lower_=np.array(lower);lp.row_upper_=np.array(upper);lp.sense_=highspy.ObjSense.kMaximize
        lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_=starts;lp.a_matrix_.index_=indices;lp.a_matrix_.value_=values
        solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',20.0)
        solver.passModel(lp);solver.run();status=solver.modelStatusToString(solver.getModelStatus())
        result={'factors':case,'group_size':len(group),'entropy_orbits':n,'orbit_representatives':reps,'rows':len(lower),'status_float_unverified':status,'objective_float_unverified':float(solver.getInfo().objective_function_value)}
        if status=='Optimal':
            sol=solver.getSolution();result['dual_support']=[{'name':names[i],'float':float(x)} for i,x in enumerate(sol.row_dual) if abs(x)>1e-8]
            result['primal']=[float(x) for x in sol.col_value]
        records.append(result);print(json.dumps({k:v for k,v in result.items() if k not in ('primal','dual_support','orbit_representatives')}),flush=True)
    out={'cases':records,'elapsed_seconds':monotonic()-started,'limits':'The Shannon LP is orbit-reduced under the factor-set stabilizer; objective and all constraints are invariant. Floating-point proposals only; not an exact certificate or original entropy-law witness. Conditioned projection and incremental caps, graph and syndrome FDs and the pinned syndrome gate are an outer relaxation, not a complete model.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print('wrote',OUT,flush=True)


if __name__=='__main__':main()
