#!/usr/bin/env python3
"""Exact rational check of a spectral point surviving the 7-state trace-2/3 test."""
from fractions import Fraction as F
z=F(8,9);p=F(8);q=F(15);h=(4+p)/7
s2=4*(1-z)+p*p-2*q
s3=-4+12*z-p**3+3*p*q
t2=s2-(4+p)**2/7
t3=s3+3*h*s2-2*(4+p)**3/49
slack=F(25,42)*t2**3-t3**2
assert h==F(12,7) and t2==F(874,63) and t3==F(-5692,147)
assert slack==F(9641252,107163)>0 and p*p-4*q==4
assert t2>0 and t3<0 and p>0 and q>0
print('Fraction exact 7-state centered trace2/trace3 non-exclusion point PASS')
print('z,p,q,h,tau2,tau3,comparison_slack:',z,p,q,h,t2,t3,slack)
print('hidden roots -3,-5; not a PH realization or existence proof')
