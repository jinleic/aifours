#!/usr/bin/env python3
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;A=P/'frontier-20261029-parker-all-mates-trade-census-v1.json';B=P/'frontier-20261029-parker-trade-dsu-replay-v1.json'
a=json.loads(A.read_bytes());b=json.loads(B.read_bytes())
assert a['T']==b['T'] and a['trades']==b['trades'] and a['transversals']==1272 and a['compatible_transversal_pairs']==311214
assert a['compatible_trade_pair_vertex_count']==b['compatible_trade_pair_vertex_count']=={'3':72} and a['compatible_trade_triangles']==b['compatible_trade_triangles']==24
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(A.read_bytes()).hexdigest(),
 'replay_sha256':hashlib.sha256(B.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'transversal_keys_matched':len(a['T']),'trade_keys_and_components_matched':len(a['trades']),'status':'PASS'}
(P/'frontier-20261029-parker-trade-coverage-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
