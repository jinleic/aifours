#!/usr/bin/env python3
"""Exact search of all color-coordinate roles for four published OLS arrays.

Uses Weisner 1963 Figs. 1-3 and Parker 1959 Section 3. For any disconnected
symbol-pair graph, builds and independently verifies rational vectors in the
original 10x10/three-ONB definition; no inferred 100-ray conclusion.
"""
from collections import Counter, defaultdict
from itertools import combinations
import importlib.util
import json
from math import gcd
from functools import reduce
from pathlib import Path

HERE=Path(__file__).resolve().parent

def load(name, filename):
    spec=importlib.util.spec_from_file_location(name,HERE/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

w1=load('weisner1','frontier-20261028-ols10-switch-v1.py')
w2=load('weisner2','frontier-20261028-weisner-fig2-components-v1.py')
w3=load('weisner3','frontier-20261028-weisner-fig3-components-v1.py')
N=10
# Transcribed from Parker 1959, p.861, table in section 3.
PARKER_A=(
 '0417298365','8152739406','9826374510','5983047621','7698415032',
 '6709852143','3071986254','1234560789','2345601897','4560123978',
)
PARKER_B=(
 '0786935412','6178094523','5027819634','9613782045','3902478156',
 '8491357260','7859246301','4560123789','1234560978','2345601897',
)


def triples_from_rows(rows):
    return tuple((r,c,int(word[0]),int(word[1]))
                 for r,row in enumerate(rows) for c,word in enumerate(row.split()))


def check_oa(points):
    assert len(points)==N*N
    for i,j in combinations(range(4),2):
        assert len({(q[i],q[j]) for q in points})==N*N
        assert all(0<=q[i]<N and 0<=q[j]<N for q in points)


def components(points,axis,a,b):
    verts=[q for q in points if q[axis] in (a,b)]
    assert len(verts)==2*N
    adjacency={q:set() for q in verts}
    for z in range(4):
        if z==axis:
            continue
        groups=defaultdict(list)
        for q in verts:
            groups[q[z]].append(q)
        assert len(groups)==N and all(len(group)==2 for group in groups.values())
        for x,y in groups.values():
            adjacency[x].add(y)
            adjacency[y].add(x)
    result=[]
    remaining=set(verts)
    while remaining:
        stack=[min(remaining)]
        comp=set()
        while stack:
            q=stack.pop()
            if q in comp:
                continue
            comp.add(q)
            stack.extend(adjacency[q]-comp)
        remaining-=comp
        result.append(tuple(sorted(comp)))
    return sorted(result)


def primitive(v):
    d=reduce(gcd,(abs(x) for x in v if x),0)
    w=tuple(x//d for x in v)
    return tuple(-x for x in w) if next(x for x in w if x)!=abs(next(x for x in w if x)) else w


def build_partial(points,axis,a,b,comps):
    assert len(comps) in (2,3)
    component={q:k for k,comp in enumerate(comps) for q in comp}
    # Common denominator65: angles 0, (3,4,5), (5,12,13).
    rotations=((65,0),(39,52),(25,60))
    vectors={}
    for q in points:
        color=q[axis]
        v=[0]*N
        if color in (a,b):
            co,si=rotations[component[q]]
            if color==a:
                v[a],v[b]=co,si
            else:
                v[a],v[b]=-si,co
        else:
            v[color]=65
        assert sum(x*x for x in v)==65**2
        vectors[q]=tuple(v)
    other=[i for i in range(4) if i!=axis]
    blocks=[]
    for j in other:
        for label in range(N):
            block=[q for q in points if q[j]==label]
            assert len(block)==N
            for x,y in combinations(block,2):
                assert sum(u*v for u,v in zip(vectors[x],vectors[y]))==0
            blocks.append(block)
    assert len(blocks)==30
    count=len({primitive(v) for v in vectors.values()})
    assert count==N+2*(len(comps)-1)
    return {'color_axis':axis,'colors':[a,b],'component_sizes':[len(c) for c in comps],
            'row_axis':other[0],'column_axis':other[1],'transversal_axis':other[2],
            'denominator':65,'ray_count':count,
            'array':[[list(vectors[next(q for q in points if q[other[0]]==r and q[other[1]]==c)])
                      for c in range(N)] for r in range(N)],
            'labels':[[next(q[other[2]] for q in points if q[other[0]]==r and q[other[1]]==c)
                       for c in range(N)] for r in range(N)]}


def main():
    datasets={
      'Weisner1963-Fig1':tuple((r,c,*w1.TABLE[r][c]) for r in range(N) for c in range(N)),
      'Weisner1963-Fig2':triples_from_rows(w2.ROWS),
      'Weisner1963-Fig3-inferred00':triples_from_rows(w3.ROWS),
      'Parker1959-section3':tuple((r,c,int(PARKER_A[r][c]),int(PARKER_B[r][c]))
                                   for r in range(N) for c in range(N)),
    }
    output=[]
    first_partial=None
    for name,points in datasets.items():
        check_oa(points)
        for axis in range(4):
            hist=Counter()
            for a,b in combinations(range(N),2):
                comps=components(points,axis,a,b)
                sizes=tuple(sorted(map(len,comps)))
                hist[sizes]+=1
                if len(comps)>1 and first_partial is None:
                    first_partial={'source':name,**build_partial(points,axis,a,b,comps)}
            item={'source':name,'color_axis':axis,
                  'component_histogram':[[list(s),n] for s,n in sorted(hist.items())]}
            output.append(item)
            print(name,'color_axis',axis,'hist',item['component_histogram'],flush=True)
    record={'tables':output,'partial_witness':first_partial,
            'caveat':'finite incidence exploration; no all-incidence or 100-ray conclusion'}
    path=HERE/'frontier-20261028-coordinate-switch-result-v1.json'
    path.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    if first_partial:
        print('EXACT_NONCLASSICAL_PARTIAL_RQLS_FOUND',first_partial['source'],
              'rays',first_partial['ray_count'],'colors',first_partial['colors'],flush=True)
    else:
        print('No disconnected pair graph in these tables/roles.',flush=True)
    print('wrote',path.name,flush=True)


if __name__=='__main__':
    main()
