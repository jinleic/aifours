#!/usr/bin/env python3
"""Exact finite polynomial coefficient controls for the P22 T2 deduction."""
from collections import defaultdict
import json
rows=[]
for s in range(1,9):
 u=1<<(s-1)
 # (1+x^u)*sum_{j=0}^{10}(-x^u)^j = 1+x^(11u).
 terms=defaultdict(int)
 for j in range(11):
  terms[j*u]+=(-1)**j;terms[(j+1)*u]+=(-1)**j
 terms={e:c for e,c in terms.items() if c}
 assert terms=={0:1,11*u:1}
 m=22*u;anchor_difference=11%m;partner=11*u
 if s==1:assert anchor_difference==partner
 else:assert anchor_difference!=partner
 rows.append({'s':s,'step':u,'period':m,'old_anchor_pair_matches':anchor_difference==partner})
print(json.dumps({'prime_power_cases':rows,
 'scope':'finite algebra controls; T2 and all-order inference are written'},indent=2))
