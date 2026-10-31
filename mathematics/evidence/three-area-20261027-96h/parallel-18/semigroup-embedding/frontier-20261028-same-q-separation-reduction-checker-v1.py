#!/usr/bin/env python3
"""Concrete positive/negative control for the generic pure-actor SEP reduction."""
from itertools import product
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));th=(0,1,0,1,0)
P=((4,4,4),(4,1,3),(4,4,1));B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
C=(((2,4),(2,0),(2,4)),((4,4),(0,4),(4,4)),((4,4),(4,0),(4,4)),((4,2),(0,2),(4,2)))
S=tuple(product(range(3),range(5),range(3)))
def m(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def q(a):return(a[0],th[a[1]],a[2])
def beta(a):return C[a[1]][a[2]] if a[1]<4 else (3 if a[0]==1 else 1,0 if a[2]==1 else 4)
def idem(a):return m(a,a)==a
E=[a for a in S if idem(a)]
assert all(a==b or q(a)!=q(b) or beta(a)!=beta(b) for a,b in product(E,repeat=2))
s=(0,1,0);t=(0,3,0);assert s!=t and q(s)==q(t) and not idem(s) and not idem(t)
sp=next(v for v in S if m(m(s,v),s)==s and m(m(v,s),v)==v)
left=(m(s,sp),m(t,sp));right=(m(sp,s),m(sp,t))
assert all(idem(x) for x in left+right)
assert q(left[0])==q(left[1]) and q(right[0])==q(right[1])
assert left[0]!=left[1] or right[0]!=right[1]
print('positive25-band model separates all same-q idempotent pairs=',len([1 for a,b in product(E,repeat=2) if a!=b and q(a)==q(b)]),sep='')
print('actor-only negative control: s=',s,' t=',t,' inverse_s=',sp,' idempotent pairs=',left,right,sep='')
print('PASS noninjective same-q elements induce an explicit unequal same-q idempotent pair')
print('LIMIT finite control; arbitrary-semi-group SEP reduction is the written argument')
