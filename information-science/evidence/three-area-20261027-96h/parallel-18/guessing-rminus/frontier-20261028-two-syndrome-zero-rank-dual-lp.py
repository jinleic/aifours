#!/usr/bin/env python3
"""Find small-support numerical duals for the conditional binary rank LP."""
from fractions import Fraction
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-two-syndrome-zero-rank-dual-lp-result.json'
SRC=ROOT/'frontier-20261028-two-syndrome-zero-rank-lp-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
S=1024;V=1023;FULL=2047

def mask(vs):return sum(1<<(v-1) for v in vs)
def row(meta,case):
    kind=meta[0]
    if kind=='mono':a=1<<meta[1];return [(FULL,1),(FULL^a,-1)],'nonneg',0
    if kind=='cmi':
        _,i,j,K=meta;a,b=1<<i,1<<j;return [(K|a,1),(K|b,1),(K|a|b,-1),(K,-1)],'nonneg',0
    if kind=='fd':v=meta[1];a=1<<(v-1);m=mask(N[v]);return [(m|a,1),(m,-1)],'zero',0
    if kind=='syndrome-neighborhood':m=mask(N[meta[1]]);return [(m|S,1),(m,-1)],'zero',0
    if kind=='syndrome-triangle':m=mask(TRI[meta[1]-1]);return [(m|S,1),(m,-1)],'zero',0
    if kind=='syndrome-global-fd':return [(V|S,1),(V,-1)],'zero',0
    if kind=='global-syndrome-gate':return [(V,3),(S,17)]+[(S|1<<i,-2) for i in range(10)],'upper',0
    if kind=='conditional-zero-rank-fd':
        A,i=meta[1:];return [(A|S|1<<(i-1),1),(A|S,-1)],'zero',0
    if kind in ('conditional-rank-increment','conditional-projection-rank'):
        A=meta[1];rank=lambda x:sum(min((x&mask(TRI[t-1])).bit_count(),2) for t in case)
        if kind=='conditional-projection-rank':return [(A|S,1),(S,-1)],'upper',rank(A)
        bit=1<<(meta[2]-1);return [(A|S|bit,1),(A|S,-1)],'upper',rank(A|bit)-rank(A)
    raise ValueError(meta)


def main():
    results=[];start=monotonic();doc=json.loads(SRC.read_bytes())
    for source in doc['cases']:
        case=source['factors'];tri={tuple(sorted(t)):i+1 for i,t in enumerate(TRI)}
        G=[p for p in P if {tri[tuple(sorted(p[v-1] for v in TRI[t-1]))] for t in case}==set(case)]
        move=lambda m,p:(m&S)|sum((1<<(p[i]-1)) for i in range(10) if m&(1<<i))
        reps=source['orbit_representatives'];ind={r:i for i,r in enumerate(reps)}
        orb=lambda m:ind[min(move(m,p) for p in G)]
        filtered=[]
        for x in source['dual_support']:
            terms,kind,rhs=row(x['name'],case)
            if rhs==0 and (kind!='nonneg' or x['float'] < -1e-8):filtered.append((x['name'],terms,kind))
        n=len(filtered);rows=[];cols=[];vals=[]
        for j,(_,terms,kind) in enumerate(filtered):
            acc={}
            for m,z in terms:
                if m:acc[orb(m)]=acc.get(orb(m),0)+z
            for i,z in acc.items():
                if z:rows.append(i);cols.append(j);vals.append(z)
        objective=np.array([0.0 if kind=='zero' else (-1.0 if kind=='nonneg' else 1.0) for _,_,kind in filtered])
        lo=np.array([0. if kind=='upper' else (-highspy.kHighsInf) for _,_,kind in filtered])
        hi=np.array([0. if kind=='nonneg' else highspy.kHighsInf for _,_,kind in filtered])
        rhs=np.zeros(len(reps));rhs[orb(V)]=1
        for i in range(10):rhs[orb(1<<i)]-=2/3
        counts=np.bincount(np.array(cols,dtype=np.int32),minlength=n);starts=np.zeros(n+1,dtype=np.int32);starts[1:]=np.cumsum(counts,dtype=np.int32)
        cursor=starts[:-1].copy();index=np.empty(len(vals),dtype=np.int32);values=np.empty(len(vals))
        for j,i,z in zip(cols,rows,vals):k=cursor[j];index[k]=i;values[k]=z;cursor[j]+=1
        lp=highspy.HighsLp();lp.num_col_=n;lp.num_row_=len(reps);lp.col_cost_=objective;lp.col_lower_=lo;lp.col_upper_=hi
        lp.row_lower_=rhs;lp.row_upper_=rhs;lp.sense_=highspy.ObjSense.kMinimize;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_=starts;lp.a_matrix_.index_=index;lp.a_matrix_.value_=values
        h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',15.0);h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus())
        result={'factors':case,'status_float_unverified':status,'input_support':n,'objective_float_unverified':float(h.getInfo().objective_function_value)}
        if status=='Optimal':
            sol=h.getSolution();result['dual']=[{'row':filtered[i][0],'float':float(x)} for i,x in enumerate(sol.col_value) if abs(x)>1e-9]
        results.append(result);print(json.dumps({k:v for k,v in result.items() if k!='dual'}),flush=True)
    out={'cases':results,'elapsed_seconds':monotonic()-start,'limits':'Numerical dual proposals only; exact rational reconstruction, binary fiber validity and independent verification required.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print('wrote',OUT)


if __name__=='__main__':main()
