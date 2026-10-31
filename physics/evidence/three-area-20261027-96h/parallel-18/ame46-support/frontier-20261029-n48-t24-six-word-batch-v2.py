#!/usr/bin/env python3
"""Certificate sweep v2: any N48/t24 residual profile, optionally with the P code.

v2 differs from v1 only by: all nine profiles with sizes in3..5 and pairwise
products>=12 are available, an optional --joint-P flag, and a tag suffix. For each
chosen zero-excess residual profile (party0
first in ascending size; party permutations are NOT used to merge cases) all
sorted per-party degree vectors with entries2..min partner size and sum12 are
enumerated. Each CNF (frozen encoder, flags recorded) is solved by CaDiCaL with
--plain textual LRAT; UNSAT proofs are checked through EOF by the separate RUP
checker; SAT models are decoded by the separate exact decoder. A checked UNSAT
certifies the exact CNF only, not encoder soundness or the written lemmas.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import shutil
import signal
import subprocess
import time

PROFILES={'3444':(3,4,4,4),'3445':(3,4,4,5),'3455':(3,4,5,5),'3555':(3,5,5,5),'4444':(4,4,4,4),'4445':(4,4,4,5),'4455':(4,4,5,5),'4555':(4,5,5,5),'5555':(5,5,5,5)}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m


def degree_vectors(r,cap):
    return [D for D in itertools.combinations_with_replacement(range(2,cap+1),r) if sum(D)==12]


def cases(profiles):
    out=[]
    for name in profiles:
        sizes=PROFILES[name];lists=[]
        for i,r in enumerate(sizes):
            cap=min(sizes[j] for j in range(4) if j!=i);lists.append(degree_vectors(r,cap))
        for combo in itertools.product(*lists):out.append((name,combo))
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('checker',type=Path);ap.add_argument('decoder',type=Path);ap.add_argument('phase_engine',type=Path)
    ap.add_argument('root',type=Path);ap.add_argument('out',type=Path);ap.add_argument('--profiles',default='3555,4455,4555,5555');ap.add_argument('--seconds',type=int,default=600)
    ap.add_argument('--no-H1',action='store_true');ap.add_argument('--six',action='store_true');ap.add_argument('--joint-P',action='store_true');ap.add_argument('--tag',default='');a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    enc=load('enc',a.encoder);chk=load('chk',a.checker);solver=Path(shutil.which('cadical'));hashes={'encoder':sha(a.encoder),'base_encoder':sha(enc.BASE_ENCODER),
      'checker':sha(a.checker),'decoder':sha(a.decoder),'phase_engine':sha(a.phase_engine),'solver':sha(solver)}
    stopped=[False]
    def stop(signum,frame):stopped[0]=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    todo=cases(a.profiles.split(','));records=[]
    for idx,(name,deg) in enumerate(todo):
        if stopped[0]:raise SystemExit('STOPPED before next launch')
        tag=f"{name}-"+'_'.join(''.join(map(str,D)) for D in deg)+a.tag;prefix=a.root/tag
        cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');log=Path(str(prefix)+'.cadical.log');receipt=Path(str(prefix)+'.rup-check.json')
        if any(p.exists() for p in (cnf,proof,log,receipt)):raise ValueError(f'{tag} output exists')
        en,E,P,info=enc.encode([tuple(D) for D in deg],a.no_H1,a.six,a.joint_P)
        with cnf.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
        meta={'degrees':[list(D) for D in deg],'no_H1_imposed':a.no_H1,'six_word_lemma_clauses':info['six_word_clauses'],'joint_P':a.joint_P,'variables':en.n,'clauses':len(en.C)}
        metapath=Path(str(prefix)+'.cnf.meta.json')
        with metapath.open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
        cnf_hash=sha(cnf);start=time.monotonic()
        with log.open('xb') as f:
            child=subprocess.Popen([str(solver),'--plain','--lrat','--no-binary','-t',str(a.seconds),str(cnf),str(proof)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                forwarded=False
                while child.poll() is None:
                    if stopped[0] and not forwarded:child.terminate();forwarded=True
                    time.sleep(0.05)
                rc=child.wait()
            finally:
                if child.poll() is None:child.terminate()
                child.wait()
        if stopped[0]:raise SystemExit('STOPPED; child reaped; no acceptance')
        status=[line for line in log.read_text().split('\n') if line.startswith('s ')]
        rec={'index':idx,'profile':name,'degrees':meta['degrees'],'tag':tag,'solver_rc':rc,'status_lines':status,'seconds':time.monotonic()-start,
          'cnf_sha256':cnf_hash,'cnf_unchanged':sha(cnf)==cnf_hash,'variables':en.n,'clauses':len(en.C),'log_sha256':sha(log)}
        if not rec['cnf_unchanged'] or sha(solver)!=hashes['solver']:raise ValueError('input or solver changed')
        if rc==20 and status==['s UNSATISFIABLE']:
            C=cnf.read_bytes();Pf=proof.read_bytes();verdict=chk.verify(C,Pf)
            verdict.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),'proof_sha256':hashlib.sha256(Pf).hexdigest(),'proof_bytes':len(Pf),
              'hashes':hashes,'scope':'Exact-CNF certificate only.'})
            with receipt.open('x',encoding='utf-8') as f:json.dump(verdict,f,indent=2);f.write('\n')
            rec.update({'checked':'VERIFIED_UNSAT','proof_sha256':verdict['proof_sha256'],'receipt_sha256':sha(receipt)})
            proof_keep=True
        elif rc==10:
            dec=Path(str(prefix)+'.decoded.json')
            r=subprocess.run(['python3','-B',str(a.decoder),str(metapath),str(log),str(a.phase_engine),str(dec)],capture_output=True,text=True)
            rec.update({'checked':'SAT_MODEL_DECODED' if r.returncode==0 else 'SAT_DECODE_FAILED','decoder_rc':r.returncode,'decoder_stderr_tail':r.stderr[-400:]})
            if r.returncode==0:rec['decoded_sha256']=sha(dec)
        else:rec['checked']='UNKNOWN'
        records.append(rec);print(json.dumps(rec),flush=True)
    result={'hashes':hashes,'flags':{'no_H1':a.no_H1,'six':a.six,'joint_P':a.joint_P,'seconds':a.seconds,'profiles':a.profiles},'cases':records,'scope':'Finite pinned-formula sweep; mathematical coverage needs written review.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')


if __name__=='__main__':main()
