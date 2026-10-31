#!/usr/bin/env python3
"""Batched probability proposals on one verified full-FD S5 subgroup antichain."""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import prod
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER=('frontier-20261028-group-coset-fd-search-v2.py','856a6b1cc28ef8d812c78769e9bb9d936e5ecc1e67838fca94661dd2f5947d5d')
SOURCE=('frontier-20261028-s5-nonuniform-antichain-search-result.json','08c6ae7e1a36bd4b41fb42618f7fe9aec360cbce863282cb33a84160dd300718')
OUT=ROOT/'frontier-20261028-s5-fixed-antichain-variational-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def helper():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HELPER')
    spec=spec_from_file_location('grouphelper',ROOT/HELPER[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod);return mod


def labels(H,table):
    n=len(table);remaining=set(range(n));label=np.empty(n,dtype=np.int32);idx=0;members=[i for i in range(n) if H>>i&1]
    while remaining:
        x=min(remaining);group={table[x][h] for h in members}
        if len(group)!=len(members) or not group<=remaining:raise ValueError('COSETS')
        label[list(group)]=idx;remaining-=group;idx+=1
    return label,idx


def exact_polynomial(q,lab):
    for scale in (16,64,256,1024):
        t=[np.rint(scale*np.cbrt(row)).astype(np.int64) for row in q]
        D=prod(sum(int(x)**3 for x in row)**2 for row in t)
        S=sum(prod(int(t[i][lab[i][g]])**2 for i in range(10)) for g in range(120))
        if S**3>D:return {'scale':scale,'integer_rows':[x.tolist() for x in t],'S':str(S),'D':str(D)}
    return None


def main():
    start=monotonic();mod=helper();src=pin(SOURCE);elements,table=mod.group(5);H=mod.subgroups(table);chosen=src['cases'][0]['subgroup_indices']
    if len(elements)!=120 or len(H)!=156 or len(chosen)!=10:raise ValueError('SOURCE')
    check=mod.exact_verify(chosen,H,120)
    if check['intersection_order']!=1 or any(H[i]&H[j] in (H[i],H[j]) for i,j in combinations(chosen,2)):raise ValueError('ANTICHAIN')
    lab=[];sizes=[]
    for i in chosen:
        v,k=labels(H[i],table);lab.append(v);sizes.append(k)
    rng=np.random.default_rng(2026102811);starts=[np.full(120,1/120)]
    for alpha in (.05,.2,.7,2.):starts.extend(rng.dirichlet(np.full(120,alpha),size=16))
    P=np.array(starts);B=len(P);best=-float('inf');best_start=-1;best_step=-1;best_q=None;iterations=0
    for step in range(1000):
        if monotonic()-start>50:break
        qs=[];logweight=np.zeros((B,120));offs=np.arange(B)[:,None]
        for label,k in zip(lab,sizes):
            q=np.bincount((label[None,:]+offs*k).ravel(),weights=P.ravel(),minlength=B*k).reshape(B,k);qs.append(q)
            logweight+=(2/3)*np.log(np.maximum(q[offs,label[None,:]],1e-300))
        shift=logweight.max(axis=1,keepdims=True);score=shift[:,0]+np.log(np.exp(logweight-shift).sum(axis=1))
        j=int(np.argmax(score))
        if float(score[j])>best:best=float(score[j]);best_start=j;best_step=step;best_q=[x[j].copy() for x in qs]
        Pnew=np.exp(logweight-shift);Pnew/=Pnew.sum(axis=1,keepdims=True);iterations=step+1
        if float(np.max(np.abs(Pnew-P)))<1e-11:P=Pnew;break
        P=Pnew
    witness=exact_polynomial(best_q,lab) if best>1e-8 else None
    out={'source_search_sha256':SOURCE[1],'helper_sha256':HELPER[1],'subgroup_indices':chosen,'subgroup_orders':check['subgroup_orders'],
         'full_fd_subgroup_checks':True,'pairwise_incomparable':True,'intersection_order':1,
         'start_count':B,'iterations':iterations,'maximum_logS_float_unverified':best,'best_start':best_start,'best_step':best_step,
         'strict_polynomial_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'One fixed full-FD S5 antichain and bounded floating variational proposals only; no global or exact nonexistence claim. Any positive exact witness needs independent verification.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_polynomial_witness'},indent=2))


if __name__=='__main__':main()
