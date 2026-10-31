#!/usr/bin/env python3
"""Finite control for the 5D support-3 ONB combinatorial lemma."""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
S=list(itertools.combinations(range(5),3));counts={'support_multisets':0,'no_single_intersection':0,'all_coordinate_degrees_at_least_two':0}
for q in itertools.combinations_with_replacement(range(len(S)),5):
 counts['support_multisets']+=1;supports=[set(S[i])for i in q]
 if any(len(a&b)==1 for a,b in itertools.combinations(supports,2)):continue
 counts['no_single_intersection']+=1
 if min(sum(x in a for a in supports)for x in range(5))>=2:counts['all_coordinate_degrees_at_least_two']+=1
assert counts['all_coordinate_degrees_at_least_two']==0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'counts':counts,'scope':'Necessary support-pattern control only; the written proof establishes the 5D ONB lemma independently.','status':'PASS'}
(P/'frontier-20261029-support3-five-control-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
