#!/usr/bin/env python3
"""Literal exact verifier: the ambiguous original source embeds in B5^2 over q_tau."""
from itertools import product
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
C=(((2,4),(2,0),(2,4)),((4,4),(0,4),(4,4)),
   ((4,4),(4,0),(4,4)),((4,2),(0,2),(4,2)))
S=tuple(product(range(3),range(5),range(3))); BB=tuple(product(range(5),repeat=2))
def sm(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def actor(a):return (a[0],th[a[1]],a[2])
def qm(a,b):return (a[0],(a[1]+th[P[a[2]][b[0]]]+b[1])%2,b[2])
def bm(a,b):return (B[a[0]][b[0]],B[a[1]][b[1]])
def act(a):return (a[1],a[0])
def beta(a):
 if a[1]<4:return C[a[1]][a[2]]
 return (3 if a[0]==1 else 1, 0 if a[2]==1 else 4)
def idem(a):return sm(a,a)==a
assert all(bm(x,x)==x for x in BB)
assert all(bm(bm(x,y),z)==bm(x,bm(y,z)) for x,y,z in product(BB,repeat=3))
assert all(act(act(x))==x for x in BB)
assert all(act(bm(x,y))==bm(act(x),act(y)) for x,y in product(BB,repeat=2))
for e in BB:
 local=tuple(x for x in BB if bm(e,x)==x==bm(x,e))
 assert all(bm(bm(bm(bm(x,y),x),z),x)==bm(bm(bm(x,y),z),x) for x,y,z in product(local,repeat=3))
x,y,z=(1,1),(0,1),(3,1)
assert bm(bm(bm(bm(x,y),x),z),x)!=bm(bm(bm(x,y),z),x)
for s,t in product(S,repeat=2):
 w=(th[s[1]]+th[P[s[2]][t[0]]])%2
 assert actor(sm(s,t))==qm(actor(s),actor(t))
 assert beta(sm(s,t))==bm(beta(s),act(beta(t)) if w else beta(t))
 assert s==t or actor(s)!=actor(t) or beta(s)!=beta(t)
E=tuple(s for s in S if idem(s));Es=set(E)
assert all(idem(s)==(qm(actor(s),actor(s))==actor(s)) for s in S)
contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in Es for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(actor(s)==actor(t)) for s,t in product(S,repeat=2))
e=(1,1,1);f=(1,3,1)
assert e!=f and idem(e) and idem(f) and actor(e)==actor(f)
assert sm(e,f)==f and sm(f,e)==e and beta(e)!=beta(f)
wrong=sum(beta(sm(s,t))!=bm(beta(s),beta(t)) for s,t in product(S,repeat=2))
assert wrong>0
print('source=45 actual_actor=18 band=25 source_idempotents=',len(E),sep='')
print('PASS B5^2 band, all25 regular local corners, explicit global regular identity failure')
print('PASS coordinate-swap C2 action; all2025 actor/host products and injectivity')
print('PASS actual tau by all 46^2 contexts per source; actor pure')
print('nontrivial same-actor R pair e,f=',e,f,' band values=',beta(e),beta(f),sep='')
print('CONTROL identity action breaks source-product equations=',wrong,sep='')
print('LIMIT source-specific exact model; no general original-class conclusion')
