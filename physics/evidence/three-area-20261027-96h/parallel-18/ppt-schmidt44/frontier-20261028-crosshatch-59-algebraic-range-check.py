#!/usr/bin/env python3
"""Exact Q(theta), theta^3=theta-1, rank2 span for a noncoordinate 4x9 cut."""
from fractions import Fraction as F
from itertools import combinations,product
import json
Z=(F(0),F(0),F(0));O=(F(1),F(0),F(0));T=(F(0),F(1),F(0));T2=(F(0),F(0),F(1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def scale(a,c):return tuple(x*F(c) for x in a)
def mul(a,b):
 c=[F(0)]*5
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 for k in (4,3):c[k-2]+=c[k];c[k-3]-=c[k];c[k]=0
 return tuple(c[:3])
assert mul(T,T2)==add(T,neg(O))
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
coords=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(x,y)) for x,y in product(edges,repeat=2)]
A=(1,3,4,5,7);source=[]
for q in coords:
 M=[[0]*9 for _ in range(5)]
 for a,b in q:
  if a in A:M[A.index(a)][b]+=1
 source.append(M)
# Alice quotient K=[I_4|-ones], kernel span(1,1,1,1,1).
images=[[[M[i][j]-M[4][j] for j in range(9)] for i in range(4)] for M in source]
def combination(d):
 M=[[Z for _ in range(9)] for _ in range(4)]
 for k,v in d.items():
  for i in range(4):
   for j in range(9):M[i][j]=add(M[i][j],scale(v,images[k][i][j]))
 return M
def det(m,rs,cs):
 a,b,c=rs;x,y,z=cs
 return add(add(mul(m[a][x],add(mul(m[b][y],m[c][z]),neg(mul(m[b][z],m[c][y])))),
                neg(mul(m[a][y],add(mul(m[b][x],m[c][z]),neg(mul(m[b][z],m[c][x])))))),
            mul(m[a][z],add(mul(m[b][x],m[c][y]),neg(mul(m[b][y],m[c][x])))))
q1={0:O,5:O};q2={1:O,4:O}
q3={0:scale(O,5),4:scale(O,7),2:scale(T2,5),3:scale(T,5),
    6:scale(T2,7),7:scale(T,7),8:scale(O,6),12:scale(O,3)}
def swapindex(i):return 4*(i%4)+i//4
q4={swapindex(i):v for i,v in q3.items()}
count=0
for q in (q1,q2,q3,q4):
 M=combination(q)
 for rr in combinations(range(4),3):
  for cc in combinations(range(9),3):assert det(M,rr,cc)==Z;count+=1
# Source high-index coefficient vectors 0,1,4,5 have determinant -70.
coef=[[F(1),0,0,1],[0,1,1,0],[5,0,7,0],[5,7,0,0]]
def detF(A):
 a=[list(map(F,row)) for row in A];d=F(1)
 for i in range(len(a)):
  j=next(k for k in range(i,len(a)) if a[k][i])
  if i!=j:a[i],a[j]=a[j],a[i];d=-d
  p=a[i][i];d*=p
  for j in range(i+1,len(a)):
   x=a[j][i]/p
   for k in range(i+1,len(a)):a[j][k]-=x*a[i][k]
 return d
assert detF(coef)==-70
# PPT of the actual 4x9 state via exact rational Schur elimination.
R=[[F(0) for _ in range(36)] for _ in range(36)]
for M in images:
 v=[F(x) for row in M for x in row]
 for i,x in enumerate(v):
  for j,y in enumerate(v):R[i][j]+=x*y
PT=[[R[9*(i//9)+j%9][9*(j//9)+i%9] for j in range(36)] for i in range(36)]
def psd(m):
 a=[row[:] for row in m];piv=[]
 while a:
  if any(a[i][i]<0 for i in range(len(a))):return None
  p=next((i for i in range(len(a)) if a[i][i]>0),None)
  if p is None:return piv if all(x==0 for row in a for x in row) else None
  s=a[p][p];piv.append(s);r=[j for j in range(len(a)) if j!=p]
  a=[[a[i][j]-a[i][p]*a[p][j]/s for j in r] for i in r]
 return piv
piv=psd(PT);assert piv is not None
print(json.dumps({'kernel':[1,1,1,1,1],'rank2_vectors':4,'qtheta_cubic':'theta^3-theta+1=0',
 'all_3x3_minors_checked':count,'high_quotient_coefficient_determinant':str(detF(coef)),
 'source_trace':str(sum(R[i][i] for i in range(36))),'pt_rank':len(piv),
 'limits':'Exact SR2-spanned range for this one noncoordinate filter, not a Schmidt-number upper bound.'},indent=2))
