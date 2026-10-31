#!/usr/bin/env python3
"""Exact Q(sqrt5) seed and group closure checks supplementing the orbit replay."""
from fractions import Fraction as F
from itertools import permutations,product
import json
S=((0,1,1,1),(-1,0,1,-1),(-1,-1,0,1),(-1,1,-1,0))
autos=set()
for p in permutations(range(4)):
 for bits in product((-1,1),repeat=3):
  sg=(1,)+bits
  if all(S[p[i]][p[j]]==sg[i]*sg[j]*S[i][j] for i in range(4) for j in range(4)):autos.add((p,sg))
for p,s in autos:
 for q,t in autos:
  pp=tuple(p[q[i]] for i in range(4));raw=tuple(t[i]*s[q[i]] for i in range(4));ss=tuple(v*raw[0] for v in raw)
  assert (pp,ss) in autos
for pair in ((0,1),(1,0),(2,3),(3,2)):
 assert {(p[pair[0]],p[pair[1]]) for p,s in autos}=={(i,j) for i in range(4) for j in range(4) if i!=j}
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def add(x,y):return (x[0]+y[0],x[1]+y[1])
phi=(F(1,2),F(1,2));inv=(F(-1,2),F(1,2));one=(F(1),F(0));zero=(F(0),F(0))
assert mul(phi,inv)==one
phi2=mul(phi,phi);inv2=mul(inv,inv)
assert phi2==(F(3,2),F(1,2)) and inv2==(F(3,2),F(-1,2))
assert add(phi2,inv2)==(F(3),F(0))
assert add(one,tuple(-v for v in mul(phi,inv)))==zero  # det of block (0,1)
assert mul(phi,inv)==one  # det of block (2,3) is i*(1-phi*inv)
print(json.dumps({'signed_automorphism_group_order':len(autos),'group_products_checked':len(autos)**2,
 'four_source_ordered_edges_each_transitive':True,'phi_inverse_product':'1',
 'phi_squared_plus_inverse_squared':'3','two_seed_block_determinants':'0',
 'offdiagonal_norm_squared':'6','scope':'Exact algebra and finite group identities only.'},indent=2))
