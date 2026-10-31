#!/usr/bin/env python3
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;A=P/'frontier-20261028-y10-seed-slice-halfgraph-v1.jsonl';B=P/'frontier-20261028-y10-seed-slice-independent-v1.jsonl'
a=[json.loads(x)for x in A.read_text().splitlines()];b=[json.loads(x)for x in B.read_text().splitlines()];b=[x for x in b if 0 in x['E']]
def key(x):return(tuple(x['E']),tuple(tuple(p)for p in x['matching']))
C={key(x):(x['status'],tuple(x['witness_edge']))for x in a};D={key(x):(x['status'],tuple(x['witness_edge']))for x in b}
assert len(C)==len(a)==len(D)==len(b)==520 and C==D
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_stream_sha256':hashlib.sha256(A.read_bytes()).hexdigest(),
 'replay_stream_sha256':hashlib.sha256(B.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'keys_compared':len(C),'witnesses_match':True,'status':'PASS'}
(P/'frontier-20261028-y10-seed-slice-coverage-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
