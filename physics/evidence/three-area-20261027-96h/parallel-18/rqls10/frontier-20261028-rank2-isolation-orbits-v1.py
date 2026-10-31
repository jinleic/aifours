#!/usr/bin/env python3
"""Exact extra orbit representatives plus finite triple-preserving orbit census."""
from itertools import combinations,product
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('base',P/'frontier-20261028-rank2-projector-isolation-v1.py')
m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
Z,ONE=m.Z,m.ONE

def make_N(q,pair):
 order=list(pair)+[j for j in range(5) if j not in pair]
 out=[]
 for basis in range(3):
  mat=[]
  for j in range(5):
   row=[]
   for a in order:
    if basis==0:val=m.omega(q*j*j+3*j*a)
    else:
     qb=q if basis==1 else (q-4)%5
     val=m.scale(m.mul(m.root5,m.summ(m.omega(qb*t*t+3*(a-j)*t) for t in range(5))),m.Q(1,5))
    assert m.mul(val,m.conj(val))==ONE
    row.append(val)
   mat.append(row)
  out.append(mat)
 return out

def certificate(q,pair):
 m.N=make_N(q,pair);J=[]
 for basis in range(3):
  for j in range(4):
   row=[]
   for x in range(3):
    for k in range(2):
     t=m.mul(m.N[basis][j][2+x],m.conj(m.N[basis][j][k]))
     row.extend((m.add(t,m.conj(t)),m.add(m.mul(m.ii,t),m.conj(m.mul(m.ii,t)))))
   assert all(m.isreal(v) for v in row);J.append(row)
 rank,K=m.nullspace(J);rankT,L=m.nullspace([list(r) for r in zip(*J)])
 assert rank==rankT==10 and len(K)==len(L)==2
 assert all(m.isreal(v) for row in K+L for v in row)
 q1=m.quadratic(K[0]);q2=m.quadratic(K[1]);both=m.quadratic([m.add(x,y) for x,y in zip(K[0],K[1])])
 cross=[m.sub(m.sub(x,y),z) for x,y,z in zip(both,q1,q2)]
 coef=[[m.dot(l,q1),m.dot(l,cross),m.dot(l,q2)] for l in L]
 assert all(m.isreal(v) for row in coef for v in row)
 (a,b,c),(d,e,f)=coef
 result=m.det([[c,b,a,Z],[Z,c,b,a],[f,e,d,Z],[Z,f,e,d]])
 assert result!=Z and not (c==Z and f==Z)
 print('PASS q',q,'pair',pair,'rank10, nonzero quadratic resultant',flush=True)

for q in (1,2):certificate(q,(0,1))
allp={(q,tuple(cs)) for q in (1,2,3) for cs in combinations(range(5),2)}
def orbit(q,pair):
 out=set()
 for c,d,nu in product(range(1,5),range(5),range(5)):
  eta=0 if c*c%5==1 else 4
  qp=(eta+q*c*c)%5
  jj=[((2*q*c*d+3*c*j+nu)*2)%5 for j in pair]
  out.add((qp,tuple(sorted(jj))))
 return out
orbits=[orbit(1,(0,1)),orbit(2,(0,1)),orbit(3,(0,1))]
assert all(len(o)==10 for o in orbits) and len(set.union(*orbits))==30
assert set.union(*orbits)==allp
print('PASS 30 standard WH pair projectors split into three 10-element symmetry orbits')
print('Each orbit representative has an exact local-isolation certificate; no global classification claimed')
