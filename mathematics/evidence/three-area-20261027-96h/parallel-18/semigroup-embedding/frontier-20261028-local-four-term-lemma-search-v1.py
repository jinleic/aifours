#!/usr/bin/env python3
"""Find a locally regular band refuting extension of the global four-term lemma."""
from itertools import product
import sys,z3

def go(n,ms):
 m=z3.Function('b_%d'%n,z3.IntSort(),z3.IntSort(),z3.IntSort())
 X,U,V,Y=[z3.Int('%s_%d'%(s,n)) for s in ('x','u','v','y')]
 solver=z3.Solver();solver.set(timeout=ms)
 for a in (X,U,V,Y):solver.add(0<=a,a<n)
 for a,b in product(range(n),repeat=2):solver.add(0<=m(a,b),m(a,b)<n)
 for a in range(n):solver.add(m(a,a)==a)
 for a,b,c in product(range(n),repeat=3):solver.add(m(m(a,b),c)==m(a,m(b,c)))
 for e,x,y,z in product(range(n),repeat=4):
  local=z3.And(m(e,x)==x,m(x,e)==x,m(e,y)==y,m(y,e)==y,m(e,z)==z,m(z,e)==z)
  solver.add(z3.Implies(local,m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x)))
 E=m(m(X,U),Y);F=m(m(X,V),Y)
 solver.add(m(U,V)==U,m(V,U)==V,m(E,F)==F,m(F,E)==E,E!=F)
 result=solver.check();print('order',n,'verdict',result,flush=True)
 if result!=z3.sat:return False
 model=solver.model()
 B=tuple(tuple(model.eval(m(a,b)).as_long() for b in range(n)) for a in range(n))
 x,u,v,y=(model.eval(a).as_long() for a in (X,U,V,Y))
 for a,b,c in product(range(n),repeat=3):assert B[B[a][b]][c]==B[a][B[b][c]]
 for a in range(n):assert B[a][a]==a
 for e in range(n):
  local=[a for a in range(n) if B[e][a]==a==B[a][e]]
  for a,b,c in product(local,repeat=3):assert B[B[B[B[a][b]][a]][c]][a]==B[B[B[a][b]][c]][a]
 e=B[B[x][u]][y];f=B[B[x][v]][y]
 assert B[u][v]==u and B[v][u]==v and B[e][f]==f and B[f][e]==e and e!=f
 glob=next(((a,b,c) for a,b,c in product(range(n),repeat=3)
            if B[B[B[B[a][b]][a]][c]][a]!=B[B[B[a][b]][c]][a]),None)
 assert glob is not None
 print('SAT_EXACT_RECHECK band=',B,' x,u,v,y=',(x,u,v,y),' E,F=',(e,f),' global_failure=',glob,sep='',flush=True)
 return True

if __name__=='__main__':
 lo,hi,ms=map(int,sys.argv[1:4])
 for n in range(lo,hi+1):
  if go(n,ms):sys.exit(0)
 print('NO_WITNESS_IN_CONCLUDED_CASES; UNKNOWN is not a negative result',flush=True)
