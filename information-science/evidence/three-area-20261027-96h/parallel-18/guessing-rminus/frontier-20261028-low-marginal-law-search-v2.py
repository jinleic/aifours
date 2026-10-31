#!/usr/bin/env python3
"""Search a finite q=8 multi-coset law with an exact 20/3 entropy target.

K is the rank-13 triangle subcode annihilated by ten local parity forms.
A 16-class independent quotient selection, each vertex parity active at most
2/16 times, would yield Hjoint=17 and Hsingle<=2+h(1/8), a strict gain.
A solver candidate requires an independent exact original-FD verifier.
"""
from collections import Counter
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
import json
from z3 import Bool,Not,Or,PbEq,PbLe,Solver,is_true,sat

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
QS=ROOT/'frontier-20261028-multicoset-quotient-search.py'
OUTPUT=ROOT/'frontier-20261028-low-marginal-law-search-v2-result.json'
ACTIVE=(0,3,6,9)
BASIS=(658,22,529,34)
TIMEOUT_MS=30000


def rank(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in piv:x ^= piv[k]
            else:piv[k]=x;break
    return len(piv)


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    occ={v:[j for j,t in enumerate(triangles) if v in t] for v in range(1,11)}
    if any(len(x)!=3 for x in occ.values()) or rank(BASIS)!=4:raise ValueError('SETUP')
    forms={}
    for v in range(1,11):
        forms[v]=[]
        for j in occ[v]:
            p=triangles[j].index(v)
            forms[v].append((1<<(2*j)) if p==0 else (1<<(2*j+1)) if p==1 else (3<<(2*j)))
    constraints=[]
    for v in range(1,11):
        g=0
        for j,f in zip(occ[v],forms[v]):
            if j in ACTIVE:g ^= f
        constraints.append(g)
    rb=[]
    for g in constraints:
        if rank(rb+[g])>len(rb):rb.append(g)
    if len(rb)!=7 or any(rank(rb+forms[v])-7!=2 for v in range(1,11)):raise ValueError('K_PROJECTION_RANK')
    rowsp={0:0}
    for i,g in enumerate(rb):
        for r,mask in tuple(rowsp.items()):rowsp[r^g]=mask^(1<<i)
    lambdas=[rowsp[g] for g in constraints]
    def project(c):return sum(((c&r).bit_count()&1)<<i for i,r in enumerate(rb))
    def off(s,v):
        return sum((s>>j)&1 for j in occ[v] if j in ACTIVE and triangles[j].index(v)==2)%2
    def gbits(s,r):
        return sum(((((lambdas[v-1]&r).bit_count()&1)^off(s,v)))<<(v-1) for v in range(1,11))
    synd=[0]*16
    for h in range(16):
        for j in range(4):
            if h&(1<<j):synd[h] ^= BASIS[j]
    if len(set(synd))!=16:raise ValueError('H_RANK')
    spec=spec_from_file_location('quotientsearch',QS);qs=module_from_spec(spec);spec.loader.exec_module(qs)
    stars,reps,kernels=qs.precompute(triangles);spans={v:qs.span(kernels[v]) for v in range(1,11)}
    deltas={}
    for s in synd[1:]:
        values=set()
        for v in range(1,11):
            if not s&stars[v]:continue
            r=0
            for j in range(10):
                if s&(1<<j):r ^= reps[v][j]
            values.update(project(r^k) for k in spans[v])
        if not values:raise ValueError(('NO_BAD_SYNDROME',s))
        deltas[s]=values
    candidates=[(h,r,gbits(synd[h],r)) for h in range(16) for r in range(128)
                if gbits(synd[h],r).bit_count()<=3]
    choose=[Bool('class_'+str(i)) for i in range(len(candidates))]
    solver=Solver();solver.set(timeout=TIMEOUT_MS)
    solver.add(PbEq([(x,1) for x in choose],16))
    for v in range(10):solver.add(PbLe([(choose[i],1) for i,(_,_,g) in enumerate(candidates) if g&(1<<v)],2))
    solver.add(PbLe([(choose[i],g.bit_count()) for i,(_,_,g) in enumerate(candidates) if g],20))
    edges=0
    for i,(h,r,_) in enumerate(candidates):
        for j in range(i+1,len(candidates)):
            h2,r2,_=candidates[j]
            if h!=h2 and (r^r2) in deltas[synd[h]^synd[h2]]:
                solver.add(Or(Not(choose[i]),Not(choose[j])));edges+=1
    status=solver.check();out={'baseline_result_sha256':EXPECTED,'producer_dependency_sha256':sha256(QS.read_bytes()).hexdigest(),
         'active_triangles':ACTIVE,'syndrome_basis':BASIS,'quotient_dimension':7,'K_dimension':13,
         'K_vertex_image_ranks':[rank(rb+forms[v])-7 for v in range(1,11)],'quotient_basis_rows':rb,
         'local_form_lambdas':lambdas,'candidate_g_weight_at_most':3,'candidate_classes':len(candidates),
         'pair_conflict_constraints':edges,'per_vertex_g_ones_max':2,'target_quotient_classes':16,
         'timeout_ms':TIMEOUT_MS,'solver_status':str(status),'delta_sizes':{str(s):len(d) for s,d in deltas.items()},
         'limits':'SAT is provisional until independent exact graph/linear checks; UNSAT concerns only this H and candidate weight/cap class, not general laws.'}
    if status==sat:
        model=solver.model();chosen=[list(candidates[i]) for i,x in enumerate(choose) if is_true(model.eval(x,model_completion=True))]
        counts=[sum(g>>v&1 for _,_,g in chosen) for v in range(10)]
        if len(chosen)!=16 or max(counts)>2:raise ValueError('MODEL')
        for (h,r,_),(h2,r2,_) in combinations(chosen,2):
            if h!=h2 and r^r2 in deltas[synd[h]^synd[h2]]:raise ValueError('MODEL_CONFLICT')
        out['selected_classes_h_r_g']=chosen;out['vertex_g_ones']=counts
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
