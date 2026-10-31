#!/usr/bin/env python3
"""Independent original 10-vector replay in Z[zeta20]/Phi20."""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(0,)*8;ONE=(1,0,0,0,0,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,b):
 c=[0]*15
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 for k in range(14,7,-1):
  q=c[k];c[k-8]-=q;c[k-6]+=q;c[k-4]-=q;c[k-2]+=q
 return tuple(c[:8])
roots=[ONE]
for _ in range(19):
 a=roots[-1];q=a[7];roots.append((-q,a[0],a[1]+q,a[2],a[3]-q,a[4],a[5]+q,a[6]))
def conj(a):
 out=Z
 for i,x in enumerate(a):out=add(out,tuple(x*y for y in roots[-i%20]))
 return out
def sm(xs):
 out=Z
 for x in xs:out=add(out,x)
 return out
E=add((3,0,0,0,0,0,0,0),tuple(4*x for x in roots[5]));F=(5,0,0,0,0,0,0,0);sigma=(0,1,3,2,4)
def vec(row,col):
 a,r=divmod(row,5);b,c=divmod(col,5);s=a^b;out=[Z]*10
 for t in range(5):out[5*s+t]=mul(E if a==1 and t==0 else F,roots[4*((r*t+c*sigma[t])%5)])
 return out
Q=[[vec(r,c)for c in range(10)]for r in range(10)]
for r,c in itertools.product(range(10),repeat=2):assert sm(mul(conj(x),x)for x in Q[r][c])==(125,0,0,0,0,0,0,0)
for i,j in itertools.combinations(range(10),2):
 for k in range(10):
  assert sm(mul(conj(x),y)for x,y in zip(Q[k][i],Q[k][j]))==Z
  assert sm(mul(conj(x),y)for x,y in zip(Q[i][k],Q[j][k]))==Z
cells=list(itertools.product(range(10),repeat=2));paircount=0
for (r,c),(s,d) in itertools.combinations(cells,2):
 paircount+=1;u,v=Q[r][c],Q[s][d];su=(r//5)^(c//5);sv=(s//5)^(d//5)
 if su!=sv:continue
 z=5*su;assert any(mul(u[z],v[z+t])!=mul(v[z],u[z+t])for t in range(1,5))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'ring':'Z[zeta20], Phi20=x^8-x^6+x^4-x^2+1','vector_norms':100,'row_gram_pairs':450,'column_gram_pairs':450,
 'ray_pairs_distinct':paircount,'rays':100,'status':'PASS'}
(P/'frontier-20261029-sector-maximal-example-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
