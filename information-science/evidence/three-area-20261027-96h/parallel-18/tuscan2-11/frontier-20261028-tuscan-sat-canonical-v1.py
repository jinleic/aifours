#!/usr/bin/env python3
"""Bounded unrestricted T2(11) SAT search with proven start-order symmetry.

Load the pinned exact event encoding, normalize the first row by common symbol
relabeling, then reorder remaining rows so row r starts with r. This is safe:
every T1 table has each symbol exactly once in its first column. Add redundant
end-symbol uniqueness for propagation. SAT rows require independent checking;
UNKNOWN and unverified UNSAT establish no nonexistence.
"""
import hashlib
import importlib.util
import json
import subprocess
import sys
import time
from pathlib import Path

helper_path=Path(__file__).with_name('frontier-20261028-tuscan-sat-v1.py')
spec=importlib.util.spec_from_file_location('base_tuscan_sat',helper_path)
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
N=h.N


def main(argv):
    if len(argv)!=5:
        raise ValueError('usage: SCRIPT OUTPUT.json OUTPUT.cnf SECONDS SEED')
    out_path,cnf_path=Path(argv[1]),Path(argv[2])
    seconds,seed=int(argv[3]),int(argv[4])
    if not 1<=seconds<=600 or not 0<=seed<=2147483647:
        raise ValueError('invalid limits')
    started=time.monotonic()
    formula=h.build('full',None,set())
    for r in range(N):
        formula.add(h.xvar(r,0,r))
    for a in range(N):
        values=[h.xvar(r,N-1,a) for r in range(N)]
        formula.add(*values)
        formula.pairwise_amo(values)
    with out_path.open('x',encoding='utf-8') as out, cnf_path.open('x',encoding='ascii') as cnf:
        cnf.write(f'p cnf {formula.variables} {len(formula.clauses)}\n')
        for clause in formula.clauses:
            cnf.write(' '.join(map(str,clause))+' 0\n')
        cnf.flush()
        construction_ms=round((time.monotonic()-started)*1000)
        command=['kissat','--sat',f'--time={seconds}',f'--seed={seed}',str(cnf_path)]
        solving=time.monotonic()
        try:
            proc=subprocess.run(command,capture_output=True,text=True,timeout=seconds+15,check=False)
            rc,stdout,stderr,timeout=proc.returncode,proc.stdout,proc.stderr,False
        except subprocess.TimeoutExpired as exc:
            rc=None
            stdout=exc.stdout.decode() if isinstance(exc.stdout,bytes) else (exc.stdout or '')
            stderr=exc.stderr.decode() if isinstance(exc.stderr,bytes) else (exc.stderr or '')
            timeout=True
        solve_ms=round((time.monotonic()-solving)*1000)
        if rc==10 and 's SATISFIABLE' in stdout:
            status='sat'
        elif rc==20 and 's UNSATISFIABLE' in stdout:
            status='unsat_unverified'
        elif rc in (0,None):
            status='unknown'
        else:
            status='solver_error'
        result={'kind':'bounded_kissat_canonical_actual_tuscan2',
                'helper_source_sha256':hashlib.sha256(helper_path.read_bytes()).hexdigest(),
                'cnf_file':str(cnf_path),'cnf_sha256':hashlib.sha256(cnf_path.read_bytes()).hexdigest(),
                'variables':formula.variables,'clauses':len(formula.clauses),
                'solver_command':command,'solver_returncode':rc,'solver_status':status,
                'supervisory_timeout':timeout,'construction_ms':construction_ms,'solve_ms':solve_ms,
                'normalization':'row 0 equals 0..10 by common relabel; row r starts with r by reordering the unique starts',
                'added_redundant_necessary_conditions':'every symbol occurs exactly once in final column',
                'scope':'No column-Latin or cyclic assumption. UNKNOWN is not nonexistence; UNSAT requires verified proof and encoding audit.',
                'solver_stdout':stdout,'solver_stderr':stderr}
        if status=='sat':
            assigned=set()
            for line in stdout.splitlines():
                if line.startswith('v '):
                    assigned.update(int(x) for x in line.split()[1:] if int(x)>0)
            rows=[]
            for r in range(N):
                row=[]
                for c in range(N):
                    selected=[a for a in range(N) if h.xvar(r,c,a) in assigned]
                    if len(selected)!=1:
                        raise AssertionError('solver output lacks a unique symbol')
                    row.append(selected[0])
                rows.append(row)
            result.update({'rows':rows,'zero_score_claim':True,'best_pair_collision_score':0,
                           'd1_pair_collisions':0,'d2_pair_collisions':0,
                           'd1_excess_events':0,'d2_excess_events':0})
        json.dump(result,out,indent=2,sort_keys=True)
        out.write('\n')
    print(json.dumps({'status':status,'returncode':rc,'construction_ms':construction_ms,
                      'solve_ms':solve_ms,'variables':formula.variables,'clauses':len(formula.clauses),
                      'output':str(out_path),'cnf_sha256':result['cnf_sha256']}))
    if status=='solver_error':
        raise SystemExit('solver failure recorded')


if __name__=='__main__':
    main(sys.argv)
