#!/usr/bin/env python3
"""Direct support-set control for the residual alphabet (4,3,3,4) case."""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2))


def options(m,degree):
    pairs=list(itertools.combinations(range(m),2))
    return [tuple(tuple(row) for row in rows) for rows in itertools.product(pairs,repeat=4)
            if tuple(sum(x in row for row in rows) for x in range(m))==degree]


def allowed(U,V):
    # Independent multiplicity counting, not XOR bitmasks.
    masks=[]
    for mask in range(1,16):
        count=Counter((x,y) for i in range(4) if mask>>i&1 for x in U[i] for y in V[i])
        if all(v%2==0 for v in count.values()):masks.append(mask)
    return masks


def projection_stats(S):
    return {pair:Counter((q[pair[0]],q[pair[1]]) for q in S) for pair in PAIRS}


def row_overlap_witness(S):
    rows=defaultdict(set)
    for a,b,c,d in S:rows[(a,d)].add((b,c))
    for x,y in itertools.combinations(sorted(rows),2):
        common=rows[x]&rows[y]
        if len(common)==1:return {'rows':[x,y],'common_column':next(iter(common)),'row_supports':[sorted(rows[x]),sorted(rows[y])]}
    return None


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);args=p.parse_args()
    G3=options(3,(2,3,3));G4=options(4,(2,2,2,2));S33={(i,j):allowed(U,V) for i,U in enumerate(G3) for j,V in enumerate(G3)}
    S34={(i,j):allowed(U,V) for i,U in enumerate(G3) for j,V in enumerate(G4)}
    count=Counter();witness=None
    for ib,B in enumerate(G3):
      for ic,C in enumerate(G3):
       for id,D in enumerate(G4):
        for fbc in S33[ib,ic]:
         for fbd in S34[ib,id]:
          for fcd in S34[ic,id]:
           absent=[(~z)&15 for z in (fbc,fbd,fcd)]
           if absent[0]&absent[1] or absent[0]&absent[2] or absent[1]&absent[2]:continue
           pb=sum((1<<i) for i in range(4) if 0 not in B[i]);pc=sum((1<<i) for i in range(4) if 0 not in C[i])
           if not (fbc==15 and fbd==pb and fcd==pc and pb==((~pc)&15)):
               raise ValueError('unexpected mixed parity normal form')
           count['parity_normal_forms']+=1
           for bits in itertools.product((0,1),repeat=4):
            S=set()
            for a in range(4):
             bb,cc,dd=B[a],C[a],D[a]
             if not(fbd>>a&1):
              for k in range(2):
               for v in cc:S.add((a,bb[k],v,dd[k^bits[a]]))
             else:
              for k in range(2):
               for v in bb:S.add((a,v,cc[k],dd[k^bits[a]]))
            if len(S)!=16:raise ValueError('bad support cardinality')
            stats=projection_stats(S)
            if not all(len(x)==8 and set(x.values())=={2} for x in stats.values()):continue
            if (0,0) in stats[(1,2)]:continue
            count['all_pair_projections_eight_and_degree_two']+=1
            w=row_overlap_witness(S)
            if w is None:raise ValueError('mixed support lacks unique overlap')
            count['AD_BC_unique_overlap']+=1
            if witness is None:witness={'support':sorted(S),'overlap':w}
    if (count['parity_normal_forms'],count['all_pair_projections_eight_and_degree_two'],count['AD_BC_unique_overlap'])!=(144,576,576):
        raise ValueError(f'unexpected enumeration: {count}')
    result={'counts':dict(count),'example':witness,
            'scope':'Exact finite mixed-case support controls; analytic incidence, parity, and no-unique-overlap proof is separate.'}
    with args.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({'counts':dict(count),'example_overlap':witness['overlap'],'scope':result['scope']},indent=2))


if __name__=='__main__':main()
