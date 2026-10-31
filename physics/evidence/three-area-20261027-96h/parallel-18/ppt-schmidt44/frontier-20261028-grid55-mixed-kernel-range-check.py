#!/usr/bin/env python3
"""Find exact rank2 A-bearing range vectors for six mixed Alice kernels.
Failure of this bounded search is INCONCLUSIVE.
"""
from itertools import combinations,product
import json
A=((0,2),(1,1),(2,0))
P=(((0,0),),((0,1),),((1,0),),((1,2),(3,4)),((1,4),),
   ((2,1),(4,3)),((2,2),(3,3)),((2,3),),((3,2),),((4,1),))
names=('u','v','w','b','p','c','d','e','f','g')
def proj(edges,head,tail):
 others=[i for i in range(5) if i not in (head,tail)]
 v=[[0]*5 for _ in range(4)]
 for a,b in edges:
  row=0 if a in (head,tail) else 1+others.index(a)
  v[row][b]+=1
 return v
def det(m,r,c):
 a,b,d=r;x,y,z=c
 return (m[a][x]*(m[b][y]*m[d][z]-m[b][z]*m[d][y])-
         m[a][y]*(m[b][x]*m[d][z]-m[b][z]*m[d][x])+
         m[a][z]*(m[b][x]*m[d][y]-m[b][y]*m[d][x]))
minors=list(product(combinations(range(4),3),combinations(range(5),3)))
cases=[]
for head,tail in product(range(3),(3,4)):
 aa=proj(A,head,tail);pp=[proj(q,head,tail) for q in P]
 active=[i for i,m in enumerate(pp) if any(v for row in m for v in row)]
 found=None;checked=0
 for vals in product((0,1,-1),repeat=len(active)):
  checked+=1;m=[row[:] for row in aa]
  for i,x in zip(active,vals):
   if x:
    for r in range(4):
     for c in range(5):m[r][c]+=x*pp[i][r][c]
  if all(det(m,r,c)==0 for r,c in minors):
   found={'coefficients':{names[i]:v for i,v in zip(active,vals) if v},'matrix':m};break
 cases.append({'kernel':f'|{head}>-|{tail}>','tested':checked,'active':len(active),
               'A_bearing_SR2_vector':found})
print(json.dumps({'cases':cases,'limits':'All hits are exact rank<=2 range vectors; every other generator is SR<=2. Therefore a hit proves the range is SR2-spanned, not that the state is SN2. No hit after the finite alphabet is inconclusive.'},indent=2))
