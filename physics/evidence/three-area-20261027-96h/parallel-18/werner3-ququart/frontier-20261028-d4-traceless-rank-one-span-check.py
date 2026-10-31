#!/usr/bin/env python3
"""Exact basis check: traceless rank-one matrices span sl_4(C).

Fixed matrices are auxiliary symbolic linear functionals, not selected
original q3 inputs or numerical state-control probes.
"""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-traceless-rank-one-span-check-results.json'
n=4

def outer(x,y):return [x[i]*y[j] for i in range(n) for j in range(n)]
def rank(rows):
    if not rows:return 0
    A=[[F(v) for v in row] for row in rows];m=len(A);cols=len(A[0]);r=0
    for c in range(cols):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];q=A[r][c];A[r]=[v/q for v in A[r]]
        for i in range(r+1,m):
            q=A[i][c]
            if q:A[i]=[u-q*v for u,v in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

basis=[[int(i==j) for i in range(n)] for j in range(n)]
terms=[];off=[]
for i,j in itertools.permutations(range(n),2):
    x=basis[i];y=basis[j];off.append(outer(x,y));terms.append((x,y))
for j in range(1,n):
    x=[basis[0][a]+basis[j][a] for a in range(n)]
    y=[basis[0][a]-basis[j][a] for a in range(n)]
    terms.extend([(x,y),(y,x)])
matrices=[outer(x,y) for x,y in terms]
orthogonal=all(sum(x[i]*y[i] for i in range(n))==0 for x,y in terms)
rankone=all(rank([[m[i*n+j] for j in range(n)] for i in range(n)])==1 for m in matrices)
traceless=all(sum(m[i*n+i] for i in range(n))==0 for m in matrices)
span=rank(matrices);offrank=rank(off)
r={'kind':'exact_sl4_rank_one_traceless_span','vectors':len(terms),
   'all_pairs_orthogonal':orthogonal,'all_matrices_rank_one':rankone,'all_matrices_traceless':traceless,
   'span_rank':span,'sl4_dimension':n*n-1,'offdiagonal_only_fault_span_rank':offrank,
   'fault_detected':offrank<span,
   'scope':'Auxiliary linear-functional span identity only; no original q3 state, low-rank proof review, q3/PPT or source novelty is inferred.',
   'verdict':'PASS' if orthogonal and rankone and traceless and span==n*n-1 and offrank<span else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
