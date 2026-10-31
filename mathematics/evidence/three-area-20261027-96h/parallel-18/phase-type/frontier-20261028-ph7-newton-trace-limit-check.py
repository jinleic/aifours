#!/usr/bin/env python3
"""Exact normalized Newton and centered trace checks for one spectral tuple."""
from fractions import Fraction as F
from math import comb
z=F(8,9);p=F(8);q=F(15)
e=[F(1),4+p,6+2*z+4*p+q,4+4*z+(6+2*z)*p+4*q,
 (1+z)**2+(4+4*z)*p+(6+2*z)*q,
 (1+z)**2*p+(4+4*z)*q,(1+z)**2*q,F(0)]
c=[v/comb(7,i)for i,v in enumerate(e)]
N=[c[i]**2-c[i-1]*c[i+1]for i in range(1,7)]
assert all(x>0 for x in N)
assert N==list(map(F,['437/1323','79949/178605','758773/2679075','2568677/1607445','2552737/413343','2088025/35721']))
a=4+p;h=a/7;s2=4*(1-z)+p*p-2*q;s3=-4+12*z-p**3+3*p*q
t2=s2-a*a/7;t3=s3+3*h*s2-2*a**3/49
slack=F(25,42)*t2**3-t3*t3
assert (t2,t3,slack)==(F(874,63),F(-5692,147),F(9641252,107163)) and slack>0
assert p*p-4*q==4
print('Fraction exact: all 6 normalized Newton inequalities and centered trace2/3 strictly pass')
print('N1..N6:',*[str(x)for x in N]);print('tau2,tau3,trace slack:',t2,t3,slack)
print('This is a spectral necessary-condition point, not a Metzler or PH witness.')
