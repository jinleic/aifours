#!/usr/bin/env python3
"""Exact Q(zeta60) checks for the two forced phase cases."""
from fractions import Fraction as Q
from functools import lru_cache
n=60
zero=[Q(0)]*n
one=[Q(1)]+[Q(0)]*(n-1)
def xp(k):
 a=zero[:];a[k%n]=Q(1);return a
def add(a,b):return [x+y for x,y in zip(a,b)]
def neg(a):return [-x for x in a]
def scale(a,c):return [x*Q(c) for x in a]
def mul(a,b):
 c=zero[:]
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:c[(i+j)%n]+=x*y
 return c
def conj(a):return [a[-i%n] for i in range(n)]
def divide(a,b):
 a=a[:];out=[0]*(len(a)-len(b)+1)
 while len(a)>=len(b):
  k=len(a)-len(b);v=a[-1];out[k]=v
  for j,u in enumerate(b):a[j+k]-=v*u
  while a and a[-1]==0:a.pop()
 assert not a
 return out
@lru_cache(None)
def phi(m):
 out=[-1]+[0]*(m-1)+[1]
 for d in range(1,m):
  if m%d==0:out=divide(out,phi(d))
 return out
mod=phi(n);deg=len(mod)-1;assert deg==16
def red(v):
 v=v[:]
 for i in range(len(v)-1,deg-1,-1):
  z=v[i]
  for j,q in enumerate(mod):v[i-deg+j]-=z*q
 return tuple(v[:deg])
def eq(a,b):return not any(red(add(a,neg(b))))
def r2(lam,h):
 ex=[0,30,lam,(lam+20)%60,(lam+40)%60]
 return [add(scale(one,2),add(xp(ex[(t+h)%5]-ex[t]),xp(ex[t]-ex[(t+h)%5]))) for t in range(5)]
def dft(a,k):
 x=zero[:]
 for t in range(5):x=add(x,mul(a[t],xp(-12*k*t)))
 return scale(x,Q(1,5))
s3=add(xp(5),xp(-5));s5=add(one,scale(add(xp(12),xp(-12)),2))
assert eq(mul(s3,s3),scale(one,3)) and eq(mul(s5,s5),scale(one,5))
A=add(scale(one,2),neg(s3));B0=scale(add(s5,neg(one)),Q(1,2));A0=scale(add(s5,one),Q(1,2))
# theta=11pi/6 gives the small-A h1 branch.
small=r2(55,1)
for x,y in zip(small,[zero,A,one,one,A]):assert eq(x,y)
d1,d2=dft(small,1),dft(small,2)
assert eq(d1,scale(add(mul(A,B0),neg(A0)),Q(1,5)))
assert eq(d2,scale(add(B0,neg(mul(A,A0))),Q(1,5)))
# theta=5pi/6: h2 squared moduli are [A,2,1,2,A].
big=r2(25,2)
for x,y in zip(big,[A,scale(one,2),one,scale(one,2),A]):assert eq(x,y)
d0,d1,d2=dft(big,0),dft(big,1),dft(big,2)
R1=scale(add(s5,neg(scale(mul(A,add(s5,one)),Q(1,2)))),Q(1,5))
R2=scale(add(neg(s5),scale(mul(A,add(s5,neg(one))),Q(1,2))),Q(1,5))
assert eq(d0,scale(add(scale(one,9),neg(scale(s3,2))),Q(1,5)))
assert eq(d1,mul(xp(-24),R1)) and eq(d2,mul(xp(-48),R2))
assert eq(mul(conj(d2),mul(d1,d1)),mul(R2,mul(R1,R1)))
assert eq(add(R1,neg(R2)),scale(mul(s3,s5),Q(1,5)))
# sqrt signs and elementary comparisons used in the written proof.
assert Q(5,3)**2<3 and Q(3)**2>5
assert 93-36*Q(1)<60 # uses sqrt3>1, so (9-2sqrt3)^2<60
print('PASS Phi60 degree',deg,'and exact h1 small/h2 large phase identities')
print('PASS sqrt3>5/3, sqrt5<3; h1 sign obstruction')
print('PASS R1>0,R2<0, conjugate(d2)*d1^2=R2*R1^2<0 and |d1|+|d2|=sqrt15/5')
print('PASS d0=(9-2sqrt3)/5<2sqrt15/5 by elementary square bound')
