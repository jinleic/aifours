#!/usr/bin/env python3
"""Independently replay saved modular commutant-rank witnesses.

Reconstructs all indexed rows from their definitions, verifies a prime field,
checks permutation columns via FLINT rank, and uses reverse/max-pivot sparse
elimination for the selected square submatrix. Does not import the generator.
"""
import hashlib
import itertools
import json
import math
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-python-deps'))
import flint
WIT=ROOT/'frontier-20261028-local-commutant-pivot-rows.json'
OUT=ROOT/'frontier-20261028-independent-local-commutant-witness-check-results.json'


def isprime(p):
    return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))


def universe(n):
    words=list(itertools.product(range(n),repeat=4));blocks={}
    for x in words:
        w=tuple(sum(z==i for z in x) for i in range(n));blocks.setdefault(w,[]).append(x)
    coords=[(x,y) for w in sorted(blocks) for x in blocks[w] for y in blocks[w]]
    return words,coords,{v:i for i,v in enumerate(coords)}


def row_from_label(n,label,lookup):
    i,j,x,y=label;x=tuple(x);y=tuple(y)
    if not (0<=i<n and 0<=j<n and i!=j and len(x)==len(y)==4):raise ValueError('bad row label')
    if any(not 0<=v<n for v in x+y):raise ValueError('bad word digit')
    wy=[y.count(z) for z in range(n)];wx=[x.count(z) for z in range(n)]
    if wy[j]==0:raise ValueError('bad raising domain')
    wy[i]+=1;wy[j]-=1
    if wy!=wx:raise ValueError('bad raising target weight')
    row={}
    for slot,v in enumerate(y):
        if v==j:
            z=list(y);z[slot]=i;c=lookup[(x,tuple(z))];row[c]=row.get(c,0)+1
    for slot,v in enumerate(x):
        if v==i:
            z=list(x);z[slot]=j;c=lookup[(tuple(z),y)];row[c]=row.get(c,0)-1
    return {k:v for k,v in row.items() if v}


def independent_rank(rows,p):
    """Max-pivot modular elimination, no normalized rows or source generator."""
    basis={}
    for row0 in reversed(rows):
        row={k:v%p for k,v in row0.items() if v%p}
        while row:
            pivot=max(row)
            if pivot not in basis:
                basis[pivot]=row;break
            br=basis[pivot];a=row[pivot];b=br[pivot]
            keys=set(row)|set(br)
            row={k:v for k in keys if (v:=(b*row.get(k,0)-a*br.get(k,0))%p)}
    return len(basis)


def check_case(c,p):
    n=c['dimension'];words,coords,lookup=universe(n);N=len(coords)
    ps=list(itertools.permutations(range(4)))
    data=[0]*(N*len(ps));perm_support=[]
    for j,perm in enumerate(ps):
        support=set()
        for y in words:
            x=[None]*4
            for i,t in enumerate(perm):x[t]=y[i]
            loc=lookup[(tuple(x),y)];data[loc*len(ps)+j]=1;support.add(loc)
        perm_support.append(support)
    prank=flint.nmod_mat(N,len(ps),data,p).rank()
    cols=c['pivot_columns'];labels=c['witness_rows'];target=N-prank
    if c['replicas']!=4 or c['modulus']!=p or c['commutant_unknowns']!=N:
        raise ValueError('witness metadata mismatch')
    if len(cols)!=target or len(set(cols))!=target or len(labels)!=target:
        raise ValueError('witness row/column count mismatch')
    if any(not 0<=v<N for v in cols):raise ValueError('column out of range')
    rows=[row_from_label(n,label,lookup) for label in labels]
    if any(sum(row.get(k,0) for k in support)%p for row in rows for support in perm_support):
        raise ValueError('permutation fails a witnessed commutator constraint')
    chosen={col:i for i,col in enumerate(cols)}
    square=[{chosen[k]:v for k,v in row.items() if k in chosen} for row in rows]
    rank=independent_rank(square,p)
    if rank!=target:raise ValueError('independent square rank failed')
    if n==2:
        mutated=list(square);mutated[-1]=mutated[0]
        mutation_rank=independent_rank(mutated,p)
        if mutation_rank>=target:raise ValueError('duplicate-row control failed')
    else:mutation_rank=None
    return {'dimension':n,'unknowns':N,'permutation_rank_mod_p':prank,
            'constraint_witness_rank_mod_p':rank,'nullity_upper_bound':N-rank,
            'duplicate_row_control_rank':mutation_rank,'permutation_kernel_check':'PASS'}


def main():
    start=time.monotonic();raw=WIT.read_bytes();w=json.loads(raw);p=w['prime']
    if not isprime(p):raise ValueError('modulus is not prime')
    if sorted(x['dimension'] for x in w['cases'])!=[2,4]:raise ValueError('dimensions missing')
    results=[check_case(c,p) for c in w['cases']]
    receipt={'kind':'independent_local_commutant_modular_witness_replay',
             'witness_sha256':hashlib.sha256(raw).hexdigest(),'modulus':p,'prime_trial_division':'PASS',
             'cases':results,'elapsed_seconds':round(time.monotonic()-start,3),
             'method':'Reconstructed integer constraint rows; reverse/max-pivot sparse field elimination; FLINT modular permutation-column rank; selected-row kernel checks; duplicate-row negative control.',
             'scope':'Exact modular ranks bound characteristic-zero local commutants when combined with the universal derivative and permutation-invariance proof; no full target theorem adoption.',
             'verdict':'PASS'}
    OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True,indent=2));return 0


if __name__=='__main__':raise SystemExit(main())
