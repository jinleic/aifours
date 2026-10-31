#!/usr/bin/env python3
"""Controls for the frozen N48/t28 support encoder (not a proof).

(1) A parametric re-implementation general(deg,n,size,maxmult,joint) is checked
    to emit a clause list IDENTICAL (same order) to the frozen encoder for all
    five t28 cases, with and without --joint-P.
(2) The parametric version with the exactly verified60-term AME support
    (t12, n24, |E|48, multiplicity2, its own partner degrees) plus unit clauses
    fixing its E and P words must be SATISFIABLE (kissat); the same with one P
    word replaced by a word repeating P[0]'s (0,1) pair value must be UNSAT. (v1 of this file
    crashed before writing any receipt because it misread the witness fields.)
This validates the pair-partition/P-code/unique-overlap encodings on a real
AME instance. It does not certify the t28 UNSAT results or their scope.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def general(enc,deg,n,size,maxmult,joint):
    en=enc.encoder_class()();sizes=tuple(len(D) for D in deg);Q=list(itertools.product(*(range(r) for r in sizes)))
    E={q:en.var() for q in Q};P={q:en.var() for q in itertools.product(range(6),repeat=4)} if joint else {}
    en.exact(list(E.values()),size);Y={}
    for i,j in PAIRS:
        for a,b in itertools.product(range(sizes[i]),range(sizes[j])):
            xs=[E[q] for q in Q if (q[i],q[j])==(a,b)];y=en.var();Y[i,j,a,b]=y
            for x in xs:en.add(-x,y)
            en.add(-y,*xs);en.amk(xs,maxmult)
            for k,x in enumerate(xs):en.add(-x,*[z for m,z in enumerate(xs) if m!=k])
        en.exact([Y[i,j,a,b] for a in range(sizes[i]) for b in range(sizes[j])],n)
        for a in range(sizes[i]):en.exact([Y[i,j,a,b] for b in range(sizes[j])],deg[i][a])
        for b in range(sizes[j]):en.exact([Y[i,j,a,b] for a in range(sizes[i])],deg[j][b])
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)))
        for side in (0,1):
            lines=RR if side==0 else CC;other=CC if side==0 else RR
            for r1,r2 in itertools.combinations(lines,2):
                both={};cells={}
                for c in other:
                    a,b=(E[enc.qword(A,r1,B,c)],E[enc.qword(A,r2,B,c)]) if side==0 else (E[enc.qword(A,c,B,r1)],E[enc.qword(A,c,B,r2)])
                    v=en.var();both[c]=v;cells[c]=(a,b);en.add(-v,a);en.add(-v,b);en.add(v,-a,-b)
                for c in other:
                    a,b=cells[c];en.add(-a,-b,*[v for t,v in both.items() if t!=c])
    if joint:
        for i,j in PAIRS:
            for a,b in itertools.product(range(6),repeat=2):
                ps=[v for q,v in P.items() if (q[i],q[j])==(a,b)];y=Y.get((i,j,a,b));en.amk(ps,1)
                if y is None:en.add(*ps)
                else:
                    en.add(y,*ps)
                    for v in ps:en.add(-v,-y)
    return en,E,P


def solve(path):
    r=subprocess.run(['kissat','-q','--time=600',str(path)],capture_output=True,text=True)
    return r.returncode,[l for l in r.stdout.split('\n') if l.startswith('s ')]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('batch',type=Path);ap.add_argument('witness',type=Path);ap.add_argument('workdir',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    enc=load('enc',a.encoder);batch=load('batch',a.batch);ident=[]
    for name,deg in batch.CASES:
        for joint in (False,True):
            e1,_,_=enc.encode([tuple(D) for D in deg],joint);e2,_,_=general(enc,[tuple(D) for D in deg],8,20,4,joint)
            same=(e1.n==e2.n and e1.C==e2.C)
            if not same:raise ValueError(f'encoder identity failed {name} {joint}')
            ident.append({'case':name,'joint_P':joint,'variables':e1.n,'clauses':len(e1.C),'identical':same})
    W=json.loads(a.witness.read_text());E=[tuple(q) for q,_ in W['witness']['E_words_and_zeta_L_exponents']];P=[tuple(q) for q in W['witness']['P_words_coefficient_one_sixth']]
    if len(E)!=48 or len(P)!=12 or W.get('E')!=48 or W.get('P')!=12 or not W.get('exact_AME_verified'):raise ValueError('witness record')
    alph=[sorted({q[i] for q in E}) for i in range(4)]
    if any(al!=list(range(len(al))) for al in alph):raise ValueError('witness E alphabet not initial segment; relabel needed')
    deg=[]
    for i in range(4):
        j=(i+1)%4;deg.append(tuple(len({q[j] for q in E if q[i]==s}) for s in alph[i]))
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in E)
        if len(C)!=24 or set(C.values())!={2}:raise ValueError('witness multiplicity')
    a.workdir.mkdir(exist_ok=True);controls=[]
    for label,units_P in (('witness',P),('mutant_duplicate_pair',P[:-1]+[(P[0][0],P[0][1],(P[0][2]+1)%6,(P[0][3]+1)%6)])):
        en,EV,PV=general(enc,deg,24,48,2,True)
        units=[EV[q] if q in set(E) else -EV[q] for q in EV]+[PV[q] if q in set(units_P) else -PV[q] for q in PV]
        path=a.workdir/f'control-{label}.cnf'
        if path.exists():raise ValueError('exists')
        with path.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)+len(units)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
            for u in units:f.write(f'{u} 0\n')
        rc,st=solve(path);controls.append({'label':label,'rc':rc,'status':st,'cnf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'degrees':deg})
    if controls[0]['rc']!=10 or controls[1]['rc']!=20:raise ValueError(f'positive/negative control failed {controls}')
    rec={'identity':ident,'witness_controls':controls,'encoder_sha256':hashlib.sha256(a.encoder.read_bytes()).hexdigest(),'witness_sha256':hashlib.sha256(a.witness.read_bytes()).hexdigest(),
      'scope':'Encoder identity and a real-AME positive control plus one mutation; not a proof of any UNSAT scope.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(rec,f,indent=2);f.write('\n')
    print(json.dumps(rec,indent=1))


if __name__=='__main__':main()
