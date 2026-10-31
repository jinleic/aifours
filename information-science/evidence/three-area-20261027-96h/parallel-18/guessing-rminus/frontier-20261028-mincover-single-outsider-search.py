#!/usr/bin/env python3
"""Batched variational proposals on canonical all-four-syndrome outsider trades."""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import prod
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER=('frontier-20261028-four-factor-cover-mip.py','e1308e6a85572dd52028ff4ef344ebff51b3fd112b94449ddbe4e5d8466c5fd1')
OUT=ROOT/'frontier-20261028-mincover-single-outsider-search-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))


def helper():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HASH')
    spec=spec_from_file_location('mixedhelper',ROOT/HELPER[0]);m=module_from_spec(spec);spec.loader.exec_module(m);return m


def canonical_support(mod,cover):
    Ts,pos=mod.model_geometry(cover);seed=mod.xor_seed(Ts,pos);outside=0
    for t,T in enumerate(Ts):
        v=T[0];slot=pos[v][[j for j,U in enumerate(Ts) if v in U].index(t)];outside^=1<<slot
    conflicts=[]
    for x in seed:
        d=x^outside;active={v for v in range(1,11) if any(d>>j&1 for j in pos[v])}
        if any(not (set(mod.N[v])&active) for v in active):conflicts.append(x)
    W=sorted((set(seed)-set(conflicts))|{outside});mod.verify(W,pos)
    labels=[];sizes=[]
    for v in range(1,11):
        labels.append(np.array([sum(((w>>j)&1)<<k for k,j in enumerate(pos[v])) for w in W],dtype=np.int32));sizes.append(1<<len(pos[v]))
    return W,pos,outside,len(conflicts),labels,sizes


def exact_polynomial(q,labels):
    n=len(labels[0])
    for scale in (16,64,256,1024):
        t=[np.rint(scale*np.cbrt(a)).astype(np.int64) for a in q]
        D=prod(sum(int(x)**3 for x in row)**2 for row in t)
        S=sum(prod(int(t[i][labels[i][j]])**2 for i in range(10)) for j in range(n))
        if S**3>D:return {'scale':scale,'integer_weights':[x.tolist() for x in t],'weighted_sum':str(S),'threshold_product':str(D)}
    return None


def main():
    start=monotonic();mod=helper();rng=np.random.default_rng(2026102822);records=[];witness=None
    for cover in mod.COVERS:
        if monotonic()-start>55:break
        W,pos,outside,removed,labels,sizes=canonical_support(mod,cover);n=len(W)
        starts=[np.full(n,1/n)]
        for a in (.05,.2,.7,2.):starts.extend(rng.dirichlet(np.full(n,a),size=12))
        P=np.array(starts);B=len(P);best=-float('inf');best_q=None;best_start=best_step=-1;iterations=0
        for step in range(1000):
            if monotonic()-start>55:break
            offs=np.arange(B)[:,None];logweight=np.zeros((B,n));qs=[]
            for label,k in zip(labels,sizes):
                q=np.bincount((label[None,:]+offs*k).ravel(),weights=P.ravel(),minlength=B*k).reshape(B,k);qs.append(q)
                logweight+=(2/3)*np.log(np.maximum(q[offs,label[None,:]],1e-300))
            shift=logweight.max(axis=1,keepdims=True);score=shift[:,0]+np.log(np.exp(logweight-shift).sum(axis=1))
            idx=int(np.argmax(score))
            if float(score[idx])>best:best=float(score[idx]);best_q=[q[idx].copy() for q in qs];best_start=idx;best_step=step
            new=np.exp(logweight-shift);new/=new.sum(axis=1,keepdims=True);iterations=step+1
            if float(np.max(np.abs(new-P)))<1e-11:P=new;break
            P=new
        if not iterations:break
        exact=exact_polynomial(best_q,labels) if best>1e-8 else None
        rec={'factor_indices':cover,'outside_word':outside,'removed_conflicts':removed,'support_size':n,'starts':B,'iterations':iterations,
             'maximum_logS_float_unverified':best,'best_start':best_start,'best_step':best_step,'strict_integer_witness':bool(exact)}
        records.append(rec)
        if exact:witness={'factor_indices':cover,'vertex_bit_positions':pos,'support_words':W,**exact};break
    out={'helper_sha256':HELPER[1],'cases':records,'strict_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'One canonical 1111 outsider per minimal-cover orbit and bounded floating variational starts. No absence/optimum claim; a positive exact witness needs independent verification.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_witness'},indent=2))


if __name__=='__main__':main()
