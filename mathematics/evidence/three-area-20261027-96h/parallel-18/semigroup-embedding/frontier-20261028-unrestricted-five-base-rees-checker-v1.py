#!/usr/bin/env python3
"""Exact verification of the arbitrary-P locally regular Rees lift."""
from itertools import product
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));th=(0,1,0,1,0)
def make(F):
 nl=len(F);ni=len(F[0]);U=tuple(('u',i) for i in range(ni));V=tuple(('v',l) for l in range(nl));W=(('w',0),('w',1));N=U+V+W
 def m(x,y):
  if y[0]!='u':return y
  if x[0] in ('u','w'):return x
  return W[F[x[1]][y[1]]]
 def b2(x,y):return(m(x[0],y[0]),m(x[1],y[1]))
 def beta(a,i,l):return ((W[0],V[l]),(V[l],W[1]),(W[1],V[l]),(V[l],W[0]),(U[i],V[l]))[a]
 return N,m,b2,beta
# All 2x2 selector functions and every possible local source-product parameter.
tests=0
for bits in product(range(2),repeat=4):
 F=(bits[:2],bits[2:]);N,m,b2,beta=make(F)
 assert all(m(x,x)==x for x in N)
 assert all(m(m(x,y),z)==m(x,m(y,z)) for x,y,z in product(N,repeat=3))
 for e in N:
  corner={m(m(e,x),e) for x in N}
  assert all(m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x) for x,y,z in product(corner,repeat=3))
 for a,b,i,j,l,mu in product(range(5),range(5),range(2),range(2),range(2),range(2)):
  for p in (4,1 if F[l][j] else 3):
   q=th[p];w=(th[a]+q)%2;target=A[A[a][p]][b]
   right=beta(b,j,mu);right=right[::-1] if w else right
   assert beta(target,i,mu)==b2(beta(a,i,l),right)
   tests+=1
assert tests==12800
# Exhaust all 81 2x2 full matrices with allowed entries, all 400 source products each.
matrices=0
for entries in product((4,1,3),repeat=4):
 P=(entries[:2],entries[2:]);F=tuple(tuple(1 if p==1 else 0 for p in row) for row in P)
 N,m,b2,beta=make(F);S=tuple(product(range(2),range(5),range(2)))
 def sm(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
 def q(a):return(a[0],th[a[1]],a[2])
 for s,t in product(S,repeat=2):
  w=(th[s[1]]+th[P[s[2]][t[0]]])%2;rhs=beta(t[1],t[0],t[2]);rhs=rhs[::-1] if w else rhs
  assert beta(sm(s,t)[1],s[0],t[2])==b2(beta(s[1],s[0],s[2]),rhs)
  assert s==t or q(s)!=q(t) or beta(s[1],s[0],s[2])!=beta(t[1],t[0],t[2])
 matrices+=1
# A 3x3 matrix with an inconsistent binary XOR rectangle; it is neither prior row-coded nor triangular.
P=((4,4,4),(4,1,1),(4,1,3));F=tuple(tuple(1 if p==1 else 0 for p in row) for row in P)
assert not any(all(p==4 or (c[j]<=r[l] and p==(1 if r[l]^c[j]==0 else 3))
               for l,row in enumerate(P) for j,p in enumerate(row))
               for r in product(range(2),repeat=3) for c in product(range(2),repeat=3))
N,m,b2,beta=make(F);S=tuple(product(range(3),range(5),range(3)))
def sm(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def actor(a):return(a[0],th[a[1]],a[2])
collapse=(0,1,1)
def qa(a):return(collapse[a[0]],th[a[1]],collapse[a[2]])
def qp(a,b):return(a[0],(a[1]+th[P[a[2]][b[0]]]+b[1])%2,b[2])
for s,t in product(S,repeat=2):
 w=(th[s[1]]+th[P[s[2]][t[0]]])%2;rhs=beta(t[1],t[0],t[2]);rhs=rhs[::-1] if w else rhs
 assert beta(sm(s,t)[1],s[0],t[2])==b2(beta(s[1],s[0],s[2]),rhs)
 assert qa(sm(s,t))==qp(qa(s),qa(t))
 assert s==t or actor(s)!=actor(t) or beta(s[1],s[0],s[2])!=beta(t[1],t[0],t[2])
 assert s==t or qa(s)!=qa(t) or (s[0],s[2])!=(t[0],t[2]) or beta(s[1],s[0],s[2])!=beta(t[1],t[0],t[2])
E={s for s in S if sm(s,s)==s};contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(qa(s)==qa(t)) for s,t in product(S,repeat=2))
for p in (0,2):
 s=(1,4,1);badP=((4,4,4),(4,p,4),(4,4,4))
 def bad(a,b):return(a[0],A[A[a[1]][badP[a[2]][b[0]]]][b[1]],b[2])
 e=bad(s,s);assert e!=s and bad(e,e)==e and bad(e,s)==e==bad(s,e)
print('abstract local band: all16 selector tables, all12800 parameter laws, all corners regular')
print('all81 2x2 allowed P matrices: 32400 source-product laws and actor-fibre injections')
print('nontriangular/non-row-coded 45-source: natural actor=',len(set(map(actor,S))),' actual=',len(set(map(qa,S))),sep='')
print('PASS 2025 host products, retained-rectangle actual-q injection, 46^2 contexts/source')
print('CONTROL forbidden entries 0,2 each yield explicit s^3=s^2!=s WEU violation')
print('LIMIT finite verification complements the arbitrary-index symbolic proof')
