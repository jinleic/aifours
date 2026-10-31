#!/usr/bin/env python3
"""Exact Gaussian-integer verification of the qubit Pauli/swap identity.

No sampled state, floating point, numerical integration, source verifier or
q3 claim. Arithmetic pairs are exact Python integers representing a+ib.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-local-eb-pauli-swap-check-results.json'
Z=(0,0);O=(1,0);M=(-1,0);I=(0,1);MI=(0,-1)


def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def plus(A,B):return [[add(A[i][j],B[i][j]) for j in range(4)] for i in range(4)]
def kron(A,B):return [[mul(A[i//2][j//2],B[i%2][j%2]) for j in range(4)] for i in range(4)]

ident=[[O,Z],[Z,O]];sx=[[Z,O],[O,Z]];sy=[[Z,MI],[I,Z]];sz=[[O,Z],[Z,M]]
I4=kron(ident,ident);F=[[O if (i//2==j%2 and i%2==j//2) else Z for j in range(4)] for i in range(4)]
paulis=plus(plus(kron(sx,sx),kron(sy,sy)),kron(sz,sz))
target=[[add((2*F[i][j][0],2*F[i][j][1]),(-I4[i][j][0],-I4[i][j][1])) for j in range(4)] for i in range(4)]
fault=plus(kron(sx,sx),kron(sz,sz))
wrong=[(i,j) for i in range(4) for j in range(4) if paulis[i][j]!=target[i][j]]
faults=[(i,j) for i in range(4) for j in range(4) if fault[i][j]!=target[i][j]]
r={'kind':'exact_qubit_pauli_swap_gaussian_integer_identity',
   'identity':'sigma_x⊗sigma_x + sigma_y⊗sigma_y + sigma_z⊗sigma_z = 2F-I',
   'matrix_entries_checked':16,'mismatches':wrong,'omitted_sigma_y_fault_mismatch_count':len(faults),
   'scope':'Exact Gaussian-integer matrix identity used in the Haar second-moment derivation only. Does not verify a sampled state, entire EB proof, tensor stability, q3 or formal/kernel review.',
   'verdict':'PASS' if not wrong and faults else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
