#!/usr/bin/env python3
"""Finite exact CRT exponent and nonzero Weyl-label partition checks."""
from itertools import product
points=list(product(range(2),range(5)))
t=lambda a,b:(5*a+6*b)%10
assert {t(a,b) for a,b in points}==set(range(10))
for (a,b),(c,d) in product(points,repeat=2):
    assert (2*t(a,b)*t(c,d)-10*a*c-12*b*d)%20==0
for a,b in points:
    assert (t(a,b)**2-5*a-16*b*b)%20==0
odd=even=0
for m,k in product(range(10),repeat=2):
    if (m,k)==(0,0):continue
    if m%2 or k%2:
        odd+=1
        assert ((5*m)%10,(5*k)%10) in {(5,0),(0,5),(5,5)}
    else:
        even+=1
        assert ((m//2)%5,(k//2)%5)!=(0,0)
assert (odd,even)==(75,24)
print('PASS 100 Fourier and 10 chirp CRT exponent identities')
print('PASS Weyl labels: 75 nonzero odd-parity -> Pauli5 axes; 24 even -> nonzero F5^2')
print('These integer checks do not replace the written eigenvector/MUB arguments.')
