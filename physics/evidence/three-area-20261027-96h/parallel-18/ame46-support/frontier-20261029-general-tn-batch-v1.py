#!/usr/bin/env python3
"""Programmatic-coverage certificate batch for one (N,t) with the P code.

Cases are generated here, not hand-listed: sorted alphabet profiles r_i in
[2,min(6,n//2)] with pairwise products>=n and nonnegative activity residue
sum_{i<j}(r_i r_j-n)-sum_i(6r_i-n)+t; then every ORDERED choice of sorted
per-party degree vectors with entries in [2,min_{j!=i} r_j] summing to n.
Each case: general(enc,deg,n,N-t,cap,joint=True) from encoder-controls v2
(unique-overlap rule, pair partition, partner degrees, P exact cover; cap is the
multiplicity cap and must be >=2+(N-t-2n)). CaDiCaL --plain LRAT + RUP check.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import shutil
import subprocess
import time


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def cases(t,n):
    n_max=min(6,n//2);out=[]
    for prof in itertools.combinations_with_replacement(range(2,n_max+1),4):
        if any(prof[i]*prof[j]<n for i,j in itertools.combinations(range(4),2)):continue
        resid=sum(prof[i]*prof[j]-n for i,j in itertools.combinations(range(4),2))-sum(6*r-n for r in prof)+t
        if resid<0:continue
        lists=[]
        for i,r in enumerate(prof):
            cap=min(prof[j] for j in range(4) if j!=i)
            lists.append([D for D in itertools.combinations_with_replacement(range(2,cap+1),r) if sum(D)==n])
        for combo in itertools.product(*lists):out.append((''.join(map(str,prof)),combo,resid))
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('controls',type=Path);ap.add_argument('checker',type=Path);ap.add_argument('root',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--N',type=int,required=True);ap.add_argument('--t',type=int,required=True);ap.add_argument('--cap',type=int,required=True);ap.add_argument('--seconds',type=int,default=1800)
    ap.add_argument('--list-only',action='store_true');a=ap.parse_args()
    n=36-a.t;size=a.N-a.t
    if size<2*n or a.cap<2+(size-2*n):raise ValueError('support/cap inconsistent with pair partition')
    todo=cases(a.t,n)
    if a.list_only:
        print(json.dumps([{'profile':p,'degrees':d,'activity_residue':r} for p,d,r in todo]));print(len(todo));return
    if a.out.exists():raise SystemExit('output exists')
    enc=load('enc',a.encoder);ctl=load('ctl',a.controls);chk=load('chk',a.checker);solver=Path(shutil.which('cadical'))
    hashes={k:sha(v) for k,v in (('encoder',a.encoder),('controls',a.controls),('checker',a.checker),('solver',solver),('driver',Path(__file__)))};records=[]
    for idx,(prof,deg,resid) in enumerate(todo):
        tag=f'N{a.N}-t{a.t}-cap{a.cap}-{prof}-'+'_'.join(''.join(map(str,D)) for D in deg);prefix=a.root/tag
        cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');log=Path(str(prefix)+'.cadical.log');receipt=Path(str(prefix)+'.rup-check.json')
        if any(p.exists() for p in (cnf,proof,log,receipt)):raise ValueError('exists '+tag)
        en,E,P=ctl.general(enc,[tuple(D) for D in deg],n,size,a.cap,True)
        with cnf.open('x',encoding='ascii') as f:
            f.write(f'p cnf {en.n} {len(en.C)}\n')
            for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
        h=sha(cnf);start=time.monotonic()
        with log.open('xb') as f:rc=subprocess.run([str(solver),'--plain','--lrat','--no-binary','-t',str(a.seconds),str(cnf),str(proof)],stdout=f,stderr=subprocess.STDOUT).returncode
        status=[l for l in log.read_text().split('\n') if l.startswith('s ')]
        rec={'index':idx,'N':a.N,'t':a.t,'profile':prof,'degrees':[list(D) for D in deg],'activity_residue':resid,'cap':a.cap,'rc':rc,'status':status,'seconds':time.monotonic()-start,'cnf_sha256':h,'variables':en.n,'clauses':len(en.C)}
        if sha(cnf)!=h:raise ValueError('cnf changed')
        if rc==20 and status==['s UNSATISFIABLE']:
            C=cnf.read_bytes();Pf=proof.read_bytes();v=chk.verify(C,Pf)
            v.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),'proof_sha256':hashlib.sha256(Pf).hexdigest(),'hashes':hashes})
            with receipt.open('x',encoding='utf-8') as f:json.dump(v,f,indent=2);f.write('\n')
            rec.update({'checked':'VERIFIED_UNSAT','proof_sha256':v['proof_sha256'],'receipt_sha256':sha(receipt)})
        else:rec['checked']='NOT_UNSAT_CERTIFIED'
        records.append(rec);print(json.dumps(rec),flush=True)
    with a.out.open('x',encoding='utf-8') as f:json.dump({'hashes':hashes,'N':a.N,'t':a.t,'cap':a.cap,'cases':records},f,indent=2);f.write('\n')


if __name__=='__main__':main()
