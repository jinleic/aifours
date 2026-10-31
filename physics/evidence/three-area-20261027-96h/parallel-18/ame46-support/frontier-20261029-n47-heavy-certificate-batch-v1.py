#!/usr/bin/env python3
"""Bounded finite research certificate batch for cases1..12 of N47/r4444.

Each instance is generated from a frozen encoder; CaDiCaL runs with --plain,
textual LRAT and its own 60s time limit. Complete on-disk CNF/proof bytes are
intentionally retained and checked by the separate strict RUP checker, through
EOF, with hashes. A checked UNSAT result is exact-CNF only: encoder soundness and
mathematical type coverage need independent review. No global theorem claim.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import signal
import subprocess
import time


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('checker',type=Path);ap.add_argument('root',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    enc=load('n47encoder',a.encoder);chk=load('rupchecker',a.checker);solver=Path(shutil.which('cadical'));solver_hash=sha(solver)
    encoder_hash=sha(a.encoder);checker_hash=sha(a.checker);records=[]
    stopped=[False]
    def request_stop(signum,frame):stopped[0]=True
    signal.signal(signal.SIGTERM,request_stop)
    signal.signal(signal.SIGINT,request_stop)
    for case in range(1,13):
        if stopped[0]:raise SystemExit('STOPPED before next launch; no further certificate acceptance')
        prefix=a.root/f'n47-heavy-case{case:02d}';cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');log=Path(str(prefix)+'.cadical.log')
        receipt=Path(str(prefix)+'.rup-check-v2.json')
        if any(p.exists() for p in (cnf,proof,log,receipt)):raise ValueError(f'case{case} output already exists')
        typ=enc.cases()[case];en,E=enc.encode(typ,True)
        with cnf.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
        cnf_hash=sha(cnf);start=time.monotonic()
        with log.open('xb') as f:
            child=subprocess.Popen([str(solver),'--plain','--lrat','--no-binary','-t','60',str(cnf),str(proof)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                forwarded=False
                while child.poll() is None:
                    if stopped[0] and not forwarded:
                        child.terminate();forwarded=True
                    time.sleep(0.02)
                rc=child.wait()
            finally:
                if child.poll() is None:child.terminate()
                child.wait()
        if stopped[0]:raise SystemExit('STOPPED; owned child reaped, certificate not accepted')
        seconds=time.monotonic()-start
        text=log.read_text();status=[line.removesuffix('\r') for line in text.split('\n') if line.startswith('s ')]
        record={'case':case,'types':typ,'solver_rc':rc,'solver_status_lines':status,'elapsed_monotonic_seconds':seconds,
          'cnf_sha256_before':cnf_hash,'cnf_sha256_after':sha(cnf),'solver_sha256_before':solver_hash,'solver_sha256_after':sha(solver),
          'solver_log_sha256':sha(log),'cnf_variables':en.n,'cnf_clauses':len(en.C)}
        if record['cnf_sha256_after']!=cnf_hash or record['solver_sha256_after']!=solver_hash:raise ValueError('input/binary changed')
        if rc==20 and status==['s UNSATISFIABLE']:
            C=cnf.read_bytes();P=proof.read_bytes();verdict=chk.verify(C,P)
            verdict.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),'cnf_bytes':len(C),
              'proof_sha256':hashlib.sha256(P).hexdigest(),'proof_bytes':len(P),'checker_sha256':checker_hash,
              'encoder_sha256':encoder_hash,'scope':'Exact-CNF certificate only; no encoder or mathematical coverage acceptance.'})
            with receipt.open('x',encoding='utf-8') as f:json.dump(verdict,f,indent=2);f.write('\n')
            record['proof_sha256']=verdict['proof_sha256'];record['checker_receipt_sha256']=sha(receipt);record['checked_status']='VERIFIED'
        else:
            record['checked_status']='UNKNOWN_OR_NON_UNSAT'
        records.append(record);print(json.dumps(record),flush=True)
    result={'encoder_sha256':encoder_hash,'checker_sha256':checker_hash,'solver_sha256':solver_hash,'cases':records,
      'scope':'Finite pinned-formula certificate batch; no mathematical theorem or normal-form claim.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')


if __name__=='__main__':main()
