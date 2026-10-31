#!/usr/bin/env python3
"""Enumerate normalized 16-term residual supports at N=46,t=30.

All conclusions are finite support conditions, not an AME feasibility proof.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def fiber_options(a):
    others=[x for x in range(3) if x!=a];cube=list(itertools.product(others,repeat=3));out=[]
    for mask in range(1,256):
        pts=tuple(cube[i] for i in range(8) if mask>>i&1)
        if all(sum(q[j]==v for q in pts)>=2 for j in range(3) for v in others):out.append(pts)
    return out


def proj(S,i,j):return Counter((q[i],q[j]) for q in S)


def cut_ok(S,cut):
    A=cut;B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
    for q in S:
        r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
    for R in (list(rows.values()),list(cols.values())):
        if any(len(x&y)==1 for x,y in itertools.combinations(R,2)):return False
    return True


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args()
    options=[fiber_options(i) for i in range(3)];counts=Counter();hist=Counter();examples={}
    for fs in itertools.product(*options):
        if sum(map(len,fs))!=16:continue
        counts['size16_fiber_combinations']+=1
        S={(i,)+q for i,F in enumerate(fs) for q in F}
        for i,j in PAIRS:
            C=proj(S,i,j)
            if len(C)!=6 or min(C.values())<2:break
            missing={(x,y) for x in range(3) for y in range(3)}-set(C)
            if len(missing)!=3 or len({x for x,y in missing})!=3 or len({y for x,y in missing})!=3:break
        else:
            counts['all_pair_projection_and_degree']+=1
            flags=tuple(cut_ok(S,c) for c in CUTS);hist[str(flags)]+=1
            if all(flags):
                counts['all_cut_quadrangular']+=1
                signature=tuple(tuple(sorted({(x,y) for x in range(3) for y in range(3)}-set(proj(S,i,j)))) for i,j in ((1,2),(1,3),(2,3)))
                if len(examples)<4:examples[str(signature)]=sorted(S)
    if counts['size16_fiber_combinations']!=117312:raise ValueError('fiber enumeration mismatch')
    result={'fiber_option_counts':[len(x) for x in options], 'counts':dict(counts),
      'cut_quadrangular_histogram':dict(hist),'examples':examples,
      'scope':'Exhaustive normalized residual SUPPORT only; no complex-unitary amplitudes or maximal-code coupling verified.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='examples'},indent=2))


if __name__=='__main__':main()
