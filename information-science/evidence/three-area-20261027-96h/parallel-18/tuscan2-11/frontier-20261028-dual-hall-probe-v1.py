#!/usr/bin/env python3
"""Seek an actual partial row set exposing per-symbol D1 matching Hall failure.

A bounded seeded search, never a no-go on unvisited rows. At each sampled
compatible six-row set, independently regenerate ALL eligible next rows. A
reported separator must pass singleton D1 support, global D2 support and the
start/end matching test, but fail matching missing outgoing D1 arcs of some
symbol to distinct remaining starts. All computations use exact integers.
"""
import hashlib
import itertools
import json
import random
import sys
import time
from pathlib import Path

N=11


def masks(row):
    one=sum(1<<(N*row[i]+row[i+1]) for i in range(N-1))
    two=sum(1<<(N*row[i]+row[i+2]) for i in range(N-2))
    return one,two


def eligible(rows,deadline):
    starts={r[0] for r in rows};ends={r[-1] for r in rows}
    d1={(r[i],r[i+1]) for r in rows for i in range(N-1)}
    d2={(r[i],r[i+2]) for r in rows for i in range(N-2)}
    out=[];nodes=0
    def visit(path,used):
        nonlocal nodes
        nodes+=1
        if nodes%4096==0 and time.monotonic()>=deadline: raise TimeoutError
        if len(path)==N:
            if path[-1] not in ends:
                row=tuple(path);a,b=masks(row);out.append((row,a,b))
            return
        for v in range(N):
            if used&(1<<v) or (not path and v in starts):continue
            if path and (path[-1],v) in d1:continue
            if len(path)>1 and (path[-2],v) in d2:continue
            path.append(v);visit(path,used|(1<<v));path.pop()
    visit([],0)
    return out,nodes


def endpoint_feasible(candidates,remaining_starts):
    neighbors={s:{r[-1] for r,_,_ in candidates if r[0]==s} for s in remaining_starts}
    matched={}
    def augment(s,seen):
        for end in neighbors[s]:
            if end in seen:continue
            seen.add(end)
            if end not in matched or augment(matched[end],seen):
                matched[end]=s;return True
        return False
    return all(augment(s,set()) for s in remaining_starts)


def inspect(rows,candidates):
    starts={r[0] for r in rows};remaining_starts=set(range(N))-starts
    used1=used2=0
    for row in rows:
        a,b=masks(row);used1|=a;used2|=b
    universe=sum(1<<(a*N+b) for a in range(N) for b in range(N) if a!=b)
    supp1=supp2=0
    for _,one,two in candidates:supp1|=one;supp2|=two
    if (universe&~used1)&~supp1:return None
    if supp2.bit_count()<(N-len(rows))*(N-2):return None
    if not endpoint_feasible(candidates,remaining_starts):return None
    # The event/start bipartite graph is exact for each source symbol; every
    # actual row has at most one outgoing adjacency from a given symbol.
    for a in range(N):
        targets=[b for b in range(N) if b!=a and not (used1&(1<<(N*a+b)))]
        neighbors={b:{r[0] for r,one,_ in candidates if one&(1<<(N*a+b))} for b in targets}
        for size in range(2,len(targets)+1):
            for subset in itertools.combinations(targets,size):
                reachable=set().union(*(neighbors[b] for b in subset))
                if len(reachable)<size:
                    return {'symbol':a,'missing_targets':subset,'reachable_starts':sorted(reachable),
                            'eligible_count':len(candidates),'global_d1_singletons_all_supported':True,
                            'global_d2_support':supp2.bit_count(),'required_d2_support':(N-len(rows))*(N-2),
                            'endpoint_matching_exists':True}
    return None


def main(argv):
    if len(argv)!=6:raise ValueError('usage: SCRIPT SOURCE.json OUTPUT.json SEED SECONDS MAX_ATTEMPTS')
    source,out=Path(argv[1]),Path(argv[2]);seed,seconds,cap=int(argv[3]),float(argv[4]),int(argv[5])
    if seconds<=0 or cap<=0:raise ValueError('invalid bounds')
    raw=source.read_bytes();base=json.loads(raw)['rows'];fixed=[base[i-1] for i in (3,5,10)]
    started=time.monotonic();deadline=started+seconds;rng=random.Random(seed)
    attempts=0;valid=0;found=None;partial=None;root_count=None;status='attempt_limit'
    try:
        root,_=eligible(fixed,deadline);root_count=len(root)
        used1=used2=0;starts=set();ends=set()
        for row in fixed:
            a,b=masks(row);used1|=a;used2|=b;starts.add(row[0]);ends.add(row[-1])
        for _ in range(cap):
            if time.monotonic()>=deadline:raise TimeoutError
            attempts+=1;selected=[];one,two=used1,used2;ss=set(starts);ee=set(ends)
            for __ in range(3):
                chosen=None
                for ___ in range(100):
                    candidate=rng.choice(root);r,a,b=candidate
                    if not (a&one or b&two or r[0] in ss or r[-1] in ee):chosen=candidate;break
                if chosen is None:break
                r,a,b=chosen;selected.append(r);one|=a;two|=b;ss.add(r[0]);ee.add(r[-1])
            if len(selected)!=3:continue
            valid+=1;partial=[tuple(r) for r in fixed]+selected
            candidates,_=eligible(partial,deadline)
            witness=inspect(partial,candidates)
            if witness is not None:found=witness;status='separator_found';break
    except TimeoutError:status='unknown_time_limit'
    result={'kind':'bounded_dual_hall_separator_probe','source_sha256':hashlib.sha256(raw).hexdigest(),
            'fixed_source_rows_1based':[3,5,10],'seed':seed,'seconds':seconds,'max_attempts':cap,
            'root_eligible_rows':root_count,'attempts':attempts,'compatible_six_row_samples':valid,
            'status':status,'partial_rows':partial if found else None,'separator':found,
            'elapsed_ms':round((time.monotonic()-started)*1000),
            'scope':'One bounded selected search; no witness or unrestricted nonexistence claim.'}
    with out.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({key:result[key] for key in ('root_eligible_rows','attempts','compatible_six_row_samples','status','separator','elapsed_ms')}))


if __name__=='__main__':main(sys.argv)
