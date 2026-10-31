#!/usr/bin/env python3
"""Rational interval proof that two coupled-gap magnitudes cannot agree."""
from fractions import Fraction as Q
from math import isqrt

def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def scale(a,c):return mul(a,(Q(c),Q(c)))
def sqrt_interval(a):
 assert a[0]>0
 S=10**8
 def floor_root(x):return isqrt((x.numerator*S*S)//x.denominator)
 return Q(floor_root(a[0]),S),Q(floor_root(a[1])+1,S)
def absolute(a):
 assert a[0]*a[1]>0
 return (a[0],a[1]) if a[0]>0 else (-a[1],-a[0])
def separate(a,b):return a[1]<b[0] or b[1]<a[0]
def show(a):return [float(a[0]),float(a[1])]
# Square these rational endpoints to certify the algebraic enclosures.
s3=(Q(1732,1000),Q(1733,1000));s5=(Q(2236,1000),Q(2237,1000))
assert s3[0]**2<3<s3[1]**2 and s5[0]**2<5<s5[1]**2
one=(Q(1),Q(1));five=(Q(5),Q(5));two=(Q(2),Q(2))
a=sub(two,s3);g0=scale(add(one,s5),Q(1,2));h0=scale(sub(s5,one),Q(1,2))
S2=scale(sub(g0,mul(a,h0)),Q(1,5));d2=scale(sub(h0,mul(a,g0)),Q(1,5))
D2=sub(S2,scale(d2,4));S=sqrt_interval(S2);D=sqrt_interval(D2)
uhi=scale(add(S,D),Q(1,2));vlo=scale(sub(S,D),Q(1,2))
assert vlo[0]>0
for u,v in ((uhi,vlo),(vlo,uhi)):
 R=sub(add(mul(s5,mul(u,u)),scale(mul(s5,mul(u,v)),Q(1,2))),
       scale(mul(add(five,s5),mul(v,v)),Q(1,4)))
 A=neg(mul(mul(add(two,s3),s5),v))
 B=sub(neg(scale(mul(add(one,s3),R),2)),one)
 absA,absB=absolute(A),absolute(B)
 assert separate(absA,absB)
 print('u,v',show(u),show(v),'|A|',show(absA),'|B|',show(absB),'DISJOINT')
print('PASS both coefficient branches; exact Fraction arithmetic, rational sqrt brackets')
