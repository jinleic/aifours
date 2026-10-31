#!/usr/bin/env python3
"""Exact 5+5 ratio pairs of the independently reconstructed BH10,6 seed."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-y10-nonaffine-seed-replay-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ab66766b4362d5c479141ea1f9290c8b52c777d67cb84f91fb51eb4dae05e390';E=json.loads(raw)['exponent_matrix'];row=[];col=[]
for i,j in itertools.combinations(range(10),2):
 a=collections.Counter((E[j][t]-E[i][t])%6 for t in range(10));b=collections.Counter((E[t][j]-E[t][i])%6 for t in range(10))
 if sorted(a.values())==[5,5]:row.append([i,j])
 if sorted(b.values())==[5,5]:col.append([i,j])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'row_5plus5_pairs':row,'col_5plus5_pairs':col,'status':'PASS'}
(P/'frontier-20261028-y10-seed-dita-ratios-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
