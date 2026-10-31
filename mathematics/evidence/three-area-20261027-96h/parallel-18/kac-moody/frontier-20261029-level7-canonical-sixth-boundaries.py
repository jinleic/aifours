#!/usr/bin/env python3
"""Exact sixth-boundary restrictions of completed full canonical certificates.

Requires the actual complete independent source/matrix/polynomial replay first.
For each canonical degree, set x=-1 or y=-1 in the certified two-variable
polynomial. A one-sign nonzero-constant univariate restriction proves the
ENTIRE corresponding boundary ray. Check the restriction at a shifted full
unisolvent set against the original canonical matrix, plus the corner(-1,-1).
Actual source transport under the added level7 seed remains a written input.
"""
import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--types',nargs='+',default=['22','32','24'])
    args=ap.parse_args()
    assert len(args.types)==len(set(args.types)) and set(args.types)=={'22','32','24'}
    records=[]
    for ab in args.types:
        names=[f'frontier-20261029-level7-{ab}-canonical-{suffix}-v1.json' for suffix in ('contraction-pencil','determinant','independent-replay')]
        documents=[]
        pins=[]
        for name in names:
            raw=(ROOT/name).read_bytes()
            documents.append(json.loads(raw))
            pins.append({'file':name,'sha256':hashlib.sha256(raw).hexdigest()})
        C,P,R=documents
        assert R['status']=='PASS_ENTIRE_CANONICAL_SOURCE_MATRIX_AND_WHOLE_QUADRANT_POLYNOMIAL'
        assert R['canonical_pencil_sha256']==P['pencil_sha256']==pins[0]['sha256']
        assert R['canonical_polynomial_sha256']==pins[1]['sha256']
        k=C['entire_primitive_dimension']
        co={(t['x_power'],t['y_power']):Q(t['coefficient']) for t in P['coefficients']}
        assert len(co)==len(P['coefficients']) and all(i>=0 and j>=0 and i+j<=k for i,j in co)
        matrix=[[[Q(c) for c in e] for e in row] for row in C['matrix']]
        scales=[math.lcm(*(c.denominator for e in row for c in e)) for row in matrix]
        denominator=math.prod(scales)
        integers=[[[int(c*s) for c in e] for e in row] for row,s in zip(matrix,scales)]
        def determinant(x,y):
            return Q(int(flint.fmpz_mat([[a+x*b+y*c for a,b,c in row] for row in integers]).det()),denominator)
        boundaries=[]
        for fixed in ('x','y'):
            cs=[Q(0)]*(k+1)
            for (i,j),c in co.items():
                cs[j if fixed=='x' else i]+=c*(-1)**(i if fixed=='x' else j)
            while cs and cs[-1]==0:
                cs.pop()
            assert cs and cs[0] and (all(c>=0 for c in cs) or all(c<=0 for c in cs)), 'canonical boundary not one-sign'
            for t in range(1,k+2):
                actual=determinant(-1,t) if fixed=='x' else determinant(t,-1)
                assert actual==sum(c*t**i for i,c in enumerate(cs))
            boundaries.append({'fixed_variable':fixed,'fixed_value':-1,'remaining_variable':'t=other_parameter-7',
                               'restriction_coefficients_low_to_high':[str(c) for c in cs],
                               'nonzero_constant':str(cs[0]),'all_coefficients_one_weak_sign':True,
                               'independent_full_shifted_matrix_grid':k+1,'claim':'nonzero for ALL real t>=0'})
        corner=sum(c*(-1)**(i+j) for (i,j),c in co.items())
        assert corner and determinant(-1,-1)==corner
        records.append({'degree':C['degree'],'entire_source_dimension':k,'inputs':pins,'boundaries':boundaries,
                        'exact_sixth_corner_determinant':str(corner),'status':'PASS_BOTH_ENTIRE_SIXTH_RAYS_AND_CORNER'})
        print('PASS canonical sixth rays',C['degree'],'grid',2*(k+1),'corner nonzero',flush=True)
    out=ROOT/'frontier-20261029-level7-canonical-sixth-boundaries-v1.json'
    with out.open('x') as stream:
        json.dump({'owner':'MathKacMoody-2','records':records,'status':'PASS_THREE_COMPLETE_GRADE7_TYPES_SIXTH_BOUNDARIES',
                   'limits':'exact restrictions of independently reconstructed canonical source polynomials, shared FLINT arithmetic; actual level7 seed types(5,8)/(8,5) differ from the checked types(5,5),(3,6),(7,1). Written source/seed transport, scientific review and parent disposition remain substantive gates. No whole-level7/B7, formal/kernel or novelty acceptance.'},stream,indent=2)
        stream.write('\n')
    print('WROTE',out.name,flush=True)


if __name__=='__main__':
    main()
