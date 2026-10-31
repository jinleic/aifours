#!/usr/bin/env python3
"""Independently replay one concrete per-symbol D1 Hall separator.

Breadth-first candidate generation, direct event unions, brute endpoint
matching, and exact event-to-start neighborhoods; no probe code is imported.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

N=11


def main(argv):
    if len(argv)!=3: raise ValueError('usage: SCRIPT PROBE.json OUTPUT.json')
    source,output=Path(argv[1]),Path(argv[2]);raw=source.read_bytes();packet=json.loads(raw)
    rows=packet['partial_rows'];assert packet['status']=='separator_found'
    if len(rows)!=6 or any(sorted(r)!=list(range(N)) for r in rows):raise ValueError('invalid partial')
    starts={r[0] for r in rows};ends={r[-1] for r in rows}
    if len(starts)!=6 or len(ends)!=6:raise AssertionError('duplicate endpoint')
    d1=[(r[i],r[i+1]) for r in rows for i in range(N-1)]
    d2=[(r[i],r[i+2]) for r in rows for i in range(N-2)]
    if len(set(d1))!=len(d1) or len(set(d2))!=len(d2):raise AssertionError('partial event collision')
    used1,used2=set(d1),set(d2)
    level=[((),0)];nodes=1
    for pos in range(N):
        next_level=[]
        for row,mask in level:
            for v in range(N):
                if mask&(1<<v) or (pos==0 and v in starts) or (pos==N-1 and v in ends):continue
                if pos and (row[-1],v) in used1:continue
                if pos>1 and (row[-2],v) in used2:continue
                next_level.append((row+(v,),mask|(1<<v)));nodes+=1
        level=next_level
    candidates=[r for r,_ in level]
    all_events={(a,b) for a in range(N) for b in range(N) if a!=b}
    supp1={(r[i],r[i+1]) for r in candidates for i in range(N-1)}
    supp2={(r[i],r[i+2]) for r in candidates for i in range(N-2)}
    unsupported1=sorted((all_events-used1)-supp1)
    free_starts=sorted(set(range(N))-starts);free_ends=sorted(set(range(N))-ends)
    pairs={(r[0],r[-1]) for r in candidates}
    matching=next((list(zip(free_starts,perm)) for perm in itertools.permutations(free_ends)
                   if all((s,t) in pairs for s,t in zip(free_starts,perm))),None)
    a=packet['separator']['symbol'];targets=packet['separator']['missing_targets']
    target_events=[(a,b) for b in targets]
    neighbors={str(b):sorted({r[0] for r in candidates if any(r[i]==a and r[i+1]==b for i in range(N-1))}) for b in targets}
    union=sorted(set().union(*(set(v) for v in neighbors.values())))
    if unsupported1 or len(supp2)<(N-len(rows))*(N-2) or matching is None:
        raise AssertionError('example does not pass the stated baseline tests')
    if any(event in used1 for event in target_events) or len(union)>=len(targets):
        raise AssertionError('reported dual Hall witness is invalid')
    result={'probe_sha256':hashlib.sha256(raw).hexdigest(),'partial_rows':rows,
            'partial_d1_events':len(d1),'partial_d2_events':len(d2),
            'generation_nodes':nodes,'eligible_rows':len(candidates),
            'unused_starts':free_starts,'unused_ends':free_ends,
            'unsupported_required_d1_events':unsupported1,'d2_support':len(supp2),
            'required_d2_support':(N-len(rows))*(N-2),
            'endpoint_matching':matching,'symbol':a,'missing_targets':targets,
            'event_to_start_neighbors':neighbors,'joint_reachable_starts':union,
            'conclusion':'Distinct missing D1 arcs from one source need distinct rows; three arcs have only two possible starts.',
            'scope':'Only this exact partial row set; no global nonexistence.'}
    with output.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({k:result[k] for k in ('eligible_rows','generation_nodes','unused_starts','unused_ends',
        'unsupported_required_d1_events','d2_support','required_d2_support','endpoint_matching',
        'symbol','missing_targets','event_to_start_neighbors','joint_reachable_starts')}))


if __name__=='__main__':main(sys.argv)
