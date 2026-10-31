#!/usr/bin/env python3
"""Check idempotent-generated core and non-complete-regularity of the original45."""
from itertools import product
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));P=((4,4,4),(4,1,3),(4,4,1));S=tuple(product(range(3),range(5),range(3)))
def m(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
E={a for a in S if m(a,a)==a};C=set(E)
while True:
 d=C|{m(a,b) for a,b in product(C,repeat=2)}
 if d==C:break
 C=d
s=(1,4,1)
assert len(E)==24 and len(C)==len(S)==45 and s in C
assert not any(m(m(s,t),s)==s and m(m(t,s),t)==t and m(s,t)==m(t,s) for t in S)
print('source45 idempotents=',len(E),' idempotent-generated core=',len(C),sep='')
print('PASS s=(1,4,1) in core has no commuting mutual inverse; core not completely regular')
print('LIMIT exact finite check of E-solid failure, not a general P2G failure')
