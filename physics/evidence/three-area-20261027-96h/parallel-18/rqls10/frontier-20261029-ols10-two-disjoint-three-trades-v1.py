#!/usr/bin/env python3
"""Search two disjoint 3+3 color trades in OLS10, not common A-subsquares.
SAT needs independent exact replay; UNKNOWN is no conclusion.
"""
import datetime,hashlib,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;N=10;S=z3.Solver();S.set(timeout=120000,random_seed=47)
A=[[z3.Int(f'A{r}_{c}')for c in range(N)]for r in range(N)];L=[[z3.Int(f'L{r}_{c}')for c in range(N)]for r in range(N)]
for r in range(N):
 for c in range(N):S.add(A[r][c]>=0,A[r][c]<N,L[r][c]>=0,L[r][c]<N)
 S.add(z3.Distinct(A[r]),z3.Distinct(L[r]))
for c in range(N):S.add(z3.Distinct([A[r][c]for r in range(N)]),z3.Distinct([L[r][c]for r in range(N)]))
S.add(z3.Distinct([N*A[r][c]+L[r][c]for r in range(N)for c in range(N)]))
for r in range(3):
 for c in range(3):S.add(L[r][c]==(r+c)%3)
for st,aa,bb in [(0,0,1),(3,2,3)]:
 for i in range(3):S.add(A[st+i][st+i]==aa,A[st+i][st+(i+1)%3]==bb)
T=[z3.Int('T%d'%i)for i in range(3)];S.add(0<=T[0],T[0]<T[1],T[1]<T[2],T[2]<N)
for r in range(3,6):
 for c in range(3,6):S.add(z3.Or(*[L[r][c]==t for t in T]))
start=time.monotonic();v=S.check();elapsed=time.monotonic()-start
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver':'Z3 '+z3.get_version_string(),'timeout_ms':120000,'elapsed_seconds':round(elapsed,6),'status':str(v),'unknown_reason':S.reason_unknown()if v==z3.unknown else None,
 'scope':'Two 3+3 orthogonality-component color trades with disjoint colors/rows/cols, L has 3-subsquares, A need not. Bounded solver search only.'}
if v==z3.sat:
 m=S.model();obj['A']=[[m.eval(A[r][c]).as_long()for c in range(N)]for r in range(N)];obj['L']=[[m.eval(L[r][c]).as_long()for c in range(N)]for r in range(N)];obj['T']=[m.eval(t).as_long()for t in T]
(P/'frontier-20261029-ols10-two-disjoint-three-trades-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
