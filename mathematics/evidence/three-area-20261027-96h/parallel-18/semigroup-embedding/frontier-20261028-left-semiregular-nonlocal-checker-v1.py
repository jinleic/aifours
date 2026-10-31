#!/usr/bin/env python3
"""Literal finite countermodel: left semiregular need not be locally regular."""
from itertools import product
B=((0,2,2,0,4,5),(1,1,1,1,1,1),(2,2,2,2,2,2),(0,1,2,3,4,5),(0,5,2,4,4,5),(5,5,5,5,5,5))
def m(a,b):return B[a][b]
def word(*v):
 x=v[0]
 for y in v[1:]:x=m(x,y)
 return x
assert all(m(x,x)==x for x in range(6))
assert all(m(m(x,y),z)==m(x,m(y,z)) for x,y,z in product(range(6),repeat=3))
assert all(word(a,b,c)==word(a,b,c,a,c,b,c) for a,b,c in product(range(6),repeat=3))
assert all(m(3,x)==x==m(x,3) for x in range(6))
assert word(0,4,0,1,0)==2 and word(0,4,1,0)==5
assert word(0,4,3,1,0)==5 and word(0,4,3,0,3,1,0)==2
print('PASS six-element band, all216 associativity and left-semiregular xyz=xyzxz y z cases')
print('identity=3; regular law at x,y,z=(0,4,1) gives 2 != 5; local identity corner is whole band')
print('seminormal law at x,y,z,w=(0,4,3,1) gives 5 != 2')
print('LIMIT establishes LS variety does not imply local regularity; does not identify Billhardt example')
