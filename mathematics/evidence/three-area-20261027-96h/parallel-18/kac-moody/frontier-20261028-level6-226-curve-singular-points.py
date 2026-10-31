#!/usr/bin/env python3
"""Exact rational singular points and tangent cones of the determinant curve.

The points lie outside x,y>=0.  No genus, Faltings, map-kernel or novelty
conclusion follows merely from these singularities.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('det',ROOT/'frontier-20261028-level5-type-determinant.py')
det=importlib.util.module_from_spec(spec);spec.loader.exec_module(det)


def shifted_coefficient(coeff,a,b,i,j):
    return sum(c*math.comb(u,i)*math.comb(v,j)*a**(u-i)*b**(v-j)
               for (u,v),c in coeff.items() if u>=i and v>=j)


def resultant(a,b):
    # ascending input coefficients; Sylvester matrix from descending lists
    while a and not a[-1]:a.pop()
    while b and not b[-1]:b.pop()
    m=len(a)-1;n=len(b)-1;ad=list(reversed(a));bd=list(reversed(b));N=m+n
    rows=[]
    for i in range(n):rows.append([0]*i+ad+[0]*(N-i-len(ad)))
    for i in range(m):rows.append([0]*i+bd+[0]*(N-i-len(bd)))
    return det.bareiss(rows)


def main():
    raw=(ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297'
    R=json.loads(raw);coeff={(a['x_power'],a['y_power']):int(a['coefficient']) for a in R['R_coefficients']}
    assert len(coeff)==253
    expected={(-5,-5):(2,[286978140,0,0]),
              (-6,-6):(4,[-6531840000*8278,-6531840000*78878,-6531840000*(-383037),-6531840000*(-189922),-6531840000*(-11447)]),
              (-4,-5):(2,[-72*221760,-72*2382515,-72*229152])}
    points=[]
    for (a,b),(order,cone) in expected.items():
        for d in range(order):
            for i in range(d+1):assert shifted_coefficient(coeff,a,b,i,d-i)==0
        got=[shifted_coefficient(coeff,a,b,order-j,j) for j in range(order+1)];assert got==cone and any(got)
        points.append({'x':a,'y':b,'multiplicity':order,'tangent_U_power_descending_coefficients':[str(q) for q in got],
                       'all_lower_total_degree_coefficients_zero':True})
    node_discriminant=2382515**2-4*221760*229152;assert node_discriminant==5473110735145
    quartic=[-11447,-189922,-383037,78878,8278]
    derivative=[i*quartic[i] for i in range(1,len(quartic))]
    res=resultant(quartic[:],derivative[:]);assert res
    out=ROOT/'frontier-20261028-level6-226-curve-singular-points-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'R_certificate_sha256':digest,'points':points,'node_quadratic_discriminant':str(node_discriminant),
            'quadruple_tangent_quartic_resultant_with_derivative':str(res),
            'status':'THREE_EXACT_RATIONAL_AFFINE_SINGULAR_POINTS',
            'scope':'outside physical x,y>=0; destroys smooth-plane genus190 route only; no normalized genus or map-kernel conclusion'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS three exact rational singular points and tangent cones; no smooth-plane genus inference;',out.name,flush=True)

if __name__=='__main__':main()
