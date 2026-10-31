#!/usr/bin/env python3
"""Search 16 cosets yielding an exact biased q=8 entropy-ratio gain.

Only rank-10 images of ten local parity forms are considered. If each
pattern's two preimages conflict, the 16-class, <=2 occurrences per vertex
criterion forces one zero pattern, all ten singleton patterns and a perfect
matching of five weight-two patterns. SAT witnesses require independent
verification; UNSAT is a solver result for the individual sampled subspace.
"""
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
from random import Random
from time import monotonic
import json
from z3 import Bool,Not,Or,PbEq,Solver,is_true,sat

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
QS=ROOT/'frontier-20261028-multicoset-quotient-search.py'
OUTPUT=ROOT/'frontier-20261028-full-rank-marginal-search-result.json'
ACTIVE=(0,3,6,9)
MAX_SOLVES=10
CASE_TIMEOUT_MS=3000
MAX_SECONDS=50


def rank(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in piv:x ^= piv[k]
            else:piv[k]=x;break
    return len(piv)


def main():
    started=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    occ={v:[j for j,t in enumerate(triangles) if v in t] for v in range(1,11)}
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
    def off(s,v):return sum((s>>j)&1 for j in occ[v] if j in ACTIVE and triangles[j].index(v)==2)%2
    def gbits(s,r):return sum(((((lambdas[v-1]&r).bit_count()&1)^off(s,v)))<<(v-1) for v in range(1,11))
    spec=spec_from_file_location('quotientsearch',QS);qs=module_from_spec(spec);spec.loader.exec_module(qs)
    stars,reps,kernels=qs.precompute(triangles);spans={v:qs.span(kernels[v]) for v in range(1,11)};cache={}
    def delta(s):
        if s not in cache:
            values=set()
            for v in range(1,11):
                if not s&stars[v]:continue
                r=0
                for j in range(10):
                    if s&(1<<j):r ^= reps[v][j]
                values.update(project(r^k) for k in spans[v])
            cache[s]=values
        return cache[s]
    random=Random(2026102802);attempts=0;cases=[];candidate=None;anomaly=None
    while len(cases)<MAX_SOLVES and monotonic()-started<MAX_SECONDS:
        basis=tuple(random.sample(range(1,1024),4));attempts+=1
        if rank(basis)!=4:continue
        synd=[0]*16
        for h in range(16):
            for j in range(4):
                if h&(1<<j):synd[h] ^= basis[j]
        by_g={}
        for h,s in enumerate(synd):
            for r in range(128):by_g.setdefault(gbits(s,r),[]).append((h,r))
        if len(by_g)!=1024:continue
        if any(len(v)!=2 for v in by_g.values()):raise ValueError('G_PREIMAGE_COUNT')
        h0,r0=by_g[0][1];s0=synd[h0]
        if not h0 or r0 not in delta(s0):
            anomaly={'basis':basis,'zero_pattern_preimages':by_g[0],'syndrome':s0};break
        items=[(h,r,g) for g,pts in by_g.items() if g.bit_count()<=2 for h,r in pts]
        if len(items)!=112:raise ValueError('PATTERN_COUNT')
        select=[Bool('p'+str(i)) for i in range(len(items))];solver=Solver();solver.set(timeout=CASE_TIMEOUT_MS)
        solver.add(PbEq([(select[i],1) for i,(_,_,g) in enumerate(items) if g==0],1))
        for v in range(10):
            solver.add(PbEq([(select[i],1) for i,(_,_,g) in enumerate(items) if g==1<<v],1))
            solver.add(PbEq([(select[i],1) for i,(_,_,g) in enumerate(items)
                             if g.bit_count()==2 and g&(1<<v)],1))
        edges=0
        for i,(h,r,g) in enumerate(items):
            for j in range(i+1,len(items)):
                h2,r2,g2=items[j]
                if h!=h2 and (r^r2) in delta(synd[h]^synd[h2]):
                    solver.add(Or(Not(select[i]),Not(select[j])));edges+=1
        status=solver.check();entry={'syndrome_basis':basis,'pattern_image_rank':10,
              'candidate_classes':len(items),'edges':edges,'solver_status':str(status)}
        if status==sat:
            model=solver.model();chosen=[list(items[i]) for i,x in enumerate(select) if is_true(model.eval(x,model_completion=True))]
            if len(chosen)!=16 or any(sum((g>>v)&1 for _,_,g in chosen)!=2 for v in range(10)):
                raise ValueError('SOLVER_MODEL')
            for (h,r,_),(h2,r2,_) in combinations(chosen,2):
                if h!=h2 and (r^r2) in delta(synd[h]^synd[h2]):raise ValueError('MODEL_CONFLICT')
            entry['selected_classes_h_r_g']=chosen;candidate=entry
        cases.append(entry)
        if candidate:break
    out={'baseline_result_sha256':EXPECTED,'dependency_sha256':sha256(QS.read_bytes()).hexdigest(),
         'active_triangles':ACTIVE,'K_rank':13,'K_vertex_image_ranks':[2]*10,
         'quotient_basis_rows':rb,'local_form_lambdas':lambdas,'random_seed':2026102802,
         'attempts':attempts,'cases':cases,'candidate_found':candidate is not None,'anomaly':anomaly,
         'elapsed_seconds':monotonic()-started,'case_timeout_ms':CASE_TIMEOUT_MS,
         'limits':'Anomaly/SAT needs an independent original-graph verification; UNSAT concerns only the sampled H and this fixed K/16-class equal-weight target.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
