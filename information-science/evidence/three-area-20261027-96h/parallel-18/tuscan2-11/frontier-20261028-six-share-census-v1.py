#!/usr/bin/env python3
"""Bounded exact completion of all compatible six-row subsets of one table.

Uses the pinned breadth-first row generator/exact-cover implementation as a
helper. A negative result concerns only the selected candidate's exact row
strings; any witness requires independent checking. UNKNOWN never means UNSAT.
"""
import hashlib
import importlib.util
import itertools
import json
import sys
import time
from pathlib import Path

helper_path=Path(__file__).with_name('frontier-20261028-five-share-exhaust-v1.py')
spec=importlib.util.spec_from_file_location('completion_helper',helper_path)
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
N=h.N


def main(argv):
    if len(argv)!=6:
        raise ValueError('usage: SCRIPT INPUT.json OUTPUT.json SECONDS_PER_CASE NODE_CAP ROW_CAP')
    source,out=Path(argv[1]),Path(argv[2])
    seconds,node_cap,row_cap=float(argv[3]),int(argv[4]),int(argv[5])
    if seconds<=0 or node_cap<=0 or row_cap<=0:
        raise ValueError('invalid limits')
    raw=source.read_bytes()
    rows=json.loads(raw)['rows']
    if len(rows)!=N or any(sorted(r)!=list(range(N)) for r in rows):
        raise ValueError('invalid candidate rows')
    start=time.monotonic()
    subsets=[ids for ids in itertools.combinations(range(N),6) if h.direct_fixed([rows[i] for i in ids])]
    cases=[]
    candidate=None
    for subset in subsets:
        fixed=[rows[i] for i in subset]
        case=h.run_subset(fixed,seconds,node_cap,row_cap)
        case['fixed_rows_1based']=[i+1 for i in subset]
        cases.append(case)
        print(json.dumps({k:case[k] for k in ('fixed_rows_1based','status','eligible_rows','cover_nodes','elapsed_ms')}),flush=True)
        if case['status']=='candidate_witness_requires_independent_check':
            candidate=[list(r) for r in fixed]+[list(r) for r in case['completion_rows']]
            break
    complete=len(cases)==len(subsets)
    excluded=complete and all(c['status']=='no_completion_exhaustive' for c in cases)
    result={'kind':'six_shared_rows_bounded_completion_census','source_sha256':hashlib.sha256(raw).hexdigest(),
            'helper_sha256':hashlib.sha256(helper_path.read_bytes()).hexdigest(),
            'total_six_subsets':462,'compatible_six_subsets':len(subsets),'cases_run':len(cases),
            'all_compatible_subsets_excluded':excluded,'cases':cases,
            'limits':{'seconds_per_case':seconds,'node_cap':node_cap,'row_cap':row_cap},
            'elapsed_ms':round((time.monotonic()-start)*1000),
            'scope':'Exact reuse of six rows from this candidate only. UNKNOWN is not nonexistence.'}
    if candidate is not None:
        result.update({'rows':candidate,'zero_score_claim':True,'best_pair_collision_score':0,
                       'd1_pair_collisions':0,'d2_pair_collisions':0,'d1_excess_events':0,'d2_excess_events':0})
    with out.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({'compatible_six_subsets':len(subsets),'cases_run':len(cases),
                      'all_compatible_subsets_excluded':excluded,
                      'candidate_witness':candidate is not None,'elapsed_ms':result['elapsed_ms']}))


if __name__=='__main__':
    main(sys.argv)
