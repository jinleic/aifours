#!/usr/bin/env python3
"""Exact-dual proposals for one specified nonlinear four-syndrome pattern.
Usage: python3 script.py OUT.json INPUT.json INPUT_SHA PATTERN_INDEX LIMIT_SECONDS
All fifteen selector partitions are used. Rows: per-partition Shannon,
information-order/refinement and lattice CMI, actual minimal-local-state FDs,
triangle/neighborhood visibility, graph FDs and ONLY the full-state factor gate.
No affine-plane or two-syndrome Delta theorem is imported. Correctness of each
accepted identity still requires the separate raw-coordinate checker.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations,permutations,product
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'));import highspy as HS
sys.path.insert(0,str(ROOT/'frontier-20261028-flint'));import flint
from fractions import Fraction
INF=HS.kHighsInf;V=1023;AUX=1024;FULL=2047
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P4=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
LEMMA='frontier-20261029-fourstate-partition-model-lemma-v1.md'

def canonical(seq):
    labels={};out=[]
    for x in seq:
        if x not in labels:labels[x]=len(labels)
        out.append(labels[x])
    return tuple(out)
PART=sorted({canonical(x) for x in product(range(4),repeat=4)});PI={p:i for i,p in enumerate(PART)}
if len(PART)!=15:raise ValueError('BELL4')
BOT=PI[(0,0,0,0)];TOP=PI[(0,1,2,3)]
def join(p,q):return PI[canonical(tuple((PART[p][s],PART[q][s]) for s in range(4)))]
def meet(p,q):
    parents=list(range(4))
    def root(i):
        while parents[i]!=i:i=parents[i]
        return i
    for a in range(4):
        for b in range(a):
            if PART[p][a]==PART[p][b] or PART[q][a]==PART[q][b]:parents[root(a)]=root(b)
    return PI[canonical(tuple(root(i) for i in range(4)))]
def leq(p,q):return all(PART[q][a]!=PART[q][b] or PART[p][a]==PART[p][b] for a in range(4) for b in range(4))
JOIN=[[join(p,q) for q in range(15)] for p in range(15)];MEET=[[meet(p,q) for q in range(15)] for p in range(15)]
ORDER=[(p,q) for p in range(15) for q in range(15) if p!=q and leq(p,q)]
COVERS=[(p,q) for p,q in ORDER if not any(r not in (p,q) and leq(p,r) and leq(r,q) for r in range(15))]
INCOMP=[(p,q) for p,q in combinations(range(15),2) if not leq(p,q) and not leq(q,p)]
BINARY={0:BOT,**{w:PI[canonical((0,*(int(bool(w>>(s-1)&1)) for s in range(1,4))))] for w in range(1,8)}}
STATE_PERMS=list(permutations(range(4)));PMAPS=[tuple(PI[canonical(tuple(PART[p][perm[s]] for s in range(4)))] for p in range(15)) for perm in STATE_PERMS]
LOOK={tuple(sorted(T)):i for i,T in enumerate(TRI)}
FMAPS=[tuple(LOOK[tuple(sorted(p[v-1] for v in T))] for T in TRI) for p in P4]
VMAPS=[[sum(1<<(p[i]-1) for i in range(10) if m>>i&1) for m in range(1024)] for p in P4]

def vm(vs):return sum(1<<(v-1) for v in vs)
def subsets(mask):
    u=mask
    while True:
        yield u
        if not u:return
        u=(u-1)&mask

def context(masks):
    if len(masks)!=10 or any(isinstance(x,bool) or not isinstance(x,int) or not 0<=x<=7 for x in masks):raise ValueError('MASK_PATTERN')
    pattern=tuple(BINARY[x] for x in masks);allinfo=BOT
    for p in pattern:allinfo=JOIN[allinfo][p]
    if allinfo!=TOP:raise ValueError('FOUR_SYNDROMES_NOT_DISTINCT')
    selected=[i for i,p in enumerate(pattern) if p!=BOT]
    local=[];localmask=[];types=[]
    for v in range(1,11):
        incident={pattern[t] for t in selected if v in TRI[t]};p=BOT
        for q in incident:p=JOIN[p][q]
        local.append(p);localmask.append(vm({u for t in selected if v in TRI[t] for u in TRI[t] if u!=v}));types.append(incident)
    acts=[]
    for vi,fmap in enumerate(FMAPS):
        for si,pmap in enumerate(PMAPS):
            moved=[BOT]*10
            for t,p in enumerate(pattern):moved[fmap[t]]=pmap[p]
            if tuple(moved)==pattern:acts.append((vi,si))
    if (0,STATE_PERMS.index(tuple(range(4)))) not in acts:raise ValueError('IDENTITY_ACTION')
    return pattern,local,localmask,types,acts

def model(masks):
    pattern,local,localmask,types,acts=context(masks)
    def canon(a,p):return min((VMAPS[vi][a],PMAPS[si][p]) for vi,si in acts)
    keys=sorted({canon(a,p) for a in range(1024) for p in range(15) if a or p!=BOT});ix={key:i for i,key in enumerate(keys)}
    rows=[];lo=[];hi=[];names=[];seen=set()
    def row(ts,l,u,name):
        clean={}
        for a,p,c in ts:
            if not(a or p!=BOT):continue
            j=ix[canon(a,p)];clean[j]=clean.get(j,0)+c
        clean={j:c for j,c in clean.items() if c}
        sig=(tuple(sorted(clean.items())),l,u)
        if not clean or sig in seen:return
        seen.add(sig);rows.append(clean);lo.append(l);hi.append(u);names.append(name)
    def H(m,p):return (m&V,p if m&AUX else BOT)
    for p in range(15):
        for i in range(11):row([(*H(FULL,p),1),(*H(FULL^(1<<i),p),-1)],0,INF,('branch-mono',p,i))
        for i,j in combinations(range(11),2):
            for z in subsets(FULL^(1<<i)^(1<<j)):
                row([(*H(z|1<<i,p),1),(*H(z|1<<j,p),1),(*H(z|1<<i|1<<j,p),-1),(*H(z,p),-1)],0,INF,('branch-cmi',p,i,j,z))
        if p!=BOT:row([(V,p,1),(V,BOT,-1)],0,0,('partition-determined',p))
    row([(V,BOT,3),(0,TOP,17)]+[(1<<i,TOP,-2) for i in range(10)],-INF,0,('state-gate',))
    for v in range(1,11):
        n=vm(N[v]);row([(n|1<<(v-1),BOT,1),(n,BOT,-1)],0,0,('graph-fd',v))
        row([(n,local[v-1],1),(n,BOT,-1)],0,0,('neighbor-info',v))
        for p in types[v-1]:row([(n,p,1),(n,BOT,-1)],0,0,('neighbor-factor-info',v,p))
        loc=localmask[v-1]
        row([(loc|1<<(v-1),local[v-1],1),(loc,local[v-1],-1)],0,0,('local-info-fd',v))
        row([(loc|1<<(v-1),TOP,1),(loc,TOP,-1)],0,0,('local-state-fd',v))
    for t,p in enumerate(pattern):
        if p!=BOT:
            m=vm(TRI[t]);row([(m,p,1),(m,BOT,-1)],0,0,('factor-info',t+1))
    for a in range(1024):
        for p,q in COVERS:
            row([(a,p,1),(a,q,-1)],-INF,0,('information-order',a,p,q))
            for i in range(10):
                if a>>i&1:continue
                ai=a|1<<i;row([(ai,p,1),(a,q,1),(ai,q,-1),(a,p,-1)],0,INF,('information-refinement',a,i,p,q))
        for p,q in INCOMP:row([(a,p,1),(a,q,1),(a,JOIN[p][q],-1),(a,MEET[p][q],-1)],0,INF,('partition-cmi',a,p,q))
    goal=[0]*len(keys);goal[ix[canon(V,BOT)]]+=3
    for i in range(10):goal[ix[canon(1<<i,BOT)]]-=2
    return keys,acts,rows,lo,hi,names,goal

def solve(masks,limit):
    t=time.monotonic();keys,acts,rows,lo,hi,names,goal=model(masks);n=len(keys);starts=[];ids=[];vals=[];sources=[]
    for r,data in enumerate(rows):
        signs=(-1,) if lo[r]==0 and hi[r]==INF else ((1,) if lo[r]==-INF and hi[r]==0 else (1,-1))
        for sign in signs:
            sources.append((r,sign));starts.append(len(ids))
            for j,c in data.items():ids.append(j);vals.append(sign*c)
    nv=len(sources);lp=HS.HighsLp();lp.num_col_=nv;lp.num_row_=n;lp.col_cost_=np.ones(nv);lp.col_lower_=np.zeros(nv);lp.col_upper_=np.full(nv,INF)
    lp.row_lower_=np.array(goal,dtype=float);lp.row_upper_=np.array(goal,dtype=float);lp.a_matrix_.format_=HS.MatrixFormat.kColwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(vals,dtype=float)
    h=HS.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit);h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on')
    h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus());report={'status_float':status,'coordinates':n,'unique_rows':len(rows),'dual_variables':nv,'actions':len(acts),'certificate':None,'exact_attempts':[]}
    if status=='Optimal':
        x=h.getSolution().col_value
        for threshold in (1e-9,1e-12,0.):
            chosen=[j for j,v in enumerate(x) if v>threshold];touch=sorted({k for j in chosen for k in rows[sources[j][0]]}|{j for j,g in enumerate(goal) if g});pos={j:i for i,j in enumerate(touch)}
            attempt={'threshold':threshold,'support':len(chosen),'touched':len(touch)}
            if not chosen:attempt['result']='EMPTY';report['exact_attempts'].append(attempt);continue
            dense=[[0]*len(chosen) for _ in touch]
            for k,j in enumerate(chosen):
                r,sign=sources[j]
                for i,c in rows[r].items():dense[pos[i]][k]=sign*c
            A=flint.fmpz_mat(dense);rank=A.rank();attempt['rank']=rank
            if rank!=len(chosen):attempt['result']='RANK_DEFICIENT';report['exact_attempts'].append(attempt);continue
            target=[goal[i] for i in touch];At=A.transpose();y=(At*A).solve(At*flint.fmpz_mat([[g] for g in target]));check=flint.fmpq_mat(A)*y
            if any(check[i,0]!=target[i] for i in range(len(touch))):attempt['result']='INCONSISTENT';report['exact_attempts'].append(attempt);continue
            weights=[Fraction(int(y[k,0].p),int(y[k,0].q)) for k in range(len(chosen))]
            if any(w<0 for w in weights):attempt['result']='SIGN';report['exact_attempts'].append(attempt);continue
            aggregate={}
            for j,w in zip(chosen,weights):
                r,sign=sources[j];aggregate[r]=aggregate.get(r,Fraction())+sign*w
            mult=[{'row':names[r],'multiplier':str(w)} for r,w in aggregate.items() if w]
            attempt['result']='EXACT';report['exact_attempts'].append(attempt)
            report['certificate']={'pattern_masks':masks,'partition_table':PART,'actions':[[P4[vi],STATE_PERMS[si]] for vi,si in acts],
                'multipliers':mult,'target':'3*Delta','row_validity_lemma_sha256':sha256((ROOT/LEMMA).read_bytes()).hexdigest()};break
    report['elapsed_s']=time.monotonic()-t;return report

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('INPUT_HASH')
    index=int(sys.argv[4]);seed=json.loads(raw)['patterns'][index];report=solve(seed['binary_partition_masks'],float(sys.argv[5]));report.update({'pattern_index':index,'pattern_id':seed['id'],'input_sha256':sys.argv[3],
        'limits':'Dual/identity proposal for this literal nonlinear four-syndrome pattern. No probability law, global bound, formal proof, novelty or adoption. Independent semantic checking required.'})
    with open(ROOT/sys.argv[1],'x') as f:json.dump(report,f);f.write('\n')
    print({k:v for k,v in report.items() if k not in ('certificate',)},flush=True)
if __name__=='__main__':main()
