#!/usr/bin/env python3
"""Bounded batch search: mixed-block visibility LPs for residual binary planes.

Residual planes: covering, >=5 varying factors, full-model visibility set
containing no certified generator. Mixed block: condition on fixed factors;
variables Y_1..Y_10 (selected components) and S (selected syndrome).
Rows: Shannon, graph FDs, J-local component FDs given S, H(S|Y_V)=0,
visibility H(S|Y_N(v))=0 for v in W, the conditional factor gate and
H(S)<=2 (valid for plane supports). Floating proposals only.
Usage: python3 script.py OUT.json [PRIOR.json ...]
"""
from itertools import combinations
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
GEN=[{6},{7},{2,5},{9,10},{1,2,10},{1,5,9},{5,8,9},{2,8,10}]
S=1<<10;V=S-1;FULL=(1<<11)-1
def mask(vs):return sum(1<<(v-1) for v in vs)
def move(m,p):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m>>i&1)
LOOK={tuple(sorted(t)):i for i,t in enumerate(TRI)}
FP=[tuple(LOOK[tuple(sorted(p[v-1] for v in t))] for t in TRI) for p in P]
def fimg(m,f):return sum(1<<f[i] for i in range(10) if m>>i&1)

def solve(J,W,limit):
    F=[t+1 for t in range(10) if J>>t&1]
    group=[p for p,f in zip(P,FP) if fimg(J,f)==J and {p[v-1] for v in W}==W]
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
        L=mask({u for t in F if v in TRI[t-1] for u in TRI[t-1] if u!=v})
        row([(L|S|1<<(v-1),1),(L|S,-1)],0,0,('mixed-local-fd',v))
        if v in W:row([(nm|S,1),(nm,-1)],0,0,('syndrome-neighborhood',v))
    row([(V|S,1),(V,-1)],0,0,('syndrome-global-fd',))
    row([(V,3),(S,17)]+[(S|(1<<i),-2) for i in range(10)],-inf,0,('conditional-factor-gate',))
    row([(S,1)],-inf,2,('plane-syndrome-cap',))
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
    h.setOptionValue('dual_simplex_cost_perturbation_multiplier',0.0);h.setOptionValue('simplex_strategy',4)
    h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus());obj=float(h.getInfo().objective_function_value)
    out={'J':J,'factors':F,'W':sorted(W),'group':group,'status':status,'objective':obj}
    if status=='Optimal':
        sol=h.getSolution();out['dual_support']=[{'name':names[i],'float':float(x)} for i,x in enumerate(sol.row_dual) if abs(x)>1e-9]
        out['orbit_representatives']=reps
    return out

def residual_classes():
    inc=[sum(1<<t for t,T in enumerate(TRI) if v in T) for v in range(1,11)];classes={}
    for a in range(1,1024):
        for b in range(a+1,1024):
            c=a^b
            if b>=c:continue
            J=a|b|c
            if bin(J).count('1')<5 or set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))!=set(N):continue
            W=frozenset(v+1 for v in range(10) if a&inc[v] and b&inc[v] and c&inc[v])
            if any(g<=W for g in GEN):continue
            key=min((fimg(J,f),tuple(sorted(p[v-1] for v in W))) for f,p in zip(FP,P))
            classes[key]=classes.get(key,0)+1
    return classes

def main():
    out=ROOT/sys.argv[1];prior=[json.loads((ROOT/x).read_text()) for x in sys.argv[2:]]
    records=[];good={};bad={}
    for doc in prior:
        for r in doc['records']:
            records.append(r);J=r['J']
            if r['status']=='good':good.setdefault(J,[]).append(frozenset(r['used']))
            if r['status']=='bad':bad.setdefault(J,[]).append(frozenset(r['W']))
    classes=residual_classes();tested={(r['J'],tuple(r['W'])) for r in records if r['status']!='unknown'}
    order=sorted(classes,key=lambda k:(k[0],-len(k[1]),-classes[k]));start=monotonic();full=[]
    for J,W in order:
        if monotonic()-start>90:break
        Wf=frozenset(W)
        if (J,W) in tested:continue
        if any(g<=Wf for g in good.get(J,[])) or any(Wf<=b for b in bad.get(J,[])):continue
        r=solve(J,Wf,25.0);rec={'J':J,'factors':r['factors'],'W':list(W),'planes':classes[(J,W)],'solver':r['status']}
        if r['status']=='Optimal' and abs(r['objective'])<1e-7:
            g=r['group'];used={p[x['name'][1]-1] for x in r['dual_support'] if x['name'][0]=='syndrome-neighborhood' for p in g}
            rec.update(status='good',used=sorted(used));good.setdefault(J,[]).append(frozenset(used));full.append(r)
        elif r['status'] in ('Unbounded',) or (r['status']=='Optimal' and r['objective']>1e-7):
            rec['status']='bad';bad.setdefault(J,[]).append(Wf)
        else:rec['status']='unknown'
        records.append(rec);tested.add((J,W));print(json.dumps(rec),flush=True)
    unresolved=sum(n for (J,W),n in classes.items() if not any(g<=frozenset(W) for g in good.get(J,[])))
    res={'records':records,'good_full_duals':full,'unresolved_planes':unresolved,'total_residual_planes':sum(classes.values()),'classes':len(classes),
         'elapsed_seconds':monotonic()-start,'limits':'Floating LP proposals; exact certificate reconstruction and independent checks required.'}
    with out.open('x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')
    print(json.dumps({'records':len(records),'unresolved_planes':unresolved,'total':res['total_residual_planes']}),flush=True)


if __name__=='__main__':main()
