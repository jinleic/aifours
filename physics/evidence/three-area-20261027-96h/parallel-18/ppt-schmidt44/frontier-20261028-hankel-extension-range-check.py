#!/usr/bin/env python3
"""Integer checks supporting the all-variable 4x4 Hankel extension argument."""
from itertools import combinations, permutations
from fractions import Fraction
import json
indices=range(4)
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
def minor(rows,cols):
 out={}
 for perm in permutations(range(3)):
  mon=tuple(sorted(rows[i]+cols[perm[i]] for i in range(3)))
  out[mon]=out.get(mon,0)+sign(perm)
 return {m:c for m,c in out.items() if c}
leading=set()
for r in combinations(indices,3):
 for c in combinations(indices,3):
  poly=minor(r,c)
  weights={m:sum(i*i for i in m) for m in poly}
  maxweight=max(weights.values())
  choices=[m for m in poly if weights[m]==maxweight]
  assert len(choices)==1
  want=tuple(sorted(r[i]+c[i] for i in range(3)))
  assert choices[0]==want
  leading.add(want)
expected={v for v in combinations(range(7),3) if v[1]-v[0]>=2 and v[2]-v[1]>=2}
assert leading==expected and len(leading)==10
faces={n:[v for v in combinations(range(7),n) if all(not set(m)<=set(v) for m in leading)] for n in (4,5)}
assert len(faces[4])==10 and not faces[5]
# Wedge coefficients for k1=(p,-s,1,0), k2=(0,p,-s,1).
# Columns are p^2, p*s, p, s^2, s, 1.
rows=[[1,0,0,0,0,0],[0,-1,0,0,0,0],[0,0,1,0,0,0],
      [0,0,-1,1,0,0],[0,0,0,0,-1,0],[0,0,0,0,0,1]]
A=[[Fraction(x) for x in r] for r in rows];det=Fraction(1)
for j in range(6):
 k=next((i for i in range(j,6) if A[i][j]),None);assert k is not None
 if k!=j:A[k],A[j]=A[j],A[k];det=-det
 t=A[j][j];det*=t
 for i in range(j+1,6):
  q=A[i][j]/t
  for k in range(j,6):A[i][k]-=q*A[j][k]
assert abs(det)==1
# Thom-Porteous specialization c2^2-c1*c3, c_i=binom(3+i,i).
assert 10**2-4*20==20
print(json.dumps({'3x3_minors':16,'distinct_diagonal_initial_monomials':len(leading),
 'four_vertex_facets':len(faces[4]),'five_vertex_faces':len(faces[5]),
 'wedge_coefficient_determinant':str(det),'Porteous_integer':20,
 'scope':'Combinatorics only; secant irreducibility, Hilbert degeneration, proper-intersection degree and Porteous theorem are named written imports.'},indent=2))
