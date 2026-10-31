#!/usr/bin/env python3
"""Finite free-band computation of left-semiregular band monoid regularity."""
from collections import deque
from itertools import product

def sig(w):
 if not w:return ()
 content=set(w)
 if len(content)==1:return ('one',w[0])
 seen=set()
 for i,x in enumerate(w):
  seen.add(x)
  if len(seen)==len(content):last=x;pre=w[:i];break
 seen=set()
 for i in range(len(w)-1,-1,-1):
  x=w[i];seen.add(x)
  if len(seen)==len(content):first=x;suf=w[i+1:];break
 return(last,sig(pre),first,sig(suf))
words=[];ix={};todo=deque()
def add(w):
 s=sig(w)
 if s not in ix:ix[s]=len(words);words.append(w);todo.append(w)
for c in 'abc':add(c)
while todo:
 w=todo.popleft()
 for c in 'abc':add(w+c)
assert len(words)==159
M=[[ix[sig(x+y)] for y in words] for x in words]
n=160
for i in range(159):M[i].append(i)
M.append(list(range(n)))
assert all(M[x][x]==x for x in range(n))
root=list(range(n));q=deque()
def find(a):
 while root[a]!=a:root[a]=root[root[a]];a=root[a]
 return a
def join(a,b):
 a,b=find(a),find(b)
 if a!=b:root[b]=a;q.append((a,b))
# Every substitution of x y z = x y z x z y z, including formal identity.
for a,b,c in product(range(n),repeat=3):
 lhs=M[M[a][b]][c]
 rhs=M[M[M[M[lhs][a]][c]][b]][c]
 join(lhs,rhs)
while q:
 a,b=q.popleft()
 for c in range(n):join(M[a][c],M[b][c]);join(M[c][a],M[c][b])
R=sorted({find(a) for a in range(n)});classes={a:i for i,a in enumerate(R)}
Q=tuple(tuple(classes[find(M[a][b])] for b in R) for a in R)
assert all(Q[x][x]==x for x in range(len(R)))
assert all(Q[Q[x][y]][z]==Q[x][Q[y][z]] for x,y,z in product(range(len(R)),repeat=3))
assert all(Q[Q[a][b]][c]==Q[Q[Q[Q[Q[Q[a][b]][c]][a]][c]][b]][c] for a,b,c in product(range(len(R)),repeat=3))
fail=next(((x,y,z) for x,y,z in product(range(len(R)),repeat=3)
           if Q[Q[Q[Q[x][y]][x]][z]][x]!=Q[Q[Q[x][y]][z]][x]),None)
print('free_band_3=159 plus identity=160; semiregular quotient=',len(R),sep='')
print('regular_identity_failure=',fail,sep='')
if fail is not None:print('COUNTERMODEL quotient_table=',Q,sep='')
else:print('PASS all quotient triples regular; conditional on Green-Rees normal forms')
print('LIMIT this tests variety implication, NOT the Billhardt source structure')
