#!/usr/bin/env python3
"""Alternative one-point KF(6^4) seeds for the B1f restricted search, not an extra target.
Points0..23, groups6i..6i+5. z(T,j) chooses a transversal triple T in class j=0,1,2 of its unique missing-group
family. Every cross-group pair is covered exactly once, and every class covers all18 points outside its
missed group exactly once. Sound prefix ordering of the triples through the least admissible point removes
class-label permutations. The output frame is checked directly before writing; no global design symmetry.
Usage: kf6_seed.py NEW_OUTDIR SEED NATIVE_SECONDS
"""
import lane_guard  # noqa: F401
import itertools
import json
import os
import sys
from collections import Counter, defaultdict
from lane_guard import fresh_dir, xopen
from lanelib import CNF, kissat


def main():
    out, sd, tl = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    fresh_dir(out)
    triples = [T for T in itertools.combinations(range(24),3) if len({p//6 for p in T})==3]
    missing = {T:(set(range(4))-{p//6 for p in T}).pop() for T in triples}
    cnf = CNF()
    z = {(T,j):cnf.var() for T in triples for j in range(3)}
    pairvars, pointvars = defaultdict(list), defaultdict(list)
    for (T,j), var in z.items():
        for pr in itertools.combinations(T,2):
            pairvars[pr].append(var)
        for p in T:
            pointvars[(missing[T],j,p)].append(var)
    for pr in itertools.combinations(range(24),2):
        if pr[0]//6 != pr[1]//6:
            cnf.exactly_one(pairvars[pr])
    for omit in range(4):
        points = [p for p in range(24) if p//6 != omit]
        for j in range(3):
            for p in points:
                cnf.exactly_one(pointvars[(omit,j,p)])
        Ts = sorted(T for T in triples if missing[T]==omit and min(points) in T)
        before = [None]*3
        for T in Ts:
            for j in (1,2):
                cnf.add([-z[(T,j)],before[j-1]] if before[j-1] is not None else [-z[(T,j)]])
            after=[]
            for j in range(3):
                v=cnf.var(); zi=z[(T,j)]
                if before[j] is None:
                    cnf.add([-v,zi]); cnf.add([v,-zi])
                else:
                    cnf.add([-before[j],v]); cnf.add([-zi,v]); cnf.add([-v,before[j],zi])
                after.append(v)
            before=after
    path=os.path.join(out,'frame.cnf')
    sha=cnf.write(path)
    st, model, seconds=kissat(path,tl,seed=sd,log=path+'.log')
    rec={'status':st,'seed':sd,'vars':cnf.nv,'clauses':len(cnf.clauses),'cnf_sha256':sha,'seconds':seconds}
    if st=='SAT':
        frames={omit:[sorted(T for T in triples if missing[T]==omit and z[(T,j)] in model) for j in range(3)]
                for omit in range(4)}
        cover=Counter(pr for Cs in frames.values() for C in Cs for T in C for pr in itertools.combinations(T,2))
        universe={pr for pr in itertools.combinations(range(24),2) if pr[0]//6 != pr[1]//6}
        assert set(cover)==universe and set(cover.values())=={1}, 'not a GDD(2,3,24) of type6^4'
        for omit,Cs in frames.items():
            target={p for p in range(24) if p//6 != omit}
            for C in Cs:
                flat=[p for T in C for p in T]
                assert len(C)==6 and len(flat)==len(set(flat)) and set(flat)==target, 'not a frame class'
        p=os.path.join(out,'kf6.json')
        with xopen(p) as fh: json.dump({'points':24,'group_size':6,'frames':frames},fh,indent=1)
        rec.update({'frame':p,'classes':12,'triples':72})
    with xopen(os.path.join(out,'summary.json')) as fh: json.dump(rec,fh,indent=1)
    print(json.dumps(rec))


if __name__=='__main__': main()
