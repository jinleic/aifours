#!/usr/bin/env python3
"""Independent raw-coordinate check of a nonlinear four-state entropy identity.
Usage: python3 script.py OUT.json REPORT.json REPORT_SHA
No producer/solver import. Partitions are independently generated as set
partitions, join/meet reconstructed from equivalence relations. Every actual
coding FD, state action and lattice row is validated, then the identity is
expanded over all 15359 original/partition coordinates with Fractions.
"""
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
LEMMA='frontier-20261029-fourstate-partition-model-lemma-v1.md';LEMMA_SHA='7a612d5a49e1222d97fc38c0b77dd6560cc1ee42021461aeea7cd68aedf30473'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))

def set_partitions():
    out=[]
    def rec(s,blocks):
        if s==4:
            labels=[None]*4
            for i,B in enumerate(blocks):
                for state in B:labels[state]=i
            out.append(tuple(labels));return
        for i in range(len(blocks)):
            b=[list(B) for B in blocks];b[i].append(s);rec(s+1,b)
        rec(s+1,[*blocks,[s]])
    rec(0,[])
    return sorted(out)
PART=set_partitions();PI={p:i for i,p in enumerate(PART)}
if len(PART)!=15 or len(PI)!=15:raise ValueError('BELL4')
BOT=PI[(0,0,0,0)];TOP=PI[(0,1,2,3)]
def relation(p):return {(a,b) for a,b in combinations(range(4),2) if PART[p][a]==PART[p][b]}
REL=[relation(p) for p in range(15)]
def from_relation(rel):
    blocks=[{s} for s in range(4)]
    for a,b in rel:
        ia=next(i for i,B in enumerate(blocks) if a in B);ib=next(i for i,B in enumerate(blocks) if b in B)
        if ia!=ib:
            merged=blocks[ia]|blocks[ib];blocks=[B for i,B in enumerate(blocks) if i not in (ia,ib)];blocks.append(merged)
    blocks.sort(key=min);labels=[None]*4
    for i,B in enumerate(blocks):
        for s in B:labels[s]=i
    return PI[tuple(labels)]
def join(p,q):return from_relation(REL[p]&REL[q])
def meet(p,q):return from_relation(REL[p]|REL[q])
def leq(p,q):return REL[q]<=REL[p]
def state_action(perm):
    return tuple(from_relation({(a,b) for a,b in combinations(range(4),2) if PART[p][perm[a]]==PART[p][perm[b]]}) for p in range(15))
def binary_id(w):
    bits=(0,*(int(bool(w>>(i-1)&1)) for i in range(1,4)))
    return from_relation({(a,b) for a,b in combinations(range(4),2) if bits[a]==bits[b]})
def vm(vs):return sum(1<<(v-1) for v in vs)
def moved(mask,p):return sum(1<<(p[i]-1) for i in range(10) if mask>>i&1)

def context(masks):
    if len(masks)!=10 or any(type(w) is not int or not 0<=w<=7 for w in masks):raise ValueError('PATTERN_MASKS')
    pattern=tuple(binary_id(w) for w in masks);allinfo=BOT
    for p in pattern:allinfo=join(allinfo,p)
    if allinfo!=TOP:raise ValueError('FOUR_SELECTOR_STATES_NOT_SEPARATED')
    local=[];locmask=[];incident=[]
    for v in range(1,11):
        types={pattern[t] for t,T in enumerate(TRI) if v in T and pattern[t]!=BOT};p=BOT
        for q in types:p=join(p,q)
        local.append(p);incident.append(types);locmask.append(vm({u for t,T in enumerate(TRI) if v in T and pattern[t]!=BOT for u in T if u!=v}))
    return pattern,local,locmask,incident

def row_terms(name,ctx):
    pattern,local,locmask,incident=ctx;k=name[0];V=1023;FULL=2047
    def mask(a):
        if type(a) is not int or not 0<=a<=V:raise ValueError('ORIGINAL_MASK')
    def pid(p):
        if type(p) is not int or not 0<=p<15:raise ValueError('PARTITION_ID')
    def H(m,p):return (m&V,p if m&1024 else BOT)
    if k=='branch-mono':
        p,i=name[1:];pid(p)
        if type(i) is not int or not 0<=i<11:raise ValueError('BRANCH_MONO')
        return [(*H(FULL,p),1),(*H(FULL^(1<<i),p),-1)],'ge'
    if k=='branch-cmi':
        p,i,j,z=name[1:];pid(p)
        if not 0<=i<j<11 or type(z) is not int or not 0<=z<=FULL or z&((1<<i)|(1<<j)):raise ValueError('BRANCH_CMI')
        return [(*H(z|1<<i,p),1),(*H(z|1<<j,p),1),(*H(z|1<<i|1<<j,p),-1),(*H(z,p),-1)],'ge'
    if k=='partition-determined':
        p=name[1];pid(p)
        return [(V,p,1),(V,BOT,-1)],'eq'
    if k=='state-gate':
        if len(name)!=1:raise ValueError('ONLY_FULL_STATE_GATE')
        return [(V,BOT,3),(0,TOP,17)]+[(1<<i,TOP,-2) for i in range(10)],'le'
    if k=='graph-fd':
        v=name[1]
        if v not in N:raise ValueError('VERTEX')
        n=vm(N[v]);return [(n|1<<(v-1),BOT,1),(n,BOT,-1)],'eq'
    if k in ('neighbor-info','neighbor-factor-info','local-info-fd','local-state-fd'):
        v=name[1]
        if v not in N:raise ValueError('VERTEX')
        if k=='neighbor-info':p=local[v-1];a=vm(N[v]);return [(a,p,1),(a,BOT,-1)],'eq'
        if k=='neighbor-factor-info':
            p=name[2];pid(p)
            if p not in incident[v-1]:raise ValueError('INCIDENT_FACTOR_INFORMATION')
            a=vm(N[v]);return [(a,p,1),(a,BOT,-1)],'eq'
        p=TOP if k=='local-state-fd' else local[v-1];a=locmask[v-1]
        if a&~vm(N[v]):raise ValueError('ACTUAL_COMPONENT_LOCAL_SET')
        return [(a|1<<(v-1),p,1),(a,p,-1)],'eq'
    if k=='factor-info':
        t=name[1]
        if type(t) is not int or not 1<=t<=10 or pattern[t-1]==BOT:raise ValueError('SELECTED_FACTOR')
        a=vm(TRI[t-1]);return [(a,pattern[t-1],1),(a,BOT,-1)],'eq'
    if k=='information-order':
        a,p,q=name[1:];mask(a);pid(p);pid(q)
        if p==q or not leq(p,q):raise ValueError('INFORMATION_ORDER')
        return [(a,p,1),(a,q,-1)],'le'
    if k=='information-refinement':
        a,i,p,q=name[1:];mask(a);pid(p);pid(q)
        if not 0<=i<10 or a>>i&1 or p==q or not leq(p,q):raise ValueError('CONDITIONAL_INFORMATION_REFINEMENT')
        ai=a|1<<i;return [(ai,p,1),(a,q,1),(ai,q,-1),(a,p,-1)],'ge'
    if k=='partition-cmi':
        a,p,q=name[1:];mask(a);pid(p);pid(q)
        return [(a,p,1),(a,q,1),(a,join(p,q),-1),(a,meet(p,q),-1)],'ge'
    raise ValueError(('UNSUPPORTED_ROW',name))

def check(cert,change=False):
    if cert.get('row_validity_lemma_sha256')!=LEMMA_SHA or sha256((ROOT/LEMMA).read_bytes()).hexdigest()!=LEMMA_SHA:raise ValueError('ROW_LEMMA_BINDING')
    if [tuple(p) for p in cert['partition_table']]!=PART:raise ValueError('PARTITION_TABLE')
    ctx=context(cert['pattern_masks']);pattern,local,locmask,incident=ctx;E={frozenset((v,u)) for v in N for u in N[v]};lookup={tuple(sorted(T)):i for i,T in enumerate(TRI)};acts=[]
    if len(E)!=26:raise ValueError('GRAPH')
    for vp,sp in cert['actions']:
        vp=tuple(vp);sp=tuple(sp)
        if sorted(vp)!=list(range(1,11)) or {frozenset(vp[v-1] for v in e) for e in E}!=E or sorted(sp)!=list(range(4)):raise ValueError('ACTION')
        fm=[lookup[tuple(sorted(vp[v-1] for v in T))] for T in TRI];pm=state_action(sp)
        if any(pm[join(p,q)]!=join(pm[p],pm[q]) or pm[meet(p,q)]!=meet(pm[p],pm[q]) for p in range(15) for q in range(15)):raise ValueError('PARTITION_LATTICE_ACTION')
        new=[BOT]*10
        for t,p in enumerate(pattern):new[fm[t]]=pm[p]
        if tuple(new)!=pattern:raise ValueError('PARITY_PATTERN_ACTION')
        for v in range(1,11):
            if pm[local[v-1]]!=local[vp[v-1]-1] or moved(locmask[v-1],vp)!=locmask[vp[v-1]-1]:raise ValueError('LOCAL_DECODER_ACTION')
        acts.append((vp,pm,sp))
    if not acts or len({(p,s) for p,pm,s in acts})!=len(acts) or not any(p==tuple(range(1,11)) and s==tuple(range(4)) for p,pm,s in acts):raise ValueError('ACTION_SET')
    acc={};counts=Counter();g=len(acts)
    for item in cert['multipliers']:
        q=Fraction(item['multiplier']);ts,kind=row_terms(item['row'],ctx)
        if not q:raise ValueError('ZERO_WEIGHT')
        if kind=='ge' and q>=0:raise ValueError('SIGN_GE')
        if kind=='le' and q<=0:raise ValueError('SIGN_LE')
        for vp,pm,sp in acts:
            for a,p,c in ts:
                a2=moved(a,vp);p2=pm[p]
                if a2 or p2!=BOT:acc[a2,p2]=acc.get((a2,p2),Fraction())+q*c/g
        counts[item['row'][0]]+=1
    target={(1023,BOT):Fraction(4 if change else 3)}
    for i in range(10):target[1<<i,BOT]=Fraction(-2)
    if {key:q for key,q in acc.items() if q}!=target:raise ValueError('RAW_IDENTITY')
    return counts

def main():
    t=time.monotonic();raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('REPORT_HASH')
    report=json.loads(raw);cert=report.get('certificate')
    if cert is None:raise ValueError('NO_EXACT_CERTIFICATE')
    counts=check(cert);controls={}
    try:check(cert,True)
    except ValueError as e:controls['changed_target']=str(e)
    else:raise ValueError('CONTROL')
    mutant=deepcopy(cert);mutant['row_validity_lemma_sha256']='0'*64
    try:check(mutant)
    except ValueError as e:controls['changed_row_contract']=str(e)
    else:raise ValueError('CONTROL')
    mutant=deepcopy(cert);mutant['partition_table'][1]=[0,0,0,0]
    try:check(mutant)
    except ValueError as e:controls['changed_partition_table']=str(e)
    else:raise ValueError('CONTROL')
    gi=next((i for i,m in enumerate(cert['multipliers']) if row_terms(m['row'],context(cert['pattern_masks']))[1]=='ge'),None)
    if gi is not None:
        mutant=deepcopy(cert);mutant['multipliers'][gi]['multiplier']=str(-Fraction(mutant['multipliers'][gi]['multiplier']))
        try:check(mutant)
        except ValueError as e:controls['flipped_shannon_sign']=str(e)
        else:raise ValueError('CONTROL')
    sigma=[0]+[sum(1<<t for t,w in enumerate(cert['pattern_masks']) if w>>(s-1)&1) for s in range(1,4)]
    out={'report_sha256':sys.argv[3],'checker_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'row_validity_lemma_sha256':LEMMA_SHA,
      'all_checked':True,'pattern_id':report['pattern_id'],'pattern_masks':cert['pattern_masks'],'syndrome_values':sigma,'rows':sum(counts.values()),'row_kinds':dict(counts),'raw_entropy_coordinates':15359,
      'negative_controls':controls,'elapsed_s':time.monotonic()-t,
      'limits':'Exact same-harness coefficient/sign/action/premise check for this explicit four-syndrome pattern, with direct written actual-component decoder and full-state-gate arguments. No actual winning law, all-four-syndrome theorem, unrestricted bound, formal proof, scientific adoption or novelty claim.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(out,f,indent=1);f.write('\n')
    print(json.dumps(out,indent=1))
if __name__=='__main__':main()
