#!/usr/bin/env python3
"""Finite C2-graded locally-r orthodox search for Billhardt condition (E) failure."""
from itertools import product
import sys,z3
ne,nf,ms=map(int,sys.argv[1:4]);n=ne+nf
D,X=z3.EnumSort('gd%d_%d'%(ne,nf),['g%d_%d_%d'%(ne,nf,i) for i in range(n)])
m=z3.Function('gm%d_%d'%(ne,nf),D,D,D);sol=z3.Solver();sol.set(timeout=ms)
E=X[:ne];O=X[ne:]
def w(*a):
 r=a[0]
 for b in a[1:]:r=m(r,b)
 return r
def member(t,choices):return z3.Or(*(t==v for v in choices))
for i,a in enumerate(X):
 for j,b in enumerate(X):sol.add(member(m(a,b),E if (i<ne)==(j<ne) else O))
for e in E:sol.add(m(e,e)==e)
for a,b,c in product(X,repeat=3):sol.add(m(m(a,b),c)==m(a,m(b,c)))
for a in O:sol.add(z3.Or(*(z3.And(w(a,b,a)==a,w(b,a,b)==b) for b in O)))
for a,b,c,d in product(E,repeat=4):
 loc=z3.And(m(a,b)==b,m(b,a)==b,m(a,c)==c,m(c,a)==c,m(a,d)==d,m(d,a)==d)
 sol.add(z3.Implies(loc,w(b,c,b,d,b)==w(b,c,d,b)))
e=E[0];x=O[0];f,g=z3.Consts('f%d_%d g%d_%d'%(ne,nf,ne,nf),D)
h,xp,hp=z3.Consts('h%d_%d xp%d_%d hp%d_%d'%(ne,nf,ne,nf,ne,nf),D)
sol.add(member(f,E),member(g,E),member(h,O),member(xp,O),member(hp,O))
sol.add(w(x,xp,x)==x,w(xp,x,xp)==xp,w(h,hp,h)==h,w(hp,h,hp)==hp)
sol.add(w(e,x,xp)==e,w(xp,x,f,g)==w(f,g),w(e,h,hp)==e)
sol.add(w(hp,h,f,xp,e,x,f,g)==w(f,xp,e,x,f,g))
sol.add(w(e,x,f,g)!=w(e,h,f,xp,e,x,f,g))
res=sol.check();print('E=',ne,' odd=',nf,' verdict=',res,sep='',flush=True)
if res==z3.sat:
 md=sol.model();ix={str(a):i for i,a in enumerate(X)}
 B=tuple(tuple(ix[str(md.eval(m(a,b)))] for b in X) for a in X);v=(0,ix[str(md.eval(f))],ix[str(md.eval(g))],ne,ix[str(md.eval(h))],ix[str(md.eval(xp))],ix[str(md.eval(hp))])
 def op(a,b):return B[a][b]
 def wd(*a):
  r=a[0]
  for b in a[1:]:r=op(r,b)
  return r
 def idem(a):return op(a,a)==a
 assert all(op(op(a,b),c)==op(a,op(b,c)) for a,b,c in product(range(n),repeat=3))
 assert all(idem(a)==(a<ne) for a in range(n))
 assert all((op(a,b)<ne)==((a<ne)==(b<ne)) for a,b in product(range(n),repeat=2))
 assert all(any(wd(a,b,a)==a and wd(b,a,b)==b for b in range(n)) for a in range(n))
 for e0 in range(ne):
  local=[a for a in range(ne) if op(e0,a)==a==op(a,e0)]
  assert all(wd(a,b,a,c,a)==wd(a,b,c,a) for a,b,c in product(local,repeat=3))
 e0,f0,g0,x0,h0,x0p,h0p=v
 assert wd(x0,x0p,x0)==x0 and wd(x0p,x0,x0p)==x0p
 assert wd(h0,h0p,h0)==h0 and wd(h0p,h0,h0p)==h0p
 assert wd(e0,x0,x0p)==e0 and wd(x0p,x0,f0,g0)==wd(f0,g0) and wd(e0,h0,h0p)==e0
 assert wd(h0p,h0,f0,x0p,e0,x0,f0,g0)==wd(f0,x0p,e0,x0,f0,g0)
 assert wd(e0,x0,f0,g0)!=wd(e0,h0,f0,x0p,e0,x0,f0,g0)
 print('SAT_EXACT_RECHECK table=',B,' witness=(e,f,g,x,h,xprime,hprime)=',v,sep='',flush=True)
