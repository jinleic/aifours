#!/usr/bin/env python3
"""Independent 9-bit compatibility graph for the n=5 normal forms.

Vertices are three-element tuples of alphabet-subset bitmasks. A singleton is
placed in a different fiber for each vertex class. An edge means that the
union of the three Cartesian products has exactly five elements.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

SINGLE=(1,2,4);DOUBLE=(3,5,6)


def vertices(fixed):
    out=[]
    for x in SINGLE:
        for y in DOUBLE:
            for z in DOUBLE:
                arr=[None,None,None];arr[fixed]=x
                rest=[j for j in range(3) if j!=fixed];arr[rest[0]]=y;arr[rest[1]]=z
                out.append(tuple(arr))
    if len(set(out))!=27:raise ValueError('vertex enumeration collision')
    return out


def product_mask(left,right):
    bits=0
    for x in range(3):
        if not left>>x&1:continue
        for y in range(3):
            if right>>y&1:bits|=1<<(3*x+y)
    return bits


def adjacent(x,y):
    union=0
    for f in range(3):union|=product_mask(x[f],y[f])
    return union.bit_count()==5


def mat(A,B):
    return [sum((1<<j) for j,b in enumerate(B) if adjacent(a,b)) for a in A]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    V=[vertices(f) for f in range(3)];AB=mat(V[0],V[1]);AC=mat(V[0],V[2]);BC=mat(V[1],V[2])
    counts=[sum(x.bit_count() for x in M) for M in (AB,AC,BC)]
    if counts!=[144,144,144]:raise ValueError('edge counts differ')
    wedges=triangles=0
    for i in range(27):
        for j in range(27):
            if not AB[i]>>j&1:continue
            wedges+=AC[i].bit_count()
            triangles+=(AC[i]&BC[j]).bit_count()
    if wedges!=1080 or triangles!=0:raise ValueError('unexpected wedge or triangle count')
    # Pin every edge mask, making the zero-triangle condition independently replayable.
    all_edges={'AB':AB,'AC':AC,'BC':BC}
    edge_bytes=json.dumps(all_edges,sort_keys=True,separators=(',',':')).encode('ascii')
    result={'vertices_per_class':[27,27,27],'edge_counts_AB_AC_BC':counts,
            'two_edge_wedges':wedges,'triangles':triangles,'edge_masks':all_edges,
            'canonical_edge_masks_sha256':hashlib.sha256(edge_bytes).hexdigest(),
            'scope':'Exact bitmask graph for the 27^3 finite normal forms; normal-form completeness is a separate mathematical proof.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='edge_masks'},indent=2))


if __name__=='__main__':main()
