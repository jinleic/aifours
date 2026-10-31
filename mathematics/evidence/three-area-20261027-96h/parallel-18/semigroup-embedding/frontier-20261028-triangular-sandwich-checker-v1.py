#!/usr/bin/env python3
"""Exhaust tag-level law and one collapsed-actor signed-sandwich source."""
from itertools import product
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));th=(0,1,0,1,0)
def coef(a,coltag,rowtag):
 v=(4,0)[rowtag];u=(1,3)[coltag]
 return ((2,v),(v,4),(4,v),(v,2),(u,v))[a]
def bm(x,y):return(B[x[0]][y[0]],B[x[1]][y[1]])
def act(x):return(x[1],x[0])
def sandwich(r,c,q):return 4 if q==0 else (1 if r^c==0 else 3)
valid=bad=outside=0
for a,b,ci,cj,r,rr,q in product(range(5),range(5),range(2),range(2),range(2),range(2),range(2)):
 p=sandwich(r,cj,q);res=A[A[a][p]][b];w=(th[a]+q)%2
 rhs=coef(b,cj,rr);rhs=act(rhs) if w else rhs
 ok=coef(res,ci,rr)==bm(coef(a,ci,r),rhs)
 if q and cj>r:
  outside+=1
  if not ok:bad+=1
 else:
  valid+=1;assert ok
assert (valid,outside,bad)==(700,100,20)
# Actual 4x3 source; Q has repeated columns 1,3, so q_tau merges source rows 1,3.
ct=(0,1,0,1);rt=(0,1,0)
P=((4,4,4,4),(4,1,3,1),(4,4,1,4))
S=tuple(product(range(4),range(5),range(3)))
def sm(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def bc(s):return coef(s[1],ct[s[0]],rt[s[2]])
def ra(s):return(s[0],th[s[1]],s[2])
def rprod(a,b):return(a[0],(a[1]+th[P[a[2]][b[0]]]+b[1])%2,b[2])
collapse=(0,1,2,1)
def qa(s):return(collapse[s[0]],th[s[1]],s[2])
def qprod(a,b):return(a[0],(a[1]+th[P[a[2]][b[0]]]+b[1])%2,b[2])
for s,t in product(S,repeat=2):
 w=(th[s[1]]+th[P[s[2]][t[0]]])%2
 assert bc(sm(s,t))==bm(bc(s),act(bc(t)) if w else bc(t))
 assert ra(sm(s,t))==rprod(ra(s),ra(t))
 assert qa(sm(s,t))==qprod(qa(s),qa(t))
 assert s==t or ra(s)!=ra(t) or bc(s)!=bc(t)
 rect=(s[0],s[2]);trect=(t[0],t[2])
 assert (rect[0],trect[1])==(sm(s,t)[0],sm(s,t)[2])
 assert s==t or qa(s)!=qa(t) or rect!=(t[0],t[2]) or bc(s)!=bc(t)
E={s for s in S if sm(s,s)==s}
assert all((s in E)==(rprod(ra(s),ra(s))==ra(s)) for s in S)
contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(qa(s)==qa(t)) for s,t in product(S,repeat=2))
print('tag-law valid=',valid,' excluded=',outside,' excluded law failures=',bad,sep='')
print('source=',len(S),' preliminary_actor=',len(set(map(ra,S))),' actual_actor=',len(set(map(qa,S))),sep='')
print('PASS all3600 source/r/q products, source-host laws, injection, retained rectangle')
print('PASS actual tau, 61^2 contexts/source; actor pure')
print('LIMIT excluded quadrant refutes only this coefficient formula')
