#!/usr/bin/env python3
"""Exact phase-polynomial halfgraph census for Szollosi's D10^(3)."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
S=[
 [1,1,1,1,1,1,1,1,1,1],
 [1,-1,-1j,-1j,-1j,-1j,1j,1j,1j,1j],
 [1,-1j,-1,1j,1j,-1j,-1j,-1j,1j,1j],
 [1,-1j,1j,-1,-1j,1j,-1j,1j,-1j,1j],
 [1,-1j,1j,-1j,-1,1j,1j,-1j,1j,-1j],
 [1,-1j,-1j,1j,1j,-1,1j,1j,-1j,-1j],
 [1,1j,-1j,-1j,1j,1j,-1,-1j,-1j,1j],
 [1,1j,-1j,1j,-1j,1j,-1j,-1,1j,-1j],
 [1,1j,1j,-1j,1j,-1j,-1j,1j,-1,-1j],
 [1,1j,1j,1j,-1j,-1j,1j,-1j,-1j,-1]]
o=(0,0,0);A=(1,0,0);B=(0,1,0);C=(0,0,1);AB=(1,-1,0);BA=(-1,1,0);na=(-1,0,0);nb=(0,-1,0);nc=(0,0,-1)
R=[
 [o,o,o,o,o,o,o,o,o,o],
 [o,o,AB,A,nc,o,nc,A,AB,o],
 [o,BA,o,B,nc,o,nc,B,o,BA],
 [o,na,nb,o,o,o,o,o,nb,na],
 [o,C,C,o,o,o,o,o,C,C],
 [o,o,o,o,o,o,o,o,o,o],
 [o,C,C,o,o,o,o,o,C,C],
 [o,na,nb,o,o,o,o,o,nb,na],
 [o,BA,o,B,nc,o,nc,B,o,BA],
 [o,o,AB,A,nc,o,nc,A,AB,o]]
E={1:0,1j:1,-1:2,-1j:3};K=[[(E[S[i][j]],)+R[i][j] for j in range(10)]for i in range(10)]
Z=(0,0);roots=[(1,0),(0,1),(-1,0),(0,-1)]
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def norm(a):return a[0]**2+a[1]**2
def poly(pairs):
 out={}
 for x,y in pairs:
  k=tuple(y[i]-x[i]for i in range(1,4));out[k]=add(out.get(k,Z),roots[(y[0]-x[0])%4])
 return {k:v for k,v in out.items()if v!=Z}
for i,j in itertools.combinations(range(10),2):
 assert not poly((K[t][i],K[t][j])for t in range(10))
 assert not poly((K[i][t],K[j][t])for t in range(10))
def typ(p):
 if not p:return 'free'
 if len(p)==1:return 'impossible'
 if len(p)>2:return 'multi'
 a,b=p.values();return 'binary' if norm(a)==norm(b) else 'impossible'
def eq(p):
 (a,x),(b,y)=sorted(p.items());e=tuple(y[i]-a[i]for i in range(3));n=neg(x);d=y
 if next(z for z in e if z)!=abs(next(z for z in e if z)):e=tuple(-z for z in e);n,d=d,n
 return e,n,d
def rank_info(v):
 if not v:return (0,None)
 for a,b,c in itertools.combinations(v,3):
  D=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
  if D:return (3,abs(D))
 for a,b in itertools.combinations(v,2):
  if any(a[i]*b[j]!=a[j]*b[i]for i in range(3)for j in range(i+1,3)):return (2,None)
 return (1,None)
def matching(mask,adj,L):
 if not mask:yield tuple(L);return
 x=(mask&-mask).bit_length()-1
 for y in range(x+1,10):
  if mask>>y&1 and adj[x][y]!='impossible':yield from matching(mask&~(1<<x)&~(1<<y),adj,L+[(x,y)])
counts=collections.Counter();profiles=collections.Counter();halves=matchinghalves=0;out=P/'frontier-20261028-n10-d10-affine-halfgraph-v1.jsonl'
with out.open('w') as fp:
 for subset in itertools.combinations(range(1,10),4):
  halves+=1;E=(0,)+subset;ps={(i,j):poly((K[t][i],K[t][j])for t in E)for i,j in itertools.combinations(range(10),2)};ts={e:typ(x)for e,x in ps.items()};adj=[['']*10 for _ in range(10)]
  for(i,j),x in ts.items():adj[i][j]=adj[j][i]=x
  ms=list(matching((1<<10)-1,adj,[]));matchinghalves+=bool(ms)
  for m in ms:
   seen={};bad=False;multi=[]
   for e in m:
    if ts[e]=='multi':multi.append(e)
    if ts[e]=='binary':
     d,n,v=eq(ps[e])
     if d in seen and mul(n,seen[d][1])!=mul(seen[d][0],v):bad=True
     seen[d]=(n,v)
   rank,minor=rank_info(list(seen));status='inconsistent' if bad else 'unresolved';counts[status]+=1
   if not bad:profiles[(rank,minor,len(multi),tuple(sorted(seen)))]+=1
   fp.write(json.dumps({'E':E,'matching':m,'inconsistent':bad,'rank':rank,'minor':minor,'exponents':list(seen),'multi':multi},separators=(',',':'))+'\n')
obj={'source':'https://arxiv.org/html/math/0610297v1#S4 D10 and D10^(3)',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'90_symbolic_grams':True,'halves':halves,'matching_halves':matchinghalves,
 'counts':dict(counts),'remaining_profiles':{str(k):v for k,v in profiles.items()},'scope':'unresolved means no phase conclusion yet'}
(P/'frontier-20261028-n10-d10-affine-halfgraph-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
