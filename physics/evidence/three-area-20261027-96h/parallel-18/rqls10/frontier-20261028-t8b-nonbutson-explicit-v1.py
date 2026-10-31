#!/usr/bin/env python3
"""Exact original-vector check for a concrete non-Butson T8B family point.

s=zeta6, s^2=s-1; d=(5+3s)/7. All Gram/ray checks are rational in the
independent tensor basis Q(zeta8) tensor Q(zeta3); no float or search proxy.
"""
import datetime,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;one=(F(1),F(0));zero=(F(0),F(0));s=(F(0),F(1));d=(F(5,7),F(3,7))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def cj(a):return(a[0]+a[1],-a[1])
def suma(seq):
 v=zero
 for x in seq:v=add(v,x)
 return v
a=b=c=s;ab=mul(a,b);ac=mul(a,c);bc=mul(b,c);ad=mul(a,d);bd=mul(b,d);cd=mul(c,d);abcd=mul(ab,cd)
K=[[one,one,one,one,one,one,one,one],[one,neg(one),neg(d),neg(c),d,c,cd,neg(cd)],[one,neg(a),neg(one),c,a,neg(ac),neg(c),ac],[one,a,d,neg(one),ad,neg(a),neg(d),neg(ad)],[one,b,neg(b),neg(bc),neg(one),neg(c),c,bc],[one,neg(b),bd,b,neg(d),neg(one),d,neg(bd)],[one,neg(ab),b,neg(b),neg(a),a,neg(one),ab],[one,ab,neg(bd),bc,neg(ad),ac,neg(cd),neg(abcd)]]
assert all(mul(cj(K[t][c]),K[t][c])==one for t in range(8)for c in range(8))
assert all(suma(mul(cj(K[t][c]),K[t][e])for t in range(8))==zero for c,e in itertools.combinations(range(8),2))
assert all(suma(mul(cj(K[r][t]),K[q][t])for t in range(8))==zero for r,q in itertools.combinations(range(8),2))
def embedding(k,v):
 k%=8;out=[zero]*4;out[k%4]=v if k<4 else neg(v);return tuple(out)
def grams(a,b):
 r,c=a;s,e=b;out=[zero]*4
 for t in range(8):
  z=embedding((s-r)*t,mul(cj(K[t][c]),K[t][e]));out=[add(x,y)for x,y in zip(out,z)]
 return tuple(out)
def same_ray(a,b):
 r,c=a;s,e=b
 return all(embedding((s-r)*t,K[t][e])==embedding(0,K[t][c])for t in range(8))
cells=list(itertools.product(range(8),repeat=2));orth={}
for a,b in itertools.combinations(cells,2):orth[a,b]=(grams(a,b)==(zero,)*4)
def O(a,b):return orth[a,b] if a<b else orth[b,a]
assert all(O((r,c),(r,e))for r in range(8)for c,e in itertools.combinations(range(8),2))
assert all(O((r,c),(q,c))for c in range(8)for r,q in itertools.combinations(range(8),2))
dups=[(a,b)for a,b in itertools.combinations(cells,2)if same_ray(a,b)];assert not dups
nodes=0;found=None
def dfs(path,used):
 global nodes,found
 nodes+=1;r=len(path)
 if r==8:found=path[:];return
 for c in range(8):
  if used>>c&1:continue
  if all(O((s,path[s]),(r,c))for s in range(r)):
   dfs(path+[c],used|1<<c)
   if found:return
dfs([0],1)
obj={'source':'https://arxiv.org/html/2505.22947v1 Proposition3.2 T8B',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'parameters':'a=b=c=zeta6; d=(5+3*zeta6)/7',
 'norms':64,'row_gram_pairs':224,'column_gram_pairs':224,'ray_pairs':2016,'duplicate_rays':len(dups),
 'transversal_DFS_nodes':nodes,'transversal_found':found,
 'field_note':'Q(zeta6) intersects Q(zeta8) in Q; Phi8 irreducible'}
(P/'frontier-20261028-t8b-nonbutson-explicit-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
