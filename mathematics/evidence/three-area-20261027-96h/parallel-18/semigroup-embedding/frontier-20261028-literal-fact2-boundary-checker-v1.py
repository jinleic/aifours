#!/usr/bin/env python3
"""Exact finite checks for the literal Fact2 regular-source boundary."""
from itertools import product
S=range(2)
def m(a,b):return b
assert all(m(a,a)==a for a in S)
assert all(m(m(a,b),c)==m(a,m(b,c)) for a,b,c in product(S,repeat=3))
for e in S:assert {m(m(e,x),e) for x in S}=={e}
assert m(0,1)!=m(1,0)
def word(*a):
 x=a[0]
 for y in a[1:]:x=m(x,y)
 return x
assert all(word(x,y,z,w,x)==word(x,y,z,x,z,w,x) for x,y,z,w in product(S,repeat=4))
# Semilattice meet by C2 with trivial action: all source inverses and idempotents explicit.
T=tuple(product(range(2),range(2)))
def tm(a,b):return(a[0]&b[0],a[1]^b[1])
Et=[a for a in T if tm(a,a)==a]
assert all(tm(a,b)==tm(b,a) for a,b in product(Et,repeat=2))
assert all(any(tm(tm(a,b),a)==a and tm(tm(b,a),b)==b for b in T) for a in T)
print('right-zero2: regular, WEU, each local corner singleton, SN, noncommuting idempotents')
print('semilattice2 by C2: size4, regular with commuting idempotents')
print('LIMIT any-homomorphic-image and regular-subsemigroup barrier is symbolic')
