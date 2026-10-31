#!/usr/bin/env python3
"""Exact nonrectangular adjoined-identity Rees evaluation-band verification."""
from itertools import product
G=range(2);BB=tuple(product(range(2),range(2),range(2)))
def bm(a,b):return(a[0],b[1],a[2]&b[2])
def act(g,b):return(b[0]^g,b[1]^g,b[2])
def oneprod(a,b):
 if a is None:return b
 if b is None:return a
 return bm(a,b)
K=tuple(p for p in BB if all(bm(bm(b,p),b)==b for b in BB));assert len(K)==4
assert all(bm(x,x)==x for x in BB)
assert all(bm(bm(x,y),z)==bm(x,bm(y,z)) for x,y,z in product(BB,repeat=3))
assert all(bm(bm(bm(bm(x,y),x),z),x)==bm(bm(bm(x,y),z),x) for x,y,z in product(BB,repeat=3))
A=(None,)+tuple(product(BB,G))
def theta(a):return 0 if a is None else a[1]
def am(a,b):
 if a is None:return b
 if b is None:return a
 return(bm(a[0],act(a[1],b[0])),a[1]^b[1])
P=((None,None,None),(None,((0,0,1),1),((1,1,1),1)))
I=range(3);L=range(2);S=tuple(product(I,A,L))
def sm(a,b):return(a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
def actor(a):return(a[0],theta(a[1]),a[2])
def rp(a,b):return(a[0],a[1]^theta(P[a[2]][b[0]])^b[1],b[2])
rows=tuple(product(I,G));cols=tuple(product(L,G))
T=tuple((row,b,col) for row in rows for b in BB for col in cols)+tuple((row,None,col) for row in rows for col in cols if row[1]==col[1])
Ts=set(T);z=K[0]
def H(col,row):
 l,t=col;j,u=row;p=P[l][j]
 if t==u:return None
 return act(t,p[0]) if p is not None and p[1]==(t^u) else z
def tm(a,b):return(a[0],oneprod(oneprod(a[1],H(a[2],b[0])),b[1]),b[2])
assert all(tm(a,b) in Ts for a,b in product(T,repeat=2))
assert all(tm(x,x)==x for x in T)
assert all(tm(tm(x,y),z0)==tm(x,tm(y,z0)) for x,y,z0 in product(T,repeat=3))
for e0 in T:
 local={tm(tm(e0,x),e0) for x in T}
 assert all(tm(tm(tm(tm(x,y),x),z0),x)==tm(tm(tm(x,y),z0),x) for x,y,z0 in product(local,repeat=3))
def beta(s):
 i,a,l=s;g=theta(a)
 return tuple(((i,k),None if a is None else act(k,a[0]),(l,g^k)) for k in G)
def shift(g,F):return tuple(F[g^k] for k in G)
def prod(F,H0):return tuple(tm(x,y) for x,y in zip(F,H0))
collapse=(0,1,1)
def qa(s):return(collapse[s[0]],theta(s[1]),s[2])
def qp(a,b):return(a[0],a[1]^theta(P[a[2]][b[0]])^b[1],b[2])
for s,t in product(S,repeat=2):
 w=theta(s[1])^theta(P[s[2]][t[0]])
 assert beta(sm(s,t))==prod(beta(s),shift(w,beta(t)))
 assert actor(sm(s,t))==rp(actor(s),actor(t)) and qa(sm(s,t))==qp(qa(s),qa(t))
 assert s==t or actor(s)!=actor(t) or beta(s)!=beta(t)
 assert s==t or qa(s)!=qa(t) or (s[0],s[2])!=(t[0],t[2]) or beta(s)!=beta(t)
E={s for s in S if sm(s,s)==s};assert all((s in E)==(rp(actor(s),actor(s))==actor(s)) for s in S)
assert all(any(sm(sm(s,t),s)==s and sm(sm(t,s),t)==t for t in S) for s in S)
for s in S:assert not ({sm(e,s) for e in E}&{sm(s,e) for e in E}&E) or s in E
for e0 in E:
 local={sm(sm(e0,x),e0) for x in S};le=tuple(x for x in local if x in E)
 assert all(sm(x,y) in E for x,y in product(le,repeat=2))
 assert all(sm(sm(sm(sm(x,y),x),z0),x)==sm(sm(sm(x,y),z0),x) for x,y,z0 in product(le,repeat=3))
contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[a]==sig[b])==(qa(a)==qa(b)) for a,b in product(S,repeat=2))
# Both forbidden types: nonunit identity-group; nonidentity group with a lower band component.
for p,a in ((((0,0,1),0),None),(((0,0,0),1),((0,0,1),1))):
 badP=((None,None,None),(None,p,None))
 def bad(x,y):return(x[0],am(am(x[1],badP[x[2]][y[0]]),y[1]),y[2])
 s=(1,a,1);d=bad(s,s);assert d!=s and bad(d,d)==d and bad(d,s)==d==bad(s,d)
# Missing unit row means a unit-middle source element cannot have any inverse.
badP=((((0,0,1),1),((0,0,1),1),((0,0,1),1)),(None,None,None))
def bad(x,y):return(x[0],am(am(x[1],badP[x[2]][y[0]]),y[1]),y[2])
s=(0,None,0);assert not any(bad(bad(s,t),s)==s for t in S)
print('base regular nonrectangular B=8, unitized A=17, source=',len(S),' natural_actor=',len(set(map(actor,S))),' actual_actor=',len(set(map(qa,S))),' T=',len(T),sep='')
print('PASS T closure/idempotence/all204^3 associativity, all local corners regular')
print('PASS all10404 source/actor/host products, q-rectangle injection, WEU/regular/local-r, actual tau')
print('CONTROLS two forbidden sandwich types violate WEU; missing unit row violates regularity')
print('LIMIT finite same-author check; full band/group theorem uses symbolic proof')
