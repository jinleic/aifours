#!/usr/bin/env python3
"""Direct exact dual-host check for the locally regular B5^2 witness."""
from itertools import product
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
C=(((2,4),(2,0),(2,4)),((4,4),(0,4),(4,4)),
   ((4,4),(4,0),(4,4)),((4,2),(0,2),(4,2)))
S=tuple(product(range(3),range(5),range(3)));BB=tuple(product(range(5),repeat=2))
def sm(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def op(a,b):return sm(b,a)
def actor(a):return (a[2],th[a[1]],a[0])
def qm(a,b):return (a[0],(a[1]+th[P[b[0]][a[2]]]+b[1])%2,b[2])
def bm(a,b):return (B[b[0]][a[0]],B[b[1]][a[1]])
def act(a):return (a[1],a[0])
def original(a):
 if a[1]<4:return C[a[1]][a[2]]
 return (3 if a[0]==1 else 1,0 if a[2]==1 else 4)
def beta(a):
 b=original(a)
 return act(b) if th[a[1]] else b
assert all(bm(a,a)==a for a in BB)
assert all(bm(bm(x,y),z)==bm(x,bm(y,z)) for x,y,z in product(BB,repeat=3))
assert all(act(act(x))==x for x in BB)
assert all(act(bm(x,y))==bm(act(x),act(y)) for x,y in product(BB,repeat=2))
for e in BB:
 local=tuple(x for x in BB if bm(e,x)==x==bm(x,e))
 assert all(bm(bm(bm(bm(x,y),x),z),x)==bm(bm(bm(x,y),z),x) for x,y,z in product(local,repeat=3))
for s,t in product(S,repeat=2):
 w=(th[s[1]]+th[P[t[2]][s[0]]])%2
 assert actor(op(s,t))==qm(actor(s),actor(t))
 assert beta(op(s,t))==bm(beta(s),act(beta(t)) if w else beta(t))
 assert s==t or actor(s)!=actor(t) or beta(s)!=beta(t)
e=(1,1,1);f=(1,3,1)
assert op(e,f)==e and op(f,e)==f and actor(e)==actor(f) and beta(e)!=beta(f)
print('PASS all25 dual-band corners regular; C2 automorphism')
print('PASS all2025 opposite-source/actor/host products and injection')
print('same-actor L pair e,f=',e,f,' dual coefficients=',beta(e),beta(f),sep='')
print('LIMIT source-specific dual model; actual tau follows by reversing contexts')
