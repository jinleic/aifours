#!/usr/bin/env python3
"""Integer-only checks for the cyclic15 rational-spectral reduction."""
import datetime,hashlib,itertools,json,math
from pathlib import Path
P=Path(__file__).resolve().parent
C3=[frozenset((a+5*j)%15 for j in range(3))for a in range(5)]
C5=[frozenset((a+3*j)%15 for j in range(5))for a in range(3)]
allcovered=[];threephase=[];fullorder=[]
for n in range(1,7):
 for tup in itertools.combinations(range(15),n):
  S=set(tup);pieces=[x for x in C3+C5 if x<=S];covered=set().union(*pieces)
  if covered!=S:continue
  allcovered.append(tup)
  if len({a%3 for a in S})<3:continue
  threephase.append(tup)
  if math.gcd(15,*[(a-tup[0])%15 for a in tup])!=1:continue
  fullorder.append(tup)
assert len(fullorder)==10 and all(any(set(a)|set(b)==set(S)for a,b in itertools.combinations(C3,2))for S in fullorder)
labels=[(2,0),(5,1),(7,2)];tables={}
for sigma in (1,-1):
 rows=[]
 for d,l in labels:
  e=(sigma*l+int(d==7))%3;rows.append({'d':d,'s':e,'t':(e-d)%3})
 tables[str(sigma)]=rows
assert [(x['s'],x['t'])for x in tables['1']]==[(0,1),(1,2),(0,2)]
assert [(x['s'],x['t'])for x in tables['-1']]==[(0,1),(2,0),(2,1)]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'supports_size_at_most_6_covered_by_C3_or_C5':len(allcovered),'covered_with_all_three_U5_eigenvalues':len(threephase),
 'covered_with_all_three_U5_eigenvalues_and_projective_order_15':len(fullorder),'full_order_supports':fullorder,
 'all_full_order_supports_two_C3_cosets':True,'row_exponent_tables':tables,'status':'PASS'}
(P/'frontier-20261029-cyclic15-rational-support-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
