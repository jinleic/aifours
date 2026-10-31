#!/usr/bin/env python3
"""Real-data shadow smoke: fresh hardlinks to an immutable data seal.

The baseline, missing, changed and unlisted variants are constructed NEW.
No existing file is changed, unlinked or deleted. A changed file is a fresh
standalone copy, NEVER an edited hardlink. The program/runtime stay at the
real owner root; only the explicit evidence root changes.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PROGRAM='frontier-20261029-level7-free-endomorphism-union-check.py'
INVENTORY='frontier-20261029-level7-free19-input-inventory-v1.json'
INVENTORY_SHA='88971535369069479adfbfd1cb1e6a3996f06f598b779777bb73624a87459ab0'
SEAL=ROOT/'frontier-20261029-level7-free19-sealed-inputs-v1'


def new_file(path,data):
    with path.open('xb') as stream:stream.write(data)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--canonical',required=True);ap.add_argument('--canonical-sha256',required=True)
    args=ap.parse_args();canonical_path=Path(args.canonical).resolve()
    assert canonical_path.parent==ROOT
    canonical_raw=canonical_path.read_bytes();assert hashlib.sha256(canonical_raw).hexdigest()==args.canonical_sha256
    canonical=json.loads(canonical_raw)
    inv_raw=(SEAL/INVENTORY).read_bytes();assert hashlib.sha256(inv_raw).hexdigest()==INVENTORY_SHA
    I=json.loads(inv_raw);pins=I['files'];missing_name=pins[0]['file']
    controls=ROOT/'free19-shadow-controls-v1';controls.mkdir(exist_ok=False)
    outcomes=[]
    variants=('baseline','missing','changed','extra','missing_with_unlisted_copy')
    for variant in variants:
        case=controls/variant;case.mkdir();evidence=case/'input';evidence.mkdir()
        for pin in pins:
            name=pin['file']
            if name==missing_name and variant in ('missing','missing_with_unlisted_copy'):continue
            if name==missing_name and variant=='changed':
                data=(SEAL/name).read_bytes();assert data
                new_file(evidence/name,data[:-1]+(b' ' if data[-1:]!=b' ' else b'\n'))
            else:os.link(SEAL/name,evidence/name)
        os.link(SEAL/INVENTORY,evidence/INVENTORY)
        if variant=='extra':new_file(evidence/'unlisted-control.json',b'{"unlisted":true}\n')
        if variant=='missing_with_unlisted_copy':os.link(SEAL/missing_name,evidence/'unfrozen-source-copy.json')
        output=case/'analysis.json';env=dict(os.environ,PYTHONINTMAXSTRDIGITS='0')
        command=[sys.executable,str(ROOT/PROGRAM),'--evidence-root',str(evidence),'--inventory',INVENTORY,
                 '--inventory-sha256',INVENTORY_SHA,'--output',str(output)]
        result=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True,timeout=3600)
        new_file(case/'stdout.txt',result.stdout.encode());new_file(case/'stderr.txt',result.stderr.encode())
        if variant=='baseline':
            assert result.returncode==0 and output.is_file(),('shadow baseline failed',result.stderr)
            shadow=json.loads(output.read_bytes())
            normalized=json.loads(json.dumps(shadow).replace(str(evidence),str(SEAL)))
            assert normalized==canonical,'shadow and canonical semantic outputs differ after root normalization'
            reason='identical canonical output after replacing only the explicit evidence-root path'
        else:
            expected=('inventoried input bytes differ: '+missing_name) if variant=='changed' else ('unlisted sealed inputs: unlisted-control.json') if variant=='extra' else ('inventoried input is missing: '+missing_name)
            assert result.returncode!=0 and expected in result.stderr,(variant,result.returncode,result.stderr)
            assert not output.exists(),('refused shadow wrote an output',variant)
            reason=expected
        outcomes.append({'variant':variant,'returncode':result.returncode,'output_written':output.exists(),
                         'expected_reason_or_equivalence':reason,'passed':True,'directory':str(case)})
        print('PASS real-data shadow',variant,'returncode',result.returncode,'output',output.exists(),flush=True)
    record={'owner':'MathKacMoody-2','canonical':{'file':str(canonical_path),'sha256':args.canonical_sha256},
        'inventory':{'file':INVENTORY,'sha256':INVENTORY_SHA},'source_seal':str(SEAL),
        'program':{'file':PROGRAM,'sha256':hashlib.sha256((ROOT/PROGRAM).read_bytes()).hexdigest()},
        'outcomes':outcomes,'all_passed':True,'original_files_or_seal_modified':False,'files_deleted':False,
        'method':'Immutable hardlinks for identical data;changed-byte variant creates a NEW standalone file instead of modifying a hardlink. Missing inputs omitted at construction;no fallback to live originals or unlisted copies. Runtime code/libraries outside the data seal are explicit,not asserted sealed.',
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status':'PASS_REAL_DATA_SHADOW_BASELINE_AND4_INTENDED_REFUSALS',
        'limits':'Integrity/control regression only,not new determinant runs,actual-source proof,scientific parent,formal/kernel,native-library or novelty acceptance.'}
    out=ROOT/'frontier-20261029-level7-free19-shadow-verification-v1.json'
    with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('PASS all real-data shadow controls',out.name,flush=True)


if __name__=='__main__':main()
