#!/usr/bin/env python3
"""Independent original 10x10 seed Gram replay in Z[zeta3]."""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
E=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,4,4,1,1,3,3,3],[0,0,3,2,4,2,4,0,3,0],[0,0,3,4,2,4,2,0,0,3],[0,4,3,0,0,3,0,2,2,4],[0,2,5,2,2,2,5,4,0,4],[0,4,0,0,3,3,3,2,5,1],[0,2,2,5,2,5,5,4,3,1],[0,3,3,3,5,0,2,3,0,0],[0,3,0,2,0,5,3,0,3,3]]
R=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def zero(seq):
 vals=[R[k%6]for k in seq];return sum(x for x,y in vals)==0 and sum(y for x,y in vals)==0
for i,j in itertools.combinations(range(10),2):
 assert zero(E[t][j]-E[t][i]for t in range(10))
 assert zero(E[j][t]-E[i][t]for t in range(10))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'order':10,'root_alphabet':6,'row_grams':45,'column_grams':45,'exponent_matrix':E,'status':'PASS'}
(P/'frontier-20261028-y10-nonaffine-seed-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='exponent_matrix'},indent=2))
