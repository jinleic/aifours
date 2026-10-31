#!/usr/bin/env python3
"""Exact incidence determinant and inverse for the graph triangle balancing map."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-triangle-balance-matrix-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    tr=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    if len(tr)!=10 or len(set(tr))!=10:raise ValueError('TRIANGLES')
    if any(any(y not in N[x] for x,y in combinations(t,2)) for t in tr):raise ValueError('NONEDGE')
    A=[[int(v in t) for t in tr] for v in range(1,11)]
    if [sum(row) for row in A]!=[3]*10:raise ValueError('REGULAR_COVER')
    aug=[[Fraction(x) for x in row]+[Fraction(int(i==j)) for j in range(10)] for i,row in enumerate(A)]
    det=Fraction(1)
    for j in range(10):
        p=next((i for i in range(j,10) if aug[i][j]),None)
        if p is None:raise ValueError('SINGULAR')
        if p!=j:aug[j],aug[p]=aug[p],aug[j];det=-det
        pivot=aug[j][j];det*=pivot;aug[j]=[x/pivot for x in aug[j]]
        for i in range(10):
            if i==j:continue
            q=aug[i][j]
            if q:aug[i]=[x-q*y for x,y in zip(aug[i],aug[j])]
    inv=[row[10:] for row in aug]
    if any(sum(Fraction(A[i][k])*inv[k][j] for k in range(10))!=int(i==j)
           for i in range(10) for j in range(10)):raise ValueError('INVERSE')
    if abs(det)!=3:raise ValueError(('DET',str(det)))
    out={'baseline_result_sha256':EXPECTED,'incidence_matrix':A,'determinant':str(det),
         'inverse':[[str(x) for x in row] for row in inv],
         'A_times_ones':[sum(row) for row in A],'inverse_exactly_checked':True,
         'limits':'Establishes an incidence-balancing lemma; no entropy-law counterexample or improved guessing number is claimed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'determinant':str(det),'inverse_exactly_checked':True,'triangles':tr},indent=2))


if __name__=='__main__':main()
