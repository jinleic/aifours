#!/usr/bin/env python3
"""Explicit 3-color certificates for proper induced graphs from the pinned graph."""
from itertools import product
N={1:{2,3,4,5,6,7},2:{1,3,7,9,10},3:{1,2,4,8,9},4:{1,3,5,8,10},
   5:{1,4,6,9,10},6:{1,5,7,8,9},7:{1,2,6,8,10},8:{3,4,6,7,9,10},
   9:{2,3,5,6,8},10:{2,4,5,7,8}}

def find_coloring(missing, graph):
    vs=sorted(set(graph)-{missing})
    edges=[(v,w) for v in vs for w in graph[v] if v<w and w in vs]
    for candidate in product(range(3), repeat=len(vs)):
        c=dict(zip(vs,candidate))
        if all(c[v]!=c[w] for v,w in edges):
            return tuple(tuple(v for v in vs if c[v]==color) for color in range(3))
    return None

positive=[]
for v in range(1,11):
    classes=find_coloring(v,N)
    if classes is None:
        print('deleted %d: no proper 3-coloring' % v)
    else:
        assert set().union(*map(set,classes))==set(N)-{v}
        assert all(not (set(part)&N[u]) for part in classes for u in part)
        print('deleted %d: classes=%s' % (v,classes))
        positive.append(v)
print('three-colorable deletion vertices:',positive)

# Add the missing edge 2-4, making {1,2,3,4} a K4 that survives deleting 10.
mut={v:set(nb) for v,nb in N.items()}
mut[2].add(4); mut[4].add(2)
assert all(w in mut[v] for v in (1,2,3,4) for w in (1,2,3,4) if v!=w)
assert find_coloring(10,mut) is None
print('negative control: K4 mutation rejected for the intended coloring reason')
