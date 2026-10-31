#!/usr/bin/env python3
"""Exact monomial invariants of the cited explicit T8B matrix."""
import collections,datetime,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-t8b-original-vector-replay-v1.py';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f3a8a629b868105a2080001095a2800a4ba8471f8f816d85ea1e2ca8fc3daba7'
exec(compile(raw.decode().split('cells=list(itertools.product',1)[0],str(src),'exec'),globals())
assert add(d,cj(d))==scale(ONE,F(13,7));assert K[0][0]==K[0][2]==K[1][0]==ONE and K[1][2]==neg(d)
edges=[];hist=collections.Counter()
for r,s in itertools.combinations(range(8),2):
 values=[mul(K[r][c],cj(K[s][c]))for c in range(8)];counts=collections.Counter(values)
 hist[len(counts)]+=1
 if len(counts)==2 and sorted(counts.values())==[4,4]:
  u,v=counts
  if u==neg(v):edges.append([r,s])
assert not edges
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'd_plus_conjugate':'13/7','two_by_two_crossratio':'-d',
 'row_pair_count':28,'distinct_ratio_histogram':dict(hist),'dita_2x4_necessary_row_pairs':edges,
 'status':'PASS'}
(P/'frontier-20261028-t8b-structural-invariants-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
