#!/usr/bin/env python3
"""Independent source-basis comparison of all T8B column-ratio multiplicities."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
paths=[P/'frontier-20261028-t8b-nonbutson-explicit-v1.py',P/'frontier-20261028-t8b-original-vector-replay-v1.py']
expected=['6ce6e5df6b6a7901d8822971dffdc1d05c17cc05dbb5f2687664cf568701b0cd','f3a8a629b868105a2080001095a2800a4ba8471f8f816d85ea1e2ca8fc3daba7'];patterns=[]
for path,sha in zip(paths,expected):
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 n={'__file__':str(path)};exec(compile(raw.decode().split('cells=list(itertools.product',1)[0],str(path),'exec'),n)
 K=n['K'];mu=n['mul'];cj=n['cj'];out=[]
 for c,d in itertools.combinations(range(8),2):
  v=collections.Counter(mu(cj(K[t][c]),K[t][d])for t in range(8));shape=tuple(sorted(v.values()));assert any(k%2 for k in shape);out.append(shape)
 patterns.append(out)
assert patterns[0]==patterns[1]
hist=collections.Counter(patterns[0])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_checker_sha256':expected,'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'column_pairs':28,'pattern_histogram':{str(k):v for k,v in sorted(hist.items())},
 'every_pair_has_odd_multiplicity':True,'bases_agree':True,'status':'PASS'}
(P/'frontier-20261028-t8b-column-ratio-parity-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
