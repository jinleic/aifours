#!/usr/bin/env python3
"""Finite group check on the complete source8 exact-transversal census."""
import collections,datetime,hashlib,json,math
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-source8-cyclic-resolution-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='0e2f088f08144bae4a52388084c4e8fb0f98177e89ea24f3aa605c1b37212bf8'
T=[tuple(t) for t in json.loads(raw)['complete_column_per_row_list']];G=set(T);assert len(G)==16 and tuple(range(8)) in G
compose=lambda a,b:tuple(a[b[i]] for i in range(8))
assert all(compose(a,b) in G for a in G for b in G)
def typ(p):
 seen=set();L=[]
 for i in range(8):
  if i not in seen:
   j=i;n=0
   while j not in seen:seen.add(j);j=p[j];n+=1
   L.append(n)
 return tuple(sorted(L,reverse=True))
C=collections.Counter(typ(p) for p in G);orders=collections.Counter(math.lcm(*typ(p)) for p in G)
assert max(orders)==4
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'census_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'group_size':len(G),'closure_checks':len(G)**2,'cycle_type_counts':{str(k):v for k,v in sorted(C.items())},
 'element_order_counts':dict(sorted(orders.items())),'maximum_element_order':4}
(P/'frontier-20261028-source8-transversal-group-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
