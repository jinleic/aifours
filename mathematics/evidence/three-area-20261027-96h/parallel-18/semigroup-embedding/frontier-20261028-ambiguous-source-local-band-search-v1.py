#!/usr/bin/env python3
"""Bounded Z3 search for a genuinely locally-regular, nonregular host band."""
from itertools import product
import sys
import z3
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
S=tuple(product(range(3),range(5),range(3)));ix={s:i for i,s in enumerate(S)}
def sm(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def q(a):return (a[0],th[a[1]],a[2])
def weight(a,b):return (th[a[1]]+th[P[a[2]][b[0]]])%2
G=((2,4,2),(1,4,1),(0,4,0))
c=set(G)
while True:
 d=c|{sm(a,b) for a,b in product(c,repeat=2)}
 if d==c:break
 c=d
assert c==set(S)

def search(n,pairs,ms):
 invol=list(range(n))
 for j in range(pairs):invol[2*j],invol[2*j+1]=2*j+1,2*j
 def act(z):
  out=z3.IntVal(invol[-1])
  for k in range(n-2,-1,-1):out=z3.If(z==k,invol[k],out)
  return out
 m=z3.Function('local_%d_%d'%(n,pairs),z3.IntSort(),z3.IntSort(),z3.IntSort())
 bs=[z3.Int('local_b_%d_%d_%d'%(n,pairs,i)) for i in range(45)]
 sol=z3.Solver();sol.set(timeout=ms)
 for b in bs:sol.add(0<=b,b<n)
 for x,y in product(range(n),repeat=2):
  sol.add(0<=m(x,y),m(x,y)<n,act(m(x,y))==m(invol[x],invol[y]))
 for x in range(n):sol.add(m(x,x)==x)
 for x,y,z in product(range(n),repeat=3):sol.add(m(m(x,y),z)==m(x,m(y,z)))
 for e,x,y,z in product(range(n),repeat=4):
  cond=z3.And(m(e,x)==x,m(x,e)==x,m(e,y)==y,m(y,e)==y,m(e,z)==z,m(z,e)==z)
  sol.add(z3.Implies(cond,m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x)))
 for a in S:
  for b in G:
   w=weight(a,b);bb=bs[ix[b]]
   sol.add(m(bs[ix[a]],act(bb) if w else bb)==bs[ix[sm(a,b)]])
 groups={}
 for s in S:groups.setdefault(q(s),[]).append(bs[ix[s]])
 for values in groups.values():sol.add(z3.Distinct(*values))
 result=sol.check();print('n=%d pairs=%d verdict=%s'%(n,pairs,result),flush=True)
 if result!=z3.sat:return False
 model=sol.model()
 tb=tuple(tuple(model.eval(m(x,y)).as_long() for y in range(n)) for x in range(n))
 beta=tuple(model.eval(b).as_long() for b in bs)
 for x,y,z in product(range(n),repeat=3):assert tb[tb[x][y]][z]==tb[x][tb[y][z]]
 for x,y in product(range(n),repeat=2):assert invol[tb[x][y]]==tb[invol[x]][invol[y]]
 for x in range(n):assert tb[x][x]==x
 for e in range(n):
  local=[x for x in range(n) if tb[e][x]==x==tb[x][e]]
  for x,y,z in product(local,repeat=3):
   assert tb[tb[tb[tb[x][y]][x]][z]][x]==tb[tb[tb[x][y]][z]][x]
 for a,b in product(S,repeat=2):
  c=beta[ix[b]];c=invol[c] if weight(a,b) else c
  assert beta[ix[sm(a,b)]]==tb[beta[ix[a]]][c]
  assert a==b or q(a)!=q(b) or beta[ix[a]]!=beta[ix[b]]
 globfail=next(((x,y,z) for x,y,z in product(range(n),repeat=3)
                if tb[tb[tb[tb[x][y]][x]][z]][x]!=tb[tb[tb[x][y]][z]][x]),None)
 assert globfail is not None
 print('SAT_EXACT_RECHECK table=',tb,' involution=',invol,' coefficients=',beta,' global_regular_counterexample=',globfail,sep='',flush=True)
 return True

if __name__=='__main__':
 lo,hi,ms=map(int,sys.argv[1:4])
 print('ambiguous source45, exact local corner regularity, verified generators',flush=True)
 for n in range(lo,hi+1):
  for pairs in range(n//2+1):
   if search(n,pairs,ms):sys.exit(0)
 print('NO_WITNESS_IN_CONCLUDED_CASES; UNKNOWN is not a negative result',flush=True)
