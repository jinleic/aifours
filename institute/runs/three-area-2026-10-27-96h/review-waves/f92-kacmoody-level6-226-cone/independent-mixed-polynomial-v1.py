#!/usr/bin/env python3
"""Verify all coefficients of the mixed 34x34 determinant independently."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, math
ROOT=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
HERE=Path(__file__).resolve().parent
pins={'frontier-20261028-level6-free-22-pencil-v1.json':'b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc',
      'frontier-20261028-level6-free-22-determinant-v1.json':'874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'}
for f,h in pins.items(): assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
P=json.loads((ROOT/list(pins)[0]).read_text())
D=json.loads((ROOT/list(pins)[1]).read_text())
coeff={}
for c in D['determinant_coefficients']:
    key=(c['x_power'],c['y_power']); value=Q(c['coefficient'])
    assert key not in coeff and key[0]>=0 and key[1]>=0 and sum(key)<=34 and value
    coeff[key]=value
assert len(coeff)==592
assert sum(v>0 for v in coeff.values())==133 and sum(v<0 for v in coeff.values())==459
pencil=[[[Q(v) for v in cell] for cell in row] for row in P['matrix']]
assert len(pencil)==34 and all(len(row)==34 for row in pencil)
scales=[math.lcm(*(v.denominator for cell in row for v in cell)) for row in pencil]
matrices=[[[int(v*scales[i]) for v in cell] for cell in row] for i,row in enumerate(pencil)]
scale=math.prod(scales)

def det(a):
    a=[row[:] for row in a]; n=len(a); previous=1; sign=1
    for j in range(n-1):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None: return 0
        if pivot!=j: a[j],a[pivot]=a[pivot],a[j];sign=-sign
        p=a[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                num=a[i][k]*p-a[i][j]*a[j][k]
                q,r=divmod(num,previous)
                assert not r
                a[i][k]=q
            a[i][j]=0
        previous=p
    return sign*a[-1][-1]

def expected(x,y):
    # Evaluate by Horner in x then y, for exact integer/rational arithmetic.
    total=Q(0)
    for i in range(34,-1,-1):
        yi=Q(0)
        for j in range(34-i,-1,-1): yi=yi*y+coeff.get((i,j),0)
        total=total*x+yi
    return total

N=0
for x in range(35):
    for y in range(35-x):
        mat=[[a+b*x+c*y for a,b,c in row] for row in matrices]
        value=det(mat)
        assert Q(value,scale)==expected(x,y),(x,y)
        N+=1
assert N==630
# Unisolvence: if a polynomial of degree <=34 vanishes on this triangle,
# it vanishes on y=0 at 35 points, hence is divisible by y; iterating
# on y=1,2,... proves the zero polynomial.  Thus the coefficient list is exact.
result={'determinant_degree_upper_bound':34,'triangular_grid_points':N,
        'grid_domain':'x,y nonnegative integers; x+y<=34',
        'positive_coefficients':133,'negative_coefficients':459,'total_nonzero_coefficients':592,
        'constant':str(coeff[(0,0)]),'positive_witness_x16':str(coeff[(16,0)]),
        'input_sha256':pins,'method':'own integer Bareiss determinants vs claimed polynomial at all 630 unisolvent points'}
with (HERE/'independent-mixed-polynomial-v1.json').open('x') as f: json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2),flush=True)
