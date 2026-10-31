#!/usr/bin/env python3
"""P-code-only relaxation for t=28 (n=8), independent of the total support N.

Variables: Y_ij(a,b) for (a,b) in A_i x A_j (E-carried pattern of each of the six
pair systems, NOT tied to any E words), then P indicators on {0..5}^4.
Constraints (all necessary for every AME state with t=28, any N):
  * each system has exactly8 E-carried values, row sums d_i(a), column sums d_j(b);
  * the P code carries every non-E value of every system exactly once and no
    E value (pair partition); |P|=28 follows.
Dropping E words and every unitarity condition is a RELAXATION: UNSAT here
implies UNSAT for all N. UNSAT is exact-CNF only unless LRAT-checked.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

BASE_ENCODER=Path(__file__).with_name('frontier-20261029-n47-heavy-support-cnf-v1.py')
PAIRS=list(itertools.combinations(range(4),2))


def encoder_class(path=BASE_ENCODER):
    s=importlib.util.spec_from_file_location('base',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.Encoder


def encode(deg,n=8,base=BASE_ENCODER):
    en=encoder_class(base)();sizes=tuple(len(D) for D in deg);Y={}
    for i,j in PAIRS:
        for a,b in itertools.product(range(sizes[i]),range(sizes[j])):Y[i,j,a,b]=en.var()
    P={q:en.var() for q in itertools.product(range(6),repeat=4)}
    for i,j in PAIRS:
        en.exact([Y[i,j,a,b] for a in range(sizes[i]) for b in range(sizes[j])],n)
        for a in range(sizes[i]):en.exact([Y[i,j,a,b] for b in range(sizes[j])],deg[i][a])
        for b in range(sizes[j]):en.exact([Y[i,j,a,b] for a in range(sizes[i])],deg[j][b])
        for a,b in itertools.product(range(6),repeat=2):
            ps=[v for q,v in P.items() if (q[i],q[j])==(a,b)];y=Y.get((i,j,a,b));en.amk(ps,1)
            if y is None:en.add(*ps)
            else:
                en.add(y,*ps)
                for v in ps:en.add(-v,-y)
    return en,Y,P


def main():
    ap=argparse.ArgumentParser();ap.add_argument('degrees');ap.add_argument('out',type=Path);ap.add_argument('--n',type=int,default=8);a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    deg=[tuple(map(int,x.split(','))) for x in a.degrees.split('/')]
    for i,D in enumerate(deg):
        if sum(D)!=a.n or min(D)<2 or max(D)>min(len(deg[j]) for j in range(4) if j!=i):raise ValueError('degrees')
    en,Y,P=encode(deg,a.n)
    with a.out.open('x',encoding='ascii') as f:
        f.write(f'p cnf {en.n} {len(en.C)}\n')
        for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
    meta={'degrees':deg,'n':a.n,'Y_variables':len(Y),'P_variables':f'{len(Y)+1}..{len(Y)+1296}','variables':en.n,'clauses':len(en.C),
      'encoder_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cnf_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta))


if __name__=='__main__':main()
