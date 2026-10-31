#!/usr/bin/env python3
"""Bounded exact Z3 search for two 3x3 common subsquares in OLS(10).
SAT requires independent replay; UNKNOWN is no conclusion, UNSAT solver-scoped.
"""
import datetime,hashlib,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;N=10;S=z3.Solver();S.set(timeout=60000,random_seed=17)
A=[[z3.Int(f'A{r}_{c}')for c in range(N)]for r in range(N)];L=[[z3.Int(f'L{r}_{c}')for c in range(N)]for r in range(N)]
for r in range(N):
 for c in range(N):S.add(A[r][c]>=0,A[r][c]<N,L[r][c]>=0,L[r][c]<N)
 S.add(z3.Distinct(A[r]),z3.Distinct(L[r]))
for c in range(N):S.add(z3.Distinct([A[r][c]for r in range(N)]),z3.Distinct([L[r][c]for r in range(N)]))
S.add(z3.Distinct([N*A[r][c]+L[r][c]for r in range(N)for c in range(N)]))
# Permute rows/cols/symbols so two disjoint subsquares occupy [0,3),[3,6)
# and color symbol sets [0,3),[3,6). Their L-symbol sets are not assumed disjoint.
for st in (0,3):
 for r in range(st,st+3):
  for c in range(st,st+3):S.add(A[r][c]>=st,A[r][c]<st+3)
# Normalize first block's A and L to the two orthogonal Z3 tables.
for r in range(3):
 for c in range(3):S.add(A[r][c]==(r+c)%3,L[r][c]==(r+2*c)%3)
# L on second block has one fixed but arbitrary three-symbol set; sorted representatives remove symmetry.
T=[z3.Int('T%d'%i)for i in range(3)];S.add(0<=T[0],T[0]<T[1],T[1]<T[2],T[2]<N)
for r in range(3,6):
 for c in range(3,6):S.add(z3.Or(*[L[r][c]==t for t in T]))
# Normalize A within the second block by relabeling its rows/cols and symbols.
for r in range(3,6):
 for c in range(3,6):S.add(A[r][c]==3+(r-3+c-3)%3)
start=time.monotonic();v=S.check();sec=time.monotonic()-start
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver':'Z3 '+z3.get_version_string(),'timeout_ms':60000,'elapsed_seconds':round(sec,6),'status':str(v),'unknown_reason':S.reason_unknown()if v==z3.unknown else None,
 'scope':'Two row/column/symbol-disjoint common 3x3 subsquares of OLS10 under displayed normalization; UNKNOWN is no conclusion.'}
if v==z3.sat:
 m=S.model();obj['A']=[[m.eval(A[r][c]).as_long()for c in range(N)]for r in range(N)];obj['L']=[[m.eval(L[r][c]).as_long()for c in range(N)]for r in range(N)];obj['T']=[m.eval(t).as_long()for t in T]
(P/'frontier-20261029-ols10-two-common3-solver-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
