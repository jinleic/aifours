#!/usr/bin/env python3
"""Independent dynamic-MRV transversal generation and Algorithm X exact cover."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-weisner-mates-independent-replay-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='3dc426dc8a1cacf46f18a9359eeb0eaa883ef252622f1ebdc771dc28bc5dea74'
# Prefix independently retranscribes, validates, enumerates L-transversals and DSU pair data.
g={'__file__':str(src)};exec(compile(raw.decode().split("source=P/'frontier-20261029-weisner-all-mates-trade-census-v1.json'",1)[0],str(src),'exec'),g)
T=g['T'];L=g['L'];masks=g['masks'];full=(1<<100)-1
contain=[[]for _ in range(100)]
for i,t in enumerate(T):
 for r,c in enumerate(t):contain[10*r+c].append(i)
solutions=[];nodes=0
def search(used,chosen):
 global nodes
 nodes+=1
 if used==full:solutions.append(tuple(chosen));return
 remaining=full^used;best=None;opts=None
 while remaining:
  bit=remaining&-remaining;remaining-=bit;x=bit.bit_length()-1
  cand=[i for i in contain[x]if not(masks[i]&used)]
  if opts is None or len(cand)<len(opts):best=x;opts=cand
  if not opts:break
 for i in opts:search(used|masks[i],chosen+[i])
search(0,[])
def square(ids):
 A=[[-1]*10 for _ in range(10)]
 for i in ids:
  color=T[i][0]
  for r,c in enumerate(T[i]):assert A[r][c]==-1;A[r][c]=color
 assert A[0]==list(range(10))
 assert all(set(row)==set(range(10))for row in A) and all({A[r][c]for r in range(10)}==set(range(10))for c in range(10))
 assert len({(A[r][c],L[r][c])for r in range(10)for c in range(10)})==100
 return A
mates=sorted(square(ids)for ids in solutions);assert len(mates)==len({tuple(sum(m,[]))for m in mates})
source=P/'frontier-20261029-weisner-all-classical-mates-v1.json';raw2=source.read_bytes();d=json.loads(raw2);assert mates==d['mates']
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'independent_L_transversal_source_sha256':hashlib.sha256(raw).hexdigest(),
 'producer_sha256':hashlib.sha256(raw2).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'transversals':len(T),'algorithm_x_nodes':nodes,'normalized_classical_mates':len(mates),'all_literal_mates_match':True,'status':'PASS'}
(P/'frontier-20261029-weisner-all-mates-algorithmx-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
