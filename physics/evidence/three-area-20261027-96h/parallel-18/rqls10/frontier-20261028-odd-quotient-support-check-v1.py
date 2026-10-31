#!/usr/bin/env python3
"""Finite sanity checks for the written odd-quotient and rank argument."""
for m in (3,5,7,9,15,21):
 checked=0
 for a in range(1,m):
  for b in range(1,m):
   assert len({0,a,(-b)%m,(a-b)%m})>=3,(m,a,b)
   checked+=1
 print('odd quotient',m,'nonzero value pairs',checked,'PASS')
for p in (3,5,7,11,13,17,19):
 assert all(p*p!=2*p*r for r in range(p+1))
 print('odd p',p,'rank trace contradiction PASS')
print('Finite checks corroborate, but do not replace, the all-odd-group written argument.')
