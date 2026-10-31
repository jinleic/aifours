#!/usr/bin/env python3
"""Audit literal cells underlying every compatible Parker trade triangle."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-parker-trade-dsu-replay-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='6446901b2381b956a76407630c0b5341650e6f41ced9cc23ed8caa6696b84fef'
d=json.loads(raw);T=d['T'];edges={(x['a'],x['b']):x['components']for x in d['trades']};neighbors=collections.defaultdict(set)
for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
tri=[]
for a in sorted(neighbors):
 for b in sorted(x for x in neighbors[a]if x>a):
  for c in sorted(x for x in neighbors[a]&neighbors[b]if x>b):
   ids=(a,b,c)
   if any(any(T[x][r]==T[y][r]for r in range(10))for x,y in itertools.combinations(ids,2)):continue
   tri.append(ids)
   assert all(edges[x][0]==[7,8,9] for x in itertools.combinations(ids,2))
   assert all({T[x][r]for r in (7,8,9)}=={7,8,9} for x in ids)
assert len(tri)==24
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'triangles':len(tri),'short_component_rows':[7,8,9],
 'short_component_cols':[7,8,9],'scope':'Only compatible triples of switched color transversals, not all 1RQLS with this L.','status':'PASS'}
(P/'frontier-20261029-parker-trade-triangle-structure-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
