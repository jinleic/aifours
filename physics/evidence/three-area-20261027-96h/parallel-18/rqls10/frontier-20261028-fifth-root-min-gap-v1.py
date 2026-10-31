#!/usr/bin/env python3
"""Exact minimum nonzero squared modulus of a sum of five fifth roots.

Uses integer pairs (U,V) for 2|S|²=U+V sqrt(5); comparisons use integer
squares, not floats. Exhausts all 126 multiplicity profiles.
"""
from itertools import combinations_with_replacement
from collections import Counter


def sign(a,b):
    if b==0:return (a>0)-(a<0)
    if b>0:
        if a>=0:return 1
        return 1 if 5*b*b>a*a else -1
    if a<=0:return -1
    return 1 if a*a>5*b*b else -1


def squared(a):
    s=sum(x*x for x in a); p1=p2=0
    for i in range(5):
        for j in range(i+1,5):
            if (j-i)%5 in (1,4):p1+=a[i]*a[j]
            else:p2+=a[i]*a[j]
    return (2*s-p1-p2,p1-p2)

best=None; examples=[]; zero=[];total=0
for roots in combinations_with_replacement(range(5),5):
    a=tuple(roots.count(i) for i in range(5));uv=squared(a);total+=1
    assert sign(*uv)>=0
    if sign(*uv)==0:
        zero.append(a);continue
    if best is None or sign(uv[0]-best[0],uv[1]-best[1])<0:
        best=uv;examples=[a]
    elif uv==best:examples.append(a)
assert total==126 and zero==[(1,1,1,1,1)]
print('all five-root multiplicity profiles',total,'zero profiles',zero)
print('minimum 2*|S|² =',best[0],'+',best[1],'*sqrt(5)')
print('minimizing profiles',examples)
print('exact adjacent-profile lower bound PASS; QLS requires separate caller')
