#!/usr/bin/env python3
"""Exact sparse 4x4 range screen for the published 5x5 grid PPT state.
A hit proves the projected range is SR2-spanned; failure is inconclusive.
"""
from itertools import product,combinations
import json

names=('u','v','w','b','p','c','d','e','f','g')
# Original paper coordinates, without a relabeling.
A=((0,2),(1,1),(2,0))
P=(((0,0),),((0,1),),((1,0),),((1,2),(3,4)),((1,4),),
   ((2,1),(4,3)),((2,2),(3,3)),((2,3),),((3,2),),((4,1),))
def projected(vec,rows,cols):
 out=[[0]*4 for _ in range(4)]
 for r,c in vec:
  if r in rows and c in cols:out[rows.index(r)][cols.index(c)]+=1
 return out
def det3(m,rr,cc):
 a,b,c=rr;x,y,z=cc
 return (m[a][x]*(m[b][y]*m[c][z]-m[b][z]*m[c][y])
        -m[a][y]*(m[b][x]*m[c][z]-m[b][z]*m[c][x])
        +m[a][z]*(m[b][x]*m[c][y]-m[b][y]*m[c][x]))
R=tuple(combinations(range(4),3));C=R
assert len(R)*len(C)==16
results=[]
for removed_row,removed_col in product((3,4),repeat=2):
 rows=[x for x in range(5) if x!=removed_row];cols=[x for x in range(5) if x!=removed_col]
 aa=projected(A,rows,cols);pp=[projected(q,rows,cols) for q in P]
 active=[i for i,m in enumerate(pp) if any(x for row in m for x in row)]
 examined=0;found=None
 for vals in product((0,1,-1),repeat=len(active)):
  examined+=1
  m=[r[:] for r in aa]
  for i,coef in zip(active,vals):
   if coef:
    for x in range(4):
     for y in range(4):m[x][y]+=coef*pp[i][x][y]
  if all(det3(m,rr,cc)==0 for rr in R for cc in C):
   found={'coefficients':{names[i]:v for i,v in zip(active,vals) if v},'matrix':m};break
 results.append({'delete_alice':removed_row,'delete_bob':removed_col,
                 'active_other_generators':len(active),'candidates_examined':examined,
                 'found_rank_at_most_2_vector_with_A_coefficient_1':found})
print(json.dumps({'source':'https://arxiv.org/html/2402.12966v1 Figure 2 and Appendix B',
  'cases':results,'limits':'Each found vector is exactly rank<=2; other edge generators are rank<=2, so the projected range is SR2-spanned. This does NOT prove the projected state has SN<=2. Search failure would be inconclusive.'},indent=2))
