#!/usr/bin/env python3
"""Produce independent integer permutation-span minors for n=2 and n=4.

No author code or FLINT is used. The saved witness supplies candidate row
indices; the permutation matrix entries and exact Bareiss determinants are
rebuilt directly from the literal replica-permutation action.
"""
import hashlib
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
WIT=ROOT/'frontier-20261028-local-commutant-pivot-rows.json'
OUT=ROOT/'frontier-20261028-permutation-span-integer-minors-results.json'
EXPECTED='1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4'
P=65521
PERMS=list(itertools.permutations(range(4)))


def coordinates(n):
    blocks={}
    for x in itertools.product(range(n),repeat=4):
        wt=tuple(x.count(i) for i in range(n));blocks.setdefault(wt,[]).append(x)
    return [(x,y) for wt in sorted(blocks) for x in blocks[wt] for y in blocks[wt]]


def image(p,y):
    x=[None]*4
    for i,j in enumerate(p):x[j]=y[i]
    return tuple(x)


def choose_columns(M,r,p):
    A=[row[:] for row in M]; cols=list(range(len(M[0])))
    for k in range(r):
        pos=next(((i,j) for i in range(k,r) for j in range(k,len(cols)) if A[i][j]%p),None)
        if pos is None:raise ValueError('row minor rank insufficient')
        i,j=pos;A[k],A[i]=A[i],A[k]
        for row in A:row[k],row[j]=row[j],row[k]
        cols[k],cols[j]=cols[j],cols[k]
        inv=pow(A[k][k]%p,-1,p)
        for i in range(k+1,r):
            fac=A[i][k]*inv%p
            for j in range(k,len(cols)):A[i][j]=(A[i][j]-fac*A[k][j])%p
    return cols[:r]


def bareiss_det(M):
    A=[row[:] for row in M];n=len(A);previous=1;sign=1
    for k in range(n-1):
        if A[k][k]==0:
            swap=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if swap is None:return 0
            A[k],A[swap]=A[swap],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pivot*A[i][j]-A[i][k]*A[k][j]
                value,remainder=divmod(numerator,previous)
                if remainder:raise ArithmeticError('Bareiss nonexact division')
                A[i][j]=value
        for i in range(k+1,n):A[i][k]=0
        previous=pivot
    return sign*A[-1][-1] if n else 1


def main():
    raw=WIT.read_bytes();h=hashlib.sha256(raw).hexdigest()
    if h!=EXPECTED:raise ValueError('witness digest mismatch')
    data=json.loads(raw);case=next(x for x in data['cases'] if x['dimension']==2)
    coords=coordinates(2);rows=[coords[i] for i in case['permutation_pivot_columns']]
    if len(rows)!=14:raise ValueError('unexpected n2 pivot-row count')
    wide=[[int(x==image(p,y)) for p in PERMS] for x,y in rows]
    chosen=choose_columns(wide,14,P)
    M=[[row[j] for j in chosen] for row in wide]
    det=bareiss_det(M)
    broken=[r[:] for r in M]
    for row in broken:row[-1]=row[0]
    duplicate_det=bareiss_det(broken)
    # n=4: all four basis labels occur once; every permutation produces a distinct row.
    y=tuple(range(4));rows4=sorted(image(p,y) for p in PERMS)
    M4=[[int(x==image(p,y)) for p in PERMS] for x in rows4]
    det4=bareiss_det(M4)
    ok=det!=0 and duplicate_det==0 and abs(det4)==1
    result={'kind':'explicit_integer_permutation_span_minors','witness_sha256':h,
            'n2':{'row_labels':[[list(x),list(y)] for x,y in rows],
                  'selected_permutations':[list(PERMS[j]) for j in chosen],
                  'minor_matrix':M,'exact_bareiss_determinant':det,
                  'duplicate_column_determinant':duplicate_det},
            'n4':{'input_basis_word':list(y),'distinct_output_rows':len(set(rows4)),
                  'minor_order':24,'exact_bareiss_determinant':det4},
            'method':'Direct 0/1 permutation actions and exact integer Bareiss determinants; no author code or FLINT.',
            'scope':'Lower bounds on permutation-span dimensions only; combine with independent commutator rank upper bounds to prove exact local spans.',
            'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'n2_determinant':det,'n2_duplicate_determinant':duplicate_det,
                      'n4_determinant':det4,'n4_distinct_rows':len(set(rows4)),
                      'verdict':result['verdict']},sort_keys=True,indent=2))
    return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
