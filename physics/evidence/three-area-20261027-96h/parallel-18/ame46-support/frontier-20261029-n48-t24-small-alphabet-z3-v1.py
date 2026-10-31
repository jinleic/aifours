#!/usr/bin/env python3
"""Uncertified necessary E-support diagnostics for four N48/t24 residual profiles.

Exactly24 residual positions; every pair is carried0 or2 times, local fiber sizes
2d(a) with d>=2,sum12. Conditional no-Hamming-one is explicitly imposed (using the
separately written exact-scope n12 lemma, not f127 outside its scope). Cut grids
must be unions of2x2 blocks. No complex phases or P-code completion are encoded.
SAT is SUPPORT ONLY; UNSAT is unverified solver output, not a theorem.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

D5={'X':(2,2,2,2,4),'Y':(2,2,2,3,3)}
D4={'A':(2,2,3,5),'B':(2,2,4,4),'C':(2,3,3,4),'D':(3,3,3,3)}
D3={'A':(3,4,5),'B':(4,4,4)}
PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def cases(profile):
    out=[]
    if profile=='3555':
        for a in D3:out.append(([D3[a]]+[D5['Y']]*3,[a,'Y','Y','Y']))
    elif profile=='4455':
        for a,b in itertools.combinations_with_replacement(('B','C','D'),2):
            for c,d in itertools.combinations_with_replacement(('X','Y'),2):out.append(([D4[a],D4[b],D5[c],D5[d]],[a,b,c,d]))
    elif profile=='4555':
        for a in D4:
            for k in range(4):out.append(([D4[a]]+[D5['X']]*k+[D5['Y']]*(3-k),[a]+['X']*k+['Y']*(3-k)))
    elif profile=='5555':
        for k in range(5):out.append(([D5['X']]*k+[D5['Y']]*(4-k),['X']*k+['Y']*(4-k)))
    else:raise ValueError('unknown profile')
    return out


def cell(E,A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def verify(E,deg):
    if len(E)!=24 or len(set(E))!=24:raise ValueError('residual cardinality')
    for i,D in enumerate(deg):
        if [sum(q[i]==a for q in E) for a in range(len(D))]!=[2*d for d in D]:raise ValueError('fiber cardinality')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in E)
        if len(C)!=12 or set(C.values())!={2}:raise ValueError('pair multiplicity')
    if any(sum(x!=y for x,y in zip(a,b))==1 for a,b in itertools.combinations(E,2)):raise ValueError('distance-one pair')
    blocks=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);R=defaultdict(set);C=defaultdict(set)
        for q in E:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);R[r].add(c);C[c].add(r)
        left=set(R);onecut=[]
        while left:
            r=min(left);cs=R[r];rs=set().union(*(C[c] for c in cs))
            if len(rs)!=2 or len(cs)!=2 or any(R[s]!=cs for s in rs):raise ValueError('not full2x2 blocks')
            left-=rs;terms=[]
            for rr,cc,sign in ((min(rs),min(cs),1),(min(rs),max(cs),-1),(max(rs),min(cs),-1),(max(rs),max(cs),1)):
                q=[0]*4
                for i,x in zip(A,rr):q[i]=x
                for i,x in zip(B,cc):q[i]=x
                terms.append((q,sign))
            onecut.append(terms)
        if len(onecut)!=6:raise ValueError('wrong block count')
        blocks.append(onecut)
    return blocks


def solve(deg,names,timeout):
    sizes=tuple(map(len,deg));Q=list(itertools.product(*(range(r) for r in sizes)));E={q:z3.Bool('q'+''.join(map(str,q))) for q in Q};S=z3.Solver();S.set(timeout=timeout)
    for i,D in enumerate(deg):
        for a,d in enumerate(D):S.add(z3.PbEq([(v,1) for q,v in E.items() if q[i]==a],2*d))
    for i,j in PAIRS:
        for a,b in itertools.product(range(sizes[i]),range(sizes[j])):
            terms=[(v,1) for q,v in E.items() if (q[i],q[j])==(a,b)];S.add(z3.Or(z3.PbEq(terms,0),z3.PbEq(terms,2)))
    # Conditional no-Hamming-one: fixing any three coordinates leaves at mostone.
    for free in range(4):
        fixed=tuple(i for i in range(4) if i!=free)
        for values in itertools.product(*(range(sizes[i]) for i in fixed)):
            S.add(z3.PbLe([(v,1) for q,v in E.items() if tuple(q[i] for i in fixed)==values],1))
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)))
        G={(r,c):cell(E,A,r,B,c) for r in RR for c in CC}
        for r in RR:
            for c,d in itertools.combinations(CC,2):S.add(z3.Implies(z3.And(G[r,c],G[r,d]),z3.Or(*[z3.And(G[t,c],G[t,d]) for t in RR if t!=r])))
    ans=S.check();rec={'degree_names':names,'degrees':deg,'status':str(ans)}
    if ans==z3.sat:
        M=S.model();support=sorted(q for q,v in E.items() if z3.is_true(M.eval(v,model_completion=True)))
        rec['support']=support;rec['directly_checked_blocks']=verify(support,deg)
    elif ans==z3.unknown:rec['reason_unknown']=S.reason_unknown()
    return rec


def main():
    ap=argparse.ArgumentParser();ap.add_argument('profile',choices=['3555','4455','4555','5555']);ap.add_argument('out',type=Path);ap.add_argument('--timeout-ms',type=int,default=15000);ap.add_argument('--case',type=int);a=ap.parse_args()
    C=cases(a.profile);selected=C if a.case is None else [C[a.case]];records=[]
    for d,names in selected:
        r=solve(d,names,a.timeout_ms);records.append(r);print(json.dumps({k:v for k,v in r.items() if k not in ('support','directly_checked_blocks')}),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'profile':a.profile,'cases':records,'scope':'Uncertified support-only diagnostics conditional on exact-scope n12 noH1; no phases/P completion.'},f,indent=2);f.write('\n')


if __name__=='__main__':main()
