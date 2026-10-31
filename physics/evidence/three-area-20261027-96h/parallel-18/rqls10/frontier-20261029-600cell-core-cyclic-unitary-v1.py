#!/usr/bin/env python3
"""Exact Q(sqrt5) physical cyclic action on the 600-cell 4D witness."""
import datetime,hashlib,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-600cell-circulant4d-core-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='665517cf4f42ad2ddc1b9f83893449e4cb26d0c5802c0a46476cafd9e2c8073c';D=json.loads(raw)
Z=(F(0),F(0));O=(F(1),F(0))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def mul(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sm(q):
 out=Z
 for x in q:out=add(out,x)
 return out
def mm(A,B):return [[sm(mul(A[i][k],B[k][j])for k in range(4))for j in range(4)]for i in range(4)]
def apply(A,v):return tuple(sm(mul(A[i][j],v[j])for j in range(4))for i in range(4))
rawT=[[(0,0),(-16,0),(0,0),(0,0)],[(4,4),(0,0),(-8,0),(-4,4)],[(4,-4),(0,0),(-4,-4),(-8,0)],[(8,0),(0,0),(-4,4),(-4,-4)]]
T=[[tuple(F(x,16)for x in q)for q in row]for row in rawT];I=[[O if i==j else Z for j in range(4)]for i in range(4)]
assert mm([[T[j][i]for j in range(4)]for i in range(4)],T)==I
power=I
for k in range(1,16):
 power=mm(power,T)
 if k<15:assert power!=I and power!=[[neg(x)for x in row]for row in I]
assert power==[[neg(x)for x in row]for row in I]
V=[tuple(tuple(F(x)for x in c)for c in v)for v in D['rays']];C=[set(q)for q in D['contexts']];ids=sorted(set.union(*C));assert len(ids)==30
mapping={}
for ray in ids:
 occ=[i for i,q in enumerate(C)if ray in q];assert len(occ)==2
 target=C[(occ[0]+1)%15]&C[(occ[1]+1)%15];assert len(target)==1;dest=next(iter(target));q=apply(T,V[ray]);v=V[dest]
 assert q==v or q==tuple(neg(x)for x in v);mapping[ray]=dest
assert len(set(mapping.values()))==30 and all({mapping[r]for r in C[i]}==C[(i+1)%15]for i in range(15))
# The projectively equivalent -T has characteristic x^4-phi*x^3+phi*x²-phi*x+1.
Pmat=[[neg(x)for x in row]for row in T];powers=[];q=I
for k in range(1,5):q=mm(q,Pmat);powers.append(sm(q[j][j]for j in range(4)))
es=[O]
for k in range(1,5):
 v=Z
 for j in range(1,k+1):
  x=mul(es[k-j],powers[j-1]);v=add(v,x if j%2 else neg(x))
 es.append((v[0]/k,v[1]/k))
phi=(F(1,2),F(1,2));assert es==[O,phi,phi,phi,O]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'witness_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'matrix_numerators_a_plus_b_sqrt5':rawT,'denominator':16,
 'orthogonal':True,'T_power_15':'-I','projective_order':15,'ray_actions_checked':len(mapping),
 'contexts_advanced':len(C),'charpoly_of_minus_T':'x^4-phi*x^3+phi*x^2-phi*x+1','status':'PASS'}
(P/'frontier-20261029-600cell-core-cyclic-unitary-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
