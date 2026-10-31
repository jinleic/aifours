#!/usr/bin/env python3
"""Zero-excess residual CNF with the THREE-BLOCK lemma (optionally without noH1).

Extends frontier-20261029-n48-t24-six-word-cnf-v1.py (imported, unchanged): same
variables and constraint families, plus one negative clause per six-word set S
that is the union of three2x2 rectangles, one in each cut, pairwise meeting in
exactly two words (|S|=6). Such S cannot lie in a zero-excess E (written lemma:
the three block phase relations admit a +-1 left-kernel vector, odd sum).
Sets are generated from all templates inside {0,1}^4 (each such configuration
uses at most two values per coordinate) by injective value maps; a control
compares with direct enumeration on small boxes.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

SIX=Path(__file__).with_name('frontier-20261029-n48-t24-six-word-cnf-v1.py')
CUTS3=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))


def load(path):
    s=importlib.util.spec_from_file_location('six',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def rectangles(cut,sizes):
    A,B=CUTS3[cut];RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)));out=[]
    for r,s in itertools.combinations(RR,2):
        for c,d in itertools.combinations(CC,2):
            ws=[]
            for x,y in ((r,c),(r,d),(s,c),(s,d)):
                q=[0]*4
                for i,v in zip(A,x):q[i]=v
                for i,v in zip(B,y):q[i]=v
                ws.append(tuple(q))
            out.append(tuple(ws))
    return out


def direct_configs(sizes):
    """Direct enumeration: (S, (b1,b2,b3)) for all qualifying rectangle triples."""
    R=[rectangles(k,sizes) for k in range(3)];idx=[{} for _ in range(3)]
    for k in range(3):
        for b in R[k]:
            for w in b:idx[k].setdefault(w,[]).append(b)
    out={}
    for b1 in R[0]:
        s1=set(b1);c2={b for w in b1 for b in idx[1].get(w,[])}
        for b2 in c2:
            s2=set(b2)
            if len(s1&s2)!=2:continue
            c3={b for w in s1^s2 for b in idx[2].get(w,[])}
            for b3 in c3:
                s3=set(b3)
                if len(s1&s3)==2 and len(s2&s3)==2 and len(s1|s2|s3)==6:out.setdefault(tuple(sorted(s1|s2|s3)),(b1,b2,b3))
    return out


def three_block_sets(sizes):
    templates=list(direct_configs((2,2,2,2)))
    out=set()
    for T in templates:
        used=[sorted({w[i] for w in T}) for i in range(4)]
        choices=[list(itertools.permutations(range(sizes[i]),len(used[i]))) for i in range(4)]
        for maps in itertools.product(*choices):
            m=[dict(zip(used[i],maps[i])) for i in range(4)]
            out.add(tuple(sorted(tuple(m[i][w[i]] for i in range(4)) for w in T)))
    return sorted(out)


def encode(deg,no_h1,joint,six_path=SIX):
    six=load(six_path);en,E,P,info=six.encode(deg,no_h1,False,joint);n3=0
    for S in three_block_sets(tuple(len(D) for D in deg)):en.add(*[-E[q] for q in S]);n3+=1
    info['three_block_clauses']=n3;return en,E,P,info


def main():
    ap=argparse.ArgumentParser();ap.add_argument('degrees');ap.add_argument('out',type=Path);ap.add_argument('--no-H1',action='store_true');ap.add_argument('--joint-P',action='store_true');a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    six=load(SIX);deg=six.parse_degrees(a.degrees);en,E,P,info=encode(deg,a.no_H1,a.joint_P)
    with a.out.open('x',encoding='ascii') as f:
        f.write(f'p cnf {en.n} {len(en.C)}\n')
        for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
    meta={'degrees':deg,'no_H1_imposed':a.no_H1,'three_block_clauses':info['three_block_clauses'],'six_word_lemma_clauses':0,'joint_P':a.joint_P,
      'variables':en.n,'clauses':len(en.C),'encoder_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'six_encoder_sha256':hashlib.sha256(SIX.read_bytes()).hexdigest(),
      'cnf_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta))


if __name__=='__main__':main()
