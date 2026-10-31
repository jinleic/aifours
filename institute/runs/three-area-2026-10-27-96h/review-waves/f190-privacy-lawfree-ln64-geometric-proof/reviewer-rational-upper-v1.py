#!/usr/bin/env python3
"""Exact shell-law upper bound at g=1/2, independent of any arc certificate."""
from fractions import Fraction as Q
m=Q(1,63)
g=Q(1,2)
E2=m+2*m*m
E3=m+6*m*m+6*m**3
E4=m+14*m*m+36*m**3+24*m**4
second=g*g+2*m*g+E2
fourth=g**4+4*m*g**3+6*E2*g*g+4*E3*g+E4
J=fourth/(3*second)
assert second>0 and fourth>0 and J<Q(1,2)
print('PASS g=1/2 diamond shell exact J =',J,'< 1/2')
assert not (J>=Q(1,2))
print('PASS negative: J >= 1/2 rejected by the exact rational comparison')
# A comparison with the candidate tight upper endpoint is deliberately not used as a premise.
lo=Q(163006627735070347894185905345794,10**33)
hi=lo+Q(1,10**33)
assert J>hi
print('PASS negative: this simpler law does not establish the claimed tight upper endpoint')
