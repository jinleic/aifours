#!/usr/bin/env python3
"""Creation-only v7 CONTROL-HARNESS pack. Production v6 sources and both v6 contracts are UNCHANGED and re-hashed;
only check_m2_ms09_k1_v7.py is new. Exact diff is v6 control -> v7 control. Metadata only; no controls run.
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
        old = pack6['source_files']['src/check_m2_ms09_k1_v6.py']['content']
        new_raw = (L/'src/check_m2_ms09_k1_v7.py').read_bytes(); new = new_raw.decode()
        stamp = time.strftime('%Y%m%dT%H%M%S')
        delta = L/'cycle2'/('full-k1-v7-harness-exact-delta-'+stamp+'.diff')
        with delta.open('x') as f:
            f.write(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='v6/src/check_m2_ms09_k1_v6.py',tofile='v7/src/check_m2_ms09_k1_v7.py')))
        pack = {'schema':'PA19-FULL-K1-HARNESS-PACK-v7','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT REVIEW; harness only; production v6 unchanged; controls NOT_RUN',
            'production_pack':{'path':str(V6.relative_to(L)),'sha256':V6_SHA,'all_source_hashes_reverified':True},
            'production_contracts_unchanged':[{'role':r,'path':p,'sha256':h} for r,p,h in CONTRACTS],
            'v6_review':{'path':'institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v6-source-codex-v1.note.md'},
            'harness_changes':['no process-global threading replacement: pipeline module receives a proxy; only the pipeline stop event and the solver feeder thread are instrumented; main thread identified by get_ident',
                'explicit acknowledgments: solver proof written/closed marker, solver exit permission after pipeline return, publication held until the settlement join begins',
                'removed-settlement-join AST mutant (exactly one change) must lose the veto: UNKNOWN/NOT_EVALUATED',
                'no subprocess timeout: monotonic poll then parameterless wait; bounded waits only detect broken handshakes',
                'exact lifecycle_error and unknown_reason equality with injected RuntimeError repr'],
            'control':{'path':'src/check_m2_ms09_k1_v7.py','sha256':hashlib.sha256(new_raw).hexdigest(),'bytes':len(new_raw),'content':new},
            'delta':{'path':str(delta.relative_to(L)),'sha256':R.digest(delta)},'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('full-k1-v7-harness-pack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(delta,R.digest(delta),flush=True)
        print('control',pack['control']['sha256'],flush=True)


if __name__ == '__main__':
    main()
