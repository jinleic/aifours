#!/usr/bin/env python3
"""Exact original-vector transversal search for the cited isolated A8A matrix.

a=(1+2*i*sqrt2)/3=(1+2*zeta8+2*zeta8^3)/3. Retain full DFS trees.
This is one literal non-Butson monomial class, not all n8 Hadamards.
"""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
S=[['a','1','-a','1','-a','-a','a','1'],['1','-a','1','a','-a','a','-a','1'],['-a','1','-a','a','1','a','1','-a'],['1','a','a','1','1','-a','-a','-a'],['-a','-a','1','1','a','-a','1','a'],['-a','a','a','-a','-a','1','1','1'],['a','-a','1','-a','1','1','a','-a'],['1','1','-a','-a','a','1','-a','a']]
Z=(0,0,0,0);ONE=(9,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 v=[0]*4
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[(i+j)%4]+=(1 if i+j<4 else -1)*x*y
 return tuple(v)
def rt(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def cj(a):
 out=Z
 for i,x in enumerate(a):out=add(out,tuple(x*y for y in rt(-i)))
 return out
A=(1,2,0,2);T=(3,0,0,0)
K=[[A if x=='a' else neg(A) if x=='-a' else T for x in row]for row in S]
def total(xs):
 out=Z
 for x in xs:out=add(out,x)
 return out
for t in range(8):
 for c in range(8):assert mul(cj(K[t][c]),K[t][c])==ONE
for a,b in itertools.combinations(range(8),2):
 assert total(mul(cj(K[t][a]),K[t][b]) for t in range(8))==Z
 assert total(mul(cj(K[a][t]),K[b][t]) for t in range(8))==Z
G=[[[mul(cj(K[t][c]),K[t][d])for d in range(8)]for c in range(8)]for t in range(8)]
def pmatch(mask,adj):
 if not mask:return True
 c=(mask&-mask).bit_length()-1
 return any(pmatch(mask&~(1<<c)&~(1<<d),adj)for d in range(c+1,8)if mask>>d&1 and adj[c]>>d&1)
cases=[];halves=matching=nodes=0;found=None
for E in itertools.combinations(range(1,8),3):
 ev=(0,)+E;od=tuple(x for x in range(8)if x not in ev);halves+=1;adj=[0]*8
 for c,d in itertools.combinations(range(8),2):
  if total(G[t][c][d]for t in ev)==Z:adj[c]|=1<<d;adj[d]|=1<<c
 if not pmatch(255,adj):continue
 matching+=1
 for ep in itertools.permutations(E):
  for op in itertools.permutations(od):
   order=(0,op[0],ep[0],op[1],ep[1],op[2],ep[2],op[3])
   good=[[[False]*8 for _ in range(8)]for _ in range(8)]
   for d in range(1,8):
    for c in range(8):
     for e in range(8):
      if c!=e:good[d][c][e]=(total(mul(rt(d*t),G[order[t]][c][e])for t in range(8))==Z)
   ass={0:0}
   def dfs():
    global nodes,found
    nodes+=1
    if len(ass)==8:found={'order':order,'column_per_row':[ass[r]for r in range(8)]};return {'found':True}
    used=set(ass.values());best=None
    for r in range(8):
     if r in ass:continue
     opts=[c for c in range(8)if c not in used and all(good[(r-s)%8][d][c]for s,d in ass.items())]
     if best is None or len(opts)<len(best[1]):best=(r,opts)
    r,opts=best;branches={}
    for c in opts:
     ass[r]=c;branches[str(c)]=dfs();del ass[r]
     if found:return {'row':r,'branches':branches}
    return {'row':r,'branches':branches}
   tree=dfs();cases.append({'E':ev,'order':order,'tree':tree})
   if found:break
  if found:break
 if found:break
obj={'source':'https://arxiv.org/html/2505.22947v1 §3.2 A_8A',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'root_a':'(1+2*zeta8+2*zeta8^3)/3','halves':halves,'matching_halves':matching,'orders':len(cases),'nodes':nodes,'found':found,'cases':cases}
(P/'frontier-20261028-isolated-a8a-product-certificate-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in obj.items()if k!='cases'},indent=2))
