#!/usr/bin/env python3
"""Run bounded CaDiCaL on the pinned canonical unrestricted T2 CNF.

No unverified UNSAT or timeout is a nonexistence result. A decoded SAT model
must be independently checked on its actual 11x11 linear rows.
"""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

N=11
EXPECTED='37fe829737eb1cb0550304dbb962b96cc7e4c937c6a3bee425d5fd9a0800d22c'

def xvar(r,c,s):
    return 1+(r*N+c)*N+s


def main(argv):
    if len(argv)!=4:
        raise ValueError('usage: SCRIPT PINNED.cnf OUTPUT.json SECONDS')
    cnf,output=Path(argv[1]),Path(argv[2]); seconds=int(argv[3])
    if not 1<=seconds<=600:
        raise ValueError('invalid time limit')
    digest=hashlib.sha256(cnf.read_bytes()).hexdigest()
    if digest!=EXPECTED:
        raise ValueError('canonical CNF bytes differ from pinned input')
    command=['cadical','--sat','-t',str(seconds),str(cnf)]
    start=time.monotonic()
    try:
        proc=subprocess.run(command,capture_output=True,text=True,timeout=seconds+15,check=False)
        rc,stdout,stderr,timeout=proc.returncode,proc.stdout,proc.stderr,False
    except subprocess.TimeoutExpired as exc:
        rc=None
        stdout=exc.stdout.decode() if isinstance(exc.stdout,bytes) else (exc.stdout or '')
        stderr=exc.stderr.decode() if isinstance(exc.stderr,bytes) else (exc.stderr or '')
        timeout=True
    status=('sat' if rc==10 and 's SATISFIABLE' in stdout else
            'unsat_unverified' if rc==20 and 's UNSATISFIABLE' in stdout else
            'unknown' if rc in (0,None) else 'solver_error')
    result={'kind':'bounded_cadical_canonical_tuscan2','cnf_sha256':digest,'command':command,
            'returncode':rc,'status':status,'supervisory_timeout':timeout,
            'elapsed_ms':round((time.monotonic()-start)*1000),'solver_stdout':stdout,'solver_stderr':stderr,
            'scope':'No Latin column or wrapped event assumption. UNKNOWN is not nonexistence; UNSAT requires checked proof and encoding audit.'}
    if status=='sat':
        assigned={int(v) for line in stdout.splitlines() if line.startswith('v ')
                  for v in line.split()[1:] if int(v)>0}
        rows=[]
        for r in range(N):
            row=[]
            for c in range(N):
                selected=[a for a in range(N) if xvar(r,c,a) in assigned]
                if len(selected)!=1:
                    raise AssertionError('model lacks a unique row symbol')
                row.append(selected[0])
            rows.append(row)
        result.update({'rows':rows,'zero_score_claim':True,'best_pair_collision_score':0,
                       'd1_pair_collisions':0,'d2_pair_collisions':0,'d1_excess_events':0,'d2_excess_events':0})
    with output.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps({key:result[key] for key in ('status','returncode','supervisory_timeout','elapsed_ms','cnf_sha256')}))
    if status=='solver_error':
        raise SystemExit('solver failure recorded')


if __name__=='__main__':
    main(sys.argv)
