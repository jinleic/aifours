#!/usr/bin/env python3
"""Exact small-residue controls for all-order anchored-tail refinement."""
from math import gcd
import json
n=2640;Y=(0,1,7,13,14)
# For odd anchor j and t=1,2 mod3, compare j+110t to 0/14.
rows=[]
for j in (1,7,13):
 for t in (1,2):
  q=j+110*t;opposite=0 if t==1 else 14
  assert gcd(q-opposite,n)==3
  rows.append({'old_tail':j,'t_mod3':t,'opposite':opposite,'gcd':3})
# For j=0, t=2 collides with each old odd anchor; j=14, t=1 likewise.
for j,t in ((0,2),(14,1)):
 for other in (1,7,13):assert gcd(j+110*t-other,n)==3
print(json.dumps({'odd_anchor_controls':rows,'even_anchor_controls':'PASS',
                  'scope':'bounded gcd identities; all-k proof is written'},indent=2))
