#!/usr/bin/env python3
"""Exact idempotent-generated nonregular subsource in the original 45-source."""
from itertools import product
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));th=(0,1,0,1,0)
P=((4,4,4),(4,1,3),(4,4,1));S=tuple(product(range(3),range(5),range(3)))
def sm(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def idem(a):return sm(a,a)==a
def q(a):return(a[0],th[a[1]],a[2])
def closure(gens):
 f=set(gens)
 while True:
  x=f|{sm(a,b) for a,b in product(f,repeat=2)}
  if x==f:return f
  f=x
e=(1,4,0);f=(0,4,1);x=sm(e,f);y=sm(f,e);z=(0,4,0)
assert idem(e) and idem(f) and x==(1,4,1) and not idem(x)
F=closure((e,f));assert len(F)==11
assert not any(sm(sm(x,t),x)==x and sm(sm(t,x),t)==t for t in F)
assert sm(sm(x,y),x)!=x
assert sm(sm(x,z),x)==x and sm(sm(z,x),z)==z and idem(z)
Fp=closure((e,f,z));assert len(Fp)==12 and F<=Fp
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in Fp) for a in Fp)
EF={a for a in Fp if idem(a)}
for a in Fp:assert not ({sm(e0,a) for e0 in EF}&{sm(a,e0) for e0 in EF}&EF) or idem(a)
for e0 in EF:
 local={sm(sm(e0,a),e0) for a in Fp};le=tuple(a for a in local if a in EF)
 assert all(sm(a,b) in EF for a,b in product(le,repeat=2))
 assert all(sm(sm(sm(sm(a,b),a),c),a)==sm(sm(sm(a,b),c),a) for a,b,c in product(le,repeat=3))
print('original45 idempotent generators e=',e,' f=',f,' generate F=',len(F),sep='')
print('x=ef=',x,' reverse fe=',y,' xyx=',sm(sm(x,y),x),' ambient inverse z=',z,sep='')
print('PASS x has no inverse in F; adjoining idempotent z gives Fprime=',len(Fp),' regular/WEU/local-r',sep='')
print('F actor image=',len({q(a) for a in F}),' Fprime actor image=',len({q(a) for a in Fp}),sep='')
print('LIMIT example only; no general finite-regular-envelope impossibility or existence')
