#!/usr/bin/env python3
"""Prove all JLL moment inequalities for the 8/9 spectral counterpoint.

Exact rational finite verification + rational geometric tail. Does not claim
existence of an entrywise nonnegative matrix with this spectrum.
"""
from fractions import Fraction as F
from pathlib import Path
import json
R=F(12,13);z=F(8,9);assert F(1097,1296)<R*R
A20=1+F(3,4)**20+F(7,12)**20+4*R**20
A1=1+F(3,4)+F(7,12)+4*R
B40=1-4*R**40
assert A20<7 and B40>0 and A20*A20<7*B40
assert A1<7 and 7*(A1/7)**40<B40
assert 1-4*R**20>0
M=19*39;C=F(1);D=F(0);s=[]
for k in range(M+1):
 s.append(F(12)**k+F(9)**k+F(7)**k+4*C)
 C,D=11*C-z*D,C+11*D
assert all(s[k]>0 for k in range(1,20))
checks=0
for k in range(1,20):
 for m in range(2,40):
  assert s[k]**m<7**(m-1)*s[k*m],(k,m)
  checks+=1
out=Path(__file__).resolve().parent/'frontier-20261028-ph7-jll-all-orders-certificate.json'
out.write_text(json.dumps({'spectrum':['12','9','7','11+i*sqrt(8/9) twice','11-i*sqrt(8/9) twice'],
 'recurrence':'C0=1,D0=0; Cnext=11C-(8/9)D, Dnext=C+11D',
 'exact_finite_JLL_pairs_k_1to19_m_2to39':checks,'positive_moments_k_1to19':'PASS',
 'tail_rate':'sqrt(1097)/36 < 12/13',
 'tail_checks':['1-4*(12/13)^20>0','A20<7','A20^2<7*B40','A1<7','7*(A1/7)^40<B40'],
 'conclusion':'all k>=1,m>=2 s_k^m < 7^(m-1)s_(km), and s_k>0; necessary inequalities only, no realization claim'},indent=2)+'\n')
print('Exact Fraction PASS: all positive moments and all JLL inequalities; finite pairs',checks)
print('Tail via rational ratio 12/13, k>=20 or m>=40; no matrix-existence claim')
