#!/usr/bin/env python3
"""Reconstruct reversed partial and all four directed dual Hall families.

Independent BFS generation and subset checks; uses only literal probe rows.
This is a bounded example, not a global nonexistence test.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

N=11


def main(argv):
    if len(argv)!=3:raise ValueError('usage: SCRIPT PROBE.json OUTPUT.json')
    source,out=Path(argv[1]),Path(argv[2]);raw=source.read_bytes();packet=json.loads(raw)
    rows=[list(reversed(row)) for row in packet['partial_rows']];k=len(rows)
    if k!=6 or any(sorted(r)!=list(range(N)) for r in rows):raise ValueError('invalid partial rows')
    starts={r[0] for r in rows};ends={r[-1] for r in rows}
    d1=[(r[i],r[i+1]) for r in rows for i in range(N-1)]
    d2=[(r[i],r[i+2]) for r in rows for i in range(N-2)]
    if len(starts)!=k or len(ends)!=k or len(set(d1))!=len(d1) or len(set(d2))!=len(d2):
        raise AssertionError('partial conflict')
    used1,used2=set(d1),set(d2);level=[((),0)];nodes=1
    for pos in range(N):
        nxt=[]
        for row,mask in level:
            for v in range(N):
                if mask&(1<<v) or pos==0 and v in starts or pos==N-1 and v in ends:continue
                if pos and (row[-1],v) in used1 or pos>1 and (row[-2],v) in used2:continue
                nxt.append((row+(v,),mask|(1<<v)));nodes+=1
        level=nxt
    eligible=[r for r,_ in level]
    fs=sorted(set(range(N))-starts);fe=sorted(set(range(N))-ends)
    pairs={(r[0],r[-1]) for r in eligible}
    matching=next((list(zip(fs,perm)) for perm in itertools.permutations(fe)
                   if all((s,e) in pairs for s,e in zip(fs,perm))),None)
    universe={(a,b) for a in range(N) for b in range(N) if a!=b}
    sup1={(r[i],r[i+1]) for r in eligible for i in range(N-1)}
    sup2={(r[i],r[i+2]) for r in eligible for i in range(N-2)}
    unsupported1=sorted((universe-used1)-sup1)
    previous_violations=[]
    for kind,values in (('starts',fs),('ends',fe)):
        for size in range(1,len(values)+1):
            for subset in itertools.combinations(values,size):
                chosen=[r for r in eligible if (r[0] if kind=='starts' else r[-1]) in subset]
                p1={(r[i],r[i+1]) for r in chosen for i in range(N-1)}
                p2={(r[i],r[i+2]) for r in chosen for i in range(N-2)}
                if len(p1)<size*(N-1) or len(p2)<size*(N-2):previous_violations.append([kind,subset,len(p1),len(p2)])
    failures={}
    for direction in ('out','in'):
        for endpoint in ('start','end'):
            examples=[]
            for a in range(N):
                targets=[b for b in range(N) if b!=a and ((a,b) if direction=='out' else (b,a)) not in used1]
                neighbors={b:{r[0] if endpoint=='start' else r[-1] for r in eligible
                    if ((a,b) if direction=='out' else (b,a)) in set(zip(r,r[1:]))} for b in targets}
                for count in range(1,len(targets)+1):
                    for subset in itertools.combinations(targets,count):
                        reachable=set().union(*(neighbors[b] for b in subset))
                        if len(reachable)<count:
                            examples.append({'symbol':a,'targets':subset,'neighbors':sorted(reachable)})
            failures[direction+'_'+endpoint]=examples
    if (unsupported1 or len(sup2)<(N-k)*(N-2) or matching is None or previous_violations or
            failures['out_start'] or failures['in_start'] or not failures['out_end'] or not failures['in_end']):
        raise AssertionError('reversal separator does not match stated scope')
    example={'symbol':3,'targets':[1,9],'end_neighbors':{str(b):sorted({r[-1] for r in eligible
             if (3,b) in set(zip(r,r[1:]))}) for b in (1,9)}}
    if set(example['end_neighbors']['1'])|set(example['end_neighbors']['9'])!={2}:
        raise AssertionError('displayed event/end neighborhood mismatch')
    result={'probe_sha256':hashlib.sha256(raw).hexdigest(),'partial_rows':rows,
            'eligible_rows':len(eligible),'generation_nodes':nodes,'unused_starts':fs,'unused_ends':fe,
            'unsupported_d1':unsupported1,'d2_support':len(sup2),'required_d2_support':(N-k)*(N-2),
            'endpoint_matching':matching,'previous_support_violations':previous_violations,
            'dual_failure_counts':{key:len(value) for key,value in failures.items()},
            'outgoing_to_end_example':example,
            'scope':'Only the displayed reversed partial set; no unrestricted nonexistence.'}
    with out.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({key:result[key] for key in ('eligible_rows','generation_nodes','unused_starts','unused_ends',
        'unsupported_d1','d2_support','required_d2_support','endpoint_matching','previous_support_violations',
        'dual_failure_counts','outgoing_to_end_example')}))


if __name__=='__main__':main(sys.argv)
