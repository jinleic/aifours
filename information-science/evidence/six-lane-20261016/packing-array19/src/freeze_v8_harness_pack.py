#!/usr/bin/env python3
"""Creation-only v8 CONTROL-HARNESS pack. Production v6 sources and both v6 contracts are UNCHANGED and re-hashed;
only check_m2_ms09_k1_v8.py is new. Exact diff is reviewed v7 harness -> v8 harness. Metadata only; no controls run.
"""
import difflib
import hashlib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract_v6 as C
import m2_supervised_runtime_v6 as R

L = C.LANE
V6 = L/'cycle2/full-k1-v6-sourcepack-20261018T075617.json'
V6_SHA = 'cb9d45ab26a7b39ee960d70f4b28ffe4483d6add3bb6900d6fcc27cdc6a74bc3'
V7_HARNESS = L/'src/check_m2_ms09_k1_v7.py'
V7_HARNESS_SHA = '94edd6496d66e70c2b983f5b6fd84eb8c9250c4ef924fa7727fed3ca4ef32768'
CONTRACTS = (('ms09-full-cover-and14-validation','cycle2/m2-ms09-k1-v6-contract-20261018T075542.json','072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8'),
             ('ms06-initial-direct-only','cycle2/m2-ms06-initial-v6-contract-20261018T075542.json','dc343809b7597804dde1c71802edd142fe87472d5e20f6220c21e7f234fc2413'))


def main():
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+2*1024**2, 'fresh metadata growth gate'
        assert R.digest(V6) == V6_SHA
        pack6 = json.loads(V6.read_bytes())
        for rel,item in pack6['source_files'].items():
            assert R.digest(L/rel) == item['sha256'], ('production v6 source changed',rel)
        for role,rel,h in CONTRACTS: assert R.digest(L/rel) == h, ('v6 contract changed',role)
        old = V7_HARNESS.read_text(); assert R.digest(V7_HARNESS) == V7_HARNESS_SHA
        new_raw = (L/'src/check_m2_ms09_k1_v8.py').read_bytes(); new = new_raw.decode()
        stamp = time.strftime('%Y%m%dT%H%M%S')
        delta = L/'cycle2'/('full-k1-v8-harness-exact-delta-'+stamp+'.diff')
        with delta.open('x') as f:
            f.write(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='v7/src/check_m2_ms09_k1_v7.py',tofile='v8/src/check_m2_ms09_k1_v8.py')))
        pack = {'schema':'PA19-FULL-K1-HARNESS-PACK-v8','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT REVIEW; harness only; production v6 unchanged; controls NOT_RUN',
            'production_pack':{'path':str(V6.relative_to(L)),'sha256':V6_SHA,'all_source_hashes_reverified':True},
            'production_contracts_unchanged':[{'role':r,'path':p,'sha256':h} for r,p,h in CONTRACTS],
            'v7_review':{'path':'institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v7-harness-codex-v1.note.md'},
            'v7_observed_failure':{'path':'cycle2/v7-required-controls-1792336621509922000/failure-receipt.json','sha256':'47c6e88af0bd7488f30e440ea48c87b5de254112ce9e6edd30e8593b24eca079'},
            'harness_changes':['fixture FIFO role classification uses exact basenames (checker-cnf.fifo / solver-cnf.fifo); v7 used substring tests and the case folder name checker-prefix misrouted the truncated feed to the solver; no assertion or production change'],
            'control':{'path':'src/check_m2_ms09_k1_v8.py','sha256':hashlib.sha256(new_raw).hexdigest(),'bytes':len(new_raw),'content':new},
            'delta':{'path':str(delta.relative_to(L)),'sha256':R.digest(delta)},'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('full-k1-v8-harness-pack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(delta,R.digest(delta),flush=True)
        print('control',pack['control']['sha256'],flush=True)


if __name__ == '__main__':
    main()
