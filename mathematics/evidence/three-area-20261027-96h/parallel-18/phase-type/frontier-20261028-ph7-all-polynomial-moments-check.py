#!/usr/bin/env python3
"""All nonnegative polynomial transforms satisfy all JLL inequalities.

An exact stronger pairwise power-sum inequality is checked by finite rational
arithmetic plus two rational geometric tails. It does not imply realization.
"""
from fractions import Fraction as F
from pathlib import Path
import json
z=F(8,9);t=F(31,6);R=F(83,100)
assert F(657,961)<R*R
A=lambda k:1+F(13,31)**k+F(1,31)**k+4*R**k
B=lambda k:1-4*R**k
assert 1-4*R**10>0 and A(10)**2<7*B(20)
assert A(1)*A(20)<7*B(21) and B(20)>0 and B(21)>0
C=F(1);D=F(0);s=[]
for k in range(29):
 s.append(t**k+(t-3)**k+(t-5)**k+4*C)
 C,D=(t-1)*C-z*D,C+(t-1)*D
assert all(s[k]>0 for k in range(1,10))
pairs=0
for a in range(1,10):
 for b in range(1,20):
  assert 7*s[a+b]>s[a]*s[b],(a,b)
  pairs+=1
out=Path(__file__).resolve().parent/'frontier-20261028-ph7-all-polynomial-moments-certificate.json'
out.write_text(json.dumps({'shift':'31/6','rational_ratio_bound':'sqrt(657)/31 < 83/100',
 'finite_pairs_a1to9_b1to19':pairs,'tail_1':'A10^2<7 B20',
 'tail_2':'A1*A20<7 B21',
 'result':'all pairwise 7 s_(a+b)>=s_a*s_b; all nonnegative-coefficient polynomial transforms satisfy all JLL orders',
 'scope':'spectral inequalities only, not a nonnegative matrix or PH realization'},indent=2)+'\n')
print('Exact Fraction PASS: all polynomial-transform JLL orders, finite mixed pairs',pairs)
