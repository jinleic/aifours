#!/usr/bin/env python3
"""Direct sparse dual certificate search for mixed-block functional classes.
Usage: python3 script.py OUT.jsonl CLASSES.json INDICES LIMIT_SECONDS
Reuses the v2 model's exact row construction, but does NOT optimize the primal
homogeneous cone. Instead solve sum(w_r*row_r)=3*Delta directly, with the
correct signs and an L1 objective (equality weights split positive/negative).
A basic positive-variable solution is proposed, then the old exact flint
identity/sign reconstruction accepts or rejects it. Independent certificate
checking is still mandatory. This is not a code-search or new entropy premise.
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

def build(col):
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
        if br==1:row([(V,0,3),(0,br,17)]+[(1<<i,br,-2) for i in range(10)],-inf,0,('gate',br))
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
    rr=[[] for _ in names]
    for r,c,value in zip(rows,cols,data):rr[r].append((c,value))
    target=np.zeros(n);target[index[canon(V,0)]]=3
    for i in range(10):target[index[canon(1<<i,0)]]-=2
    return keys,acts,names,rr,lo,hi,target

from importlib.util import spec_from_file_location,module_from_spec
from hashlib import sha256
spec=spec_from_file_location('oldbatch',ROOT/'frontier-20261028-plane-functional-batch.py');oldbatch=module_from_spec(spec);spec.loader.exec_module(oldbatch)

def direct_certificate(col,limit):
    keys,acts,names,rr,lo,hi,target=build(col);n=len(keys);starts=[];ids=[];values=[];which=[];inf=highspy.kHighsInf
    for r,items in enumerate(rr):
        signs=(-1,) if lo[r]==0 and hi[r]==inf else ((1,) if lo[r]==-inf and hi[r]==0 else (1,-1))
        for sign in signs:
            starts.append(len(ids));which.append((r,sign))
            for c,a in items:ids.append(c);values.append(sign*a)
    nv=len(which);lp=highspy.HighsLp();lp.num_col_=nv;lp.num_row_=n
    lp.col_cost_=np.ones(nv);lp.col_lower_=np.zeros(nv);lp.col_upper_=np.full(nv,inf)
    lp.row_lower_=target;lp.row_upper_=target;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit)
    h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on');h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9)
    h.passModel(lp);t=monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    report={'status_float':status,'dual_variables':nv,'coefficient_equations':n,'solve_s':monotonic()-t,'certificate':None}
    if status!='Optimal':return report
    weights={}
    for (r,sign),v in zip(which,h.getSolution().col_value):
        if v!=0:weights[r]=weights.get(r,0.)+sign*float(v)
    proposal={'colors':list(col),'actions':[[list(p),list(cp)] for p,cp in acts],'keys':keys,
      'dual_support':[{'name':names[r],'float':v} for r,v in weights.items() if v!=0]}
    cert,exact_status=oldbatch.exact(proposal)
    report.update({'exact_status':exact_status,'certificate':cert,'proposed_support_rows':len(proposal['dual_support']),'floating_L1_objective':h.getInfo().objective_function_value})
    return report

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes();classes=json.loads(raw)['colorings'];indices=[int(i) for i in sys.argv[3].split(',')];limit=float(sys.argv[4])
    with out.open('x') as f:
        for i in indices:
            text=classes[i];col=tuple(None if ch=='-' else int(ch) for ch in text);r=direct_certificate(col,limit)
            r.update({'index':i,'colors':text,'class_file_sha256':sha256(raw).hexdigest(),'status':('ok' if r.get('exact_status')=='ok' else r.get('exact_status',r['status_float']))})
            f.write(json.dumps(r)+'\n');f.flush();print(i,text,r['status'],r.get('proposed_support_rows'),r['solve_s'],flush=True)
if __name__=='__main__':main()
