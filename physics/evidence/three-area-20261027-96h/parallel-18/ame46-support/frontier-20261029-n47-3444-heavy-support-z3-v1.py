#!/usr/bin/env python3
"""Uncertified necessary-support diagnostics for N47,t27,n9, residual alph3444.

Party A: degree vector234 or333; heavy-excess sum2, normalized within equal-degree
classes. Parties B,C,D: degree2223 and types S0/S1/M0/M1. At most one merged party.
Exactly56 party-type normal forms. SAT support is not an AME witness; UNSAT is
not an independent proof certificate. No phases or P-code completion encoded.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

B_TYPES={'S0':((2,2,2,3),(1,0,0,1)),'S1':((2,2,2,3),(1,1,0,0)),
         'M0':((2,2,2,3),(0,0,0,2)),'M1':((2,2,2,3),(2,0,0,0))}
A_TYPES={'U_S01':((2,3,4),(1,1,0)),'U_S02':((2,3,4),(1,0,1)),
         'U_S12':((2,3,4),(0,1,1)),'V_S':((3,3,3),(1,1,0)),
         'U_M0':((2,3,4),(2,0,0)),'U_M1':((2,3,4),(0,2,0)),
         'U_M2':((2,3,4),(0,0,2)),'V_M':((3,3,3),(2,0,0))}
PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));AL=(3,4,4,4)
Q=list(itertools.product(*(range(x) for x in AL)))


def cases():
    out=[]
    for A in ('U_S01','U_S02','U_S12','V_S'):
        for k in range(4):out.append([A]+['S0']*k+['S1']*(3-k))
        for M in ('M0','M1'):
            for k in range(3):out.append([A,M]+['S0']*k+['S1']*(2-k))
    for A in ('U_M0','U_M1','U_M2','V_M'):
        for k in range(4):out.append([A]+['S0']*k+['S1']*(3-k))
    if len(out)!=56:raise ValueError('case list')
    return out


def spec(typ):return [A_TYPES[typ[0]]]+[B_TYPES[x] for x in typ[1:]]


def cell(E,A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def verify(points,typ):
    sh=spec(typ)
    if len(points)!=20 or len(set(points))!=20:raise ValueError('support count')
    for i in range(4):
        d,h=sh[i]
        if [sum(q[i]==a for q in points) for a in range(AL[i])]!=[2*x+y for x,y in zip(d,h)]:raise ValueError('fiber counts')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in points)
        if len(C)!=9 or Counter(C.values())!={2:7,3:2}:raise ValueError('pair counts')
        for a in range(AL[i]):
            if (sum((a,b) in C for b in range(AL[j])),sum(C[a,b]==3 for b in range(AL[j])))!=(sh[i][0][a],sh[i][1][a]):raise ValueError('left d/h')
        for b in range(AL[j]):
            if (sum((a,b) in C for a in range(AL[i])),sum(C[a,b]==3 for a in range(AL[i])))!=(sh[j][0][b],sh[j][1][b]):raise ValueError('right d/h')
    shapes=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in points:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
        if any(len(x&y)==1 for D in (rows,cols) for x,y in itertools.combinations(D.values(),2)):raise ValueError('unique overlap')
        remain=set(rows);comp=[]
        while remain:
            rr={next(iter(remain))}
            while True:
                cc=set().union(*(rows[r] for r in rr));grow=set().union(*(cols[c] for c in cc))
                if rr==grow:break
                rr=grow
            comp.append((len(rr),len(cc),sum(len(rows[r]) for r in rr)));remain-=rr
        shapes.append(sorted(comp))
    return shapes


def solve(typ,timeout):
    sh=spec(typ);E={q:z3.Bool('e'+''.join(map(str,q))) for q in Q};S=z3.Solver();S.set(timeout=timeout)
    for i in range(4):
        for a in range(AL[i]):S.add(z3.PbEq([(v,1) for q,v in E.items() if q[i]==a],2*sh[i][0][a]+sh[i][1][a]))
    for i,j in PAIRS:
        IJ=list(itertools.product(range(AL[i]),range(AL[j])));Y={p:z3.Bool(f'y{i}{j}_{p[0]}{p[1]}') for p in IJ};H={p:z3.Bool(f'h{i}{j}_{p[0]}{p[1]}') for p in IJ}
        for a,b in IJ:
            terms=[(v,1) for q,v in E.items() if (q[i],q[j])==(a,b)]
            S.add(z3.Or(z3.And(z3.Not(Y[a,b]),z3.Not(H[a,b]),z3.PbEq(terms,0)),
              z3.And(Y[a,b],z3.Not(H[a,b]),z3.PbEq(terms,2)),z3.And(Y[a,b],H[a,b],z3.PbEq(terms,3))))
        for a in range(AL[i]):S.add(z3.PbEq([(Y[a,b],1) for b in range(AL[j])],sh[i][0][a]),z3.PbEq([(H[a,b],1) for b in range(AL[j])],sh[i][1][a]))
        for b in range(AL[j]):S.add(z3.PbEq([(Y[a,b],1) for a in range(AL[i])],sh[j][0][b]),z3.PbEq([(H[a,b],1) for a in range(AL[i])],sh[j][1][b]))
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(AL[i]) for i in A)));CC=list(itertools.product(*(range(AL[i]) for i in B)))
        G={(r,c):cell(E,A,r,B,c) for r in RR for c in CC}
        for r in RR:
            for c,d in itertools.combinations(CC,2):S.add(z3.Implies(z3.And(G[r,c],G[r,d]),z3.Or(*[z3.And(G[t,c],G[t,d]) for t in RR if t!=r])))
    ans=S.check();record={'types':typ,'status':str(ans)}
    if ans==z3.sat:
        M=S.model();points=sorted(q for q,v in E.items() if z3.is_true(M.eval(v,model_completion=True)));record['support']=points;record['direct_component_checks']=verify(points,typ)
    elif ans==z3.unknown:record['reason_unknown']=S.reason_unknown()
    return record


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--timeout-ms',type=int,default=10000);p.add_argument('--case',type=int);a=p.parse_args()
    selected=cases() if a.case is None else [cases()[a.case]];records=[]
    for typ in selected:
        r=solve(typ,a.timeout_ms);records.append(r);print(json.dumps({k:v for k,v in r.items() if k!='support'}),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'cases':records,'scope':'Uncertified support-only diagnostics, no phases/P completion.'},f,indent=2);f.write('\n')


if __name__=='__main__':main()
