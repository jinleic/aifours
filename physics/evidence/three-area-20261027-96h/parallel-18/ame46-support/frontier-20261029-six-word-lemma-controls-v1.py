#!/usr/bin/env python3
"""Exact controls for the zero-excess six-word lemma (not its proof).

1. For every parity class and omitted antipodal pair (8 six-sets of the binary
   4-cube), the three2x2 rectangles (one per cut) are present, and the integer
   block system has the left-kernel vector (1,-1,1) up to ordering with odd sum.
2. The CNF generator's six_word_sets(sizes) equals an independent re-derivation
   on small boxes and has8*prod C(r_i,2) members.
3. A deliberately broken set (parity class minus a NON-antipodal pair) is not
   flagged and its residual blocks need not exist (mutation control).
"""
import argparse
import importlib.util
import itertools
import json
from math import comb
from pathlib import Path

CUTS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))


def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def rectangles(S):
    """For each cut, the2x2 rectangles (two rows, two columns, all4 words in S)."""
    S=set(S);out=[]
    for A,B in CUTS:
        rows={};found=[]
        for w in S:rows.setdefault(tuple(w[i] for i in A),set()).add(tuple(w[i] for i in B))
        for r,s in itertools.combinations(sorted(rows),2):
            common=rows[r]&rows[s]
            for c,d in itertools.combinations(sorted(common),2):found.append((r,s,c,d))
        out.append(found)
    return out


def block_row(A,B,r,s,c,d,index):
    row=[0]*len(index)
    def word(x,y):
        q=[0]*4
        for i,v in zip(A,x):q[i]=v
        for i,v in zip(B,y):q[i]=v
        return tuple(q)
    for x,y,sign in ((r,c,1),(r,d,-1),(s,c,-1),(s,d,1)):row[index[word(x,y)]]+=sign
    return row


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    enc=load('enc',a.encoder);records=[]
    cube=list(itertools.product((0,1),repeat=4))
    for parity in (0,1):
        cls=[b for b in cube if sum(b)%2==parity]
        for g in cls:
            gbar=tuple(1-x for x in g)
            if gbar<g:continue
            S=[b for b in cls if b not in (g,gbar)];rect=rectangles(S)
            if [len(x) for x in rect]!=[1,1,1]:raise ValueError('rectangle count')
            index={w:k for k,w in enumerate(sorted(S))}
            M=[block_row(A,B,*rect[k][0],index) for k,(A,B) in enumerate(CUTS)]
            hits=[]
            for lam in itertools.product((1,-1),repeat=3):
                if all(sum(l*row[j] for l,row in zip(lam,M))==0 for j in range(6)):hits.append(lam)
            if not hits or any(sum(l)%2==0 for l in hits):raise ValueError('no odd kernel vector')
            records.append({'parity':parity,'omitted':[g,gbar],'six':S,'odd_kernel_vectors':hits})
    # non-antipodal mutation: removing two words at distance2 leaves no full three-cut rectangle triple
    mut=[b for b in cube if sum(b)%2==0 and b not in ((0,0,0,0),(0,0,1,1))]
    mutation_rectangles=[len(x) for x in rectangles(mut)]
    gen_checks=[]
    for sizes in ((2,2,2,2),(3,2,2,2),(3,3,2,2),(3,5,5,5)):
        sets=enc.six_word_sets(sizes);expect=8
        for r in sizes:expect*=comb(r,2)
        independent=set()
        for vals in itertools.product(*(itertools.combinations(range(r),2) for r in sizes)):
            for rec in records:independent.add(tuple(sorted(tuple(vals[i][b[i]] for i in range(4)) for b in rec['six'])))
        if len(sets)!=expect or set(sets)!=independent or len(set(sets))!=expect:raise ValueError('generator mismatch')
        gen_checks.append({'sizes':sizes,'six_sets':expect})
    receipt={'scope':'Exact integer controls of the six-word lemma encodings; the proof is written separately.',
      'cube_cases':records,'mutation_nonantipodal_rectangles_per_cut':mutation_rectangles,'generator_checks':gen_checks}
    with a.out.open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=1);f.write('\n')
    print(json.dumps({'cases':len(records),'mutation':mutation_rectangles,'generator':gen_checks}))


if __name__=='__main__':main()
