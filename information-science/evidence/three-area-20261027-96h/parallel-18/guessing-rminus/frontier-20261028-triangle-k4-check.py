#!/usr/bin/env python3
"""Verify K4-free and triangle-cover premises independently by enumeration."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-triangle-k4-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    quads=list(combinations(range(1,11),4))
    cliques=[q for q in quads if all(y in N[x] for x,y in combinations(q,2))]
    if cliques:raise ValueError(('K4_FOUND',cliques))
    if len(triangles)!=10 or any(len(set(t))!=3 or any(y not in N[x] for x,y in combinations(t,2)) for t in triangles):
        raise ValueError('INVALID_TRIANGLE_COVER')
    if any(sum(v in t for t in triangles)!=3 for v in range(1,11)):raise ValueError('INVALID_VERTEX_MULTIPLICITY')
    checks=0
    for v in range(1,11):
        for t in triangles:
            checks+=1
            if v not in t and not any(u not in N[v] for u in t):raise ValueError(('NO_NONNEIGHBOUR',v,t))
    out={'input_sha256':EXPECTED,'four_vertex_sets_checked':len(quads),'K4_count':0,
         'chosen_triangles':triangles,'vertex_triangle_multiplicity':3,
         'vertex_triangle_nonneighbour_checks':checks,
         'limits':'Verifies hypotheses of the written two-coset theorem; not a global upper bound or an exhaustive search over nonlinear strategies.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
