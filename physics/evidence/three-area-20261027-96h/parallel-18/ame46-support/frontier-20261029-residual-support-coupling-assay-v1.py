#!/usr/bin/env python3
"""Turn individual SAT residual supports into exact phase/code assays.

For each support24 on the residual12x12 zero-excess shape:
 * independently reconstruct all2x2 block equations;
 * solve complex phase congruences via the explicitly supplied integer engine;
 * if phases exist, exact-cover the complement pair universe with24 P words;
 * only a FOUND classical cover + complete exact cyclotomic Gram check is labeled
   an AME candidate. A bounded search is UNKNOWN, not INFEASIBLE.
This is an individual-instance assay, not a global support theorem.
"""
import argparse
from collections import Counter,defaultdict
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def load(path):
    s=importlib.util.spec_from_file_location('phase_engine',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def reconstruct(E):
    E=sorted(tuple(q) for q in E)
    if len(E)!=24 or len(set(E))!=24:raise ValueError('wrong residual support size')
    if any(len(q)!=4 or any(type(v)!=int or not 0<=v<6 for v in q) for q in E):raise ValueError('bad residual coordinate')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in E)
        if len(C)!=12 or set(C.values())!={2}:raise ValueError('residual pair projection/multiplicity')
    bl=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);R=defaultdict(set)
        for q in E:R[tuple(q[i] for i in A)].add(tuple(q[i] for i in B))
        seen=set();one=[]
        for r in sorted(R):
            if r in seen:continue
            partners=[s for s in R if s!=r and R[r]&R[s]]
            if len(partners)!=1 or R[partners[0]]!=R[r] or len(R[r])!=2:raise ValueError('not full2x2 residual blocks')
            s=partners[0];seen|={r,s};c,d=sorted(R[r]);terms=[]
            for rr,cc in ((r,c),(r,d),(s,c),(s,d)):
                q=[0]*4
                for i,x in zip(A,rr):q[i]=x
                for i,x in zip(B,cc):q[i]=x
                terms.append(tuple(q))
            one.append(tuple(terms))
        if len(one)!=6:raise ValueError('residual block count')
        bl.append(one)
    return E,bl


def exact_cover(E,node_limit,seconds):
    E_pairs={ij:{(q[ij[0]],q[ij[1]]) for q in E} for ij in PAIRS}
    universe=[(i,j,a,b) for i,j in PAIRS for a,b in itertools.product(range(6),repeat=2) if (a,b) not in E_pairs[i,j]]
    if len(universe)!=144:raise ValueError('complement universe size')
    uid={x:i for i,x in enumerate(universe)};candidates=[];masks=[];rows=[0]*144
    for q in itertools.product(range(6),repeat=4):
        if any((q[i],q[j]) in E_pairs[i,j] for i,j in PAIRS):continue
        mask=0
        for i,j in PAIRS:mask|=1<<uid[i,j,q[i],q[j]]
        if mask.bit_count()!=6:raise ValueError('word coverage size')
        idx=len(candidates);candidates.append(q);masks.append(mask)
        for u in range(144):
            if mask>>u&1:rows[u]|=1<<idx
    start=time.monotonic();nodes=0;stopped=False;answer=None
    def search(uncovered,available,chosen):
        nonlocal nodes,stopped,answer
        nodes+=1
        if nodes>node_limit or time.monotonic()-start>seconds:stopped=True;return False
        if not uncovered:answer=chosen[:];return True
        best=None;bestcount=10**9;todo=uncovered
        while todo:
            bit=todo&-todo;u=bit.bit_length()-1;todo-=bit;opts=rows[u]&available;c=opts.bit_count()
            if not c:return False
            if c<bestcount:best=opts;bestcount=c
            if c==1:break
        while best:
            bit=best&-best;idx=bit.bit_length()-1;best-=bit;cover=masks[idx]
            if cover&~uncovered:raise ValueError('available word overlaps covered universe')
            conflict=0;bits=cover
            while bits:
                ubit=bits&-bits;u=ubit.bit_length()-1;bits-=ubit;conflict|=rows[u]
            if search(uncovered^cover,available&~conflict,chosen+[idx]):return True
            if stopped:return False
        return False
    found=search((1<<144)-1,(1<<len(candidates))-1,[])
    result={'candidate_P_words':len(candidates),'nodes':nodes,'monotonic_seconds':time.monotonic()-start,
      'status':'FOUND' if found else 'UNKNOWN' if stopped else 'COMPLETE_INFEASIBLE'}
    if found:
        P=[candidates[i] for i in answer]
        if len(P)!=24:raise ValueError('cover word count')
        for i,j in PAIRS:
            actual={(q[i],q[j]) for q in P}
            if len(actual)!=24 or actual|E_pairs[i,j]!=set(itertools.product(range(6),repeat=2)) or actual&E_pairs[i,j]:raise ValueError('P cover direct binding')
        result['P_words']=P
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('diagnostics',type=Path);ap.add_argument('phase_engine',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--node-limit',type=int,default=1000000);ap.add_argument('--seconds',type=float,default=30);a=ap.parse_args()
    data=a.diagnostics.read_bytes();source=json.loads(data);engine=load(a.phase_engine);records=[]
    for case in source['cases']:
        if case['status']!='sat':continue
        E,bl=reconstruct(case['support']);phase,solution=engine.solve(E,[],bl);r={'degree_names':case.get('degree_names'),'E_support':E,'phase_result':phase}
        if solution is not None:
            L,expo=solution;r['phase_denominator_L']=L
            cover=exact_cover(E,a.node_limit,a.seconds);r['complement_exact_cover']=cover
            if cover['status']=='FOUND':
                P=[tuple(q) for q in cover['P_words']];checks=engine.verify_exact(E,P,L,expo)
                r.update({'is_exact_AME_candidate':True,'support':48,'exact_cyclotomic_Gram_entries_checked':checks,
                  'tensor':{'normalization':'E:zeta_L^a/sqrt72;P:1/6','L':L,'E_words_exponents':[[q,expo[q]] for q in E],'P_words':P}})
        records.append(r);print(json.dumps({k:v for k,v in r.items() if k not in ('E_support','tensor')}),flush=True)
    result={'diagnostics_sha256':hashlib.sha256(data).hexdigest(),'phase_engine_sha256':hashlib.sha256(a.phase_engine.read_bytes()).hexdigest(),
      'records':records,'scope':'Individual exact phase/code/Gram assays; any new witness needs independent complete checking and review. No global theorem.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')


if __name__=='__main__':main()
