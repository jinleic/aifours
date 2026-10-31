#!/usr/bin/env python3
"""Exact enumeration of binary syndrome direction planes by triangle cover."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
OUT=Path(__file__).resolve().parent/'frontier-20261028-three-syndrome-cover-census-result.json'

def census(tri):
    sets=[sum(1<<(v-1) for v in t) for t in tri];out=Counter();count=0
    for a,b in combinations(range(1,1024),2):
        c=a^b
        if b>=c:continue
        J=a|b|c;vertices=0
        for i,t in enumerate(sets):
            if J>>i&1:vertices|=t
        out[J.bit_count(),vertices==1023]+=1;count+=1
    return count,out


def main():
    count,out=census(TRI)
    expected={(2,False):45,(3,False):480,(4,False):2483,(4,True):247,
              (5,False):6480,(5,True):3600,(6,False):7865,(6,True):17545,
              (7,False):3640,(7,True):40040,(8,True):49185,(9,True):32800,(10,True):9841}
    if count!=174251 or dict(out)!=expected:raise ValueError('CENSUS')
    # An algebraic count control is independent of graph incidence.
    if (1023*1022)//6!=count:raise ValueError('PLANE_COUNT')
    report={'all_checked':True,'direction_planes':count,'noncover_planes':sum(v for (k,c),v in out.items() if not c),
            'cover_planes':sum(v for (k,c),v in out.items() if c),
            'counts':[{'varying_factors':k,'covers_vertices':c,'planes':n} for (k,c),n in sorted(out.items())],
            'limits':'Exact combinatorial plane count only; noncover entropy consequence imports the separately pinned proper-subgraph theorem.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
