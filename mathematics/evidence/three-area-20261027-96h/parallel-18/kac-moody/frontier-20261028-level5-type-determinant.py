#!/usr/bin/env python3
"""Exact complete determinant of a level-five affine full-source pencil.

Each 19x19 entry is affine in x,y, so total degree <=19.  All integer
triangular grid points i+j<=19 determine the polynomial.  Fraction-free
integer Bareiss determinants, exact 2-D Newton finite differences and
falling-factorial conversion recover EVERY rational monomial coefficient.
No sampling inference: the degree bound and unisolvent grid are essential.
"""
import argparse
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def bareiss(rows):
    n=len(rows); a=[row[:] for row in rows];previous=1;sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pk=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pk-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
            a[i][k]=0
        previous=pk
    return sign*a[-1][-1]


def falling_binomial(k):
    poly=[Q(1)]
    for i in range(k):
        new=[Q(0)]*(len(poly)+1)
        for j,c in enumerate(poly):new[j]-=i*c;new[j+1]+=c
        poly=new
    return [v/math.factorial(k) for v in poly]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args();a,b=args.a,args.b
    inp=ROOT/f'frontier-20261028-level5-free-{a}{b}-pencil-v1.json'
    out=ROOT/f'frontier-20261028-level5-free-{a}{b}-determinant-v1.json'
    if out.exists():raise FileExistsError(out)
    p=json.loads(inp.read_text(encoding='utf-8'))
    assert p['status']=='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    raw=[[[Q(x) for x in entry] for entry in row] for row in p['matrix']]
    n=len(raw);assert all(len(row)==n for row in raw)
    row_scales=[math.lcm(*(q.denominator for entry in row for q in entry)) for row in raw]
    data=[[[int(q*row_scales[i]) for q in entry] for entry in row] for i,row in enumerate(raw)]
    scale=math.prod(row_scales)
    values={}
    for i in range(n+1):
        for j in range(n+1-i):
            A=[[v[0]+i*v[1]+j*v[2] for v in row] for row in data]
            values[i,j]=Q(bareiss(A),scale)
        print('grid row',i,'of',n,flush=True)
    newton={}
    for i in range(n+1):
        for j in range(n+1-i):
            newton[i,j]=sum((-1)**(i+j-u-v)*math.comb(i,u)*math.comb(j,v)*values[u,v]
                            for u in range(i+1) for v in range(j+1))
    bases=[falling_binomial(i) for i in range(n+1)]
    powers=defaultdict(Q)
    for (i,j),q in newton.items():
        for u,cu in enumerate(bases[i]):
            for v,cv in enumerate(bases[j]):powers[u,v]+=q*cu*cv
    powers={k:q for k,q in powers.items() if q}
    assert all(i+j<=n for i,j in powers)
    for (x,y),v in values.items():
        assert sum(q*x**i*y**j for (i,j),q in powers.items())==v
    signs=sorted({1 if q>0 else -1 for q in powers.values()})
    result={'degree':p['degree'],'matrix_size':n,'variables':p['variables'],'evaluations':len(values),
            'total_degree_bound':n,'row_scales':row_scales,'all_triangular_grid_values_reconstructed':True,
            'determinant_coefficients':[{'x_power':i,'y_power':j,'coefficient':str(q)} for (i,j),q in sorted(powers.items())],
            'signs':signs,'constant_coefficient':str(powers.get((0,0),0)),
            'status':'ONE_SIGN_ALL_ORTHANT' if len(signs)==1 and powers.get((0,0),0) else 'MIXED_OR_ZERO_CONSTANT',
            'scope':'free-model selected minor; actual quotient/source representation is a separate obligation',
            'not_formal_or_independent_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('DONE',p['degree'],'size',n,'grid',len(values),'terms',len(powers),'signs',signs,result['status'],out.name,flush=True)

if __name__=='__main__':main()
