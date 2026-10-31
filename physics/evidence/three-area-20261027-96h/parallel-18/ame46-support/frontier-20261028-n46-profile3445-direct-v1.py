#!/usr/bin/env python3
"""Direct exact enumeration of the (3,4,4,5) 46-support residual case.

The mathematical packet supplies the complete normal form and symmetries.
This implementation uses balanced 4-point fibers and exact pair counts,
not the independent checker's F2 rectangle-parity prefilter.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path

B=((0,1),(0,2),(0,2),(1,2),(1,2))
FORBID={(0,0),(1,1)}
CUTS=((0,1),(0,2),(0,3))


def graphs4():
    pairs=list(itertools.combinations(range(4),2))
    return [rows for rows in itertools.product(pairs,repeat=5)
            if tuple(sum(x in row for row in rows) for x in range(4))==(2,2,3,3)]


def fibers(b,c,d):
    out=[];cube=list(itertools.product(b,c,d))
    for F in itertools.combinations(cube,4):
        if any((x[0],x[1]) in FORBID or (x[0],x[2]) in FORBID for x in F):continue
        if all(sum(x[j]==v for x in F)==2 for j,values in enumerate((b,c,d)) for v in values):out.append(F)
    return out


def overlap(S,cut):
    A=cut;B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
    for q in S:
        r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
    for kind,T in (('rows',rows),('columns',cols)):
        for x,y in itertools.combinations(sorted(T),2):
            common=T[x]&T[y]
            if len(common)==1:return {'side':kind,'lines':[x,y],'shared':next(iter(common))}
    return None


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    G=graphs4();pairs=list(itertools.combinations(range(4),2))
    cache={(g,c,d):fibers(B[g],c,d) for g in range(5) for c in pairs for d in pairs}
    cnt=Counter();witness=None
    for ic,C in enumerate(G):
      for id in range(ic,len(G)):
       D=G[id];choices=[cache[g,C[g],D[g]] for g in range(5)]
       if any(not x for x in choices):continue
       cnt['incidence_pairs_with_fiber_options']+=1
       # This direct enumeration deliberately includes the F=0 free-fiber cases.
       for fs in itertools.product(*choices):
        cnt['balanced_support_combinations']+=1
        S={(g,)+q for g,F in enumerate(fs) for q in F}
        if len(S)!=20:raise ValueError('wrong support size')
        valid=True
        for i,j in itertools.combinations(range(4),2):
            proj=Counter((q[i],q[j]) for q in S)
            if len(proj)!=10 or set(proj.values())!={2}:valid=False;break
        if not valid:continue
        cnt['all_pair_projection10_multiplicity2']+=1
        obs=[overlap(S,c) for c in CUTS]
        if all(v is None for v in obs):cnt['all_cuts_no_unique_overlap']+=1
        if witness is None:witness={'support':sorted(S),'cut_overlap_obstructions':obs}
    if (cnt['incidence_pairs_with_fiber_options'],cnt['balanced_support_combinations'],
        cnt['all_pair_projection10_multiplicity2'],cnt['all_cuts_no_unique_overlap'])!=(10116,2827560,76,0):
        raise ValueError(f'unexpected enumeration counts {cnt}')
    result={'B_rowsets':B,'C_D_graphs_each':len(G),'ordered_C_le_D_graph_pairs':len(G)*(len(G)+1)//2,
      'normalized_missing_BC_BD_pairs':sorted(FORBID),'counts':dict(cnt),'survivor_example':witness,
      'scope':'Exact normalized finite support enumeration; the written normal-form and symmetry proof is separate.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='survivor_example'},indent=2))


if __name__=='__main__':main()
