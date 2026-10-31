#!/usr/bin/env python3
"""All-unit sandwich branch when the globally regular base has empty K."""
from itertools import product
B=range(3);G=range(2);auto=(0,2,1)
def bm(a,b):return a if a==b else 0
def act(g,b):return auto[b] if g else b
def bp(a,b):return b if a is None else a if b is None else bm(a,b)
K={p for p in B if all(bm(bm(x,p),x)==x for x in B)};assert not K
assert all(bm(bm(x,y),z)==bm(x,bm(y,z)) for x,y,z in product(B,repeat=3))
assert all(auto[bm(x,y)]==bm(auto[x],auto[y]) for x,y in product(B,repeat=2))
A=(None,)+tuple(product(B,G));S=tuple(product(range(2),A,range(2)))
def theta(a):return 0 if a is None else a[1]
def am(a,b):
 if a is None:return b
 if b is None:return a
 return(bm(a[0],act(a[1],b[0])),a[1]^b[1])
def sm(s,t):return(s[0],am(s[1],t[1]),t[2])
def actor(s):return(s[0],theta(s[1]),s[2])
def qa(s):return theta(s[1])
rows=tuple(product(range(2),G));cols=tuple(product(range(2),G));T=tuple(product(rows,(None,0,1,2),cols))
def tm(x,y):return(x[0],bp(x[1],y[1]),y[2])
assert all(tm(x,x)==x for x in T)
assert all(tm(tm(x,y),z)==tm(x,tm(y,z)) for x,y,z in product(T,repeat=3))
assert all(tm(tm(tm(tm(x,y),x),z),x)==tm(tm(tm(x,y),z),x) for x,y,z in product(T,repeat=3))
def beta(s):
 i,a,l=s;g=theta(a)
 return tuple(((i,k),None if a is None else act(k,a[0]),(l,g^k)) for k in G)
def shift(g,F):return tuple(F[g^k] for k in G)
def prod(F,H):return tuple(tm(x,y) for x,y in zip(F,H))
for s,t in product(S,repeat=2):
 assert beta(sm(s,t))==prod(beta(s),shift(theta(s[1]),beta(t)))
 assert qa(sm(s,t))==qa(s)^qa(t)
 assert s==t or actor(s)!=actor(t) or beta(s)!=beta(t)
 assert s==t or qa(s)!=qa(t) or (s[0],s[2])!=(t[0],t[2]) or beta(s)!=beta(t)
E={s for s in S if sm(s,s)==s};contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(qa(s)==qa(t)) for s,t in product(S,repeat=2))
print('base=3 semilattice K=empty; A=',len(A),' source=',len(S),' natural_actor=',len(set(map(actor,S))),' actual_actor=',len(set(map(qa,S))),' T=',len(T),sep='')
print('PASS all64^3 T associativity+regular-band laws; all784 source/host laws, fibre and retained-rectangle injection, true tau')
print('LIMIT same-author finite control for all-unit branch; arbitrary proof is symbolic')
