#!/usr/bin/env python3
"""Exact finite spectrum quotient; assumes separately written cyclic no-gos."""
import collections,datetime,hashlib,itertools,json,math
from pathlib import Path
P=Path(__file__).resolve().parent
units=(1,4,11,14);D={2,5,7,8,10,13}
assert all({u*d%15 for d in D}==D for u in units)
def canonical(S):return min(tuple(sorted((u*a+t)%15 for a in S))for u in units for t in range(15))
C3=[frozenset((a+5*k)%15 for k in range(3))for a in range(5)]
allsets=list(itertools.combinations(range(15),6));classes={};rejected=collections.Counter()
for S in allsets:
 counts=collections.Counter(a%3 for a in S)
 if len(counts)<3:rejected['missing_U5_class']+=1;continue
 if sorted(counts.values())==[1,1,4]:rejected['multiplicity_4_1_1']+=1;continue
 assert sorted(counts.values()) in ([1,2,3],[2,2,2])
 classes.setdefault(canonical(S),[]).append(S)
assert len(allsets)==5005 and len(classes)==80 and sum(map(len,classes.values()))==4000
records=[]
for rep,orbit in sorted(classes.items()):
 two=any(set(a)|set(b)==set(rep)for a,b in itertools.combinations(C3,2));mult=sorted(collections.Counter(x%3 for x in rep).values());records.append({'representative':rep,'orbit_size':len(orbit),'U5_multiplicities':mult,'excluded_two_3cosets':two})
assert sum(q['excluded_two_3cosets']for q in records)==2
remain=[q for q in records if not q['excluded_two_3cosets']];assert len(remain)==78
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'six_distinct_spectra_total':len(allsets),'rejected':dict(rejected),'before_two_coset_exclusion':len(classes),
 'remaining_classes':len(remain),'remaining_U5_multiplicities':dict(collections.Counter(str(q['U5_multiplicities'])for q in remain)),
 'all_orbit_records':records,'scope':'conditional finite spectrum quotient; remaining amplitude and Gram equations not solved','status':'PASS'}
(P/'frontier-20261029-cyclic15-residual-spectra-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='all_orbit_records'},indent=2))
