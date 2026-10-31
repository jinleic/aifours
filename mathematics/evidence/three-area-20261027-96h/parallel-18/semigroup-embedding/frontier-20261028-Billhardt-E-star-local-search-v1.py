#!/usr/bin/env python3
"""Finite search for a locally-r orthodox base satisfying Billhardt 1998 E*."""
from itertools import product
import sys,z3
n=int(sys.argv[1]);ms=int(sys.argv[2]);E,X=z3.EnumSort('ed%d'%n,['e%d_%d'%(n,i) for i in range(n)])
m=z3.Function('em%d'%n,E,E,E);sol=z3.Solver();sol.set(timeout=ms)
def w(*args):
 x=args[0]
 for y in args[1:]:x=m(x,y)
 return x
def idem(x):return m(x,x)==x
for a,b,c in product(X,repeat=3):sol.add(m(m(a,b),c)==m(a,m(b,c)))
for a in X:sol.add(z3.Or(*(z3.And(w(a,b,a)==a,w(b,a,b)==b) for b in X)))
for a,b in product(X,repeat=2):sol.add(z3.Implies(z3.And(idem(a),idem(b)),idem(m(a,b))))
for e,a,b,c in product(X,repeat=4):
 guard=z3.And(idem(e),idem(a),idem(b),idem(c),m(e,a)==a,m(a,e)==a,m(e,b)==b,m(b,e)==b,m(e,c)==c,m(c,e)==c)
 sol.add(z3.Implies(guard,w(a,b,a,c,a)==w(a,b,c,a)))
x=X[0];ei,fi,gi,hi,xp=z3.Consts('ee%d ff%d gg%d hh%d xp%d'%(n,n,n,n,n),E)
sol.add(idem(ei),idem(fi),idem(gi),idem(hi))
sol.add(w(x,xp,x)==x,w(xp,x,xp)==xp)
sol.add(w(ei,x,xp)==ei,w(xp,x,fi,gi)==w(fi,gi),w(ei,hi)==ei)
sol.add(w(hi,fi,xp,ei,x,fi,gi)==w(fi,xp,ei,x,fi,gi))
sol.add(w(ei,x,fi,gi)!=w(ei,fi,ei,x,fi,gi),idem(w(x,hi)),idem(w(hi,x)))
res=sol.check();print('n=',n,' verdict=',res,sep='',flush=True)
if res==z3.sat:
 model=sol.model();ix={str(y):i for i,y in enumerate(X)}
 B=tuple(tuple(ix[str(model.eval(m(a,b)))] for b in X) for a in X)
 vals=(ix[str(model.eval(ei))],ix[str(model.eval(fi))],ix[str(model.eval(gi))],ix[str(model.eval(hi))],0,ix[str(model.eval(xp))])
 def op(a,b):return B[a][b]
 def wd(*v):
  t=v[0]
  for y in v[1:]:t=op(t,y)
  return t
 def idm(a):return op(a,a)==a
 assert all(op(op(a,b),c)==op(a,op(b,c)) for a,b,c in product(range(n),repeat=3))
 assert all(any(wd(a,b,a)==a and wd(b,a,b)==b for b in range(n)) for a in range(n))
 Es={a for a in range(n) if idm(a)};assert all(op(a,b) in Es for a,b in product(Es,repeat=2))
 for e0 in Es:
  loc=[a for a in Es if op(e0,a)==a==op(a,e0)]
  assert all(wd(a,b,a,c,a)==wd(a,b,c,a) for a,b,c in product(loc,repeat=3))
 a,b,c,d,x0,xx=vals
 assert all(t in Es for t in (a,b,c,d)) and wd(x0,xx,x0)==x0 and wd(xx,x0,xx)==xx
 assert wd(a,x0,xx)==a and wd(xx,x0,b,c)==wd(b,c) and wd(a,d)==a
 assert wd(d,b,xx,a,x0,b,c)==wd(b,xx,a,x0,b,c)
 assert wd(a,x0,b,c)!=wd(a,b,a,x0,b,c) and idm(wd(x0,d)) and idm(wd(d,x0))
 print('SAT_EXACT_RECHECK table=',B,' E*= (e,f,g,h,x,xprime)=',vals,sep='',flush=True)
