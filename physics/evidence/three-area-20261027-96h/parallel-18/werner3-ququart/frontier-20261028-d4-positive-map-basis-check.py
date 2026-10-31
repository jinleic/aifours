#!/usr/bin/env python3
"""Integer basis check of the d4 positive-map decomposition and Choi spectrum.

All 16 elementary matrices are tested; no physical C or state is chosen.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-positive-map-basis-check-results.json'
n=4

def Z():return [[0]*n for _ in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]
def trans(a):return [list(x) for x in zip(*a)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def eu(i,j):
    a=Z();a[i][j]=1;return a

E=[eu(i,j) for i in range(n) for j in range(n)]
K=[sub(eu(i,j),eu(j,i)) for i in range(n) for j in range(i+1,n)]
def cp_sum(X,ks):
    out=Z()
    for a in ks:out=add(out,mul(mul(a,X),trans(a)))
    return out

def directD(X):
    t=sum(X[i][i] for i in range(n));return [[int(i==j)*t for j in range(n)] for i in range(n)]

checks={'trace_channel':0,'antisymmetric_kraus':0,'phi_equals_transpose_psi':0}
controls={'missing_antisymmetric_kraus_detected':0,'wrong_transpose_detected':0}
for X in E:
    D=directD(X);A=sub(D,trans(X))
    checks['trace_channel']+=cp_sum(X,E)==D
    checks['antisymmetric_kraus']+=cp_sum(X,K)==A
    # 2 Phi=2D-X and 2 Psi=D+A=2D-X^T.
    twoPhi=sub(add(D,D),X);twoPsi=add(D,A)
    checks['phi_equals_transpose_psi']+=twoPhi==trans(twoPsi)
    controls['missing_antisymmetric_kraus_detected']+=cp_sum(X,K[:-1])!=A
    controls['wrong_transpose_detected']+=twoPhi!=twoPsi

# 2J=2I-|Omega><Omega|; (2J)^2=4I, so J²=I.
m=n*n;omega=[int(i//n==i%n) for i in range(m)]
twoJ=[[2*int(i==j)-omega[i]*omega[j] for j in range(m)] for i in range(m)]
I4=[[4*int(i==j) for j in range(m)] for i in range(m)]
square=[[sum(twoJ[i][k]*twoJ[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
twotrace=sum(twoJ[i][i] for i in range(m))
if twotrace%2:raise ValueError('nonintegral trace')
trace=twotrace//2;cube_dim=m**3;cube_trace=trace**3
plus=(cube_dim+cube_trace)//2;minus=(cube_dim-cube_trace)//2
ok=all(v==16 for v in checks.values()) and all(v>0 for v in controls.values()) and square==I4 and (plus,minus)==(3420,676)
r={'kind':'full_matrix_basis_positive_map_and_choi_check','dimension':n,'basis_count':len(E),
   'checks_passed_by_basis_count':checks,'fault_detections_by_basis_count':controls,
   'local_choi_involution':square==I4,'local_choi_trace':trace,
   'tensor3_dimension':cube_dim,'tensor3_trace':cube_trace,'positive_eigen_dimension':plus,'negative_eigen_dimension':minus,
   'scope':'Exact integer linear-map/basis identities and Choi dimension arithmetic; not rank-two positivity, general source validity or formal-kernel proof.',
   'verdict':'PASS' if ok else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if ok else 1)
