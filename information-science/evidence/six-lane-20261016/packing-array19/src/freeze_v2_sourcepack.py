#!/usr/bin/env python3
"""Creation-only requested parent source pack/delta. Pure metadata; one existing lane token, no native child.
The immutable initial v1 source pack is the diff authority. Existing mathematical dependencies are hash-bound,
not misleadingly presented as new files. This pack does not authorize production or claim controls were run.
"""
import argparse
import difflib
import hashlib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract as C
import m2_supervised_runtime_v2 as R

L = C.LANE
OLD = L/'cycle2/full-k1-static-sourcepack-20261018T042044.json'
OLD_SHA = '8825589b46c8c2df711f6b778edf7137fa77a00f086fa7b3b5f583b0fa445bd8'
NEW = ('src/m2_supervised_runtime_v2.py','src/m2_native_staged_v2.py','src/m2_item_owner_v2.py',
       'src/m2_supervised_evidence_v2.py','src/run_m2_ms06_direct_v2.py')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ms09_contract'); ap.add_argument('ms06_contract'); args = ap.parse_args()
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+2*1024**2
        assert R.digest(OLD) == OLD_SHA
        original = json.loads(OLD.read_bytes())
        c = json.loads(Path(args.ms09_contract).read_bytes())
        m6 = json.loads(Path(args.ms06_contract).read_bytes())
        assert c['source_sha256'] == m6['source_sha256']
        sources = {}
        for rel,h in c['source_sha256'].items():
            raw = (L/rel).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == h
            sources[rel] = {'sha256':h,'bytes':len(raw),'content':raw.decode()}
        pieces = []
        for rel,old in original['source_files'].items():
            assert hashlib.sha256(old['content'].encode()).hexdigest() == old['sha256']
            pieces.extend(difflib.unified_diff(old['content'].splitlines(True),sources[rel]['content'].splitlines(True),
                fromfile='v1/'+rel,tofile='v2/'+rel))
        for rel in NEW:
            pieces.extend(difflib.unified_diff([],sources[rel]['content'].splitlines(True),fromfile='/dev/null',tofile='v2/'+rel))
        stamp = time.strftime('%Y%m%dT%H%M%S')
        delta = L/'cycle2'/('full-k1-v2-delta-'+stamp+'.diff')
        with delta.open('x') as f: f.write(''.join(pieces))
        output = {'schema':'PA19-FULL-K1-SOURCEPACK-v2','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT SOURCE REVIEW; NATIVE HOLD; seven-family controls NOT_RUN at this pack',
            'supersedes':{'path':str(OLD.relative_to(L)),'sha256':OLD_SHA},
            'hostile_review':{'path':'institute/runs/six-lane-2026-10-16/review/pa19-full-k1-source-review-v1.md',
                              'sha256':'9a25ac64731b388fdd5614b3bedbd30be1fa1a60cdb33fb804338dce0cc2e2cf'},
            'scope':'same independent B mathematical inputs; transport fixes, tiered resources and strict final census only',
            'delta':{'path':str(delta.relative_to(L)),'sha256':R.digest(delta)},'source_files':sources,
            'external_supervisor':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA,'observed_sha256':R.digest(R.SUP_PATH)},
            'contracts':[{'role':role,'path':str(Path(p).relative_to(L)),'sha256':R.digest(p)} for role,p in
                         [('ms09-full-cover-and14-validation',args.ms09_contract),('ms06-initial-direct-only',args.ms06_contract)]],
            'readme_amendment_sha256':R.digest(L/'README.md'),
            'controls':{'source':'src/check_m2_ms09_k1.py','sha256':sources['src/check_m2_ms09_k1.py']['sha256'],
                        'required_families':7,'observed_receipt':None,'production_coverage':False},
            'calibration_reuse':'WITHDRAWN:14 new measured-validation tasks; old count=false files unchanged',
            'resource_thresholds_are_sampled_not_instantaneous':True,
            'no_production_from_this_program':True,'pack_generator_sha256':R.digest(__file__)}
        assert output['external_supervisor']['observed_sha256'] == R.SUP_SHA
        dest = L/'cycle2'/('full-k1-v2-sourcepack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(output,f,indent=1)
        print(dest,R.digest(dest),flush=True)
        print(delta,R.digest(delta),flush=True)
        print(json.dumps(output['contracts'],indent=1),flush=True)


if __name__ == '__main__':
    main()
