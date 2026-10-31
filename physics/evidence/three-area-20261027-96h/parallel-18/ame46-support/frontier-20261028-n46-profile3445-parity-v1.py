#!/usr/bin/env python3
"""Independent F2/parity replay of the normalized (3,4,4,5) support case."""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path

B=((0,1),(0,2),(0,2),(1,2),(1,2));BAD={(0,0),(1,1)}


def graph4():
    p=list(itertools.combinations(range(4),2));return [r for r in itertools.product(p,repeat=5)
      if tuple(sum(x in q for q in r) for x in range(4))==(2,2,3,3)]


def recmask(x,y):return sum(1<<(4*a+b) for a in x for b in y)


def parity_options(U,V):
    rect=[recmask(U[i],V[i]) for i in range(5)];val=[0]*32;ok=[]
    for m in range(32):
        if m:
            p=m&-m;val[m]=val[m^p]^rect[p.bit_length()-1]
        if val[m]==0:ok.append(m)
    return ok


def blocks(B,C,D,flags):
    # Each balanced binary 4-point subset is either one of two parity
    # sets or one of two cylinders correlating one coordinate pair.
    out=[]
    for sign in (0,1):
      F=[]
      for b,c,d in itertools.product(range(2),repeat=3):
        if flags==(1,1,1):keep=(b^c^d)==sign
        elif flags==(0,1,1):keep=(b^c)==sign
        elif flags==(1,0,1):keep=(b^d)==sign
        elif flags==(1,1,0):keep=(c^d)==sign
        else:raise ValueError('invalid balanced-fiber flag')
        if keep:F.append((B[b],C[c],D[d]))
      if len(F)!=4:raise ValueError('bad balanced fiber')
      if all((q[0],q[1]) not in BAD and (q[0],q[2]) not in BAD for q in F):out.append(F)
    return out


def degree2(S):
    for i,j in itertools.combinations(range(4),2):
        d=defaultdict(int)
        for q in S:d[q[i],q[j]]+=1
        if len(d)!=10 or any(x!=2 for x in d.values()):return False
    return True


def unique_overlap(S,cut):
    X=cut;Y=tuple(j for j in range(4) if j not in X);rows=defaultdict(set)
    for q in S:rows[tuple(q[j] for j in X)].add(tuple(q[j] for j in Y))
    return any(len(a&b)==1 for a,b in itertools.combinations(rows.values(),2))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    G=graph4();L=[parity_options(B,C) for C in G];R={(i,j):parity_options(G[i],G[j]) for i in range(len(G)) for j in range(i,len(G))}
    if len(G)!=310:raise ValueError('bad graph count')
    counts=Counter();types=Counter();example=None
    for i,C in enumerate(G):
      for j in range(i,len(G)):
       D=G[j]
       for fbc,fbd,fcd in itertools.product(L[i],L[j],R[i,j]):
        absent=[(~x)&31 for x in (fbc,fbd,fcd)]
        if absent[0]&absent[1] or absent[0]&absent[2] or absent[1]&absent[2]:continue
        options=[blocks(B[g],C[g],D[g],tuple(int(bool(x>>g&1)) for x in (fbc,fbd,fcd))) for g in range(5)]
        if any(not x for x in options):continue
        counts['parity_forms_with_allowed_fibers']+=1
        for fs in itertools.product(*options):
            counts['constructed_supports']+=1
            S={(g,)+q for g,F in enumerate(fs) for q in F}
            if not degree2(S):continue
            counts['all_pair_projection10_multiplicity2']+=1
            types[(fbc.bit_count(),fbd.bit_count(),fcd.bit_count())]+=1
            # These are different row cuts; both must independently obstruct.
            ac=unique_overlap(S,(0,2));ad=unique_overlap(S,(0,3))
            if not(ac and ad):raise ValueError('survivor without both unique-overlap cuts')
            counts['both_AC_and_AD_unique_overlap']+=1
            if example is None:example=sorted(S)
    if tuple(counts[k] for k in ('parity_forms_with_allowed_fibers','constructed_supports','all_pair_projection10_multiplicity2','both_AC_and_AD_unique_overlap'))!=(12,324,76,76):
        raise ValueError(f'unexpected counts {counts}')
    result={'C_D_graph_count_each':len(G),'counts':dict(counts),'full_fiber_size_histogram':{str(k):v for k,v in types.items()},
            'example_support':example,'scope':'Independent exact F2/parity and binary-fiber replay; written symmetry completeness is separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='example_support'},indent=2))


if __name__=='__main__':main()
