#!/usr/bin/env python3
"""Exact check of the two-gap P-flat equations on one known affine example."""
from fractions import Fraction as Q
p=5;zero=[Q(0)]*5;one=[Q(1)]+[Q(0)]*4
def xp(k):v=zero[:];v[k%5]=Q(1);return v
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(a,b):return [sum((a[i]*b[(k-i)%5] for i in range(5)),Q(0)) for k in range(5)]
def conj(a):return [a[-i%5] for i in range(5)]
def scale(a,c):return [x*Q(c) for x in a]
def eq(a,b):return all(a[i]-b[i]==a[4]-b[4] for i in range(4))
def dft(arr,k):
 s=zero[:]
 for t in range(5):s=add(s,mul(arr[t],xp(-k*t)))
 return scale(s,Q(1,5))
z=[xp(3*t) for t in range(5)];phase=[xp(3*t*t) for t in range(5)]
y=[];r=[]
for t in range(5):
 w=add(one,mul(z[(t+1)%5],conj(z[t])))
 y.append(mul(mul(phase[(t+1)%5],conj(phase[t])),w))
 w2=add(one,mul(z[(t+2)%5],conj(z[t])))
 r.append(mul(mul(phase[(t+2)%5],conj(phase[t])),w2))
c=[dft(y,k) for k in range(5)]
assert eq(c[0],zero) and eq(c[2],zero) and eq(c[3],zero) and eq(c[4],zero)
assert eq(c[1],mul(xp(3),add(one,xp(3))))
rr=[mul(v,conj(v)) for v in y];d=[dft(rr,k) for k in range(3)]
assert eq(d[1],zero) and eq(d[2],zero)
assert eq(d[0],mul(c[1],conj(c[1])))
assert eq(dft(r,0),zero) and eq(dft(r,1),zero) # sum r*omega^(4t) is dft index1
s=zero[:]
for v in z:s=add(s,v)
assert eq(s,zero)
print('PASS exact affine z=omega^(3t), p=omega^(3t²) satisfies all P-flat two-gap equations')
print('The example fails the separate X/Y cross-phase condition and is NOT a 10D MUB vector.')
