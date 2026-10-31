#!/usr/bin/env python3
"""Exact per-order comparison of independently generated local clique counts."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;a=P/'frontier-20261028-t8b-all-row-orders-tensor-parity-v3.jsonl';b=P/'frontier-20261028-t8b-all-row-orders-clique-replay-v1.jsonl'
A=[json.loads(x)for x in a.read_text().splitlines()];B=[json.loads(x)for x in b.read_text().splitlines()];assert len(A)==len(B)==5040
for x,y in zip(A,B):assert x['O']==y['O'] and x['cliques']==y['cliques'] and y['bad']==0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'producer_stream_sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'replay_stream_sha256':hashlib.sha256(b.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'orders_compared':len(A),'bad_congruences':0,'status':'PASS'}
(P/'frontier-20261028-t8b-all-row-orders-coverage-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
