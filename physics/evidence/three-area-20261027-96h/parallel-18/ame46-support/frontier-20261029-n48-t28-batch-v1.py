#!/usr/bin/env python3
"""Certificate batch for all five N48/t28 profile/degree cases.

Cases (party0 smallest; no party-permutation merging): 4444|2222^4;
3444|(224 or 233),2222^3; 3344|233,233,2222,2222; 2444|44,2222^3. Each CNF is
built by the frozen t28 encoder (flag --joint-P recorded), solved by CaDiCaL
--plain textual LRAT, and UNSAT proofs are checked through EOF by the separate
RUP checker. SAT outcomes are only recorded, never called witnesses here.
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

CASES=[('4444',((2,2,2,2),)*4),('3444a',((2,2,4),)+((2,2,2,2),)*3),('3444b',((2,3,3),)+((2,2,2,2),)*3),
 ('3344',((2,3,3),(2,3,3),(2,2,2,2),(2,2,2,2))),('2444',((4,4),)+((2,2,2,2),)*3)]


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('checker',type=Path);ap.add_argument('root',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--joint-P',action='store_true');ap.add_argument('--seconds',type=int,default=900);a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    enc=load('enc',a.encoder);chk=load('chk',a.checker);solver=Path(shutil.which('cadical'))
    hashes={'encoder':sha(a.encoder),'base_encoder':sha(enc.BASE_ENCODER),'checker':sha(a.checker),'solver':sha(solver)}
    stopped=[False]
    def stop(signum,frame):stopped[0]=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop);records=[]
    for name,deg in CASES:
        if stopped[0]:raise SystemExit('STOPPED')
        for i,D in enumerate(deg):
            if sum(D)!=8 or min(D)<2 or max(D)>min(len(deg[j]) for j in range(4) if j!=i):raise ValueError('case list')
        tag=f't28-{name}'+('-P' if a.joint_P else '');prefix=a.root/tag
        cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');log=Path(str(prefix)+'.cadical.log');receipt=Path(str(prefix)+'.rup-check.json')
        if any(p.exists() for p in (cnf,proof,log,receipt)):raise ValueError('exists')
        en,E,P=enc.encode([tuple(D) for D in deg],a.joint_P)
        with cnf.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
        h=sha(cnf);start=time.monotonic()
        with log.open('xb') as f:
            child=subprocess.Popen([str(solver),'--plain','--lrat','--no-binary','-t',str(a.seconds),str(cnf),str(proof)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                sent=False
                while child.poll() is None:
                    if stopped[0] and not sent:child.terminate();sent=True
                    time.sleep(0.05)
                rc=child.wait()
            finally:
                if child.poll() is None:child.terminate()
                child.wait()
        if stopped[0]:raise SystemExit('STOPPED; reaped')
        status=[l for l in log.read_text().split('\n') if l.startswith('s ')]
        rec={'case':name,'degrees':[list(D) for D in deg],'joint_P':a.joint_P,'rc':rc,'status':status,'seconds':time.monotonic()-start,'cnf_sha256':h,'cnf_unchanged':sha(cnf)==h,
          'variables':en.n,'clauses':len(en.C)}
        if not rec['cnf_unchanged'] or sha(solver)!=hashes['solver']:raise ValueError('changed')
        if rc==20 and status==['s UNSATISFIABLE']:
            C=cnf.read_bytes();Pf=proof.read_bytes();v=chk.verify(C,Pf)
            v.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),'proof_sha256':hashlib.sha256(Pf).hexdigest(),'hashes':hashes,'scope':'Exact-CNF certificate only.'})
            with receipt.open('x',encoding='utf-8') as f:json.dump(v,f,indent=2);f.write('\n')
            rec.update({'checked':'VERIFIED_UNSAT','proof_sha256':v['proof_sha256'],'receipt_sha256':sha(receipt)})
        else:rec['checked']='NOT_UNSAT_CERTIFIED'
        records.append(rec);print(json.dumps(rec),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'hashes':hashes,'cases':records,'scope':'Pinned-formula certificates; coverage/encoder soundness need written review.'},f,indent=2);f.write('\n')


if __name__=='__main__':main()
