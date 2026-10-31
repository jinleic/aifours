#!/usr/bin/env python3
"""Exact second-gap Phi5 and all-q triple-symmetry checks."""
from fractions import Fraction as Q
from itertools import product
z=[Q(0)]*5;one=[Q(1)]+[Q(0)]*4
def xp(k):
 v=z[:];v[k%5]=Q(1);return v
def add(a,b):return [x+y for x,y in zip(a,b)]
def neg(a):return [-x for x in a]
def scale(a,c):return [Q(c)*x for x in a]
def mul(a,b):return [sum((a[i]*b[(k-i)%5] for i in range(5)),Q(0)) for k in range(5)]
def conj(a):return [a[-i%5] for i in range(5)]
def eq(a,b):return all((a[i]-b[i])==(a[4]-b[4]) for i in range(4))
sigma=[0,1,2,4,3];h=2;diff=[(sigma[(t+h)%5]-sigma[t])%5 for t in range(5)]
assert diff==[2,3,1,1,3]
r2=[mul(add(one,xp(k)),conj(add(one,xp(k)))) for k in diff]
def d(k):
 s=z[:]
 for t in range(5):s=add(s,mul(r2[t],xp(-k*t)))
 return scale(s,Q(1,5))
g=add(one,scale(add(xp(1),xp(4)),2));d0,d1,d2=d(0),d(1),d(2)
assert eq(d0,scale(add(scale(one,15),neg(g)),Q(1,10)))
assert eq(d1,scale(add(scale(one,5),g),Q(-1,10)))
assert eq(d2,scale(add(scale(one,5),neg(g)),Q(1,10)))
assert eq(add(neg(d1),d2),one)
assert eq(mul(d1,mul(d2,d2)),scale(add(scale(one,5),neg(g)),Q(-1,50)))
count=0
for q,c,dd in product(range(1,5),range(1,5),range(5)):
 eta=0 if c*c%5==1 else q
 images=[]
 for bq in (0,q):
  qq=(eta+bq*c*c)%5;images.append(qq)
  for j in range(5):
   jj=((2*bq*c*dd+3*c*j)*2)%5;const=(bq*dd*dd+3*dd*j)%5
   for t in range(5):
    assert (eta*t*t+bq*(c*t+dd)**2+3*(c*t+dd)*j-(qq*t*t+3*t*jj+const))%5==0;count+=1
 assert set(images)=={0,q}
print('PASS h2 Phi5 identities d0=(15-sqrt5)/10, d1=-(5+sqrt5)/10, d2=(5-sqrt5)/10')
print('PASS d1*d2²=-(5-sqrt5)/50<0 and |d1|+|d2|=1; d0<2')
print('PASS',count,'basis-preserving exact exponent identities for every nonzero q')
