#!/usr/bin/env python3
"""Independently verify one solver-recorded D2 support pruning prefix.

Regenerate every eligible next row by direct prefix DFS; compute exact D1 and
D2 support and forced-missing D2 events. This concerns only that fixed prefix.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

N=11


def main(argv):
    if len(argv)!=4: raise ValueError('usage: SCRIPT SOURCE.json SOLVER.json OUTPUT.json')
    source,solver,output=map(Path,argv[1:]);source_raw=source.read_bytes();solver_raw=solver.read_bytes()
    all_rows=json.loads(source_raw)['rows'];metadata=json.loads(solver_raw)
    kept=[all_rows[i-1] for i in metadata['fixed_rows_1based']]
    added=metadata['first_d2_support_prune']['added_rows']
    rows=kept+added;k=len(rows)
    if not 0<k<N or any(len(row)!=N or sorted(row)!=list(range(N)) for row in rows):
        raise ValueError('bad partial row list')
    starts={r[0] for r in rows};ends={r[-1] for r in rows}
    if len(starts)!=k or len(ends)!=k: raise AssertionError('partial duplicate endpoints')
    event1=[(r[i],r[i+1]) for r in rows for i in range(N-1)]
    event2=[(r[i],r[i+2]) for r in rows for i in range(N-2)]
    if len(set(event1))!=len(event1) or len(set(event2))!=len(event2):
        raise AssertionError('partial event collision')
    used1,used2=set(event1),set(event2)
    eligible=[]; nodes=0
    def visit(prefix,used):
        nonlocal nodes
        nodes+=1
        if len(prefix)==N:
            if prefix[-1] not in ends: eligible.append(tuple(prefix))
            return
        for v in range(N):
            if used & (1<<v) or (not prefix and v in starts): continue
            if prefix and (prefix[-1],v) in used1: continue
            if len(prefix)>1 and (prefix[-2],v) in used2: continue
            prefix.append(v);visit(prefix,used|(1<<v));prefix.pop()
    visit([],0)
    universe={(a,b) for a in range(N) for b in range(N) if a!=b}
    support1={(r[i],r[i+1]) for r in eligible for i in range(N-1)}
    support2={(r[i],r[i+2]) for r in eligible for i in range(N-2)}
    missing1=sorted((universe-used1)-support1)
    forced_missing2=sorted((universe-used2)-support2)
    if len(forced_missing2)<=N:
        raise AssertionError('reported D2 support prune is unsupported')
    by_start={s:[r for r in eligible if r[0]==s] for s in set(range(N))-starts}
    hall=[];keys=sorted(by_start)
    for size in range(1,len(keys)+1):
        for selected in itertools.combinations(keys,size):
            u1={(r[i],r[i+1]) for s in selected for r in by_start[s] for i in range(N-1)}
            u2={(r[i],r[i+2]) for s in selected for r in by_start[s] for i in range(N-2)}
            targets={r[-1] for s in selected for r in by_start[s]}
            if len(u1)<size*(N-1) or len(u2)<size*(N-2) or len(targets)<size:
                hall.append({'starts':selected,'d1_support':len(u1),'d2_support':len(u2),'end_support':len(targets)})
    result={'source_sha256':hashlib.sha256(source_raw).hexdigest(),
            'solver_output_sha256':hashlib.sha256(solver_raw).hexdigest(),
            'fixed_source_rows_1based':metadata['fixed_rows_1based'],'added_rows':added,
            'partial_row_count':k,'partial_d1_events':len(event1),'partial_d2_events':len(event2),
            'eligible_rows':len(eligible),'generation_nodes':nodes,
            'unsupported_required_d1_events':missing1,'forced_missing_d2_events':forced_missing2,
            'forced_missing_d2_count':len(forced_missing2),'start_subset_hall_violations':hall,
            'conclusion':'This exact partial set cannot be extended to T2(11): more than eleven D2 events are forced missing.',
            'scope':'Only this concrete partial row set; no unrestricted nonexistence claim.'}
    with output.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({key:result[key] for key in ('partial_row_count','eligible_rows','generation_nodes',
        'unsupported_required_d1_events','forced_missing_d2_count','start_subset_hall_violations')}))


if __name__=='__main__':main(sys.argv)
