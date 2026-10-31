#!/usr/bin/env python3
"""Exact scaled inverse identities on all 16 local matrix units."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-inverse-map-basis-check-results.json'
n=4

def unit(i,j):return [[int(a==i and b==j) for b in range(n)] for a in range(n)]
def times(k,X):return [[k*x for x in row] for row in X]
def phi2(X):
    tr=sum(X[i][i] for i in range(n))
    return [[2*tr*int(i==j)-X[i][j] for j in range(n)] for i in range(n)]
def inv7(X,trace_factor=4,matrix_factor=14):
    tr=sum(X[i][i] for i in range(n))
    return [[trace_factor*tr*int(i==j)-matrix_factor*X[i][j] for j in range(n)] for i in range(n)]

lr=rl=fault_trace=fault_matrix=0
for i in range(n):
    for j in range(n):
        E=unit(i,j);target=times(14,E)
        lr+=phi2(inv7(E))==target
        rl+=inv7(phi2(E))==target
        fault_trace+=phi2(inv7(E,trace_factor=5))!=target
        fault_matrix+=phi2(inv7(E,matrix_factor=13))!=target
ok=lr==rl==16 and fault_trace>0 and fault_matrix>0
r={'kind':'exact_d4_inverse_map_full_basis_check',
   'basis_count':16,'left_composition_pass_count':lr,'right_composition_pass_count':rl,
   'wrong_trace_factor_detected_basis_count':fault_trace,'wrong_matrix_factor_detected_basis_count':fault_matrix,
   'identity':'2Phi(7Phi^{-1}(E))=7Phi^{-1}(2Phi(E))=14E',
   'scope':'Exact integer verification of the local linear inverse on a full basis; tensor inversion follows algebraically. Not the rank-two contraction or a formal-kernel proof.',
   'verdict':'PASS' if ok else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if ok else 1)
