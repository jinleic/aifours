#!/usr/bin/env python3
"""Independent Y_10_3_278 slice, all252 halves in Z[zeta3] basis."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
E=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,4,4,1,1,3,3,3],[0,0,3,2,4,2,4,0,3,0],[0,0,3,4,2,4,2,0,0,3],[0,4,3,0,0,3,0,2,2,4],[0,2,5,2,2,2,5,4,0,4],[0,4,0,0,3,3,3,2,5,1],[0,2,2,5,2,5,5,4,3,1],[0,3,3,3,5,0,2,3,0,0],[0,3,0,2,0,5,3,0,3,3]]
X=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,-1,-1],[0,0,0,0,0,0,0,0,-1,-1],[0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,1]]
R=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def gram(seq):
 acc={}
 for i,j,k,l in seq:
  e=l-j;v=R[(k-i)%6];w=acc.get(e,(0,0));acc[e]=(w[0]+v[0],w[1]+v[1])
 return {k:v for k,v in acc.items()if v!=(0,0)}
for i,j in itertools.combinations(range(10),2):
 assert not gram((E[t][i],X[t][i],E[t][j],X[t][j])for t in range(10))
 assert not gram((E[i][t],X[i][t],E[j][t],X[j][t])for t in range(10))
def nm(a):return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
def tp(p):
 if not p:return 'free'
 if len(p)==1:return 'no'
 if len(p)==2:
  a,b=p.values();return 'binary' if nm(a)==nm(b) else 'no'
 return 'other'
def matching(V):
 if not V:yield ();return
 a=V[0]
 for i in range(1,len(V)):
  for t in matching(V[1:i]+V[i+1:]):yield ((a,V[i]),)+t
ALL=list(matching(list(range(10))));assert len(ALL)==945
out=P/'frontier-20261028-y10-seed-slice-independent-v1.jsonl';counts=collections.Counter();eligible=0
with out.open('w') as f:
 for I in itertools.combinations(range(10),5):
  polys={(i,j):gram((E[t][i],X[t][i],E[t][j],X[t][j])for t in I)for i,j in itertools.combinations(range(10),2)};kind={e:tp(p)for e,p in polys.items()};n=0
  for m in ALL:
   if any(kind[e]=='no'for e in m):continue
   n+=1;w=next((e for e in m if kind[e]=='binary' and max(polys[e])-min(polys[e])==1),None)
   status='c_in_Qzeta6' if w else 'UNRESOLVED';counts[status]+=1
   f.write(json.dumps({'E':I,'matching':m,'status':status,'witness_edge':w},separators=(',',':'))+'\n')
  eligible+=bool(n)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'symbolic_row_col_grams':90,'halves':252,'eligible_halves':eligible,
 'counts':dict(counts),'status':'PASS' if not counts['UNRESOLVED'] else 'UNRESOLVED'}
(P/'frontier-20261028-y10-seed-slice-independent-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
