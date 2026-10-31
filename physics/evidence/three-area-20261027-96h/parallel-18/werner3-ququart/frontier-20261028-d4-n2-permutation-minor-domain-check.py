#!/usr/bin/env python3
"""Check actual n=2 permutation-minor row domain and a relabeling fault.

Independent stdlib source-witness check; no physical target state or source
certificate execution. The old-checker behavior is simulated from its written
index/determinant guards, not run or modified.
"""
import copy
import hashlib
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'frontier-20261028-permutation-span-integer-minors-results.json'
PIN='b8996e8f6fb9103be8ce6daa4798b0d5440c5544483ebf30c0ed8609c486e426'
OUT=ROOT/'frontier-20261028-d4-n2-permutation-minor-domain-check-results.json'
PERMS=set(itertools.permutations(range(4)))

def domain(rows,n):
    return all(len(x)==len(y)==4 and all(type(v)==int and 0<=v<n for v in x+y)
               and sorted(x)==sorted(y) for x,y in rows)

def image(p,y):
    out=[0]*4
    for i in range(4):out[p[i]]=y[i]
    return tuple(out)

def matrix(rows,ps):return [[int(tuple(x)==image(p,tuple(y))) for p in ps] for x,y in rows]

def bareiss(M):
    A=[r[:] for r in M];n=len(A);prev=1;sign=1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((i for i in range(k+1,n) if A[i][k]),None)
            if q is None:return 0
            A[k],A[q]=A[q],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value,rem=divmod(pivot*A[i][j]-A[i][k]*A[k][j],prev)
                if rem:raise ArithmeticError('non-exact division')
                A[i][j]=value
        for i in range(k+1,n):A[i][k]=0
        prev=pivot
    return sign*A[-1][-1] if n else 1

def shape_and_domain(rows,ps,n):
    return len(rows)==len(ps)==14 and len({tuple(p) for p in ps})==14 and all(tuple(p) in PERMS for p in ps) and domain(rows,n)

raw=SRC.read_bytes()
if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('minor witness SHA mismatch')
data=json.loads(raw)['n2'];rows=[(tuple(x),tuple(y)) for x,y in data['row_labels']];ps=[tuple(p) for p in data['selected_permutations']]
M=matrix(rows,ps);actual_domain=shape_and_domain(rows,ps,2);det=bareiss(M)
if M!=data['minor_matrix']:raise ValueError('literal minor differs from pinned witness')
# A consistent alphabet relabel preserves equality and hence the old 0/1
# matrix/determinant, but destroys membership in the actual C^2 tensor basis.
relabel=[(tuple(v+2 for v in x),tuple(v+2 for v in y)) for x,y in rows]
old_style_accepts_relabel=(len(relabel)==14 and len(set(ps))==14 and all(p in PERMS for p in ps) and matrix(relabel,ps)==data['minor_matrix'] and bareiss(matrix(relabel,ps)) in (-1,1))
weight_fault=copy.deepcopy(rows);x,y=weight_fault[0];weight_fault[0]=(tuple([0,1,1,1]),y)
duplicate=copy.deepcopy(rows);duplicate[-1]=duplicate[0]
controls={'relabel_out_of_domain_rejected':not shape_and_domain(relabel,ps,2),
          'wrong_weight_rejected':not shape_and_domain(weight_fault,ps,2),
          'duplicate_row_determinant_zero':bareiss(matrix(duplicate,ps))==0}
ok=actual_domain and det==-1 and old_style_accepts_relabel and all(controls.values())
r={'kind':'exact_n2_permutation_minor_domain_audit','witness_sha256':PIN,
   'rows':len(rows),'columns':len(ps),'all_rows_actual_C2_four_replica_same_weight':actual_domain,
   'literal_minor_matches_witness':M==data['minor_matrix'],'exact_integer_determinant':det,
   'simulated_old_guard_accepts_consistent_out_of_domain_relabel':old_style_accepts_relabel,
   'fault_controls_detected':controls,
   'scope':'Actual n=2 permutation-minor row-domain and determinant only. The old pinned data are valid; the deliberately relabeled witness is an in-memory guard fault, not a physical counterexample. Constraint minor/n4/source theorem remain separate.',
   'verdict':'PASS' if ok else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if ok else 1)
