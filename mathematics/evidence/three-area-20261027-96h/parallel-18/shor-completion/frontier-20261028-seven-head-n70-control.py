#!/usr/bin/env python3
"""Optional bounded Boolean control for the all-order seven-head proof."""
from itertools import combinations
from pathlib import Path
import json,runpy,time

solver=runpy.run_path(str(Path(__file__).with_name('frontier-20261028-border-exact-one-replay.py')))['exact_one']
n=70;A={0,3,8,11};Y=(0,1,7,13,14);stats={'n':n,'tested':0,'root_conflict':0,'search_unsat':0,'unknown':0,'sat':0,'nodes':0}
deadline=time.monotonic()+50
for extra in combinations(sorted(set(range(n))-A),3):
    if time.monotonic()>=deadline:break
    P=tuple(sorted(A|set(extra)));answer,nodes=solver(n,P,Y,deadline,100000);stats['tested']+=1;stats['nodes']+=nodes
    if answer is None:stats['unknown']+=1
    elif answer is False:stats['root_conflict' if nodes==0 else 'search_unsat']+=1
    else:
        stats['sat']+=1
        if not set(Y)<=set(answer) or len({(p+q)%n for p in P for q in answer})!=n:
            raise AssertionError('invalid SAT')
        print(json.dumps({'SAT':{'P':P,'Q':answer},'stats':stats}));break
print(json.dumps(stats,indent=2))
