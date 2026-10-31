#!/usr/bin/env python3
"""Each possible D10^(3) halfgraph matching forces all three phases into mu24."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-n10-d10-affine-halfgraph-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='86d2bfe9eef2eb0dfacdba177d412afd55f4c80a788ae193e2b367f02f6edfcd'
g={'__file__':str(src)};exec(compile(raw.decode().split('counts=collections.Counter()',1)[0],str(src),'exec'),g)
K=g['K'];poly=g['poly'];typ=g['typ'];matching=g['matching'];mul=g['mul'];unit={(1,0),(0,1),(-1,0),(0,-1)}
def rootquot(a,b):return any(mul(x,b)==a for x in unit)
def vectors(p,edge):
 it=sorted(p.items())
 if len(it)!=3 or not all(rootquot(c,it[0][1])for _,c in it[1:]):return []
 base=it[0][0];return [(tuple(it[j][0][i]-base[i]for i in range(3)),edge,j)for j in (1,2)]
def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
counts=collections.Counter();out=P/'frontier-20261028-n10-d10-cube-rigidity-v1.jsonl';halves=eligible=0
with out.open('w') as fp:
 for sub in itertools.combinations(range(1,10),4):
  halves+=1;E=(0,)+sub;ps={(i,j):poly((K[t][i],K[t][j])for t in E)for i,j in itertools.combinations(range(10),2)};ts={e:typ(x)for e,x in ps.items()};adj=[['']*10 for _ in range(10)]
  for (i,j),x in ts.items():adj[i][j]=adj[j][i]=x
  ms=list(matching((1<<10)-1,adj,[]));eligible+=bool(ms)
  for ma in ms:
   v=[x for edge in ma for x in vectors(ps[edge],edge)];chosen=None
   for tri in itertools.combinations(v,3):
    d=abs(det(*(x[0]for x in tri)))
    if d and d%5:chosen=(d,tri);break
   if not chosen:status='UNRESOLVED';witness=None
   else:
    d,tri=chosen;status='rigid';counts[str(d)]+=1;witness={'abs_determinant':d,'exponent_vectors':[x[0]for x in tri],'source_edges':[x[1]for x in tri]}
   if not chosen:counts['UNRESOLVED']+=1
   fp.write(json.dumps({'E':E,'matching':ma,'status':status,'witness':witness},separators=(',',':'))+'\n')
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'symbolic_input_sha256':hashlib.sha256(raw).hexdigest(),
 'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'halves':halves,'eligible_halves':eligible,'counts':dict(counts),'status':'PASS' if not counts['UNRESOLVED'] else 'UNRESOLVED'}
(P/'frontier-20261028-n10-d10-cube-rigidity-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
