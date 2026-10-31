#!/usr/bin/env python3
"""Bounded local-regular/nonseminormal search, six distinct witness/output labels."""
from itertools import product
import sys,z3
n=int(sys.argv[1]);ms=int(sys.argv[2]);E,X=z3.EnumSort('sd%d'%n,['s%d_%d'%(n,i) for i in range(n)])
m=z3.Function('sop%d'%n,E,E,E);sol=z3.Solver();sol.set(timeout=ms)
for x in X:sol.add(m(x,x)==x)
for x,y,z in product(X,repeat=3):sol.add(m(m(x,y),z)==m(x,m(y,z)))
for e,x,y,z in product(X,repeat=4):
 guard=z3.And(m(e,x)==x,m(x,e)==x,m(e,y)==y,m(y,e)==y,m(e,z)==z,m(z,e)==z)
 sol.add(z3.Implies(guard,m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x)))
a,b,c,d,l,r=X[:6]
sol.add(m(m(m(m(a,b),c),d),a)==l)
sol.add(m(m(m(m(m(m(a,b),c),a),c),d),a)==r)
sol.add(m(m(c,a),c)!=c,m(a,l)==l,m(l,a)==l,m(a,r)==r,m(r,a)==r)
res=sol.check();print('n=',n,' six_distinct_values=true verdict=',res,sep='',flush=True)
if res==z3.sat:
 model=sol.model();ix={str(x):i for i,x in enumerate(X)};B=tuple(tuple(ix[str(model.eval(m(a,b)))] for b in X) for a in X)
 def op(a,b):return B[a][b]
 assert all(op(x,x)==x for x in range(n))
 assert all(op(op(x,y),z)==op(x,op(y,z)) for x,y,z in product(range(n),repeat=3))
 for e in range(n):
  C=[x for x in range(n) if op(e,x)==x==op(x,e)]
  assert all(op(op(op(op(x,y),x),z),x)==op(op(op(x,y),z),x) for x,y,z in product(C,repeat=3))
 assert op(op(op(op(0,1),2),3),0)==4
 assert op(op(op(op(op(op(0,1),2),0),2),3),0)==5
 print('SAT_EXACT_RECHECK table=',B,' witness=(0,1,2,3) values=(4,5)',sep='',flush=True)
