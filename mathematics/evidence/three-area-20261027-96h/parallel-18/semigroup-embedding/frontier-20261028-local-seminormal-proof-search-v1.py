#!/usr/bin/env python3
"""Bounded sound congruence proof search for local regular => seminormal.

Only explicitly instantiated local identities and generator contexts are used.
A limit/absence result proves nothing. Green-Rees normal forms are an import.
"""
from itertools import product
from collections import deque
import sys,time

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
limit=int(sys.argv[1]);seconds=float(sys.argv[2]);deadline=time.monotonic()+seconds
W=[];ids={};parent=[];queue=deque();edges=[];adj=[]
def add(w):
 k=sig(w)
 if k not in ids:
  if len(W)>=limit:raise OverflowError('state cap')
  ids[k]=len(W);W.append(w);parent.append(len(parent));adj.append([])
 return ids[k]
def root(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
def join(a,b,why):
 ra,rb=root(a),root(b)
 if ra!=rb:
  parent[rb]=ra;eid=len(edges);edges.append((a,b,why));adj[a].append((b,eid));adj[b].append((a,eid));queue.append((a,b,eid))
u=add('abcda');v=add('abcacda')
try:
 for e,a,b,c in product('abcd',repeat=4):
  x=e+a+e;y=e+b+e;z=e+c+e
  join(add(x+y+x+z+x),add(x+y+z+x),('local_identity',e,a,b,c))
 while queue and root(u)!=root(v):
  if time.monotonic()>=deadline:raise TimeoutError('time cap')
  a,b,eid=queue.popleft()
  for k in 'abcd':
   join(add(k+W[a]),add(k+W[b]),('left',eid,k))
   join(add(W[a]+k),add(W[b]+k),('right',eid,k))
 if root(u)==root(v):
  path=deque([u]);seen={u:None}
  while path and v not in seen:
   z=path.popleft()
   for w,eid in adj[z]:
    if w not in seen:seen[w]=(z,eid);path.append(w)
  seq=[];x=v
  while x!=u:
   p,eid=seen[x];seq.append(eid);x=p
  needed=set(seq);todo=list(seq)
  while todo:
   eid=todo.pop();why=edges[eid][2]
   if why[0] in ('left','right') and why[1] not in needed:needed.add(why[1]);todo.append(why[1])
  print('PROOF_FOUND states=',len(W),' merges=',len(edges),' root_path=',seq,' needed=',len(needed),sep='')
  for i in sorted(needed):
   a,b,why=edges[i];print('edge',i,repr(W[a]),repr(W[b]),repr(why))
 else:print('INCONCLUSIVE initial literal instances exhausted states=',len(W),' merges=',len(edges),sep='')
except (OverflowError,TimeoutError) as ex:
 print('INCONCLUSIVE reason=',str(ex),' states=',len(W),' merges=',len(edges),' queued=',len(queue),sep='')
