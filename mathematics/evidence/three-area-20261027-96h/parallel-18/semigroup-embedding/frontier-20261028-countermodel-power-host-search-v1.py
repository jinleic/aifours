#!/usr/bin/env python3
"""Search source hosts in B5^k with involutive coordinate swap/automorphisms."""
from itertools import product
import sys,z3
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));sigma=(0,3,4,1,2)
S=tuple(product(range(3),range(5),range(3)));ix={s:i for i,s in enumerate(S)}
G=((2,4,2),(1,4,1),(0,4,0))
def sm(a,b):return(a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def q(s):return(s[0],th[s[1]],s[2])
def w(a,b):return (th[a[1]]+th[P[a[2]][b[0]]])%2
c=set(G)
while True:
 d=c|{sm(a,b) for a,b in product(c,repeat=2)}
 if d==c:break
 c=d
assert c==set(S)

def solve(k,kind,ms):
 assert k%2==0
 m=z3.Function('fixed_%d_%d'%(k,kind),z3.IntSort(),z3.IntSort(),z3.IntSort())
 sol=z3.Solver();sol.set(timeout=ms)
 for x,y in product(range(5),repeat=2):sol.add(m(x,y)==B[x][y])
 vals=[[z3.Int('v_%d_%d_%d_%d'%(k,kind,j,t)) for t in range(k)] for j in range(45)]
 for row in vals:
  for x in row:sol.add(0<=x,x<5)
 def sig(x):
  out=z3.IntVal(sigma[-1])
  for i in range(3,-1,-1):out=z3.If(x==i,sigma[i],out)
  return out
 for a in S:
  for b in G:
   for t in range(k):
    rhs=vals[ix[b]][t]
    if w(a,b):
     rhs=vals[ix[b]][t^1]
     if kind:rhs=sig(rhs)
    sol.add(m(vals[ix[a]][t],rhs)==vals[ix[sm(a,b)]][t])
 for i,a in enumerate(S):
  for j,b in enumerate(S[:i]):
   if q(a)==q(b):sol.add(z3.Or(*(vals[i][t]!=vals[j][t] for t in range(k))))
 result=sol.check();print('factors=%d twist=%d result=%s'%(k,kind,result),flush=True)
 if result!=z3.sat:return False
 mod=sol.model();coef=tuple(tuple(mod.eval(x).as_long() for x in row) for row in vals)
 def action(v):
  return tuple(sigma[v[t^1]] if kind else v[t^1] for t in range(k))
 for a,b in product(S,repeat=2):
  va=coef[ix[a]];vb=coef[ix[b]]
  if w(a,b):vb=action(vb)
  assert tuple(B[va[t]][vb[t]] for t in range(k))==coef[ix[sm(a,b)]]
  assert a==b or q(a)!=q(b) or va!=coef[ix[b]]
 print('SAT_EXACT_RECHECK coefficients=',coef,sep='',flush=True)
 return True

if __name__=='__main__':
 k,kind,ms=map(int,sys.argv[1:4]);solve(k,kind,ms)
