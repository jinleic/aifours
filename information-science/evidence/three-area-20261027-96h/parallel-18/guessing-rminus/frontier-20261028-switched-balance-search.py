#!/usr/bin/env python3
"""Bounded search for positive entropy-balance gap on q=8 coset switches.

Constructs full 128-class independent supports in two syndrome cosets by
switching an affine subspace of the rank-13 K quotient. Float optimization is
only a proposal. Any strict result is checked with integer entropy powers and
still needs an independent original-FD verifier.
"""
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
from time import monotonic
import json,math
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
KRECEIPT=ROOT/'frontier-20261028-rank13-local-parity-obstruction-result.json'
KEXPECTED='f310ca326f23607a8a06a2445cf4bfc2752b5cfa98aad255cbb92ff4fd78154f'
QS=ROOT/'frontier-20261028-multicoset-quotient-search.py'
OUTPUT=ROOT/'frontier-20261028-switched-balance-search-result.json'
ACTIVE=(0,3,6,9)
TOTAL=4096
MAX_SUPPORTS=40
RESTARTS=3
ITERATIONS=3000
MAX_SECONDS=25


def round_weights(p):
    x=p*TOTAL;w=np.floor(x).astype(np.int64);rem=TOTAL-int(w.sum())
    if rem:w[np.argsort(-(x-w))[:rem]]+=1
    return [int(z) for z in w]


def exact(weights,B):
    n=sum(weights);joint=(2**n)*n**(17*n)
    for w in weights:
        if w:joint*=w**(3*w)
    counts=[sum(w*int(B[i,v]) for i,w in enumerate(weights)) for v in range(10)]
    left=1
    for a in counts:
        b=n-a
        if a:left*=a**(2*a)
        if b:left*=b**(2*b)
    return {'denominator':n,'marginal_one_counts':counts,'exact_balance_strict':left>joint,
            'left_bits':left.bit_length(),'right_bits':joint.bit_length()}


def main():
    start=monotonic();raw=INPUT.read_bytes();kr=KRECEIPT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(kr).hexdigest()!=KEXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(t) for t in json.loads(raw)['chosen_triangles']];kdoc=json.loads(kr)
    rows=kdoc['quotient_basis_rows'];local=kdoc['local_forms_in_20bit_code_coordinates']
    rowsp={0:0}
    for i,z in enumerate(rows):
        for x,m in tuple(rowsp.items()):rowsp[x^z]=m^(1<<i)
    lam=[rowsp[z] for z in local]
    occ={v:[j for j,t in enumerate(triangles) if v in t] for v in range(1,11)}
    def project(c):return sum(((c&r).bit_count()&1)<<i for i,r in enumerate(rows))
    def pattern(s,r):
        return sum(((((lam[v-1]&r).bit_count()&1)^sum((s>>j)&1 for j in occ[v]
                   if j in ACTIVE and triangles[j].index(v)==2)%2))<<(v-1) for v in range(1,11))
    spec=spec_from_file_location('quotientsearch',QS);qs=module_from_spec(spec);spec.loader.exec_module(qs)
    stars,reps,kernels=qs.precompute(triangles);spans={v:qs.span(kernels[v]) for v in range(1,11)}
    switches=[]
    for s in range(1,1024):
        delta=set()
        for v in range(1,11):
            if not s&stars[v]:continue
            rep=0
            for j in range(10):
                if s&(1<<j):rep ^= reps[v][j]
            delta.update(project(rep^x) for x in spans[v])
        d=min(delta);group=qs.span([x^d for x in delta])
        if len(group)>=128:continue
        pending=set(range(128))
        while pending:
            t=min(pending);b={t^x for x in group};pending-=b;a=set(range(128))-{r^d for r in b}
            if len(a)+len(b)!=128 or any((x^y) in delta for x in a for y in b):raise ValueError('SWITCH_CONFLICT')
            switches.append((len(group),s,t,sorted(a),sorted(b)))
    switches.sort(key=lambda x:(x[0],x[1],x[2]));rng=np.random.default_rng(2026102803)
    best=None;strict=None;tested=0;steps=0
    for gsize,s,t,a,b in switches[:MAX_SUPPORTS]:
        if monotonic()-start>=MAX_SECONDS:break
        classes=[(0,r) for r in a]+[(s,r) for r in b]
        B=np.array([[(pattern(h,r)>>v)&1 for v in range(10)] for h,r in classes],dtype=float)
        if len(classes)!=128 or np.any(B.sum(axis=0)!=64):raise ValueError('SWITCH_BALANCE')
        Z=1-2*B
        if not np.array_equal(Z.T@Z,128*np.eye(10)):raise ValueError('SWITCH_PAIRWISE_ORTHOGONAL')
        tested+=1
        for restart in range(RESTARTS):
            if monotonic()-start>=MAX_SECONDS:break
            logp=rng.normal(0,0.65 if restart<3 else 1.3,len(classes))
            for it in range(ITERATIONS):
                if it%100==0 and monotonic()-start>=MAX_SECONDS:break
                logp-=np.max(logp);p=np.exp(np.maximum(logp,-700));p/=p.sum()
                joint=13*math.log(2)-float(np.dot(p,np.log(np.maximum(p,1e-300))))
                one=p@B;one=np.clip(one,1e-300,1-1e-15)
                marg=2*math.log(2)-one*np.log(one)-(1-one)*np.log(1-one)
                cap=float(marg.max());gap=joint-(2/3)*float(marg.sum());steps+=1
                if best is None or gap>best['gap_nats']:
                    best={'gap_nats':gap,'ratio_float':joint/cap,'syndrome':s,'switch_representative':t,
                          'group_size':gsize,'restart':restart,'iteration':it,
                          'class_ones':one.tolist()}
                if gap>1e-7:
                    weights=round_weights(p);test=exact(weights,B)
                    if test['exact_balance_strict']:
                        strict={'syndrome':s,'switch_representative':t,'group_size':gsize,
                                'classes':classes,'weights':weights,'integer_entropy_check':test}
                        break
                observed=np.where(B>0.5,one[None,:],1-one[None,:])
                grad=-np.log(np.maximum(p,1e-300))-1+(2/3)*np.sum(np.log(np.maximum(observed,1e-300))+1,axis=1)
                logp+=(0.012/math.sqrt(1+it/300))*np.clip(grad,-100,100)
            if strict:break
        if strict:break
    out={'baseline_result_sha256':EXPECTED,'K_receipt_sha256':KEXPECTED,'total_switches':len(switches),
         'supports_tested':tested,'optimizer_steps':steps,'seed':2026102803,'best_float':best,
         'strict_integer_candidate':strict,'elapsed_seconds':monotonic()-start,
         'limits':'A bounded search on selected switches, not an upper bound. Floating values are exploratory; even a passing integer candidate requires independent original-neighbour and decoder verification.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_integer_candidate'},indent=2))
    if strict:print('STRICT POSITIVE BALANCE CANDIDATE: independent verification required')


if __name__=='__main__':main()
