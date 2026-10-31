#!/usr/bin/env python3
"""Synthetic fibre tiling and anchored residue controls for the P=5*2^a family."""
from math import gcd
import json
n=2640;m=16;P=list(range(20));Q=list(range(0,n,20))
assert len(P)==20 and len(Q)==132 and len({(p+q)%n for p in P for q in Q})==n
Pf=[[((p-i)//5)%m for p in P if p%5==i] for i in range(5)]
Qf=[[((q-j)//33)%m for q in Q if q%33==j] for j in range(33)]
assert all(len(v)==len(set(v))==4 for v in Pf+Qf)
assert all(len({(p+q)%m for p in a for q in b})==m for a in Pf for b in Qf)
assert all(len({x%2 for x in qf})==1 for qf in Qf) and not {0,1,7,13,14}<=set(Q)
# Odd anchored fibres: each excluded t class creates gcd5 vs0 or14.
for j in (1,7,13):
 for t in range(5):
  if t in ((-j)%5,(14-j)%5):
   assert gcd(j+66*t-(0 if t==(-j)%5 else 14),n)==5
# Even anchored fibres: compare to an appropriate old odd tail.
for j in (0,14):
 for t in range(5):
  for other in (1,7,13):
   if (j+66*t-other)%5==0:assert gcd(j+66*t-other,n)==5
print(json.dumps({'synthetic_fibre_pairs':len(Pf)*len(Qf),'all_single_parity':True,
 'residue_gcd_controls':'PASS','scope':'synthetic tiling, NOT a Shor completion'},indent=2))
