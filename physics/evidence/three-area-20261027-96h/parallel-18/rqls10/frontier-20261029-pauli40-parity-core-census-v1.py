#!/usr/bin/env python3
"""Complete exact 40-ray parity-core and balanced-3-color census."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli40-source-vectors-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='a4f6cfedaa499442551a664599a8fbd9c8529388abc9c040f39ec57d9ddd5d10';d=json.loads(raw);V=[[(a,b)for a,b in d['vectors'][str(i)]]for i in range(1,41)]
def dot(a,b):return (sum(x*u+y*v for (x,y),(u,v)in zip(a,b)),sum(x*v-y*u for (x,y),(u,v)in zip(a,b)))
def norm(a):return sum(x*x+y*y for x,y in a)
assert all(norm(x)>0 for x in V)
for i,j in itertools.combinations(range(40),2):
 x,y=dot(V[i],V[j]);assert x*x+y*y!=norm(V[i])*norm(V[j])
B=[q for q in itertools.combinations(range(40),4)if all(dot(V[a],V[b])==(0,0)for a,b in itertools.combinations(q,2))];assert len(B)==40
inc=[[j for j,q in enumerate(B)if i in q]for i in range(40)];assert all(len(x)==4 for x in inc)
solutions=[];nodes=0
def search(state):
 global nodes
 nodes+=1;state=state[:]
 while True:
  change=False;k=state.count(1);free=[i for i,x in enumerate(state)if x<0]
  if k>15 or k+len(free)<15:return
  forced={}
  if k==15:forced.update({i:0 for i in free})
  elif k+len(free)==15:forced.update({i:1 for i in free})
  for ids in inc:
   count=sum(state[i]==1 for i in ids);F=[i for i in ids if state[i]<0]
   if count>2 or count==1 and not F:return
   val=0 if count==2 or count==0 and len(F)==1 else 1 if count==1 and len(F)==1 else None
   if val is not None:
    for i in F:
     if i in forced and forced[i]!=val:return
     forced[i]=val
  if forced:
   for i,v in forced.items():
    if state[i]<0:state[i]=v;change=True
    elif state[i]!=v:return
  if not change:break
 if all(x>=0 for x in state):
  assert sum(state)==15;solutions.append(tuple(i for i,x in enumerate(state)if x==1));return
 best=max((i for i,x in enumerate(state)if x<0),key=lambda j:sum(1 for ids in inc if j in ids and any(state[i]==1 for i in ids)))
 for v in (0,1):state[best]=v;search(state);state[best]=-1
search([-1]*40)
assert len(solutions)==len(set(solutions))
def color(inds):
 q=[B[i]for i in inds];adj=[0]*15
 for i,j in itertools.combinations(range(15),2):
  if set(q[i])&set(q[j]):adj[i]|=1<<j;adj[j]|=1<<i
 masks=[1,0,0];counts=[1,0,0];nodes=0;answer=None
 def rec(todo):
  nonlocal nodes,answer
  nodes+=1
  if not todo:answer=masks[:];return
  best=min(todo,key=lambda v:sum(counts[c]<5 and not(adj[v]&masks[c])for c in range(3)))
  for c in range(3):
   if counts[c]>=5 or adj[best]&masks[c]:continue
   masks[c]|=1<<best;counts[c]+=1;rec(todo-{best});counts[c]-=1;masks[c]&=~(1<<best)
 rec(set(range(1,15)))
 return answer,nodes,tuple(sorted(x.bit_count()for x in adj))
records=[]
for q in sorted(solutions):
 answer,n,coldeg=color(q);records.append({'basis_indices':q,'colorable':answer is not None,'color_masks':answer,'color_nodes':n,'degrees':coldeg})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'source_rays':40,'distinct_projective_pairs':780,'orthogonal_4bases':len(B),
 'parity_search_nodes':nodes,'30ray_15basis_2occ_sets':len(solutions),'balanced_3colorable':sum(x['colorable']for x in records),
 'bases':B,'records':records,'scope':'Only the cited 40-ray subset; not all 4D 30–15 configurations.'}
(P/'frontier-20261029-pauli40-parity-core-census-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k not in ('bases','records')},indent=2))
