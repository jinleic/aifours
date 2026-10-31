#!/usr/bin/env python3
"""Bounded nonuniform S5-coset proposals with necessary subgroup antichain.

Floating entropy/MIP/alternating updates propose candidates only. Positive
rational probability or polynomial witnesses are checked using integers.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from math import log,prod
from pathlib import Path
from random import Random
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
MOD=('frontier-20261028-group-coset-fd-search-v2.py','856a6b1cc28ef8d812c78769e9bb9d936e5ecc1e67838fca94661dd2f5947d5d')
OUT=ROOT/'frontier-20261028-s5-nonuniform-antichain-search-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def module():
    raw=(ROOT/MOD[0]).read_bytes()
    if sha256(raw).hexdigest()!=MOD[1]:raise ValueError('SOURCE_HASH')
    spec=spec_from_file_location('grouphelper',ROOT/MOD[0]);m=module_from_spec(spec);spec.loader.exec_module(m);return m


def cosets(H,table):
    n=len(table);remaining=set(range(n));out=[]
    elements=[h for h in range(n) if H>>h&1]
    while remaining:
        x=min(remaining);block={table[x][h] for h in elements}
        if len(block)!=len(elements) or not block<=remaining:raise ValueError('COSET_PARTITION')
        out.append(tuple(sorted(block)));remaining-=block
    return out


def exact_gap(weights,chosen,blocks):
    w=sum(weights);left=1
    for h in chosen:
        for block in blocks[h]:
            s=sum(weights[g] for g in block)
            if s:left*=s**(2*s)
    right=w**(17*w)*prod(v**(3*v) for v in weights if v)
    digest=lambda x:sha256(x.to_bytes((x.bit_length()+7)//8,'big')).hexdigest()
    return {'left_sha256_big_endian':digest(left),'right_sha256_big_endian':digest(right),
            'left_bits':left.bit_length(),'right_bits':right.bit_length(),'strict':left>right}


def variational(chosen,blocks,start):
    n=len(start);p=np.array(start,dtype=float);p/=p.sum();look=[]
    for h in chosen:
        idx=np.empty(n,dtype=np.int32)
        for i,block in enumerate(blocks[h]):idx[list(block)]=i
        look.append(idx)
    for _ in range(500):
        q=[np.bincount(idx,weights=p,minlength=int(idx.max())+1) for idx in look]
        logw=np.zeros(n)
        for idx,arr in zip(look,q):logw+=np.log(np.maximum(arr[idx],1e-300))*(2./3.)
        logw-=logw.max();new=np.exp(logw);new/=new.sum()
        if np.max(np.abs(new-p))<1e-12:p=new;break
        p=new
    q=[np.bincount(idx,weights=p,minlength=int(idx.max())+1) for idx in look]
    # Test the exact nonnegative integer-polynomial witness after discretization.
    for scale in (32,128,512,2048):
        t=[np.rint(scale*np.cbrt(arr)).astype(np.int64) for arr in q]
        S=sum(prod(int(t[i][idx[g]])**2 for i,idx in enumerate(look)) for g in range(n))
        D=prod(sum(int(x)**3 for x in row)**2 for row in t)
        if S**3>D:return {'scale':scale,'integer_rows':[row.tolist() for row in t],'S':str(S),'D':str(D)}
    return None


def main():
    start=monotonic();helper=module();elements,table=helper.group(5);H=helper.subgroups(table);n=len(elements);ns=len(H)
    if n!=120 or ns!=156:raise ValueError('GROUP')
    blocks=[cosets(h,table) for h in H];lp=helper.build(n,H)
    lo=np.array(lp.row_lower_,dtype=float);hi=np.array(lp.row_upper_,dtype=float);lo[-1]=hi[-1]=1;lp.row_lower_=lo;lp.row_upper_=hi
    upper=np.array(lp.col_upper_,dtype=float)
    for i in range(10):
        for j,h in enumerate(H):
            if h.bit_count() in (1,n):upper[i*ns+j]=0
    lp.col_upper_=upper;lp.sense_=highspy.ObjSense.kMinimize
    starts=list(lp.a_matrix_.start_[:-1]);indices=list(lp.a_matrix_.index_);values=list(lp.a_matrix_.value_);low=list(lp.row_lower_);up=list(lp.row_upper_)
    comparable=[(a,b) for a,A in enumerate(H) for b,B in enumerate(H) if A&B in (A,B)]
    for i in range(10):
        for j in range(i+1,10):
            for a,b in comparable:
                starts.append(len(indices));indices.extend((i*ns+a,j*ns+b));values.extend((1.,1.));low.append(-highspy.kHighsInf);up.append(1.)
    lp.num_row_=len(starts);lp.row_lower_=np.array(low);lp.row_upper_=np.array(up)
    lp.a_matrix_.start_=np.array(starts+[len(indices)],np.int32);lp.a_matrix_.index_=np.array(indices,np.int32);lp.a_matrix_.value_=np.array(values,float)
    seed=[j for j,h in enumerate(H) if h.bit_count() in (2,3)][:10]
    if len(seed)!=10 or any(H[a]&H[b] in (H[a],H[b]) for a,b in __import__('itertools').combinations(seed,2)):raise ValueError('SEED_ANTICHAIN')
    helper.exact_verify(seed,H,n)
    init=np.zeros(lp.num_col_)
    for i,j in enumerate(seed):init[i*ns+j]=1
    init[10*ns]=1  # identity is the sole common group element
    rng=Random(2026102809)
    cases=[[1]*n,[16]+[1]*(n-1),[5]*4+[1]*(n-4)]+[[rng.randint(1,5) for _ in range(n)] for _ in range(3)]
    results=[];witness=None
    for weights in cases:
        total=sum(weights);cost=[]
        for group in blocks:
            sizes=[sum(weights[g] for g in block) for block in group]
            cost.append(log(total)-sum((s/total)*log(s) for s in sizes))
        lp.col_cost_=np.array(cost*10+[0.]*n)
        h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',5.)
        h.passModel(lp);seed_status=str(h.setSolution(lp.num_col_,np.arange(lp.num_col_,dtype=np.int32),init));t0=monotonic();h.run();sol=h.getSolution()
        record={'weight_numerators':weights,'status_float_unverified':h.modelStatusToString(h.getModelStatus()),'seed_status':seed_status,'elapsed_seconds':monotonic()-t0}
        if sol.value_valid:
            chosen=[]
            for i in range(10):
                picked=[j for j in range(ns) if sol.col_value[i*ns+j]>.5]
                if len(picked)!=1:raise ValueError('ONEHOT')
                chosen.append(picked[0])
            structural=helper.exact_verify(chosen,H,n)
            if structural['intersection_order']!=1 or any(H[a]&H[b] in (H[a],H[b]) for a,b in __import__('itertools').combinations(chosen,2)):raise ValueError('STRUCTURE')
            gap=exact_gap(weights,chosen,blocks);poly=variational(chosen,blocks,weights)
            record.update({'subgroup_indices':chosen,'subgroup_orders':structural['subgroup_orders'],'rational_gap_test':gap,'strict_polynomial_witness':poly})
            if gap['strict'] or poly:
                witness={'weights':weights,'subgroup_masks':[str(H[j]) for j in chosen],'group_elements':elements,'rational_gap':gap,'polynomial':poly};results.append(record);break
        results.append(record)
    out={'group_order':n,'subgroup_count':ns,'antichain_rows':45*len(comparable),'fixed_intersection_order':1,
         'cases':results,'strict_witness':witness,'per_case_time_limit_seconds':5.,'elapsed_seconds':monotonic()-start,
         'limits':'Six selected positive rational distributions and bounded MIP/variational proposals only; no nonexistence or exact optimization inference. A positive witness requires separate graph, group and entropy/polynomial checking.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_witness'},indent=2))


if __name__=='__main__':main()
