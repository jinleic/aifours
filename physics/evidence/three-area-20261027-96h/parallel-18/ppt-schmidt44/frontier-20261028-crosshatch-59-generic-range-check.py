#!/usr/bin/env python3
"""Exact polynomial and rational checks for generic 5x9 rank4 range construction."""
from fractions import Fraction as F
from itertools import combinations,product
import json
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
coords=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(x,y)) for x,y in product(edges,repeat=2)]
A=(1,3,4,5,7);src=[]
for q in coords:
 m=[[0]*9 for _ in range(5)]
 for a,b in q:
  if a in A:m[A.index(a)][b]+=1
 src.append(m)
N=7;zero={};unit={(0,)*N:1}
def var(i):
 x=[0]*N;x[i]=1;return{tuple(x):1}
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return{k:v for k,v in c.items() if v}
def neg(a):return{k:-v for k,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   k=tuple(i+j for i,j in zip(x,y));c[k]=c.get(k,0)+u*v
 return{k:v for k,v in c.items() if v}
v,p,l0,l1,l2,l3,l4=(var(i) for i in range(N))
coeff={0:unit,2:mul(v,v),3:v,8:mul(p,p),12:p}
M=[[{} for _ in range(9)] for _ in range(5)]
for j,c in coeff.items():
 for r in range(5):
  for b in range(9):
   if src[j][r][b]:M[r][b]=add(M[r][b],c)
C0=[M[r][0] for r in range(5)];C2=[M[r][2] for r in range(5)];C6=[M[r][6] for r in range(5)]
assert C0==[mul(p,p),mul(v,v),unit,zero,zero]
assert C2==[zero,unit,zero,v,zero] and C6==[unit,zero,zero,zero,p]
assert all(M[r][1]==mul(v,C2[r]) and M[r][3]==mul(p,C6[r]) for r in range(5))
assert all(not M[r][b] for r in range(5) for b in (4,5,7,8))
# pv*ell - [pv*l2*C0 + p*l3*C2 + v*l4*C6].
ell=(l0,l1,l2,l3,l4);res=[]
for i in range(5):
 rhs=add(add(mul(mul(mul(p,v),l2),C0[i]),mul(mul(p,l3),C2[i])),mul(mul(v,l4),C6[i]))
 res.append(sub(mul(mul(p,v),ell[i]),rhs))
assert res[0]==mul(v,sub(sub(mul(l0,p),mul(l2,mul(mul(p,p),p))),l4))
assert res[1]==mul(p,sub(sub(mul(l1,v),mul(l2,mul(mul(v,v),v))),l3))
assert res[2:]==[zero,zero,zero]
# Division-free kernel identity remains valid at v=0 or p=0.
beta=sub(l0,mul(l2,mul(p,p)));gamma=sub(l1,mul(l2,mul(v,v)));res2=[]
for i in range(5):
 rhs=add(add(mul(l2,C0[i]),mul(gamma,C2[i])),mul(beta,C6[i]))
 res2.append(sub(ell[i],rhs))
assert res2[:3]==[zero,zero,zero]
assert res2[3]==add(sub(mul(l2,mul(mul(v,v),v)),mul(l1,v)),l3)
assert res2[4]==add(sub(mul(l2,mul(mul(p,p),p)),mul(l0,p)),l4)
# Independent source copy reflections, including their local row/column actions.
perm=(1,0,3,2);high=(0,1,4,5);low={2,3,6,7,8,9,12,13}
for f1,f2 in product((0,1),repeat=2):
 for j in range(16):
  jj=4*(perm[j//4] if f1 else j//4)+(perm[j%4] if f2 else j%4)
  for rr,(a1,a2) in enumerate(((0,1),(1,0),(1,1),(1,2),(2,1))):
   aa=((2-a1) if f1 else a1,(2-a2) if f2 else a2);r2=A.index(3*aa[0]+aa[1])
   for bb in range(9):
    b1,b2=divmod(bb,3);bb2=3*((2-b1) if f1 else b1)+((2-b2) if f2 else b2)
    assert src[j][rr][bb]==src[jj][r2][bb2]
 assert (4*(perm[0] if f1 else 0)+(perm[0] if f2 else 0)) in high
 assert {4*(perm[j//4] if f1 else j//4)+(perm[j%4] if f2 else j%4) for j in low}==low
# Exceptional-looking kernel ell=(1,2,0,1,3), four reflected rational constructions.
ell0=(F(1),F(2),F(0),F(1),F(3));images=[]
for M0 in src:
 images.append([[F(M0[i][j])-ell0[i]*F(M0[4][j])/ell0[4] for j in range(9)] for i in range(4)])
def rank2(M):
 for rr in combinations(range(4),3):
  for cc in combinations(range(9),3):
   a,b,c=rr;x,y,z=cc
   d=M[a][x]*(M[b][y]*M[c][z]-M[b][z]*M[c][y])-M[a][y]*(M[b][x]*M[c][z]-M[b][z]*M[c][x])+M[a][z]*(M[b][x]*M[c][y]-M[b][y]*M[c][x])
   if d:return False
 return True
hits=[]
for f1,f2 in product((0,1),repeat=2):
 e=list(ell0)
 if f1:e[0],e[4]=e[4],e[0]
 if f2:e[1],e[3]=e[3],e[1]
 vv=e[3]/e[1];pp=e[4]/e[0]
 base={0:F(1),2:vv*vv,3:vv,8:pp*pp,12:pp}
 transformed={4*(perm[j//4] if f1 else j//4)+(perm[j%4] if f2 else j%4):x for j,x in base.items()}
 M0=[[sum(co*images[j][r][b] for j,co in transformed.items()) for b in range(9)] for r in range(4)]
 assert rank2(M0)
 H=[j for j in transformed if j in high];assert len(H)==1 and transformed[H[0]]==1
 hits.append({'high_index':H[0],'v':str(vv),'p':str(pp)})
assert {x['high_index'] for x in hits}==set(high)
# Center-coordinate kernel: zero roots v=p=0 also give all high directions.
for j in high:
 assert rank2([[F(src[j][r][b]) for b in range(9)] for r in (0,1,3,4)])
print(json.dumps({'source_rank3_columns_checked':True,'cubic_kernel_identities':10,
 'source_copy_reflections_checked':4*16*5*9,'sample_kernel':list(map(str,ell0)),
 'sample_rank2_minors_checked':8*4*84,'sample_high_vectors':hits,'zero_root_cases_checked':4,
 'limits':'Proves a broad open class of SR2-spanned ranges, not SN<=2 or a 4x4 witness.'},indent=2))
