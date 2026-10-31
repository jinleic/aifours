#!/usr/bin/env python3
"""Exact nonorthogonal, non-CR E-solid original-source finite-envelope control."""
from itertools import product

def swap(m):return ((m&1)<<1)|((m&2)>>1)
A=tuple(product(range(4),range(2)))
def am(a,b):return(a[0]&(swap(b[0]) if a[1] else b[0]),a[1]^b[1])
Q=((0,0),(0,1));D=tuple(product(range(2),range(2),range(2)))
def dm(a,b):return(a[0],a[1]^Q[a[2]][b[0]]^b[1],b[2])
S=tuple(product(A,D))
def sm(a,b):return(am(a[0],b[0]),dm(a[1],b[1]))
def idem(a):return sm(a,a)==a
def q(a):return(a[0][1],)+a[1]
def qm(a,b):return(a[0]^b[0],a[1],a[2]^Q[a[3]][b[1]]^b[2],b[3])
E={s for s in S if idem(s)}
assert len(S)==64 and len(E)==16
assert any(sm(a,b) not in E for a,b in product(E,repeat=2))
assert all(q(sm(a,b))==qm(q(a),q(b)) for a,b in product(S,repeat=2))
assert all((s in E)==(qm(q(s),q(s))==q(s)) for s in S)
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in S) for a in S)
for a in S:assert not ({sm(e,a) for e in E}&{sm(a,e) for e in E}&E) or a in E
for e in E:
 local={sm(sm(e,a),e) for a in S};le=tuple(a for a in local if a in E)
 assert all(sm(a,b) in E for a,b in product(le,repeat=2))
 assert all(sm(sm(sm(sm(a,b),a),c),a)==sm(sm(sm(a,b),c),a) for a,b,c in product(le,repeat=3))

def closure(gens):
 out=set(gens)
 while True:
  new=out|{sm(a,b) for a,b in product(out,repeat=2)}
  if new==out:return out
  out=new
core=closure(E)
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b and sm(a,b)==sm(b,a) for b in core) for a in core)
s=((1,1),(0,0,0));sp=((2,1),(0,0,0))
assert sm(sm(s,sp),s)==s and sm(sm(sp,s),sp)==sp
assert not any(sm(sm(s,b),s)==s and sm(sm(b,s),b)==b and sm(s,b)==sm(b,s) for b in S)
e=((3,0),(0,0,1));f=((3,0),(1,0,0));assert e in E and f in E and sm(e,f) not in E
F=closure((s,sp,e,f));EF={x for x in F if idem(x)}
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in F) for a in F)
for a in F:assert not ({sm(e,a) for e in EF}&{sm(a,e) for e in EF}&EF) or a in EF
assert any(sm(a,b) not in EF for a,b in product(EF,repeat=2))
for e0 in EF:
 local={sm(sm(e0,a),e0) for a in F};le=tuple(a for a in local if a in EF)
 assert all(sm(a,b) in EF for a,b in product(le,repeat=2))
 assert all(sm(sm(sm(sm(a,b),a),c),a)==sm(sm(sm(a,b),c),a) for a,b,c in product(le,repeat=3))
contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[a]==sig[b])==(q(a)==q(b)) for a,b in product(S,repeat=2))
print('ambient=',len(S),' E=',len(E),' core=',len(core),' actual_actor=',len(set(map(q,S))),sep='')
print('PASS regular/WEU/local-r, nonorthodox, non-completely-regular, core completely regular')
print('finite inverse-generator envelope=',len(F),' regular, locally-r and nonorthodox',sep='')
print('PASS actor purity and full 65^2 contexts/source')
print('LIMIT example only; abstract E-solid envelope proof is written')
