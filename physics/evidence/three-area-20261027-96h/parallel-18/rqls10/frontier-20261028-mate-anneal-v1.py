#!/usr/bin/env python3
"""Search Latin mates of Weisner Fig.1 transversal L, preserving row symbols.

Integer energy counts duplicate color pairs in each column and transversal.
Zero-energy tables are checked exactly. Search is finite and non-exhaustive.
"""
import argparse
from collections import Counter
import importlib.util
import json
import math
from pathlib import Path
import random
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('switch', HERE / 'frontier-20261028-ols10-switch-v1.py')
switch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(switch)
N = switch.N
LATIN = [[switch.TABLE[r][c][1] for c in range(N)] for r in range(N)]
BASE = [[switch.TABLE[r][c][0] for c in range(N)] for r in range(N)]


def count_tables(A):
    cols = [[0]*N for _ in range(N)]
    labels = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            a = A[r][c]
            cols[c][a] += 1
            labels[LATIN[r][c]][a] += 1
    return cols, labels


def energy(cols, labels):
    return sum(v*(v-1)//2 for line in cols + labels for v in line)


def normalized(A):
    # Symbol relabelling fixes the first row as 0,...,N-1.
    rename = {a:c for c,a in enumerate(A[0])}
    return tuple(tuple(rename[a] for a in row) for row in A)


def moves(A, cols, labels, r, c1, c2, do):
    a,b = A[r][c1], A[r][c2]
    t1,t2 = LATIN[r][c1], LATIN[r][c2]
    updates = ((cols[c1],a,b),(cols[c2],b,a),(labels[t1],a,b),(labels[t2],b,a))
    delta = sum(-(line[old]-1)+line[new] for line,old,new in updates)
    if do:
        for line,old,new in updates:
            line[old] -= 1
            line[new] += 1
        A[r][c1],A[r][c2] = b,a
    return delta


def check_and_components(A):
    saved = switch.TABLE
    switch.TABLE = tuple(tuple((A[r][c],LATIN[r][c]) for c in range(N)) for r in range(N))
    try:
        switch.check_table()
        counts = Counter(tuple(sorted(map(len, switch.components(a,b))))
                         for a in range(N) for b in range(a+1,N))
        return [[list(sizes), count] for sizes,count in sorted(counts.items())]
    finally:
        switch.TABLE = saved


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--restarts',type=int,default=5)
    p.add_argument('--steps',type=int,default=250000)
    p.add_argument('--seconds',type=float,default=45)
    p.add_argument('--seed',type=int,default=24001)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0:
        raise ValueError('positive run bounds required')
    rng=random.Random(args.seed)
    start=time.monotonic()
    ref=normalized(BASE)
    all_solutions={ref}
    distinct=[]
    runs=[]
    for restart in range(args.restarts):
        A=[row[:] for row in BASE]
        cols,labels=count_tables(A)
        for _ in range(8 + restart*3):
            r=rng.randrange(N)
            c1,c2=rng.sample(range(N),2)
            moves(A,cols,labels,r,c1,c2,True)
        E=energy(cols,labels)
        best=E
        for step in range(1,args.steps+1):
            # Reheating avoids freezing at the unperturbed reference.
            t=step % 30000
            temperature=0.18 + 1.20*(1-t/30000)
            r=rng.randrange(N)
            c1,c2=rng.sample(range(N),2)
            delta=moves(A,cols,labels,r,c1,c2,False)
            if delta<=0 or rng.random()<math.exp(-delta/temperature):
                moves(A,cols,labels,r,c1,c2,True)
                E+=delta
                best=min(best,E)
            if E==0:
                assert E == energy(cols,labels)
                key=normalized(A)
                if key not in all_solutions:
                    all_solutions.add(key)
                    components=check_and_components(A)
                    distinct.append({'restart':restart,'step':step,
                                     'table':[row[:] for row in A],
                                     'pair_component_histogram':components})
                    print('distinct mate',len(distinct),'restart',restart,'step',step,
                          'components',components,flush=True)
                    if any(len(sizes)>1 for sizes,count in components):
                        print('NONTRIVIAL_PAIR_SWITCH_FOUND',flush=True)
                        break
                # Move away from any zero-energy point; these moves maintain rows.
                for _ in range(8):
                    rr=rng.randrange(N)
                    x,y=rng.sample(range(N),2)
                    E+=moves(A,cols,labels,rr,x,y,True)
            if step%2000==0 and time.monotonic()-start>=args.seconds:
                break
        assert E == energy(cols,labels)
        runs.append({'restart':restart,'steps':step,'best_energy':best,'final_energy':E})
        print('restart',restart,'steps',step,'best_energy',best,'distinct_mates',len(distinct),flush=True)
        if time.monotonic()-start>=args.seconds or (distinct and any(len(s)>1 for s,c in distinct[-1]['pair_component_histogram'])):
            break
    record={'fixed_L':'Weisner 1963 Fig.1 second digit','parameters':vars(args),
            'elapsed_seconds':time.monotonic()-start,'runs':runs,'distinct_mates':distinct,
            'caveat':'bounded stochastic search; no exhaustive or unrestricted conclusion'}
    path=HERE/'frontier-20261028-mate-anneal-result-v1.json'
    path.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('wrote',path.name,flush=True)


if __name__=='__main__':
    main()
