#!/usr/bin/env python3
"""Mechanics check for finite canonical quotient on the 2-point right-zero source."""
from collections import deque
from itertools import product
# Green-Rees recursive prefix/suffix signature, used here only on two letters.
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
words=('a','b','ab','ba','aba','bab');ids={sig(w):i for i,w in enumerate(words)}
assert len(ids)==6
M=tuple(tuple(ids[sig(x+y)] for y in words) for x in words)
assert all(M[x][x]==x for x in range(6))
assert all(M[M[x][y]][z]==M[x][M[y][z]] for x,y,z in product(range(6),repeat=3))
for e,a,b,c in product(range(6),repeat=4):
 x=M[M[e][a]][e];y=M[M[e][b]][e];z=M[M[e][c]][e]
 assert M[M[M[M[x][y]][x]][z]][x]==M[M[M[x][y]][z]][x]
def quotient(collapse=False):
 root=list(range(6));todo=deque()
 def find(a):
  while root[a]!=a:root[a]=root[root[a]];a=root[a]
  return a
 def join(a,b):
  a,b=find(a),find(b)
  if a!=b:root[b]=a;todo.append((a,b))
 # Mixed source relations: a*b=b and b*a=a, as the actor group is trivial.
 join(M[0][1],1);join(M[1][0],0)
 if collapse:join(0,1)
 while todo:
  a,b=todo.popleft()
  for c in range(6):join(M[a][c],M[b][c]);join(M[c][a],M[c][b])
 return [find(x) for x in range(6)]
normal=quotient();mutated=quotient(True)
assert len(set(normal))==2 and normal[0]!=normal[1]
assert len(set(mutated))==1 and mutated[0]==mutated[1]
c=[0,1]
for n in range(2,5):c.append(n*n*c[-1]*c[-1])
from math import comb
sizes=[sum(comb(n,k)*c[k] for k in range(1,n+1)) for n in range(1,5)]
assert sizes==[1,6,159,332380]
print('free band sizes ranks1..4=',sizes,'; rank2 local-regular identity checked on 6^4 substitutions',sep='')
print('2-point right-zero source: actual actor trivial, canonical quotient=2, distinct generators separated')
print('CONTROL forcing generator equality: canonical quotient=1 and injection fails')
print('LIMIT tiny mechanics check; general finite decidability uses Green-Rees finite-band theorem')
