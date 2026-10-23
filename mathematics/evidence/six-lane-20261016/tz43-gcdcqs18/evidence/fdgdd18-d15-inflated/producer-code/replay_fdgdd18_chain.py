#!/usr/bin/env python3
"""Resolve the pinned bare H(5,6,4,3) KM CNF (seed0), then rerun both inflated-frame SAT solves (seed1).
Every file/directory is new. The old producer independently checks the master CNF hash, actual SAT model,
bare-design triple coverage and the complete final certificate. Require the final bytes to equal the pin.
Usage: replay_fdgdd18_chain.py PINNED_MASTER_INPUT_DIR NEW_OUTDIR PINNED_FDGDD_CERT
"""
import lane_guard  # noqa: F401
import hashlib
import json
import os
import subprocess
import sys
from lane_guard import xopen
from lanelib import parse_status, model_satisfies


def main():
    source,out,pin=sys.argv[1:4]
    os.mkdir(out)
    inputs=os.path.join(out,'master-inputs');os.mkdir(inputs)
    cnfdata=open(os.path.join(source,'model.cnf'),'rb').read()
    sha=hashlib.sha256(cnfdata).hexdigest()
    meta=json.load(open(os.path.join(source,'summary.json')))
    assert sha==meta['cnf_sha256'] and meta['group']=='D15' and meta['km_only']==1
    cnf=os.path.join(inputs,'model.cnf')
    with xopen(cnf,'xb') as fh:fh.write(cnfdata)
    run=subprocess.run(['kissat','-q','--time=60','--seed=0',cnf],capture_output=True,text=True)
    with xopen(cnf+'.log') as fh:fh.write(run.stdout)
    st,model=parse_status(run.stdout)
    assert st=='SAT' and model_satisfies(cnf,model), 'bare master re-solve failed'
    with xopen(os.path.join(inputs,'summary.json')) as fh:json.dump(meta,fh,indent=1)
    assembly=os.path.join(out,'assembly')
    cmd=[sys.executable,os.path.join(os.path.dirname(__file__),'inflate_h6_frames.py'),
         'FD','D15',inputs,assembly,'60','1']
    run=subprocess.run(cmd,capture_output=True,text=True)
    with xopen(os.path.join(out,'producer.stdout.txt')) as fh:fh.write(run.stdout)
    with xopen(os.path.join(out,'producer.stderr.txt')) as fh:fh.write(run.stderr)
    assert run.returncode==0, 'inflation/frame producer failed'
    cert=os.path.join(assembly,'fdgdd_5_18_inflated_D15.txt')
    expected=open(pin,'rb').read();actual=open(cert,'rb').read()
    assert actual==expected,'full solver-chain replay changed raw bytes'
    rec={'master_cnf_sha256':sha,'master_model_re_solved':True,'master_seed':0,'frame_seed':1,
         'certificate':cert,'certificate_sha256':hashlib.sha256(actual).hexdigest(),
         'byte_identical':True,'source_pin':pin,'producer_summary':os.path.join(assembly,'summary.json')}
    with xopen(os.path.join(out,'chain-replay.json')) as fh:json.dump(rec,fh,indent=1)
    print(json.dumps(rec))


if __name__=='__main__':main()
