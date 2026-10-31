#!/usr/bin/env python3
"""Search for an LSRB whose local corner is not a regular band."""
from itertools import product
import sys,z3

def go(n,ms):
 m=z3.Function('s_%d'%n,z3.IntSort(),z3.IntSort(),z3.IntSort());sol=z3.Solver();sol.set(timeout=ms)
 for x,y in product(range(n),repeat=2):sol.add(0<=m(x,y),m(x,y)<n)
 for x in range(n):sol.add(m(x,x)==x)
 for a,b,c in product(range(n),repeat=3):
  sol.add(m(m(a,b),c)==m(a,m(b,c)))
  sol.add(m(m(a,b),c)==m(m(m(m(m(m(a,b),c),a),c),b),c))
 e,x,y,z=[z3.Int('v_%s_%d'%(s,n)) for s in ('e','x','y','z')]
 for a in (e,x,y,z):sol.add(0<=a,a<n)
 sol.add(*(z3.And(m(e,a)==a,m(a,e)==a) for a in (x,y,z)))
 sol.add(m(m(m(m(x,y),x),z),x)!=m(m(m(x,y),z),x))
 res=sol.check();print('size=',n,' verdict=',res,sep='',flush=True)
 if res!=z3.sat:return False
 md=sol.model();B=tuple(tuple(md.eval(m(a,b)).as_long() for b in range(n)) for a in range(n));v=tuple(md.eval(a).as_long() for a in (e,x,y,z))
 assert all(B[a][a]==a for a in range(n))
 assert all(B[B[a][b]][c]==B[a][B[b][c]] for a,b,c in product(range(n),repeat=3))
 assert all(B[B[a][b]][c]==B[B[B[B[B[B[a][b]][c]][a]][c]][b]][c] for a,b,c in product(range(n),repeat=3))
 e0,a,b,c=v;assert all(B[e0][t]==t==B[t][e0] for t in (a,b,c))
 assert B[B[B[B[a][b]][a]][c]][a]!=B[B[B[a][b]][c]][a]
 print('SAT_EXACT_RECHECK B=',B,' local_regular_failure=',v,sep='',flush=True);return True

if __name__=='__main__':
 lo,hi,ms=map(int,sys.argv[1:4])
 for n in range(lo,hi+1):
  if go(n,ms):break
