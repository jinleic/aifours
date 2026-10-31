#!/usr/bin/env python3
"""Exact search for a seminormal failure in the previously checked T204."""
from itertools import product
G=range(2);BB=tuple(product(range(2),range(2),range(2)))
def bm(a,b):return(a[0],b[1],a[2]&b[2])
def act(g,b):return(b[0]^g,b[1]^g,b[2])
def bp(a,b):return b if a is None else a if b is None else bm(a,b)
K=tuple(p for p in BB if all(bm(bm(b,p),b)==b for b in BB));z0=K[0]
P=((None,None,None),(None,((0,0,1),1),((1,1,1),1)))
rows=tuple(product(range(3),G));cols=tuple(product(range(2),G))
T=tuple((row,b,col) for row in rows for b in BB for col in cols)+tuple((row,None,col) for row in rows for col in cols if row[1]==col[1]);ids={x:i for i,x in enumerate(T)}
def H(col,row):
 l,t=col;j,u=row;p=P[l][j]
 if t==u:return None
 return act(t,p[0]) if p is not None and p[1]==(t^u) else z0
def tm(a,b):return(a[0],bp(bp(a[1],H(a[2],b[0])),b[1]),b[2])
M=tuple(tuple(ids[tm(a,b)] for b in T) for a in T);units=[i for i,x in enumerate(T) if x[1] is None]
checks=0;found=None
for a in units:
 for c in units:
  if T[a][0][1]==T[c][0][1]:continue
  for b,d in product(range(len(T)),repeat=2):
   left=M[M[M[M[a][b]][c]][d]][a]
   right=M[M[M[M[M[M[a][b]][c]][a]][c]][d]][a]
   checks+=1
   if left!=right:found=(a,b,c,d,left,right);break
  if found:break
 if found:break
if found:
 a,b,c,d,left,right=found
 print('COUNTEREXAMPLE checked=',checks,' T=',len(T),' indices=',found,' terms=',(T[a],T[b],T[c],T[d]),' values=',(T[left],T[right]),sep='')
else:print('NO_COUNTEREXAMPLE checked=',checks,' T=',len(T),' all aligned-unit x,z distinct indices; NOT universal',sep='')
