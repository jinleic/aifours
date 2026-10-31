#!/usr/bin/env python3
"""Exact nonrectangular regular-band base check for the top-sandwich Rees lift."""
from itertools import product
G=range(2); BB=tuple(product(range(2),range(2),range(2)))
def bm(a,b):return(a[0],b[1],a[2]&b[2])
def act(g,b):return(b[0]^g,b[1]^g,b[2])
assert all(bm(x,x)==x for x in BB)
assert all(bm(bm(x,y),z)==bm(x,bm(y,z)) for x,y,z in product(BB,repeat=3))
assert all(bm(bm(bm(bm(x,y),x),z),x)==bm(bm(bm(x,y),z),x) for x,y,z in product(BB,repeat=3))
assert all(act(g,bm(x,y))==bm(act(g,x),act(g,y)) for g,x,y in product(G,BB,BB))
top=tuple(x for x in BB if x[2]==1)
assert all(bm(bm(x,t),x)==x for x in BB for t in top)
P=((((0,0,1),0),((1,0,1),0)),(((0,1,1),0),((1,1,1),1)))
A=tuple(product(BB,G));S=tuple(product(range(2),A,range(2)))
def am(a,b):return(bm(a[0],act(a[1],b[0])),a[1]^b[1])
def sm(a,b):return(a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
def actor(a):return(a[0],a[1][1],a[2])
def qp(a,b):return(a[0],a[1]^P[a[2]][b[0]][1]^b[1],b[2])
rows=tuple(product(range(2),G));cols=tuple(product(range(2),G));T=tuple(product(rows,BB,cols))
def sandwich(col,row):
 l,t=col;j,u=row;pb,q=P[l][j]
 return act(t,pb) if q==(t^u) else top[0]
def tm(a,b):return(a[0],bm(bm(a[1],sandwich(a[2],b[0])),b[1]),b[2])
assert all(tm(x,x)==x for x in T)
assert all(tm(tm(x,y),z)==tm(x,tm(y,z)) for x,y,z in product(T,repeat=3))
for e in T:
 local={tm(tm(e,x),e) for x in T}
 assert all(tm(tm(tm(tm(x,y),x),z),x)==tm(tm(tm(x,y),z),x) for x,y,z in product(local,repeat=3))
def beta(s):
 i,(b,g),l=s
 return tuple(((i,k),act(k,b),(l,g^k)) for k in G)
def shift(g,F):return tuple(F[g^k] for k in G)
def prod(F,H):return tuple(tm(x,y) for x,y in zip(F,H))
for s,t in product(S,repeat=2):
 w=s[1][1]^P[s[2]][t[0]][1]
 assert beta(sm(s,t))==prod(beta(s),shift(w,beta(t)))
 assert actor(sm(s,t))==qp(actor(s),actor(t))
 assert s==t or actor(s)!=actor(t) or beta(s)!=beta(t)
E={s for s in S if sm(s,s)==s}
assert all((s in E)==(qp(actor(s),actor(s))==actor(s)) for s in S)
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in S) for a in S)
for s in S:assert not ({sm(e,s) for e in E}&{sm(s,e) for e in E}&E) or s in E
for e in E:
 local={sm(sm(e,x),e) for x in S};le=tuple(x for x in local if x in E)
 assert all(sm(x,y) in E for x,y in product(le,repeat=2))
 assert all(sm(sm(sm(sm(x,y),x),z),x)==sm(sm(sm(x,y),z),x) for x,y,z in product(le,repeat=3))
contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(actor(s)==actor(t)) for s,t in product(S,repeat=2))
# Replacing one top sandwich by a lower D-class element violates WEU.
badP=((P[0][0],P[0][1]),(P[1][0],((0,0,0),0)))
def bad(a,b):return(a[0],am(am(a[1],badP[a[2]][b[0]]),b[1]),b[2])
s=(1,((0,0,1),0),1);e=bad(s,s)
assert e!=s and bad(e,e)==e and bad(e,s)==e==bad(s,e)
print('base regular band=8, top rectangular D-class=4, group=C2; source=',len(S),' actor=',len(set(map(actor,S))),' T=',len(T),sep='')
print('PASS all128 T elements idempotent, all T associativity and local-corner regularity')
print('PASS all4096 source/actor/host products+injection, regularity, WEU, local-r, actual tau')
print('CONTROL lower-D sandwich yields explicit s^3=s^2!=s')
print('LIMIT finite same-author check; symbolic theorem is for arbitrary regular bands/groups')
