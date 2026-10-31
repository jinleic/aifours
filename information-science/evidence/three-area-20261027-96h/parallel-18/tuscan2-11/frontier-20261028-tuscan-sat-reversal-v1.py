#!/usr/bin/env python3
"""Bounded T2 SAT with a proven NON-STRICT reversal endpoint lex cut.

Normalize row0 to 0..10 and order rows by their unique starts. Global row
reversal plus x->10-x, then re-sorting by starts, keeps that normalization and
maps the endpoint permutation E to E'=c E^{-1} c. Keep E<=lex E'; ties are
allowed, so every reversal orbit retains at least one table. No Latin or wrap
condition is added. Unverified UNSAT and UNKNOWN do not prove nonexistence.
"""
import hashlib
import importlib.util
import json
import subprocess
import sys
import time
from pathlib import Path

helper_path=Path(__file__).with_name('frontier-20261028-tuscan-sat-v1.py')
spec=importlib.util.spec_from_file_location('tuscan_sat_helper',helper_path)
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
N=h.N


def build():
    f=h.build('full',None,set())
    for r in range(N):
        f.add(h.xvar(r,0,r))
    for a in range(N):
        endpoints=[h.xvar(r,N-1,a) for r in range(N)]
        f.add(*endpoints)
        f.pairwise_amo(endpoints)
    # r=0 is necessarily equal in both endpoints because e(0)=10.
    prefix=f.new(); f.add(prefix)
    for r in range(1,N):
        eq=f.new()
        equal_values=[]
        for value in range(N):
            left=h.xvar(r,N-1,value)
            # E'(r)=value iff E(10-value)=10-r.
            right=h.xvar(N-1-value,N-1,N-1-r)
            both=f.new()
            f.add(-both,left); f.add(-both,right); f.add(-left,-right,both)
            f.add(-both,eq)
            equal_values.append(both)
        f.add(-eq,*equal_values)
        for a in range(N):
            for b in range(a):
                # If all previous positions agree, E[r] > E'[r] is forbidden.
                f.add(-prefix,-h.xvar(r,N-1,a),-h.xvar(N-1-b,N-1,N-1-r))
        if r<N-1:
            following=f.new()
            f.add(-following,prefix); f.add(-following,eq); f.add(-prefix,-eq,following)
            prefix=following
    return f


def main(argv):
    if len(argv)!=5:
        raise ValueError('usage: SCRIPT OUTPUT.json OUTPUT.cnf SECONDS SEED')
    output,cnf_path=Path(argv[1]),Path(argv[2]);seconds,seed=int(argv[3]),int(argv[4])
    if not 1<=seconds<=600 or not 0<=seed<=2147483647:
        raise ValueError('invalid limits')
    start=time.monotonic();formula=build()
    with output.open('x',encoding='utf-8') as stream,cnf_path.open('x',encoding='ascii') as cnf:
        cnf.write(f'p cnf {formula.variables} {len(formula.clauses)}\n')
        for clause in formula.clauses: cnf.write(' '.join(map(str,clause))+' 0\n')
        cnf.flush()
        construction_ms=round((time.monotonic()-start)*1000)
        command=['kissat','--sat',f'--time={seconds}',f'--seed={seed}',str(cnf_path)]
        solving=time.monotonic()
        try:
            proc=subprocess.run(command,capture_output=True,text=True,timeout=seconds+15,check=False)
            rc,stdout,stderr,timeout=proc.returncode,proc.stdout,proc.stderr,False
        except subprocess.TimeoutExpired as exc:
            rc=None;stdout=exc.stdout.decode() if isinstance(exc.stdout,bytes) else (exc.stdout or '')
            stderr=exc.stderr.decode() if isinstance(exc.stderr,bytes) else (exc.stderr or '');timeout=True
        status=('sat' if rc==10 and 's SATISFIABLE' in stdout else
                'unsat_unverified' if rc==20 and 's UNSATISFIABLE' in stdout else
                'unknown' if rc in (0,None) else 'solver_error')
        result={'kind':'bounded_reversal_canonical_tuscan2_sat',
                'helper_source_sha256':hashlib.sha256(helper_path.read_bytes()).hexdigest(),
                'cnf_sha256':hashlib.sha256(cnf_path.read_bytes()).hexdigest(),
                'variables':formula.variables,'clauses':len(formula.clauses),
                'command':command,'returncode':rc,'solver_status':status,'supervisory_timeout':timeout,
                'construction_ms':construction_ms,'solve_ms':round((time.monotonic()-solving)*1000),
                'normalization':'first row 0..10; starts 0..10; end permutation E<=lex c E^-1 c; ties included',
                'scope':'Unrestricted exact linear event model; UNKNOWN and unchecked UNSAT prove nothing.',
                'solver_stdout':stdout,'solver_stderr':stderr}
        if status=='sat':
            assigned={int(v) for line in stdout.splitlines() if line.startswith('v ')
                      for v in line.split()[1:] if int(v)>0}
            rows=[]
            for r in range(N):
                row=[]
                for c in range(N):
                    choices=[a for a in range(N) if h.xvar(r,c,a) in assigned]
                    if len(choices)!=1: raise AssertionError('model lacks unique row symbol')
                    row.append(choices[0])
                rows.append(row)
            result.update({'rows':rows,'zero_score_claim':True,'best_pair_collision_score':0,
                           'd1_pair_collisions':0,'d2_pair_collisions':0,'d1_excess_events':0,'d2_excess_events':0})
        json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({k:result[k] for k in ('solver_status','returncode','construction_ms','solve_ms','variables','clauses','cnf_sha256')}))
    if status=='solver_error': raise SystemExit('solver error recorded')


if __name__=='__main__':
    main(sys.argv)
