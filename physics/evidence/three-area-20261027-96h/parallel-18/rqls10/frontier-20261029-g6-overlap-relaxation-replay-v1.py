#!/usr/bin/env python3
"""Exact rational PSD/overlap-relaxation replay; no ray realization claimed."""
import datetime,hashlib,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
w=P/'frontier-20261029-g6-overlap-relaxation-witness-v1.json';wr=w.read_bytes()
assert hashlib.sha256(wr).hexdigest()=='ab38d176f88cfab17307e31ae75b254a7ad3790d9bf097e5afbdb7f79ee64c01';D=json.loads(wr)
c=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';cr=c.read_bytes()
assert hashlib.sha256(cr).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd'
G=[set()for _ in range(15)]
for z in json.loads(cr)['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;G[u].add(v);G[v].add(u)
assert all(len(s)==6 for s in G)
E=[tuple(q)for q in D['edge_order']];assert len(E)==len(set(E))==45 and set(E)=={(i,j)for i in range(15)for j in G[i]if i<j}
Q=D['squared_overlap_candidate_numerator_matrix'];den=D['denominator'];assert den==20000 and len(Q)==45 and all(len(row)==45 for row in Q)
for i in range(45):
 assert Q[i][i]==den
 for j in range(45):
  assert Q[i][j]==Q[j][i] and 0<=Q[i][j]<=den
  if i!=j:
   if set(E[i])&set(E[j]):assert Q[i][j]==0
   else:assert 0<Q[i][j]<den
 for v in range(15):assert sum(Q[i][j]for j,e in enumerate(E)if v in e)==den
 assert sum(Q[i])==15*den//2
# Exact symmetric Schur complements: nonnegative pivots, and each zero pivot has zero residual row.
A=[[F(x)for x in row]for row in Q];positive=[];zeros=[]
for k in range(45):
 p=A[k][k]
 if not p:
  assert all(A[k][j]==0 for j in range(k+1,45));zeros.append(k);continue
 assert p>0;positive.append(k)
 for i in range(k+1,45):
  for j in range(i,45):A[i][j]-=A[i][k]*A[k][j]/p
  for j in range(i+1,45):A[j][i]=A[i][j]
assert len(positive)==31 and len(zeros)==14
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'witness_sha256':hashlib.sha256(wr).hexdigest(),
 'core_sha256':hashlib.sha256(cr).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'dimension':45,'denominator':den,'exact_psd':True,'rank':len(positive),'zero_pivots':len(zeros),
 'edge_orthogonality_and_strict_nonedges':True,'context_sum_checks':45*15,'each_row_sum':'15/2',
 'scope':'necessary squared-projector-overlap constraints only; not a 6D rank-one projector realization','status':'PASS'}
(P/'frontier-20261029-g6-overlap-relaxation-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
