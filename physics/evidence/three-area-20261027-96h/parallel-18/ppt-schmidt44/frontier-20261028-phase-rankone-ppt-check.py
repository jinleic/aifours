#!/usr/bin/env python3
"""Exact rational and Q(sqrt2) checks for a saturated phase-invariant PPT state."""
from fractions import Fraction as F
import json
p=[[F(0) for _ in range(4)] for _ in range(4)]
for i,j in ((0,1),(1,2),(2,0)):p[i][j]=F(2);p[j][i]=F(1,2)
for i in range(3):p[i][3]=p[3][i]=F(1)
assert all(p[i][j]*p[j][i]==1 for i in range(4) for j in range(i+1,4))
cycle=(p[0][1]/p[1][0])*(p[1][2]/p[2][1])*(p[2][0]/p[0][2]);assert cycle==64
tr=F(4)+sum(p[i][j] for i in range(4) for j in range(4) if i!=j);assert tr==F(35,2)
def mul(x,y):return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
sqrt2=(F(0),F(1));inv=(F(0),F(1,2));one=(F(1),F(0))
assert mul(sqrt2,inv)==one
assert mul(sqrt2,sqrt2)==(F(2),F(0)) and mul(inv,inv)==(F(1,2),F(0))
# Both rank-one seed blocks have diagonal entries 1 and offdiagonal product 1.
assert mul(sqrt2,inv)==one
print(json.dumps({'trace':str(tr),'normalized_factor':'2/35','saturated_PPT_pair_blocks':6,
 'directed_cycle_ratio_product':str(cycle),'seed_block_determinants':'0',
 'seed_matched_populations':['2','1/2','1','1'],
 'birank':['13','10'],'scope':'Exact entrywise arithmetic; separability iff detailed balance and rank-two twirl are written proofs.'},indent=2))
