#!/usr/bin/env python3
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;A=P/'frontier-20261028-n14-bjorck7-order-cliques-producer-v1.jsonl';B=P/'frontier-20261028-bjorck7-order-cliques-replay-v1.jsonl'
a=[json.loads(x)for x in A.read_text().splitlines()];b=[json.loads(x)for x in B.read_text().splitlines()]
assert len(a)==len(b)==720
for x,y in zip(a,b):assert all(x[k]==y[k]for k in ('order','cliques','rows','cols')) and y['other']==0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_stream_sha256':hashlib.sha256(A.read_bytes()).hexdigest(),
 'replay_stream_sha256':hashlib.sha256(B.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'orders_compared':len(a),'counts_match':True,'status':'PASS'}
(P/'frontier-20261028-bjorck7-order-clique-coverage-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
