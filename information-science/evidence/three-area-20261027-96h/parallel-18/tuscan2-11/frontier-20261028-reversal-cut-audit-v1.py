#!/usr/bin/env python3
"""Bounded exact audit of the new SAT endpoint lex symmetry cut.

Check its actual added CNF projection against direct permutation reversal on
100 random derangements, then reconstruct that reversal on an actual T1 table.
This finite audit is not a proof of full SAT encoding or a nonexistence result.
"""
import hashlib
import importlib.util
import json
import random
import sys
import time
from pathlib import Path
import z3

HERE=Path(__file__).parent

def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,HERE/filename)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj

base=load('tuscan_base','frontier-20261028-tuscan-sat-v1.py')
cut=load('tuscan_cut','frontier-20261028-tuscan-sat-reversal-v1.py')
N=base.N


def reverse_endpoints(end):
    inverse=[None]*N
    for r,v in enumerate(end): inverse[v]=r
    return [N-1-inverse[N-1-r] for r in range(N)]


def normalize(rows):
    mapping={symbol:index for index,symbol in enumerate(rows[0])}
    transformed=[[mapping[symbol] for symbol in row] for row in rows]
    return sorted(transformed,key=lambda row:row[0])


def main(argv):
    if len(argv)!=3: raise ValueError('usage: SCRIPT INPUT.json OUTPUT.json')
    source,output=Path(argv[1]),Path(argv[2]);raw=source.read_bytes()
    rows=json.loads(raw)['rows'];n=len(rows)
    if n!=N or any(sorted(row)!=list(range(N)) for row in rows): raise ValueError('invalid rows')
    direct=normalize(rows)
    if direct[0]!=list(range(N)) or [r[0] for r in direct]!=list(range(N)):
        raise AssertionError('input not normalizable by unique starts')
    mirrored=sorted([[N-1-x for x in reversed(row)] for row in direct],key=lambda row:row[0])
    e=[r[-1] for r in direct];eprime=[r[-1] for r in mirrored]
    if eprime!=reverse_endpoints(e) or mirrored[0]!=list(range(N)):
        raise AssertionError('reversal endpoint conjugation mismatch')
    for d in (1,2):
        original=[(row[i],row[i+d]) for row in direct for i in range(N-d)]
        changed=[(row[i],row[i+d]) for row in mirrored for i in range(N-d)]
        if len(set(original))!=len(set(changed)):
            raise AssertionError('reversal changed distinct event count')
    start=time.monotonic(); raw_base=base.build('full',None,set());formula=cut.build()
    extra=formula.clauses[len(raw_base.clauses):]
    variables={abs(lit) for clause in extra for lit in clause}
    b={v:z3.Bool('v%d'%v) for v in variables}
    solver=z3.Solver()
    for clause in extra:
        solver.add(z3.Or(*[(b[abs(v)] if v>0 else z3.Not(b[abs(v)])) for v in clause]))
    randomizer=random.Random(2026102821);tested=0
    while tested<100:
        suffix=list(range(N-1));randomizer.shuffle(suffix);end=[N-1]+suffix
        if any(end[i]==i for i in range(N)): continue
        image=reverse_endpoints(end);expected=end<=image
        solver.push()
        for r in range(N):
            for value in range(N):
                solver.add(b[base.xvar(r,N-1,value)] == (end[r]==value))
        observed=solver.check()
        solver.pop()
        if observed==z3.unknown: raise RuntimeError('unexpected Z3 unknown')
        if (observed==z3.sat)!=expected: raise AssertionError('lex cut projection mismatch')
        tested+=1
    result={'input_sha256':hashlib.sha256(raw).hexdigest(),
            'cut_source_sha256':hashlib.sha256((HERE/'frontier-20261028-tuscan-sat-reversal-v1.py').read_bytes()).hexdigest(),
            'seed':2026102821,'derangements_checked':tested,'all_cnf_projections_match_direct_lex':True,
            'actual_input_endpoints':e,'actual_reversed_endpoints':eprime,
            'actual_reversal_endpoint_formula_matches':True,
            'added_clauses':len(extra),'added_variable_count':len(variables),
            'elapsed_ms':round((time.monotonic()-start)*1000),
            'scope':'Bounded cut audit only, not proof of the full SAT encoding.'}
    with output.open('x',encoding='utf-8') as stream: json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main(sys.argv)
