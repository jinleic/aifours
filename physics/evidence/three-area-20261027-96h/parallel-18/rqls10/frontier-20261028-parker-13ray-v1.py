#!/usr/bin/env python3
"""Exact 13-ray 1-resolvable QLS(10) from Parker's 3x3 subarray.

Uses the integral Householder matrix 3I-2J, divided by 3, only on the
sub-orthogonal-array with all four coordinates in {7,8,9}.
"""
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',HERE/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)
n=10
P=tuple((r,c,int(oa.PARKER_A[r][c]),int(oa.PARKER_B[r][c]))
        for r in range(n) for c in range(n))
oa.check_oa(P)
sub=[q for q in P if all(x in (7,8,9) for x in q)]
assert len(sub)==9
# Color is original Parker row; row/column/transversal are c,A,B.
arr=[]
labels=[]
for row in range(n):
    vecrow=[]
    labelrow=[]
    for col in range(n):
        q=next(q for q in P if q[1]==row and q[2]==col)
        color=q[0]
        v=[0]*n
        if q in sub:
            for d in (7,8,9):
                v[d]=(3 if d==color else 0)-2
        else:
            v[color]=3
        vecrow.append(v)
        labelrow.append(q[3])
    arr.append(vecrow)
    labels.append(labelrow)

certificate={'method':'local 3-dimensional Householder rotation on exact OA(3)',
             'source':'Parker1959 section3, color axis original row',
             'ray_count':13,'denominator':3,'array':arr,'labels':labels}
output=HERE/'frontier-20261028-parker-13ray-result-v1.json'
output.write_text(json.dumps({'partial_witness':certificate},indent=2,sort_keys=True)+'\n')
print('subarray size',len(sub),'generated',output.name)
print('claimed ray count13: MUST independently verify original definition')
