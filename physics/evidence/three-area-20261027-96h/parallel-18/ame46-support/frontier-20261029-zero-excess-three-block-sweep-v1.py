#!/usr/bin/env python3
"""Zero-excess (N=72-t) sweep with the three-block lemma, no no-Hamming-one.

Cases: cases(t,n) of frontier-20261029-general-tn-batch-v1.py (n=36-t). With
--party-symmetric, ordered degree choices are reduced by requiring the degree
vectors of EQUAL-SIZE parties to be lexicographically non-decreasing in party
order; this is complete because permuting parties maps every constraint family
(fibers, pair counts, cut closure, three-block sets, P exact cover) to itself.
Each case: frontier-20261029-three-block-cnf-v1.py encode(deg,no_h1=False,
joint=--joint-P). CaDiCaL --plain textual LRAT + RUP check; SAT models decoded.
Shard k of m takes the k-th residue class of the (reduced) case index.
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


def reduced(cases):
    out=[]
    for prof,deg,resid in cases:
        sizes=[int(c) for c in prof];ok=True
        for i in range(4):
            for j in range(i+1,4):
                if sizes[i]==sizes[j] and tuple(deg[i])>tuple(deg[j]):ok=False
        if ok:out.append((prof,deg,resid))
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('cases_src',type=Path);ap.add_argument('checker',type=Path);ap.add_argument('decoder',type=Path);ap.add_argument('phase_engine',type=Path)
    ap.add_argument('root',type=Path);ap.add_argument('out',type=Path);ap.add_argument('--t',type=int,required=True);ap.add_argument('--shard',type=int,default=0);ap.add_argument('--nshards',type=int,default=1)
    ap.add_argument('--joint-P',action='store_true');ap.add_argument('--party-symmetric',action='store_true');ap.add_argument('--seconds',type=int,default=3600);ap.add_argument('--list-only',action='store_true');a=ap.parse_args()
    n=36-a.t;gtn=load('gtn',a.cases_src);allc=gtn.cases(a.t,n)
    if a.party_symmetric:allc=reduced(allc)
    if a.list_only:print(len(allc));return
    if a.out.exists():raise SystemExit('output exists')
    enc=load('tb',a.encoder);chk=load('chk',a.checker);solver=Path(shutil.which('cadical'))
    hashes={k:sha(v) for k,v in (('encoder',a.encoder),('six_encoder',enc.SIX),('cases_src',a.cases_src),('checker',a.checker),('decoder',a.decoder),('phase_engine',a.phase_engine),('solver',solver),('driver',Path(__file__)))};records=[]
    for idx,(prof,deg,resid) in enumerate(allc):
        if idx%a.nshards!=a.shard:continue
        tag=f'z{a.t}-{prof}-'+'_'.join(''.join(map(str,D)) for D in deg)+('-P' if a.joint_P else '');prefix=a.root/tag
        cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');log=Path(str(prefix)+'.cadical.log');receipt=Path(str(prefix)+'.rup-check.json')
        if any(p.exists() for p in (cnf,proof,log,receipt)):raise ValueError('exists '+tag)
        en,E,P,info=enc.encode([tuple(D) for D in deg],False,a.joint_P)
        with cnf.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
        meta={'t':a.t,'n':n,'degrees':[list(D) for D in deg],'no_H1_imposed':False,'three_block_clauses':info['three_block_clauses'],'joint_P':a.joint_P,'variables':en.n,'clauses':len(en.C)}
        metapath=Path(str(prefix)+'.cnf.meta.json')
        with metapath.open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
        h=sha(cnf);start=time.monotonic()
        with log.open('xb') as f:rc=subprocess.run([str(solver),'--plain','--lrat','--no-binary','-t',str(a.seconds),str(cnf),str(proof)],stdout=f,stderr=subprocess.STDOUT).returncode
        status=[l for l in log.read_text().split('\n') if l.startswith('s ')]
        rec={'index':idx,'t':a.t,'profile':prof,'degrees':meta['degrees'],'activity_residue':resid,'tag':tag,'joint_P':a.joint_P,'rc':rc,'status':status,'seconds':time.monotonic()-start,'cnf_sha256':h,'variables':en.n,'clauses':len(en.C)}
        if sha(cnf)!=h:raise ValueError('cnf changed')
        if rc==20 and status==['s UNSATISFIABLE']:
            C=cnf.read_bytes();Pf=proof.read_bytes();v=chk.verify(C,Pf)
            v.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),'proof_sha256':hashlib.sha256(Pf).hexdigest(),'hashes':hashes})
            with receipt.open('x',encoding='utf-8') as f:json.dump(v,f,indent=2);f.write('\n')
            rec.update({'checked':'VERIFIED_UNSAT','proof_sha256':v['proof_sha256'],'receipt_sha256':sha(receipt)})
        elif rc==10:
            dec=Path(str(prefix)+'.decoded.json')
            r=subprocess.run(['python3','-B',str(a.decoder),str(metapath),str(log),str(a.phase_engine),str(dec)],capture_output=True,text=True)
            rec.update({'checked':'SAT_MODEL_DECODED' if r.returncode==0 else 'SAT_DECODE_FAILED','decoder_rc':r.returncode,'decoder_stdout_tail':r.stdout[-800:],'decoder_stderr_tail':r.stderr[-400:]})
        else:rec['checked']='UNKNOWN'
        records.append(rec);print(json.dumps(rec),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'hashes':hashes,'t':a.t,'shard':a.shard,'nshards':a.nshards,'joint_P':a.joint_P,'party_symmetric':a.party_symmetric,'cases':records},f,indent=2);f.write('\n')


if __name__=='__main__':main()
