#!/usr/bin/env python3
"""Finite-domain attack for local-regular but non-seminormal bands; fixed distinct witness."""
from itertools import product
import sys,z3
n=int(sys.argv[1]);ms=int(sys.argv[2])
E,X=z3.EnumSort('dom%d'%n,['v%d_%d'%(n,i) for i in range(n)])
m=z3.Function('m%d'%n,E,E,E);sol=z3.Solver();sol.set(timeout=ms)
for x in X:sol.add(m(x,x)==x)
for x,y,z in product(X,repeat=3):sol.add(m(m(x,y),z)==m(x,m(y,z)))
for e,x,y,z in product(X,repeat=4):
 local=z3.And(m(e,x)==x,m(x,e)==x,m(e,y)==y,m(y,e)==y,m(e,z)==z,m(z,e)==z)
 sol.add(z3.Implies(local,m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x)))
a,b,c,d=X[:4]
sol.add(m(m(m(m(a,b),c),d),a)!=m(m(m(m(m(m(a,b),c),a),c),d),a))
res=sol.check();print('n=',n,' distinct_witness=true verdict=',res,sep='',flush=True)
if res==z3.sat:
 model=sol.model();idx={str(x):i for i,x in enumerate(X)}
 B=tuple(tuple(idx[str(model.eval(m(a,b)))] for b in X) for a in X)
 def m0(a,b):return B[a][b]
 assert all(m0(x,x)==x for x in range(n))
 assert all(m0(m0(x,y),z)==m0(x,m0(y,z)) for x,y,z in product(range(n),repeat=3))
 for e in range(n):
  local=[x for x in range(n) if m0(e,x)==x==m0(x,e)]
  assert all(m0(m0(m0(m0(x,y),x),z),x)==m0(m0(m0(x,y),z),x) for x,y,z in product(local,repeat=3))
 assert m0(m0(m0(m0(0,1),2),3),0)!=m0(m0(m0(m0(m0(m0(0,1),2),0),2),3),0)
 print('SAT_EXACT_RECHECK table=',B,' witness=(0,1,2,3)',sep='',flush=True)
