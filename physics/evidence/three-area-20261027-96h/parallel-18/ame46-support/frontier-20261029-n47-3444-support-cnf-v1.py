#!/usr/bin/env python3
"""Necessary-support CNF for N47/t27/n9 residual alphabet3444.

Imports only the already-pinned standard-library Encoder cardinality primitive.
The input base encoder path is explicit when called as CLI. For programmatic
batch use BASE_ENCODER defaults to the neighboring frozen heavy-support source.
No amplitudes, P-code completion or mathematical theorem is encoded.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

BASE_ENCODER=Path(__file__).with_name('frontier-20261029-n47-heavy-support-cnf-v1.py')
A_TYPES={'U_S01':((2,3,4),(1,1,0)),'U_S02':((2,3,4),(1,0,1)),'U_S12':((2,3,4),(0,1,1)),
 'V_S':((3,3,3),(1,1,0)),'U_M0':((2,3,4),(2,0,0)),'U_M1':((2,3,4),(0,2,0)),
 'U_M2':((2,3,4),(0,0,2)),'V_M':((3,3,3),(2,0,0))}
B_TYPES={'S0':((2,2,2,3),(1,0,0,1)),'S1':((2,2,2,3),(1,1,0,0)),
 'M0':((2,2,2,3),(0,0,0,2)),'M1':((2,2,2,3),(2,0,0,0))}
AL=(3,4,4,4);Q=list(itertools.product(*(range(x) for x in AL)))
PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


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


def encoder_class():
    s=importlib.util.spec_from_file_location('base_heavy_encoder',BASE_ENCODER);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.Encoder


def cell(E,A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def encode(typ,overlap=True):
    en=encoder_class()();spec=[A_TYPES[typ[0]]]+[B_TYPES[x] for x in typ[1:]];E={q:en.var() for q in Q}
    for i in range(4):
        for a in range(AL[i]):en.exact([E[q] for q in Q if q[i]==a],2*spec[i][0][a]+spec[i][1][a])
    for i,j in PAIRS:
        IJ=list(itertools.product(range(AL[i]),range(AL[j])));Y={p:en.var() for p in IJ};H={p:en.var() for p in IJ}
        for a,b in IJ:
            xs=[E[q] for q in Q if (q[i],q[j])==(a,b)];y=Y[a,b];h=H[a,b]
            for x in xs:en.add(-x,y)
            en.add(-y,*xs);en.add(-h,y)
            for omitted in range(len(xs)):en.add(-y,*[x for k,x in enumerate(xs) if k!=omitted])
            en.amk(xs,3)
            for aa,bb in itertools.combinations(range(len(xs)),2):en.add(-h,*[x for k,x in enumerate(xs) if k not in (aa,bb)])
            for tri in itertools.combinations(xs,3):en.add(*[-x for x in tri],h)
        for a in range(AL[i]):en.exact([Y[a,b] for b in range(AL[j])],spec[i][0][a]);en.exact([H[a,b] for b in range(AL[j])],spec[i][1][a])
        for b in range(AL[j]):en.exact([Y[a,b] for a in range(AL[i])],spec[j][0][b]);en.exact([H[a,b] for a in range(AL[i])],spec[j][1][b])
    if overlap:
        for A in CUTS:
            B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(AL[i]) for i in A)));CC=list(itertools.product(*(range(AL[i]) for i in B)))
            for side in (0,1):
                lines=RR if side==0 else CC;other=CC if side==0 else RR
                for r1,r2 in itertools.combinations(lines,2):
                    both={};cells={}
                    for c in other:
                        a,b=(cell(E,A,r1,B,c),cell(E,A,r2,B,c)) if side==0 else (cell(E,A,c,B,r1),cell(E,A,c,B,r2))
                        v=en.var();both[c]=v;cells[c]=(a,b);en.add(-v,a);en.add(-v,b)
                    for c in other:
                        a,b=cells[c];en.add(-a,-b,*[v for t,v in both.items() if t!=c])
    return en,E


def main():
    ap=argparse.ArgumentParser();ap.add_argument('case',type=int);ap.add_argument('out',type=Path);ap.add_argument('--no-overlap',action='store_true');a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    typ=cases()[a.case];en,E=encode(typ,not a.no_overlap)
    with a.out.open('x',encoding='ascii') as f:
        f.write(f'p cnf {en.n} {len(en.C)}\n')
        for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
    meta={'case':a.case,'types':typ,'base_encoder_sha256':hashlib.sha256(BASE_ENCODER.read_bytes()).hexdigest(),
      'variables':en.n,'clauses':len(en.C),'E_variables':'first192, lex order on3x4x4x4',
      'cnf_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest(),'no_unique_overlap':not a.no_overlap}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta,indent=2))


if __name__=='__main__':main()
