#!/usr/bin/env python3
"""t=28 (n=8) certificate batch for a general total support N=28+size.

Uses general(enc,deg,8,size,cap,joint=True) of the encoder-controls v2 file,
whose cap4/size20 output is clause-identical to the frozen N48/t28 encoder.
The five profile/degree cases depend only on (t,n), so they are the same for
every N with t=28. cap must be >= 2+(size-16) to be implied by the pair
partition alone. CaDiCaL --plain textual LRAT; RUP check through EOF.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import time


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('controls',type=Path);ap.add_argument('batch',type=Path);ap.add_argument('checker',type=Path)
    ap.add_argument('root',type=Path);ap.add_argument('out',type=Path);ap.add_argument('--size',type=int,required=True);ap.add_argument('--cap',type=int,required=True)
    ap.add_argument('--seconds',type=int,default=1800);a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    if a.cap<2+(a.size-16):raise ValueError('cap smaller than the pair-partition bound')
    enc=load('enc',a.encoder);ctl=load('ctl',a.controls);bat=load('bat',a.batch);chk=load('chk',a.checker);solver=Path(shutil.which('cadical'))
    hashes={k:sha(v) for k,v in (('encoder',a.encoder),('controls',a.controls),('batch_cases',a.batch),('checker',a.checker),('solver',solver))};records=[]
    for name,deg in bat.CASES:
        prefix=a.root/f'N{28+a.size}-t28-cap{a.cap}-{name}-P';cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');log=Path(str(prefix)+'.cadical.log');receipt=Path(str(prefix)+'.rup-check.json')
        if any(p.exists() for p in (cnf,proof,log,receipt)):raise ValueError('exists')
        en,E,P=ctl.general(enc,[tuple(D) for D in deg],8,a.size,a.cap,True)
        with cnf.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
        h=sha(cnf);start=time.monotonic()
        with log.open('xb') as f:rc=subprocess.run([str(solver),'--plain','--lrat','--no-binary','-t',str(a.seconds),str(cnf),str(proof)],stdout=f,stderr=subprocess.STDOUT).returncode
        status=[l for l in log.read_text().split('\n') if l.startswith('s ')]
        rec={'N':28+a.size,'case':name,'degrees':[list(D) for D in deg],'size':a.size,'cap':a.cap,'rc':rc,'status':status,'seconds':time.monotonic()-start,'cnf_sha256':h,'variables':en.n,'clauses':len(en.C)}
        if sha(cnf)!=h:raise ValueError('cnf changed')
        if rc==20 and status==['s UNSATISFIABLE']:
            C=cnf.read_bytes();Pf=proof.read_bytes();v=chk.verify(C,Pf)
            v.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),'proof_sha256':hashlib.sha256(Pf).hexdigest(),'hashes':hashes})
            with receipt.open('x',encoding='utf-8') as f:json.dump(v,f,indent=2);f.write('\n')
            rec.update({'checked':'VERIFIED_UNSAT','proof_sha256':v['proof_sha256'],'receipt_sha256':sha(receipt)})
        else:rec['checked']='NOT_UNSAT_CERTIFIED'
        records.append(rec);print(json.dumps(rec),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'hashes':hashes,'size':a.size,'cap':a.cap,'cases':records},f,indent=2);f.write('\n')


if __name__=='__main__':main()
