#!/usr/bin/env python3
"""Compare all source-pair order counts and the literal low-rank branch keys."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
names=['frontier-20261028-n10-dita-arbitrary-block-order-summary-producer-v1.jsonl','frontier-20261028-n10-dita-arbitrary-block-order-summary-replay-v1.jsonl','frontier-20261028-n10-dita-arbitrary-block-rank-scan-v2.jsonl','frontier-20261028-n10-dita-arbitrary-block-independent-v1.jsonl']
data=[[json.loads(x)for x in(P/n).read_text().splitlines()]for n in names]
def pairs(q):return (tuple(tuple(x)for x in q['pairs']),tuple(q['sigma']))
def key(q):return (pairs(q),tuple(q['f']),tuple(q['g']))
A={pairs(x):tuple(x[k]for k in ('f','fg','full','low'))for x in data[0]};B={pairs(x):tuple(x[k]for k in ('f','fg','full','low'))for x in data[1]}
assert len(A)==len(B)==len(data[0])==len(data[1])==136080 and A==B
C={key(x):x['rank31']for x in data[2]};D={key(x):x['rank41']for x in data[3]}
assert len(C)==len(D)==len(data[2])==len(data[3])==4000 and C==D and all(x['excluded']for x in data[3])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest()for n in names},
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'pairings_compared':len(A),'low_rank_keys_compared':len(C),'source_counts_match':True,'low_rank_keys_and_ranks_match':True,'all_replay_low_rank_excluded':True,'status':'PASS'}
(P/'frontier-20261028-n10-dita-arbitrary-block-coverage-comparison-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
