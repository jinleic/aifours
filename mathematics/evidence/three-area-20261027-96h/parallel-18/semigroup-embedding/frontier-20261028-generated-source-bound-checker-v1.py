#!/usr/bin/env python3
"""Check generator-orbit bound and orbit expressions on the 45-source host."""
from itertools import product,combinations
from collections import deque
from math import comb
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));th=(0,1,0,1,0)
P=((4,4,4),(4,1,3),(4,4,1));S=tuple(product(range(3),range(5),range(3)))
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
C=(((2,4),(2,0),(2,4)),((4,4),(0,4),(4,4)),((4,4),(4,0),(4,4)),((4,2),(0,2),(4,2)))
def m(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def bm(a,b):return(B[a[0]][b[0]],B[a[1]][b[1]])
def beta(a):
 if a[1]<4:return C[a[1]][a[2]]
 return (3 if a[0]==1 else 1,0 if a[2]==1 else 4)
def weight(a,b):return(th[a[1]]+th[P[a[2]][b[0]]])%2

def closure(gens,express=False):
 expr={g:((0,i),) for i,g in enumerate(gens)};todo=deque(gens)
 while todo:
  s=todo.popleft()
  for i,g in enumerate(gens):
   t=m(s,g)
   if t not in expr:expr[t]=expr[s]+((weight(s,g),i),);todo.append(t)
 return expr
pairs=0
for p in combinations(S,2):
 pairs+=1;assert len(closure(p))<len(S)
G=((2,4,2),(1,4,1),(0,4,0));E=closure(G)
assert len(E)==len(S) and pairs==990
wrong=0
for s,w in E.items():
 result=None;incorrect=None
 for shift,i in w:
  b=beta(G[i]);v=b[::-1] if shift else b
  result=v if result is None else bm(result,v)
  incorrect=b if incorrect is None else bm(incorrect,b)
 assert result==beta(s)
 if incorrect!=beta(s):wrong+=1
assert wrong>0
c=[0,1]
for n in range(2,7):c.append(n*n*c[-1]*c[-1])
f6=sum(comb(6,k)*c[k] for k in range(1,7))
assert f6==272622932796281408879065986
print('source=45 generating rank=3; all',pairs,' two-generator pairs fail; three listed generators generate all',sep='')
print('PASS all45 generator-orbit coefficient expressions, max word=',max(map(len,E.values())),' wrong-shift failures=',wrong,sep='')
print('group orbit generators=6; Green-Rees F(6)=',f6,sep='')
print('LIMIT rank/orbit finite check; bound is theoretical, not an actual quotient size')
