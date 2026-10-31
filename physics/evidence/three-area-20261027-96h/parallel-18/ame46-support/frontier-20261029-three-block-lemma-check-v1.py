#!/usr/bin/env python3
"""Complete finite check behind the three-block lemma (exact integers).

A configuration is (B1,B2,B3): B_k a2x2 rectangle of word positions in cut k
(AB|CD, AC|BD, AD|BC), |B_a & B_b|=2, |B1|B2|B3|=6. Then B1&B2&B3 is empty and
B3=(B1^B2), so it is determined by B1 and B2. Up to independent relabeling of
values at each party (a symmetry of the whole question), B1 has rows (0,0),r'
and columns (0,0),c' with r',c' in {(0,1),(1,0),(1,1)}. For each of the6 shared
pairs of B1 and every rectangle B2 of cut AC|BD in the box6^4 containing that
pair and no other word of B1, test whether B1^B2 is a rectangle of cut AD|BC.
For every configuration found, check that each party uses at most2 values and
that some lambda in {+-1}^3 gives sum lambda_k M_k = 0 (M_k = signed block row
+(r,c) -(r,c') -(r',c) +(r',c')), so the phase system is odd-inconsistent.
Also cross-checks the template generator of frontier-20261029-three-block-cnf-v1.py.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

CUTS3=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))


def word(cut,r,c):
    A,B=CUTS3[cut];q=[0]*4
    for i,v in zip(A,r):q[i]=v
    for i,v in zip(B,c):q[i]=v
    return tuple(q)


def rect(cut,r,s,c,d):return ((word(cut,r,c),1),(word(cut,r,d),-1),(word(cut,s,c),-1),(word(cut,s,d),1))


def as_rect(cut,S):
    """If the4-set S is a rectangle of cut, return its signed form, else None."""
    A,B=CUTS3[cut];rows=sorted({tuple(w[i] for i in A) for w in S});cols=sorted({tuple(w[i] for i in B) for w in S})
    if len(rows)!=2 or len(cols)!=2:return None
    R=rect(cut,rows[0],rows[1],cols[0],cols[1])
    return R if {w for w,_ in R}==set(S) else None


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    box=6;pairs2=list(itertools.product(range(box),repeat=2));configs={};stats={'B1':0,'B2_candidates':0}
    for rp in ((0,1),(1,0),(1,1)):
        for cp in ((0,1),(1,0),(1,1)):
            B1=rect(0,(0,0),rp,(0,0),cp);S1={w for w,_ in B1};stats['B1']+=1
            for shared in itertools.combinations(sorted(S1),2):
                for r,s in itertools.combinations(pairs2,2):
                    for c,d in itertools.combinations(pairs2,2):
                        B2=rect(1,r,s,c,d);S2={w for w,_ in B2}
                        if not set(shared)<=S2 or len(S1&S2)!=2:continue
                        stats['B2_candidates']+=1
                        B3=as_rect(2,S1^S2)
                        if B3 is None:continue
                        key=tuple(sorted(S1|S2))
                        configs.setdefault(key,(B1,B2,B3))
    bad=[];values_hist={}
    for key,(B1,B2,B3) in configs.items():
        sig=tuple(len({w[i] for w in key}) for i in range(4));values_hist[str(sig)]=values_hist.get(str(sig),0)+1
        if max(sig)>2:bad.append(('values',key))
        ix={w:k for k,w in enumerate(key)};M=[]
        for B in (B1,B2,B3):
            row=[0]*6
            for w,sg in B:row[ix[w]]+=sg
            M.append(row)
        if not any(all(sum(l*M[k][j] for k,l in enumerate(lam))==0 for j in range(6)) for lam in itertools.product((1,-1),repeat=3)):bad.append(('kernel',key))
    if bad:raise ValueError(f'counterexample {bad[:3]}')
    s=importlib.util.spec_from_file_location('tb',a.encoder);tb=importlib.util.module_from_spec(s);s.loader.exec_module(tb)
    gen_checks=[]
    for sizes in ((2,2,2,2),(3,3,3,3),(2,3,3,4)):
        g=set(tb.three_block_sets(sizes));d=set(tb.direct_configs(sizes))
        if g!=d:raise ValueError('generator mismatch')
        gen_checks.append({'sizes':sizes,'sets':len(g)})
    rec={'scope':'Complete enumeration (up to value relabeling) of three-block configurations in box6^4; exact integer kernel test.','stats':stats,
      'canonical_configurations':len(configs),'value_signatures':values_hist,'all_use_at_most_two_values_per_party':True,'all_odd_kernel':True,'generator_checks':gen_checks}
    with a.out.open('x',encoding='utf-8') as f:json.dump(rec,f,indent=2);f.write('\n')
    print(json.dumps(rec,indent=1))


if __name__=='__main__':main()
