#!/usr/bin/env python3
"""Exact all-c halfgraph certificate on Y_10_3_278 seed slice."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-y10-nonaffine-seed-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='3cc8a22262c7766ff74375b3042e35acd563a02668a3c7b9c13b0cf6804457eb'
E=json.loads(raw)['exponent_matrix'];X=[[0]*10 for _ in range(10)]
for r in (2,3):
 for c in (8,9):X[r][c]=-1
for r in (4,5):
 for c in (5,6):X[r][c]=1
for r in (6,7):
 for c in (3,4):X[r][c]=1
for r in (8,9):
 for c in range(2,10):X[r][c]=1
R=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def gram(entries):
 p={}
 for a,b in entries:
  k=b[1]-a[1];v=R[(b[0]-a[0])%6];old=p.get(k,(0,0));p[k]=(old[0]+v[0],old[1]+v[1])
 return {k:v for k,v in p.items()if v!=(0,0)}
def item(r,c):return E[r][c],X[r][c]
for i,j in itertools.combinations(range(10),2):
 assert not gram((item(t,i),item(t,j))for t in range(10))
 assert not gram((item(i,t),item(j,t))for t in range(10))
def norm(v):return v[0]**2+v[0]*v[1]+v[1]**2
def typ(p):
 if not p:return 'free'
 if len(p)==1:return 'impossible'
 if len(p)==2:
  a,b=p.values();return 'binomial' if norm(a)==norm(b) else 'impossible'
 return 'other'
def matches(mask,adj,L):
 if mask==0:yield tuple(L);return
 a=(mask&-mask).bit_length()-1
 for b in range(a+1,10):
  if mask>>b&1 and adj[a][b]!='impossible':yield from matches(mask&~(1<<a)&~(1<<b),adj,L+[(a,b)])
counts=collections.Counter();halves=eligible=0;out=P/'frontier-20261028-y10-seed-slice-halfgraph-v1.jsonl'
with out.open('w') as f:
 for sub in itertools.combinations(range(1,10),4):
  halves+=1;I=(0,)+sub;polys={(a,b):gram((item(t,a),item(t,b))for t in I)for a,b in itertools.combinations(range(10),2)};kinds={e:typ(p)for e,p in polys.items()};adj=[['']*10 for _ in range(10)]
  for(a,b),v in kinds.items():adj[a][b]=adj[b][a]=v
  ms=list(matches((1<<10)-1,adj,[]));eligible+=bool(ms)
  for ma in ms:
   witness=next((e for e in ma if kinds[e]=='binomial' and max(polys[e])-min(polys[e])==1),None)
   status='c_in_Qzeta6' if witness else 'UNRESOLVED';counts[status]+=1
   f.write(json.dumps({'E':I,'matching':ma,'status':status,'witness_edge':witness,'coefficients':polys[witness] if witness else None},separators=(',',':'))+'\n')
rowpairs=[];colpairs=[]
for a,b in itertools.combinations(range(10),2):
 Rr=collections.Counter(((E[b][t]-E[a][t])%6,X[b][t]-X[a][t])for t in range(10));Cc=collections.Counter(((E[t][b]-E[t][a])%6,X[t][b]-X[t][a])for t in range(10))
 if sorted(Rr.values())==[5,5]:rowpairs.append([a,b])
 if sorted(Cc.values())==[5,5]:colpairs.append([a,b])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256(raw).hexdigest(),
 'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'symbolic_row_col_grams':90,'halves':halves,'eligible_halves':eligible,'counts':dict(counts),
 'nonroot_c_row_5plus5_pairs':rowpairs,'nonroot_c_col_5plus5_pairs':colpairs,'status':'PASS' if not counts['UNRESOLVED'] else 'UNRESOLVED'}
(P/'frontier-20261028-y10-seed-slice-halfgraph-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
