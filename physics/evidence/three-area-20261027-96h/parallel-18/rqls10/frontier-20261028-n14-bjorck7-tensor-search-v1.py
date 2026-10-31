#!/usr/bin/env python3
"""Seek any even Fourier transversal from F2 tensor circulant Björck7.

All arithmetic in Z[zeta7]. Complete local7-ONB clique and two-label
incidence search for all 720 normalized source orders. If positive, an
independent original 14-vector replay is REQUIRED before adoption.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(0,)*6;ONE=(1,0,0,0,0,0)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def mul(x,y):
 p=[0]*11
 for i,a in enumerate(x):
  for j,b in enumerate(y):p[i+j]+=a*b
 for k in range(10,5,-1):
  v=p[k]
  for j in range(1,7):p[k-j]-=v
 return tuple(p[:6])
def rt(k):
 k%=7
 if k==6:return (-1,-1,-1,-1,-1,-1)
 v=[0]*6;v[k]=1;return tuple(v)
def cj(x):
 o=Z
 for i,a in enumerate(x):o=add(o,tuple(a*y for y in rt(-i)))
 return o
G=Z
for i in (1,2,4):G=add(G,rt(i))
for i in (3,5,6):G=add(G,neg(rt(i)))
assert mul(G,G)==(-7,0,0,0,0,0)
A=add((-3,0,0,0,0,0),G);V=(4,0,0,0,0,0);assert mul(cj(A),A)==(16,0,0,0,0,0)
seq=[V,V,V,A,V,A,A];K=[[seq[(t-c)%7]for c in range(7)]for t in range(7)]
def sumv(xs):
 o=Z
 for x in xs:o=add(o,x)
 return o
for i,j in itertools.combinations(range(7),2):
 assert sumv(mul(cj(K[t][i]),K[t][j])for t in range(7))==Z
 assert sumv(mul(cj(K[i][t]),K[j][t])for t in range(7))==Z
B=[[[[mul(rt(h),mul(cj(K[t][c]),K[t][d]))for h in range(7)]for d in range(7)]for c in range(7)]for t in range(7)]

def graph(O):
 adj=[0]*49
 good=[[[False]*7 for _ in range(7)]for _ in range(7)]
 for k in range(1,7):
  for c in range(7):
   for d in range(7):good[k][c][d]=(sumv(B[O[t]][c][d][k*t%7]for t in range(7))==Z)
 for i,j in itertools.combinations(range(49),2):
  r,c=divmod(i,7);s,d=divmod(j,7)
  if r==s or c==d or good[(s-r)%7][c][d]:adj[i]|=1<<j;adj[j]|=1<<i
 return adj

def cliques(adj):
 out=[];nodes=0
 def rec(mask,can,depth):
  nonlocal nodes;nodes+=1
  if depth==7:out.append(tuple(i for i in range(49)if mask>>i&1));return
  if depth+can.bit_count()<7:return
  while can:
   v=can&-can;can-=v;i=v.bit_length()-1;rec(mask|v,can&adj[i],depth+1)
 rec(0,(1<<49)-1,0);return out,nodes

def shape(Q):
 rr=[0]*7;cc=[0]*7
 for x in Q:rr[x//7]+=1;cc[x%7]+=1
 return rr,cc

def assign(Q,S):
 occ=[(0,x)for x in Q]+[(1,x)for x in S];adj=[[]for _ in range(14)]
 for axis in (0,1):
  for k in range(7):
   v=[i for i,(t,x) in enumerate(occ)if (x//7 if axis==0 else x%7)==k]
   if len(v)!=2:return None
   a,b=v;parity=1 if axis==0 else 1^occ[a][0]^occ[b][0];adj[a].append((b,parity));adj[b].append((a,parity))
 val=[None]*14
 for i in range(14):
  if val[i] is not None:continue
  val[i]=0;todo=[i]
  while todo:
   v=todo.pop()
   for w,p in adj[v]:
    a=val[v]^p
    if val[w] is None:val[w]=a;todo.append(w)
    elif val[w]!=a:return None
 return [(x//7,val[i],x%7,t^val[i])for i,(t,x) in enumerate(occ)]
orders=nodes=total=eligible=compatible=0;found=None;profiles=collections.Counter()
for perm in itertools.permutations(range(1,7)):
 O=(0,)+perm;adj=graph(O);cls,nd=cliques(adj);nodes+=nd;orders+=1;total+=len(cls);selected=[]
 for Q in cls:
  rr,cc=shape(Q)
  if max(rr)<=2 and max(cc)<=2:selected.append((Q,rr,cc))
 eligible+=len(selected);profiles[(len(cls),len(selected))]+=1
 for i,(Q,rr,cc) in enumerate(selected):
  for S,rs,cs in selected[i:]:
   if any(rr[k]+rs[k]!=2 or cc[k]+cs[k]!=2 for k in range(7)):continue
   compatible+=1;chosen=assign(Q,S)
   if chosen is not None:
    assert len({(r,u)for r,u,c,v in chosen})==14 and len({(c,v)for r,u,c,v in chosen})==14
    for (r,u,c,v),(s,x,d,y) in itertools.combinations(chosen,2):
     assert (u+v)%2!=(x+y)%2 or adj[7*r+c]>>(7*s+d)&1
    found={'source_order':O,'transversal':chosen,'local_cliques':[Q,S]};break
  if found:break
 if found:break
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'source':'circulant sequence (1,1,1,a,1,a,a), a=(-3+sqrt(-7))/4',
 'orders_examined':orders,'local_cliques':total,'eligible_local_cliques':eligible,'compatible_clique_pairs':compatible,'DFS_nodes':nodes,
 'profiles':{str(k):v for k,v in profiles.items()},'found':found,
 'boundary':'SAT is an exact combinatorial candidate requiring independent 14-dimensional original-vector replay; no SAT does not rule out arbitrary even products.'}
(P/'frontier-20261028-n14-bjorck7-tensor-search-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
