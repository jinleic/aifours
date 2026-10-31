#!/usr/bin/env python3
"""Necessary-support CNF for N48/t28 (n8 E pair values per system, |E|=20).

E indicators first (lexicographic on the residual box). Encoded NECESSARY
conditions, each a separately written elementary fact:
  * every pair system has exactly8 E-carried values, each with2..4 extensions
    (excess4 per cut; a pair value carried once would be a maximal row);
  * per-symbol partner degree d_i(a) in every pair system containing i;
  * |E|=20;
  * unique-overlap rule in every cut: two rows (columns) never share exactly one
    nonzero column (row);
  * optional --joint-P: the28-word P code covers every non-E pair value of all
    six pair systems exactly once and no E pair value.
No amplitudes or component classification are encoded; SAT models are only
candidates for the separate decoder; checked UNSAT certifies this CNF only.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

BASE_ENCODER=Path(__file__).with_name('frontier-20261029-n47-heavy-support-cnf-v1.py')
PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def encoder_class(path=BASE_ENCODER):
    s=importlib.util.spec_from_file_location('base_heavy_encoder',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.Encoder


def qword(A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return tuple(q)


def parse_degrees(text):
    deg=[tuple(map(int,x.split(','))) for x in text.split('/')]
    if len(deg)!=4:raise ValueError('four degree vectors')
    for i,D in enumerate(deg):
        if sum(D)!=8 or min(D)<2:raise ValueError('degree vector')
        if max(D)>min(len(deg[j]) for j in range(4) if j!=i):raise ValueError('degree cap')
    return deg


def encode(deg,joint=False,base=BASE_ENCODER):
    en=encoder_class(base)();sizes=tuple(len(D) for D in deg);Q=list(itertools.product(*(range(r) for r in sizes)))
    E={q:en.var() for q in Q};P={q:en.var() for q in itertools.product(range(6),repeat=4)} if joint else {}
    en.exact(list(E.values()),20);Y={}
    for i,j in PAIRS:
        for a,b in itertools.product(range(sizes[i]),range(sizes[j])):
            xs=[E[q] for q in Q if (q[i],q[j])==(a,b)];y=en.var();Y[i,j,a,b]=y
            for x in xs:en.add(-x,y)
            en.add(-y,*xs);en.amk(xs,4)
            for k,x in enumerate(xs):en.add(-x,*[z for m,z in enumerate(xs) if m!=k])
        en.exact([Y[i,j,a,b] for a in range(sizes[i]) for b in range(sizes[j])],8)
        for a in range(sizes[i]):en.exact([Y[i,j,a,b] for b in range(sizes[j])],deg[i][a])
        for b in range(sizes[j]):en.exact([Y[i,j,a,b] for a in range(sizes[i])],deg[j][b])
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)))
        for side in (0,1):
            lines=RR if side==0 else CC;other=CC if side==0 else RR
            for r1,r2 in itertools.combinations(lines,2):
                both={};cells={}
                for c in other:
                    a,b=(E[qword(A,r1,B,c)],E[qword(A,r2,B,c)]) if side==0 else (E[qword(A,c,B,r1)],E[qword(A,c,B,r2)])
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


def main():
    ap=argparse.ArgumentParser();ap.add_argument('degrees');ap.add_argument('out',type=Path);ap.add_argument('--joint-P',action='store_true');a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    deg=parse_degrees(a.degrees);en,E,P=encode(deg,a.joint_P)
    with a.out.open('x',encoding='ascii') as f:
        f.write(f'p cnf {en.n} {len(en.C)}\n')
        for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
    meta={'degrees':deg,'joint_P':a.joint_P,'E_variables':f'1..{len(E)}','P_variables':(f'{len(E)+1}..{len(E)+len(P)}' if a.joint_P else None),
      'variables':en.n,'clauses':len(en.C),'encoder_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'base_encoder_sha256':hashlib.sha256(BASE_ENCODER.read_bytes()).hexdigest(),'cnf_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta,indent=2))


if __name__=='__main__':main()
