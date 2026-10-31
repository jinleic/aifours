#!/usr/bin/env python3
"""Bounded exact algebra controls for a written CM-T2 parity deduction."""
from itertools import combinations
import json
rows=[]
for a in (1,2,3):
 for S in combinations((2,3,4,5,6),a):
  # Product of (1+y^(2^(s-1))) is in y^2 and evaluates to 2^a.
  powers=[1<<(s-1) for s in S]
  assert all(p%2==0 for p in powers)
  coeff={0:1}
  for p in powers:
   nxt=dict(coeff)
   for e,c in coeff.items():nxt[e+p]=nxt.get(e+p,0)+c
   coeff=nxt
  assert sum(coeff.values())==1<<a and all(e%2==0 for e in coeff)
  # Distinct-prime identity (1+x^u)(1-x^u+x^(2u))=1+x^(3u).
  for s in S:
   u=1<<(s-1);out={}
   for e,c in ((0,1),(u,1)):
    for f,d in ((0,1),(u,-1),(2*u,1)):out[e+f]=out.get(e+f,0)+c*d
   assert {e:c for e,c in out.items() if c}=={0:1,3*u:1}
  rows.append({'a':a,'owned_s':S,'even_factor_value':sum(coeff.values())})
print(json.dumps({'cases':len(rows),'examples':rows[:4],
                  'scope':'finite coefficient controls; CM-T2/all-order proof is written'},indent=2))
