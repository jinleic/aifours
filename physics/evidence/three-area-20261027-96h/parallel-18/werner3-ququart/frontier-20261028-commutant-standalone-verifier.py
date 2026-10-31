#!/usr/bin/env python3
"""Verify d4 certificate's local commutant witnesses using stdlib integers only.

Reconstructs commutator rows and permutation actions from definitions; checks
full-rank minors modulo a proven prime and a unimodular n=2 permutation minor;
checks permutation kernel on ALL commutator rows. No other checker is imported.
"""
import hashlib
import itertools
import json
import math
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
WIT=ROOT/'frontier-20261028-local-commutant-pivot-rows.json'
MINOR=ROOT/'frontier-20261028-permutation-span-integer-minors-results.json'
OUT=ROOT/'frontier-20261028-commutant-standalone-verifier-results.json'
WHASH='1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4'
MHASH='b8996e8f6fb9103be8ce6daa4798b0d5440c5544483ebf30c0ed8609c486e426'
PERMS=list(itertools.permutations(range(4)))


def check_hash(path,want):
    b=path.read_bytes();h=hashlib.sha256(b).hexdigest()
    if h!=want:raise ValueError('pinned input mismatch')
    return json.loads(b)


def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))


def universe(n):
    blocks={}
    for x in itertools.product(range(n),repeat=4):
        wt=tuple(x.count(i) for i in range(n));blocks.setdefault(wt,[]).append(x)
    coords=[(x,y) for wt in sorted(blocks) for x in blocks[wt] for y in blocks[wt]]
    return blocks,coords,{xy:i for i,xy in enumerate(coords)}


def image(p,y):
    out=[0]*4
    for i in range(4):out[p[i]]=y[i]
    return tuple(out)


def constraint(n,i,j,x,y,ids):
    row={}
    if i==j or not (0<=i<n and 0<=j<n):raise ValueError('invalid generator')
    if len(x)!=4 or len(y)!=4 or any(not 0<=v<n for v in x+y):raise ValueError('invalid word')
    yy=[y.count(v) for v in range(n)];xx=[x.count(v) for v in range(n)]
    if yy[j]==0:raise ValueError('empty generator action')
    yy[i]+=1;yy[j]-=1
    if xx!=yy:raise ValueError('incompatible weights')
    for k in range(4):
        if y[k]==j:
            z=list(y);z[k]=i;c=ids[(x,tuple(z))];row[c]=row.get(c,0)+1
        if x[k]==i:
            z=list(x);z[k]=j;c=ids[(tuple(z),y)];row[c]=row.get(c,0)-1
    return {c:v for c,v in row.items() if v}


def modular_rank(rows,p):
    """Sparse normalized max-pivot elimination, rows in reverse order."""
    pivots={}
    for inputrow in reversed(rows):
        row={k:v%p for k,v in inputrow.items() if v%p}
        while row:
            c=max(row)
            if c not in pivots:
                inv=pow(row[c],-1,p)
                pivots[c]={k:(v*inv)%p for k,v in row.items() if (v*inv)%p}
                break
            v=row.pop(c)
            for k,a in pivots[c].items():
                if k==c:continue
                q=(row.get(k,0)-v*a)%p
                if q:row[k]=q
                else:row.pop(k,None)
    return len(pivots)


def bareiss(A):
    A=[r[:] for r in A];n=len(A);prev=1;sign=1
    for k in range(n-1):
        if not A[k][k]:
            t=next((i for i in range(k+1,n) if A[i][k]),None)
            if t is None:return 0
            A[k],A[t]=A[t],A[k];sign=-sign
        v=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z,rem=divmod(v*A[i][j]-A[i][k]*A[k][j],prev)
                if rem:raise ArithmeticError('nonexact determinant division')
                A[i][j]=z
        for i in range(k+1,n):A[i][k]=0
        prev=v
    return sign*A[-1][-1] if n else 1


def verify_permutation_minor(data,n):
    if n==2:
        d=data['n2'];rows=[(tuple(x),tuple(y)) for x,y in d['row_labels']]
        perms=[tuple(p) for p in d['selected_permutations']]
        if len(rows)!=14 or len(set(perms))!=14 or any(p not in PERMS for p in perms):raise ValueError('invalid n2 minor')
        M=[[int(x==image(p,y)) for p in perms] for x,y in rows]
        if M!=d['minor_matrix']:raise ValueError('n2 literal minor mismatch')
        det=bareiss(M)
        if abs(det)!=1:raise ValueError('n2 minor not unimodular')
        return 14,det
    y=tuple(range(4));outputs=[image(p,y) for p in PERMS]
    if len(set(outputs))!=24:raise ValueError('n4 permutation actions not distinct')
    return 24,'universal distinct-output basis argument'


def all_constraint_kernel(n,blocks,ids):
    supports=[]
    for p in PERMS:
        supports.append({ids[(image(p,y),y)] for block in blocks.values() for y in block})
    rows=0
    for w,ys in blocks.items():
        for i in range(n):
            for j in range(n):
                if i==j or not w[j]:continue
                beta=list(w);beta[i]+=1;beta[j]-=1
                for y in ys:
                    for x in blocks[tuple(beta)]:
                        row=constraint(n,i,j,x,y,ids);rows+=1
                        if any(sum(row.get(c,0) for c in supp) for supp in supports):
                            raise ValueError('permutation violates exact integer commutator')
    return rows


def verify_case(case,p,minor):
    n=case['dimension'];blocks,coords,ids=universe(n);N=len(coords)
    r,det=verify_permutation_minor(minor,n)
    target=N-r;cols=case['pivot_columns'];labels=case['witness_rows']
    if case['replicas']!=4 or case['modulus']!=p or case['commutant_unknowns']!=N:
        raise ValueError('witness dimensions mismatch')
    if len(cols)!=target or len(set(cols))!=target or len(labels)!=target:
        raise ValueError('bad selected minor dimensions')
    selected={c:i for i,c in enumerate(cols)}
    rows=[]
    for i,j,x,y in labels:
        full=constraint(n,i,j,tuple(x),tuple(y),ids)
        rows.append({selected[c]:v for c,v in full.items() if c in selected})
    rank=modular_rank(rows,p)
    if rank!=target:raise ValueError('commutator minor rank failure')
    fault=list(rows);fault[-1]=fault[0];fault_rank=modular_rank(fault,p)
    if fault_rank>=target:raise ValueError('duplicate row not detected')
    allrows=all_constraint_kernel(n,blocks,ids)
    return {'n':n,'same_weight_unknowns':N,'permutation_rank_lower':r,
            'permutation_minor':det,'commutator_minor_rank_mod_p':rank,
            'duplicate_row_control_rank':fault_rank,'all_constraint_rows_checked_against_24_permutations':allrows}


def main():
    start=time.monotonic();w=check_hash(WIT,WHASH);m=check_hash(MINOR,MHASH);p=w['prime']
    if not prime(p):raise ValueError('composite modulus')
    cases=sorted(w['cases'],key=lambda x:x['dimension'])
    if [c['dimension'] for c in cases]!=[2,4]:raise ValueError('missing physical dimension')
    rows=[verify_case(c,p,m) for c in cases]
    result={'kind':'stdlib_local_commutant_witness_replay','prime':p,'prime_trial_division':'PASS',
            'witness_sha256':WHASH,'permutation_minor_sha256':MHASH,'cases':rows,
            'elapsed_seconds':round(time.monotonic()-start,3),
            'method':'Standard-library integer rank and Bareiss determinant; full literal commutator/permutation incidence check; no numpy, FLINT, author code or other checker imports.',
            'scope':'Concrete n=2 and n=4 4-replica commutant rank sandwich. The unitary derivative and tensor-product bridge remain written mathematical arguments, not formal-kernel verification.',
            'verdict':'PASS'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2));return 0


if __name__=='__main__':raise SystemExit(main())
