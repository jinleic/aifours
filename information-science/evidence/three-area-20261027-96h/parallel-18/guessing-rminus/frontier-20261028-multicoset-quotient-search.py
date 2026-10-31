#!/usr/bin/env python3
"""Bounded exact search for a q=8 nonlinear lift over a parity subcode.

Four syndrome cosets are quotiented by a codimension-k subgroup K of the
verified triangle parity code. A selected quotient class lifts to all of K.
Forbidden quotient differences are computed exactly from isolated-vertex
subspaces. Z3 searches for >2^k independent quotient classes; no numerical
LP or external source code is executed. A SAT finding requires a separate
independent verifier before admission.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from random import Random
from time import monotonic
import json
from z3 import Bool,Not,Or,PbGe,Solver,is_true,sat

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-multicoset-quotient-search-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
K=5
MAX_CASES=16
TOTAL_SECONDS=28
CASE_MILLISECONDS=1200


def proj(mask,bits):
    return sum(((mask>>p)&1)<<j for j,p in enumerate(bits))


def span(vectors):
    result={0}
    for v in vectors:result |= {x^v for x in tuple(result)}
    return result


def precompute(triangles):
    stars={};reps={};kernels={}
    for v in range(1,11):
        non=set(range(1,11))-set(N[v])-{v}
        stars[v]=sum(1<<j for j,t in enumerate(triangles) if v in t)
        reps[v]=[];kernels[v]=[]
        for j,t in enumerate(triangles):
            selected=v if v in t else next(u for u in t if u in non)
            index=t.index(selected)
            reps[v].append((1<<(2*j+index)) if index<2 else 0)
            avail=[i for i,u in enumerate(t) if u in non]
            if len(avail)>1:
                for b in avail[1:]:
                    g=0
                    for p in (avail[0],b):
                        if p<2:g ^= 1<<(2*j+p)
                    kernels[v].append(g)
    return stars,reps,kernels


def delta(s,bits,stars,reps,kernels,projected):
    found=set()
    for v in range(1,11):
        if not s&stars[v]:continue
        representative=0
        for j in range(10):
            if s&(1<<j):representative ^= reps[v][j]
        o=proj(representative,bits)
        found.update(o^u for u in projected[v])
    return found


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    stars,reps,kernels=precompute(triangles)
    random=Random(20261028);candidates=[]
    # Distinct unit syndromes and their xor minimize the number of possible
    # isolated vertices; rank candidates by actual quotient conflict density.
    pairs=list(combinations(range(10),2))
    for _ in range(120):
        bits=tuple(sorted(random.sample(range(20),K)))
        projected={v:span([proj(g,bits) for g in kernels[v]]) for v in range(1,11)}
        for a,b in pairs:
            s1,s2=1<<a,1<<b
            ds=[delta(s,bits,stars,reps,kernels,projected) for s in (s1,s2,s1^s2)]
            if any(not z for z in ds):raise ValueError('NONZERO_SYNDROME_WITHOUT_CONFLICT')
            if any(len(z)==1<<K for z in ds):continue
            candidates.append((sum(map(len,ds)),max(map(len,ds)),bits,a,b,ds))
    candidates.sort(key=lambda x:x[:5]);cases=[];candidate_support=None
    for _,_,bits,a,b,ds in candidates:
        if monotonic()-start>TOTAL_SECONDS or len(cases)>=MAX_CASES:break
        n=1<<K;syndrome=(0,1<<a,1<<b,(1<<a)^(1<<b));by_xor={1:ds[0],2:ds[1],3:ds[2]}
        select=[[Bool(f'x_{h}_{x}') for x in range(n)] for h in range(4)]
        solver=Solver();solver.set(timeout=CASE_MILLISECONDS)
        solver.add(PbGe([(select[h][x],1) for h in range(4) for x in range(n)],n+1))
        for h in range(4):
            for j in range(h+1,4):
                for x in range(n):
                    for d in by_xor[h^j]:solver.add(Or(Not(select[h][x]),Not(select[j][x^d])))
        status=solver.check();entry={'projection_bits':bits,'syndrome_basis':[1<<a,1<<b],
             'delta_sizes':[len(z) for z in ds],'solver_status':str(status)}
        if status==sat:
            model=solver.model()
            chosen=[[h,x] for h in range(4) for x in range(n)
                    if is_true(model.eval(select[h][x],model_completion=True))]
            if len(chosen)<n+1:raise ValueError('SOLVER_SELECTION_TOO_SMALL')
            for i,(h,x) in enumerate(chosen):
                for j,y in chosen[i+1:]:
                    if h!=j and (x^y) in by_xor[h^j]:raise ValueError('QUOTIENT_CONFLICT')
            entry['chosen_quotient_classes']=chosen;candidate_support=entry
        cases.append(entry)
        if candidate_support:break
    out={'input_sha256':EXPECTED,'projection_codimension':K,'random_seed':20261028,
         'projection_bit_samples':120,'ranked_candidate_instances':len(candidates),
         'solver_case_time_limit_ms':CASE_MILLISECONDS,'elapsed_seconds':monotonic()-start,
         'examined_cases':cases,'candidate_found':candidate_support is not None,
         'limits':'A candidate is not admitted until an independently implemented exact check of quotient conflicts and original graph decoder; UNSAT applies only to the individual finite quotient, not all q=8 or general alphabets.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
