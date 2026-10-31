#!/usr/bin/env python3
"""Exact all-transversal / all 8-cycle census of the pinned primary QLS8.

Reuse only the pinned exact source parser/check prefix, never its output write.
No 8-cycle orbit of transversals means no resolution isotopic to Z8 addition.
"""
import hashlib,itertools,json,datetime
from pathlib import Path
P=Path(__file__).resolve().parent
base=P/'frontier-20261028-source8-covariance-check-v1.py'
raw=base.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='504e7521ec91d932f8f29adf3711ad76c8a85d5d3d184a4779903c7eb2c8ec9f'
code=raw.decode().split('\nobj={',1)[0]
exec(compile(code,str(base),'exec'),globals())
O={(r,c,s,d):gram(V[r][c],V[s][d])==Z for r in range(8)for s in range(r+1,8)for c in range(8)for d in range(8)}
T=[]
def dfs(path,used):
 r=len(path)
 if r==8:T.append(tuple(path));return
 for c in range(8):
  if (used>>c)&1:continue
  if all(O[(s,path[s],r,c)] for s in range(r)):dfs(path+[c],used|(1<<c))
dfs([],0);Tset=set(T);cycles=0;orbits=[];membership_tests=0
for p in itertools.permutations(range(1,8)):
 seq=(0,)+p;S=[0]*8
 for i in range(8):S[seq[i]]=seq[(i+1)%8]
 cycles+=1
 for t in T:
  cur=t
  for k in range(1,8):
   nxt=[0]*8
   for r in range(8):nxt[S[r]]=cur[r]
   cur=tuple(nxt);membership_tests+=1
   if cur not in Tset:break
  else:orbits.append({'row_cycle':S,'starting_transversal':t})
obj={'source_fragment_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'parser_sha256':hashlib.sha256(raw).hexdigest(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'transversal_count':len(T),'complete_column_per_row_list':T,'row_cycles':cycles,
 'membership_tests':membership_tests,'cyclic_resolutions':orbits}
(P/'frontier-20261028-source8-cyclic-resolution-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
