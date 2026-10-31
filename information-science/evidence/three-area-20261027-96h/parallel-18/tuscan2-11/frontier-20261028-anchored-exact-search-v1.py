#!/usr/bin/env python3
"""Bounded exact search for completions of selected compatible row subsets.

This is a search over specified candidate-row anchors, not an unrestricted
nonexistence procedure. Any candidate witness must be independently checked;
an unknown or stopped case never means UNSAT.
"""
import hashlib
import importlib.util
import itertools
import json
import random
import sys
import time
from pathlib import Path

helper_path=Path(__file__).with_name('frontier-20261028-five-share-exhaust-v1.py')
spec=importlib.util.spec_from_file_location('anchor_completion_helper',helper_path)
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
N=h.N


def main(argv):
    if len(argv)!=9:
        raise ValueError('usage: SCRIPT SOURCE OUTPUT FIXED_COUNT MAX_CASES SEED SECONDS_PER_CASE NODE_CAP ROW_CAP')
    source,output=Path(argv[1]),Path(argv[2])
    k,max_cases,seed=int(argv[3]),int(argv[4]),int(argv[5])
    seconds,node_cap,row_cap=float(argv[6]),int(argv[7]),int(argv[8])
    if not 1<=k<N or max_cases<=0 or seconds<=0 or node_cap<=0 or row_cap<=0:
        raise ValueError('invalid limits')
    raw=source.read_bytes(); rows=json.loads(raw)['rows']
    if len(rows)!=N or any(sorted(r)!=list(range(N)) for r in rows):
        raise ValueError('expected eleven valid permutation rows')
    started=time.monotonic()
    subsets=[ids for ids in itertools.combinations(range(N),k) if h.direct_fixed([rows[i] for i in ids])]
    random.Random(seed).shuffle(subsets)
    cases=[]; candidate=None
    for ids in subsets[:max_cases]:
        fixed=[rows[i] for i in ids]
        case=h.run_subset(fixed,seconds,node_cap,row_cap)
        case['fixed_rows_1based']=[i+1 for i in ids]
        cases.append(case)
        print(json.dumps({key:case[key] for key in ('fixed_rows_1based','status','eligible_rows','cover_nodes','elapsed_ms')}),flush=True)
        if case['status']=='candidate_witness_requires_independent_check':
            candidate=[list(r) for r in fixed]+[list(r) for r in case['completion_rows']]
            break
    complete=len(cases)==len(subsets)
    excluded=complete and all(c['status']=='no_completion_exhaustive' for c in cases)
    result={'kind':'bounded_selected_anchor_exact_completion','source_sha256':hashlib.sha256(raw).hexdigest(),
            'helper_sha256':hashlib.sha256(helper_path.read_bytes()).hexdigest(),
            'fixed_count':k,'seed':seed,'compatible_subsets':len(subsets),'cases_run':len(cases),
            'all_compatible_subsets_excluded':excluded,'cases':cases,
            'limits':{'max_cases':max_cases,'seconds_per_case':seconds,'node_cap':node_cap,'row_cap':row_cap},
            'elapsed_ms':round((time.monotonic()-started)*1000),
            'scope':'Only exact rows retained from this candidate; unrun or UNKNOWN cases have no verdict.'}
    if candidate is not None:
        result.update({'rows':candidate,'zero_score_claim':True,'best_pair_collision_score':0,
                       'd1_pair_collisions':0,'d2_pair_collisions':0,'d1_excess_events':0,'d2_excess_events':0})
    with output.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({'compatible_subsets':len(subsets),'cases_run':len(cases),
        'candidate_witness':candidate is not None,'all_compatible_subsets_excluded':excluded,
        'elapsed_ms':result['elapsed_ms']}))


if __name__=='__main__':
    main(sys.argv)
