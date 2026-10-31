#!/usr/bin/env python3
"""CNF for N48/t24 zero-excess residual supports, optionally with the P code.

Variables 1..|Q| are E indicators in lexicographic order on the residual box
r0 x r1 x r2 x r3. With --joint-P the next1296 variables are P indicators on
{0..5}^4 (lexicographic). Encoded NECESSARY conditions:
  * exact fiber sizes |E_a| = 2 d_i(a) from the supplied degree vectors;
  * every pair value is carried by0 or2 E words (zero excess);
  * full2x2 cut blocks: rows r!=t, columns c!=d, (r,c),(r,d),(t,c) => (t,d);
  * optional conditional no-Hamming-one (flag recorded, not proved here);
  * optional six-word phase lemma (written separately): no binary sub-grid may
    contain a parity class minus one antipodal pair;
  * optional P code: every non-E pair value in each of the six pair systems is
    carried by exactly one P word and no E pair value by a P word.
No amplitudes are encoded; a SAT model is only a candidate to be checked by the
separate exact decoder. UNSAT is uncertified unless an LRAT proof is checked,
and even then certifies only this exact CNF, not encoder soundness.
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
    if len(deg)!=4:raise ValueError('four degree vectors required')
    for i,D in enumerate(deg):
        if sum(D)!=12 or min(D)<2 or len(D)>6:raise ValueError('degree vector')
        cap=min(len(deg[j]) for j in range(4) if j!=i)
        if max(D)>cap:raise ValueError('degree exceeds partner alphabet (D3)')
    return deg


def six_word_sets(sizes):
    """All parity-class-minus-antipodal-pair six-sets inside binary sub-grids."""
    out=[]
    for vals in itertools.product(*(itertools.combinations(range(r),2) for r in sizes)):
        for parity in (0,1):
            cls=[bits for bits in itertools.product((0,1),repeat=4) if sum(bits)%2==parity]
            antipodes=[]
            for b in cls:
                nb=tuple(1-x for x in b)
                if b<nb:antipodes.append((b,nb))
            if len(antipodes)!=4:raise ValueError('antipodal pairing')
            for pair in antipodes:
                six=[tuple(vals[i][b[i]] for i in range(4)) for b in cls if b not in pair]
                out.append(tuple(sorted(six)))
    return out


def encode(deg,no_h1=False,six=False,joint=False,base=BASE_ENCODER):
    en=encoder_class(base)();sizes=tuple(len(D) for D in deg);Q=list(itertools.product(*(range(r) for r in sizes)))
    E={q:en.var() for q in Q}
    P={q:en.var() for q in itertools.product(range(6),repeat=4)} if joint else {}
    for i,D in enumerate(deg):
        for a,d in enumerate(D):en.exact([E[q] for q in Q if q[i]==a],2*d)
    Y={}
    for i,j in PAIRS:
        for a,b in itertools.product(range(sizes[i]),range(sizes[j])):
            xs=[E[q] for q in Q if (q[i],q[j])==(a,b)];en.amk(xs,2)
            for k,x in enumerate(xs):en.add(-x,*[z for m,z in enumerate(xs) if m!=k])
            if joint:
                y=en.var();Y[i,j,a,b]=y
                for x in xs:en.add(-x,y)
                en.add(-y,*xs)
    if no_h1:
        for free in range(4):
            fixed=tuple(i for i in range(4) if i!=free)
            for vals in itertools.product(*(range(sizes[i]) for i in fixed)):
                en.amk([E[q] for q in Q if tuple(q[i] for i in fixed)==vals],1)
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)))
        for r,t in itertools.permutations(RR,2):
            for c,d in itertools.permutations(CC,2):
                en.add(-E[qword(A,r,B,c)],-E[qword(A,r,B,d)],-E[qword(A,t,B,c)],E[qword(A,t,B,d)])
    nsix=0
    if six:
        for S in six_word_sets(sizes):en.add(*[-E[q] for q in S]);nsix+=1
    if joint:
        for i,j in PAIRS:
            for a,b in itertools.product(range(6),repeat=2):
                ps=[v for q,v in P.items() if (q[i],q[j])==(a,b)];y=Y.get((i,j,a,b))
                en.amk(ps,1)
                if y is None:en.add(*ps)
                else:
                    en.add(y,*ps)
                    for v in ps:en.add(-v,-y)
    return en,E,P,{'six_word_clauses':nsix}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('degrees');ap.add_argument('out',type=Path)
    ap.add_argument('--no-H1',action='store_true');ap.add_argument('--six',action='store_true');ap.add_argument('--joint-P',action='store_true');a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    deg=parse_degrees(a.degrees);en,E,P,info=encode(deg,a.no_H1,a.six,a.joint_P)
    with a.out.open('x',encoding='ascii') as f:
        f.write(f'p cnf {en.n} {len(en.C)}\n')
        for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
    meta={'degrees':deg,'no_H1_imposed':a.no_H1,'six_word_lemma_clauses':info['six_word_clauses'],'joint_P':a.joint_P,
      'E_variables':f'1..{len(E)} lexicographic on residual box','P_variables':(f'{len(E)+1}..{len(E)+len(P)} lexicographic on 6^4' if a.joint_P else None),
      'variables':en.n,'clauses':len(en.C),'base_encoder_sha256':hashlib.sha256(BASE_ENCODER.read_bytes()).hexdigest(),
      'encoder_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cnf_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta,indent=2))


if __name__=='__main__':main()
