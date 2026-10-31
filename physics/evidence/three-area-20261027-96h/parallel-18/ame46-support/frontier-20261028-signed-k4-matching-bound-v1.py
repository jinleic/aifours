#!/usr/bin/env python3
"""Exact controls for the 3-symbol K4 forbidden-matching bound."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path


def allowed(a,f,g,h):
    others=[x for x in range(3) if x!=a]
    return [(b,c,d) for b,c,d in itertools.product(others,repeat=3)
            if c!=f[b] and d!=g[b] and d!=h[c]]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    permutations=list(itertools.permutations(range(3)));hist=Counter();fiberhist=Counter();maxf=0;witness=None
    for f,g,h in itertools.product(permutations,repeat=3):
        sizes=[len(allowed(x,f,g,h)) for x in range(3)]
        total=sum(sizes);hist[total]+=1
        for v in sizes:fiberhist[v]+=1;maxf=max(maxf,v)
        if total==12 and witness is None:witness={'BC':f,'BD':g,'CD':h,'fiber_sizes':sizes}
    if maxf!=4 or max(hist)!=12 or sum(hist.values())!=216:raise ValueError('matching bound failure')
    # Drop CD entirely: the weakened constraint must allow >12 tuples.
    relaxed=max(sum(1 for x in range(3) for b,c,d in itertools.product([z for z in range(3) if z!=x],repeat=3)
                    if c!=f[b] and d!=g[b]) for f,g in itertools.product(permutations,repeat=2))
    if relaxed!=15:raise ValueError('weakened-constraint control')
    # Any three distinct edges of the binary cube cover at least four vertices.
    cube=list(itertools.product((0,1),repeat=3))
    edges=[frozenset((u,v)) for u,v in itertools.combinations(cube,2) if sum(x!=y for x,y in zip(u,v))==1]
    if min(len(set().union(*E)) for E in itertools.combinations(edges,3))!=4:raise ValueError('cube edge claim')
    result={'matching_triples':sum(hist.values()),'allowed_tuple_histogram':dict(sorted(hist.items())),
      'fiber_size_histogram':dict(sorted(fiberhist.items())),'maximum_per_fiber':maxf,'maximum_total':max(hist),
      'maximal_example':witness,'relaxed_drop_one_edge_maximum':relaxed,
      'three_cube_edges_minimum_vertex_union':4,
      'scope':'Exact finite controls for a general written matching bound; not an AME witness.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
