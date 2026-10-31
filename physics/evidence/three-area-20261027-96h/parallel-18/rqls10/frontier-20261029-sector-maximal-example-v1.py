#!/usr/bin/env python3
"""Original 10-vector exact checks in Z[zeta5,i] for the 100-ray sector QLS."""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(0,)*8;ONE=(1,0,0,0,0,0,0,0);I=(0,0,0,0,1,0,0,0);FIVE=(5,0,0,0,0,0,0,0)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def m5(x,y):
 v=[0]*7
 for i,a in enumerate(x):
  for j,b in enumerate(y):v[i+j]+=a*b
 for k in range(6,3,-1):
  a=v[k]
  for j in range(1,5):v[k-j]-=a
 return tuple(v[:4])
def mul(x,y):
 a,b=x[:4],x[4:];c,d=y[:4],y[4:];ac=m5(a,c);bd=m5(b,d);ad=m5(a,d);bc=m5(b,c)
 return tuple(ac[i]-bd[i]for i in range(4))+tuple(ad[i]+bc[i]for i in range(4))
def root(k):
 k%=5
 if k==4:return (-1,-1,-1,-1,0,0,0,0)
 return tuple(int(i==k)for i in range(8))
def conj(x):
 out=Z
 for i in range(4):
  z=root(-i);coeff=(x[i],0,0,0,-x[i+4],0,0,0);out=add(out,mul(coeff,z))
 return out
def sm(xs):
 q=Z
 for x in xs:q=add(q,x)
 return q
eta5=add((3,0,0,0,0,0,0,0),tuple(4*x for x in I));sigma=[0,1,3,2,4]
def cell(a,r,b,c):
 q=[Z]*10;s=a^b
 for t in range(5):
  phase=root(r*t+c*sigma[t]);scale=eta5 if a and t==0 else FIVE;q[5*s+t]=mul(scale,phase)
 return tuple(q)
K={(a,r,b,c):cell(a,r,b,c)for a,r,b,c in itertools.product(range(2),range(5),range(2),range(5))}
N=(125,0,0,0,0,0,0,0)
for v in K.values():assert sm(mul(conj(x),x)for x in v)==N
for a,r in itertools.product(range(2),range(5)):
 for (b,c),(d,e)in itertools.combinations(itertools.product(range(2),range(5)),2):
  assert sm(mul(conj(x),y)for x,y in zip(K[a,r,b,c],K[a,r,d,e]))==Z
for b,c in itertools.product(range(2),range(5)):
 for (a,r),(d,e)in itertools.combinations(itertools.product(range(2),range(5)),2):
  assert sm(mul(conj(x),y)for x,y in zip(K[a,r,b,c],K[d,e,b,c]))==Z
pairs=0
for x,y in itertools.combinations(K,2):
 pairs+=1;v,w=K[x],K[y];s=x[0]^x[2]
 if s!=y[0]^y[2]:continue
 t=5*s;assert any(mul(v[t],w[t+j])!=mul(w[t],v[t+j])for j in range(1,5))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'ring':'Z[zeta5,i], zeta5^4+zeta5^3+zeta5^2+zeta5+1=0','sigma':sigma,'eta':'(3+4i)/5',
 'vector_norms':100,'row_gram_pairs':450,'column_gram_pairs':450,'ray_pairs_distinct':pairs,'rays':100,'status':'PASS'}
(P/'frontier-20261029-sector-maximal-example-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
