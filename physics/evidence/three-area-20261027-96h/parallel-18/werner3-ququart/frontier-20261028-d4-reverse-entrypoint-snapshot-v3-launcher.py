#!/usr/bin/env python3
"""Run v2 CRT from exact verified entrypoint bytes, with fresh outputs.

This launcher must itself be compiled from a hash-verified byte snapshot by
the caller, which supplies __launcher_snapshot_sha__. It never modifies any
previous verifier/result. Runtime/hash/OS libraries remain trusted.
"""
import hashlib
import json
import types
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parent
V2=ROOT/'frontier-20261028-d4-reverse-snapshot-crt-v2.py'
PIN_V2='425e5d827f1f4a9592732a124b5f791ebef90148c114084696131c81b9d7f971'
OUT=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-results.json'
PROGRESS=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-progress.json'
RECEIPT=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-launch-receipt.json'


def verified_snapshot(path,expected):
    raw=path.read_bytes();digest=hashlib.sha256(raw).hexdigest()
    if digest!=expected:raise ValueError('entrypoint snapshot SHA mismatch')
    return raw

def main():
    launcher_hash=globals().get('__launcher_snapshot_sha__')
    if not isinstance(launcher_hash,str) or len(launcher_hash)!=64:
        raise ValueError('launcher must be invoked from a verified caller byte snapshot')
    if any(p.exists() for p in (OUT,PROGRESS,RECEIPT)):
        raise ValueError('fresh exclusive output paths required')
    started=datetime.now().astimezone().isoformat(timespec='seconds')
    raw=verified_snapshot(V2,PIN_V2)
    module=types.ModuleType('verified_v2_entrypoint');module.__file__=str(V2)
    exec(compile(raw,str(V2),'exec'),module.__dict__)
    module.OUT=OUT;module.PROGRESS=PROGRESS
    rc=module.main()
    finished=datetime.now().astimezone().isoformat(timespec='seconds')
    if rc!=0:raise ValueError('v2 main returned '+str(rc))
    result_raw=OUT.read_bytes();progress_raw=PROGRESS.read_bytes()
    result=json.loads(result_raw);progress=json.loads(progress_raw)
    if result['verdict']!='PASS' or result['prime_count']!=424 or not result['product_exceeds_twice_fresh_bound']:
        raise ValueError('invalid final source identity receipt')
    if progress['state']!='PRIMES_COMPLETE' or progress['tested_count']!=424 or progress['bad_primes']:
        raise ValueError('invalid final progress receipt')
    after=hashlib.sha256(V2.read_bytes()).hexdigest()
    if after!=PIN_V2:raise ValueError('entrypoint path changed during run')
    r={'kind':'verified_entrypoint_snapshot_v3_launch','launcher_snapshot_sha256':launcher_hash,
       'v2_executed_snapshot_sha256':PIN_V2,'v2_path_postrun_sha256':after,
       'start_wall_time':started,'finish_wall_time':finished,'main_return_code':rc,
       'result_file':OUT.name,'result_sha256':hashlib.sha256(result_raw).hexdigest(),
       'progress_file':PROGRESS.name,'progress_sha256':hashlib.sha256(progress_raw).hexdigest(),
       'prime_count':result['prime_count'],'height_bound_bits':result['height_bound_bits'],
       'prime_product_bits':result['prime_product_bits'],'all_orbits_zero':not result['nonzero_residue_primes'],
       'product_exceeds_twice_bound':result['product_exceeds_twice_fresh_bound'],
       'method':'Caller verifies and compiles the launcher byte snapshot. Launcher verifies and compiles the v2 entrypoint byte snapshot, then the v2 main verifies/compiles all helper snapshots and verifies source/data/receipt bytes.',
       'scope':'Execution-to-source input binding for the exact d4 orbit identity, conditional on Python/hash/NumPy/FLINT/OS and mathematical source/height assumptions; physical theorem and human/family/formal review remain separate.',
       'verdict':'PASS'}
    with RECEIPT.open('x') as f:f.write(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0


if __name__=='__main__':raise SystemExit(main())
