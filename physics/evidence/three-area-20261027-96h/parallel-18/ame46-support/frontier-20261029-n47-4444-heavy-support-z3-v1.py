#!/usr/bin/env python3
"""Uncertified E-support diagnostics for N47,t27,n9, residual alphabet4444.

Every local degree vector is (2,2,2,3); heavy excess vector sums to2 and is
j-independent. Cases are split S0(h0=h3=1), split S1(h0=h1=1), merged M0(h3=2),
merged M1(h0=2); at most one party is merged. All thirteen type multisets are
covered up to party permutations. SAT models are SUPPORT ONLY, not AME states;
UNSAT reports are NOT proof certificates.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

DEG=(2,2,2,3)
TYPES={'S0':(1,0,0,1),'S1':(1,1,0,0),'M0':(0,0,0,2),'M1':(2,0,0,0)}
Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));IDX=list(itertools.product(range(4),repeat=2))


def cases():
    out=[]
    for k in range(5):out.append(['S0']*k+['S1']*(4-k))
    for m in ('M0','M1'):
        for k in range(4):out.append([m]+['S0']*k+['S1']*(3-k))
    return out


def cell(E,A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def check_model(S,typ):
    if len(S)!=20 or len(set(S))!=20:raise ValueError('wrong support cardinality')
    for i in range(4):
        if [sum(q[i]==a for q in S) for a in range(4)]!=[2*DEG[a]+TYPES[typ[i]][a] for a in range(4)]:raise ValueError('fiber cardinality mismatch')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in S)
        if len(C)!=9 or Counter(C.values())!={2:7,3:2}:raise ValueError('pair projection multiplicities')
        for a in range(4):
            if sum((a,b) in C for b in range(4))!=DEG[a] or sum(C[a,b]==3 for b in range(4))!=TYPES[typ[i]][a]:raise ValueError('left degree/heavy mismatch')
            if sum((b,a) in C for b in range(4))!=DEG[a] or sum(C[b,a]==3 for b in range(4))!=TYPES[typ[j]][a]:raise ValueError('right degree/heavy mismatch')
    components=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in S:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
        if any(len(x&y)==1 for M in (rows,cols) for x,y in itertools.combinations(M.values(),2)):raise ValueError('unique overlap')
        remaining=set(rows);shapes=[]
        while remaining:
            rr={next(iter(remaining))};cc=set()
            while True:
                cc=set().union(*(rows[r] for r in rr));grow=set().union(*(cols[c] for c in cc))
                if grow==rr:break
                rr=grow
            shapes.append((len(rr),len(cc),sum(len(rows[r]) for r in rr)));remaining-=rr
        components.append(sorted(shapes))
    return components


def solve(typ,timeout):
    E={q:z3.Bool('w'+''.join(map(str,q))) for q in Q};S=z3.Solver();S.set(timeout=timeout)
    S.add(z3.PbEq([(v,1) for v in E.values()],20))
    for i in range(4):
        for a in range(4):S.add(z3.PbEq([(v,1) for q,v in E.items() if q[i]==a],2*DEG[a]+TYPES[typ[i]][a]))
    for i,j in PAIRS:
        pair={};heavy={}
        for a,b in IDX:
            pp=z3.Bool(f'pair{i}{j}_{a}{b}');hh=z3.Bool(f'heavy{i}{j}_{a}{b}');pair[a,b]=pp;heavy[a,b]=hh
            cells=[(v,1) for q,v in E.items() if (q[i],q[j])==(a,b)]
            S.add(z3.Or(z3.And(z3.Not(pp),z3.Not(hh),z3.PbEq(cells,0)),
                        z3.And(pp,z3.Not(hh),z3.PbEq(cells,2)),z3.And(pp,hh,z3.PbEq(cells,3))))
        for a in range(4):
            S.add(z3.PbEq([(pair[a,b],1) for b in range(4)],DEG[a]),z3.PbEq([(pair[b,a],1) for b in range(4)],DEG[a]))
            S.add(z3.PbEq([(heavy[a,b],1) for b in range(4)],TYPES[typ[i]][a]),z3.PbEq([(heavy[b,a],1) for b in range(4)],TYPES[typ[j]][a]))
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);G={(r,c):cell(E,A,r,B,c) for r in IDX for c in IDX}
        for r in IDX:
            for c,d in itertools.combinations(IDX,2):
                S.add(z3.Implies(z3.And(G[r,c],G[r,d]),z3.Or(*[z3.And(G[t,c],G[t,d]) for t in IDX if t!=r])))
    ans=S.check();record={'types':typ,'status':str(ans)}
    if ans==z3.sat:
        m=S.model();points=sorted(q for q,v in E.items() if z3.is_true(m.eval(v,model_completion=True)))
        record['support']=points;record['direct_component_checks']=check_model(points,typ)
    elif ans==z3.unknown:record['reason_unknown']=S.reason_unknown()
    return record


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);ap.add_argument('--timeout-ms',type=int,default=10000);ap.add_argument('--case',type=int);a=ap.parse_args()
    selected=cases() if a.case is None else [cases()[a.case]];result=[]
    for typ in selected:
        rec=solve(typ,a.timeout_ms);result.append(rec)
        print(json.dumps({k:v for k,v in rec.items() if k!='support'}),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'cases':result,'scope':'Uncertified E-support diagnostic; no amplitudes or P completion.'},f,indent=2);f.write('\n')


if __name__=='__main__':main()
