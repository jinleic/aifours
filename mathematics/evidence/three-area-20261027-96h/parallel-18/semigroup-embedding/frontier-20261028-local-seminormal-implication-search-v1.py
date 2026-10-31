#!/usr/bin/env python3
"""Finite search for either-direction distinction of local regularity and seminormality."""
from itertools import product
import sys,z3

def search(n,mode,ms):
 m=z3.Function('m_%s_%d'%(mode,n),z3.IntSort(),z3.IntSort(),z3.IntSort())
 sol=z3.Solver();sol.set(timeout=ms)
 for x,y in product(range(n),repeat=2):sol.add(0<=m(x,y),m(x,y)<n)
 for x in range(n):sol.add(m(x,x)==x)
 for x,y,z in product(range(n),repeat=3):sol.add(m(m(x,y),z)==m(x,m(y,z)))
 def regular(x,y,z):return m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x)
 def local(e,x,y,z):return z3.And(m(e,x)==x,m(x,e)==x,m(e,y)==y,m(y,e)==y,m(e,z)==z,m(z,e)==z)
 def semi(a,b,c,d):return m(m(m(m(a,b),c),d),a)==m(m(m(m(m(m(a,b),c),a),c),d),a)
 if mode=='loc':
  for e,x,y,z in product(range(n),repeat=4):sol.add(z3.Implies(local(e,x,y,z),regular(x,y,z)))
  v=[z3.Int('v%d_%d'%(j,n)) for j in range(4)]
  for x in v:sol.add(0<=x,x<n)
  sol.add(z3.Not(semi(*v)))
 elif mode=='semi':
  for a,b,c,d in product(range(n),repeat=4):sol.add(semi(a,b,c,d))
  v=[z3.Int('v%d_%d'%(j,n)) for j in range(4)]
  for x in v:sol.add(0<=x,x<n)
  sol.add(local(*v),z3.Not(regular(*v[1:])))
 else:raise ValueError('mode')
 result=sol.check();print('mode=',mode,' size=',n,' verdict=',result,sep='',flush=True)
 if result!=z3.sat:return False
 model=sol.model();B=tuple(tuple(model.eval(m(a,b)).as_long() for b in range(n)) for a in range(n))
 vals=tuple(model.eval(x).as_long() for x in v)
 assert all(B[x][x]==x for x in range(n))
 assert all(B[B[x][y]][z]==B[x][B[y][z]] for x,y,z in product(range(n),repeat=3))
 def r(x,y,z):return B[B[B[B[x][y]][x]][z]][x]==B[B[B[x][y]][z]][x]
 def sn(a,b,c,d):return B[B[B[B[a][b]][c]][d]][a]==B[B[B[B[B[B[a][b]][c]][a]][c]][d]][a]
 if mode=='loc':
  for e0 in range(n):
   corner=[x for x in range(n) if B[e0][x]==x==B[x][e0]]
   assert all(r(x,y,z) for x,y,z in product(corner,repeat=3))
  assert not sn(*vals)
 else:
  assert all(sn(*p) for p in product(range(n),repeat=4))
  e0,x,y,z=vals;assert all(B[e0][a]==a==B[a][e0] for a in (x,y,z)) and not r(x,y,z)
 print('SAT_EXACT_RECHECK table=',B,' witness=',vals,sep='',flush=True);return True

if __name__=='__main__':
 mode=sys.argv[1];lo,hi,ms=map(int,sys.argv[2:5])
 for n in range(lo,hi+1):
  if search(n,mode,ms):break
