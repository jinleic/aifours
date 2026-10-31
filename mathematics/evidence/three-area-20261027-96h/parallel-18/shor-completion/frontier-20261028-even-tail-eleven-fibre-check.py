#!/usr/bin/env python3
"""Synthetic fibre tiling and anchored gcd11 controls for P=11*2^a."""
from math import gcd
import json
n=2640;m=16;P=list(range(44));Q=list(range(0,n,44))
assert len(P)==44 and len(Q)==60 and len({(p+q)%n for p in P for q in Q})==n
Pf=[[((p-i)//11)%m for p in P if p%11==i] for i in range(11)]
Qf=[[((q-j)//15)%m for q in Q if q%15==j] for j in range(15)]
assert all(len(v)==len(set(v))==4 for v in Pf+Qf)
assert all(len({(p+q)%m for p in a for q in b})==m for a in Pf for b in Qf)
assert all(len({x%2 for x in qf})==1 for qf in Qf) and not {0,1,7,13,14}<=set(Q)
rows=[]
for j in (0,1,7,13,14):
 other=(0,14) if j%2 else (1,7,13)
 bad=sorted({(7*(y-j))%11 for y in other})
 for t in bad:
  y=next(y for y in other if (7*(y-j))%11==t)
  assert gcd(j+30*t-y,n)==11
 rows.append({'j':j,'forbidden_t_mod11':bad})
print(json.dumps({'synthetic_fibre_pairs':len(Pf)*len(Qf),'all_single_parity':True,
 'anchor_controls':rows,'scope':'synthetic tiling, NOT a Shor completion'},indent=2))
