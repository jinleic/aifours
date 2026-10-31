#!/usr/bin/env python3
"""Exact noninjective idempotent-separating quotient and outside-local control."""
from itertools import product
H=tuple(product(range(2),range(2),range(2)))
U=tuple(product(range(2),range(2)))
def hm(a,b):return(b[0],a[1]^b[1],a[2]^b[2])
def um(a,b):return(b[0],a[1]^b[1])
def pi(a):return(a[0],a[1])
EH={x for x in H if hm(x,x)==x};EU={x for x in U if um(x,x)==x}
assert len(H)==8 and len(U)==4 and len(EH)==len(EU)==2
assert {pi(x) for x in EH}==EU and len({pi(x) for x in EH})==len(EH)
assert len({pi(x) for x in H})==len(U) and len(H)>len(U)
assert all(pi(hm(a,b))==um(pi(a),pi(b)) for a,b in product(H,repeat=2))
assert all(any(um(um(a,b),a)==a and um(um(b,a),b)==b for b in U) for a in U)
assert um((0,0),(1,0))!=(um((1,0),(0,0)))
for e in EU:
 local={um(um(e,x),e) for x in U};le=[x for x in local if x in EU]
 assert all(um(a,b) in EU for a,b in product(le,repeat=2))
 assert all(um(um(um(um(a,b),a),c),a)==um(um(um(a,b),c),a) for a,b,c in product(le,repeat=3))
# Published-scope six-band control: identity corner itself fails regularity.
B=((0,2,2,0,4,5),(1,1,1,1,1,1),(2,2,2,2,2,2),(0,1,2,3,4,5),(0,5,2,4,4,5),(5,5,5,5,5,5))
def bm(a,b):return B[a][b]
assert all(bm(x,x)==x for x in range(6))
assert all(bm(bm(x,y),z)==bm(x,bm(y,z)) for x,y,z in product(range(6),repeat=3))
assert all(bm(3,x)==x==bm(x,3) for x in range(6))
assert bm(bm(bm(bm(0,4),0),1),0)!=bm(bm(bm(0,4),1),0)
print('noninjective idempotent-separating physical quotient H=8 → U=4; E maps bijectively')
print('PASS every U local idempotent band regular; source is noninverse')
print('CONTROL six-element regular band source has nonregular identity corner, outside target upper bound')
print('LIMIT finite check; arbitrary quotient/subsemigroup upper bound is symbolic')
