#!/usr/bin/env python3
"""Screen general one-step copy structures (copy X_S over X_T) at the FLOATING optimum h1 of the
symmetric publisher LP plus conditional DFZ cuts (screening only: the base is a float profile, so
Infeasible statuses are leads for adding a branch, not separators).

Usage: python3 script.py OUT.jsonl SIZE BUDGET_SECONDS [START] [POINT.json POINT_SHA]
SIZE=|S| in {1,2}. Every (S,T) with S,T disjoint, S of the given size and T
nonempty is reduced modulo the 8 graph automorphisms. For each representative
the copy LP (10+|S| variables, full elemental Shannon, copy marginals
h(Q'U)=h(QU) for nonempty Q<=S and U<=T, and I(S';V\\T|T)=0) is solved with
the original coordinates fixed to h*. Floating feasibility is exploratory. An
infeasible case is promoted only after an exact rational Farkas combination
(z3, exact arithmetic) cancels every auxiliary coordinate and evaluates
strictly negative on h*.
"""
from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations,product
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
from z3 import Real,Solver,Sum,sat
INPUT=ROOT/sys.argv[5] if len(sys.argv)>5 else ROOT/'frontier-20261029-dfz-cutting-plane-gurpinar-sym-result.json'
EXPECTED=sys.argv[6] if len(sys.argv)>6 else '5a544c2bf5816b1e7aa998d045f2caa34edec81c4c770bfd396b531c6f95527c'
BASE='abcdefghij';FULL=1023
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),
   6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
GENS=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
SOLVE_S=12.0;Z3_MS=30000


def group():
    edges={frozenset((u-1,v-1)) for u,ns in N.items() for v in ns}
    for p in GENS:
        if {frozenset(p[i] for i in e) for e in edges}!=edges:raise ValueError('AUTOMORPHISM')
    ident=tuple(range(10));seen={ident};queue=deque([ident])
    while queue:
        p=queue.popleft()
        for g in GENS:
            q=tuple(g[p[i]] for i in range(10))
            if q not in seen:seen.add(q);queue.append(q)
    if len(seen)!=8:raise ValueError('GROUP')
    return sorted(seen)


def load_base():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    doc=json.loads(raw)
    if 'final_original_profile_float' in doc:
        vals=doc['final_original_profile_float']
        if len(vals)!=1023:raise ValueError('BASE_COUNT')
        base={m:Fraction(vals[m-1]) for m in range(1,1024)}
    else:
        cols=doc['final_columns_float'];base={m:Fraction(cols[repr(('o',m))]) for m in range(1,1024)}
    base[0]=Fraction(0);return base


def shannon_rows(base,k):
    n=10+k;allm=(1<<n)-1;rows=[]
    def add(terms,meta):
        full={}
        for m,c in terms:
            if m:full[m]=full.get(m,0)+c
        full={m:c for m,c in full.items() if c}
        if all(m<1024 for m in full):return
        rows.append((full,False,meta))
    for i in range(n):add(((allm,1),(allm^(1<<i),-1)),('mono',i))
    for i,j in combinations(range(n),2):
        rest=allm^(1<<i)^(1<<j);z=rest
        while True:
            if i>=10 or j>=10 or z>=1024:
                add(((z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)),('cmi',i,j,z))
            if not z:break
            z=(z-1)&rest
    return rows


def copy_rows(base,S,T):
    k=len(S);Tm=sum(1<<t for t in T);rows=[]
    for choice in range(1,1<<k):
        old=sum(1<<S[a] for a in range(k) if choice>>a&1);new=sum(1<<(10+a) for a in range(k) if choice>>a&1)
        U=Tm
        while True:
            rows.append(({U|new:1,U|old:-1},True,('copy',choice,U)))
            if not U:break
            U=(U-1)&Tm
    cp=sum(1<<(10+a) for a in range(k))
    full={Tm|cp:1,FULL|cp:-1,FULL:1}
    if Tm:full[Tm]=-1
    rows.append((full,True,('independence',)))
    return rows


def solve(rows,k,base):
    ncol=(1<<(10+k))-1024;starts=[];ids=[];vals=[];lo=[];hi=[]
    rhss=[]
    for full,eq,meta in rows:
        starts.append(len(ids));rhs=-sum((Fraction(c)*base[m] for m,c in full.items() if m<1024),Fraction());rhss.append(rhs)
        for m,c in full.items():
            if m>=1024:ids.append(m-1024);vals.append(float(c))
        r=float(rhs);lo.append(r);hi.append(r if eq else highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_=ncol;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(ncol);lp.col_lower_=np.full(ncol,-highspy.kHighsInf);lp.col_upper_=np.full(ncol,highspy.kHighsInf)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float)
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',SOLVE_S)
    h.passModel(lp);t=time.monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    out={'status_float_unverified':status,'solve_s':round(time.monotonic()-t,3),'rows':len(rows)}
    if status!='Infeasible':return out
    state,exists,ray=h.getDualRay();out['dual_ray_exists']=bool(exists)
    if not exists:return out
    active=[i for i,x in enumerate(ray) if abs(float(x))>1e-9];out['ray_rows']=len(active)
    zs=Solver();zs.set(timeout=Z3_MS);y=[Real(f'y{a}') for a in range(len(active))]
    for a,i in enumerate(active):
        if not rows[i][1]:zs.add(y[a]>=0)
    cols={}
    for a,i in enumerate(active):
        for m,c in rows[i][0].items():
            if m>=1024:cols.setdefault(m,[]).append((a,c))
    for m,lst in cols.items():zs.add(Sum([y[a]*c for a,c in lst])==0)
    zs.add(Sum([y[a]*str(rhss[i]) for a,i in enumerate(active)])>=1)
    st=zs.check();out['exact_status']=str(st)
    if st!=sat:return out
    model=zs.model();w=[Fraction(model.eval(v,model_completion=True).as_fraction()) for v in y]
    acc={};sel=[]
    for a,i in enumerate(active):
        if not w[a]:continue
        full,eq,meta=rows[i]
        if not eq and w[a]<0:raise ValueError('SIGN')
        for m,c in full.items():acc[m]=acc.get(m,Fraction())+w[a]*c
        sel.append({'weight':str(w[a]),'equality':eq,'meta':list(meta),'terms':[[m,c] for m,c in sorted(full.items())]})
    acc={m:c for m,c in acc.items() if c}
    if any(m>=1024 for m in acc):raise ValueError('UNCANCELLED')
    value=sum((base[m]*c for m,c in acc.items()),Fraction())
    if value>=0:raise ValueError(('NONNEGATIVE',str(value)))
    out['exact_separator']={'rows':sel,'base_coefficients':[[m,str(c)] for m,c in sorted(acc.items())],'base_value':str(value)}
    return out


def representatives(G,k):
    seen=set();reps=[]
    for S in combinations(range(10),k):
        rest=[v for v in range(10) if v not in S]
        for bits in range(1,1<<len(rest)):
            T=tuple(rest[a] for a in range(len(rest)) if bits>>a&1)
            key=min((tuple(sorted(g[s] for s in S)),tuple(sorted(g[t] for t in T))) for g in G)
            if key in seen:continue
            seen.add(key);reps.append(key)
    return reps


def main():
    out=ROOT/sys.argv[1];k=int(sys.argv[2]);budget=float(sys.argv[3]);start=int(sys.argv[4]) if len(sys.argv)>4 else 0
    t0=time.monotonic();base=load_base();G=group();reps=representatives(G,k);sh=shannon_rows(base,k)
    print('representatives',len(reps),'shannon rows',len(sh),flush=True)
    with open(out,'x',encoding='utf-8') as f:
        f.write(json.dumps({'header':True,'input_sha256':EXPECTED,'size':k,'representatives':len(reps),'start':start,'shannon_rows':len(sh)})+'\n')
        for idx in range(start,len(reps)):
            if time.monotonic()-t0>budget:break
            S,T=reps[idx];r=solve(sh+copy_rows(base,S,T),k,base)
            r.update({'index':idx,'S_one_based':[s+1 for s in S],'T_one_based':[t+1 for t in T]})
            f.write(json.dumps(r)+'\n');f.flush()
            if r['status_float_unverified']!='Optimal':print(idx,r['S_one_based'],r['T_one_based'],r['status_float_unverified'],r.get('exact_status'),flush=True)
            if 'exact_separator' in r:print('EXACT_SEPARATOR',idx,r['S_one_based'],r['T_one_based'],r['exact_separator']['base_value'],flush=True)
        f.write(json.dumps({'footer':True,'elapsed_s':time.monotonic()-t0})+'\n')


if __name__=='__main__':main()
