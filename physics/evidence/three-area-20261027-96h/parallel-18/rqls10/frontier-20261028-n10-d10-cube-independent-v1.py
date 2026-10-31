#!/usr/bin/env python3
"""Independent D10^(3) 252-half, 945-matching cube-rigidity replay."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
# Literal source D10 as exponents of i; symbolic phase matrix transcribed separately.
S=[
 [0,0,0,0,0,0,0,0,0,0],
 [0,2,3,3,3,3,1,1,1,1],
 [0,3,2,1,1,3,3,3,1,1],
 [0,3,1,2,3,1,3,1,3,1],
 [0,3,1,3,2,1,1,3,1,3],
 [0,3,3,1,1,2,1,1,3,3],
 [0,1,3,3,1,1,2,3,3,1],
 [0,1,3,1,3,1,3,2,1,3],
 [0,1,1,3,1,3,3,1,2,3],
 [0,1,1,1,3,3,1,3,3,2]]
T=[
 ['.','.','.','.','.','.','.','.','.','.'],
 ['.','.','a-b','a','-c','.','-c','a','a-b','.'],
 ['.','-a+b','.','b','-c','.','-c','b','.','-a+b'],
 ['.','-a','-b','.','.','.','.','.','-b','-a'],
 ['.','c','c','.','.','.','.','.','c','c'],
 ['.','.','.','.','.','.','.','.','.','.'],
 ['.','c','c','.','.','.','.','.','c','c'],
 ['.','-a','-b','.','.','.','.','.','-b','-a'],
 ['.','-a+b','.','b','-c','.','-c','b','.','-a+b'],
 ['.','.','a-b','a','-c','.','-c','a','a-b','.']]
D={'.':(0,0,0),'a-b':(1,-1,0),'-a+b':(-1,1,0),'a':(1,0,0),'-a':(-1,0,0),'b':(0,1,0),'-b':(0,-1,0),'c':(0,0,1),'-c':(0,0,-1)}
K=[[(S[i][j],)+D[T[i][j]] for j in range(10)] for i in range(10)]
def gram(pairs):
 counts={}
 for x,y in pairs:
  exp=tuple(y[j]-x[j]for j in (1,2,3));h=(y[0]-x[0])%4;counts.setdefault(exp,[0]*4)[h]+=1
 return {exp:(a[0]-a[2],a[1]-a[3])for exp,a in counts.items()if a[0]!=a[2] or a[1]!=a[3]}
for i,j in itertools.combinations(range(10),2):
 assert not gram((K[t][i],K[t][j])for t in range(10))
 assert not gram((K[i][t],K[j][t])for t in range(10))
def possible(p):
 if not p:return True
 if len(p)==1:return False
 if len(p)==2:
  a,b=p.values();return a[0]*a[0]+a[1]*a[1]==b[0]*b[0]+b[1]*b[1]
 return True
def diffvec(p):
 E=sorted(p)
 if len(E)!=3:return []
 x=p[E[0]];orbit={x,(-x[1],x[0]),(-x[0],-x[1]),(x[1],-x[0])}
 if any(p[e] not in orbit for e in E[1:]):return []
 return [tuple(E[j][i]-E[0][i]for i in range(3))for j in (1,2)]
def det(v):
 a,b,c=v;return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def allmatch(V):
 if not V:yield ();return
 x=V[0]
 for i in range(1,len(V)):
  y=V[i]
  for m in allmatch(V[1:i]+V[i+1:]):yield ((x,y),)+m
MATCH=list(allmatch(list(range(10))));assert len(MATCH)==945
out=P/'frontier-20261028-n10-d10-cube-independent-v1.jsonl';counts=collections.Counter();eligible=0
with out.open('w') as fp:
 for E in itertools.combinations(range(10),5):
  p={(i,j):gram((K[t][i],K[t][j])for t in E)for i,j in itertools.combinations(range(10),2)};n=0
  for m in MATCH:
   if any(not possible(p[e])for e in m):continue
   n+=1;v=[z for e in m for z in diffvec(p[e])];d=next((abs(det(x))for x in itertools.combinations(v,3)if det(x) and det(x)%5),0)
   if d:counts[str(d)]+=1
   else:counts['UNRESOLVED']+=1
   fp.write(json.dumps({'E':E,'matching':m,'determinant':d},separators=(',',':'))+'\n')
  eligible+=bool(n)
# Generic formal ratio-pair incidence, before any parameter coincidences.
rr=[];cc=[]
for i,j in itertools.combinations(range(10),2):
 def ratio(items):return collections.Counter(((y[0]-x[0])%4,)+(tuple(y[k]-x[k]for k in (1,2,3)))for x,y in items)
 if sorted(ratio((K[i][t],K[j][t])for t in range(10)).values())==[5,5]:rr.append([i,j])
 if sorted(ratio((K[t][i],K[t][j])for t in range(10)).values())==[5,5]:cc.append([i,j])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'original_gram_pairs_checked':90,'halves':252,'eligible_halves':eligible,'counts':dict(counts),
 'generic_row_ratio_5plus5':rr,'generic_col_ratio_5plus5':cc,'status':'PASS' if not counts['UNRESOLVED'] else 'UNRESOLVED'}
(P/'frontier-20261028-n10-d10-cube-independent-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
