#!/usr/bin/env python3
from fractions import Fraction as F
# Candidate's actual q=C*b^(1/3), here q^3=2*b exactly.
b, q = F(1,16), F(1,2)
assert q**3 == 2*b
m = b/(1-b)
M2 = q*q + 2*m*q + m + 2*m*m
M3 = q**3 + 3*m*q*q + 3*(m+2*m*m)*q + m + 6*m*m + 6*m*m*m
# Layer cake b^index = (1-b) * sum_{k>=0} b^k 1_{(q+k)D}.
claimed_Z = 2*M2
actual_Z = (1-b)*claimed_Z
assert M2 == F(353,900)
assert claimed_Z == F(353,450)
assert actual_Z == F(353,480)
assert actual_Z/claimed_Z == F(15,16)
print('b=',b,'q=',q,'q^3=2b:',q**3==2*b)
print('M2=',M2,'M3=',M3,'displayed Z=',claimed_Z,'integral of b^index=',actual_Z)
print('If p=b^index/(2M2), its total mass=',actual_Z/claimed_Z,'not 1')
print('Repair: p=b^index/((1-b)*2M2); expected norm remains (2/3)*M3/M2=',F(2,3)*M3/M2)
