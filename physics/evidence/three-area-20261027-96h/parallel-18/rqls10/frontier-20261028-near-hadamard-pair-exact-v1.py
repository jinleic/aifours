#!/usr/bin/env python3
"""Exact algebraic objective of one recovered near pair, NOT a witness."""
from itertools import combinations
E=[[0,0,0,0,0,0,0,0,0,0],
[0,9,9,3,14,0,9,16,5,0],
[0,16,0,12,12,16,8,4,4,8],
[0,5,9,15,6,16,17,0,9,8],
[0,12,0,4,4,12,16,8,8,16],
[0,1,9,7,18,12,5,4,13,16],
[0,8,0,16,16,8,4,12,12,4],
[0,17,9,19,10,8,13,8,17,4],
[0,4,0,8,8,4,12,16,16,12],
[0,13,9,11,2,4,1,12,1,12]]
# Phi20(x)=x^8-x^6+x^4-x^2+1.
phi=[1,0,-1,0,1,0,-1,0,1]
def rem(p):
    p=p[:]
    for i in range(len(p)-1,7,-1):
        v=p[i]
        for j in range(9):p[i-8+j]-=v*phi[j]
    return tuple((p+[0]*8)[:8])
P=[0]*20;bad0=bad1=0
for c,d in combinations(range(10),2):
    for k in range(10):
        if len({(E[t][c]-E[t][d]-2*k*t)%20 for t in range(10)})==1:
            raise AssertionError('parallel cells')
    for shift in (0,1):
        terms=[(E[t][d]-E[t][c]+2*shift*t*(d-c))%20 for t in range(10)]
        coeff=[terms.count(j) for j in range(20)]
        if any(rem(coeff)):
            if shift==0:bad0+=1
            else:bad1+=1
        for x in terms:
            for y in terms:P[(x-y)%20]+=2
# Ordered offdiagonal sum; squared normalized Gram entries divide by 100.
expected=[0]*20;expected[0]=1000;expected[1]=-500;expected[19]=-500
assert rem([P[j]-expected[j] for j in range(20)])==(0,)*8
assert bad0>0 and bad1>0
print('45 column-pair × 10 characters: no projectively parallel rays')
print('nonorthogonal unordered column pairs: H',bad0,'H∘F',bad1)
print('EXACT cost = 10 - 5*(zeta20+zeta20^-1) = 10*(1-cos(pi/10))')
print('NOT a Hadamard pair, NOT an original QLS witness, NO global bound claimed')
