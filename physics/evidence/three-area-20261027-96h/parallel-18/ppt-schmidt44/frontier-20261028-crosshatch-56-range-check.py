#!/usr/bin/env python3
"""Exact source/matrix identities for the 5x6 CH concentration range."""
from itertools import product
from fractions import Fraction as F
import json
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
coords=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(x,y)) for x,y in product(edges,repeat=2)]
A=(1,3,4,5,7);B=(0,1,2,3,6,7)
def ket(q,rows,cols):
 v=[0]*(len(rows)*len(cols))
 for a,b in q:
  if a in rows and b in cols:v[len(cols)*rows.index(a)+cols.index(b)]+=1
 return v
def mat(gs,n):
 M=[[F(0) for _ in range(n)] for _ in range(n)]
 for v in gs:
  for i,x in enumerate(v):
   for j,y in enumerate(v):M[i][j]+=x*y
 return M
def psd(m):
 a=[row[:] for row in m];piv=[]
 while a:
  if any(a[i][i]<0 for i in range(len(a))):return None
  p=next((i for i in range(len(a)) if a[i][i]>0),None)
  if p is None:return piv if all(x==0 for row in a for x in row) else None
  s=a[p][p];piv.append(s);r=[j for j in range(len(a)) if j!=p]
  a=[[a[i][j]-a[i][p]*a[p][j]/s for j in r] for i in r]
 return piv
v6=[ket(q,A,B) for q in coords];v9=[ket(q,A,tuple(range(9))) for q in coords]
c6=[sum(x) for x in v6];c9=[sum(x) for x in v9]
assert c6==[3,2,2,2,2,2,2,1,2,1,0,0,2,0,0,0] and sum(c6)==21
assert c9==[3,3,2,2,3,3,2,2,2,2,0,0,2,2,0,0] and sum(c9)==28
flat6=[k for v in v6 for k,x in enumerate(v) if x];flat9=[k for v in v9 for k,x in enumerate(v) if x]
assert len(flat6)==len(set(flat6)) and len(flat9)==len(set(flat9))
for v in v9:
 assert all(sum(v[9*r+c] for c in range(9))<=1 for r in range(5))
 assert all(sum(v[9*r+c] for r in range(5))<=1 for c in range(9))
R=mat(v6,30);PT=[[R[6*(i//6)+j%6][6*(j//6)+i%6] for j in range(30)] for i in range(30)]
piv=psd(PT);assert piv is not None
R9=mat(v9,45);PT9=[[R9[9*(i//9)+j%9][9*(j//9)+i%9] for j in range(45)] for i in range(45)]
piv9=psd(PT9);assert piv9 is not None
# Normalized anchor a=1; variables b,c,d,e,f,g,h,i,j,k.
names=('b','c','d','e','f','g','h','i','j','k');n=10;unit={(0,)*n:1};zero={}
def var(i):
 x=[0]*n;x[i]=1;return{tuple(x):1}
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return{k:v for k,v in c.items() if v}
def neg(a):return{k:-v for k,v in a.items()}
def mul(a,b):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   k=tuple(i+j for i,j in zip(x,y));c[k]=c.get(k,0)+u*v
 return{k:v for k,v in c.items() if v}
def determinant(M,rs,cs):
 i,j,k=rs;a,b,c=cs
 return add(add(mul(M[i][a],add(mul(M[j][b],M[k][c]),neg(mul(M[j][c],M[k][b])))),
                neg(mul(M[i][b],add(mul(M[j][a],M[k][c]),neg(mul(M[j][c],M[k][a])))))),
            mul(M[i][c],add(mul(M[j][a],M[k][b]),neg(mul(M[j][b],M[k][a])))))
def drop(p,idx):return{ex:x for ex,x in p.items() if all(not ex[i] for i in idx)}
b,c,d,e,f,g,h,i,j,k=[var(x) for x in range(n)]
M=[[i,zero,j,k,unit,zero],[c,d,unit,zero,g,h],[unit,zero,b,zero,e,zero],
   [b,c,d,zero,f,g],[e,zero,f,i,k,zero]]
params=(unit,b,c,d,e,f,g,h,i,j,k);source_ids=(0,1,2,3,4,5,6,7,8,9,12)
actual=[[zero for _ in range(6)] for _ in range(5)]
for par,idx in zip(params,source_ids):
 for rr in range(5):
  for cc in range(6):
   if v6[idx][6*rr+cc]:actual[rr][cc]=add(actual[rr][cc],par)
assert actual==M
assert determinant(M,(2,3,4),(0,1,3))==mul(c,i)
assert drop(determinant(M,(1,2,4),(0,2,3)),(1,))==neg(i)
assert drop(determinant(M,(0,2,3),(0,1,4)),(7,))==c
assert drop(determinant(M,(0,1,2),(0,1,4)),(1,7))==neg(d)
assert drop(determinant(M,(0,2,3),(0,4,5)),(1,2,7))==neg(g)
assert drop(determinant(M,(0,1,2),(0,2,4)),(1,2,5,7))==neg(unit)
# One exact rational instance of the head-kernel column construction.
l=(F(1),F(2),F(3),F(4),F(5));C=l[1]*l[3]-l[0]*l[4]
p=(l[2]-C+1)/2;q=(l[2]-C-1)/2;b0=p/l[1];e0=q/l[0];tau=C;f0=(l[3]-tau*b0)/l[0]
C0=(0,0,1,b0,e0);C2=(0,1,b0,0,f0);C4=(1,0,e0,f0,0)
assert tuple(l[0]*C4[z]+l[1]*C2[z]+tau*C0[z] for z in range(5))==l
# Fixed rank3 q: a=b=c=e=g=i=j=1, all other coefficients zero.
fixed=[[1,0,1,0,1,0],[1,0,1,0,1,0],[1,0,1,0,1,0],
       [1,1,0,0,0,1],[1,0,0,1,0,0]]
assert fixed==[[sum(v6[idx][6*rr+cc] for idx in (0,1,2,4,6,8,9))
               for cc in range(6)] for rr in range(5)]
assert [fixed[rr][2] for rr in range(5)]==[1,1,1,0,0]
assert all(fixed[r]==fixed[0] for r in (1,2))
assert [fixed[r][1] for r in range(5)]==[0,0,0,1,0]
assert [fixed[r][3] for r in range(5)]==[0,0,0,0,1]
print(json.dumps({'source_5x6_trace':21,'source_5x6_rank':11,'source_5x6_pt_pivots':len(piv),
 'source_5x9_trace':28,'source_5x9_rank':12,'source_5x9_pt_pivots':len(piv9),'max_5x9_generator_schmidt_rank':3,
 'anchor_range_minor_identities':6,'head_column_sample_checked':True,'fixed_tail_plane_columns_checked':True,
 'limits':'SN3 source follows from the written range argument; all-projection span uses written complex-quadratic existence.'},indent=2))
