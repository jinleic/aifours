#!/usr/bin/env python3
"""Independent fraction-free determinant of the LISTED 162x162 matrix.
Does not import, execute, or rely on the author's modular replay.
"""
import hashlib,json,math,subprocess
from fractions import Fraction as Q
from pathlib import Path
R=Path(__file__).resolve().parent
source=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261028-level6-446-leading-map-cone-v1.json')
b=source.read_bytes(); sha=hashlib.sha256(b).hexdigest()
assert sha=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
d=json.loads(b); L=[[Q(entry[0]) for entry in row] for row in d['matrix_entries']]
n=len(L);assert n==162 and all(len(row)==n for row in L)
scales=[math.lcm(*(x.denominator for x in row)) for row in L]
A=[]
for i,row in enumerate(L):
    a=[x*scales[i] for x in row];assert all(x.denominator==1 for x in a)
    A.append([int(x) for x in a])
scale=math.prod(scales); swaps=0; previous=1
for k in range(n-1):
    if A[k][k]==0:
        row=next((j for j in range(k+1,n) if A[j][k]),None)
        assert row is not None,('singular matrix',k)
        A[k],A[row]=A[row],A[k];swaps+=1
    pivot=A[k][k]
    for i in range(k+1,n):
        q=A[i][k]
        for j in range(k+1,n):
            numerator=A[i][j]*pivot-q*A[k][j]
            result,remainder=divmod(numerator,previous)
            assert remainder==0,(k,i,j)
            A[i][j]=result
        A[i][k]=0
    previous=pivot
    if k%30==29:print('Fraction-free pivot',k+1,'of',n,flush=True)
integer_det=(-1 if swaps%2 else 1)*A[-1][-1]
exact=Q(integer_det,scale)
assert exact==Q(d['leading_determinant']) and exact!=0
print('PASS listed leading matrix exact determinant:',exact,flush=True)
r={'clock_before_receipt_creation':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
   'listed_matrix_source_sha256':sha,'dimensions':[n,n],
   'algorithm':'independent pure-integer fraction-free Bareiss elimination after per-row denominator clearing; every division exact',
   'row_swaps':swaps,'row_scale_product':str(scale),
   'row_scaled_integer_determinant':str(integer_det),'rational_determinant':str(exact),
   'scope':'ONLY determinant of listed entries; no reconstruction of source, kernel basis, listed entries, full-Cartan/ideal descent, or cone proof'}
with (R/'independent-446-receipt-v1.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print('PASS exclusive review receipt',flush=True)
