#!/usr/bin/env python3
"""Exact integer-arc filter on the 40 conditional cyclic spectra."""
import collections,datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-40-residual-spectra-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='dd178c5ee25f214b97d843adbe5ed1fe93a0b8eccacb738fb09f1644ddc5a153';D=json.loads(raw)
def gap(S,d):
 E=sorted((d*a)%15 for a in S);return max((E[(j+1)%len(E)]-E[j])%15 for j in range(len(E)))
removed=[];remaining=[]
for rec in D['remaining_spectrum_classes']:
 S=tuple(rec['representative']);g2,g7=gap(S,2),gap(S,7)
 item={**rec,'gap_d2':g2,'gap_d7':g7}
 if max(g2,g7)>=8:removed.append(item)
 else:remaining.append(item)
assert len(removed)==8 and len(remaining)==32
cnt=collections.Counter(tuple(x['U5_multiplicities'])for x in remaining);assert cnt=={(1,2,3):26,(2,2,2):6}
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'excluded_count':len(removed),'remaining_count':len(remaining),
 'remaining_multiplicities':{str(k):v for k,v in cnt.items()},'excluded':removed,'remaining':remaining,
 'scope':'necessary numerical-range spectral filter; surviving Gram equations unsolved','status':'PASS'}
(P/'frontier-20261029-cyclic15-semicircle-filter-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ('excluded','remaining')},indent=2))
