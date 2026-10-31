#!/usr/bin/env python3
"""Compare every producer half/matching classification to the independent replay."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
A=P/'frontier-20261028-n10-a30-phase-elimination-v1.jsonl';B=P/'frontier-20261028-n10-a30-phase-independent-v1.jsonl'
a=[json.loads(x)for x in A.read_text().splitlines()];b=[json.loads(x)for x in B.read_text().splitlines()];b=[x for x in b if 0 in x['E']]
def key(x):return (tuple(x['E']),tuple(tuple(p)for p in x['matching']))
C={key(x):x['status']for x in a};D={key(x):x['status']for x in b}
assert len(C)==len(a)==len(D)==len(b)==1152 and C==D and 'UNRESOLVED' not in C.values()
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_stream_sha256':hashlib.sha256(A.read_bytes()).hexdigest(),
 'replay_stream_sha256':hashlib.sha256(B.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'keys_compared':len(C),'identical_classification':True,'status':'PASS'}
(P/'frontier-20261028-n10-a30-coverage-comparison-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
