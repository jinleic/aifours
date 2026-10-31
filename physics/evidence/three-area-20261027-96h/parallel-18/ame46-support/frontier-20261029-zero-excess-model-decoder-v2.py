#!/usr/bin/env python3
"""Decode a SAT model of a zero-excess residual CNF (any n) and check it exactly.

v2 differs from frontier-20261029-n48-t24-model-decoder-v1.py only in replacing
the fixed sizes |E|=24, n=12, six blocks per cut, |P|=24 by |E|=2n, n, n/2 and
t=36-n, with n read from the degree vectors (n=sum of party-0 degrees).

Independently of the encoder: verify the zero-excess residual axioms directly,
apply the explicit integer phase engine, and if phases fail extract a minimal
infeasible block subsystem by greedy deletion (each step an exact integer test).
With a P code present and phases solvable, build the literal tensor and check
all3888 Gram entries in cyclotomic arithmetic. Output is exclusive.
"""
import argparse
from collections import Counter,defaultdict
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def load(path):
    s=importlib.util.spec_from_file_location('phase_engine',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def model_true(path):
    true=set();status=None
    for line in path.read_text().splitlines():
        if line.startswith('s '):status=line[2:].strip()
        if line.startswith('v '):true.update(int(t) for t in line[2:].split() if int(t)>0)
    return status,true


def residual_blocks(E,n):
    E=sorted(E)
    if len(E)!=2*n or len(set(E))!=2*n:raise ValueError('E size')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in E)
        if len(C)!=n or set(C.values())!={2}:raise ValueError('pair multiplicity')
    out=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);R=defaultdict(set)
        for q in E:R[tuple(q[i] for i in A)].add(tuple(q[i] for i in B))
        seen=set();one=[]
        for r in sorted(R):
            if r in seen:continue
            partners=[s for s in R if s!=r and R[r]&R[s]]
            if len(partners)!=1 or R[partners[0]]!=R[r] or len(R[r])!=2:raise ValueError('not full2x2 blocks')
            s=partners[0];seen|={r,s};c,d=sorted(R[r]);terms=[]
            for rr,cc in ((r,c),(r,d),(s,c),(s,d)):
                q=[0]*4
                for i,x in zip(A,rr):q[i]=x
                for i,x in zip(B,cc):q[i]=x
                terms.append(tuple(q))
            one.append(tuple(terms))
        if 2*len(one)!=n:raise ValueError('block count')
        out.append(one)
    return out


def feasible(engine,blist):
    bl=[[b for c,b in blist if c==k] for k in range(3)];words=sorted({w for c,b in blist for w in b})
    res,sol=engine.solve(words,[],bl);return res['complex_phase_solvable'],res,sol


def minimal_infeasible(engine,bl):
    cur=[(k,b) for k in range(3) for b in bl[k]];i=0
    while i<len(cur):
        trial=cur[:i]+cur[i+1:]
        if trial and not feasible(engine,trial)[0]:cur=trial
        else:i+=1
    for i in range(len(cur)):
        if not feasible(engine,cur[:i]+cur[i+1:])[0]:raise ValueError('not minimal')
    return cur


def six_word_type(blocks):
    words=sorted({w for c,b in blocks for w in b})
    if len(blocks)!=3 or len(words)!=6 or sorted(c for c,b in blocks)!=[0,1,2]:return False
    vals=[sorted({w[i] for w in words}) for i in range(4)]
    if any(len(v)!=2 for v in vals):return False
    bits=[tuple(v.index(w[i]) for i,v in enumerate(vals)) for w in words]
    par={sum(b)%2 for b in bits}
    if len(par)!=1:return False
    cls=[b for b in itertools.product((0,1),repeat=4) if sum(b)%2==par.pop()]
    missing=[b for b in cls if b not in bits]
    return len(missing)==2 and all(x!=y for x,y in zip(*missing))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('meta',type=Path);ap.add_argument('model',type=Path);ap.add_argument('phase_engine',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    meta=json.loads(a.meta.read_text());deg=[tuple(D) for D in meta['degrees']];sizes=[len(D) for D in deg];n=sum(deg[0])
    if any(sum(D)!=n for D in deg):raise ValueError('degree sums differ')
    Q=list(itertools.product(*(range(r) for r in sizes)));status,true=model_true(a.model)
    rec={'meta_sha256':hashlib.sha256(a.meta.read_bytes()).hexdigest(),'model_sha256':hashlib.sha256(a.model.read_bytes()).hexdigest(),'solver_status':status}
    if status!='SATISFIABLE':
        rec['note']='No model to decode.'
    else:
        E=[q for k,q in enumerate(Q) if k+1 in true]
        for i,D in enumerate(deg):
            if [sum(q[i]==s for q in E) for s in range(len(D))]!=[2*d for d in D]:raise ValueError('fiber sizes')
        if meta['no_H1_imposed'] and any(sum(x!=y for x,y in zip(u,v))==1 for u,v in itertools.combinations(E,2)):raise ValueError('distance one')
        bl=residual_blocks(E,n);engine=load(a.phase_engine);ok,res,sol=feasible(engine,[(k,b) for k in range(3) for b in bl[k]])
        rec.update({'E_support':E,'phase_result':res})
        if not ok:
            m=minimal_infeasible(engine,bl);rec['minimal_infeasible_blocks']=[[c,list(b)] for c,b in m]
            rec['minimal_infeasible_is_six_word_type']=six_word_type(m)
        if meta.get('joint_P'):
            base=len(Q);P=[q for k,q in enumerate(itertools.product(range(6),repeat=4)) if base+k+1 in true]
            for i,j in PAIRS:
                ep={(q[i],q[j]) for q in E};pp=[(q[i],q[j]) for q in P]
                if len(P)!=36-n or len(set(pp))!=36-n or set(pp)&ep or set(pp)|ep!=set(itertools.product(range(6),repeat=2)):raise ValueError('P cover')
            rec['P_words']=P
            if ok:
                L,expo=sol;rec['exact_Gram_entries']=engine.verify_exact(E,P,L,expo);rec['L']=L;rec['E_exponents']=[[q,expo[q]] for q in E]
                rec['CANDIDATE_AME_SUPPORT']=len(E)+len(P)
    rec['scope']='Exact checks of one solver model; no claim about other models or UNSAT cases.'
    with a.out.open('x',encoding='utf-8') as f:json.dump(rec,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('E_support','P_words','E_exponents')},indent=1))


if __name__=='__main__':main()
