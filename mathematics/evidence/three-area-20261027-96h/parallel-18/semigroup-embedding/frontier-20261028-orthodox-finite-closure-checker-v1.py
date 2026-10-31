#!/usr/bin/env python3
"""Exact finite orthodox inverse-closure example with non-globally-regular E."""
from itertools import product
from collections import deque
B0=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));sig=(0,3,4,1,2)
def swap(m):return ((m&1)<<1)|((m&2)>>1)
def bm(a,b):return(B0[a[0]][b[0]],a[1]&b[1])
def act(g,a):return (sig[a[0]],swap(a[1])) if g else a
B=tuple(product(range(5),range(4)));S=tuple(product(B,range(2)))
def sm(a,b):return(bm(a[0],act(a[1],b[0])),a[1]^b[1])
E={a for a in S if sm(a,a)==a}
assert len(E)==20 and all((a in E)==(a[1]==0) for a in S)
assert all(sm(a,b) in E for a,b in product(E,repeat=2))
x=((1,3),0);y=((0,3),0);z=((3,3),0)
assert sm(sm(sm(sm(x,y),x),z),x)!=sm(sm(sm(x,y),z),x)
for e in E:
 local={sm(sm(e,a),e) for a in S};le=tuple(a for a in local if a in E)
 assert all(sm(a,b) in E for a,b in product(le,repeat=2))
 assert all(sm(sm(sm(sm(a,b),a),c),a)==sm(sm(sm(a,b),c),a) for a,b,c in product(le,repeat=3))
a=((1,1),1);ai=(act(1,a[0]),1)
assert sm(sm(a,ai),a)==a and sm(sm(ai,a),ai)==ai

def closure(gens):
 result=set(gens)
 while True:
  nxt=result|{sm(a,b) for a,b in product(result,repeat=2)}
  if nxt==result:return result
  result=nxt
F=closure((a,));Freg=closure((a,ai))
assert len(F)==3 and not any(sm(sm(a,b),a)==a for b in F)
assert F<=Freg
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in Freg) for a in Freg)
assert all(not ({sm(e,s) for e in E}&{sm(s,e) for e in E}&E) or s in E for s in Freg)
Ef={s for s in Freg if sm(s,s)==s}
for e in Ef:
 local={sm(sm(e,x),e) for x in Freg};le=tuple(x for x in local if x in Ef)
 assert all(sm(x,y) in Ef for x,y in product(le,repeat=2))
 assert all(sm(sm(sm(sm(x,y),x),z),x)==sm(sm(sm(x,y),z),x) for x,y,z in product(le,repeat=3))
# Directly verify reversed inverse words on all generated products.
for s,t in product(Freg,repeat=2):
 invs=[x for x in Freg if sm(sm(s,x),s)==s and sm(sm(x,s),x)==x]
 invt=[x for x in Freg if sm(sm(t,x),t)==t and sm(sm(x,t),x)==x]
 for si,ti in product(invs,invt):
  st=sm(s,t);rev=sm(ti,si)
  assert sm(sm(st,rev),st)==st and sm(sm(rev,st),rev)==rev
print('ambient orthodox source=',len(S),' idempotents=',len(E),' E locally regular but NOT globally regular',sep='')
print('monogenic finite F=',len(F),' nonregular; inverse-closed finite Fprime=',len(Freg),' regular/WEU/local-r',sep='')
print('PASS all inverse choices reversed, all Fprime products and local corners')
print('LIMIT finite same-author example; local-to-global/compactness is written theorem')
