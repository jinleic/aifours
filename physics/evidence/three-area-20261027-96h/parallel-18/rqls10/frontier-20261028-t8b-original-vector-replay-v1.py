#!/usr/bin/env python3
"""Independent original-vector replay in Q[zeta24]/(x^8-x^4+1).

No tensor basis, no source-producer inputs; separately transcribes T8B point.
"""
import datetime,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;Z=(F(0),)*8;ONE=(F(1),)+(F(0),)*7
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(a,s):return tuple(x*s for x in a)
def mul(a,b):
 z=[F(0)]*15
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 for k in range(14,7,-1):z[k-4]+=z[k];z[k-8]-=z[k]
 return tuple(z[:8])
rts=[];v=ONE
for j in range(24):
 rts.append(v);q=v[7];v=(-q,v[0],v[1],v[2],v[3]+q,v[4],v[5],v[6])
assert v==ONE
def cj(a):
 v=Z
 for i,x in enumerate(a):v=add(v,scale(rts[-i%24],x))
 return v
s=rts[4];d=scale(add(scale(ONE,5),scale(s,3)),F(1,7));a=b=c=s
ab=mul(a,b);ac=mul(a,c);bc=mul(b,c);ad=mul(a,d);bd=mul(b,d);cd=mul(c,d);abcd=mul(ab,cd)
K=[[ONE,ONE,ONE,ONE,ONE,ONE,ONE,ONE],[ONE,neg(ONE),neg(d),neg(c),d,c,cd,neg(cd)],[ONE,neg(a),neg(ONE),c,a,neg(ac),neg(c),ac],[ONE,a,d,neg(ONE),ad,neg(a),neg(d),neg(ad)],[ONE,b,neg(b),neg(bc),neg(ONE),neg(c),c,bc],[ONE,neg(b),bd,b,neg(d),neg(ONE),d,neg(bd)],[ONE,neg(ab),b,neg(b),neg(a),a,neg(ONE),ab],[ONE,ab,neg(bd),bc,neg(ad),ac,neg(cd),neg(abcd)]]
def vec(r,c):return [mul(rts[(3*r*t)%24],K[t][c])for t in range(8)]
cells=list(itertools.product(range(8),repeat=2));V={a:vec(*a)for a in cells}
def gram(a,b):
 v=Z
 for x,y in zip(V[a],V[b]):v=add(v,mul(cj(x),y))
 return v
assert all(gram(a,a)==scale(ONE,8)for a in cells)
assert all(gram((r,c),(r,d))==Z for r in range(8)for c,d in itertools.combinations(range(8),2))
assert all(gram((r,c),(s,c))==Z for c in range(8)for r,s in itertools.combinations(range(8),2))
dup=[];orth={}
for a,b in itertools.combinations(cells,2):
 if V[a]==V[b]:dup.append((a,b))
 orth[a,b]=(gram(a,b)==Z)
assert not dup
def good(a,b):return orth[a,b] if a<b else orth[b,a]
nodes=0;found=None
def dfs(path,used):
 global nodes,found
 nodes+=1;r=len(path)
 if r==8:found=path[:];return
 for c in range(8):
  if not (used>>c)&1 and all(good((j,path[j]),(r,c))for j in range(r)):
   dfs(path+[c],used|1<<c)
   if found:return
dfs([0],1)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'field':'Q[zeta24]/(x^8-x^4+1)','norms':64,'row_gram_pairs':224,'column_gram_pairs':224,
 'ray_pairs':2016,'duplicate_rays':len(dup),'transversal_DFS_nodes':nodes,'transversal_found':found,'status':'PASS'}
(P/'frontier-20261028-t8b-original-vector-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
