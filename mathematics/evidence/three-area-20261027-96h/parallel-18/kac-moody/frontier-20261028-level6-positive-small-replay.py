#!/usr/bin/env python3
"""Independent complete-source/positive-minor proofs for six omitted small cases.

The five coordinate-boundary baseline minors and the (2,4,6) seed1 minor have
one-sign coefficients and nonzero constant. Independently rebuild all source
combinations and actions, verify their completeness by exact Witt character,
and check each entire determinant polynomial on a shifted unisolvent grid by
standard-library integer Bareiss arithmetic. No FLINT/SymPy/producer imports.
"""
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('independent', ROOT / 'frontier-20261028-level6-two-minor-general-replay.py')
r = importlib.util.module_from_spec(sp)
sp.loader.exec_module(r)


def character():
    weights = ((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
    c = Counter()
    for d,mu in ((1,1),(2,-1),(3,-1),(6,1)):
        p = Counter({(0,0):1})
        for _ in range(6//d):
            q = Counter()
            for (a,b),v in p.items():
                for i,j in weights:
                    q[a+i,b+j] += v
            p = q
        for (a,b),v in p.items():
            c[d*a,d*b] += mu*v
    assert all(v%6==0 for v in c.values())
    return {m:v//6 for m,v in c.items()}


def main():
    out = ROOT / 'frontier-20261028-level6-positive-small-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    char = character()
    results = []
    for a,b,tag in ((0,1,'baseline'),(0,2,'baseline'),(0,3,'baseline'),(1,1,'baseline'),(1,2,'baseline'),(2,4,'seed1')):
        degree = (a,b,6)
        name = f'frontier-20261028-level6-{a}{b}6-minor-{tag}-v1.json'
        raw = (ROOT/name).read_bytes()
        M = json.loads(raw)
        praw = (ROOT/M['pencil']).read_bytes()
        assert hashlib.sha256(praw).hexdigest()==M['pencil_sha256']
        P = json.loads(praw)
        source_words=P['source_words']
        assert tuple(source_words)==r.ind.lyndon_words(degree)
        basis=[r.ind.ind.standard_bracket(w) for w in source_words]
        assert len(basis)==char[a,b] and all(v.get(w)==1 and min(v)==w for w,v in zip(source_words,basis))
        k=char.get((a,b),0)-char.get((a-1,b),0)-char.get((a,b-1),0)+char.get((a-2,b-1),0)+char.get((a-1,b-2),0)-char.get((a-2,b-2),0)
        coeffs=P['horizontal_kernel_coefficients']
        assert len(coeffs)==k
        assert len(r.ind.ind.ReducedSpace([{int(i):Q(c) for i,c in co.items()} for co in coeffs]))==k
        vectors=[r.ind.combine(basis,co) for co in coeffs]
        for v in vectors:
            for gen in ('f1','f2'):
                assert not r.ind.act(v,gen,6,6)
        aa=[r.ind.d3(v,degree,6,6) for v in vectors]
        bb=[r.ind.d3(v,degree,7,6) for v in vectors]
        cc=[r.ind.d3(v,degree,6,7) for v in vectors]
        mat=[[[Q(aa[j].get(w,0)),Q(bb[j].get(w,0))-Q(aa[j].get(w,0)),Q(cc[j].get(w,0))-Q(aa[j].get(w,0))]
              for j in range(k)] for w in M['rows']]
        poly={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in M['coefficients']}
        assert len(poly)==len(M['coefficients']) and max(i+j for i,j in poly)<=k
        assert poly.get((0,0),0) and (all(c>0 for c in poly.values()) or all(c<0 for c in poly.values()))
        scales=[math.lcm(*(c.denominator for e in row for c in e)) for row in mat]
        integer=[[[int(c*scale) for c in e] for e in row] for row,scale in zip(mat,scales)]
        count=0
        for i in range(k+1):
            for j in range(k+1-i):
                xv,yv=i-3,j+2
                det=r.bareiss([[u+xv*v+yv*w for u,v,w in row] for row in integer])
                assert Q(det,math.prod(scales))==sum(c*xv**p*yv**q for (p,q),c in poly.items())
                count+=1
        results.append({'degree':list(degree),'minor':name,'minor_sha256':hashlib.sha256(raw).hexdigest(),
                        'pencil_sha256':M['pencil_sha256'],'whole_primitive_dimension':k,
                        'horizontal_actions_checked':2*k,'exact_shifted_grid_determinants':count,
                        'one_sign_terms':len(poly),'constant_coefficient':str(poly[0,0]),
                        'status':'FULL_PRIMITIVE_MAP_INJECTIVE_FOR_ALL_X_Y_GE_ZERO_AT_NAMED_SOURCE_INTERFACES'})
        print('PASS positive complete primitive',degree,'k',k,'grid',count,flush=True)
    with out.open('x') as stream:
        json.dump({'results':results,'status':'PASS_ALL_SIX_COMPLETE_SOURCE_POSITIVE_MINOR_PROOFS',
                   'engine':'standard-library integer/Fraction arithmetic and independent tree-Jacobi, no FLINT/SymPy/producer imports',
                   'limits':'named Witt/finite-Levi/actual-source interfaces; no formal or independent-model assurance'},stream,indent=2)
        stream.write('\n')
    print('WROTE',out.name)


if __name__=='__main__':
    main()
